# 2章

## テキストコーパス

* udhr（エンコードされたもの）
* 独自のテキストコーパス

## 頻度分布

* ConditionalFreqDist
* tabluateによる図表作成
* 累積頻度をオプションで指定可能

### カレンダー

カレンダーモジュールを使って曜日一覧を取得した

```
>>> import calendar
>>> calendar.day_name
Out[63]: <calendar._localized_day instance at 0x106a1a170>
>>> calendar.day_name[:]
Out[64]: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
```

カレンダーオブジェクトからの曜日一覧(定数)の取得
始まる曜日を指定できる

```
>>> c = calendar.Calendar()
>>> list(c.iterweekdays())
Out[74]: [0, 1, 2, 3, 4, 5, 6]
>>> c = calendar.Calendar(6)
>>> list(c.iterweekdays())
Out[76]: [6, 0, 1, 2, 3, 4, 5]
```

## 2.2.3 やってみよう

* 対象はブラウンコーパスのニュースとロマンス
* この中からどの曜日が新聞またはロマンチックであるか

```
>>> import nltk
>>> from nltk.corpus import brown
>>> import calendar
>>> cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in ['news', 'romance']
        for word in brown.words(categories=genre))
>>> cfd.tabulate(samples=list(calendar.day_name))
        Monday Tuesday Wednesday Thursday Friday Saturday Sunday
   news   54   43   22   20   41   33   51
romance    2    3    3    1    3    4    5
```

* 新聞っぽいのは月曜日
* ロマンチックなのは日曜日

## 語彙資源

* 品詞などの情報付き単語やその一覧
* テキストから重複の排除したものや、頻度分布も語彙資源といえる
* 語彙資源用のコーパスが存在する
* ストップワード(高頻度に出現する単語、例として冠詞や定冠詞に加え前置詞など)
* ストップワードに含まれない単語を調べることでより制限できる

### 日本語のコーパス

englishと指定するときがあったので、日本語についてはどんなものがあるか調べてみた

```
>>> !find ~/nltk_data/ -type f -iname *japan*
~/nltk_data//corpora/udhr/Japanese_Nihongo-EUC
~/nltk_data//corpora/udhr/Japanese_Nihongo-JIS
~/nltk_data//corpora/udhr/Japanese_Nihongo-SJIS
~/nltk_data//corpora/udhr/Japanese_Nihongo-UTF8
```

## 頻度分布の比較

* nltk.FreqDist同士の比較
* nltk.FreqDist() に文字列を渡すと文字に分解してそれぞれの頻度を保持する
* これとコーパスの単語一覧を使ってターゲットというパズルを解いている

```
>>> nltk.FreqDist('abc') < nltk.FreqDist('abc')
Out[59]: False
>>> nltk.FreqDist('abc') <= nltk.FreqDist('abc')
Out[60]: True
>>> nltk.FreqDist('ac') < nltk.FreqDist('abc')
Out[61]: True
>>> nltk.FreqDist('ac') < nltk.FreqDist('ab')
Out[62]: False
```

## 発音辞書

* nltk.corpus.cmudict
* 音素という発音コード
* 同じ単語に違う発音の仕方がある
* NLPとは関係ないが、英語の発音勉強に良さそう
* 今回のコーパスおよび音素に関する詳細はArpabetを参照

### タプルの返却および展開

```
>>> def return_tuple():
        return 1,2
>>> type(return_tuple())
Out[64]: tuple
>>> a, b = return_tuple()
>>> (type(a), a, type(b), b)
Out[66]: (int, 1, int, 2)
>>> a, b, c = return_tuple()
Traceback (most recent call last):
>>> a, b
Out[71]: (1, 2)
```

* 返すときは括弧で閉じなくても良い
* 展開するときは個数が合わないとエラーになる
* そのため、事前に長さを確認しておくコードが必要となる
* 単純に出力するとタプルとなる(python2.7のprintはタプルを渡している？)

## 比較語彙リスト

* ある単語の言語コードにおける違いを比較できる
* 上記はタプルで表現される
* ja がなかった…

## 語彙目録

* 動詞などの種別や注釈などをもつデータ
* 詳細＋翻訳
* 言語について習える良いデータだと思ったが、いろいろな構造をもつらしいので扱うには難しいとのこと

## WordNet

* シラーソスとは類語辞典
* 語義および同義語
* WordNet には同義語の識別の集合がある(Synset)
* 識別には各単語に対する同義語の一覧が含まれる(lemma)
* http://ejje.weblio.jp/content/lemma
* 同義に対する定義や例文が含まれる
* 抽象的な語彙を親に、具体的な語彙を子にもつ階層構造がある
* 同義語と意味類似性を把握することで、それらを紐付け早く検索するためのインデックス構築に役立つ

### dishの語義

* 皿
* 料理

くらししか浮かばなかった

