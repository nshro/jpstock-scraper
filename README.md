# jpstock_scraper
[株式投資メモ]（https://kabuoji3.com）から日本の株式情報をスクレイピングで取得するGoプログラム

## Config
main関数内の`company={[銘柄名]:[コード]}`に該当する株式の情報を取得する．

## Output
`outputJSON()`, `outputCSV()`でそれぞれJSON形式，CSV形式で結果を出力できる．

## 注意
大規模なスクレイピングは[株式投資メモ]（https://kabuoji3.com）のサーバーに負担をかけることになります．
実行は各自の責任で行ってください．
