import { create } from 'zustand';

interface IAuthToken {
  accessToken: string;
  setAccessToken: (token: string) => void;
  refreshToken: string;
  setRefreshToken: (token: string) => void;
}

export const useAuthTokenStore = create<IAuthToken>(set => ({
  accessToken: '',
  setAccessToken: (token: string) => set({ accessToken: token }),
  refreshToken: '',
  setRefreshToken: (token: string) => set({ refreshToken: token }),
}));
