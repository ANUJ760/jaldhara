export function Select({ children, className = '', ...props }: React.SelectHTMLAttributes<HTMLSelectElement>) {
  return <select className={`w-full p-2 bg-slate-900 border border-slate-700 rounded text-slate-200 focus:outline-none focus:border-brand-blue ${className}`} {...props}>{children}</select>;
}