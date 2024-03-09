import { AUTH_LOCAL_STORAGE_KEY } from '@/utils/constants';
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';

interface IAuthToken {
  accessToken: string;
  setAccessToken: (token: string) => void;
  refreshToken: string;
  setRefreshToken: (token: string) => void;
}

export const useAuthTokenStore = create(
  persist<IAuthToken>(
    (set, _get) => ({
      accessToken: '',
      setAccessToken: (token: string) => set({ accessToken: token }),
      refreshToken: '',
      setRefreshToken: (token: string) => set({ refreshToken: token }),
    }),
    {
      name: AUTH_LOCAL_STORAGE_KEY,
      // storage: createJSONStorage(() => sessionStorage), // (optional) by default, 'localStorage' is used
    },
  ),
);
