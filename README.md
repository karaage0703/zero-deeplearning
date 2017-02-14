# zero-deeplearning
ゼロから作るDeep Learningの勉強用リポジトリ

詳細は以下サイト参照ください

http://hendigi.karaage.xyz/raspberry-pi/image_processing/zero-deeplearning/

公式サイトは以下
https://github.com/oreilly-japan/deep-learning-from-scratch


3.6章のファイル実行時は本リポジトリの中で以下コマンド実行して、公式サイトとからいくつかのファイルをコピーする必要があります
```sh
$ git clone https://github.com/oreilly-japan/deep-learning-from-scratch
$ cp deep-learning-from-scratch/dataset/mnist.py ./
$ cp deep-learning-from-scratch/ch03/sample_weight.pkl ./
```

また、PILという画像処理ライブラリをインストールするために以下を実行します

```sh
$ conda install pillow
```

参考
http://python.dogrow.net/?p=117

http://sucrose.hatenablog.com/entry/2013/05/12/171105
