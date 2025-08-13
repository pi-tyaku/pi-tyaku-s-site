+++
date = "2025-08-12T12:30:48+09:00"
draft = false
title = "Hugoの使い方"
tags = ["Tech"]
categories = ["Tech"]
+++

## 初めに
とりあえずHugoのコマンドを良く忘れるので、練習がてら使い方を記述してみる。

## Webページの作り方
このコマンドで作れる。
```shell
$ hugo new page "Pagename"
```


## テンプレートを用いたコンテンツの追加

ページは/hugo/contents/postsに保存するものとする。
```shell
$ hugo new /hugo/contents/posts/"your contents name".md`
```
ファイルを作る場合は
```shell
`$ hugo new /hugo/contents/posts/"your contents name"/"your contents name".md`
```
でOK
## 簡易的にローカルサーバでデバッグする時
```shell
$ hugo server -D
```
"http://localhost:1313"にサーバが立つ。