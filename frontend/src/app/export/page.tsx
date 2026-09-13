'use client';
import { Card } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';

export default function ExportPage() {
  return (
    <div className="max-w-4xl mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6 text-white">Export Results</h1>
      <div className="grid grid-cols-2 gap-6">
        <Card>
          <h3 className="font-bold text-lg mb-2">GIS Data</h3>
          <p className="text-sm text-slate-400 mb-4">Download geospatial data for further analysis in QGIS/ArcGIS.</p>
          <div className="flex flex-col gap-2">
            <Button className="bg-slate-700 hover:bg-slate-600">Export as Shapefile (SHP)</Button>
            <Button className="bg-slate-700 hover:bg-slate-600">Export as GeoJSON</Button>
            <Button className="bg-slate-700 hover:bg-slate-600">Export as GeoTIFF</Button>
          </div>
        </Card>
        <Card>
          <h3 className="font-bold text-lg mb-2">Reports</h3>
          <p className="text-sm text-slate-400 mb-4">Download PDF summary reports for stakeholders.</p>
          <div className="flex flex-col gap-2">
            <Button>Generate PDF Report</Button>
            <Button className="bg-slate-700 hover:bg-slate-600">Download CSV (Impact Data)</Button>
          </div>
        </Card>
      </div>
    </div>
  );
}