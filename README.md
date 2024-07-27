私の担当部分のプログラムは "pubrep01/modules/test.py" です。
実行には、ライブラリのインストールが必要です。これがすごく面倒でして…
backendリポジトリを編集する前に動作確認した段階です。

プログラムの内容は、
"pubrep01/modules/emo.txt" (中身:'happy') を読み、
"pubrep01/sounds/a.wav" (音声ファイル) を出力する
というものです。
meta(facebook)が公開しているaudiocraftという音声生成ライブラリをそのまま使っています。
学習済みモデルをそのまま持ってきていまして、現状、私が手を加えた部分はありません。

jupyterファイル "pubrep01/test.ipynb" を作っておきました。
Google Driveにこのテストファイルをアップロードし、Google Colabで実行することで、
皆さんも手軽に動作確認できるはず。
進捗報告としてどうぞご査収ください。
