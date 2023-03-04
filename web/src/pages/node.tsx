import { useCallback, useState } from 'react';
import axios from 'axios';
import AppLayout from '@/components/AppLayout';
import AnimationWeather from '@/components/AnimationWeather';

interface tmpStyle {
  comment: string;
  top: string;
  pants: string;
}

function Node() {
  const [style, setStyle] = useState<tmpStyle>();
  const onGetClick = useCallback(async () => {
    const data = await axios.get('http://localhost:3030/sample');
    alert(`현재 기온은\n섭씨 ${data.data.temperatures}도 입니다.`);
  }, []);
  const onPostClick = useCallback(async () => {
    const data = await axios.post('http://localhost:3030/recommend', {
      style: 'casual',
    });
    setStyle(data.data);
  }, []);
  return (
    <AppLayout>
      <div className="flex flex-col justify-center items-center">
        <h1>Node 데모 서버 연결 확인</h1>
        <button onClick={onGetClick}>Get</button>
        <button onClick={onPostClick}>Post</button>
        <div>
          {style ? (
            <div>
              <h2>{style.comment}</h2>
              <h3>상의 - {style.top}</h3>
              <h3>하의 - {style.pants}</h3>
            </div>
          ) : (
            <p>Post를 누르세요</p>
          )}
        </div>
      </div>
      <AnimationWeather />
    </AppLayout>
  );
}

export default Node;
