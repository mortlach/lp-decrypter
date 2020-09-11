from itertools import combinations
from .gematria import gematria
from PyQt5.QtCore import *
from data.data import data
import itertools
from text_ranking.FourGramTextScore import FourGramTextScore
from text_ranking.WordMatch import WordMatch
import time
from collections import namedtuple

# TODO these all need to be tidied up and rationalized
''' These namedTuples are used to store labelled data '''
DecryptionSetup = namedtuple('DecryptionSetup', 'keys_runeglish key_lengths ct_rune_words '
                                                'ct_rune_chars ct_lengths ct_rot ct_rune_word_len '
                                                'dec_map interrupters interrupters_p  '
                                                'ct_use_gematria_forward ct_use_gematria_reverse '
                                                'ct_gematria_forward_shifts '
                                                'ct_gematria_reverse_shifts '
                                                'key_use_gematria_forward '
                                                'key_use_gematria_reverse '
                                                'key_gematria_forward_shifts '
                                                'key_gematria_reverse_shifts '
                                                "undefined_answers_are_all "
                                                "use_reverse_keys "
                                                "wrap_key_around_ct "
                                                "score_reversed_decryption")
EncryptionData = namedtuple('EncryptionData', 'method k_shift c_shift ciphertext key interrupter '
                                              'interrupter_pos_set ct_start_index')
AnswerData = namedtuple('AnswerData', 'decryption score decryption_string encryptiondata')


