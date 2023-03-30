import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import { motion } from 'framer-motion';

import AppLayout from '@/components/AppLayout';
import { FakePhoto } from '@/types/fakeApi';
import { motionVariants } from '@/utils/motion';
import Link from 'next/link';
import MainIntroduce from '@/components/MainIntroduce ';

const photoApi = async (): Promise<FakePhoto> => {
  const data = await axios.get('https://jsonplaceholder.typicode.com/photos/2');
  return data.data;
};

export default function Home({ randomBgColor }: { randomBgColor: string }) {
  const { data, isLoading } = useQuery({
    queryKey: ['photos'],
    queryFn: photoApi,
  });

  if (isLoading) {
    <div>..... Loading</div>;
  }

  return (
    <AppLayout>
      <div
        className={`flex flex-col items-center text-center ${randomBgColor} min-h-screen`}
      >
        <h1 className="text-2xl my-4">
          Clothing recommendation service according to the weather
        </h1>
        {/* <Link
          href="/node"
          className="border-4 border-orange-700 hover:border-orange-900 hover:bg-slate-50 p-1 rounded-md"
        >
          Node 데모 서버
        </Link> */}
        <Link
          href="/reco"
          className="border-4 border-orange-700 hover:border-orange-900 hover:bg-slate-50 p-1 rounded-md"
        >
          Let's Go ~!
        </Link>
        <div className="h-full">
          {data ? (
            <motion.div
              className="flex flex-col items-center py-4"
              initial="offscreen"
              whileInView="onscreen"
              whileHover="onhover"
            >
              <motion.img src={data.url} alt="img" variants={motionVariants} />
              <p>{data.title}</p>
            </motion.div>
          ) : null}
        </div>
        <MainIntroduce />
      </div>
    </AppLayout>
  );
}

export async function getStaticProps() {
  const backgroundColors = [
    'bg-orange-100',
    'bg-amber-100',
    'bg-lime-100',
    'bg-green-100',
    'bg-teal-100',
    'bg-sky-100',
    'bg-violet-100',
    'bg-fuchsia-100',
    'bg-pink-100',
    'bg-rose-100',
  ];
  const idx = Math.floor(Math.random() * backgroundColors.length);
  const randomBgColor = backgroundColors[idx];
  return {
    props: {
      randomBgColor,
    },
  };
}
