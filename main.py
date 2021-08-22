import os
import subprocess
from tabula import read_pdf
import datetime
from dateutil.relativedelta import relativedelta

# ドメインパスを格納する。
domainPath = 'http://web.archive.org/web/20210801150703/https://www.fukushihoken.metro.tokyo.lg.jp/iryo/kansen/corona_portal/info/kunishihyou.files/'
# 出力するフォルダパスを格納する。
# os.getcwd() : 現在のディレクトリを取得する。
outputPath = os.getcwd() + "/content"

# 2日前の日付取得
# 参考 : https://zenn.dev/wtkn25/articles/python-relativedelta
towDaysAgo = datetime.date.today() + relativedelta(days=-2)
# 日付の形式を整える。
# 参考 : https://prograshi.com/language/python/python-change-datetime-output-format/
towDaysAgo = towDaysAgo.strftime("%m%d")
# ファイル名を設定
fileName = 'kuni' + str(towDaysAgo)

# PDF, CSVそれぞれの出力ファイル名を設定
outputPdfFileName = outputPath + '/' + fileName + '.pdf'
outputCsvFileName = outputPath + '/' + fileName + '.csv'

# 既に2日前のPDFデータを取得している場合、何もしない。
if not os.path.isfile(outputPdfFileName):
    # wgetを用いて、PDFのダウンロードを行う。
    # -O : ダウンロードするファイルの名前を変更
    # 参考 : http://kyotoforest.blog82.fc2.com/blog-entry-28.html
    cmd = "wget -O '{}' '{}'".format(outputPdfFileName, domainPath + fileName + '.pdf')
    # コマンドを実行する。
    # shell : True(参考 : https://stackoverflow.com/questions/18962785/oserror-errno-2-no-such-file-or-directory-while-using-python-subprocess-in-dj)
    subprocess.run(cmd, shell=True)

# PDFデータをもとに、CSVファイルを生成する。
with open(outputCsvFileName, "w") as f:
    # pages : どのPDFファイルを読み込むのか、指定する。
    # area : PDFファイルのどの領域を読み込むのか、指定する。
    # areaの値確認方法について part1: https://tabula-py.readthedocs.io/en/latest/faq.html#how-to-use-area-option
    # areaの値確認方法について part2 : https://github.com/tabulapdf/tabula-java/wiki/Using-the-command-line-tabula-extractor-tool#use-preview--to-grab-table-coordinates-os-x-only
    # tabula公式ドキュメント : https://tabula-py.readthedocs.io/en/latest/index.html
    dfs = read_pdf(outputPdfFileName, pages='all', area=(45.38, 508.03, 500, 600.37))
    for df in dfs:
        # PDFから読み込んだデータを、CSVファイルへ書き込む。
        # dropna : 欠損値を除外（削除）する。(参考 : https://note.nkmk.me/python-pandas-nan-dropna-fillna/)
        # rename : 行名、列名を変更する。(参考 : https://note.nkmk.me/python-pandas-dataframe-rename/)
        # to_csv : dataframeをCSVファイルへ書き込む。(参考 : https://note.nkmk.me/python-pandas-to-csv/)
        df.dropna(how='all').rename(columns={'Unnamed: 0': '結果'}, index={0: '新規感染者数', 2: '感染経路不明割合', 4: 'PCR陽性率', 6: '療養者数', 8: '病床全体', 10: '入院率', 12: 'うち重症者用病床'}).to_csv(f)
