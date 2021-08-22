# Covid-19-part1
COVID-19に関するデータを収集するスクリプトです。

# 事前準備

PDFのダウンロードのため、Wgetコマンドを活用します。以下の手順を踏まえてWgetを利用できるようにしてください。

## MacOSの方

1. Homebrewをインストールする。(参考 : https://brew.sh/index_ja)
2. `brew install wget`を実行する。(Homebrew内へwgetをインストールする。)

## Windowの方
[参考](https://mebee.info/2020/05/25/post-10477/)

# 各種サービスのversion

| サービス | version |
| ------------- | ------------- |
| Mac OS  | macOS Big Sur 11.5.2  |
| python  | 3.8.6, 3.8.7, 3.9.0(pipを利用するため、3.4系以降のご利用を推奨します。3.4系以降だとデフォルトでpipが入っているため。)  |

## zipをダウンロードする
1. https://github.com/kuroroblog/Covid-19-part1 へアクセスする。
2. 緑色の「Code」と書かれたボタンを選択
3. 「Download ZIP」を選択
4. ダウンロードされたzipファイルをデスクトップへ移動
5. zipファイルをダブルクリック
6. ターミナルを開く。
7. ターミナルを活用して、zipを展開して生成されたフォルダへ移動する。(`$ cd Desktop/Covid-19-part1-master`)
8. `pip install -r requirements.txt`を実行する。(Pythonファイルを実行する上で必要なモジュールをインストールする。[参考](https://note.nkmk.me/python-pip-install-requirements/))
9. `python main.py`を実行する。(content内へPDFファイル、CSVファイルが生成されていることを確認する。)

## 結果画像

**PDF**

<img width="1680" alt="screenshot 2021-08-22 15 57 57" src="https://user-images.githubusercontent.com/23373288/130345685-80121400-af9c-4516-b5b3-a27104c32434.png">

**CSV**

<img width="1680" alt="screenshot 2021-08-22 15 59 12" src="https://user-images.githubusercontent.com/23373288/130345735-25ff2141-4a01-4fbc-9f1b-51bfc74d48a1.png">

