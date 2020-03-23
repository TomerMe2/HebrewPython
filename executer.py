from reader import Program
import replacer
import expander
import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as fd:
        string_program = fd.read()
    prgrm = Program(string_program)
    shifted_prgrm = replacer.replace(prgrm)
    new_string = expander.prgrm_to_text(shifted_prgrm)
    print(new_string)
    print('\n')
    exec(new_string)