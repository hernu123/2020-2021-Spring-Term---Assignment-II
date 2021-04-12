import sys


def generate_dict(arr, shift_count):
    dictionary = {}
    reverse_dictionary = {}
    list_length = len(arr)

    for index, alphabet in enumerate(arr):
        if index + shift_count <= list_length - 1:
            new_alphabet = arr[index + shift_count]
            dictionary[alphabet] = new_alphabet
            reverse_dictionary[new_alphabet] = alphabet
        else:
            overflow = index + shift_count
            new_index = overflow - list_length
            new_alphabet = arr[new_index]
            dictionary[alphabet] = new_alphabet
            reverse_dictionary[new_alphabet] = alphabet

    return dictionary, reverse_dictionary


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
    text = result['text']

    operation = result['operation']
    shift_count = result['shift_count']
    language_file_path = './' + result['language'] + '.txt'
    language_file_content = get_file_content(language_file_path)
    encrypt_dict, decrypt_dict = generate_dict(language_file_content.split(','), shift_count)

    if operation == '0':
        new_text = transform(text, encrypt_dict)
    else:
        new_text = transform(text, decrypt_dict)

    print(new_text)


def transform(text, dictionary):
    text_array = list(text)
    result_array = []

    for char in text_array:
        if char == ' ':
            result_array.append(' ')
        else:
            result_array.append(dictionary[char.lower()])

    return "".join(result_array)


# Press the green button in the gutter to run the script.

if name=='main':
    run()
