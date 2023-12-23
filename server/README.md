### Demo Server

🍔 Django

## 실행 방법

1. 파이썬 설치

2. cmd에서 server 폴더로 이동

3. 키 파일 생성

   - server 폴더에 .env 파일 생성 (환경변수 및 키 파일)

4. 가상환경 생성

   - cmd 입력</br>
     python -m venv venv

5. 가상환경 실행

   - cmd 입력</br>
     venv\Scripts\activate.bat

6. 가상환경에 필요 모듈 설치

   - cmd 입력</br>
     pip install -r requirements.txt

7. 모델 적용

   - cmd 입력</br>
     python manage.py makemigrations</br>
     python manage.py migrate

8. 시드 적용

   - cmd 입력</br>
     python manage.py add_data --total [원하는 데이터 수]

9. 서버 실행
   - cmd 입력</br>
     python manage.py runserver 입력(서버 실행)

</br></br>

## 에러 발생시

- .env 파일 확인</br>
  해당 파일이 존재하지 않거나 내용이 적합하지 않다면 실행 불가능
