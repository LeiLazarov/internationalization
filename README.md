# Django internationalization

This is a easy sample using Django to do language internationalization. It shows switching languages between Chinese and English, but it's the same way to add more languages.

1.clone the project to your computer or IDE

2.enter the directory of the project by 'cd internationalization'

3.set venv for the project in your way (I always use pycharm to add one)

3.install libraries the project required by 
'pip install -r requirements.txt'

4.run django sevser by 
'python manage.py runserver'

5.access to the default page

(FYI)
6.use 'django-admin makemessages -l zh_Hans' to generate the .po file

7.use 'django-admin compilemessages' to generate the .mo file

index page with Chinese
![image](https://github.com/LeiLazarov/images/blob/master/internationalization/Chinese.jpg)

index page with English
![image](https://github.com/LeiLazarov/images/blob/master/internationalization/English.jpg)
