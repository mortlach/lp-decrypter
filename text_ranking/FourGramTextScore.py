import csv
import os
from enc import gematria
from collections import namedtuple

# todo is this all the data that is needed ??
#
TextScoreResults = namedtuple('TextScoreResults',
                              'total_score score_per_ngram min_score_count ngram_count rejected')


class FourGramTextScore(object):
    '''
        FourGramTextScore can take a passed list of numbers and return the 4gram log prob score
        the 4 gram log prob scores are held in a dict four_gram_probability_runes
        four_gram_probability_runes returns two values (count, score)
        the count is the number of occurrences of teh 4gram in project Guttenburg
        the score is the log probability of that count

        The results can be cropped (cropping helps reduce noise, but may crop the correct
        answer!

        counts are cropped, a min_count can be specified, and results with less counts are scored
        as min_score.

        The scores for a phrase can also be cropped. this is achieved by comparing the total
        phrase, with a straight line defining score per n-gram + offset.

        In offline tests a linear model for  "score pre n-gram " has looked reasonable
    '''

    ''' import data '''
    gem = gematria.gematria()  # gematria object
    four_gram_probabilty_runes = {}
    with open(os.path.join('4gram_probability', "4GramProbabilityData.csv"), 'r',
              encoding="utf8") as f:
        reader = csv.reader(f)
        for k, v1, v2 in reader:
            four_gram_probabilty_runes[k] = tuple(
                [int(v1), float(v2)])  # print(  # four_gram_probabilty_runes[k])

    four_gram_probabilty_pos = {}
    for key, value in four_gram_probabilty_runes.items():
        chars = list(key)
        positions = tuple(gem.encode_as_forward_position(chars))
        four_gram_probabilty_pos[
            positions] = value  # print(four_gram_probabilty_pos[   # positions ])

    def __init__(self):
        pass

    def get_4gram_log_prob_pos(self, pos_tuple, min_counts, min_score):
        '''
        get 4gram log probability score for a passed tuple of runes as normal gematria positions
        :param pos_tuple: tuple, in positions, to get log prob score
        :param min_counts: the min counts the entry must have to return real core
        :param min_score: score to return if counts i < min_counts or
        :return: score
        '''
        # print("get_4gram_log_prob_pos, pos_tuple = ", pos_tuple)
        # print("get_4gram_log_prob_pos, min_counts = ", min_counts)
        # print("get_4gram_log_prob_pos, min_score = ", min_score)
        ans = FourGramTextScore.four_gram_probabilty_pos.get(pos_tuple, [0, min_score])
        # print("ans = ", ans)
        # print("get_4gram_log_prob_pos ", ans)
        if ans[0] < min_counts:
            return min_score
        # print(" ans[0] !<  ", min_counts)
        return ans[1]

    def get_pos_phrase_log_prob_with_min_count(self, four_gram, min_counts, min_score,
                                               min_score_per_4gram_gradient,
                                               min_score_per_4gram_offset):
        """
            score the passed phrase, with a cut on the amount of counts
        :param four_gram: passed 4-gram in numbers
        :param min_counts: min counts in data to be accepted, otherwise min_score returned
        :param min_score: min_score to return if phrase does not exist or has counts below
        min_counts
        :return: log probability score for phrase
        """
        # print("min_counts= ",min_counts)
        # print("min_score= ",min_score)
        score = 0.0
        min_score_count = 0
        num_ngrams = len(four_gram) - 3
        for i in range(0, num_ngrams):
            new_score = self.get_4gram_log_prob_pos(tuple(four_gram[i:i + 4]), min_counts,
                                                    min_score)
            if new_score == min_score:
                min_score_count += 1
            score += new_score
        # is rejected
        rejected = False
        # print("score ", score)
        # print("min_score_per_4gram_gradient ", min_score_per_4gram_gradient)
        # print("min_score_per_4gram_offset ", min_score_per_4gram_offset)
        # print("num_ngrams ", num_ngrams)
        # print("min_score_per_4gram_gradient * num_ngrams + min_score_per_4gram_offset ",
        # min_score_per_4gram_gradient * num_ngrams + min_score_per_4gram_offset)
        if score < min_score_per_4gram_gradient * num_ngrams + min_score_per_4gram_offset:
            rejected = True

        return TextScoreResults(round(score, 4), round(score / num_ngrams, 4), min_score_count,
                                num_ngrams, rejected)
