#!/usr/local/bin/python

import os
import glob

TARGET_DIR = "<insert your root dir here>"

def main():
    if TARGET_DIR == "<insert your root dir here>":
        print('Please insert a targer dir.')
        return

    if os == 'nt':
        files = glob.glob(TARGET_DIR + '\\**\\*.md', recursive=True)
    else:
        files = glob.glob(TARGET_DIR + '/**/*.md', recursive=True)

    if os == 'nt':
        outFile = open(TARGET_DIR + '\\' + 'AllInOne.md', 'w+')
    else:
        outFile = open(TARGET_DIR + '/' + 'AllInOne.md', 'w+')

    for file in files:
        inFile = open(file)
        outFile.write(str(inFile.read()))
        outFile.write('\n' + '----' + '\n')

if __name__ == "__main__":
    main()