```
>>> import nltk
>>> from nltk.corpus import wordnet as wn
>>> for s in wn.synsets('dish'): print s, s.lemma_names
Synset('dish.n.01') ['dish']
Synset('dish.n.02') ['dish']
Synset('dish.n.03') ['dish', 'dishful']
Synset('smasher.n.02') ['smasher', 'stunner', 'knockout', 'beauty', 'ravisher', 'sweetheart', 'peach', 'lulu', 'looker', 'mantrap', 'dish']
Synset('dish.n.05') ['dish', 'dish_aerial', 'dish_antenna', 'saucer']
Synset('cup_of_tea.n.01') ['cup_of_tea', 'bag', 'dish']
Synset('serve.v.06') ['serve', 'serve_up', 'dish_out', 'dish_up', 'dish']
Synset('dish.v.02') ['dish']
```

* 1.5.1 語義曖昧性消化 に出てきた serve が出てきた
* Synset('smasher.n.02') には粉砕・暴力などに関連する単語がある
* dishには　敵を料理するより やっつける, 相手のくじくかせる　などの意味がある

### nltk.app.wordnet()

* アプリケーション“Pytho.app”へのネットワーク受信接続を許可しますか?というダイアログが表示された
* ブラウザが立ち上がり、http://localhost:8000/ に NLTK Wordnet Browser 表示された
* current word テキストボックスは読み込み専用だったので、next word テキストボックスに dish を入力して search ボタンをクリックした
* noun に dish の関連単語が表示された（noun は 名詞）
* 上記は、synsets の lemma_names と同じである
* verb は 動詞。SVOCのVっぽい。
* 上記にはSynset('serve.v.06') と Synset('dish.v.02') が表示された
* Synset の名称 ('dish.n.01'), ('dish.v.02') の n,v はnounとverbであることがわかった
* リンクによって辿れるため英英辞典として使える

### 語彙関係

http://ja.wikipedia.org/wiki/-onym

* holonym（ホロニム）：全体を現す名詞
* meronym（メロニム）：部分を表す名詞
* hypernym（ハイパーニム）：上位語
* hyponym（ハイポニム）：下位語

ほかにもいろいろ

## ジェネレータの扱い

ジェネレータ式、リストを扱う関数を作って試してみた

```
>>> def gen_use_func(it):
     print it
     s = 0
     for i in it:
         s += i
     return s
>>> gen_use_func(xrange(10))
xrange(10)
Out[124]: 45
>>> gen_use_func(i for i in range(10))
<generator object <genexpr> at 0x10feb77d0>
Out[125]: 45
>>> gen_use_func(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Out[126]: 45
```

ジェネレータから値を任意で取るには next() を呼び出す

```
>>> g = (i for i in range(3))
>>> g.next()
Out[5]: 0
>>> g.next()
Out[6]: 1
>>> g.next()
Out[7]: 2
>>> g.next()
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py", line 2820, in run_code
    exec code_obj in self.user_global_ns, self.user_ns
  File "<ipython-input-8-d7e53364a9a7>", line 1, in <module>
    g.next()
StopIteration
```

## イテレータ

簡単なまとめ

* イテレータとなるオブジェクトは \__iter\__() でコンテナを指定して
* next() で次の要素を返す

作ってみた

```
>>> class it:
     def __init__(self):
         self.index = 0
         self.l = range(5)
     def __iter__(self):
         return self
     def next(self):
         print 'next start'
         if self.index == len(self.l):
            raise StopIteration
         v = self.l[self.index]
         self.index += 1
         return v

>>>
>>> a = it()
for v in a: print v
next start
0
next start
1
next start
2
next start
3
next start
4
next start
```

```
def next(self):
    print 'next start'
    for v in self.l:
        yield v
```

* generatorオブジェクトがたくさん生成され、ループが終わらなかった
* next() には yield があるので ジェネレータが返ってくる
* ジェネレータ作成のみを行うので、next() からStopIteration は吐き出されない
* print v を print v.next() にすると range(5) の最初の要素 0 が返ってくる
* この場合、next() 内で for であつかうものがジェネレータでない場合にメモリを多く消費する(リストなど)
* 走査するときに位置を覚えておき、\__iter\__() でリセットするのが良い？

## 型

```
>>> type(True)
Out[3]: bool
>>> bool
Out[4]: bool
>>> type(bool)
Out[5]: type
>>> type(int)
Out[6]: type
>>> type(tuple)
Out[7]: type
```

関数だと思っていたが、typeで調べると型そのものであった

## toString

\__str\__ を実装すると文字列扱いした時に、このメソッドが呼ばれる

## 変数が定義されているかを確かめる

* 定義されていない変数を呼び出すと NameError が起こる
* try ~ except で NameError を期待して置く必要がある
* 下記の変数一覧を使うことで try ~ except を使う必要がなくなる

```
>>> type(locals())
Out[3]: dict
>>> type(globals())
Out[4]: dict
```

* dictなので時間がかからない
* 最初にきちんと定義するべきではある

## set同士の差分

```
>>> set([1,2,3]).difference(set([1,2,4]))
Out[38]: {3}
>>> set([1,2,3]) - set([1,2,4])
Out[39]: {3}
```
