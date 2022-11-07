from dataclasses import dataclass
from typing import Optional
import MeCab


@dataclass
class Morph:
    word: str


class MeCabAgent:
    def __init__(self) -> None:
        self.tagger: MeCab.Tagger = MeCab.Tagger()
        self.input: str = ''
        self.results: list[Morph] = []  # List of results from MeCab

    def parse(self, sentence: Optional[str] = None) -> list[str]:
        """Parse single sentence by using MeCab.

        Parameters
        ----------
        sentence : str, optional
            A single line string that you want to
            input to MeCab. Default to None.

        Returns
        -------
        list[str]
            Result
        """
        ret: list[str] = []
        if sentence is not None:
            self.input = sentence
        words: list[str] = self.tagger.parse(self.input).split('\n')
        words.remove('EOS')
        words.remove('')
        print(words)
        for w in words:
            surface, others = w.split('\t')
            info = others.split(',')
            print(info)
            ret.append(surface)
        return ret


if __name__ == '__main__':
    mgr = MeCabAgent()
    print(mgr.parse("犬と犬がぶつかる"))
