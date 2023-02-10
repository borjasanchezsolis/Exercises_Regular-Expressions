import sys
import re

def main():
    print(count(input('Text: ')))



def count(s):
    find_um = re.findall(r'\b\W*um\W*', s, re.IGNORECASE)    # \b is the boundary between a \w and a \W character  (\W represents a character that its not alphabetical)
    return len(find_um)


if __name__ == '__main__':
    main()