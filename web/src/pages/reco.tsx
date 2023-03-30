import { useCallback, useEffect, useState } from 'react';
import AppLayout from '@/components/AppLayout';
import axios from 'axios';

enum gender {
  female = 0,
  male = 1,
}

const commonButton = 'p-4 m-4';
const inActiveButton = 'bg-gray-400 text-slate-50';
const activeButton = 'bg-red-500 text-slate-50';

function Recomend() {
  const [select, setSelect] = useState<null | gender>(null);
  const [clothesData, setClothesData] = useState<null | object>(null);
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
      setClothesData(result.data);
    } catch (error) {
      alert('ERROR!!!!!!!!!!!!!!!!!!!!');
    }
  }, [select]);

  return (
    <AppLayout>
      <div className="flex flex-col min-h-screen items-center justify-center">
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
            Female
          </button>
          <button
            className={
              commonButton +
              ' ' +
              (select === 1 ? activeButton : inActiveButton)
            }
            onClick={() => setSelect(gender.male)}
          >
            Male
          </button>
        </div>
        <button
          className={
            commonButton + ' bg-emerald-200 rounded-lg hover:bg-emerald-100'
          }
          onClick={onClickGetClothes}
        >
          Get Clothes !!
        </button>
        {clothesData ? (
          <div>
            <h2>{clothesData[0].cloth_type}</h2>
            <h2>{clothesData[0].color}</h2>
          </div>
        ) : null}
      </div>
    </AppLayout>
  );
}

export default Recomend;
