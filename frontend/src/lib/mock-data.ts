
export const getMockFloodExtent = (timeStep: number) => {
  // Returns a GeoJSON polygon that grows slightly with timeStep
  const baseRadius = 0.05 + (timeStep * 0.002);
  const center = [86.9225, 26.5194];
  return {
    type: 'FeatureCollection',
    features: [{
      type: 'Feature',
      properties: { depth: Math.random() * 5 + 1 },
      geometry: {
        type: 'Polygon',
        coordinates: [[
          [center[0] - baseRadius, center[1] - baseRadius],
          [center[0] + baseRadius, center[1] - baseRadius],
          [center[0] + baseRadius, center[1] + baseRadius],
          [center[0] - baseRadius, center[1] + baseRadius],
          [center[0] - baseRadius, center[1] - baseRadius]
        ]]
      }
    }]
  };
};

export const mockVillages = [
  { name: 'Birpur', distance: 5.2, eta: '0.5h', maxDepth: 4.5, population: 15000, evacuationPriority: 'High' },
  { name: 'Supaul', distance: 25.4, eta: '2.5h', maxDepth: 2.1, population: 85000, evacuationPriority: 'Medium' },
  { name: 'Madhepura', distance: 45.1, eta: '5.2h', maxDepth: 1.2, population: 42000, evacuationPriority: 'Low' },
  { name: 'Saharsa', distance: 60.3, eta: '8.0h', maxDepth: 0.8, population: 120000, evacuationPriority: 'Low' },
  { name: 'Nirmali', distance: 18.2, eta: '1.8h', maxDepth: 3.2, population: 28000, evacuationPriority: 'High' },
];
