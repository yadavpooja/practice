def make_out_word(out, word):
    return out[:2] + word + out[2:4]



print make_out_word('<<>>', 'yay')
print make_out_word('<<>>', 'hii')
print make_out_word('[[]]', 'word')
