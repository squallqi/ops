安装依赖
#MySQLdb
pip install salt
pip install django-suit
pip install salt

#pip install django-mptt

backports-abc==0.5
certifi==2016.9.26
Django==1.10.5
django-crontab==0.7.1
django-filter==1.0.1
django-jet==1.0.4
django-mptt==0.8.7
django-nested-inline==0.3.6
djangorestframework==3.5.3
docutils==0.13.1
futures==3.0.5
Jinja2==2.9.4
Markdown==2.6.7
MarkupSafe==0.23
msgpack-python==0.4.8
pycrypto==2.6.1
PyYAML==3.12
pyzmq==16.0.2
requests==2.12.5
salt==2016.11.1
singledispatch==3.4.0.3
six==1.10.0
tornado==4.4.2
wheel==0.24.0

python manager.py makemigrations deploy_manager
python manager.py migrate

