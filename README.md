### **Django 초보 가이드 - 실습을 통해 알아보는 장고 입문**

[[강의 링크]](https://www.inflearn.com/course/django-%EC%B4%88%EB%B3%B4-%EA%B0%80%EC%9D%B4%EB%93%9C-%EC%8B%A4%EC%8A%B5%EC%9D%84-%ED%86%B5%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%EC%9E%A5%EA%B3%A0-%EC%9E%85%EB%AC%B8/dashboard)

1강. 웹 프레임워크 Django(python) 개념 정리 [[pdf]](https://github.com/y00njaekim/Django-study/blob/inflearn/Django-beginner-guide/%EC%9B%B9-%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC-Django-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC.pdf)

2강. 웹 프레임워크 Django(python) 실습

1. 프로젝트 & app 생성

   ```bash
    1  pip install django
    2  django-admin startproject tutorial
    3  cd tutorial
    4  python3 manage.py startapp community
   ```

2. 디렉토리 구조 확인

3. 관리자 페이지 확인

   ```bash
    7  python3 manage.py createsuperuser
   ```

   `url/admin` 을 통해 관리자 페이지 접근 가능 (http://127.0.0.1:8000/admin/)

4. 글쓰기

5. 리스트

6. 글 보기

---

> 전체 terminal history

```bash
 1  pip install django
 2  django-admin startproject tutorial
 3  cd tutorial
 4  python3 manage.py startapp community
 5  python3 manage.py migrate
 6  python3 manage.py createsuperuser
 7  python3 manage.py runserver
 
```

