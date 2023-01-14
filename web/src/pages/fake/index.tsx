import React, { useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import { useQuery } from '@tanstack/react-query';
import { FakePost } from './../../types/fakeApi';

const postsApi = (): Promise<FakePost> => {
  return axios
    .get('https://jsonplaceholder.typicode.com/posts/1')
    .then(res => res.data);
};

const Fake = () => {
  const { data, isLoading } = useQuery({
    queryKey: ['posts'],
    queryFn: postsApi,
  });
  return (
    <div className="flex text-center">
      {isLoading ? (
        <p className="text-3xl color-red">loading.....</p>
      ) : (
        <div className="border-2 border-amber-500 m-4 p-4">
          <h1 className="text-sky-400/100 font-bold text-3xl">{data?.title}</h1>
          <p className="text-sky-400/75 text-base text-slate-700">
            {data?.userId}
          </p>
          <h2 className="text-sky-400/75 text-xl">{data?.body}</h2>
        </div>
      )}
    </div>
  );
};

export default Fake;
