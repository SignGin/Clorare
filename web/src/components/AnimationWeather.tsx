import { useEffect, useRef } from 'react';
import Lottie from 'lottie-web';
import dayNightLottie from '../assets/day-night.json';

function AnimationWeather() {
  const lottieRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (lottieRef.current) {
      Lottie.loadAnimation({
        container: lottieRef.current,
        renderer: 'svg',
        loop: true,
        autoplay: true,
        animationData: dayNightLottie,
      });
    }
    return () => Lottie.destroy();
  }, []);
  return <div ref={lottieRef}></div>;
}

export default AnimationWeather;
