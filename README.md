# WebForum
Web forum project for course Secure Programming. It is still quite far away from finished at this point.
## Requirements
Python 3.7  
## Installation
Program is build with Django and run with pipenv https://github.com/pypa/pipenv on Windows  
`pip install pipenv`  

Clone repository  
`git clone https://github.com/TeroMi/WebForum.git`  

In repository folder install pipenv packages from Pipfile running command  
`pipenv install`  

Once all packages are succesfully installed, before running change to Django app folder (where manage.py resides) and run the migrations  
`pipenv run python manage.py makemigrations`  
and    
`pipenv run python manage.py migrate`  

After the migrations are done you can run the server  
`pipenv run python manage.py runserver`  

In your browser go to localhost:8000 to access the WebForum  

## Current features
- Create Threads
- Upvote/downvote threads
- Comment on threads (UI is not complete)

## Possible future features/improvements
- Moderator rights to manage content
- Author can edit/delete own post
- Upvote/Downvote comments
- Share code snippets
- Rich text editor for both creation of threads and comments
- Login expiration
- Change database to MySQL, PostgreSQL etc. 
