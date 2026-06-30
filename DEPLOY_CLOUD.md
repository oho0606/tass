# TASS 무료 클라우드 배포 가이드

```
Frontend  → Vercel    (Next.js — 무료, 무제한)
Backend   → Render    (FastAPI Python — 무료, 512MB)
Database  → Supabase  (PostgreSQL — 무료, 500MB)
Cache     → Upstash   (Redis — 무료, 1만 req/day)
```

총 비용: **$0/월**

---

## 사전 준비

- GitHub 계정 (코드를 GitHub에 푸시해야 Vercel/Render가 배포)
- 아래 서비스 무료 계정 생성
  - [Vercel](https://vercel.com)
  - [Render](https://render.com)
  - [Supabase](https://supabase.com)
  - [Upstash](https://upstash.com) (선택 — 없어도 파일 캐시로 동작)

---

## Step 1. GitHub에 코드 올리기

```powershell
# GitHub에서 새 레포 생성 후
git remote add origin https://github.com/YOUR_NAME/tass.git
git push -u origin master
```

---

## Step 2. Supabase — PostgreSQL 생성

1. [supabase.com](https://supabase.com) → New Project
2. Project 이름: `tass`, 비밀번호 메모
3. `Settings` → `Database` → `Connection string` → **URI** 복사
   - 형식: `postgresql://postgres:[password]@db.[ref].supabase.co:5432/postgres`

---

## Step 3. Upstash — Redis 생성 (선택)

1. [upstash.com](https://upstash.com) → Create Database
2. 이름: `tass`, Region: `ap-northeast-1` (도쿄)
3. `.env` 탭 → `REDIS_URL` 값 복사
   - 형식: `rediss://:[password]@[host].upstash.io:6379`

---

## Step 4. Render — 백엔드 배포

### 방법 A: render.yaml Blueprint (권장)

1. [render.com](https://render.com) → New → Blueprint
2. GitHub 레포 연결
3. `render.yaml` 자동 감지 → Apply
4. 환경변수 입력 (Dashboard → tass-backend → Environment):

| Key | 값 |
|-----|-----|
| `DATABASE_URL` | Step 2에서 복사한 Supabase URI |
| `REDIS_URL` | Step 3에서 복사한 Upstash URI (선택) |
| `CORS_ORIGINS` | 나중에 Vercel URL 확정 후 입력 |

5. Manual Deploy → Deploy Latest Commit
6. 로그에서 `Application startup complete` 확인
7. 서비스 URL 메모: `https://tass-backend.onrender.com`

### 방법 B: 수동 설정

1. Render → New → Web Service → GitHub 레포 선택
2. Runtime: **Python 3**
3. Build Command: `pip install -e ".[api,data]"`
4. Start Command: `alembic upgrade head && uvicorn api.app:app --host 0.0.0.0 --port $PORT`
5. Plan: **Free**
6. 환경변수 위와 동일하게 입력

---

## Step 5. Vercel — 프론트엔드 배포

1. [vercel.com](https://vercel.com) → New Project → GitHub 레포 선택
2. Root Directory: `frontend`
3. Framework: **Next.js** (자동 감지)
4. Environment Variables 추가:

| Key | 값 |
|-----|-----|
| `NEXT_PUBLIC_API_URL` | *(빈 값)* — 리라이트 프록시 사용 |
| `BACKEND_URL` | `https://tass-backend.onrender.com` |

5. Deploy
6. 배포된 URL 확인: `https://tass-xxxx.vercel.app`

---

## Step 6. CORS 설정 완료

Render 백엔드 대시보드 → tass-backend → Environment:

```
CORS_ORIGINS=https://tass-xxxx.vercel.app
```

Save → 자동 재배포

---

## Step 7. 동작 확인

```
https://tass-xxxx.vercel.app          ← 프론트엔드 (Today's Picks)
https://tass-backend.onrender.com/health    ← 백엔드 헬스체크
https://tass-backend.onrender.com/docs      ← API 문서
https://tass-backend.onrender.com/picks/today  ← Today's Picks API
```

---

## 알아둘 점

| 항목 | 무료 티어 제한 |
|------|---------------|
| Render | 15분 비활성 시 슬립 → 첫 요청 30~60초 지연 |
| Supabase | 7일 비활성 시 일시 정지 (매주 한 번 접속하면 유지) |
| Upstash | 1만 커맨드/일 초과 시 추가 불가 (무료) |
| Vercel | 월 100GB 대역폭, 함수 100시간 |

### Render 슬립 방지 (선택)

`cron-job.org` 무료 서비스로 14분마다 `/health` ping:

```
URL: https://tass-backend.onrender.com/health
Interval: 14 minutes
```

---

## 커스텀 도메인 연결 (선택)

- **Vercel**: Project → Settings → Domains → 도메인 추가
- **Render**: Service → Settings → Custom Domain → 도메인 추가
- Render 커스텀 도메인 추가 시 `CORS_ORIGINS`도 업데이트 필요

---

## 재배포 방법

```powershell
git add -A
git commit -m "update: ..."
git push origin master
# Vercel과 Render 모두 자동으로 감지하여 재배포
```
