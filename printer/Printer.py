
class Printer:

    def __init__(self):
        self.source = ''
        self.indent_level = 0
        self.indent = '    '
        self.newline = '\n'

    def print(self, str):
        for i in range(self.indent_level):
            self.source += self.indent
        self.source += str

    def indent(self):
        self.indent_level += 1

    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1
        else:
            raise Exception('Error: indent level cannot go below 0')

    def get_source(self):
        return self.source