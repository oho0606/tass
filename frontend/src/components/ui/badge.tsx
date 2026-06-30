import { cn } from "@/lib/utils";

const variants = {
  default: "bg-border/80 text-foreground",
  positive: "bg-success/20 text-success border border-success/40 font-semibold",
  negative: "bg-danger/20 text-danger border border-danger/40 font-semibold",
  warning: "bg-warning/20 text-warning border border-warning/40 font-semibold",
  primary: "bg-primary/20 text-primary border border-primary/40",
};

export function Badge({
  className,
  variant = "default",
  ...props
}: React.HTMLAttributes<HTMLSpanElement> & { variant?: keyof typeof variants }) {
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-md px-2.5 py-0.5 text-xs",
        variants[variant],
        className,
      )}
      {...props}
    />
  );
}
