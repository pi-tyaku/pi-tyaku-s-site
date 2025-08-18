+++
date = "2025-08-12T12:30:48+09:00"
draft = false
title = "Hugoの使い方"
slug = 'How_To_Use_Hugo'
tags = ["Tech"]
categories = ["Tech"]
comments = true
+++

## 初めに
とりあえずHugoのコマンドを良く忘れるので、練習がてら使い方を記述してみる。
## このページの記述方法
基本的にこのページでは、windowsを利用して開発しているユーザを対象とする。
```shell
$ "Command name" 
基本的にこの書き方が出てきたらPowerShell等でコマンドを実行するものとする。
最初の$はコマンドラインの先頭を表すため、コマンドに含まない
```
```shell
基本的に""で囲んだ文章は、""内の文章に対応した値として扱う。
コマンド実行時には、各自の値に書き換えて実行して欲しい。
```
```shell
Folder/
├── Folder1
│   ├── index.md
│   └── welcome.jpg
├── Folder2
│   └── index.md
└── Test.md
このような記述が出てきたらファイル構造を表す。
```

```markdown
最初に何も書かれていない場合はmarkdownファイルとして扱う。
```

## Webページの作り方
このコマンドで作れる。
```shell
 hugo new page "Pagename"
```

## gitの導入
テーマの追加や、アップロード時に**git**を使う事が多いので簡単な導入方法を記す。<br>
gitは各自exeファイルをダウンロードして実行するか、以下のwingetコマンドを利用してインストールするかどちらかを実行する。
```shell
$ winget install Git.git
```
git導入が完了したら、Hugoのサイトのルートディレクトリでこのコマンドを実行してgitを導入する
```shell
$ git init
```
## テーマの導入方法
テーマの導入には、gitのsubmoduleツールを利用する。<br>
gitのsubmoduleは、感覚的には、他言語のimport文が近い。
```shell
$ git submodule add "theme URL" themes/"Theme Name"
```
こうすることによって./themes内にテーマが追加される。
このままだと、テーマを追加しただけになるので、設定ファイルを書き換える。<br>
ページのルートにある**Hugo.toml**が設定ファイルなので、コレに以下を追加する。
```toml
theme = "Your Theme name"
```
こうするとテーマが変更される。

## テーマの注意点
git submoduleで追加されたファイルは、GitHubにアップロードされた際に元のリポジトリのファイルに書き換えられる。<br>
そのため基本的に./themes以下のディレクトリにファイルを追加したり、設定ファイルを書き換えるようなことをしてはいけない。<br>
どうしても設定の書き換えやファイルの追加をする場合は、ルート内のテーマ内のディレクトリ名と同じディレクトリにファイルを追加する。
簡単に言うと、
```shell
./themes/"your theme"/assets/img
```
にファイルを追加する場合は、
```shell
./assets/img
```
にファイルを追加する。

## テンプレートを用いたコンテンツの追加

ページは/hugo/contents/postsに保存するものとする。
```shell
`$ hugo new /hugo/contents/posts/"your contents name"/index.md`
```
でOK
こうする理由としては、Hugoには**Page Bangle**という物が存在するため、それに合わせたファイル構造をした方が都合がよいからである。

## Page Bandleとは？

>Page Bandleは、コンテンツと関連リソースの両方をカプセル化するディレクトリです。
> Hugoの公式リファレンスより

Page Bandleはコンテンツを保存するディレクトリ配下以下に
```shell
./"Contents name"/index.md
```
のように保存されているページのことである。

```shell
post/
├── Hoge
│   ├── index.md
│   └── welcome.jpg
├── fuga
│   └── index.md
└── piyo.md
```
このファイル構造になっている場合、HogeディレクトリとfugaディレクトリがPage Bandleとして扱われる。piyo.mdはPage Bandleとして見なされない。<br>
また、Page Bandle内に画像ファイル等を保存しても問題無いが、Page Bandle内のディレクトリに保存しないと、Page Bandleとして見なされない。

## Page Bandleにするメリット
色々なページをPage Bandleの形式で保存すると以下のようなメリットが有る。

- ファイルの整理になる。
  - 画像とMarkdownファイルを同時に保存するため、画像がばらけて面倒なことにならない。 
- Hugo公式のツールが使用可能になる
  - Page Bandle内のPNG画像を一律でWebP画像に変換する等のツールが使える
- 記事の移植性が上がる
  - 記事のディレクトリを移動するだけで別の場所に移植できる。

のようにかなり大きなメリットがあるため、ページは基本的にPage Bandle形式で保存すると後々が楽になる。


## ローカルサーバでのデバッグ
サイトを追加し、実際に実行できるかどうか試したい債は以下のコマンドを実行する。
```shell
$ hugo server -D
```
"http://localhost:1313"にサーバが立つ。

## GitHubへのアップロード(Push)
CloudflarePagesやGitHubPagesにアップロードする際には必ずGitHubのリポジトリにプッシュする必要がある。<br>
この章ではgitの用語がたくさん出てくるので、適宜調べて貰うか、[ココ](URL:"https://qiita.com/toshi_um/items/72c9d929a600323b2e77")等を見て貰いたい。<br>
また、gitとGitHubが連携されているものとする。<br>
初めに、git addをして今までの変更を追加する。
```shell
git add .
```
次に、今までの変更を保存する。
```shell
git commit -m "Messeage"
```
-mオプションを追加することによって、コミットメッセージを後半に追加することが出来る。
最後に、リモートリポジトリにプッシュをする。
```shell
git push origin main
```
今のコマンドは、ローカルのmainブランチのコミットをリモートのmainブランチに適用するコマンドである。<br>

