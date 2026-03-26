+++
date = '2026-03-26T13:27:13+09:00'
draft = true
title = 'Git Hooksのつかいかた'
slug = 'How_to_use_git_hooks'
tags = ["tech"]
categories = ["tech"]
image = ''
comments = true
+++
## はじめに
どうも、pi-tyakuです。本文となるような記事は教習所シリーズ以降久しぶりな気がします。
今回は、`git commit`時に処理を実行するgit hooksの扱いを解説します。

## git hooksとは?
> Git フック
> 他のバージョンコントロールシステムと同じように、Gitにも特定のアクションが発生した時にカスタムスクリプトを叩く方法があります。  
引用元:[Git-のカスタマイズ-Git-フック](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%82%A4%E3%82%BA-Git-%E3%83%95%E3%83%83%E3%82%AF)  
git hooksは、git公式が提供している、カスタムスクリプトを実行するためのhooksです。
今回は`git commit`時に、スクリプトを実行するように設定します。

## スクリプトの準備
初めにコレをやらないと意味がありません。
スクリプトはシェルスクリプトでもpython等のスクリプトでもOKなので各自用意しましょう。
また、プロジェクトのルートディレクトリからコマンドで実行できるようにしておきましょう。

## git hooksの設定
gitを設定したプロジェクトルート内の`.git/hooks`ディレクトリにhooksスクリプトがあります。
流れとして、必要なタイミングのスクリプトを書き換えてスクリプトを実行できるようにします。
今回は、`git commit`時に実行したいので、`pre-commit.sample`を書き換える事にします。
