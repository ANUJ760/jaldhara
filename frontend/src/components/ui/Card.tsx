export function Card({ children, className = '' }: { children: React.ReactNode, className?: string }) {
  return <div className={`bg-slate-800 rounded-lg shadow border border-slate-700 p-4 ${className}`}>{children}</div>;
}