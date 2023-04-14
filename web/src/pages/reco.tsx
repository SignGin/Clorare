import { useCallback, useState } from 'react';
import axios from 'axios';
import Image from 'next/image';
import AppLayout from '@/components/AppLayout';
import { serverDomain } from '@/utils/constants';

enum gender {
  female = 0,
  male = 1,
}

interface ClothesData {
  top: {
    cloth_type: string;
    color: string;
    image: string;
  };
  bot: {
    cloth_type: string;
    color: string;
    image: string;
  };
  w_data: string;
  w_temp: number;
  sex: gender;
}

const commonButton = 'p-4 m-4';
const inActiveButton = 'bg-gray-400 text-slate-50';
const activeButton = 'bg-red-500 text-slate-50';

function Recomend() {
  const [select, setSelect] = useState<null | gender>(null);
  const [clothesData, setClothesData] = useState<ClothesData>();
  const [isLoading, setIsLoading] = useState<null | boolean>(null);

  const onClickGetClothes = useCallback(async () => {
    if (select === null) {
      alert('SELECT GENDER PLZ');
      return;
    }
    try {
      setIsLoading(true);
      const result = await axios.get(
        `http://127.0.0.1:8000/weatherdata/reco/${select}/`,
      );
      console.log(result.data);
      setClothesData({ ...result.data, gender: select });
    } catch (error) {
      alert('ERROR!!!!!!!!!!!!!!!!!!!!');
    } finally {
      setIsLoading(false);
    }
  }, [select]);

  return (
    <AppLayout>
      <div className="flex flex-col min-h-screen items-center justify-center bg-stone-100">
        <h1>Check Your Gender</h1>
        <div>
          <button
            className={
              commonButton +
              ' ' +
              (select === 0 ? activeButton : inActiveButton)
            }
            onClick={() => setSelect(gender.female)}
          >
            Female 👩
          </button>
          <button
            className={
              commonButton +
              ' ' +
              (select === 1 ? activeButton : inActiveButton)
            }
            onClick={() => setSelect(gender.male)}
          >
            Male 👨
          </button>
        </div>
        <button
          className={
            commonButton +
            ' bg-emerald-200 border-2 border-emerald-300 rounded-lg hover:bg-emerald-100'
          }
          onClick={onClickGetClothes}
        >
          Get Clothes !!
        </button>
        {isLoading === null ? null : isLoading ? (
          <h2>is Loading...</h2>
        ) : (
          <div>
            {clothesData?.w_data &&
            clothesData.w_temp &&
            clothesData.sex !== null ? (
              <div
                className={
                  'w-fit border-2 my-2 mx-auto p-4 bg-white ' +
                  (clothesData.sex === gender.male
                    ? 'border-blue-700'
                    : 'border-rose-700')
                }
              >
                <h2>
                  Hi! Today's{' '}
                  <strong className="text-rose-600">
                    {clothesData.w_data}
                  </strong>{' '}
                  !
                </h2>
                <h2>
                  And temperature is{' '}
                  <strong className="text-rose-600">
                    {clothesData.w_temp} °C
                  </strong>
                </h2>
              </div>
            ) : null}
            <div className="flex flex-col items-center justify-center">
              {clothesData?.top ? (
                <div className="flex flex-row m-4 animate-[showUp_1s_ease-in-out]">
                  <div className="flex flex-col p-4 m-4 border-2 rounded border-orange-400 h-fit bg-white">
                    <h1 className="text-emerald-700 text-2xl">TOP 👔</h1>
                    <h2>{clothesData.top.color}</h2>
                    <h2>{clothesData.top.cloth_type}</h2>
                  </div>
                  <div>
                    <Image
                      src={`${serverDomain}${clothesData.top.image}`}
                      alt="dummy-img"
                      width={500}
                      height={350}
                    />
                  </div>
                </div>
              ) : null}
              {clothesData?.bot ? (
                <div className="flex flex-row m-4 animate-[showUp_1s_ease-in-out]">
                  <div className="flex flex-col p-4 m-4 border-2 rounded border-orange-600 h-fit bg-white">
                    <h1 className="text-emerald-700 text-2xl">PANTS 👖</h1>
                    <h2>{clothesData.bot.color}</h2>
                    <h2>{clothesData.bot.cloth_type}</h2>
                  </div>
                  <div>
                    <Image
                      src={`${serverDomain}${clothesData.bot.image}`}
                      alt="dummy-img"
                      width={500}
                      height={350}
                    />
                  </div>
                </div>
              ) : null}
            </div>
          </div>
        )}
      </div>
    </AppLayout>
  );
}

export default Recomend;
