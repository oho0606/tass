import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",

  // Rewrite backend API paths to the catch-all proxy route handler at
  // /api/proxy/[...path]. The proxy reads BACKEND_URL at request time
  // (runtime), so no build-time env var is needed here.
  async rewrites() {
    return [
      { source: "/health", destination: "/api/proxy/health" },
      { source: "/picks/:path*", destination: "/api/proxy/picks/:path*" },
      { source: "/ranking/:path*", destination: "/api/proxy/ranking/:path*" },
      { source: "/stock/:path*", destination: "/api/proxy/stock/:path*" },
      { source: "/market/:path*", destination: "/api/proxy/market/:path*" },
      { source: "/backtest/:path*", destination: "/api/proxy/backtest/:path*" },
    ];
  },
};

export default nextConfig;
