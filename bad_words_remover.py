import re

input_string = 'негры пидарасы'
bad_words_filename = 'bad_words.txt'
with open(bad_words_filename, encoding='utf-8') as f:
    bad_words = f.read().splitlines()

print(f'bad words list\n{bad_words}')
print(f'input string\n{input_string}')


def func_to_remove_bad_words(match):
    input_str = match.group()
    if input_str.lower().strip() not in bad_words:
        return input_str
    else:
        return ''


result = re.sub(r'\w+\s?', func_to_remove_bad_words, input_string)
print(f'resulting string\n{result}')
