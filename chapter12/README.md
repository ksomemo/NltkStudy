# 12章

## 日本語と英語の違い

* 単語の分かち書きをしない
* スペースで区切られていない
* 正規表現で簡単に分割できない
* 集合知プログラミングでも日本語の補足があった

## Python2と日本語

* デフォルトエンコーディングASCIIでは扱えない
* 標準出力・標準入力・ファイル読み込みなどで不便
* UTF-8にすれば扱える
* Pythonファイルの場合は、先頭にエンコーディング指定
* ipythonなどの場合は、sysモジュールで変更する
* pprintモジュールとunichrなどを使うとユニコード文字を日本語として表示できる
* codecsは、import codecsする必要があった

## 日本語

* 膠着語
* 自立語＋付属語

## コーパス

* 平文コーパス
* 文や単語の区切り方を指定できる
* 元ネタは青空文庫（著作権切れ）を使う
* 全角空白がコードに書かれているので、わからなくなったら以下参照
* http://nltk.googlecode.com/svn/trunk/doc/book-jp/ch12.html
* rawなどでの出力は、ユニコード文字であり、printで表示しないと日本語として表示されない

```
>>> import nltk
>>> from nltk.corpus.reader import *
>>> from nltk.corpus.reader.util import *
>>> from nltk.text import Text
```

```
>>> jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')
>>> jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')
>>> ginga = PlaintextCorpusReader("corpora/", [r'gingatetsudono_yoru.txt'],
                               encoding='utf-8',
                               para_block_reader=read_line_block,
                               sent_tokenizer=jp_sent_tokenizer,
                               word_tokenizer=jp_chartype_tokenizer)
```

## ChaSen(茶筌)

* 形態素解析のためのツール
* nltkでは上記のツールによって解析済みのコーパスをダウンロードできる
* nltk.download() からallのjeitaというコーパスをダウンロードする

```
% find ~/nltk_data/ -iname '*jeita*'
~/nltk_data//corpora/jeita.zip
% cd ~/nltk_data//corpora/
% unzip jeita.zip
```

含まれるファイルは以下のとおり

* README, _copyright.html
* \*.chasen

chasen用のコーパスReaderは以下のようにしてインポートする

```
>>> from nltk.corpus.reader.chasen import *
```

## 依存構造

* https://kaigi.org/jsai/webprogram/2012/pdf/124.pdf が詳しい
* 修飾と被修飾，係り受けの関係に着目した構造
* よく句構造と比較されている
* 句構造は隣接する語の関係に着目した構造
* 依存構造を解析済みのコーパスが提供されている
* jeitaと同様にダウンロード後、zipファイルを解凍しておくこと

```
>>> from nltk.corpus.reader.knbc import *
>>> from nltk.corpus.util import LazyCorpusLoader
```
* knbcコーパスをnltkコーパスと同様に扱える準備をする
* nltk.data.find はパスが通っているところのnltk_dataディレクトリを見る
