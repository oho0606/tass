import { NextRequest, NextResponse } from "next/server";
import { getAdminDb } from "@/lib/firebase/admin";

async function verifyIdTokenViaRest(idToken: string): Promise<string | null> {
  const apiKey = process.env.NEXT_PUBLIC_FIREBASE_API_KEY;
  if (!apiKey) return null;

  const res = await fetch(
    `https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=${apiKey}`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idToken }),
    },
  );

  if (!res.ok) return null;

  const data = (await res.json()) as { users?: Array<{ localId: string }> };
  return data.users?.[0]?.localId ?? null;
}

/**
 * POST /api/auth/verify
 * Firebase ID token을 검증하고 Firestore 승인 상태를 확인한다.
 */
export async function POST(req: NextRequest) {
  let body: { idToken?: string };
  try {
    body = (await req.json()) as { idToken?: string };
  } catch {
    return NextResponse.json({ message: "잘못된 요청입니다." }, { status: 400 });
  }

  const { idToken } = body;
  if (!idToken) {
    return NextResponse.json({ message: "인증 토큰이 없습니다." }, { status: 401 });
  }

  const uid = await verifyIdTokenViaRest(idToken);
  if (!uid) {
    return NextResponse.json({ message: "유효하지 않은 토큰입니다." }, { status: 401 });
  }

  const snap = await getAdminDb().collection("users").doc(uid).get();
  if (!snap.exists) {
    return NextResponse.json(
      { message: "가입 정보를 찾을 수 없습니다. 회원가입을 먼저 진행해 주세요." },
      { status: 403 },
    );
  }

  const data = snap.data()!;
  if (data.status === "pending") {
    return NextResponse.json({ message: "승인 대기" }, { status: 403 });
  }
  if (data.status === "rejected") {
    return NextResponse.json(
      { message: "가입이 거절된 계정입니다. 운영자에게 문의해 주세요." },
      { status: 403 },
    );
  }
  if (data.status !== "approved") {
    return NextResponse.json({ message: "접근이 거부되었습니다." }, { status: 403 });
  }

  return NextResponse.json({ ok: true });
}
