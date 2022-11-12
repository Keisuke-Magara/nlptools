#!py -3.10
from dataclasses import dataclass

import MeCab


@dataclass
class Morph:
    """MeCabの解析結果を要素別に格納するためのdataclassです。

    Variables
    ---------
    word : str
        形態素 （例：'食べ'）

    pos0 : str | None
        語の品詞 (part of speech)
        （例：'動詞'）

    pos1 : str | None
        品詞細分類1
        （例：'一般'）

    pos2 : str | None
        品詞細分類2

    pos3 : str | None
        品詞細分類3

    conjugation_type : str | None
        活用型
        （例：'下一段-バ行'）

    conjugation : str | None
        活用形
        （例：'未然形-一般'）

    stem_form : str | None
        原形
        （例：'食べる'）

    pronunciation : str | None
        発音
        （例：'タベ'）
    """
    word: str
    pos0: str | None
    pos1: str | None
    pos2: str | None
    pos3: str | None
    conjugation_type: str | None
    conjugation: str | None
    stem_form: str | None
    pronunciation: str | None


class MeCabAgent:
    """MeCabをより簡単に使えるようにするラッパークラスです。

    Features
    --------
    ・MeCabの処理結果をdataclassに格納し、アクセスしやすくしています。

    ・EOSや空文字('')の除去を行っています。

    Dependencies
    ------------
    ・コンピュータにMeCabがインストールされ、プログラムからアクセス可能である必要があります。

    ・ `mecab-python3` ライブラリがインストールされている必要があります。

    ・同ライブラリの中の Morph dataclassを使用して結果を格納します。
    """

    def __init__(self, dict_path=None) -> None:
        """
        Parameters
        ----------
        dict_path : str, optional
            MeCab実行時に参照する辞書のパスを指定してください。
            （例：`MeCab("./dict_file")`と書くと、
            `MeCab -d ./dict_file`をコマンドラインで指定したことと同義になります。）
            `None` を指定すると、デフォルト辞書を使用します。
        """
        self.tagger = MeCab.Tagger(
            r"-d ".join(dict_path) if dict_path is not None else '')

    def parse(self, sentence: str) -> list[Morph]:
        """1行の文字列をMeCabで解析します。

        Parameters
        ----------
        sentence : str
            MeCabで解析したい1行の文章

        Returns
        -------
        list[Morph]
            形態素ごとにそれぞれ Morph クラスに情報が格納されています。
            （アクセス例：`mecab_agent.parse()[0].word`）
        """
        result: list[Morph] = []
        if sentence is not None:
            self.input = sentence
        words: list[str] = self.tagger.parse(self.input).split('\n')
        words.remove('EOS')
        words.remove('')
        # print(words)
        for w in words:
            surface, others = w.split('\t')
            info = others.split(',')
            r = Morph(surface,
                      info[0] if len(info) > 0 and info[0] != '' else None,
                      info[1] if len(info) > 1 and info[1] != '' else None,
                      info[2] if len(info) > 2 and info[2] != '' else None,
                      info[3] if len(info) > 3 and info[3] != '' else None,
                      info[4] if len(info) > 4 and info[4] != '' else None,
                      info[5] if len(info) > 5 and info[5] != '' else None,
                      info[7] if len(info) > 7 and info[7] != '' else None,
                      info[9] if len(info) > 9 and info[9] != '' else None)
            result.append(r)
        return result

    def wakati_gaki(self, sentence: str):
        """文を分かち書きして、リストに格納します。

        Parameters
        ----------
        sentence : str
            分かち書きしたい文（一文）

        Returns
        -------
        list[str]
            分かち書きされた形態素のリスト
        """
        wakati_list = []
        for e in self.parse(sentence):
            wakati_list.append(e.word)
        return wakati_list


if __name__ == '__main__':
    # ----- 名詞の出現頻度をカウントするプログラム -----

    # 例文
    sentences = "庭を東へ二十歩に行き尽つくすと、" \
        "南上がりにいささかばかりの菜園があって、" \
        "真中まんなかに栗くりの木が一本立っている。これは命より大事な栗だ。" \
        "実の熟する時分は起き抜けに背戸せどを出て落ちた奴を拾ってきて、学校で食う。"

    # 出現した名詞の辞書
    appear_dict = {}

    # 出現した名詞の出現回数をカウント
    mecab = MeCabAgent()  # MeCabAgentのインスタンス生成は重いので、毎回行わないようにする
    result = mecab.parse(sentences)
    for w in result:
        if w.pos0 == '名詞':
            try:
                appear_dict[w.word] = appear_dict[w.word] + 1
            except KeyError:
                appear_dict[w.word] = 1

    print(appear_dict)
