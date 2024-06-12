# 베이스 이미지로 Node 사용
FROM node:14

# 작업 디렉토리 설정
WORKDIR /app

# 필요 패키지 복사 및 설치
COPY ./frontend/package.json ./frontend/package-lock.json* /app/
RUN npm install

# 프로젝트 파일 복사
COPY ./frontend /app/

# 포트 개방
EXPOSE 5175

# 컨테이너 실행 시 명령어
CMD ["npm", "run", "dev"]
