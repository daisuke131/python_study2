# seleniumでスクレイピング！

## task1. selenium起動

以下のサイトをchromeで立ち上げましょう。  
https://tenshoku.mynavi.jp/

## task2. 検索

seleniumでテキストボックスに検索ワードを入力させ、検索ボタンを押しましょう。

## task3. スクレイピング

1ページ目のスクレイピング  
会社名、タイトル、仕事内容、給与、URLを取得し、for文で全件取得し、print文で表示させましょう。

## task4. try文

エラーが発生した場合に、処理が停止してしまいますが、停止させるのではなく、パスして処理を継続できるようにしてみましょう。

## task5. 複数ページ

確認できたら、検索した全ページ全てスクレイピングし、print文で表示させましょう。

## task6. pandas

スクレイピングしたデータをpandasのDataFrameに詰め込んでいきましょう。

## task7. csv出力

DataFrameのデータをcsvにしましょう。  
csvフォルダに保存しましょう。

## task8. コンソールから入力

検索ワードをコンソールから入力できるようにしましょう。

## task9. クエリパラメーター

検索時等にWeb画面を更新する処理はurlにより制御されます。  
そのため、検索窓を使用せずにURLを直接変更することでも検索結果を取得することが可能です。  
ブラウザ操作が不要になります。  
URLのうち、検索ワードを制御している部分を見つけて、直接プログラムにて修正し検索結果を表示させましょう。  
もしわからなければ、「クエリパラメーター」などで調べてみましょう。
