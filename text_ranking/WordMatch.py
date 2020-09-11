import os
from enc.gematria import gematria
import functools


class WordMatch(object):
    '''
        Use this test when deciding if decrypted words are "real.'

        There are many ways these methods could be made more sophisticated.

        Load in crib words These **MUST** be in consecutive rune length, with no gaps,
        convert cribs to forward Gematria position.

        Then,
        Compare passed word to crib words and get min number of char difference (0 means
        word is a real word).
        or
        find if passed word has <= requested number of char differences.

        These scores provide another way to cut adn rank decrypted plaintext,

        The min char difference is designed to allow some wiggle room, e.g. 75% of a correct
        answer might still be worth investigating, as we know there are  potential typos,
        interrupters, and maybe other tricks.

        Tuning this wiggle room is up for experimentation.
    '''
    # the usual gematria object
    gem = gematria()

    ''' files that contain lists of words you think are in the LP, '''
    cribfiles = ["mycribs1.txt", "mycribs2.txt", "mycribs3.txt", "mycribs4.txt", "mycribs5.txt",
                 "mycribs6.txt", "mycribs7.txt", "mycribs8.txt"]
    max_crib_length = len(cribfiles)
    criblist = []
    for cribs in cribfiles:
        print(cribs)
        with open(os.path.join(os.getcwd(), 'data', 'word_lists', cribs), 'r',
                  encoding="utf8") as f:
            data = f.read().replace('\n', '').split()
            temp = []
            for word in data:
                temp.append(gem.encode_as_forward_position(gem.translate_to_gematria(word)))
        criblist.append(temp)

    def get_char_dif(self, word):
        '''
            Find the the min number of chars that are different to words in a criblist e.g
            0 means there is zero char differences between word and a word in the criblist
            1 means there is one  char differences between word and a word in the criblist, etc.
        :param word: a word, in runes as forward position
        :return: the best match (i.e, the min number of chars that are different to words in the
        list
                 (or 0 for words longer than we have data for)
        '''
        word_len = len(word)
        if word_len > WordMatch.max_crib_length:
            return 0
        cribs = WordMatch.criblist[word_len - 1]
        best_score = word_len
        for crib in cribs:
            match_char = sum([1 for (x1, x2) in zip(word, crib) if abs(x1 - x2) == 0])
            score = (word_len - match_char)

            if score == 0:
                return 0
            elif score < best_score:
                best_score = score
        return best_score

    def is_char_dif_good_enough(self, word, enough):
        '''
            check word char dif until the 'enough' value is found, then return True, otherwise False
        :param word: a word, in runes as forward position
        :param enough: integer, char diff required to accept result without further checking
        :return: the best match (i.e, the min number of chars that are different to words in the
        list
                 (or 0 for words longer than we have data for)
        '''
        word_len = len(word)
        if word_len > WordMatch.max_crib_length:
            return 0
        cribs = WordMatch.criblist[word_len - 1]
        for crib in cribs:
            match_char = sum([1 for (x1, x2) in zip(word, crib) if abs(x1 - x2) == 0])
            score = (word_len - match_char)
            if score <= enough:
                return True
        return False

    @functools.lru_cache(maxsize=None)
    def is_word_char_dif_good_enough(self, word, required_score):
        '''
            get the char diff between passed words and crib word, then check if its below the
            required_score
        :param word: word to check (encoded in forward postion runes)
        :param required_score: max score
        :return: True if char diff is <= required_score
        '''
        if self.is_char_dif_good_enough(word, required_score):
            return [len(word), required_score, True]
        return [len(word), required_score, False]
