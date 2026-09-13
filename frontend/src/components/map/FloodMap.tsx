'use client';
import { useEffect, useRef } from 'react';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';
import { MAP_CENTER, MAP_ZOOM } from '@/lib/constants';
import { useMapStore } from '@/store/map';
import { getMockFloodExtent } from '@/lib/mock-data';

export default function FloodMap() {
  const mapContainer = useRef<HTMLDivElement>(null);
  const map = useRef<maplibregl.Map | null>(null);
  const timeStep = useMapStore(state => state.currentTimeStep);

  useEffect(() => {
    if (map.current || !mapContainer.current) return;
    
    map.current = new maplibregl.Map({
      container: mapContainer.current,
      style: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
      center: MAP_CENTER,
      zoom: MAP_ZOOM
    });

    map.current.on('load', () => {
      map.current?.addSource('flood', {
        type: 'geojson',
        data: getMockFloodExtent(0)
      });
      map.current?.addLayer({
        id: 'flood-layer',
        type: 'fill',
        source: 'flood',
        paint: {
          'fill-color': [
            'interpolate',
            ['linear'],
            ['get', 'depth'],
            0, '#0f766e',
            2, '#0284c7',
            5, '#1d4ed8'
          ],
          'fill-opacity': 0.7
        }
      });
    });
  }, []);

  useEffect(() => {
    if (map.current && map.current.getSource('flood')) {
      const source = map.current.getSource('flood') as maplibregl.GeoJSONSource;
      source.setData(getMockFloodExtent(timeStep));
    }
  }, [timeStep]);

  return <div ref={mapContainer} className="w-full h-full rounded" />;
}