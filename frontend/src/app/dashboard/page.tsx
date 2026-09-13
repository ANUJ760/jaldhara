'use client';
import FloodMap from '@/components/map/FloodMap';
import TimeSlider from '@/components/map/TimeSlider';
import { Card } from '@/components/ui/Card';

export default function DashboardPage() {
  return (
    <div className="h-[calc(100vh-6rem)] flex flex-col gap-4">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold text-white">Live Dashboard - Kosi Barrage</h1>
        <div className="flex gap-2">
          <select className="bg-slate-800 p-2 rounded text-sm"><option>SPH Model</option><option>Delft3D</option></select>
        </div>
      </div>
      
      <div className="flex flex-1 gap-4 overflow-hidden">
        <div className="flex-[3] relative flex flex-col rounded-xl overflow-hidden border border-slate-700">
          <div className="flex-1 relative">
            <FloodMap />
          </div>
          <div className="absolute bottom-6 left-6 right-6">
            <TimeSlider />
          </div>
        </div>
        
        <div className="flex-1 flex flex-col gap-4 overflow-y-auto pr-2">
          <Card>
            <h3 className="font-semibold mb-2 text-brand-light">Simulation Status</h3>
            <div className="text-3xl font-bold text-green-400 mb-1">Running</div>
            <p className="text-sm text-slate-400">Current elapsed time: 14h 30m</p>
          </Card>
          
          <Card>
            <h3 className="font-semibold mb-2 text-brand-light">Impact Overview</h3>
            <div className="space-y-2">
              <div className="flex justify-between"><span>Villages Affected:</span><span className="font-mono">14</span></div>
              <div className="flex justify-between"><span>Pop. at Risk:</span><span className="font-mono">124,500</span></div>
              <div className="flex justify-between"><span>Max Depth:</span><span className="font-mono text-red-400">5.2m</span></div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}