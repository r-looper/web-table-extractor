## プロジェクト概要

このリポジトリは、Webページに掲載されている表データを自動で取得し、整形してExcel/CSVに保存するツールです。
想定される依頼内容は以下のようなものです：

「公開Webページにある表をExcelにまとめたい」
「複数ページのデータをCSVに統合してほしい」
「不要な列を削除し、列名を整理した上で納品してほしい」
本プロジェクトはそのPoC（概念実証）として作成しました。

## 使用技術
Python 3.13
pandas
requests
lxml
openpyxl

## 機能
requests + pandas.read_html により、公開Webページの表を自動取得
HTML構造が複雑でも、BeautifulSoupを併用してパース可能（拡張余地あり）
Excel（.xlsx）とCSV（.csv）の両形式で出力
将来的には不要列削除・列名リネーム・処理ログ出力なども対応可能
デモ（サンプル）

## 対象ページ：
Wikipedia: List of Japanese prefectures by population

## 実行コマンド:
python pref_population.py


## 出力ファイル:
pref_population_en.xlsx
pref_population_en.csv
Excelサンプル（先頭行イメージ）:
Prefecture	Population	Percent	Population density	Change
Tokyo	14,043,239	11.1%	6,363	+0.20%

## 想定案件との接続
管理画面からダウンロードしたCSVを整理 → Excel統合
公開ページにある表のデータ収集 → 加工・納品
不要列削除、列名統一、数値/日付の型変換などの追加対応

## 使い方
必要ライブラリをインストール
pip install pandas requests lxml openpyxl
スクリプトを実行
python pref_population.py
同一フォルダに pref_population_en.xlsx と pref_population_en.csv が生成されます

## 注意事項
本ツールは公開情報（ログイン不要ページ）を対象としています
大量アクセスや規約違反となる用途は対象外です
実際の案件では、クライアントの要件に応じて列の削除・加工・ログ出力などを追加実装可能です

## 作者について
Python学習者
データ整形・自動化処理を得意とし、継続力を強みとする
GitHub公開を通じて、クラウドソーシング案件におけるPoC事例として活用予定
