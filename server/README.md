### Demo Server

🍔 Django

## 실행 방법

1. 파이썬 설치

2. cmd에서 server 폴더로 이동

3. 키 파일 생성
   + server 폴더에 secrets.json 파일 생성 (비밀키 파일)

4. 가상환경 생성
   + cmd 입력</br>
      python -m venv venv

5. 가상환경 실행
   + cmd 입력</br>
      venv\Scripts\activate.bat

6. 가상환경에 필요 모듈 설치
<<<<<<< HEAD
   cmd 입력
      pip install django
      pip install djangorestframework
      pip install mysqlclient
      pip install django-cors-header
      pip install django-seed
      pip install psycopg2
=======
   + cmd 입력</br>
      pip install django djangorestframework mysqlclient django-cors-header django-seed psycopg2 requests
>>>>>>> ea38e235e5b16f4763240b36ae86cc3bac7aed14

7. 모델 적용
   + cmd 입력</br>
      python manage.py makemigrations</br>
      python manage.py migrate

8. 시드 적용
<<<<<<< HEAD
   cmd 입력
      python manage.py add_data

9. 서버 실행
   cmd 입력
      python manage.py runserver 입력(서버 실행)

10. 에러 발생시
   mysql 확인
      사용자이름: root
      패스워드: rootuser
=======
   + cmd 입력</br>
      python manage.py add_data

9. 서버 실행
   + cmd 입력</br>
      python manage.py runserver 입력(서버 실행)

</br></br>
>>>>>>> ea38e235e5b16f4763240b36ae86cc3bac7aed14

## 에러 발생시
   + mysql 확인</br>
      사용자이름: root</br>
      패스워드: rootuser</br>
      혹은 settings.py 파일에서 해당 부분을 찾아 본인에 맞게 수정
   
   + secrets.json 파일 확인</br>
      해당 파일이 존재하지 않거나 내용이 적합하지 않다면 실행 불가능

<<<<<<< HEAD
   psycopg2 설치 확인
      설치하지 않았다면 8번 시드 적용 중 에러 발생 가능성
   
=======
   + psycopg2 설치 확인</br>
      설치하지 않았다면 8번의 시드 적용 과정 중 에러 발생 가능성
   
>>>>>>> ea38e235e5b16f4763240b36ae86cc3bac7aed14
