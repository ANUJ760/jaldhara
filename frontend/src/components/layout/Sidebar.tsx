import Link from 'next/link';

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-800 h-screen p-4 flex flex-col gap-4 text-sm fixed">
      <div className="font-bold text-xl text-brand-light mb-6">Jaldhara</div>
      <Link href="/" className="hover:text-brand-light">Home</Link>
      <Link href="/dashboard" className="hover:text-brand-light">Dashboard</Link>
      <Link href="/aoi" className="hover:text-brand-light">AOI Management</Link>
      <Link href="/breach" className="hover:text-brand-light">Breach Setup</Link>
      <Link href="/simulations" className="hover:text-brand-light">Simulations</Link>
      <Link href="/impact" className="hover:text-brand-light">Impact Analysis</Link>
      <Link href="/export" className="hover:text-brand-light">Export</Link>
      <Link href="/monitoring" className="hover:text-brand-light">Monitoring</Link>
    </aside>
  );
}
