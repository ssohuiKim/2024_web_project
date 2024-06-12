STUDY_MOA# STUDY_MOA

STUDY_MOA는 다양한 스터디 모임을 쉽게 찾고 참여할 수 있도록 돕는 웹사이트입니다. 사용자들은 공부하기 좋은 카페 추천과 모임 후기를 확인할 수 있으며, 새로운 모임을 모집하거나 기존 모임에 참여할 수 있습니다.

## 주요 기능

- **홈 화면**
  - 공부하기 좋은 카페 추천
  - 모임 후기

- **모집하기 탭**
  - 새로운 스터디 모임 모집글 작성
  - 모집글 관리

- **참여하기 탭**
  - 스터디 모임 참여 신청
  - 참여 완료된 모임 확인

## 설치 및 실행 방법

### 요구 사항

- Python 3.x
- Django 3.x
- 기타 패키지는 `requirements.txt` 파일을 참고하세요.

### 설치

1. 저장소를 클론합니다.

    ```bash
    git clone https://github.com/ssohuiKim/2024_web_project.git
    ```

2. 가상 환경을 설정하고 활성화합니다.

    ```bash
    conda activate webapp
    conda create -n django python=3.8
    conda activate django
    ```

3. 필요한 패키지를 설치합니다.

    ```bash
    npm install
    npm install flowbite-svelte date-fns
    conda install django djangorestframework

    ```

4. 데이터베이스를 설정합니다.

    ```bash
    python manage.py migrate
    ```

5. 개발 서버를 실행합니다.

    ```bash
    python manage.py runserver 0.0.0.0:8500
    ```

6. 웹 브라우저를 열고 `http://localhost:5175/`에 접속합니다.

## 사용된 기술 스택

- **백엔드**: Django
- **프론트엔드**: svelte
- **데이터베이스**: 

## contribute 방법

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 만듭니다 (`git checkout -b feature/새기능`).
3. 변경 사항을 커밋합니다 (`git commit -m '새 기능 추가'`).
4. 브랜치를 푸시합니다 (`git push origin feature/새기능`).
5. 풀 리퀘스트를 생성합니다.

## 라이선스

자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.

## 문의

궁금한 사항이나 제안 사항이 있다면, (https://github.com/ssohuiKim/ssohuiKim/2024_web_project/issues)를 통해 연락해 주세요.
