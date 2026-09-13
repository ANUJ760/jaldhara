export function MapLegend() {
  return (
    <div className="bg-slate-900/80 backdrop-blur p-3 rounded border border-slate-700 text-xs text-slate-300">
      <div className="font-semibold mb-2">Water Depth (m)</div>
      <div className="flex flex-col gap-1">
        <div className="flex items-center gap-2"><div className="w-4 h-4 rounded bg-[#1d4ed8]" /><span>> 5.0m</span></div>
        <div className="flex items-center gap-2"><div className="w-4 h-4 rounded bg-[#0284c7]" /><span>2.0 - 5.0m</span></div>
        <div className="flex items-center gap-2"><div className="w-4 h-4 rounded bg-[#0f766e]" /><span>0.0 - 2.0m</span></div>
      </div>
    </div>
  );
}