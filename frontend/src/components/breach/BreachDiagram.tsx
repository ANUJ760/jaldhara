export function BreachDiagram() {
  return (
    <svg width="100%" height="100%" viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
      {/* Dam body */}
      <polygon points="50,250 150,50 350,50 450,250" fill="#334155" stroke="#475569" strokeWidth="2"/>
      {/* Breach cut */}
      <polygon points="180,250 210,120 290,120 320,250" fill="#1e293b" stroke="#ef4444" strokeWidth="2" strokeDasharray="5,5"/>
      {/* Labels */}
      <text x="250" y="110" fill="#94a3b8" textAnchor="middle" fontSize="12">Breach Width (Wb)</text>
      <line x1="210" y1="120" x2="290" y2="120" stroke="#94a3b8" strokeWidth="1" />
      <text x="170" y="180" fill="#94a3b8" fontSize="12">Side Slope (Z)</text>
    </svg>
  );
}