# Basic Recommender

古典的推薦システムの実装を行う

# Run

```bash
cp .env.example .env
docker compose up -d --build
```
関連パッケージを読み込んでビルドするので初回は時間がかかる。

# Add python package

```bash
docker compose exec brs_python3 pip3 install xxx
docker compose exec brs_python3 python3 -m pip freeze > ./.docker/python/requirements.txt
```

# Dev

localhostで立ち上がるのでブラウザからアクセスするのが楽。

intelijeで実行させる場合はPythonパッケージとJupyterパッケージを追加し、  
interpreterをdocker-composeにして接続する。

※jupter labのパスワードを求められた場合は入力せずにログインを数回クリックすればエラーが出るがアクセス可能。パスワード無しで設定しているが入力を促されてしまう。


# Files

## data

CSVデータの格納場所  
src.data.DataLoaderからダウンロードしたCSVを格納する

## notebook

jupyter notebookファイルを格納している。

- notebook/analysis.ipynb: EDA実行
- notebook/content-based: 内容ベース推薦の実行
- notebook/mf: MatrixFactorizationの実行
- notebook/svd: 特異値分解の実行

他諸々

## src

諸々のスクリプトをまとめている。

- src/data: 実験に必要なデータをダウンロード、読み込むクラス郡
- src/notification: slack等に通知する
- src/recommender: 推薦システムのクラス郡
- src/recommender/contents_based: 内容ベース推薦の実装
- src/recommender/avd: 特異値分解推薦の実装

# 参考

推薦システム実践入門　風間 正弘、飯塚 洸二郎、松村 優也
https://www.oreilly.co.jp/books/9784873119663/

推薦システムのアルゴリズム　神嶌 敏弘
https://www.kamishima.net/archive/recsysdoc.pdf