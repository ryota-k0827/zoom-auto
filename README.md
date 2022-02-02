# zoom-auto

- オンライン授業への出席を自動化するツールです。

- HALのzoom授業に合わせて、授業開始時と終了時のチャット入力にも対応。

- zoomの録画にも対応しています。

## 動作環境

> Windows 10以上

> Python 3.10.2 (WSLは不可)

## 必須プログラム

> [Python 3.10.2](https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe)

> [Zoom クライアント](https://zoom.us/client/5.9.3.3169/ZoomInstaller.exe?archType=x64)

## 使用方法

- 上記のプログラムをインストール。
- pywinautoをインストール。
  ```
  pip install pywinauto
  ```
- apprun.batを編集。設定する項目は以下の通り。
  - ミーティングID
  - パスワード
  - 授業実施時間
  - 出席確認のチャットメッセージ
- apprun.batを実行。
- あとは、時間割に合わせてタスクスケジューラを設定しておくだけ。
  - ```apprun.bat```を複製して、授業ごとに合わせて作成しておくと良い。

## 注意事項
- コンピューターオーディオへの接続をあらかじめ自動に設定。
- マイクデバイスを接続していること。（マイクデバイスを接続していないと、警告ダイアログが起動して画面キャプチャに失敗します。）