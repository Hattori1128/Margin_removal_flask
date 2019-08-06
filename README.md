# Margin_removal_flask
画像の余白を削除するwebアプリです。　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
.png, .jpg, .bmpに対応しています。　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
Pillowを用いて背景と元の画像の境界を求めて切り抜いています。

実行環境：python3.5

ディレクトリの構造

 Margin_removal_flask
 ├── README.md
 ├── app.py
 ├── static
 │   └── img
 │       └── crop_exeample.png
 ├── templates
 │   └── upload.html
 └── uploads
     └── exeample.png

ディレクトリの説明：
　/templatesにはサイトのレイアウト等を行う"upload.html"があります。
  ・サイトのレイアウト関連はここに置きます。
　/uploadsには余白のついた画像のサンプル"exeample.png"があります。
　・用いた画像の元画像は/uploadsに保存されます。
　/static/imgには余白を削除した画像のサンプル"crop_exeample.png"があります。
　・余白が削除された画像は/static/imgに、元のファイルネームに'crop_'がついた名前で保存されます。

以下の手順で実行します。
①$ cd ~/Margin_removal_flask
②$ python3.5 app.py
③表示されたサイトへアクセス
④余白を削除したい画像を参照へ
⑤'upload'を押す
⑥余白を削除した画像が表示される。
