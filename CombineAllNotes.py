#!/usr/local/bin/python

import os
import glob

TARGET_DIR = "<insert your root dir here>"

def get_target_dir():
    if TARGET_DIR == "<insert your root dir here>":
        print('TARGET DIRECTORY:')
        target_dir = input()
    else:
        target_dir = TARGET_DIR
    return target_dir

def get_files(target_dir):
    # Get all files
    if os == 'nt':
        files = glob.glob(target_dir + '\\**\\*.md', recursive=True)
    else:
        files = glob.glob(target_dir + '/**/*.md', recursive=True)
    return files

def get_outfile(target_dir):
    if os == 'nt':
        outFile = open(target_dir + '\\' + 'AllInOne.md', 'w+')
    else:
        outFile = open(target_dir + '/' + 'AllInOne.md', 'w+')
    return outFile

def main():
    print('TARGET_DIR = ' + str(TARGET_DIR))
    target_dir = get_target_dir()
    files = get_files(target_dir)
    outfile = get_outfile(target_dir)

    for file in files:
        inFile = open(file)
        outfile.write(str(inFile.read()))
        outfile.write('\n' + '----' + '\n')

if __name__ == "__main__":
    main()