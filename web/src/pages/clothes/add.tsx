import { ErrorMessage, Field, Formik } from 'formik';
import { ErrorClothes, PostClothes } from '@/types/postClothes';
import axios from 'axios';
import { Category, Gender, Season } from '@/types/enums';
import { borderLinkStyle } from '@/styles';
import Link from 'next/link';

const formRequiredData = ['category', 'cloth_type', 'season', 'gender'];
const seasons = ['spring', 'summer', 'autumn', 'winter'];
const category = ['top', 'bottom', 'coat'];
const gender = ['male', 'female', 'unisex'];

export default function Add() {
  const initialValues: PostClothes = {
    category: Category.top,
    cloth_type: 'T-Shirt',
    season: Season.spring,
    gender: Gender.unisex,
    image: null,
  };

  return (
    <div className="flex flex-col bg-slate-100 justify-center items-center min-h-screen">
      <h1>Add Clothes To Clorare</h1>
      <Formik
        initialValues={initialValues}
        validate={values => {
          const errors: Partial<ErrorClothes> = {};
          if (!values.category) {
            errors.category = 'Required';
          } else if (values.category.length === 0) {
            errors.category = 'Invalid category';
          }
          if (!values.cloth_type) {
            errors.cloth_type = 'Required';
          } else if (values.cloth_type.length === 0) {
            errors.cloth_type = 'Invalid cloth_type';
          }
          if (!values.season) {
            errors.season = 'Required';
          } else if (values.season.length === 0) {
            errors.season = 'Invalid cloth_type';
          }
          if (!values.gender) {
            errors.gender = 'Required';
          } else if (values.gender.length === 0) {
            errors.gender = 'Invalid gender';
          }
          return errors;
        }}
        onSubmit={(values, actions) => {
          axios
            .post('http://127.0.0.1:8000/clothes/add/', values)
            .then(res => {
              console.log('res', res);
              alert('추가 성공!');
              actions.setSubmitting(false);
            })
            .catch(err => {
              console.error(err);
              alert('Error');
            });
        }}
      >
        {({ isSubmitting, handleSubmit }) => (
          <form className="flex flex-col bg-slate-200" onSubmit={handleSubmit}>
            {formRequiredData.map(data => {
              if (
                data === 'season' ||
                data === 'category' ||
                data === 'gender'
              ) {
                const nowData =
                  data === 'season'
                    ? seasons
                    : data === 'category'
                    ? category
                    : gender;
                return (
                  <div className="m-4" key={data}>
                    <span className="mr-4" id={`${data}-radio`}>
                      {data}
                    </span>
                    <div
                      role="group"
                      aria-labelledby={`${data}-radio`}
                      className="flex flex-row gap-5"
                    >
                      {nowData.map(season => (
                        <label>
                          <Field type="radio" name={data} value={season} />
                          {season}
                        </label>
                      ))}
                    </div>
                    <ErrorMessage
                      name={data}
                      component="div"
                      className="text-center"
                    />
                  </div>
                );
              }
              return (
                <div className="m-4" key={data}>
                  <span className="mr-4">{data}</span>
                  <Field type={data} name={data} />
                  <ErrorMessage
                    name={data}
                    component="div"
                    className="text-center"
                  />
                </div>
              );
            })}
            <button
              type="submit"
              disabled={isSubmitting}
              className="bg-pink-200 font-bold"
            >
              Submit
            </button>
          </form>
        )}
      </Formik>
      <div className="flex gap-5 mt-10 mb-5">
        <div className={borderLinkStyle}>
          <Link href={'/'}>Go Home</Link>
        </div>
        <div className={borderLinkStyle}>
          <Link href={'/reco'}>Get Recommendation</Link>
        </div>
      </div>
    </div>
  );
}
