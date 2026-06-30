import { test, expect } from "@playwright/test";

test.describe("TASS v1 Main Screen", () => {
  test("main screen loads with analyze button", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByRole("heading", { name: "TASS" })).toBeVisible();
    await expect(page.getByRole("button", { name: /분석 시작/ })).toBeVisible();
    await expect(page.getByText("종가 분석")).toBeVisible();
    await expect(page.getByText("백엔드 Rule Engine")).toBeVisible();
  });

  test("removed routes redirect or 404", async ({ page }) => {
    const picks = await page.goto("/picks");
    if (picks) {
      expect(picks.status()).toBe(404);
    } else {
      await expect(page.getByText(/not found|404/i)).toBeVisible();
    }

    const backtest = await page.goto("/backtest");
    if (backtest) {
      expect(backtest.status()).toBe(404);
    } else {
      await expect(page.getByText(/not found|404/i)).toBeVisible();
    }
  });

  test("analysis mode controls are visible", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByRole("button", { name: "종가 분석" })).toBeVisible();
    await expect(page.getByRole("button", { name: "시가 분석" })).toBeVisible();
    await expect(page.getByRole("button", { name: "장중 분석" })).toBeVisible();
  });
});
