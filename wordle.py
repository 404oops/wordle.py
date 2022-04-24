import json
import sys

with open('wordlist.json', 'r') as file: wordlists = json.load(file)

def read():
    read = input()
    sys.stdout.write("\033[F")
    return read

import back
word = back.get(wordlists)

for i in range(5):
    check = back.check(read(), word)
    print(check)
print("The word was:", word)