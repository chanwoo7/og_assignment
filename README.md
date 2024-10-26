<h1 align="center">OpenGallery - 오픈갤러리 개발 과제</h1>

<img width="1472" alt="image" src="https://github.com/user-attachments/assets/7a3ada7b-1e2a-431d-8200-7fe8e7bd23f4">


<br>

## 프로젝트 개요
이 프로젝트는 **Django 프레임워크** 기반의 풀스택 웹 프로젝트이며, 오픈갤러리 개발 과제 프로젝트입니다.<br>
- 웹 사이트 주소: http://opengalleryassignment.site/
<br>

## 개발 과정
### 📍 개발 기간
- 2024.10.19 ~ 2024.10.26

### 📍 작업 관리
- GitHub의 Issue 및 Pull Request를 사용하여 작업을 관리했습니다.

### 📍 커밋 컨벤션
- 코드 변경 이력을 원활히 추적하기 위해, **커밋 메시지의 맨 앞**에 아래와 같은 종류의 태그를 붙여 관리했습니다.

  - **[feat]**: 새로운 기능 추가
  - **[refactor]**: 코드 리팩토링
  - **[fix]**: 버그 수정
  - **[style]**: 스타일 변경
  - **[chore]**: 자잘한 작업 또는 일부 변경
  - **[setting]**: 빌드 및 설정 관련 작업
  - **[docs]**: README.md 문서 수정
<br>

## 기술 스택
- **Backend**: Django 4.2, Django REST framework 3.14.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Library**: BootStrap5, flatpickr (날짜 선택 용도)
- **IDE**: PyCharm
<br>

### 📍 ERD
<img width="1408" alt="image" src="https://github.com/user-attachments/assets/24b58f9a-fe2c-423e-a100-6da07d43afdf">
<br>

## 프로젝트 설명
### Backends
- 전반적으로 Django 프레임워크를 이용해 **템플릿을 렌더링**하고, **동적으로 데이터를 처리**하는 구조를 구축했습니다.
- 각 View 클래스마다 **GET 요청**과 **POST 요청**의 처리 방식을 구분했으며, 보다 RESTful하게 구현하고자 POST 요청 시에는 프론트엔드에 **JSON 형식의 응답**을 반환하여 해당 응답에 따라 프론트엔드에서의 처리 결과를 사용자에게 반환하도록 했습니다.

### Frontends
- HTML, CSS, JavaScript, BootStrap을 함께 사용하여 구현했습니다.
- 프론트엔드에서는 JavaScript를 이용하여, 비동기적으로 **AJAX 요청**을 수행하도록 구현했습니다.

### Deployments
- **AWS 라이트세일 인스턴스**를 사용했으며, **Nginx**를 기반으로 웹 서버가 동작하게끔 구현했습니다.
<br>

## 디렉토리 구조
- 📂 **artist**: 작가 관련 모델 및 뷰 app
- 📂 **artwork**: 작품 관련 모델 및 뷰 app
- 📂 **exhibiton**: 전시 관련 모델 및 뷰 app
- 📂 **management**: 관리자 관련 뷰 app
- 📂 **core**: 공통 로직 app
- 📂 **static**: 정적 파일(css, js) 폴더
- 📂 **templates**: HTML 템플릿 파일 폴더
<br>

## 참고
- 현재 웹사이트에서는 username: `admin`, password: `admin`인 유저가 관리자로 등록되어 있습니다.
  - 서버 측에서 `python manage createsuperuser` 명령어로 관리자 계정을 생성할 수 있습니다.
 
- 로컬 환경 테스트를 원하시는 경우, 이 Repository를 클론하신 후, 가상환경이 활성화된 상태에서 아래의 명령을 사용해주시면 됩니다.
  - `$ pip install -r requirements.txt`
  - `$ python manage.py runserver --settings=og_assignment.settings.local`
