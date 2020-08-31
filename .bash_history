wokon django
workon django
mkvirtualenv django
pip install django
pip update python
exit
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
django-admin startproject mysite
python manage.py runserver
python3 manage.py runserver
cd mysite
python3 manage.py runserver
python manage.py runserver
python manage.py migrate
python manage.py runserver
exit
python manage.py runserver
cd mysite
python manage.py runserver
python manage.py runserver 8001
python manage.py runserver 0:8000
python manage.py runserver 8080
python manage.py runserver 80001
python manage.py runserver 8001
python manage.py runserver 8000
netstat -ano | findstr :8000
taskkill
python manage.py runserver
exit
python manage.py migrate
cd mysite
python manage.py migrate
\dt
.schema
.schema 
schema 
cd
.schema 
dir
cd mysete
cd mysite
dir
cd mysite
dir
.schema
python settings.py
.schema
cd
\dt
SHOW TABLES;
cd mysite
python manage.py makemigrations polls
python manage.py migrations polls
python manage.py migrate polls
python manage.py startapp bolg
python manage.py startapp blog
exit
exut
exit
cllose
close
exiy
exit
mkvirtualenv django2 --python=/usr/bin/python3.8
pip instal django
pip install django
python -m django --version
exit
python manage.py createsuperuser
cd mysite
python manage.py createsuperuser
python manage.py migrate
python manage.py createsuperuser
git init
git config --global user.name "Seunghyeon Yeon"
Django 관리자 
배포하기! 
Django urls 
Django 뷰 만들기 
HTML 시작하기 
Django ORM(Querysets) 
템플릿 동적 데이터 
Django 템플릿 
CSS - 예쁘게 만들기 
템플릿 확장하기 
애플리케이션 확장하기 
Django 폼 
더 나아가기 
GitBook에 게시 
💖 Support our work and donate to our project! ✨
Donate now! 
배포하기! 
배포하기!
Note 이번 장은 조금 따라 하기 어려울 수도 있습니다. 하지만 끝까지 따라와 주세요. 배포는 웹 사이트 개발의 가장 중요한 부분이에요. 튜토리얼 중간에 배포 내용이 있는 이유는 코치가 웹사이트를 온라인으로 배포하는 까다로운 과정을 도와줄 수 있기 때문이에요. 시간이 부족하면 혼자서 해볼 수 있을 겁니다.
지금까지는 웹사이트를 내 컴퓨터에서만 볼 수 있었어요. 지금부터 웹사이트를 배포방법을 배워봅시다! 배포(deployment)는 애플리케이션을 인터넷에 올려놓아 다른 사람들도 볼 수 있게 해주는 것 말해요. :)
앞에서 배웠듯이, 웹사이트는 서버라는 곳에 들어갑니다. 인터넷 상에 서버를 제공하는 업체들은 참 많습니다. 우리는 이 중에 비교적 배포 과정이 간단한 PythonAnywhere을 사용할 거에요. PythonAnywhere는 방문자가 아주 많지 않은 소규모 애플리케이션을 위한 무료 서비스를 제공하고 있습니다. 지금 우리가 만드는 웹사이트도 해당됩니다. 
우리가 사용할 다른 외부 서비스는 GitHub이라는 코드 호스팅 서비스입니다. 요즘에는 모든 프로그래머들은 GitHub 계정을 가지고 있으니, 여러분도 GitHub 계정을 만들어봐요!
로컬컴퓨터, GitHub, Pythonanywhere 이 세 곳은 모두 중요해요. 로컬 컴퓨터는 개발 및 테스트를 수행하는 곳이 될 것입니다. 개발이 완료되면 프로그램 복사본을 GitHub에 저장합니다. 웹사이트는 PythonAnywhere에 있고 GitHub에서 코드 사본을 업데이트할 거에요.
Git 설치하기
Note 이미 설치가 완료되었다면, 다시 할 필요가 없어요. 다음 장으로 넘어가서 Git 저장소를 만드는 것부터 시작하세요.
Git이란 "버전 관리 시스템(version control system)"으로 많은 프로그래머들이 사용하고 있습니다. 이 소프트웨어는 시간 경과에 따른 파일 변경을 추적이 가능해 나중에라도 특정 버전을 다시 불러올 수 있습니다. Microsoft Word의 "변경 사항 추적"기능과 비슷하지만 훨씬 강력합니다.
Git 설치하기
Windows
OS X
Debian / Ubuntu
Fedora
openSUSE
Git 저장소 만들기
Git은 코드 저장소(repository: 줄여서 "repo"라고 합니다)에 특정한 파일들 집합의 변화를 추적하여 관리합니다. 이제 프로젝트를 시작해 볼까요? 콘솔 창을 열고 djangogirls 디렉터리에서 아래 명령어들을 실행하세요.
Note 저장소를 초기화하기 전에 여러분의 현재 작업 디렉터리가 어디인지 꼭 확인하세요. 맥OS나 Linux라면 pwd 명령으로, 윈도우라면 cd 명령어를 실행하면 알 수 있을 거예요. 반드시 djangogirls 폴더에서 해야 합니다.
command-line 
$ git init
Initialized empty Git repository in ~/djangogirls/.git/
$ git config --global user.name "Your Name"
$ git config --global user.email you@example.com
git config --global user.email tmdgus904@gmail.com
git status
git add --all
git commit -m "My Django Girls app, first commit"
https://github.com/sxy771/myblog.git
git remote add origin https://github.com/sxy771/myblog.git
git push -u origin master
tree myblog
tree mysite
dir
tree blog
python manage.py migrate
python manage.py runserver
exit
git pull
cd mysite
git pull
exit
mkvirtualenv django2 --python=/usr/bin/python3.6
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
python -m django --version
exit
close
exit
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
python --version
eixt
eix
exit
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
django-admin startproject mysite
exit
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
django-admin startproject mysite
exiy
eixt
exit
python manage.py makemigrations
cd mysite
python manage.py makemigrations
python manage.py migrate --fake
python manage.py makemigrations
python manage.py migrate
pip install django-ckeditor
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
git status
git init
git status
git add --all .
git commit -m "My Django app, first commit"
git remote add orgin https://github.com/sxy771/myblog.git
git push -u origin master
git push
git remote add origin https://github.com/sxy771/myblog.git
git push -u origin master
git status
git add --all .
git commit -m "added file for detailed blog"
git push
git push -u origin master
git pull
git merge
git commit -m "test"
git push
git pull
exit
cd mysie
cd mysite
git status
python manage.py collecstatic
python manage.py collectstatic
exit
git status
cd mysite
git status
git add --all .
git commit -m "implement simple login&logout fuction"
git push
git status
git add --all .
git commit -m "upload cv template"
git push
git status
git pull
cd mysite
django-admin startapp users
python mange.py makemigrations
python manage.py makemigrations
pythons migrate
python manage.py migrate
python manage.py makemigrations users
python manage.py createsuperuser
exit
cd mysite
python manage.py createsuperuser
cd mysite
git pull
exit
django-admin startproject mysite
cd mysite
python mamange.py startapp blogapp
python manage.py startapp blogapp
exit
cd mysite
python manage.py collectstatic
exit
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
django-admin startproject mysite
exit
git commit -m "upload others"
git add --all .
git add .gitignore
git commit -m "gitignore"
git push -u origin master
git push
git remote add https://github.com/sxy771/myblog.git
git remote add -m  https://github.com/sxy771/myblog.git
git remote add origin  https://github.com/sxy771/myblog.git
git push -u origin master
git push
git push -u origin master
git pull
git push -u origin master
git pull
cd mysite
exit
cd mysite
python manage.py startapp blogapp
git init
git config --global user.name "Seunghyeon Yeon"
git config --global user.email tmdgus904@gmail.com
git status
git add --all .
git commit -m "1st draft"
git remote add origin https://github.com/sxy771/myblog.git
git push -u origin master
django-admin startapp notice
python manage.py makemigrations notice
python manage.py migrate
git status
git add --all .
git commit -m "still trying to make webblog"
git push -u origin master
git status
git add --all .
git commit
git commit -m ""
git commit -m "revised"
git push -u origin master
python manage.py createsuperuser
git add --all .
git commit -m "revised secre_key"
git push -u origin master
git add --all .
git commit -m "revised gitignore"
git push -u origin master
git status
cd
git init
git status
git add --all .
git status
git add --all .
exit
git init
git status
git add --all .
git add mysite/
git status
git add .gitignore
git status
git commit -m "remake"
git remote origin https://github.com/sxy771/myblog.git
git add .gitignore
git status
git add .
git push -u origin master
cd mysite
ls
dir
django-admin startapp users
python manage.py makemigrations users
python manage.py makemigrations notice
exit
git add mysite/
git status
git commit -m "upload usersapp
"
git push -u origin master
cd mysite
python manage.py makemigrations notice
python manage.py migrate
cd add --all.
git status
git commit -m "updated"
cd
git add mysite/
git commit -m "updated"
git push -u origin master
git add mysite/
git commit -m "upload the form of registration page."
git push -u origin master
git add .gitignore
git status
git commit -m "revise secret.json"
git push -u origin master
exit
git clone https://github.com/sxy771/myblog.git
git status
git pull
git add mysite/
git status
git commit -m "re-upload"
django-admin startproject mysite
cd mysite
django-admin startapp blogapp
django-admin startapp notice
exit
python -i /var/www/seung904_pythonanywhere_com_wsgi.py
exit
mkvirtualenv django2 --python=usr/bin/python3.8
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
python -m django --version
ext
exit
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
git pull
django-admin startproject mysite
cd mysite
django-admin startapp blogapp
cd
django-admin startproject mysite
cd mysite
django-admin startapp blogapp
exit
git add mysite
git commit -m "I hope there're errors anymore"
git push -u origin master
cd mysite
django-admin startapp users
exit
mkvirtualenv django2 --python=/usr/bin/python3.8
pip install django
django-admin startproject mysite
exit
django-admin startproject mysite
cd mysite
django-admin startapp users
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
git pull
git add .gitignore
cd
git add .gitignore
git add mysite
git status
git commit -m "processing well till now"
git push -u origin master
exit
git add mysite
git status
git push -u origin master
git commit -m "going well"
git push -u origin master
cd mysite
django-admin startapp notice
python manage.py makemigrations
python manage.py migrate
cd
git mysite
git add mysite
git commit -m "almost done, added postionf form"
git push -u origin master
git add mysite
git commit -m "need to add cv template"
git push -u origin master
exit
pip install pillow
python manage.py makemigrations notice
ls
cd mysite
python manage.py makemigrations notice
python manage.py migrate
python manage.py makemigrations notice
python manage.py migrate
python manage.py makemigrations notice
python manage.py migrate
python manage.py startapp
python manage.py makemigrations free
ls
exit
python manage.py makemigrations free
cd mysite
python manage.py makemigrations free
python manage.py migrate
python manage.py startapp resume
python manage.py makemigrations resume
python manage.py migrate
python manage.py makemigrations resume
python manage.py makemigrations users
python manage.py migrate
python manage.py makemigrations notice
python manage.py makemigrations free
python manage.py makemigrations resume
cd
git add mysite
git commit -m "only one function doesn't work"
git push -u origin master
git add mysite
git commit -m "only one function doesn't work"
git push -u origin master
python -m django --version
pip install selenium
from selenium import webdriver as wd driver = wd.Chrome(executable_path="chromedriver.exe") url = "https://www.naver.com" driver.get(url)
출처: https://somjang.tistory.com/entry/WindowsWindows10에-Selenium설치하기 [솜씨좋은장씨]
git status
git init
git remote add -f origin https://github.com/sxy771/myblog.git
git status
git add --all .
git reset --merge ORIG_HEAD
git stuatus
git status
git reset --hard ORIG_HEAD
git add --all .
git commit -m "dd"
git status
git add .
got add --.*
got add --all .
got add --all.
git add -A
git init
git pull
git add --all.
git add --all .
exit
