# coding: utf-8
# 日本語入力の文字コードの注意として、
#こちらの 1 行をコードの先頭にいれておくことで
# 日本語で表示させたときに文字化けしなくなります。
# 2023/09/23
#
# requirements.txt生成方法
# pip freeze > requirements.txt　から必要なライブラリに絞る。バージョンを合わせる
#
# render
#  [Reagion] 日本に近い地域を選択する　Singapore
#  [Build Command] pip install -r requirements.txt
#  [Start Command] gunicorn app:app を gunicorn --chdir src view:app
#   [Addvanced][Add Environment Variable] PYTHON_VERSION 追加、Python -V で確認した値を入れる 3.11.5
#

# from flask import Flask
from flask import Flask, render_template

# app という名前で Flask オブジェクト をインスタンス化
# また、app を使用する際には「＠」をつけ忘れないよう注意しましょう。
app = Flask(__name__)

# --- View側の設定 ---
# ルートディレクトリにアクセスした場合の挙動
@app.route('/')
# def以下がアクセス後の操作
def index():
    # return 'Hello World! view.py'
    return render_template('index.html')

# エントリーポイント
if __name__ == '__main__':
    app.run()


