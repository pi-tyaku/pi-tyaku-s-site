+++
date = '2025-09-05T15:41:37+09:00'
draft = false
title = 'PCにNanoKVMを導入した話'
slug = 'Add_NanoKVM'
tags = ["Tech"]
categories = ["Tech"]
comments = true
+++
## 初めに
どうも、pi-tyakuです。久しぶりにPCを開けてNanoKVMをPC内に導入し、NanoKVMにZerotier Oneをインストールしました。<br>
導入に結構時間がかかり、KVM内のOSの仕様の癖も強く、かなり苦労しました。<br>
なので、次の使用者の為に、これらのやり方を残しておこうと思います。
## 導入理由
元々[この動画](https://www.youtube.com/watch?v=5p9bfWYjdgE&t=298s&pp=ygUDS1ZN0gcJCbIJAYcqIYzv)を見て興味を持って購入していました。しかし、PCの管理には、Raspberry piを用いたIoTサーバを利用しているため導入する決断を果たせませんでした。<br>
しかし、あるタイミングでIoTサーバが止まり、SSHも出来ない状態に陥ってしまいました。<br>
今後の事を考えた際、PCの管理をIoTサーバだけに任せるよりも、KVMを導入してサーバの並列化を行った方が良いと考えたため導入に至りました。<br>
## 使用したKVM
Aliexpressで購入したNano KVM PCie を利用しました。wifi無しのモデルです。<br>
![KVM](https://ae-pic-a1.aliexpress-media.com/kf/S1c250f0b1d2c46669b3cdb4c6fb194a41.jpg_220x220q75.jpg_.avif)<br>
[商品サイト](https://ja.aliexpress.com/item/1005008285472731.html?spm=a2g0o.order_list.order_list_main.5.6e20585aD51Czh&gatewayAdapt=glo2jpn)
## 導入編
初めに、KVMのピンと、PCケースの電源ボタンなどを管理するピン、マザーボードの電源などのピンを繋ぎます。<br>
次に、KVMをPCieに刺します。<br>
KVMのHDMI端子とPCのHDMI端子を繋ぎ、KVMのUSB-HUD端子とPCのUSBポートを繋ぎます。また、LANケーブルをKVMのLAN端子に繋ぎます。<br>
ここまでで問題がなければ、PCの元電源をONにするとKVMが起動します。また、PCの電源ボタンを押すとPCが起動します。<br>
詳しい説明は公式ページの[クイックガイド](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM_PCIe/quick_start.html)を参考にしてください。
## 接続編
KVMを起動させるとIPアドレスがKVMのディスプレイに表示されます。若しくはルータの設定画面からKVMのIPアドレスを確認します。
ブラウザのURL欄にKVMのIPアドレスを入力してKVMにアクセスします。
パスワードとユーザ名を聞かれます。初めは。両方ともadminで通ります。
そうするとKVMのメイン画面に入ります。ここからPCの操作を行います。
次に、パスワードとユーザ名を変えます。
コレで、ローカルネットワーク内でKVMに接続できるようになりました。

## VPN編
KVMを外部からアクセスする際にVPNを利用することが多いと思います。デフォルトでTailScaleに対応しているので、TailScaleを利用している方はそのままログインしてください。
しかし、今回はメインで使っているZerotierOneを利用します。
[ココ](https://github.com/sipeed/NanoKVM/issues/79)と[ココ](https://github.com/Msprg/nanoKVM-ZeroTier-one)を参考にして導入します。
KVMにSSHするかブラウザからKVMのシェルを起動します。

```shell
# curl -LO https://github.com/Msprg/nanoKVM-ZeroTier-one/releases/download/latest/nanokvm-zerotier.tar
# tar x -f nanokvm-zerotier.tar && cd nanokvm-zerotier
# ./install.sh
```

専用のインストールシェルをダウンロードして実行します。
次に、導入出来ているか確認します。

```shell
# zerotier-cli status
```
これで

```shell
200 info XXXXXXXXXX 1.8.1 ONLINE
```

となれば導入が出来ています。
さらに、このコマンドを実行することによって実行時に起動するようにできます。
```shell
# mv /etc/init.d/zerotier-one /etc/init.d/S97zerotier-one
```

init.d内の実行順序にzerotierをねじ込みます。
```shell
#  mv /etc/init.d/zerotier-one /etc/init.d/S97zerotier-one
```
後は、zerotierのLinuxガイドの通りにすることによって接続できます。

## 感想
今回はNanoKVM　PCIeの導入をしました。
PCIeレーンから給電出来たりや