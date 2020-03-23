

class Token:
    def __init__(self, string):
        self.str = string


class Line:
    def __init__(self, line_string='', list_of_tokens=None):
        if line_string != '':
            toks = []
            string_buffer = ''
            quote_type = ''
            starting_quotes = False
            for string in line_string.split(' '):
                if '"' in string:
                    quote_type = '"'
                    starting_quotes = True
                elif "'" in string:
                    quote_type = "'"
                    starting_quotes = True
                if string_buffer == '':
                    toks.append(Token(string))
                else:
                    string_buffer += string
                    if quote_type in string and not starting_quotes:
                        # ending quotes!
                        toks.append(Token(string_buffer))
                        string_buffer = ''

            self.tokens = [Token(string) for string in Line.split(line_string)]
        elif list_of_tokens is not None:
            self.tokens = list_of_tokens
        else:
            self.tokens = []

    @staticmethod
    def split(string):
        """
        splits a string in a way that a string remains in the same element, and space splits elements
        """
        buffer = ''
        quotes_type = ''
        lst = []
        for char in string:
            # check that we are not inside quotes
            if quotes_type == '':
                if char == ' ':
                    lst.append(buffer)
                    buffer = ''
                else:
                    buffer += str(char)
                if char == '"' or char == "'":
                    quotes_type = char
            else:
                buffer += str(char)
                if char == quotes_type:
                    # end quotes!
                    lst.append(buffer)
                    buffer = ''
        if buffer != '':
            lst.append(buffer)
        return lst


class Program:
    def __init__(self, program_string='', list_of_lines=None):
        if program_string != '':
            self.lines = [Line(line_string) for line_string in program_string.split('\n')]
        elif list_of_lines is not None:
            self.lines = list_of_lines
        else:
            self.lines = []


def read_file(file_path):
    with open(file_path, 'r') as fd:
        program_string = fd.read()
    return Program(program_string)