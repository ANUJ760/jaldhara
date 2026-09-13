'use client';
import { useState } from 'react';
export function Tabs({ tabs }: { tabs: { id: string, label: string, content: React.ReactNode }[] }) {
  const [active, setActive] = useState(tabs[0].id);
  return (
    <div>
      <div className="flex border-b border-slate-700 mb-4 gap-4">
        {tabs.map(t => (
          <button key={t.id} onClick={() => setActive(t.id)} className={`pb-2 border-b-2 font-medium ${active === t.id ? 'border-brand-blue text-brand-light' : 'border-transparent text-slate-400 hover:text-slate-200'}`}>
            {t.label}
          </button>
        ))}
      </div>
      <div>{tabs.find(t => t.id === active)?.content}</div>
    </div>
  );
}