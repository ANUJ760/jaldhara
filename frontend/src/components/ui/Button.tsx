export function Button({ children, className = '', ...props }: React.ButtonHTMLAttributes<HTMLButtonElement>) {
  return <button className={`px-4 py-2 bg-brand-blue hover:bg-blue-700 text-white rounded transition-colors ${className}`} {...props}>{children}</button>;
}