/**
 * Catch-all proxy route: /api/proxy/... → Render backend
 * Reads BACKEND_URL at request time (runtime), not build time.
 */
import { type NextRequest, NextResponse } from "next/server";

const BACKEND = (
  process.env.BACKEND_URL ||
  process.env.NEXT_PUBLIC_API_URL ||
  "http://localhost:8000"
).replace(/\/$/, "");

async function handler(
  req: NextRequest,
  { params }: { params: Promise<{ path: string[] }> }
) {
  const { path } = await params;
  const targetPath = "/" + path.join("/");
  const search = req.nextUrl.search;
  const url = `${BACKEND}${targetPath}${search}`;

  const headers = new Headers();
  req.headers.forEach((v, k) => {
    if (!["host", "connection"].includes(k.toLowerCase())) headers.set(k, v);
  });

  try {
    const hasBody = !["GET", "HEAD"].includes(req.method);
    const body = hasBody ? await req.text() : undefined;

    const res = await fetch(url, {
      method: req.method,
      headers,
      body,
    });

    const resHeaders = new Headers();
    res.headers.forEach((v, k) => resHeaders.set(k, v));
    resHeaders.delete("content-encoding");

    return new NextResponse(res.body, {
      status: res.status,
      headers: resHeaders,
    });
  } catch (err) {
    return NextResponse.json(
      { error: "Proxy error", detail: String(err) },
      { status: 502 }
    );
  }
}

export const GET = handler;
export const POST = handler;
export const PUT = handler;
export const PATCH = handler;
export const DELETE = handler;
