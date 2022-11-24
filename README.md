# Python package "mag-nlptools"

**自然言語処理関連のプログラムを書くときに便利なツールです。**

## インストール方法

1. ターミナルで `pip install git+https://github.com/Keisuke-Magara/mag-nlptools.git` を実行し、パッケージをインストールします。

## 使い方

### simple_mecab

`simple_mecab` モジュールは、 `mecab-python3` ライブラリをより簡単に利用するためのモジュールです。

#### 文の形態素を分析

```python
from nlptools import simple_mecab

agent = simple_mecab.MeCabAgent()
result = agent.parse("犬も歩けば棒に当たる。")
print(result[0])
print(result[2])
```

```bash
bash out
```

#### 文を分かち書きする

```python
from nlptools import simple_mecab

agent = simple_mecab.MeCabAgent()
wakati_gaki_list = agent.wakati_gaki("犬も歩けば棒に当たる。")
print(wakati_gaki_list)
```

```bash
bash out
```

### simple_scraping

`simple_scraping` モジュールは XPath または CSS Selector を用いて簡単にWebスクレイピングができるモジュールです。

#### CSS Selector を用いて要素をスクレイピングする

#### XPath を用いて要素をスクレイピングする
