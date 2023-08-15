import { ErrorMessage, Field, Form, Formik } from 'formik';
import { Gender } from '@/types/gender';
import { ErrorClothes, PostClothes } from '@/types/postClothes';
import axios from 'axios';

const formRequiredData = [
  'category',
  'cloth_type',
  'max_temp',
  'min_temp',
  'gender',
];

export default function Add() {
  const initialValues: PostClothes = {
    category: 'hat',
    cloth_type: 'summer',
    max_temp: 100,
    min_temp: -100,
    gender: Gender.female,
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
          if (!values.max_temp) {
            errors.max_temp = 'Required';
          } else if (values.max_temp > 100) {
            errors.max_temp = 'Invalid max_temp';
          }
          if (!values.min_temp) {
            errors.min_temp = 'Required';
          } else if (values.min_temp < -100) {
            errors.min_temp = 'Invalid min_temp';
          }
          if (!values.gender) {
            errors.gender = 'Required';
          } else if (values.gender !== 'male' && values.gender !== 'female') {
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
            {formRequiredData.map(data => (
              <div className="m-4" key={data}>
                <span className="mr-4">{data}</span>
                <Field type={data} name={data} />
                <ErrorMessage
                  name={data}
                  component="div"
                  className="text-center"
                />
              </div>
            ))}
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
    </div>
  );
}
