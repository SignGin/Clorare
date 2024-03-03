import { useAuthTokenStore } from '@/atom/auth';
import '@/styles/globals.css';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import type { AppProps } from 'next/app';
import { useRouter } from 'next/router';
import { useEffect } from 'react';

const queryClient = new QueryClient();

export default function App({ Component, pageProps }: AppProps) {
  // 로그인 체크
  const { accessToken, refreshToken } = useAuthTokenStore();
  const router = useRouter();

  useEffect(() => {
    // console.log(router.pathname);
    const pathName = router.pathname;
    const exceptionPath = ['/', '/auth/login', '/auth/signUp'];
    if (!exceptionPath.includes(pathName) && !accessToken && !refreshToken) {
      // 로그인 필요
      router.push('/auth/login');
    }
  });

  return (
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
    </QueryClientProvider>
  );
}
