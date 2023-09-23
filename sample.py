# Python アプリケーション開発コースFlask の基礎Flask の基礎
# 2023/09/23
# sample.py
# 仮想環境を作成し実行します。
# 仮想環境を作成するには、以下のようにしてください。
# python3 -m venv flask
# source flask/bin/activate
# pip install flask
#
# python3 sample.py
# ローカルサーバの停止は、ctl+c

#必要なモジュールのインポート
from flask import Flask

#　Flask をインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあった時の処理
@app.route('/') 
def hello():
    return 'Hello World!'

# エントリーポイント
if __name__ == '__main__':
    app.run()


