# 베이스 이미지로 Python 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /code

# 필요 패키지 복사 및 설치
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# 프로젝트 파일 복사
COPY . /code/

# 포트 개방
EXPOSE 8500

# 컨테이너 실행 시 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8500"]
