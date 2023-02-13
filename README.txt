求人企業のスクレイピングを行うためのツールです。
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

