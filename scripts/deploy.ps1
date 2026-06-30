# =============================================================================
# TASS v1.0.0 — 원클릭 배포 스크립트 (Windows / Docker Desktop)
# 사용법:
#   .\scripts\deploy.ps1           # 빌드 + 기동
#   .\scripts\deploy.ps1 -Down     # 스택 종료
#   .\scripts\deploy.ps1 -Rebuild  # 이미지 강제 재빌드 후 기동
#   .\scripts\deploy.ps1 -Logs     # 실시간 로그 보기
# =============================================================================
param(
    [switch]$Down,
    [switch]$Rebuild,
    [switch]$Logs,
    [switch]$NoData
)

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

function Write-Step($msg) { Write-Host "`n==> $msg" -ForegroundColor Cyan }
function Write-OK($msg)   { Write-Host "    [OK] $msg" -ForegroundColor Green }
function Write-Fail($msg) { Write-Host "    [FAIL] $msg" -ForegroundColor Red; exit 1 }

# ── 0. 종료 ──────────────────────────────────────────────────────────────────
if ($Down) {
    Write-Step "스택 종료"
    docker compose down -v
    Write-OK "종료 완료"
    exit 0
}

# ── 1. 로그 스트리밍 ──────────────────────────────────────────────────────────
if ($Logs) {
    docker compose logs -f
    exit 0
}

# ── 2. 필수 도구 체크 ────────────────────────────────────────────────────────
Write-Step "사전 요구사항 확인"
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Fail "Docker가 설치되어 있지 않습니다. https://www.docker.com/products/docker-desktop 에서 설치하세요."
}
$dockerInfo = docker info 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Fail "Docker Desktop이 실행 중이지 않습니다. Docker Desktop을 먼저 시작하세요."
}
Write-OK "Docker Desktop 실행 중"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Fail "Python이 설치되어 있지 않습니다."
}
Write-OK "Python 확인"

# ── 3. .env 확인 ─────────────────────────────────────────────────────────────
Write-Step ".env 파일 확인"
if (-not (Test-Path ".env")) {
    Write-Host "    .env 파일이 없습니다. .env.example을 복사하여 생성합니다." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
}
Write-OK ".env 준비"

# ── 4. 초기 picks 데이터 생성 ────────────────────────────────────────────────
if (-not $NoData) {
    Write-Step "오늘의 종목 추천 데이터 생성 (picks 사전 캐시)"
    python scripts/run_daily_picks.py --universe config/universe_sample.csv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "    경고: picks 생성 실패 — API 기동 후 /picks/today 첫 접속 시 자동 생성됩니다." -ForegroundColor Yellow
    } else {
        Write-OK "picks 데이터 생성 완료"
    }
}

# ── 5. Docker 이미지 빌드 ────────────────────────────────────────────────────
Write-Step "Docker 이미지 빌드"
if ($Rebuild) {
    docker compose build --no-cache
} else {
    docker compose build
}
if ($LASTEXITCODE -ne 0) { Write-Fail "Docker 빌드 실패" }
Write-OK "이미지 빌드 완료"

# ── 6. 스택 기동 ─────────────────────────────────────────────────────────────
Write-Step "스택 기동 (postgres → redis → backend → frontend)"
docker compose up -d
if ($LASTEXITCODE -ne 0) { Write-Fail "스택 기동 실패" }

# ── 7. 백엔드 헬스체크 대기 ──────────────────────────────────────────────────
Write-Step "백엔드 준비 대기 (최대 120초)"
$max = 40
$ok = $false
for ($i = 1; $i -le $max; $i++) {
    Start-Sleep -Seconds 3
    try {
        $resp = Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing -TimeoutSec 3 -ErrorAction SilentlyContinue
        if ($resp.StatusCode -eq 200) { $ok = $true; break }
    } catch {}
    Write-Host "    ... 대기 중 ($($i * 3)초)" -ForegroundColor DarkGray
}
if (-not $ok) { Write-Fail "백엔드가 120초 내에 기동되지 않았습니다. 'docker compose logs backend'로 확인하세요." }
Write-OK "백엔드 정상 (http://localhost:8000/health)"

# ── 8. 프론트엔드 헬스체크 대기 ──────────────────────────────────────────────
Write-Step "프론트엔드 준비 대기 (최대 120초)"
$ok = $false
for ($i = 1; $i -le $max; $i++) {
    Start-Sleep -Seconds 3
    try {
        $resp = Invoke-WebRequest -Uri "http://localhost:3000" -UseBasicParsing -TimeoutSec 3 -ErrorAction SilentlyContinue
        if ($resp.StatusCode -eq 200) { $ok = $true; break }
    } catch {}
    Write-Host "    ... 대기 중 ($($i * 3)초)" -ForegroundColor DarkGray
}
if (-not $ok) { Write-Fail "프론트엔드가 120초 내에 기동되지 않았습니다. 'docker compose logs frontend'로 확인하세요." }
Write-OK "프론트엔드 정상 (http://localhost:3000)"

# ── 9. 스모크 테스트 ─────────────────────────────────────────────────────────
Write-Step "스모크 테스트"
try {
    $health = Invoke-RestMethod -Uri "http://localhost:8000/health" -TimeoutSec 5
    Write-OK "헬스: status=$($health.status) engine=$($health.engine_version) mvp_mode=$($health.mvp_mode)"
} catch {
    Write-Host "    경고: /health 응답 파싱 실패" -ForegroundColor Yellow
}
try {
    $picks = Invoke-RestMethod -Uri "http://localhost:8000/picks/today" -TimeoutSec 30
    Write-OK "Today's Picks: $($picks.picks.Count)개 종목 ($($picks.date))"
} catch {
    Write-Host "    경고: /picks/today 응답 실패 — 첫 번째 요청은 엔진 실행으로 시간이 걸릴 수 있습니다." -ForegroundColor Yellow
}

# ── 10. 완료 ─────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  TASS v1.0.0 배포 완료!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  Frontend  : http://localhost:3000" -ForegroundColor White
Write-Host "  API       : http://localhost:8000" -ForegroundColor White
Write-Host "  API Docs  : http://localhost:8000/docs" -ForegroundColor White
Write-Host "  Health    : http://localhost:8000/health" -ForegroundColor White
Write-Host "  Picks     : http://localhost:8000/picks/today" -ForegroundColor White
Write-Host ""
Write-Host "  로그 보기 : .\scripts\deploy.ps1 -Logs" -ForegroundColor DarkGray
Write-Host "  종료하기  : .\scripts\deploy.ps1 -Down" -ForegroundColor DarkGray
Write-Host "============================================================" -ForegroundColor Green
