'use client';
import { useMapStore } from '@/store/map';
import { Play, Pause, RotateCcw } from 'lucide-react';
import { useState, useEffect } from 'react';

export default function TimeSlider() {
  const { currentTimeStep, setTimeStep } = useMapStore();
  const [isPlaying, setIsPlaying] = useState(false);

  useEffect(() => {
    let interval: any;
    if (isPlaying) {
      interval = setInterval(() => {
        setTimeStep(currentTimeStep >= 72 ? 0 : currentTimeStep + 1);
      }, 500);
    }
    return () => clearInterval(interval);
  }, [isPlaying, currentTimeStep, setTimeStep]);

  return (
    <div className="flex items-center gap-4 bg-slate-900 p-4 rounded-lg border border-slate-700">
      <button onClick={() => setIsPlaying(!isPlaying)} className="p-2 hover:bg-slate-800 rounded">
        {isPlaying ? <Pause size={20} /> : <Play size={20} />}
      </button>
      <button onClick={() => { setIsPlaying(false); setTimeStep(0); }} className="p-2 hover:bg-slate-800 rounded">
        <RotateCcw size={20} />
      </button>
      <div className="flex-1">
        <input type="range" min="0" max="72" value={currentTimeStep} onChange={e => setTimeStep(Number(e.target.value))} className="w-full" />
      </div>
      <div className="w-12 text-right text-brand-light font-mono">{currentTimeStep}h</div>
    </div>
  );
}