from sys import argv
OpcodeBitSize = 4

Operator1Size = 4
Operator2Size = 0 # leave at 0 for no second operator

AccSize = 4
MemCellSize = 4
MemAddressSize = 4

"""
syntax = {
    'while',
    'if',
    'else',

    'true',
    'false'
}"""

subThings = [
    ';',

    '{',
    '}',

    '(',
    ')',

    '"',
    "'"
]

lines = []

infile = open(argv[1])
while (line := infile.readline()):
    lines.append(line)

tokens = []

for line in lines:
    token = ""
    for char in line:
        if char.isspace() or char in subThings:
            if token:
                tokens.append(token)
                token = ""
            if char in subThings:
                tokens.append(char)
        else:
            token += char
    if token:
        tokens.append(token)

print(tokens)
