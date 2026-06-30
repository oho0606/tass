import { StockDetailClient } from "@/components/stock/stock-detail-client";

export default async function StockDetailPage({
  params,
}: {
  params: Promise<{ code: string }>;
}) {
  const { code } = await params;
  return <StockDetailClient code={code} />;
}
