私の担当部分のプログラムは "pubrep01/modules/test.py" です。

meta(facebook)が公開しているaudiocraftという音声生成ライブラリをそのまま使っています。
学習済みモデルをそのまま持ってきていまして、現状、私が手を加えた部分はありません。

プログラムの内容は、
"pubrep01/modules/emo.txt" (中身:'happy') を読み、
"pubrep01/sounds/a.wav" (音声ファイル) を出力する
というものです。

実行には、ライブラリのインストールが必要です。これがすごく面倒でして…
同じ環境ですぐ動作確認できるよう、Google Colabでテスト用のjupyterファイル "pubrep01/test.ipynb" を作っておきましたので、
ご査収ください。
