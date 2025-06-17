from sys import argv
OpcodeBitSize = 4

Operator1Size = 4
Operator2Size = 0 # leave at 0 for no second operator

AccSize = 4
MemCellSize = 4
MemAddressSize = 4


#INSTRUCTIONS:

JZopcode  = 0x1  # JZ,  x # PC <- x IF ACC = 0
ADDopcode = 0x2  # ADD, x # ACC <- ACC + MEM(x)
NOTopcode = 0x3  # NOT    # ACC <- NOT ACC
JMPopcode = 0x4  # JMP, x # PC <- ACC
LDRopcode = 0x5  # LDR, x # MEM(x) <- ACC
LDopcode  = 0x6  # LD,  x # ACC <- MEM(x)
LDIopcode = 0x7  # LDI, x # ACC <- x
LDPopcode = 0x8  # LDP, x # ACC <- MEM(MEM(x))

# I/O instructions; Required to use IO libary

OUTopcode = 0x9  # OUT  # ACC -> I/O
INopcode  = 0xA  # IN   # ACC <- I/O
COUTopcode= 0xB  # COUT # ACC -> I/O


def compileAdd(a, b):
    asm = [
        (LDIopcode, a),
        (LDRopcode, 1),
        (LDIopcode, b),
        (ADDopcode, 1),
        (LDRopcode, 2)
    ]
    return asm

def compileSub(a, b):
    asm = [
        (LDIopcode, a),
        (LDRopcode, 0),

        (LDIopcode, 0),
        
        (LDIopcode, b),
        (NOTopcode),
        (LDRopcode, 1),
        (LDIopcode, 0),
        (ADDopcode, 1),
        (LDRopcode, 1),
        (LDIopcode, a),
        (ADDopcode, 1),

        (ADDopcode, 0),
        (LDRopcode, 2)
    ]
    return asm

def compileAND(a, b):
    asm = [
        (LDIopcode, a),
        (NOTopcode),
        (LDPopcode, 0),
        (LDIopcode, b),
        (NOTopcode),
        (ADDopcode, 0),
        (NOTopcode)
    ]

def compileOR(a, b):
    asm = [
        (LDIopcode, a),
        (NOTopcode),
        (LDRopcode, 0),
        (LDIopcode, b),
        (NOTopcode),
        (ADDopcode, 0),
        (NOTopcode)
    ]

def compileNOT(a):
    asm = [
        (LDIopcode, a)
        (NOTopcode)
    ]
    return asm

def compileIF(a):
    pass

def compileWHILE(a):
    pass

subThings = [
    ';',

    '{',
    '}',

    '(',
    ')',

    '"',
    "'",

    '+',
    '-',

    '&&'
    '|'
    '!'
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
