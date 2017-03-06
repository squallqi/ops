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



salt -C '*' test.ping -l debug
curl -sSk https://localhost:8000/login     -H 'Accept: application/x-yaml'     -d username=admin     -d password=admin123     -d eauth=pam

return:
- eauth: pam
  expire: 1488869377.946074
  perms:
  - .*
  - '@wheel'
  - '@runner'
  start: 1488826177.946074
  token: 29efb7c2a4ff8dc4b532366c07da390d65d8fd09
  user: admin

curl -sSk https://localhost:8000 \
    -H 'Accept: application/x-yaml' \
    -H 'X-Auth-Token: 29efb7c2a4ff8dc4b532366c07da390d65d8fd09'\
    -d client=local \
    -d tgt='*' \
    -d fun=test.ping


curl -sSk https://localhost:8000 \
    -H 'Accept: application/x-yaml' \
    -H 'X-Auth-Token: 29efb7c2a4ff8dc4b532366c07da390d65d8fd09'\
    -d client=local \
    -d tgt='*' \
    -d fun='grains.items'

curl -sSk https://localhost:8000 \
    -H 'Accept: application/x-yaml' \
    -H 'X-Auth-Token: 29efb7c2a4ff8dc4b532366c07da390d65d8fd09'\
    -d client=local \
    -d tgt='*' \
    -d fun='cmd.run' \
    -d arg="free -m"


 pip install --upgrade cffi
sudo apt-get install libffi-dev
sudo apt-get install libssl-dev
sudo apt-get install python-dev
pip install  pyopenssl==0.14 
sudo apt-get install libffi-dev g++ libssl-de
ImportError! No module named tornado
https://docs.saltstack.com/en/latest/ref/netapi/all/salt.netapi.rest_cherrypy.html

