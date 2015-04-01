from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):
    def __init__(self, input):
        self.input = input  # Lexer object
        self.markers = []  # Stack of index markers into lookahead buffer
        self.lookahead = []  # Lookahead tokens
        self.p = 0  # Index of current lookahead token

    def consume(self):
        """
        Consume one token
        """
        self.p += 1

        # Check if it reached to the end of the buffer (when not backtracking)
        if self.p == len(self.lookahead) and not self.isSpeculating():
            self.p = 0
            self.lookahead = []  # Initialize lookahead tokens

        self.sync(1)

    def sync(self, i):
        """
        Make sure to have i tokens from current position `self.p`
        """
        # Check if the number of the lookahead tokens is enough
        if self.p + i - 1 > (len(self.lookahead) - 1):
            n = (self.p + i - 1) - (len(self.lookahead) - 1)
            self.fill(n)

    def fill(self, n):
        """
        Put n tokens to the lookahead variable
        """
        for i in range(n):
            self.lookahead.append(self.input.next_token())

    def LT(self, i):
        """
        Return the i-th token (from `self.p`)
        """
        self.sync(i)
        return self.lookahead[self.p + i - 1]

    def LA(self, i):
        """
        Return the kind of the i-th token (from `self.p`)
        """
        return self.LT(i).kind

    def match(self, x):
        """
        Consume if `x` matches the lookahead token
        """
        if self.LA(1) == x:
            self.consume()
        else:
            raise Exception("exception %s; %s" % (self.input.get_token_name(x), self.lookahead))

    def mark(self):
        """
        Save current `self.p` to the markers list
        """
        self.markers.append(self.p)
        return self.p

    def release(self):
        """
        Pop one saved marker and seek to the position
        """
        marker = self.markers.pop()
        self.seek(marker)

    def seek(self, index):
        """
        Change current `self.p` to `index`
        """
        self.p = index

    def isSpeculating(self):
        """
        Return if it's speculating
        """
        return 0 < len(self.markers)
