+++
date = "2026-03-26T12:30:48+09:00"
draft = false
title = "Hugoの使い方"
slug = 'How_To_Use_Hugo'
tags = ["Tech"]
categories = ["Tech"]
comments = true
+++

## 初めに
とりあえずHugoのコマンドを良く忘れるので、練習がてら使い方を記述してみる。
### このページの記述方法
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
 hugo new site "Pagename"
```
コレで何もないページが作成される。


## gitの導入
テーマの追加や、アップロード時に**git**を使う事が多いので簡単な導入方法を記す。<br>
gitはexeファイルをダウンロードして実行、またはwingetコマンドを扱ってインストールの2種類の方法が有る。  
本記事ではwingetコマンドを利用してインストールする。
次にインストールコマンドを記す。  
```shell
$ winget install Git.git
```
git導入が完了したら、先ほどコマンドを実行したディレクトリでgitを導入する。
```shell
$ git init
```
コレでgitを導入することが出来た。
## テーマの導入方法
テーマの導入には、gitのsubmoduleツールを利用する。  
gitのsubmoduleは、感覚的には、他言語のimport文が近い。  
```shell
$ git submodule add "theme URL" themes/"Theme Name"
```
こうすることによって`./themes`内にテーマが追加される。
このままだと、テーマを追加しただけになるので、設定ファイルを書き換える。<br>
ページのルートにある**Hugo.toml**が設定ファイルなので、コレに以下を追加する。
```toml
theme = "Your Theme name"
```
こうするとテーマが変更される。

### テーマの注意点
git submoduleで追加されたファイルは、GitHubにアップロードされた際、元のリポジトリのファイルに書き換えられる。  
そのため、基本的に`./themes`以下のディレクトリにファイルを追加したり、設定ファイルを書き換えるようなことをしてはいけない。  
どうしても設定の書き換えやファイルの追加をする場合は、ルート内のテーマ内のディレクトリ名と同じディレクトリにファイルを追加する。  
例として、`./themes/"your theme"/assets/img`にファイルを追加する場合は、`./assets/img`にファイルを追加する。

## テンプレートを用いたコンテンツの追加

ページは/hugo/contents/postsに保存するものとする。
また、コマンドはプロジェクトのルートディレクトリで実行しているものとする。
```shell
$ hugo new ./contents/posts/"your contents name"/index.md
```
このコマンドを実行すると、`/contents/posts/`以下に`"your contents name"/index.md`というディレクトリとmarkdownファイルが作成される。  
記事を書く際はこのディレクトリ内のindex.mdに本文を書き、ディレクトリ内に画像ファイル等を設置する。  
こうする理由としては、Hugoの**Page Bangle**という物の形にするためだ。

### Page Bandleとは

>Page Bandleは、コンテンツと関連リソースの両方をカプセル化するディレクトリです。
> Hugoの公式リファレンスより

Page Bandleはコンテンツを保存するディレクトリ配下以下に`./"Contents name"/index.md`のように保存されているページのこと。

```shell
post/
├── Hoge
│   ├── index.md
│   └── hogehoge.jpg
├── fuga
│   └── index.md
├── piyo.md
└── fugafuga.jpg
```
このファイル構造になっている場合、HogeディレクトリとfugaディレクトリがPage Bandleとして扱われる。piyo.mdはPage Bandleとして見なされない。  
また、Page Bandle内に画像ファイル等を保存しても問題無いが、Page Bandle内のディレクトリに保存しないと、Page Bandleとして見なされない。
この場合だと、Hogeディレクトリ内の`HogeHoge.jpg`はHogeのページバンドルとして扱われる。また、どのディレクトリにも属していない`FugaFuga.jpg`はページバンドルとして扱われない。
### Page Bandleにするメリット
色々なページをPage Bandleの形式で保存すると次のようなメリットが有る。

- ファイルの整理になる。
  - 画像とMarkdownファイルを同時に保存するため、画像がばらけて面倒なことにならない。 
- Hugo公式のツールが使用可能になる
  - Page Bandle内のPNG画像を一律でWebP画像に変換する等のツールが使える
- 記事の移植性が上がる
  - 記事のディレクトリを移動するだけで別の場所に移植できる。

のようにかなり大きなメリットがあるため、ページは基本的にPage Bandle形式で保存すると後々が楽になる。

## Markdownファイル内の設定
```shell
$ hugo new ./contents/posts/"your contents name"/index.md
```  
このコマンドを用いて制作したmarkdownファイルの先頭にこういった設定部分が記述されている。
```markdown
+++
date = "2025-08-12T12:30:48+09:00"
draft = false
title = ""
slug = ''
tags = ["Tech"]
categories = ["Tech"]
comments = true
image = ""
+++
```
コレを解説していく。
これら1つ1つの意味は次の通り。
- date        :記事の制作した日を表す。コマンド実行時に記入される
- draft       :下書きファイルかどうかを表す。trueなら下書き、falseなら公開のようになる。デフォルトではtrue
- title       :記事のタイトルを表す
- slug        :記事のURLを表す。デフォルトではファイル名
- tags        :記事のタグ付けを表す
- categories  :記事のカテゴリー付けを表す
- comments    :コメントの可否を表す。デフォルトではfalse。また、設定ファイルでコメント機能をONにしないと使用不可
- image       :記事のトップに表示する画像を指定する

記事を公開する際は`draft`をfalse、`title`を記入しておこう。

## デフォルトMarkdownファイルの書き換え
先ほど、このコマンドを用いてmarkdownファイルを作成した。  
```shell
$ hugo new ./contents/posts/"your contents name"/index.md
```
このコマンドは`/archetypes/default.md`を参考にしてファイルを作成する。  
そのため、「一部の設定をコマンド実行時に設定したい」または「記事を書く際の大枠を設定したい」場合はこのmarkdownファイルを書き換える。  
筆者は、このファイルに`image`と`comments`の設定を追加している。

## ローカルサーバでのデバッグ
サイトを追加し、デバッグを行う際は、次のコマンドを実行する。
```shell
$ hugo server -D
```
`http://localhost:1313`にサーバが立つ。
この場合、markdown内の`draft`値がfalseの場合でもローカルサーバでは表示される。

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
今のコマンドは、ローカルのmainブランチのコミットをリモートのmainブランチに適用するコマンドだ。  
これで問題が無ければ、ページが追加される。

## 編集履歴
2025/08/12 初版作成  
2026/03/25 一部コマンドの修正及び機能の解説の追加