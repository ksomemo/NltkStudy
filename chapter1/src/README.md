# 1章のサンプル用

## ユニークな単語の一覧

* set(集合)
* string.lower(小文字化)

などをよく使う

## nltkのテキストから使われた関数

* concordance       (検索)
* similar           (同じ文脈で使われている別の単語を見つける)
* common_contexts   (単語を共通に使っている文脈を見つける)
* dispersion_plot   (テキスト内における単語の使用箇所の分散プロットを表示する)
* generate          (テキストからテキストを生成する)

## 他でもよく使われる関数

* count
* index

これより、テキストはシーケンスやイテレータでもありそう

## nltkのテキストを引数にとって使った関数

* nltk.FreqDist

単語をキー、使用頻度を値としたdictに似た nltk.probability.FreqDist を返す

* xxx.plot を実行すると累積頻度を表示できる
* xxx.freq を実行すると指定したものの割合を返す
* 他にもいろいろ

## コロケーションとバイグラム

### コロケーションと共起
ある単語がある文章中に出たとき、その文章中に別の限られた単語が頻繁に出現すること。

コロケーションはその単語列。
形容詞付きの名詞はコロケーションであるが、定冠詞はコロケーションではないらしい。
USAなどにつく定冠詞はコロケーションになる？

### バイグラム

```
>>> help(bigrams)
Help on function bigrams in module nltk.util:

bigrams(sequence, **kwargs)
    Return a sequence of bigrams from a sequence of items.  For example:
        >>> from nltk.util import bigrams
        >>> bigrams([1,2,3,4,5])
        [(1, 2), (2, 3), (3, 4), (4, 5)]
```

前後の単語同士のペアをコロケーションとしてみなしている。

## plot されないとき

下記を実行して、
matplotlib の設定状況及びどのファイルによって設定されているかを確認できる

```
python -c "import matplotlib; print matplotlib.get_backend()"
python -c "import matplotlib; print matplotlib.matplotlib_fname()"
```

自分の場合、~/ に設定ファイル(中途半端に記述したもの)があったため動かなかった

## 自然言語の理解

自然言語処理の応用

* 語義曖昧解消
* 代名詞解析
* 言語出力の生成
* 機械翻訳
* 音声対話システム
* 含意関係

上記の概要

* 単語と単語の意味がその文脈で正しく使われているか
* 代名詞の主格や目的格などに正しく合っているか
* 質問応答。質問に対して文脈を読み取り正しい回答を出力できるか
* 上記に加えて文法の違いによる翻訳の難しさがある
* Yes/Noだけでなく、No場合や5W1Hに対して予測を行い有益な情報を導けるか
* 一方のテキストから他方のテキストを証明できるか？

## 会話システムの流れ

* 音声
* 形態素
* 構文
* 意味
* 推論

この流れは、入力を別のものに置き換えれば、会話にかぎらず翻訳や言語処理系などにも当てはまる
