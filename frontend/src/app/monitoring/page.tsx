'use client';
import { Card } from '@/components/ui/Card';
import { Alert } from '@/components/ui/Alert';
import { NDWIChart } from '@/components/charts/NDWIChart';
import { Toggle } from '@/components/ui/Toggle';

export default function MonitoringPage() {
  return (
    <div className="h-full flex flex-col gap-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-white">Live Monitoring Dashboard</h1>
        <div className="flex items-center gap-3">
          <span className="text-sm text-slate-400">Sentinel-1 SAR</span>
          <Toggle enabled={true} onChange={() => {}} />
          <span className="text-sm text-slate-400">Sentinel-2 Optical</span>
        </div>
      </div>
      
      <Alert type="warning">Anomaly detected at coordinates (26.5°N, 86.9°E) - High NDWI deviation in past 24 hours.</Alert>
      
      <div className="grid grid-cols-2 gap-6 h-96">
        <Card className="flex flex-col">
          <h3 className="font-semibold text-brand-light mb-4">NDWI Time Series</h3>
          <div className="flex-1"><NDWIChart data={[{date: '10/01', ndwi: 0.1}, {date: '10/02', ndwi: 0.2}, {date: '10/03', ndwi: 0.45}]} /></div>
        </Card>
        <Card className="flex flex-col">
          <h3 className="font-semibold text-brand-light mb-4">Latest Satellite Imagery</h3>
          <div className="flex-1 bg-slate-700/50 rounded flex items-center justify-center text-slate-500">Map view / Image overlay here</div>
        </Card>
      </div>
    </div>
  );
}