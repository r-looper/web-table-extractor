import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_Japanese_prefectures_by_population"

# User-Agent を指定してリクエスト
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
resp = requests.get(url, headers=headers)
resp.raise_for_status()

# 取得したHTMLをpandasに渡す
tables = pd.read_html(resp.text)

print(f"見つかったテーブル数: {len(tables)}")

df = tables[0]  # 最初の表
print(df.head())

# Excel と CSV に保存
df.to_excel("pref_population_en.xlsx", index=False)
df.to_csv("pref_population_en.csv", index=False)

print("pref_population_en.xlsx / pref_population_en.csv に保存しました")
