export default function Home() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Jaldhara Overview</h1>
      <div className="grid grid-cols-3 gap-4">
        <div className="p-4 bg-slate-800 rounded">Total Simulations: 12</div>
        <div className="p-4 bg-slate-800 rounded">Active Alerts: 2</div>
        <div className="p-4 bg-slate-800 rounded">System Health: OK</div>
      </div>
    </div>
  );
}
