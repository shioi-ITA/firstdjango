firstdjango
===========

I'm a newbie with django. I read the Django Book on the Internet.

This is my first django project based on python2.7, django1.6 and sqlite3.
I used GenericViews(ListView, DetailView, UpdateView, CreateView, DeleteView).
I implement CSRF, Authentication and Authorization.

Before you try, you can create tables by syncdb, and implement the data.

update 2014/03/30
------------------
I added flatpages samples.
(I'm reading the book "The Practical Django Project 2nd edition".)

I tried to use tinyMCE_3.5.10, but it did'nt work well.
So, I used tinyMCE.4.0.20. and Admin GUI of flatpages is little odd.

If you access "http://localhost:8000/search/?q=django",you can get HttpResponce.

update 2014/02/16
------------------
I added I18N and sampleDB(db.sqlite3).

Site Administrator's username/password is administrator/administrator.

The Users's username/password are adam.smith/adam.smith and john/due.

update 2014/02/19
------------------
update GUI

update 2014/02/24
------------------
update templates (href description)




DJANGOの初心者です。インターネット上のthe Django Bookを読んで、実装してみました。
python2.7, django1.6, sqlite3を基に作成しています。
（python3.3でも動きます。）

GenericViewのみを駆使して、シンプルなサンプルを作成してみました。
CSRF、認証、認可も装備しました
ここに至るまでには四苦八苦しましたが、漸く動くものが出来ました。

お試し頂く前に、syncdbでテーブルを作成し、データをご用意作成下さい。

update 2014/03/30
------------------
Djangoのフラットページを使用したサンプルを追加しました。
The Practical Django Project 2nd editionを基に勉強しています。
tinyMCEを入れることで、コンテンツにリッチテキストで入力できます。
使用する上では支障ありませんが、少し画面表示が変です。（content項目）

update 2014/02/16
------------------
国際化対応とサンプルデータベース(db.sqlite3)を追加しました。

サイト管理者のユーザ名／パスワードが、administrator/administratorです。

一般ユーザー名／パスワードが、adam.smith/adam.smith と john/dueです。


update 2014/02/19
------------------
GUI回りを少し改善（整形しました）

update 2014/02/24
------------------
テンプレートのhrefの辺りの記述を改訂しました。
