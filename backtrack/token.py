class Token(object):
    TOKEN_NAMES = ["n/a", "<EOF>", "NAME", "COMMA", "LBRACK", "RBRACK"]

    def __init__(self, kind, text):
        self.kind = kind
        self.text = text

    def __str__(self):
        return '<"%s", %s>' % (self.text, self.TOKEN_NAMES[self.kind])
