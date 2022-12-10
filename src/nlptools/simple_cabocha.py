"""係り受け解析ツールCaboChaを簡単に扱えるようにするモジュールです。
Requirements
------------
- Python 3.6 以上の32bit版でのみ動作します。
- コンピュータに CaboCha がインストールされている必要があります。
- cabocha-python ライブラリが必要です。
"""
from typing import Dict
import CaboCha


class CaboChaHelper:
    def __init__(self, args: str = '') -> None:
        self._cabocha = CaboCha.Parser(str)

    def parse(self, setntence: str) -> Dict[str, str]:
        self.result_xml = self._cabocha.parse(setntence)
        self.result_xml.toString(CaboCha.CABOCHA_FORMAT_XML)
        # TODO: Implemens xml parser
        return {}
