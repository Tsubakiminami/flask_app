# coding: utf-8
# 日本語入力の文字コードの注意として、
#こちらの 1 行をコードの先頭にいれておくことで
# 日本語で表示させたときに文字化けしなくなります。
# 2023/09/23
#
# requirements.txt生成方法
# pip freeze > requirements.txt　から必要なライブラリに絞る。バージョンを合わせる
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


