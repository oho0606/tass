from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any
from urllib import error, parse, request

logger = logging.getLogger("KISClient")

_TOKEN_PATH = "/oauth2/tokenP"
_DAILY_CHART_PATH = "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice"
_DAILY_CHART_TR_ID = "FHKST03010100"
_MAX_ROWS_PER_REQUEST = 100


@dataclass(frozen=True)
class KISConfig:
    app_key: str
    app_secret: str
    base_url: str = "https://openapi.koreainvestment.com:9443"

    @property
    def is_configured(self) -> bool:
        return bool(self.app_key and self.app_secret)


class KISClient:
    """Minimal KIS Open API HTTP client (token + daily OHLCV)."""

    def __init__(self, config: KISConfig) -> None:
        self.config = config
        self._access_token: str | None = None
        self._token_expires_at: float = 0.0

    def get_daily_ohlcv(self, symbol: str, start_date: date, end_date: date) -> list[dict[str, Any]]:
        code = symbol.strip().split(".")[0].zfill(6)
        rows: list[dict[str, Any]] = []
        chunk_end = end_date

        while chunk_end >= start_date:
            payload = self._request_daily_chart(code, start_date, chunk_end)
            if not payload:
                break

            rows.extend(payload)
            if len(payload) < _MAX_ROWS_PER_REQUEST:
                break

            oldest = min(int(item["stck_bsop_date"]) for item in payload)
            oldest_date = date(oldest // 10000, (oldest % 10000) // 100, oldest % 100)
            if oldest_date <= start_date:
                break
            chunk_end = oldest_date - timedelta(days=1)

        return rows

    def _request_daily_chart(
        self,
        code: str,
        start_date: date,
        end_date: date,
    ) -> list[dict[str, Any]]:
        query = parse.urlencode(
            {
                "FID_COND_MRKT_DIV_CODE": "J",
                "FID_INPUT_ISCD": code,
                "FID_INPUT_DATE_1": start_date.strftime("%Y%m%d"),
                "FID_INPUT_DATE_2": end_date.strftime("%Y%m%d"),
                "FID_PERIOD_DIV_CODE": "D",
                "FID_ORG_ADJ_PRC": "0",
            }
        )
        url = f"{self.config.base_url.rstrip('/')}{_DAILY_CHART_PATH}?{query}"
        headers = self._auth_headers(_DAILY_CHART_TR_ID)
        body = self._http_get(url, headers)
        if body.get("rt_cd") not in (None, "0"):
            message = body.get("msg1", "KIS API error")
            raise RuntimeError(message)

        output = body.get("output2") or []
        if isinstance(output, dict):
            return [output]
        return list(output)

    def _auth_headers(self, tr_id: str) -> dict[str, str]:
        token = self._ensure_token()
        return {
            "Content-Type": "application/json",
            "authorization": f"Bearer {token}",
            "appkey": self.config.app_key,
            "appsecret": self.config.app_secret,
            "tr_id": tr_id,
            "custtype": "P",
        }

    def _ensure_token(self) -> str:
        if self._access_token and time.time() < self._token_expires_at:
            return self._access_token

        url = f"{self.config.base_url.rstrip('/')}{_TOKEN_PATH}"
        payload = json.dumps(
            {
                "grant_type": "client_credentials",
                "appkey": self.config.app_key,
                "appsecret": self.config.app_secret,
            }
        ).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        body = self._http_post(url, headers, payload)

        token = body.get("access_token")
        if not token:
            raise RuntimeError("KIS token response missing access_token")

        expires_in = int(body.get("expires_in", 86_400))
        self._access_token = token
        self._token_expires_at = time.time() + max(expires_in - 60, 60)
        return token

    def _http_get(self, url: str, headers: dict[str, str]) -> dict[str, Any]:
        req = request.Request(url, headers=headers, method="GET")
        return self._read_json(req)

    def _http_post(self, url: str, headers: dict[str, str], payload: bytes) -> dict[str, Any]:
        req = request.Request(url, data=payload, headers=headers, method="POST")
        return self._read_json(req)

    def _read_json(self, req: request.Request) -> dict[str, Any]:
        try:
            with request.urlopen(req, timeout=15) as response:
                raw = response.read().decode("utf-8")
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"KIS HTTP {exc.code}: {detail}") from exc
        except error.URLError as exc:
            raise ConnectionError(str(exc)) from exc

        data = json.loads(raw)
        if not isinstance(data, dict):
            raise RuntimeError("KIS response is not a JSON object")
        return data
