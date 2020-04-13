from reader import Token, Line, Program

keywords = {'הגדר': 'def',
            'שקר': 'False',
            'אמת': 'True',
            'אם': 'if',
            'אחרת': 'else',
            'וגם': 'and',
            'או': 'or',
            'לא': 'not',
            'כלום': 'None',
            'הוא': 'is',
            'הפסק': 'break',
            'החזר': 'return',
            'עבור': 'for',
            'כלעוד': 'while',
            'בתוך': 'in',
            'הצג': 'print',
            'קלוט': 'input',
            'שלם': 'int',
            'ממשי': 'float',
            'מרוכב': 'complex',
            'מחרוזת': 'str',
            'מילון': 'dict',
            'רשימה': 'list',
            'קבוצה': 'set',
            'טווח': 'range'}


def replace(prgrm):
    def translate_tok_str(tok_str):
        before_strip, stripped, after_strip = strip(tok_str)
        # if stripped == '':
        #    return ''
        if tok_str.startswith('"') or tok_str.startswith("'"):
            return tok_str
        if stripped in keywords:
            return before_strip + keywords[stripped] + translate_tok_str(after_strip)
            # new_tok = Token(before_strip + keywords[stripped] + after_strip)
            # return new_tok
        else:
            return english_for_non_keyword(tok_str)

    new_lines = []
    for line in prgrm.lines:
        new_toks = []
        for tok in line.tokens:
            new_toks.append(Token(translate_tok_str(tok.str)))
        new_lines.append(Line(list_of_tokens=new_toks))
    return Program(list_of_lines=new_lines)


def english_for_non_keyword(string):
    new_str = ''
    diff_small_letter = ord('א') - ord('a')
    for char in string:
        if 'ש' >= char >= 'א':
            new_chr = chr(ord(char) - diff_small_letter)
            new_str += str(new_chr)
        elif char == 'ת':
            new_str += 'A'
        else:
            new_str += str(char)
    return new_str


def get_whitespace(string):
    whitespace_str = ''
    for char in string:
        if char != '\t' and char != ' ':
            break
        whitespace_str += str(char)
    return whitespace_str


def strip(string):
    stripped = ''
    before_strip = ''
    after_strip = ''
    step = 0   # 0 for before_strip, 1 for stripped and 2 for after_strip
    for char in string:
        if step == 1 and (char == '(' or char == ':'):
            step = 2
        if step == 0 and char != '\t' and char != ' ' and char != '(':
            step = 1
        if step == 0:
            before_strip += str(char)
        elif step == 1:
            stripped += str(char)
        elif step == 2:
            after_strip += str(char)
    return before_strip, stripped, after_strip


