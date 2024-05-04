from argparse import ArgumentParser
from enum import Enum


OPERATORS = {
    "+": "ADD",
    "-": "SUBTRACT",
    "=": "ASSIGN",
    "*": "MULTIPLY",
    "/": "DIVIDE",
}

SYMBOLS = {
    "(": "OPAREN",
    ")": "CPAREN"
}


def parseArgs():
    parser = ArgumentParser()
    parser.add_argument('input', help='Input file')
    parser.add_argument(
        '-o', '--output', help='Output file', default='output.txt')
    return parser.parse_args()


def readInputFile(inputFile):
    with open(inputFile, 'r') as file:
        return file.read()


def printTable(table):
    print("Value\tType")
    for row in table:
        print(f"{row.get('value')}\t{row.get('type')}")


def isNumber(s: str):
    hasMaxOneDot = s.count(".") <= 1
    charsAreNumeric = s.replace(".", "").isnumeric()
    return hasMaxOneDot and charsAreNumeric


def isFloat(s: str):
    hasOneDot = s.count(".") == 1
    charsAreNumeric = s.replace(".", "").isnumeric()
    return hasOneDot and charsAreNumeric


def isInt(s: str):
    charsAreNumeric = s.isnumeric()
    return charsAreNumeric


def isOperator(s: str):
    inOperators = s in OPERATORS
    return inOperators


def isSymbol(s: str):
    inSymbols = s in SYMBOLS
    return inSymbols


def isIdentifier(s: str):
    isAnOperator = isOperator(s)
    isFirstCharNum = s[0].isnumeric()
    isRestAlphaNum = s[0:len(s)].isalnum()
    return not isAnOperator and not isFirstCharNum and isRestAlphaNum


class Tokens:
    def __init__(self):
        self.tokens = []

    def add(self, value: str, type: str):
        self.tokens.append({"value": value, "type": type})

    def get(self):
        return self.tokens


def main():
    args = parseArgs()

    contents = readInputFile(args.input)
    i, j = 0, 0

    tokens = Tokens()

    while i < len(contents) and j < len(contents):
        substr = contents[i:j + 1]
        if isOperator(substr):
            # if we are an identifier, don't expand. just add the value
            tokens.add(substr, OPERATORS[substr])
            i += 1
            j = i
            continue

        if isSymbol(substr):
            # if we are a symbol, don't expand. just add the value
            tokens.add(substr, SYMBOLS[substr])
            i += 1
            j = i
            continue

        if isNumber(substr):
            # if we are a number, expand as far as you can
            while isNumber(substr) and j < len(contents):
                j += 1
                substr = contents[i:j + 1]
            # once we are no longer a number, go back one j
            j -= 1
            substr = contents[i:j + 1]

            if isInt(substr):
                tokens.add(substr, "INT")
            if isFloat(substr):
                tokens.add(substr, "FLOAT")

            # move our pointers to char after j
            i = j + 1
            j = i
            continue

        if isIdentifier(substr):
            # if we are an identifier, expand as far as we can
            while isIdentifier(substr) and j < len(contents):
                j += 1
                substr = contents[i:j + 1]

            # once we are no longer an identifier
            j -= 1
            substr = contents[i:j + 1]
            tokens.add(substr, "IDENTIFIER")

            # move our pointer to char after j
            i = j + 1
            j = i
            continue

        # if we don't match anything move the pointer and ignore
        i += 1
        j += 1

    printTable(tokens.get())


if __name__ == '__main__':
    main()
