import re


class BadWordsRemover:
    def __init__(self, bad_words_filename='bad_words.txt'):
        with open(bad_words_filename, encoding='utf-8') as f:
            self.bad_words = f.read().splitlines()
        print(f'bad words list\n{self.bad_words}')

    def func_to_remove_bad_words(self, match):
        input_str = match.group()
        if input_str.lower().strip() not in self.bad_words:
            return input_str
        else:
            return ''

    def remove_bad_words(self, input_string):
        result = re.sub(r'\w+\s?', self.func_to_remove_bad_words, input_string)
        return result


bad_words_remover = BadWordsRemover('bad_words.txt')
result = bad_words_remover.remove_bad_words('негры или  пидарасы')
print(f'result string is\n{result}')
