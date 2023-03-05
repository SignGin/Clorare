### Demo Server

🍔 Django

## 실행 방법

1. 파이썬 설치

2. cmd에서 venv 폴더가 있는 위치로 이동

3. venv\Scripts\activate.bat 실행(가상환경 실행)

4. python manage.py runserver 실행(서버 실행)

5. 에러난다면 mysql 확인
   사용자이름: root
   패스워드: rootuser

사용자이름과 패스워드에 불만이라면 settings.py파일에서 수정

---

1. 파이썬 설치

2. cmd에서 server 폴더로 이동

3. python -m venv venv 실행해서 가상환경 생성

4. venv\Scripts\activate.bat 입력(가상환경 실행)

5. 가상환경에 필요 모듈 설치

pip install django
pip install djangorestframework
pip install mysqlclient

6. python manage.py runserver 입력(서버 실행)

p. 에러난다면 mysql 확인
사용자이름: root
패스워드: rootuser

사용자이름과 패스워드에 불만이라면 settings.py파일에서 수정

---

demo 라는 이름의 스키마 생성
python manage.py migrate 실행
그 후에 python manage.py runserver로 서버 시작
