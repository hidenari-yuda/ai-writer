support your owned media by writing blog and searching keywords with AI. 
====

## Install

1. install the package
$ python setup.py develop

## Requirement


## Usage


2. start
$ python manage.py

(オプション: 保存するCSVやテンプレート先を変更する場合は、settings.pyに以下の値を入れる。)
# vim settings.py
CSV_FILE_PATH = '/tmp/test.csv'
TEMPLATE_PATH = '/tmp/templates/'

# settings.pyファイルを作成した場合は、変更しない場合のDefaultは以下に設定する
CSV_FILE_PATH = None
TEMPLATE_PATH = None

## venv
sudo pip install virtualenv

virtualenv -p python3 venv 

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver 8080

pip freeze > requirements.txt

deactivate

