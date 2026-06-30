# TASS Backend API (TASS-040)
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml requirements.txt ./
COPY engine ./engine
COPY api ./api
COPY config ./config
COPY alembic ./alembic
COPY alembic.ini ./
COPY main.py ./

RUN mkdir -p data/cache output logs backtest/reports

RUN pip install --no-cache-dir -e ".[api,data]"

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=5s --start-period=40s --retries=5 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')" || exit 1

# Run DB migrations then start the API server
# Render injects $PORT at runtime; fall back to 8000 for local Docker usage
CMD ["sh", "-c", "alembic upgrade head && uvicorn api.app:app --host 0.0.0.0 --port ${PORT:-8000}"]
