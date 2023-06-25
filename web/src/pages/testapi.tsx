import { SubmitHandler, useForm } from 'react-hook-form';
import axios from 'axios';

type Methods = 'GET' | 'POST';

interface Form {
  method: Methods;
  body: string;
  url: string;
}

export default function App() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Form>();
  const onSubmit: SubmitHandler<Form> = data => {
    if (!data.url.startsWith('http')) {
      alert('잘못된 URL !');
      return;
    }
    try {
      const str = JSON.parse(data.body);
      console.log(data);
      if (str) {
        axios({
          method: data.method,
          url: data.url,
          data: data.body,
        })
          .then(res => {
            console.log('res', res);
            alert(JSON.stringify(res));
          })
          .catch(err => {
            console.error(err);
          });
      }
    } catch (err) {
      console.error(err);
      alert('잘못된 body JSON !');
      return;
    }
  };

  return (
    <div className="flex w-full">
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-col w-full items-center"
      >
        <select {...register('method')} defaultValue="GET">
          <option value="GET">GET</option>
          <option value="POST">POST</option>
        </select>
        <input
          defaultValue="http://localhost:3000"
          {...register('url', { required: true })}
          placeholder="url"
          className="border-2 border-teal-700 bg-rose-200 w-1/2"
        />
        <input
          defaultValue="{}"
          {...register('body', { required: true })}
          placeholder="body"
          className="border-2 border-rose-700 bg-teal-200 w-1/2"
        />
        {errors.body && <span>This field is required</span>}
        <input type="submit" />
      </form>
    </div>
  );
}
