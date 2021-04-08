# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


def encrypt(plaintext, options):
    print('Encrypting...')


def decrypt(ciphertext, options):
    print('Decrypting...')


def get_file_content(path):
    handler = open(path, 'r')
    return handler.readline()


def parse_file_content(content):
    args = content.split(':')
    shift_count = args[0]
    operation = args[1]
    language_code = args[2]
    text = args[3]

    if language_code == '0':
        language = 'english'
    elif language_code == '1':
        language = 'french'
    elif language_code == '2':
        language = 'spanish'
    else:
        language = 'turkish'

    return {'shift_count': int(shift_count), 'operation': operation, 'language': language, 'text': text}


def run():
    file_path = sys.argv[1]
    file_contents = get_file_content(file_path)
    result = parse_file_content(file_contents)
    # print('text is: ' + result['text'])

    operation = result['operation']
    shift_count = result['shift_count']
    language_file_path = './' + result['language'] + '.txt'
    language_file_content = get_file_content(language_file_path)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
