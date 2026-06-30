"""Export OpenAPI schema for frontend type generation."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    try:
        from api.app import app
    except ImportError:
        print("Install API deps: pip install -e '.[api]'", file=sys.stderr)
        return 1

    if app is None:
        print("FastAPI app not available", file=sys.stderr)
        return 1

    schema = app.openapi()
    out = Path("frontend/openapi.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
