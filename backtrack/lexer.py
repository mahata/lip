from abc import ABCMeta, abstractmethod


class Lexer(metaclass=ABCMeta):
    EOF = "\0"
    EOF_KIND = 1

    def __init__(self, input):
        """
        input: str
        """
        self.input = input
        self.c = input[0]
        self.p = 0

    def consume(self):
        self.p += 1
        if len(self.input) <= self.p:
            self.c = self.EOF
        else:
            self.c = self.input[self.p]

    def match(x):
        if self.c == x:
            self.consume()
        else:
            raise Error("expecting %s; found %s" % (x, self.c))

    @abstractmethod
    def next_token(self):
        raise NotImplementedError("next_token() is not implemented.")

    @abstractmethod
    def get_token_name(self, token_kind):
        raise NotImplementedError("get_token_name() is not implemented.")
