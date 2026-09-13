'use client';
import { mockVillages } from '@/lib/mock-data';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';

export default function ImpactPage() {
  return (
    <div className="h-full flex flex-col gap-6">
      <h1 className="text-3xl font-bold text-white">Impact Analysis</h1>
      
      <div className="grid grid-cols-3 gap-4">
        <Card><h3 className="text-slate-400">Total Population Risk</h3><p className="text-2xl">342,000</p></Card>
        <Card><h3 className="text-slate-400">High Priority Villages</h3><p className="text-2xl text-red-400">8</p></Card>
        <Card><h3 className="text-slate-400">Avg Evacuation Time</h3><p className="text-2xl">4.2 hrs</p></Card>
      </div>
      
      <Card className="flex-1 overflow-auto">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="border-b border-slate-700 text-slate-400">
              <th className="p-4 font-medium">Village Name</th>
              <th className="p-4 font-medium">Distance (km)</th>
              <th className="p-4 font-medium">ETA</th>
              <th className="p-4 font-medium">Max Depth (m)</th>
              <th className="p-4 font-medium">Population</th>
              <th className="p-4 font-medium">Priority</th>
            </tr>
          </thead>
          <tbody>
            {mockVillages.map((v, i) => (
              <tr key={i} className="border-b border-slate-700/50 hover:bg-slate-700/20">
                <td className="p-4 font-medium">{v.name}</td>
                <td className="p-4 text-slate-300">{v.distance}</td>
                <td className="p-4 text-slate-300">{v.eta}</td>
                <td className="p-4 font-mono">{v.maxDepth}</td>
                <td className="p-4">{v.population.toLocaleString()}</td>
                <td className="p-4">
                  <Badge className={v.evacuationPriority === 'High' ? 'bg-red-500/20 text-red-400' : 'bg-yellow-500/20 text-yellow-400'}>
                    {v.evacuationPriority}
                  </Badge>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}