class DecryptModel(QObject):
    '''
        This class takes the data held in data and passed to main_loop_rune


        Functions loop over all settings, decrypting cipher-text with keys,
        different interrupters, geaatria order/rotations, key offsets in ct, ..

        Resulting plaintext  is scoring and ranked based on its similarity to english (converted
        to runes).

        (set through the gui, but should work independent of GUI)
        TODO When things have settled, this will need lots of refactoring to make get/set data
        more convenient and intuitive.
    '''
    decrypt_finished = pyqtSignal()     # signals for worker threads
    decrypt_progress = pyqtSignal()

    def __init__(self):
        super(DecryptModel, self).__init__()
        self.data_obj = data()          # data obj allows access to data across multiple classes
        self.data = self.data_obj.data
        self.gem = gematria()           # gematria object for encoding and converting to runes
        self.previous_decryption_data = {}
        self.previous_decryption_results = {}
        ''' this object scores 4grams '''
        self.fourgram_textscore = FourGramTextScore()
        ''' this object compares list of chars to words in a dict, and fins the numbe of 
        different chars '''
        self.wordmatch = WordMatch()
        self.score_rejected_phrases = {}
        # with open(os.path.join(os.getcwd(), 'data', 'rejected_text', "rejected.csv"), 'r',
        #           encoding="utf8") as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         self.score_rejected_phrases[tuple(row)] = True
        self.score_rejected_phrases = {}
        self.ans_already_considered = {}
        self.previous_decryption_data = {}
        self.previous_decryption_results = {}  # self.current_int = None  # self.current_keyrot =
        # None  # self.current_ctrot = None

    def main_loop_rune(self, dec_data, progress_callback):
        '''
            called by the Worker
            this is the main loop run(e), it uses parameters set in dec_data
            this data is further processed, and then we loop all options
            TODO very likely this can be made neater, cleaner and faster
            answers are added to self.data["answers]
        '''
        print("\nMAIN_LOOP_RUNE")


        time_start = time.time()
        # for now reset these here,
        self.score_rejected_phrases = {}
        self.ans_already_considered = {}
        self.previous_decryption_data = {}
        self.previous_decryption_results = {}
        # OPTIONS
        undefined_answers_are_all = dec_data.undefined_answers_are_all
        wrap_key_around_ct = dec_data.wrap_key_around_ct
        score_reversed_decryption = dec_data.score_reversed_decryption

        # make a local copy for ease ..
        keys_runeglish = dec_data.keys_runeglish
        ''' if use_reverse_keys then add reversed text to keylist '''
        if dec_data.use_reverse_keys:
            keys_runeglish.append(keys_runeglish[::-1])

        # key_lengths = [len(x) for x in keys_runeglish]
        # # key_lengths = dec_data.key_lengths # TODO can calculate here
        # ct_rune_words = dec_data.ct_rune_words
        # ct_rune_chars = dec_data.ct_rune_chars  # TODO can calculate here
        # ct_lengths = dec_data.ct_lengths  # TODO can calculate here
        # ct_rot = dec_data.ct_rot  # TODO can calculate here
        # ct_rune_word_len = dec_data.ct_rune_word_len  # TODO can calculate here
        # #dec_map = dec_data.dec_map
        # #interrupters = dec_data.interrupters
        # #interrupters_p = dec_data.interrupters_p  # TODO can calculate here
        # ct_use_gematria_reverse = dec_data.ct_use_gematria_reverse
        # ct_use_gematria_forward = dec_data.ct_use_gematria_forward
        # ct_gematria_forward_shifts = dec_data.ct_gematria_forward_shifts
        # ct_gematria_reverse_shifts = dec_data.ct_gematria_reverse_shifts
        # key_use_gematria_forward = dec_data.key_use_gematria_forward
        # key_use_gematria_reverse = dec_data.key_use_gematria_reverse
        # key_gematria_forward_shifts = dec_data.key_gematria_forward_shifts
        # key_gematria_reverse_shifts = dec_data.key_gematria_reverse_shifts

        '''' which Gematria order / rotation to apply to each ct'''
        ct_order_shift_list = []
        if  dec_data.ct_use_gematria_forward:
            for i in dec_data.ct_gematria_forward_shifts:
                ct_order_shift_list.append(["forward", i])
        if dec_data.ct_use_gematria_reverse:
            for i in dec_data.ct_gematria_reverse_shifts:
                ct_order_shift_list.append(["reverse", i])
        '''' which Gematria order / rotation to apply to keys'''
        key_order_shift_list = []
        if dec_data.key_use_gematria_forward:
            for i in  dec_data.key_gematria_forward_shifts:
                key_order_shift_list.append(["forward", i])
        if dec_data.key_use_gematria_reverse:
            for i in dec_data.key_gematria_reverse_shifts:
                key_order_shift_list.append(["reverse", i])

        # TODO use this signal to emit decrypting loop status, counters, etc ..
        progress_callback.emit(1)
        ''' all answers will go in here for now, but this needs to change '''
        self.answers = []
        ''' count how many iterations we are doing '''
        ct_key_counter = 0
        ct_start_index_counter = 0
        interrupter_counter = 0
        interrupter_pos_set_counter = 0
        kc_shift_counter = 0
        counter = 0
        ''' Loop over each CT '''
        #print(list(itertools.product(dec_data.ct_rune_words, keys_runeglish)))
        # input()
        # for ct,key in ct_rune_words:
        for ct_key in itertools.product(dec_data.ct_rune_words, keys_runeglish):
            ct_key_counter += 1
            print("\nct_key_counter = ", ct_key_counter)
            print("ct_key", ct_key)
            ct = ct_key[0]
            key = ct_key[1]
            ct_rune_char = self.flatten(ct)
            ct_length = len(ct_rune_char)

            ct_rune_word_len = [len(x) for x in ct]
            print("ct_rune_char =", ct_rune_char)
            print("ct_length =", ct_length)
            print("ct_rune_word_len =", ct_rune_word_len)
            ''' Loop over each KEY '''
            # for key in keys_runeglish:
            key_length = len(key)
            print("key_length =", key_length)
            ''' KEY DRAGGING '''
            ''' rotate CT so that each rune takes a turn as the first rune the key is applied 
            to, use the data entry wrap_key_around_ct is an option to see how far to rotateright 
            if using an entire cipher text it might be worth setting this to true'''
            if dec_data.wrap_key_around_ct:
                max_ct_start_index = ct_length
            else:
                max_ct_start_index = ct_length - key_length
            print("max_ct_start_index = ", max_ct_start_index)
            for ct_start_index in range(0, max_ct_start_index):
                ct_start_index_counter += 1
                print("ct_start_index_counter = ", ct_start_index_counter)
                print("ct_start_index =", ct_start_index)

                rotated_ct = ct_rune_char[ct_start_index:] + ct_rune_char[:ct_start_index]
                print("rotated_ct =", rotated_ct)
                ''' for each rotated CT we need to get enough CT to apply the key, 
                WITH interrupters. Therefore we call this function to crop the CT    
                '''
                rot_crop_ct = self.crop_ct_to_keylen_with_interrupter(rotated_ct, key_length)
                print("rot_crop_ct =", rot_crop_ct)
                rot_crop_ct_p = self.flatten([self.gem.rune_to_pos(c) for c in rot_crop_ct])
                print("rot_crop_ct_p =", rot_crop_ct_p)
                ''' CIPHER TEXT INTERRUPTERS, WORTH THINKING ABOUT '''
                ''' Are interrupters always encoded as 'normal' forward unshifted gematria? 
                So far that is 
                true, but need  it be? This definition of interrupters we'll call 
                "canonical". We will 
                find every possible combination of every interrupter Not all interrupter 
                runes in the CT ARE interrupters, they just could be, therefore, 
                we find all possible sets of each interrupter position in the CT'''
                ''' stands for cannonical_interrupter_position_sets '''
                # cannonincal_interrutper_position_sets = {}
                # for i in interrupters_p:
                #     cannonincal_interrutper_position_sets[
                #         i] = self.get_all_interrupter_position_lists(rot_crop_ct_p, i)
                # print("cannonincal_interrutper_position_sets ",
                #       cannonincal_interrutper_position_sets)
                for interrupter in dec_data.interrupters_p:
                    interrupter_counter += 1
                    print("interrupter_counter = ", interrupter_counter)
                    print("interrupter = ", interrupter)
                    interrupter_r = self.gem.pos_to_rune(interrupter)
                    print("interrupter_r = ", interrupter_r)
                    interrupter_pos_sets = self.get_all_interrupter_position_lists(rot_crop_ct_p,
                                                                               interrupter)
                    print("interrupter_pos_sets = ", interrupter_pos_sets)
                    for interrupter_pos_set in interrupter_pos_sets:  # #range(0,
                        interrupter_pos_set_counter += 1
                        print("interrupter_pos_set_counter = ", interrupter_pos_set_counter)
                        print("interrupter_pos_set =", interrupter_pos_set)

                        for kc_shift in itertools.product(key_order_shift_list,
                                                          ct_order_shift_list):
                            kc_shift_counter += 1
                            print("kc_shift_counter = ", kc_shift_counter)
                            k_shift = kc_shift[0]
                            c_shift = kc_shift[1]
                            print("k_shift, c_shift = ", k_shift, c_shift)
                            # convert the key an dct to position numbers based on gem
                            # order and shift
                            # convert the
                            keyp = tuple(self.gem.encode_as_position(key, k_shift[0], k_shift[1]))
                            print("keyp = ", keyp)

                            ''' for the CT force any CT interrupters to be encoded in forward gematria '''
                            ctp = self.gem.encode_as_position_with_interrupter(rot_crop_ct, c_shift[0], c_shift[1],
                                                                    interrupter, interrupter_pos_set)
                            ''' use this method to encode interrupter according to shift '''
                            #ctp = self.gem.encode_as_position(rot_crop_ct,
                            # c_shift[0], c_shift[1])
                            # print("ctp = ", ctp)
                            # ctp = self.gem.encode_as_position(rot_crop_ct,c_shift[0], c_shift[1])
                            # print("ctp = ", ctp)
                            #ciphertext = tuple(self.getCipherRunes(ctp, interrupter, key_length))
                            #print("ciphertext = ", ciphertext)
                            counter += 1
                            # print("counter = ", counter)
                            # d THE DFECRYPTIO NFUCNTION
                            ans_to_check = self.decrypt_and_get_ans_to_score(interrupter_pos_set,
                                                                             ctp, keyp, interrupter,
                                                                             dec_data.dec_map)
                            # print("ans_to_check = ", ans_to_check)
                            # print("len(ans_to_check) = ", len(ans_to_check))
                            # print("ans_to_check = ", ans_to_check)
                            # if ans_to_check is not []:
                            #     for ans in ans_to_check:
                            #         # if ans already done, reject
                            #         print("ans = ", ans_to_check)
                            #         if self.new_answer_to_score(tuple(ans)):
                            #             print("score_ans, ans = ", ans)
                            # print("try scoree")
                            self.score_ans_to_check(ans_to_check=ans_to_check, k_shift=k_shift,
                                                    c_shift=c_shift, interrupter=interrupter,
                                                    interrupter_pos_set=interrupter_pos_set,
                                                    ct_start_index=ct_start_index,
                                                    ct_rune_word_len=ct_rune_word_len,
                                                    ct_length=ct_length, ct=ct, key=key)
                            #print("k_shift = {}, c_shift {}".format(k_shift, c_shift))
        # self.answers.sort(key=lambda x: x[1])
        # print("sort ans")
        self.answers.sort(key=lambda x: x.score.score_per_ngram)
        self.answers.reverse()  # EncryptionData = namedtuple('EncryptionData',
                        # 'method k_shift c_shift  # ciphertext  # interrupter
                        # interrupter_pos_set')  # AnswerData = namedtuple('AnswerData',
                        # 'decryption score  # decryption_string encryptiondata')  # for i,
                        # entry in enumerate(self.answers):  #     print("entry == ",
                        # entry.decryption)  #     f = self.flatten( entry.decryption)  #
                        # #print("Checking ", f)  #     f2= []  #     for item in f:  #
                        # if item == "_":  #             f2.append(item)  #         else:  #
                        # #f2.append(self.gem.pos_to_eng_dict_f[item])  #             f2.append(
                        # self.gem.pos_to_eng(item))  #  #     t2 = []  #     for entry in
                        # self.ragged_partition(f2, self.ct_rune_word_len[0]):  #
                        # t2.append("".join(entry))  #     self.answers[i].decryption_string = "
                        # ".join(t2)  # print(i, entry[1], self.answers[i][-1])
        # TODO this won't work when threads are fully implemented
        self.data["answers"] = self.answers
        # print("Answer check:")
        # for ans in self.answers:
        #     dec = [x for x in ans.decryption if x is not '_']
        #     print("dec = ", dec)
        #     score = self.fourgram_textscore.get_pos_phrase_log_prob_with_min_count(dec, self.data[
        #         "4gram_count_cut"], self.data["four_gram_log_prob_min"], self.data[
        #                                                                                "min_score_per_4gram_gradient"],
        #                                                                            self.data[
        #                                                                                "min_score_per_4gram_offset"])
        #
        #     print("ciphertext = ", ans.encryptiondata.ciphertext)
        #     print("decryption = ", ans.decryption)
        #     print("ct_word_len = ", [len(x) for x in ans.encryptiondata.ciphertext])
        #     print("interrupter = ", ans.encryptiondata.interrupter)
        #     print("interrupter_pos_set = ", ans.encryptiondata.interrupter_pos_set)
        #     # self.get_decryptions_in_words_string(decryption_in_words, ct_rune_word_len, interrupter,
        #     #                             interrupter_pos_set)
        #     print(score)
        print("\nRUN FINIHSED\n")
        print("COUNTER RESULTS")
        print("counter = ", counter)
        print("kc_shift_counter = ", kc_shift_counter)
        print("ct_start_index_counter = ", ct_start_index_counter)
        print("ct_key_counter = ", ct_key_counter)
        print("interrupter_pos_set_counter = ", interrupter_pos_set_counter)
        print("interrupter_counter = ", interrupter_counter)
        print("ans count ", len(self.answers))
        # TODO put these back in
        #       print("self.decryptDataRepeats ", self.decryptDataRepeats)
        #       print("self.decryptAnswerRepeats ", self.decryptAnswerRepeats)
        # print("self.iPosSetsTotal ", self.iPosSetsTotal)
        # print( "self.answers ", self.answers[0:2]  )
        # print("self.decryptAnswerRepeats ", self.decryptAnswerRepeats)
        # print("self.decryptDataRepeats ", self.decryptDataRepeats)
        print("main_loop finished ", time.time() - time_start)

    def crop_ct_to_keylen_with_interrupter(self, ct, keylen):
        '''
            Crop the CT so that it is just long enough to apply the key, with all possible
            passed interrupters. This is used so that when a very long CT is passed we don't get
            interrupters for the whole CT, just the part that the key can be applied to.
        :param ct: ct to crop
        :param keylen: number of runes in key
        :return: the cropped CT
        '''
        # use normal gematria position for interrupters
        ct_p = self.gem.encode_as_position(ct,'forward',0)
        ct_p_len = len(ct_p)
        ct_out = ct[:keylen]
        ct_out_max_count = max([ct_out.count(x) for x in set(ct_out)])
        while 1:
            ''' check if keylength + max count == length of return text (then we can return) '''
            ''' check if keylength + max count > length of passed ct (then we must return) '''
            ''' else add to the return list '''
            if keylen + ct_out_max_count == len(ct_out):
                return ct_out
            elif keylen + ct_out_max_count > ct_p_len:
                return ct_out
            else:
                ct_out = ct[:keylen + ct_out_max_count]
                ct_out_max_count = max([ct_out.count(x) for x in set(ct_out)])

    def decrypt_ct_key(self, cipher_runes, key_runes, interrupter, interrupter_pos, decrypt_map):
        '''
            The main decryption function, passed data is all in numbers
            TODO: write a version for ct and pt to get keys
        :param cipher_runes: list in numbers,
        :param key_runes: list(tuple) in numbers,
        :param interrupter: interrupter run in number (normal gematria enforced?)
        :param interrupter_pos: list(tuple) interrupter position in CT, NB not all CT interrupter
        runes are interrupters
        :param decrypt_map: dictionary giving ()
        :return: (decrytped runes (list), TRUE or FALSE) flag if decryption passed test)
        '''
        print("\nDECRYPT_CT_KEY")
        print("cipher_runes = ",  cipher_runes )
        print("key_runes = ",  key_runes )
        print("interrupter = ",  interrupter )
        print("interrupter_pos = ",  interrupter_pos )
        # print("decrypt_map = ",  decrypt_map )
        # print("type(cipher_runes) = ",  type(cipher_runes) )
        # print("type(key_runes) = ",  type(key_runes) )
        # print("type(interrupter) = ",  type(interrupter) )
        # print("type(interrupter_pos) = ",  type(interrupter_pos) )
        # print("type(decrypt_map) = ",  type(decrypt_map) )
        # TODO types are all confused here, lists  / tuples, meh
        # TODO: write a version where not all plaintext interrupters cause an interruption ?
        interrupter_tuple = tuple([interrupter])
        answer = []
        ''' result of chekcing if interrupter found in non-interrupter position '''
        no_interrupter_in_decrypt = True
        ''' OOB flags and counters, keep track of list indexes '''
        int_fin = True if interrupter_pos == () else False
        key_fin = False
        int_index = 0
        key_index = 0
        for i, rune in enumerate(cipher_runes):
            ''' check if this is an interrupter position '''
            if i in interrupter_pos:
                answer.append(interrupter_tuple)
                int_index += 1 # OOB check stuff
                if int_index == len(interrupter_pos):
                    int_fin = True
            else:
                if key_index == len(key_runes):
                    # print("key_index ==  len(key_runes) BREAK")
                    break
                # answer.append(decrypt_map[(cipher_runes[i], key_runes[key_index])])
                answer.append(
                    self.decrypt_a_char(cipher_runes[i], key_runes[key_index], decrypt_map))
                '''we "DEFINE" where interrupters are. If decrypted rune is the interrupter 
                rune, then that breaks this scheme, and result is rejected '''
                if answer[-1] == interrupter_tuple:
                    no_interrupter_in_decrypt = False
                    # print("interrupter in decryption BREAK")
                    break
                ''' key index  OOB checks '''
                key_index += 1
                if key_index == len(key_runes):
                    key_fin = True
            '''  finished check '''
            if key_fin:
                if int_fin:
                    # print("key_fin == int_fin  BREAK")
                    break
        print("answer = ", answer)
        return (answer, no_interrupter_in_decrypt)

    def decrypt_and_get_ans_to_score(self, interrupter_pos_set, ct_rune_p, keyp, interrupter,
                                     dec_map):
        '''
            gets the decrypted test, then gets all rotations and shifts of the decrypted text
            TODO as usual, rationalize all data structures, I/O
        :param interrupter_pos_set: the position of the interrutpers for this setup
        :param ct_rune_p:  the cipher text (as list / tuple of numbers)
        :param keyp:  the cipher text (as list / tuple of numbers)
        :param interrupter: the interrupter (in canonical position)
        :param k_shift: k_shift parameters (f, r and number)
        :param c_shift: ct_shift parameters (f, r and number)
        :param rotation: current rotation index, used when scoring
        :param ct_rune_word_len:
        :param ct_length:
        :param dec_map:
        :return:
        '''
        #print("\nDECRYPT_AND_GET_ANS_TO_SCORE")
        self.saving_fails = True
        # keep a record of what input data has been attempted
        # TODO make these tuples from when first create din main_loop_rune ????
        dataToDecrypt = (tuple(ct_rune_p), tuple(keyp), interrupter, interrupter_pos_set)
        # print(dataToDecrypt)
        ans_to_check = []
        if self.new_data_to_decrypt(tuple(dataToDecrypt)):
            ''' function returns decryption runes from look up table, can be more than 1 ans 
            for each CT rune, and a TRUE or FALSE, if the ans "WAS_GOOD" see decrypt_ct_key '''
            decryption = self.decrypt_ct_key(ct_rune_p, keyp, interrupter,
                                             tuple(interrupter_pos_set), dec_map)


            ''' if the decryption was good ( bad would be something "impossible" like a plaintext 
            rune is an interrupter in a position where one is not allowed '''
            #print("decryption = ", decryption)
            if decryption[1]:
                ans_to_check = self.get_decryptions_to_keep(decryption,interrupter,
                                                            interrupter_pos_set)
                if False in ans_to_check:
                    print("!!FALSE!!", ans_to_check)
        # print("type(ans_to_check) = ", type(ans_to_check))
        # print("len(ans_to_check) = ", len(ans_to_check))
        # print("decrypt_and_get_ans_to_score ans_to_check = ", ans_to_check)
        # print("\ndecrypt_and_get_ans_to_score FIN")
        return ans_to_check

    def getCipherRunes(self, runes, interrupter, key_length):
        '''
        :param runes:
        :param interrupter:
        :param key_length:
        :return:
        '''
        i = 0
        # a = len([char for char in runes[0:key_length+i] if char != interrupter ]) < key_length
        # print(a)
        while len([char for char in runes[0:key_length + i] if char != interrupter]) < key_length:
            i += 1
        return runes[0: key_length + i]

    def get_all_sublists(self, my_list):
        ''' all tuples, probably itertools function for this  '''
        subs = []
        for i in range(0, len(my_list) + 1):
            temp = [tuple(x) for x in combinations(my_list, i)]
            if len(temp) > 0:
                subs.extend(tuple(temp))
        #     print("temp = ", temp)
        # print("subs = ", subs)
        return subs

    def get_all_interrupter_position_lists(self, runes, interrupter):
        '''
        :param runes: list of runes
        :param interrupter: interrupter runes
        :return: all possible combinations of possible positions for interrutper in runes
        '''
        # print("get_all_interrupter_position_lists = ")
        # print("runes = ", runes)
        # print("interrupter = ", interrupter)
        interrupter_indexes = []
        for index, rune in enumerate(runes):
            if rune == interrupter:
                interrupter_indexes.append(index)
        # print("interrupter_indexes = ", interrupter_indexes)
        return self.get_all_sublists(interrupter_indexes)

    # Returns the rotated list
    def rightRotate(self, lists, num):
        output_list = []
        # Will add values from n to the new list
        for item in range(len(lists) - num, len(lists)):
            output_list.append(lists[item])  # Will add the values before
        # n to the end of new list
        for item in range(0, len(lists) - num):
            output_list.append(lists[item])
        return output_list

    def getDecryptionsInWords(self, decryption, rotateIndex, wordlen, ctLen):
        '''
            convert main_loop decryption to letters and words
        '''
        # print("getDecryptionsInWords")
        decryption2 = decryption
        # print("decryption2 = ", decryption2)
        ''' we pad right with _ char, so when we split into words we can see word lengtsh mroe 
        clearly, thats why we pass in the full CT length, not the ct_crop_rot length '''
        decryption2 += ['_'] * (ctLen - len(decryption))
        # print("decryption22 = ", decryption2)
        # print("rotateIndex = ", rotateIndex)

        decryption2 = self.rightRotate(decryption2, rotateIndex)
        # print("decryption23 = ", decryption2)
        # print(decryption2[rotateIndex:] + decryption2[:rotateIndex])
        # print(decryption2[-rotateIndex:] + decryption2[:-rotateIndex])
        # print("wordlen = ", wordlen)
        ''' now the ct is rotated back to its original position and length (with blanks) split 
        into words  '''
        decryption3 = []
        for length in wordlen:
            decryption3.append(decryption2[:length])
            del decryption2[:length]
        # print("decryption3= ", decryption3)
        return decryption3

    def ragged_partition(self, list, wordlen):
        decryption3 = []
        for length in wordlen:
            decryption3.append(list[:length])
            del list[:length]
        # print(decryption3)
        return decryption3

    def decrypt_a_char(self, c, k, dec_map):
        return dec_map.get((c, k), [False])

    # def get_decryptions(self, ct, key, dec_map):
    #     d = [self.decrypt_a_char(c, k, dec_map) for c, k in zip(ct, key)]
    #     if [False] in d:
    #         return [False]
    #     return [p for p in
    #             itertools.product(*[self.decrypt_a_char(c, k, dec_map) for c, k in zip(ct, key)])]

    def new_data_to_decrypt(self, dataToDecrypt):
        # print("dataToDecrypt = ", dataToDecrypt)
        # print("type(dataToDecrypt) = ", type(dataToDecrypt))
        # print("type(self.previous_decryption_data) = ", type(self.previous_decryption_data))
        self.saving_repeated_data_to_decrypt = True
        if dataToDecrypt in self.previous_decryption_data:
            print("dataToDecrypt  is not new ")
            #self.decryptDataRepeats += 1  # print("dataToDecrypt in previous_decryption_data" )
            return False
        else:
            if self.saving_repeated_data_to_decrypt:
                self.previous_decryption_data[dataToDecrypt] = True
        return True

    def new_answer_to_score(self, ans):
        saving_repeated_data_to_decrypt = True
        if ans in self.ans_already_considered:
            # todo used to have global variable counting here
            #            self.ansToScoreRepeats += 1  # print("dataToDecrypt in
            #            previous_decryption_data" )
            return False
        else:
            if saving_repeated_data_to_decrypt:
                self.ans_already_considered[ans] = True
        return True

    def get_decryptions_to_keep(self, decryption,interrupter, interrupter_pos_set):
        # print("\nGET_DECRYPTIONS_TO_KEEP")
        decryptions_to_keep = []

        if False in decryption:
            print("FALSE!!", decryption)

        ''' here the decryption result is expanded to give all possible plaintexts 
        NB: some decryption maps can give more than one answer for the same key and ct  '''
        decryption2 = [p for p in itertools.product(*list(decryption[0]))]
        # print("get_decryptions_to_keep decryption2 = ", decryption2)
        for item in decryption2:
            # print("get_decryptions_to_keep item = ", item)
            ''' each decryption could be the plaintext rotated, inverted, so get all possible 
            shifts of the decryption to score '''
            for decrypt in self.gem.get_all_shifts(item):  # loop here to rotate all plaintext
                ''' get_all_shifts will have replaced the interrupters, so put them back '''
                ''' this is probably a bit sketchy and could cause crashes ... or wrong output  '''
                for pos in interrupter_pos_set:
                    if pos < len(decrypt):
                        decrypt[pos] = interrupter
                    elif pos == len(decrypt):
                        decrypt.append(interrupter)
                    else:
                        pass

                decryptions_to_keep.append(list(decrypt))

                # print("get_decryptions_to_keep decrypt = ", decrypt)
                # todo kept a list of repeated hits here, for monitoring, but lost it
                # if tuple(decrypt) in self.previous_decryption_results:
                #     pass
                # #     self.decryptAnswerRepeats += 1
                # else:
                #     ''' add these results to previous_decryption_results'''
                #     self.previous_decryption_results[tuple(decrypt)] = True
                #     # add to return list
                #     decryptions_to_keep.append(list(decrypt))
        # print("decryptions_to_keep = ", decryptions_to_keep)
        return decryptions_to_keep

    def score_ans_to_check(self, ans_to_check, k_shift, c_shift, interrupter,
                           interrupter_pos_set, ct_start_index, ct_rune_word_len, ct_length, ct,
                           key):
        '''
            score the answers, by getting log probability score and then comparing to cribwords
            we pass in various parameters to be kept as meta data with the ans to keep
        :param ans_to_check: ans reults
        :param k_shift:
        :param c_shift:
        :param rotated_ct:
        :param interrupter:
        :param interrupter_pos_set:
        :param ct_start_index:
        :param ct_rune_word_len:
        :param ct_length:
        :return: just updates global ans dict
        '''
        # print("\nSCORE_ANS_TO_CHE")
        if ans_to_check is not []:
            for ans in ans_to_check:
                # if ans already done, reject
                if self.new_answer_to_score(tuple(ans)):
                    # print("score_ans, ans = ", ans)
                    # self.score_ans(ans, k_shift, c_shift, rotated_ct, interrupter,
                    #                interrupter_pos_set, ct_start_index, ct_rune_word_len,
                    #                ct_length)
                    # def score_ans(self, ans, k_shift, c_shift, ciphertext, interrupter,
                    # interrupter_pos_set,
                    #               rotation, ct_rune_word_len, ct_length):
                    # print("\nSCORE_ANS")
                    # ScoreResults is namedtuple('ScoreResults', 'total_score score_per_ngram
                    # min_score_count
                    # ngram_count')
                    # TODO dis-entagle this from data dict

                    score = self.fourgram_textscore.get_pos_phrase_log_prob_with_min_count(ans, self.data[
                        "4gram_count_cut"], self.data["four_gram_log_prob_min"],
                        self.data["min_score_per_4gram_gradient"],
                        self.data["min_score_per_4gram_offset"])

                    # print("score = ", score)
                    # check if score should be rejected
                    if score.rejected:
                        # print("reject score")
                        self.ans_already_considered[tuple(score)] = True
                    else:
                        print("score ok, get decryptedd words")
                        print("ans = ", ans)
                        print("score = ", score)

                        #trackign a big, wer ethe sae m printed words gets different scores ...

                        decryption_in_words = self.getDecryptionsInWords(ans, ct_start_index,
                                                                         ct_rune_word_len,
                                                                         ct_length)
                        print("decryption_in_words = ", decryption_in_words)
                        ''' Get the decrypted words  where we know all the characters. we're 
                        going to check these words against ones a criblist. The check is:
                        
                            criblist_word - decrypted_word (as gematria forward position)
                            compare number of zeros to word length
                            if there are enough zeros accept the answer 
                        This helps cut noise by a lot - its a great sieve
                        however, we know there are typos, maybe uncommon words, so configure 
                        it appropriately  '''
                        # TODO needs neatening up
                        decryption_full_words = [x for x in decryption_in_words if "_" not in x]
                        print("decryption_full_words = ", decryption_full_words)
                        word_distances = []
                        for w in decryption_full_words:
                            word = tuple(w)
                            wl = len(word)
                            if wl == 1:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "1_rune_char_dif"])
                            elif wl == 2:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "2_rune_char_dif"])
                            elif wl == 3:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "3_rune_char_dif"])
                            elif wl == 4:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "4_rune_char_dif"])
                            elif wl == 5:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "5_rune_char_dif"])
                            elif wl == 6:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "6_rune_char_dif"])
                            elif wl == 7:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "7_rune_char_dif"])
                            elif wl == 8:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "8_rune_char_dif"])
                            elif wl == 9:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "9_rune_char_dif"])
                            elif wl == 10:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "10_rune_char_dif"])
                            elif wl == 11:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "11_rune_char_dif"])
                            elif wl == 12:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "12_rune_char_dif"])
                            elif wl == 13:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "13_rune_char_dif"])
                            elif wl == 14:
                                d = self.wordmatch.is_word_char_dif_good_enough(word, self.data[
                                    "14_rune_char_dif"])
                            else:
                                d = [[True]]  # dummy value, no 15+ rune word dict
                            word_distances.append(d)
                        print("word_distances = ", word_distances)  # input()
                        if all([x[-1] for x in word_distances]):
                            # EncryptionData = namedtuple('EncryptionData', 'method k_shift c_shift
                            # ciphertext interrupter interrupter_pos_set')
                            # AnswerData = namedtuple('AnswerData', 'decryption score
                            # decryption_string
                            # encryptiondata')
                            # TODO  ahh self.data should nto be here, much tidying possible ;)

                            ed = EncryptionData(method=self.data["enc_map_name"], k_shift=k_shift,
                                                c_shift=c_shift, ciphertext=ct, key=key,
                                                interrupter=interrupter,
                                                interrupter_pos_set=interrupter_pos_set,
                                                ct_start_index=ct_start_index)
                            # print("ed = ", ed)

                            decryption_string = self.get_decryptions_in_words_string(
                                decryption_in_words, ct_rune_word_len, interrupter,
                                interrupter_pos_set)

                            ad = AnswerData(decryption=ans, score=score,
                                            decryption_string=decryption_string, encryptiondata=ed)
                            # print("ad = ", ad)
                            # self.answers.append([ans, score, word_distances, k_shift, c_shift,
                            # ciphertext,
                            # interrupter, interrupter_pos_set,
                            # decryption_in_words])
                            self.answers.append(ad)
                else:
                    pass  # print("self.new_answer_to_score(tuple(ans)) == FALSE")  # anscounter
                    # += 1  #  # print("Last Answer = ",answers[-1])  # input()  #
                    # self.answers.append([ans, score, word_distances, k_shift, c_shift,
                    # ciphertext,  # interrupter, interrupter_pos_set,  #
                    # decryption_in_words])  # self.anscounter += 1  # print("Last Answer = ",
                    # answers[-1])  # input()  # print("\nSCORE_ANS_TO_CHE FIN")

    def get_decryptions_in_words_string(self, decryption_in_words, ct_rune_word_len, interrupter,
                                        interrupter_pos_set):
        print("\nGET_DECRYPTIONS_IN_WORDS_STRING")
        # decryption_full_words = [x for x in decryption_in_words if "_" not in x]
        f = self.flatten(decryption_in_words)
        print("Checking ", f)
        print("interrupter ", interrupter, self.gem.pos_to_eng(interrupter))
        print("interrupter_pos_set ", interrupter_pos_set)

        f2 = []
        for i, rune in enumerate(f):
            if rune == "_":
                f2.append(rune)
            elif i in interrupter_pos_set:
                print(i, " is an interrutper")
                f2.append(self.gem.pos_to_eng(interrupter))
            else:
                # f2.append(self.gem.pos_to_eng_dict_f[item])
                f2.append(self.gem.pos_to_eng(rune))

        #
        # ther is abug in this funciton
        # if there are interrutpers, we have to inlcud ethem#
        # by thsi stage we are workgin in nromal geamtrai positions
        # so its failry easy apart from the interrupter_pos_set
        # is the position in ct, so does not inldue the "_" cahr

        # Checking ['_', '_', '_', '_', '_', 18, 6, 1, 15, 1, 20, 23, 18, 4, 27, 4, 20, 21, 17, '_']

        # f2 = []
        # for item in f:
        #     if item == "_":
        #         f2.append(item)
        #     else:
        #         # f2.append(self.gem.pos_to_eng_dict_f[item])
        #         f2.append(self.gem.pos_to_eng(item))
        t2 = []
        for entry in self.ragged_partition(f2, ct_rune_word_len):
            t2.append("".join(entry))
        print("t2 = ", t2)
        return "  ".join(t2)  # decrypt_and_get_ans_to_score

    def print_output(self, s):
        if self.should_print:
            print(s)

    def flatten(self, li):
        return sum(([x] if not isinstance(x, list) else self.flatten(x) for x in li), [])
