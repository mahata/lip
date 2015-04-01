from lexer import Lexer
from token import Token


class BacktrackLexer(Lexer):
    NAME = 2
    COMMA = 3
    LBRACK = 4
    RBRACK = 5
    EQUALS = 6

    def __init__(self, input):
        super(BacktrackLexer, self).__init__(input)

    def get_token_name(self, x):
        # return self.TOKEN_NAMES[x]
        return Token.TOKEN_NAMES[x]

    def next_token(self):
        while self.c != Lexer.EOF:
            if self.c == " " or self.c == "\t" or self.c == "\n" or self.c == "\r":
                self._ws()
                continue
            elif self.c == ",":
                self.consume()
                return Token(self.COMMA, ",")
            elif self.c == "[":
                self.consume()
                return Token(self.LBRACK, "[")
            elif self.c == "]":
                self.consume()
                return Token(self.RBRACK, "]")
            elif self.c == "=":
                self.consume()
                return Token(self.EQUALS, "=")
            else:
                if self.c.isalpha():
                    return self._name()
                raise Exception("invalid character: %s" % (self.c))

        return Token(self.EOF_KIND, "<EOF>")

    def _name(self):
        buf = []
        while True:
            buf.append(self.c)
            self.consume()
            if not self.c.isalpha():
                break

        return Token(self.NAME, "".join(buf))

    def _ws(self):
        while self.c == " " or self.c == "\t" or self.c == "\n" or self.c == "\r":
            self.consume()
