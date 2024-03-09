import { useAuthTokenStore } from '@/atom/auth';
import { AUTH_LOCAL_STORAGE_KEY } from '@/utils/constants';

function Footer() {
  const { accessToken, refreshToken, setAccessToken, setRefreshToken } =
    useAuthTokenStore();

  const isLogin = accessToken && refreshToken;

  const onClickLogout = () => {
    if (isLogin) {
      localStorage.removeItem(AUTH_LOCAL_STORAGE_KEY);
      setAccessToken('');
      setRefreshToken('');
      alert('Logout Success 🙌');
    }
  };

  return (
    <div className="flex flex-row justify-evenly w-full h-fit my-1">
      <p className="text-center text-xs">SignGin@2023</p>
      <a href="https://github.com/SignGin/demo" target="_blank">
        Github
      </a>
      {isLogin && (
        <p className="cursor-pointer" onClick={onClickLogout}>
          Logout
        </p>
      )}
    </div>
  );
}

export default Footer;
