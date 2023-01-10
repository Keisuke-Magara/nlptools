# Python package "simple-mecab"

**MeCabをPythonから簡単に使えるようにした、`mecab`パッケージのラッパーです。**

## インストール方法

ターミナルで `pip install git+https://github.com/Keisuke-Magara/simple-mecab.git` を実行し、パッケージをインストールします。

## 使い方 **[執筆中]**

### 文の形態素を分析

```python
import simple_mecab

mecab = simple_mecab.MeCabWrapper()
result = mecab.parse("犬も歩けば棒に当たる。")
print(result[0])
print(result[2])
```

```bash
Morph(word='犬', pos0='名詞', pos1='一般', pos2=None, pos3=None, conjugation_type=None, conjugation=None, stem_form='犬', pronunciation='イヌ', unknown=None)
Morph(word='歩け', pos0='動詞', pos1='自立', pos2=None, pos3=None, conjugation_type='五段・カ行イ音便', conjugation='仮定形', stem_form='歩く', pronunciation='アルケ', unknown=None)
```

### 文を分かち書きする

```python
import simple_mecab

mecab = simple_mecab.MeCabWrapper(r"-r c:\progra~2\mecab\etc\mecabrc-u")
wakati_gaki_list = mecab.wakati_gaki("犬も歩けば棒に当たる。")
print(wakati_gaki_list)
```

```bash
['犬', 'も', '歩け', 'ば', '棒', 'に', '当たる', '。']
```
