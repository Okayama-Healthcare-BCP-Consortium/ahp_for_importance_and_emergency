import pandas as pd
import ahp
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['xlsx'])

app = Flask(__name__, template_folder='templates')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ファイルを受け取る方法の指定
@app.route('/', methods=['GET', 'POST'])
def uploads_file():
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # データの取り出し
        file = request.files['file']
        # ファイルのチェック
        if file and allowed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            # ファイルの保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # アップロード後のページに転送
            return redirect(url_for('render_result', filename=filename))
    return render_template('index.html')


@app.route('/result')
def render_result():
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], request.args.get('filename'))
    
    result = ahp.calc_ahp(file_path)

    os.remove(file_path) # 不要になったデータのコピーを削除

    return render_template('result.html', result=result)


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=3000)
