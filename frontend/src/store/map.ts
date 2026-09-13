import { create } from 'zustand';

interface MapState {
  currentTimeStep: number;
  setTimeStep: (step: number) => void;
}

export const useMapStore = create<MapState>((set) => ({
  currentTimeStep: 0,
  setTimeStep: (step) => set({ currentTimeStep: step }),
}));
