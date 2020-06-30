# The role of the lexer is to take the program and convert it to tokens

from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Left Paren
        self.lexer.add('OPEN_PAREN', r'\(')
        # Right Paren
        self.lexer.add('CLOSE_PAREN', r'\)')
        # semi-colon (line end)
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Numbers
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()