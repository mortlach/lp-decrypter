#!/usr/bin/env python3
# simple gematria encoding
# thanks to 'solvers, and bb who started this many years ago
#
import re


class gematria(object):
    '''
        converting between text, runes and numbers,

        This is just general class i use, it needs  a thorough checking, and rationalizing

        probably different functions do the same thing,  or there are bizarre definitions

        this can all be tidied up and re-written ...

        hopefully function names make sense

        rune number definitions are somewhat arbitrary, but hopefully well accepted

        probably lots of speed improvements, these functions may be called a lot

        towards the end of this class are functions such as
        process_string_to_type_with_order_and_shift which are used with strings of a
        pre-determined format Use this convention from now on? maybe add to it by include entry
        in rune prime values
        (ambiguity for short texts?)

    '''
    lower = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', \
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    upper = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', \
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'

    all_orders = ["forward, reverse"]
    all_shifts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                  23, 24, 25, 26, 27, 28]

    runes = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛂ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ",
             "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]
    latin_fragments = ['F', 'U', 'TH', 'O', 'R', 'C', 'G', 'W', 'H', 'N', 'I', 'J', 'EO', 'P', 'X',
                       'S', 'T', 'B', 'E', 'M', 'L', 'ING', 'OE', 'D', 'A', 'AE', 'Y', 'IA',
                       'EA']  # arbitrarily chosen common choices

    rune_prime_values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                         73, 79, 83, 89, 97, 101, 103, 107,
                         109]  # arbitrarily chosen common choices
    bigram = ['TH', 'EO', 'NG', 'OE', 'AE', 'IA', 'IO',
              'EA']  # alternative letters that have more than  1 char, used for conversion of
    trgram = 'ING'
    # Todo: add in letters with diacritic marks here etc.
    rune_to_position_forward_dict = {}  # build dictionaries to convert runes to position in
    # gematria
    rune_to_position_reverse_dict = {}

    f = 0  # forward position offsets
    r = 28  # reverse position offsets
    for rune in runes:  # add in values for each rune
        rune_to_position_reverse_dict[rune] = r
        rune_to_position_forward_dict[rune] = f
        f += 1
        r -= 1

    f = 0
    r = 28
    for rune in latin_fragments:  # add in the latin fragments
        rune_to_position_reverse_dict[rune] = r
        rune_to_position_forward_dict[rune] = f
        rune_to_position_reverse_dict[rune.lower()] = r  # and lower case versions
        rune_to_position_forward_dict[rune.lower()] = f  # and lower case versions
        f += 1
        r -= 1

    rune_to_position_forward_dict["ᛄ"] = rune_to_position_forward_dict[
        "ᛂ"]  # sometimes ᛄ and ᛂ get confused
    rune_to_position_forward_dict["NG"] = rune_to_position_forward_dict[
        "ING"]  # alternative latin characters
    rune_to_position_forward_dict["Z"] = rune_to_position_forward_dict["S"]
    rune_to_position_forward_dict["IO"] = rune_to_position_forward_dict["IA"]
    rune_to_position_forward_dict["K"] = rune_to_position_forward_dict["C"]
    rune_to_position_forward_dict["V"] = rune_to_position_forward_dict["U"]
    rune_to_position_reverse_dict["NG"] = rune_to_position_reverse_dict["ING"]
    rune_to_position_reverse_dict["Z"] = rune_to_position_reverse_dict["S"]
    rune_to_position_reverse_dict["IO"] = rune_to_position_reverse_dict["IA"]
    rune_to_position_reverse_dict["K"] = rune_to_position_reverse_dict["C"]
    rune_to_position_reverse_dict["V"] = rune_to_position_reverse_dict["U"]
    rune_to_position_forward_dict["ng"] = rune_to_position_forward_dict[
        "ING"]  # lower case of above
    rune_to_position_forward_dict["z"] = rune_to_position_forward_dict["S"]
    rune_to_position_forward_dict["io"] = rune_to_position_forward_dict["IA"]
    rune_to_position_forward_dict["k"] = rune_to_position_forward_dict["C"]
    rune_to_position_forward_dict["v"] = rune_to_position_forward_dict["U"]
    rune_to_position_reverse_dict["ng"] = rune_to_position_reverse_dict["ING"]
    rune_to_position_reverse_dict["z"] = rune_to_position_reverse_dict["S"]
    rune_to_position_reverse_dict["io"] = rune_to_position_reverse_dict["IA"]
    rune_to_position_reverse_dict["k"] = rune_to_position_reverse_dict["C"]
    rune_to_position_reverse_dict["v"] = rune_to_position_reverse_dict["U"]

    position_to_latin_forward_dict = {}  # converting positions to latin forward
    position_to_latin_reverse_dict = {}  # converting positions to latin reverse
    position_to_rune_forward_dict = {}
    position_to_rune_reverse_dict = {}
    for pos in range(0, 29):
        position_to_latin_forward_dict[pos] = latin_fragments[pos]
        position_to_latin_reverse_dict[28 - pos] = latin_fragments[pos]
        position_to_rune_forward_dict[pos] = runes[pos]
        position_to_rune_reverse_dict[28 - pos] = runes[pos]

    # TODO could be better written andn neater, and not compete
    ''' some more dictionaries for converting between latin, runes, forward positions '''
    r2e = {}
    for i, j in zip(runes, latin_fragments):
        r2e[i] = j
    e2r = {}
    for i, j in zip(latin_fragments, runes):
        e2r[i] = j
    e2r["IO"] = e2r["IA"]
    e2r["K"] = e2r["C"]
    e2r["NG"] = e2r["ING"]
    e2r["Z"] = e2r["S"]
    e2r["Q"] = e2r["C"]
    e2r["V"] = e2r["U"]
    # for key in e2r.keys():
    #     e2r[key.lower()] = e2r[key]

    r2p = {}
    p2r = {}
    p2e = {}
    e2p = {}
    p2pr = {}
    r2pr = {}
    for i in range(0, 29):
        p2r[i] = runes[i]
        p2e[i] = latin_fragments[i]
        e2p[latin_fragments[i]] = i
        r2p[runes[i]] = i
        p2pr[i] = rune_prime_values[i]
        r2pr[runes[i]] = rune_prime_values[i]
    e2p["IO"] = e2p["IA"]
    e2p["K"] = e2p["C"]
    e2p["NG"] = e2p["ING"]
    e2p["Z"] = e2p["S"]
    e2p["Q"] = e2p["C"]
    e2p["V"] = e2p["U"]

    ''' and the same for rune primes '''
    r2pr = {}
    for i, j in zip(runes, rune_prime_values):
        r2pr[i] = j
    e2pr = {}
    for i, j in zip(latin_fragments, rune_prime_values):
        e2pr[i] = j
    e2pr["IO"] = e2pr["IA"]
    e2pr["K"] = e2pr["C"]
    e2pr["NG"] = e2pr["ING"]
    e2pr["Z"] = e2pr["S"]
    e2pr["Q"] = e2pr["C"]
    e2pr["V"] = e2pr["U"]
    # for key in e2pr.keys():
    #     e2pr[key.lower()] = e2pr[key]
    calculate_extended_positons = True  # extend positions values higher values to save

    # calculating mod when looking up

    def __init__(self):
        if gematria.calculate_extended_positons:
            print(__name__ + " Calculating extended positons")
            for pos in range(0, 2900):
                gematria.position_to_latin_forward_dict[pos] = \
                    gematria.position_to_latin_forward_dict[self.mod29(pos)]
                gematria.position_to_latin_reverse_dict[pos] = \
                    gematria.position_to_latin_reverse_dict[self.mod29(pos)]
                gematria.position_to_rune_forward_dict[pos] = \
                    gematria.position_to_rune_forward_dict[self.mod29(pos)]
                gematria.position_to_rune_reverse_dict[pos] = \
                    gematria.position_to_rune_reverse_dict[self.mod29(pos)]
            gematria.calculate_extended_positons = False

    def rune_to_prime_value(self, c):
        '''
            convert a char or char list to rune prime values
        '''
        try:
            return [gematria.r2pr.get(x, None) for x in c]
        except:
            pass
        try:
            return gematria.r2pr.get(c, None)
        except:
            return None

    def pos_to_eng(self, c):
        '''
            convert a forward pos or forward pos  list to rune_eng
        '''
        try:
            return [gematria.p2e.get(x, None) for x in c]
        except:
            pass
        try:
            return gematria.p2e.get(c, None)
        except:
            return None

    def pos_to_rune(self, c):
        '''
            convert a forward pos or forward pos  list to rune
        '''
        try:
            return [gematria.p2r.get(x, None) for x in c]
        except:
            pass
        try:
            return gematria.p2r.get(c, None)
        except:
            return None

    def eng_to_pos(self, c):
        '''
            convert a eng rune or eng rune list to forward pos
        '''
        try:
            return [gematria.e2p.get(x, None) for x in c]
        except:
            pass
        try:
            return gematria.e2p.get(c, None)
        except:
            return None

    def rune_to_pos(self, c):
        '''
            convert a rune or rune list to forward pos
        '''
        try:
            return [gematria.r2p.get(x, None) for x in c]
        except:
            pass
        try:
            return gematria.r2p.get(c, None)
        except:
            return None

    def eng_to_prime_value(self, c):
        '''
            convert a char or char list to rune prime values
        '''
        try:
            return [gematria.e2pr.get(x, None) for x in c]
        except:
            pass
        try:
            return gematria.e2pr.get(c, None)
        except:
            return None

    def eng_to_rune(self, c):
        '''
            convert a char or char list to runes
        '''
        try:
            return [gematria.e2r.get(x, None) for x in c]
        except:
            pass
        try:
            return gematria.e2r.get(c, None)
        except:
            return None

    def rune_to_eng(self, c):
        '''
            convert a char or char list to runes
        '''
        try:
            return [gematria.r2e.get(x, None) for x in c]
        except:
            pass
        try:
            return gematria.r2e.get(c, None)
        except:
            return None

    def translate_to_gematria(self, word):
        '''
            convert word standard english to runes (Latin), TODO no diacritics
        '''
        res = []
        skip = 0
        WORD = word.upper().replace("QU", "KW")
        WORD = WORD.replace("Q", "K")
        for i, val in enumerate(WORD):
            if skip:
                skip -= 1
                continue
            if WORD[i:i + 3] == gematria.trgram:
                res.append(gematria.trgram)
                skip += 2
                continue
            if WORD[i:i + 2] in gematria.bigram:
                res.append(WORD[i:i + 2])
                skip += 1
                continue
            res.append(val)
        return res

    def translate_phrase_to_gematria(self, phrase):
        '''
            convert a string to runes, multiple words are seperated by spaces (ligatured runes
            don't span the spaces)
        '''
        return [self.translate_to_gematria(x) for x in re.sub('[^0-9a-zA-Z]+', ' ', phrase).split()]

    def encode_as_forward_position(self, char_list):
        '''
            list of characters to a position index using the forward gematria, zero offset
        '''
        return [gematria.rune_to_position_forward_dict[rune] for rune in char_list]

    def encode_as_reverse_position(self, char_list):
        '''
            list of characters to a position index using the reverse gematria, zero offset
        '''
        return [gematria.rune_to_position_reverse_dict[rune] for rune in char_list]

    def encode_word_as_position_forward(self, word):
        '''
            english word to a position index using the forward gematria, zero offset
        '''
        return self.encode_as_forward_position(self.translate_to_gematria(word))

    def encode_word_as_position_reverse(self, word):
        '''
            english word to a position index using the forward gematria, zero offset
        '''
        return self.encode_as_reverse_position(self.translate_to_gematria(word))

    def positions_to_latin_forward(self, number_sequence):
        '''
            numbers to runeglish using the forward Gematria
        '''
        return [gematria.position_to_latin_forward_dict[rune] for rune in number_sequence]

    def positions_to_latin_reverse(self, number_sequence):
        '''
            numbers to runeglish  using the forward gematria
        '''
        return [gematria.position_to_latin_reverse_dict[rune] for rune in number_sequence]

    def positions_to_rune_forward(self, number_sequence):
        '''
            numbers to runeglish using the forward gematria
        '''
        return [gematria.position_to_rune_forward_dict[rune] for rune in number_sequence]

    def positions_to_rune_reverse(self, number_sequence):
        '''
            numbers to runes using the reverse gematria
        '''
        return [gematria.position_to_rune_reverse_dict[rune] for rune in number_sequence]

    def phrase_to_forward_position(self, phrase):
        '''
            english phrase to a position index using the reverse gematria
        '''
        return self.encode_as_forward_position(self.translate_phrase_to_gematria(phrase))

    def phrase_to_position_reverse(self, phrase):
        '''
            english phrase to a position index using the reverse gematria
        '''
        return self.encode_as_reverse_position(self.translate_phrase_to_gematria(phrase))

    # def runes_to_pos2(self, runes, order, shift):
    def encode_as_position(self, runes, order, shift):
        '''
            do not call this multiple times,
            :param runes: runes
            :param order: forward or reverse as string
            :param shift: shift between 0 and 28
            :return:
        '''
        if order.lower() == "reverse":
            return self.mod29L(
                [(gematria.rune_to_position_reverse_dict[char] + shift) for char in runes])
        return self.mod29L(
            [(gematria.rune_to_position_forward_dict[char] + shift) for char in runes])


    def encode_as_position_with_interrupter(self, runes, order, shift, interrupter_p,
                                            interrupter_pos):
        '''
            specify interrupter and position, and convert encoded runes back to interrupters
        :param runes:
        :param order:
        :param shift:
        :param interrupter_p:
        :param interrupter_pos:
        :return:
        '''
        #print("interrupter_p = {}, interrupter_pos = {}".format(interrupter_p,interrupter_pos))
        a = self.encode_as_position(runes, order, shift)
        for pos in interrupter_pos:
            a[pos] = interrupter_p
        return a

    def runes_to_pos(self, runes, shift_in=1):
        '''
        In this definition shift=1 is canonical forward position,
        F=0, U=0, etc.
        +2 is rotated canonical forward position by 1
        F=1, U=2, etc.
        shift -1 is
        shift=-1 is canonical forward position,
        F=28, U=27, etc.
        -2 is rotated canonical reverse position by 1
        F=27, U=26, etc.
        ultimatyley it
        '''
        if shift_in == 0:
            shift = 1
        else:
            shift = shift_in
        # if shift < 0:
        #     return self.mod29L([(gematria.rune_to_position_reverse_dict[char] - abs(shift) + 1)
        #     for char in runes])
        # return self.mod29L([(gematria.rune_to_position_forward_dict[char] + shift - 1) for char
        # in runes])
        if shift_in > -1:
            return self.encode_as_position(runes, "forward", shift - 1)
        return self.encode_as_position(runes, "reverse", shift + 1)

    def shift_pos(self, pos_list, shift_in=1):
        '''
        '''
        if shift_in == 0:
            shift = 1
        else:
            shift = shift_in
        if shift < 0:
            pos_list_r = [28 - char for char in pos_list]
            return self.mod29L([(char - abs(shift) + 1) for char in pos_list_r])
        return self.mod29L(
            [(gematria.rune_to_position_forward_dict[char] + shift - 1) for char in pos_list])

    def get_all_shifts(self, p):
        # todo this is a hst name and needs checking, plus output orde r is not canonical
        '''
        convert a list into all gematria orders and shifts 
        :param p: list to convert
        :return: list of all shifts for F and R gematria from input list
        '''
        r = []
        for i in range(0, 29):
            r.append(self.mod29L([(char + i) for char in p]))
            r.append(self.mod29L([(28 - char + i) for char in p]))
        return r

    def process_string_to_latin_forward(self, string):
        '''
            convert an input assumed to be one of a predetermined type/format to return_type,
        :param string: string to process
        :return:
        '''
        # print("\nprocess_string_to_latin_forward")
        # print("string = ", string)
        str_ls = list(string.replace(" ", ""))
        # print("list(string) = ", str_ls)
        # simple error check, that no mixed string is passed
        test = [any([x in gematria.runes for x in str_ls]),
                any([self.areEnglish(x) for x in str_ls]), any([x.isdigit() for x in str_ls])]
        # print("test = ", test)
        if test.count(True) > 1:
            print("!!ERROR!! iinput string is a mixture of runes, english or numbers")
            return []
        r = []
        if any([x in gematria.runes for x in str_ls]):
            # print("Keys are runes")
            for key in string.replace("\n", "").split(","):
                if key is not "":
                    # print(" key = ", key)
                    r.append([self.r2e[x] for x in list(key.replace(" ", ""))])
        elif any([x.isalpha() for x in str_ls]):
            # print("Keys are english")
            eng_key_list = string.replace("\n", "").split(",")
            # print("eng_key_list = ", eng_key_list)
            # for key in eng_key_list:
            # print(self.translate_phrase_to_gematria(key.replace(" ","")))
            r = [self.flatten(self.translate_phrase_to_gematria(x)) for x in eng_key_list]
        elif any([x.isdigit() for x in str_ls]):
            # print("Keys are numbers")
            keylist = []
            for key in string.split("\n"):
                if key is not "":
                    # print(" key = ", key)
                    keylist.append(
                        [int(e) if e else e for e in key.split(',')])  # print(keylist[-1])
            r = [self.positions_to_latin_forward(x) for x in keylist]
        #     print('keylist = ', keylist)
        # print('r = ', r)
        return r

    def process_string_to_type_word_length(self, string):
        '''
            convert an input assumed to be one of a predetermined type to return_type,
        :param string: string to process
        :param return_type: return runes, numbers, eng, or f-pos, r-pos etc ...
        :return:
        '''
        print("\nprocess_string_to_type_word_length")
        str_ls = list(string)
        # simple error check, that no mixed string is passed
        test = [any([x in gematria.runes for x in str_ls]), any([x.isalpha() for x in str_ls]),
                any([x.isdigit() for x in str_ls])]
        if test.count(True) > 1:
            return []
        r = []
        if any([x in gematria.runes for x in str_ls]):
            for key in string.replace("\n", "").split(","):
                if key is not "":
                    len_list = []
                    # print("key = ", key)
                    for key_part in key.split(" "):
                        # print("key_part = ", key_part)
                        len_list.append([len(list(key_part))])
                    r.append(len_list)
        elif any([x.isalpha() for x in str_ls]):
            eng_key_list = string.replace("\n", "").split(",")
            # print("eng_key_list = ", eng_key_list)
            for key in eng_key_list:
                # print("key = ", key)
                r.append([len(x) for x in self.translate_phrase_to_gematria(key)])
        elif any([x.isdigit() for x in str_ls]):
            keylist = []
            for key in string.split("\n"):
                if key is not "":
                    r.append(len(key.split(',')))  # print(keylist[-1])
        # print('r = ', r)
        return r

    def process_string_to_type(self, string, type):
        latin_forward = self.process_string_to_latin_forward(string)
        if type == "latin":
            return latin_forward
        elif type == "rune":
            return self.eng_to_rune(latin_forward)
        elif type == "prime":
            return self.eng_to_prime_value(latin_forward)
        elif type == "f_pos":
            return self.encode_as_forward_position(latin_forward)
        elif type == "r_pos":
            return self.encode_as_reverse_position(latin_forward)
        return latin_forward

    def process_string_to_type_with_order_and_shift(self, string, output_type, order, shift):
        '''
            convert a string (of STANDARD FORMAT, runes, english or forward position list) to
            output_type
            TODO: if else tree could be moved into a separate function, its used in multiple places
        :param string: input string
        :param output_type: string defining output format, one of latin, runes, prime, f_pos, r_pos
        :param order: the gematria order, forward or reverse
        :param shift: the gematria shift, number 0 to 28
        :return: the input string converted to output format (list of lists)
        '''
        # print("process_string_to_type_with_order_and_shift")
        # print("order ", order)
        # print("shift ", shift)
        runes = self.process_string_to_type(string, "runes")
        # print("runes ", runes)
        rot_pos = [self.encode_as_position(x, order, shift) for x in runes]
        # print("rot_pos ",rot_pos)
        rotated_latin = [self.pos_to_eng(x) for x in rot_pos]
        # print("rotated_latin",rotated_latin)
        r = []
        if output_type == "latin":
            r = rotated_latin
        elif output_type == "rune":
            r = [self.eng_to_rune(x) for x in rotated_latin]
        elif output_type == "prime":
            r = [self.eng_to_prime_value(x) for x in rotated_latin]
        elif output_type == "f_pos":
            r = [self.encode_as_forward_position(x) for x in rotated_latin]
        elif output_type == "r_pos":
            r = [self.encode_as_reverse_position(x) for x in rotated_latin]
        elif output_type == "forward_pos":
            r = [self.encode_as_forward_position(x) for x in rotated_latin]
        elif output_type == "reverse_pos":
            r = [self.encode_as_reverse_position(x) for x in rotated_latin]
        else:
            r = [self.eng_to_rune(x) for x in rotated_latin]

        # TODO one of these days add in prime values with forward and backward maps, maybe mod
        #  prime value maps,
        # elif output_type == "prime":
        #     for key in [self.eng_to_prime_value(x) for x in rotated_latin]:
        #         r.append([str(x) for x in key])
        # elif output_type == "f_pos":
        #     for key in [self.encode_as_forward_position(x) for x in rotated_latin]:
        #         r.append([str(x) for x in key])
        # elif output_type == "r_pos":
        #     for key in [self.encode_as_reverse_position(x) for x in rotated_latin]:
        #         r.append([str(x) for x in key])
        # elif output_type == "forward_pos":
        #     for key in [self.encode_as_forward_position(x) for x in rotated_latin]:
        #         r.append([x for x in key])
        # elif output_type == "reversee_pos":
        #     for key in [self.encode_as_reverse_position(x) for x in rotated_latin]:
        #         r.append([str(x) for x in key])
        # else:
        #     r = [self.eng_to_rune(x) for x in rotated_latin]
        # print(r)
        return r

    def flatten(self, li):
        return sum(([x] if not isinstance(x, list) else self.flatten(x) for x in li), [])

    def isRune(self, char):
        '''
            check if char is a rune
        '''
        return char in gematria.runes

    def isLatin(self, char):
        if char in gematria.latin_fragments:
            return True
        if char in gematria.bigram:
            return True
        if char in gematria.trgram:
            return True
        return False

    def areRunes(self, char_list):
        chars = self.flatten(char_list)
        for char in chars:
            if self.isRune(char):
                pass
            else:
                return False
        return True

    def areLatins(self, char_list):
        chars = self.flatten(char_list)
        for char in chars:
            if self.isLatin(char):
                pass
            else:
                return False
        return True

    def isEnglish(self, char):
        if char in gematria.lower:
            return True
        elif char in gematria.upper:
            return True
        return False

    def areEnglish(self, char_list):
        chars = self.flatten(char_list)
        for char in chars:
            if self.isEnglish(char):
                pass
            else:
                return False
        return True

    def mod29(self, k):
        '''
            mod 29 of a number
        '''
        if isinstance(k, int):
            return k % 29
        return k

    def mod29L(self, list):
        '''
            mod 29 for a list of numbers
        '''
        return [self.mod29(x) for x in list]
