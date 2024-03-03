import axios from 'axios';

const myAxios = axios.create();

// axios default 설정
myAxios.defaults.baseURL = 'http://127.0.0.1:8000';
myAxios.defaults.withCredentials = true;

export default myAxios;
