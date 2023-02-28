import { ReactNode } from 'react';
import Head from 'next/head';

function AppLayout({ children }: { children: ReactNode }) {
  return (
    <div className="font-mono min-h-screen min-w-full">
      <Head>
        <title>Clothing X Weather</title>
        <meta name="description" content="날씨에 따른 외출복 추천 시스템" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      {children}
    </div>
  );
}

export default AppLayout;
