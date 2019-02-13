#!/usr/bin/python
import sys
import re


def doesFileExist(filename):

    try:
        file_handler=open(filename, 'r')
    except IOError:
        print('Make sure the file exists: ' + filename)
    else:
        return file_handler


def splitData(fileprocess):

    for line in fileprocess:
        word = re.match(r'(.*) - (.*)', line)
        if word:
            print(word.group(1))
            meaning = re.match(r'(.*) - (.*),(.*)', line)
            if meaning:
                moremeanings = re.match(r'(.*) - (.*),(.*),(.*)', line)
                if moremeanings:
                    print(moremeanings.group(2))
                    print(moremeanings.group(3))
                    print(moremeanings.group(4) + '\n')
                else:
                    print(meaning.group(2))
                    print(meaning.group(3) + '\n')
            else:
                print(word.group(2) + '\n')
        else:
            print('No word definition found at this line' + '\n')


def main():

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
        print('File analysis begin: ' + input_file +'\n')
        file_to_process=doesFileExist(input_file)
        splitData(file_to_process)
        file_to_process.close()
    else:
        print('Please provide a filename as first argument')


if __name__ == '__main__':
    main()