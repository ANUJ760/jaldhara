'use client';
import { DataTable } from '@/components/ui/DataTable';
import { Badge } from '@/components/ui/Badge';
import { Button } from '@/components/ui/Button';

export default function SimulationsPage() {
  const data = [
    ['SIM-001', 'Kosi Barrage Break', '2023-10-15 10:00', <Badge className="bg-green-500/20 text-green-400">Completed</Badge>, <Button className="text-xs py-1">View</Button>],
    ['SIM-002', 'Tehri Piping Case', '2023-10-16 14:30', <Badge className="bg-blue-500/20 text-blue-400">Running (45%)</Badge>, <Button className="text-xs py-1" disabled>View</Button>],
    ['SIM-003', 'Hirakud Overtopping', '2023-10-16 09:15', <Badge className="bg-red-500/20 text-red-400">Failed</Badge>, <Button className="text-xs py-1">Logs</Button>],
  ];
  return (
    <div className="py-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-white">Simulations</h1>
        <Button>+ New Simulation</Button>
      </div>
      <DataTable headers={['Job ID', 'Scenario Name', 'Started At', 'Status', 'Actions']} data={data} />
    </div>
  );
}