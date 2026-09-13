'use client';
import { useState } from 'react';
export function ModelToggle() {
  const [model, setModel] = useState('sph');
  return (
    <div className="flex bg-slate-900 rounded p-1 border border-slate-700 w-max">
      {['SPH', 'Delft3D', 'Divergence'].map(m => (
        <button key={m} onClick={() => setModel(m.toLowerCase())} className={`px-4 py-1 text-sm rounded ${model === m.toLowerCase() ? 'bg-slate-700 text-white' : 'text-slate-400 hover:text-slate-200'}`}>
          {m}
        </button>
      ))}
    </div>
  );
}