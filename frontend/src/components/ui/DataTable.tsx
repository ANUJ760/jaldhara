export function DataTable({ headers, data }: { headers: string[], data: any[][] }) {
  return (
    <div className="overflow-x-auto border border-slate-700 rounded-lg">
      <table className="w-full text-left bg-slate-800">
        <thead className="bg-slate-700 text-slate-200">
          <tr>{headers.map((h, i) => <th key={i} className="p-3 font-medium">{h}</th>)}</tr>
        </thead>
        <tbody className="divide-y divide-slate-700/50">
          {data.map((row, i) => (
            <tr key={i} className="hover:bg-slate-700/20">{row.map((cell, j) => <td key={j} className="p-3 text-slate-300">{cell}</td>)}</tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}