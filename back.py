import random
def get(list): return random.choice(list)
def split(word):
    return [char for char in word]
def check(string, word):
    xstring = split(string.lower())
    xword = split(word.lower())
    if len(string) != len(word): return False
    for i in range(len(string)):
        if xstring[i] in xword:
            if xstring[i] == xword[i]: xstring[i] = "\u001b[42;1m" + xstring[i]
            elif xstring[i] in word: xstring[i] = "\u001b[43;1m" + xstring[i]
        else: xstring[i] = "\u001b[40;1m" + xstring[i]
    
    return "".join(xstring) + "\u001b[0m"

