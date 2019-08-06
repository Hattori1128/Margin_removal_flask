import os
# request：フォームから送信した情報を扱うためのモジュール
# redirect：ページの移動
# url_for：アドレス遷移
from flask import Flask, render_template, request, redirect, url_for
# secure_filename：ファイル名をチェックするための関数
from werkzeug.utils import secure_filename
# send_from_directory：画像のダウンロード
# flash：flashメッセージを表示
from flask import send_from_directory, flash
# Image：画像を取扱
# ImageChops：画像を合成
from PIL import Image, ImageChops

# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = 'uploads'
CHANGE_FOLDER = 'static/img'

# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'bmp','PNG', 'JPG', 'BMP'])

app = Flask(__name__)

# 紐付け
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CHANGE_FOLDER'] = CHANGE_FOLDER
app.config["SECRET_KEY"] = "kouhei1128"

def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def Crop_Image(image):
    # 背景色画像を作成
    bg = Image.new("RGB", image.size, image.getpixel((0, 0)))

    # 背景色画像と元画像の差分画像を作成
    diff = ImageChops.difference(image, bg)

    # 背景色との境界を求めて画像を切り抜く
    croprange = diff.convert("RGB").getbbox()
    crop_image = image.crop(croprange)

    return crop_image

@app.route('/', methods=["GET", "POST"])
def upload_file():
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'file' not in request.files:
            flash("ファイルがありません","failed")
            return redirect(request.url)
        # データの取り出し
        file = request.files['file']
        print('data_catch')
        # ファイル名がなかった時の処理
        if file.filename == '':
            flash("ファイルがありません","failed")
            return redirect(request.url)
        # ファイルのチェック
        if file and allwed_file(file.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(file.filename)
            # ファイルの保存
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('data_save')

            #画像として読込
            image = Image.open('uploads/'+filename)
            #余白削除
            crop_image=Crop_Image(image)
            crop_filename = 'crop_' + filename
            crop_image.save(os.path.join(app.config['CHANGE_FOLDER'], crop_filename))

            flash("photo_upload","success")
            return redirect(url_for('uploaded_file', filename=crop_filename))
    else:
        print('connect')
    return render_template('upload.html')

@app.route('/uploads/<filename>')
# ファイルを表示する
def uploaded_file(filename):
    return send_from_directory(app.config['CHANGE_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
