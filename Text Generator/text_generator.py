import re

from nltk import WhitespaceTokenizer, bigrams,trigrams
from collections import Counter
import random


def tokenize(corpus):
    with open(corpus, "r") as f:
        text = f.read()
        return WhitespaceTokenizer().tokenize(text)


def generate_bigrams(tokens):
    bigrams_ = trigrams(tokens)
    bigrams_list = [' '.join(x) for x in bigrams_]
    return bigrams_list


def generate_dictionary(list_of_bigrams):
    new_dict = {}
    for word in list_of_bigrams:
        new_dict.setdefault(word[0], []).append(word[1])
    return new_dict


def is_starting_word(word):
    starting_word_template = "^[A-Z]+[a-z']+[^.?!]$"
    return bool(re.match(starting_word_template, word))


def is_ending_word(word):
    ending_word_template = ".*[.?!]"
    return bool(re.match(ending_word_template, word))


filename = input()
list_of_tokens = tokenize(filename)
bigrams_in_corpus = generate_bigrams(list_of_tokens)
try:
    lst = [(obj.split()[0], obj.split()[1]) for obj in bigrams_in_corpus]
    data = generate_dictionary(lst)
    starting_words = [word for word in list_of_tokens if is_starting_word(word)]
    for i in range(10):
        sentence = list()
        first_word = random.choice(starting_words)
        sentence.append(first_word)
        while True:
            tail = data[first_word]
            freq_tail = Counter(tail)
            tail_weights = [freq_tail[value] for value in tail]
            second_word = ''.join(random.choices(tail, weights=tail_weights))
            sentence.append(second_word)
            first_word = second_word
            if is_ending_word(sentence[-1]) and len(sentence) >= 5:
                break
        print(" ".join(sentence))

except KeyError:
    print('Key Error. The requested word is not in the model. Please input another word.')
