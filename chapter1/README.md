# 1章

## pycharm
* pycharmはidea同様にCommunityEditionがあるので、これを使う
* REPLをIDE上で使えるのでとても便利である
* 上記はimport済みモジュールおよび変数を把握できる
* クリア状態にする方法がわからないのであとで調べる

### keymap
* C-dがデバッグ実行なので、変更したい
* C-hが型階層表示なので、変更したい
* 上記は、MacOS10.5+なので、デフォルトでいいキーバインドを探す

## python
* virtualenvでインストールした2.7.5を使用する
* python3を使ってみたかったが、互換性に関するいい噂を聞かないため保留している

### 割り算
* python2.7.5では浮動小数で割らないと小数点以下切り捨てになる
* 下記でインポートしているものを使うと、切り捨てられないようになる
* これはpython3ではデフォルトらしいので、互換性問題に少し納得をした

```
1/3
0
1/3.0
0.3333333333333333
from __future__ import division
1/3
0.3333333333333333
```

### import nltk.book と from nltk import * は違う？

```
import nltk.book
nltk.book.text1
<Text: Moby Dick by Herman Melville 1851>
text1
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'text1' is not defined
```

```
from nltk import *
text1
<Text: Moby Dick by Herman Melville 1851>
```

上記より、モジュールの読み込みとモジュールの名前空間を省略可能になる読み込みの2種類がある

## NLTK
* データダウンロードにはインターネットを介するので事前に行う
* similarは同じ文脈で使われている単語を調べる
* common_contextsは同じ文脈で使われている単語を複数調べることができる
* 自然言語処理らしいことができることが分かった
* plot表示も行える(Numpy,Matplotlibに依存している)

### len

* 引数の型を気にせずに使える
* 補完時に引数名objectと出ていた

```
len(text3)
44764
len("abcdefg")
7
```

### type

* 型を調べることができる
* classに対する型はtypeなので、メタな感じがする

```
type(text3)
<class 'nltk.text.Text'>
type("abcdefg")
<type 'str'>
import nltk.text
type(nltk.text.Text)
<type 'type'>
```

### count

* 対象文字列の出現回数を調べることができる
* 文字列も同じメソッド名を持っていて、文字でなく文字列について調べることができた
* lenメソッドを持っていると思って調べたがなかった
* プリミティブと思えるものもオブジェクトなので、補完することで何を持っているか調べることができる


```
text3.count("smote")
5
"abcdefg".count("bc")
1
```

### 関数およびメソッドの型

* 関数の型も調べられるがそれぞれによって得られる結果が異なった
* nltkのメソッドとそれ以外によって下記のような結果になっている
* static扱いがあるのか疑問が残った

```
type(len)
<type 'builtin_function_or_method'>
type(text3.count)
<type 'instancemethod'>
type("abcdefg".count)
<type 'builtin_function_or_method'>
```

### 関数定義

* 下記のように複数行にまたがる場合、プロンプト表示が変わり、indentを行う必要がある
* 空行を入力すると元の表記に戻る

```
def lexical_diversity(text):
...     return len(text) / len(set(text))
...
```
