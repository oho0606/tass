import type { NextConfig } from "next";

const backendUrl =
  process.env.BACKEND_URL ||
  process.env.NEXT_PUBLIC_API_URL ||
  "http://localhost:8000";

const nextConfig: NextConfig = {
  output: "standalone",

  // Proxy all /api/* and direct backend routes through Next.js server.
  // This avoids CORS issues when deploying frontend on Vercel and backend on Render.
  // Set BACKEND_URL (server-only) in Vercel environment variables.
  async rewrites() {
    return [
      { source: "/health", destination: `${backendUrl}/health` },
      { source: "/picks/:path*", destination: `${backendUrl}/picks/:path*` },
      { source: "/api/:path*", destination: `${backendUrl}/api/:path*` },
      { source: "/ranking/:path*", destination: `${backendUrl}/ranking/:path*` },
      { source: "/stock/:path*", destination: `${backendUrl}/stock/:path*` },
      { source: "/market/:path*", destination: `${backendUrl}/market/:path*` },
      { source: "/backtest/:path*", destination: `${backendUrl}/backtest/:path*` },
    ];
  },
};

export default nextConfig;
