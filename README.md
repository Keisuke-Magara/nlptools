# Python package "simple-mecab"

**MeCabをPythonから簡単に使えるようにした、`mecab`パッケージのラッパーです。**

## インストール方法

ターミナルで `pip install git+https://github.com/Keisuke-Magara/simple-mecab.git` を実行し、パッケージをインストールします。

## 使い方 **[執筆中]**

### 文の形態素を分析

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

### 文を分かち書きする

```python
from nlptools import simple_mecab

agent = simple_mecab.MeCabAgent()
wakati_gaki_list = agent.wakati_gaki("犬も歩けば棒に当たる。")
print(wakati_gaki_list)
```

```bash
bash out
```
