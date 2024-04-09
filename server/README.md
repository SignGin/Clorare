### Demo Server

🍔 Django

## 실행 방법

1. Docker 설치

2. cmd에서 server 폴더로 이동

3. 키 파일 생성

   - server 폴더에 .env 파일 생성 (환경변수 및 키 파일)

4. Docker 실행

   - cmd 입력</br>
     docker-compose up -d --build

5. 모델 적용

   - cmd 입력</br>
     docker exec -it django bash</br>
     python manage.py makemigrations</br>
     python manage.py migrate</br>

6. 시드 적용

   - cmd 입력</br>
     python manage.py add_data --total [원하는 데이터 수]
     exit

</br></br>

## 에러 발생시

- .env 파일 확인</br>
  해당 파일이 존재하지 않거나 내용이 적합하지 않다면 실행 불가능
