def prgrm_to_text(prgrm):
    str_lines = []
    for line in prgrm.lines:
        str_toks = [tok.str for tok in line.tokens]
        str_lines.append(' '.join(str_toks))
    return '\n'.join(str_lines)
