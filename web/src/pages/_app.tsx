import '@/styles/globals.css';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import axios from 'axios';
import type { AppProps } from 'next/app';

const queryClient = new QueryClient();

let isFirst = true;

export default function App({ Component, pageProps }: AppProps) {
  // axios default 설정
  axios.defaults.baseURL = 'http://127.0.0.1:8000';
  axios.defaults.withCredentials = true;

  // axios의 설정을 django에 맞게 맞춘다.
  axios.defaults.xsrfCookieName = 'csrftoken';
  axios.defaults.xsrfHeaderName = 'X-CSRFToken';

  axios.interceptors.request.use(
    function (config) {
      // 요청이 전달되기 전에 작업 수행
      if (isFirst) {
        axios.get('/clothes/csrf/'); // 토큰 발급
        isFirst = false;
      }
      return config;
    },
    function (error) {
      // 요청 오류가 있는 작업 수행
      return Promise.reject(error);
    },
  );
  return (
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
    </QueryClientProvider>
  );
}
