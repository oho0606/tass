# TASS stack startup (Windows)
# Usage after reboot (Docker):  .\scripts\start_stack.ps1 -Docker
# Usage without Docker:        .\scripts\start_stack.ps1

param(
    [switch]$Docker
)

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

python scripts/run_daily_picks.py --universe config/universe_sample.csv | Out-Null

if ($Docker) {
    $docker = "C:\Program Files\Docker\Docker\resources\bin\docker.exe"
    if (-not (Test-Path $docker)) {
        Write-Error "Docker not found. Install Docker Desktop first."
        exit 1
    }
    & $docker compose up --build -d
    Write-Host "Stack starting via Docker Compose..."
    Write-Host "  Backend:  http://localhost:8000/health"
    Write-Host "  Frontend: http://localhost:3000"
    exit 0
}

Write-Host "Starting local stack (no Docker)..."
Start-Process python -ArgumentList "-m", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000" -WorkingDirectory $Root
Start-Process npm -ArgumentList "run", "dev", "--", "--port", "3000" -WorkingDirectory (Join-Path $Root "frontend")
Write-Host "  Backend:  http://localhost:8000/health"
Write-Host "  Frontend: http://localhost:3000"
