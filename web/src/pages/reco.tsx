import { useCallback, useEffect, useState } from 'react';
import AppLayout from '@/components/AppLayout';
import axios from 'axios';

enum gender {
  female = 0,
  male = 1,
}

interface ClothesData {
  top: {
    id: number;
    category: number;
    cloth_type: string;
    color: string;
    temp: number;
    sex: number;
  };
  bot: {
    id: number;
    category: number;
    cloth_type: string;
    color: string;
    temp: number;
    sex: number;
  };
  w_daily_range: number;
  w_data: string;
  w_feels_like: number;
  w_humidity: number;
  w_temp: number;
  w_wind_speed: number;
  gender: gender;
}

const commonButton = 'p-4 m-4';
const inActiveButton = 'bg-gray-400 text-slate-50';
const activeButton = 'bg-red-500 text-slate-50';

function Recomend() {
  const [select, setSelect] = useState<null | gender>(null);
  const [clothesData, setClothesData] = useState<ClothesData>();
  const onClickGetClothes = useCallback(async () => {
    if (select === null) {
      alert('SELECT GENDER PLZ');
      return;
    }
    try {
      const result = await axios.get(
        `http://127.0.0.1:8000/weatherdata/reco/${select}/`,
      );
      console.log(result.data);
      setClothesData({ ...result.data, gender: select });
    } catch (error) {
      alert('ERROR!!!!!!!!!!!!!!!!!!!!');
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
        {clothesData?.w_data &&
        clothesData.w_temp &&
        clothesData.gender !== null ? (
          <div
            className={
              'border-2 m-2 p-2 bg-white ' +
              (clothesData.gender === gender.male
                ? 'border-blue-700'
                : 'border-rose-700')
            }
          >
            <h2>
              Hi! Today's{' '}
              <strong className="text-rose-600">{clothesData.w_data}</strong> !
            </h2>
            <h2>
              And temperature is{' '}
              <strong className="text-rose-600">{clothesData.w_temp} °C</strong>
            </h2>
          </div>
        ) : null}
        <div className="flex items-center justify-center">
          {clothesData?.top ? (
            <div className="flex flex-row m-4 animate-[showUp_1s_ease-in-out]">
              <div className="flex flex-col p-4 m-4 border-2 rounded border-orange-400 h-fit bg-white">
                <h1 className="text-emerald-700 text-2xl">TOP 👔</h1>
                <h2>{clothesData.top.color}</h2>
                <h2>{clothesData.top.cloth_type}</h2>
              </div>
              <img src="https://picsum.photos/200/300" alt="dummy-img" />
            </div>
          ) : null}
          {clothesData?.bot ? (
            <div className="flex flex-row m-4 animate-[showUp_1s_ease-in-out]">
              <div className="flex flex-col p-4 m-4 border-2 rounded border-orange-600 h-fit bg-white">
                <h1 className="text-emerald-700 text-2xl">PANTS 👖</h1>
                <h2>{clothesData.bot.color}</h2>
                <h2>{clothesData.bot.cloth_type}</h2>
              </div>
              <img src="https://picsum.photos/200/300" alt="dummy-img" />
            </div>
          ) : null}
        </div>
      </div>
    </AppLayout>
  );
}

export default Recomend;
