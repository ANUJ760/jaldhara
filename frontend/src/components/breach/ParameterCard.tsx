'use client';
import { useState } from 'react';
import { Input } from '../ui/Input';

export function ParameterCard({ label, computedValue }: { label: string, computedValue: number }) {
  const [isManual, setIsManual] = useState(false);
  const [value, setValue] = useState(computedValue);
  
  return (
    <div className="bg-slate-800 p-4 rounded-lg border border-slate-700 flex flex-col gap-2">
      <div className="flex justify-between items-center">
        <span className="text-sm text-slate-300">{label}</span>
        <label className="flex items-center gap-2 text-xs">
          <input type="checkbox" checked={isManual} onChange={(e) => setIsManual(e.target.checked)} />
          Override
        </label>
      </div>
      {isManual ? (
        <Input type="number" value={value} onChange={(e) => setValue(Number(e.target.value))} />
      ) : (
        <div className="p-2 bg-slate-900 rounded text-slate-400 cursor-not-allowed">{computedValue}</div>
      )}
    </div>
  );
}