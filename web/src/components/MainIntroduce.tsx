import { useEffect, useState } from 'react';
import { useInView } from 'react-intersection-observer';

const subTitle = 'text-lg font-bold';
const defaultTextClass = 'tracking-widest';

function MainIntroduce() {
  const { ref, inView } = useInView({
    threshold: 0,
  });
  const [textClass, setTextClass] = useState(defaultTextClass);
  useEffect(() => {
    setTextClass(
      inView
        ? `animate-[showUp_1s_ease-in-out] ${defaultTextClass}`
        : defaultTextClass,
    );
  }, [inView]);
  return (
    <div className="my-20" ref={ref}>
      <h1 className="text-2xl mb-20">옷을 잘 챙겨 입으세요!</h1>
      <h4 className={subTitle + ' ' + textClass}>당신은 아름답습니다.</h4>
      <p className={textClass}>
        옷을 잘 챙겨 입는 것은 중요합니다.
        <br /> 복장을 통해서 자신을 표현하세요.
        <br />
        아름다운 옷은 자신감을 키워주고 당신의 삶을 윤택하게 만듭니다.
      </p>
      <br />
      <h4 className={subTitle + ' ' + textClass}>
        의복으로 당신을 보호하세요.
      </h4>
      <p className={textClass}>
        튼튼한 복장으로 자신의 몸을 지키세요.
        <br /> 위험한 순간에 적절한 복장이 당신의 삶과 가족을 구할 수도
        있습니다.
        <br /> 늘 신중하고 꼼꼼하게 의복을 챙겨입으세요.
        <br /> 당신의 늘 평온하고 안전한 삶을 응원하겠습니다.
        <br />
      </p>
      <br />
      <h4 className={subTitle + ' ' + textClass}>
        당신의 소중한 순간에 함께하겠습니다.
      </h4>
      <p className={textClass}>
        당신이 기쁘거나 슬플때도 늘 함께하겠습니다.
        <br /> 포근하고 청량한 당신의 옷은 늘 함께합니다.
        <br /> 당신의 건강한 삶을 응원합니다!
      </p>
    </div>
  );
}

export default MainIntroduce;
