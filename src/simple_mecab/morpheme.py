from dataclasses import dataclass
from typing import Optional


@dataclass
class Morpheme:
    """MeCabの解析結果を要素別に格納するためのdataclassです。

    Variables
    ---------
    token : str
        形態素 （例：'食べ'）

    pos0 : str | None
        語の品詞 (part of speech)
        （例：'動詞'）

    pos1 : str | None
        品詞細分類1
        （例：'代名詞'）

    pos2 : str | None
        品詞細分類2
        （例：'一般'）

    pos3 : str | None
        品詞細分類3
        （例：'場所'）

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

    unknown : str | None
        正常に抽出できなかった場合はここに入ります。

    **それぞれの要素に入る値は使用する辞書によって異なります。**
    """
    __token: str

    @property
    def token(self) -> str:
        """形態素

        Returns
        -------
        str
            形態素の文字列を返します。

        Example
        -------
        "渋谷", "行っ"
        """
        return self.__token

    __pos0: Optional[str]

    @property
    def pos0(self) -> Optional[str]:
        """品詞

        Returns
        -------
        str | None
            形態素の品詞を文字列として返します。
            存在しない場合は`None`を返します。

        Example
        -------
        "名詞", "動詞", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__pos0

    __pos1: Optional[str]

    @property
    def pos1(self) -> Optional[str]:
        """品詞細分類1

        Returns
        -------
        str | None
            形態素の品詞細分類1を文字列として返します。
            存在しない場合は`None`を返します。

        Example
        -------
        "固有名詞", "自立", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__pos1

    __pos2: Optional[str]

    @property
    def pos2(self) -> Optional[str]:
        """品詞細分類2

        Returns
        -------
        str | None
            形態素の品詞細分類2を文字列として返します。
            存在しない場合は`None`を返します。

        Example
        -------
        "地域", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__pos2

    __pos3: Optional[str]

    @property
    def pos3(self) -> Optional[str]:
        """品詞細分類3

        Returns
        -------
        str | None
            形態素の品詞細分類3を文字列として返します。
            存在しない場合は`None`を返します。

        Example
        -------
        "一般", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__pos3

    __conjugation_type: Optional[str]

    @property
    def conjugation_type(self) -> Optional[str]:
        """活用型

        Returns
        -------
        str | None
            形態素の活用型を文字列として返します。
            存在しない場合は`None`を返します。

        Example
        -------
        "五段・カ行促音便", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__conjugation_type

    __conjugation: Optional[str]

    @property
    def conjugation(self) -> Optional[str]:
        """活用形

        Returns
        -------
        str | None
            形態素の活用形を文字列として返します。
            存在しない場合は`None`を返します。

        Example
        -------
        "連用タ接続", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__conjugation

    __stem_form: Optional[str]

    @property
    def stem_form(self) -> Optional[str]:
        """原型

        Returns
        -------
        str | None
            形態素の原型を文字列として返します。
            存在しない場合は`None`を返します。

        Example
        -------
        "渋谷", "行く", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__stem_form

    __pronunciation: Optional[str]

    @property
    def pronunciation(self) -> Optional[str]:
        """発音

        Returns
        -------
        str | None
            形態素の発音をカタカナ表記の文字列として返します。
            存在しない場合は`None`を返します。

        Example
        -------
        "シブヤ", "イッ", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__pronunciation

    __unknown: Optional[str]

    @property
    def unknown(self) -> Optional[str]:
        """不明な値

        Returns
        -------
        str | None
            要素を分類できなかった場合に、MeCabの結果のfeature部分を文字列として返します。
            通常は`None`を返します。

        Example
        -------
        "名詞,固有名詞,地域,一般,*,*,渋谷,シブヤ,シブヤ", None

        格納される値は使用する辞書によって異なります。
        """
        return self.__unknown
