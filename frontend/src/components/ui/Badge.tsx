export function Badge({ children, className = '' }: { children: React.ReactNode, className?: string }) {
  return <span className={`px-2 py-1 text-xs font-semibold rounded-full bg-slate-700 text-slate-300 ${className}`}>{children}</span>;
}