export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen text-foreground">
      <div className="mx-auto min-h-screen w-full max-w-2xl px-4 py-5 sm:max-w-3xl sm:px-6 sm:py-8">
        {children}
      </div>
    </div>
  );
}
