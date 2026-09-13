export function Alert({ type = 'info', children }: { type?: 'info' | 'warning' | 'error', children: React.ReactNode }) {
  const colors = {
    info: 'bg-blue-900/30 border-blue-800 text-blue-300',
    warning: 'bg-yellow-900/30 border-yellow-800 text-yellow-300',
    error: 'bg-red-900/30 border-red-800 text-red-300'
  };
  return <div className={`p-4 rounded border ${colors[type]}`}>{children}</div>;
}