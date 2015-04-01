from parser import Parser
from backtracklexer import BacktrackLexer


class BacktrackParser(Parser):
    def __init__(self, input):
        self.list_memo = {}
        super(BacktrackParser, self).__init__(input)

    def clear_memo(self):
        self.list_memo.clear()

    def stat(self):
        """
        stat : list EOF | assign EOF ;
        """
        if self.speculate_stat_alt1():  # Attempt alternative 1: list EOF
            self.list()
            self.match(BacktrackLexer.EOF_KIND)
        elif self.speculate_stat_alt2():  # Attempt alternative 2: assign EOF
            self.assign()
            self.match(BacktrackLexer.EOF_KIND)
        else:
            raise Exception("expecting stat, but found (%s)" % (self.LT(1)))

    def speculate_stat_alt1(self):
        """
        Trying "list EOF" branch
        """
        self.mark()  # Mark current position so that it can rewind
        success = True
        try:
            self.list()
            self.match(BacktrackLexer.EOF_KIND)
        except Exception:
            success = False
        self.release()  # Rewind anyway
        return success

    def speculate_stat_alt2(self):
        """
        Trying "assign EOF" branch
        """
        self.mark()  # Mark current position so that it can rewind
        success = True
        try:
            self.assign()
            self.match(BacktrackLexer.EOF_KIND)
        except Exception:
            success = False
        self.release()  # Rewind anyway
        return success

    def assign(self):
        """
        assign : list '=' list
        """
        self.list()
        self.match(BacktrackLexer.EQUALS)
        self.list()

    def list(self):
        """
        list : '[' elements ']'
        """
        self.match(BacktrackLexer.LBRACK)
        self.elements()
        self.match(BacktrackLexer.RBRACK)

    def elements(self):
        """
        elements : element (',' element)*
        """
        self.element()
        while self.LA(1) == BacktrackLexer.COMMA:
            self.match(BacktrackLexer.COMMA)
            self.element()

    def element(self):
        """
        element : name '=' NAME | NAME | list
        """
        if self.LA(1) == BacktrackLexer.NAME and self.LA(2) == BacktrackLexer.EQUALS:
            self.match(BacktrackLexer.NAME)
            self.match(BacktrackLexer.EQUALS)
            self.match(BacktrackLexer.NAME)
        elif self.LA(1) == BacktrackLexer.NAME:
            self.match(BacktrackLexer.NAME)
        elif self.LA(1) == BacktrackLexer.LBRACK:
            self.list()
        else:
            raise Exception("expecting element, but found " + self.LT(1))
