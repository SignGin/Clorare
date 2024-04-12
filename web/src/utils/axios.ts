import { useAuthTokenStore } from '@/atom/auth';
import axios, { AxiosHeaders } from 'axios';

const myAxios = axios.create();

// axios default 설정
myAxios.defaults.baseURL =
  process.env.NODE_ENV === 'development'
    ? 'http://127.0.0.1:8000'
    : 'https://www.clothes-random-recommendation-project.shop';
myAxios.defaults.withCredentials = true;

myAxios.interceptors.request.use(
  config => {
    const { accessToken, refreshToken } = useAuthTokenStore.getState();

    if (accessToken && config.headers) {
      config.headers = config.headers ?? {};
      (config.headers as AxiosHeaders).set(
        'Authorization',
        `Bearer ${accessToken}`,
      );
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  },
);

export default myAxios;
