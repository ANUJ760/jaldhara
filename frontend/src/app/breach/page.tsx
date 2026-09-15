'use client';
import { Card } from '@/components/ui/Card';
import { Input } from '@/components/ui/Input';
import { Button } from '@/components/ui/Button';
import { Select } from '@/components/ui/Select';

export default function BreachPage() {
  return (
    <div className="max-w-4xl mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6 text-white">Breach Parameters</h1>
      
      <div className="grid grid-cols-2 gap-6">
        <Card className="flex flex-col gap-4">
          <h2 className="text-xl font-semibold border-b border-slate-700 pb-2">Configuration</h2>
          
          <div>
            <label className="text-sm text-slate-400">Select Dam/Barrage</label>
            <Select><option>Kosi Barrage</option><option>Tehri Dam</option></Select>
          </div>
          
          <div>
            <label className="text-sm text-slate-400">Failure Mode</label>
            <Select><option>Overtopping</option><option>Piping</option><option>Instant Collapse</option></Select>
          </div>
        </Card>
        
        <Card className="flex flex-col gap-4 bg-slate-800/50">
          <h2 className="text-xl font-semibold border-b border-slate-700 pb-2">Computed Froehlich Values</h2>
          
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="text-xs text-slate-400">Breach Width (m)</label>
              <Input defaultValue="120.5" />
            </div>
            <div>
              <label className="text-xs text-slate-400">Side Slope</label>
              <Input defaultValue="1.4" />
            </div>
            <div>
              <label className="text-xs text-slate-400">Formation Time (h)</label>
              <Input defaultValue="2.5" />
            </div>
          </div>
          
          <Button className="mt-4 w-full">Run Simulation Pipeline</Button>
        </Card>
      </div>
      
      <Card className="mt-6 p-8 flex justify-center items-center h-64 border-dashed border-2">
        <span className="text-slate-500">Breach Geometry Visualization Placeholder (SVG)</span>
      </Card>
    </div>
  );
}