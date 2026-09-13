export function Toggle({ enabled, onChange }: { enabled: boolean, onChange: (v: boolean) => void }) {
  return (
    <div className={`w-12 h-6 flex items-center rounded-full p-1 cursor-pointer transition-colors ${enabled ? 'bg-brand-blue' : 'bg-slate-600'}`} onClick={() => onChange(!enabled)}>
      <div className={`bg-white w-4 h-4 rounded-full shadow-md transform transition-transform ${enabled ? 'translate-x-6' : ''}`} />
    </div>
  );
}