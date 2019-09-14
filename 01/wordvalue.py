from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    text_file = open(DICTIONARY)
    lines = text_file.readlines()
    post = [line.rstrip('\n') for line in lines]
    text_file.close()
    return post


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    count = 0
    for letter in word:
        if letter is not '-':
            count += LETTER_SCORES[letter.upper()]
    return count


def max_word_value(arr=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    count = 0
    max_word = None
    if not arr:
        default_dict = load_words()
        for word in default_dict:
            current_word_count = calc_word_value(word)
            if current_word_count > count:
                max_word = word
                count = current_word_count
    else:
        for word in arr:
            current_word_count = calc_word_value(word)
            if current_word_count > count:
                max_word = word
                count = current_word_count
    return max_word


if __name__ == "__main__":
    pass  # run unittests to validate
