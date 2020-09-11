from os import path


class data(object):
    '''

        data is class with a static dict also called data that is used by gui/controller,
        etc. classes to store data.

        This is done for convenience, whenever you need access to data in any class
        just create one of these objects, helping a lot during development.

    TODO as the code matures there will be better solutions to pass data around, especially
        if we do some threading properly
    '''
    data = {}  # data the main dictionary with values used throughout the app
    data["chosen_sections"] = []
    data["chosen_redrunes"] = []

    data["cipher_text"] = None
    data["cipher_text_lengths"] = None
    data["ct_order_list"] = None

    data["chosen_interrupters"] = None
    data["keys"] = None
    data["enc_data"] = None
    data["enc_map"] = None

    data["dec_map"] = None
    data["enc_map_name"] = None
    data["enc_map_text"] = None

    data["test_key_start_index"] = None
    data["test_interrupter"] = None

    data["4gram_count_cut"] = None
    data["4gram_max_no_scores"] = None
    data["4gram_min_score"] = None

    data["min_score_per_4gram_offset"] = None
    data["min_score_per_4gram_gradient"] = None
    data["four_gram_log_prob_min"] = None
    data["four_gram_max_num_zero_count"] = None
    data["four_gram_count_cut"] = None

    ''' used for checking decrypted words against crib words, 
    how many different chars are allowed ?? '''
    data["1_rune_char_dif"] = None
    data["2_rune_char_dif"] = None
    data["3_rune_char_dif"] = None
    data["4_rune_char_dif"] = None
    data["5_rune_char_dif"] = None
    data["6_rune_char_dif"] = None
    data["7_rune_char_dif"] = None
    data["8_rune_char_dif"] = None
    data["9_rune_char_dif"] = None
    data["10_rune_char_dif"] = None
    data["11_rune_char_dif"] = None
    data["12_rune_char_dif"] = None
    data["13_rune_char_dif"] = None
    data["14_rune_char_dif"] = None

    data["answers"] = []
    data["cancel_thread"] = False

    data["use_reverse_keys"] = None
    data["cancel_thread"] = None
    data["wrap_key_around_ct"] = None

    data["undefined_answers_are_all"] = None
    data["use_reverse_keys"] = None
    data["score_reversed_text"] = None
    # test stuff
    data["test_pt"] = None
    data["test_pt_index"] = None
    data["test_interrupter"] = None
    data["test_pt_order"] = None
    data["test_pt_shift"] = None
    data["test_pt_word_Length"] = None
    data["test_key"] = None
    data["test_key_string"] = None
    data["test_key_eng"] = None
    data["test_key_order"] = None
    data["test_key_shift"] = None
    data["test_key_start_index"] = None
    # cipher text gematria order and shifts
    data["ct_use_gematria_forward"] = None
    data["ct_use_gematria_reverse"] = None
    data["ct_gematria_forward_shifts"] = None
    data["ct_gematria_reverse_shifts"] = None
    data["key_use_gematria_forward"] = None
    data["key_use_gematria_reverse"] = None
    data["key_gematria_forward_shifts"] = None
    data["key_gematria_reverse_shifts"] = None

    data["results_table_string"] = None

    # default folder locations
    data["key_folder"] = path.join(path.dirname(path.abspath(__file__)), 'keys')
    data["encrypt_data"] = path.join(path.dirname(path.abspath(__file__)), 'encryption_table')
    data["enc_map_folder"] = path.join(path.dirname(path.abspath(__file__)), 'enc_map_data')
    data["save_results"] = path.join(path.dirname(path.abspath(__file__)), 'save_results')

    def __init__(self):
        pass

    def print_test_encryption_settings(self):
        print("print_test_encryption_settings")
        print("test_interrupter = ", self.data["test_interrupter"])
        print("test_pt_order = ", self.data["test_pt_order"])
        print("test_pt_shift = ", self.data["test_pt_shift"])
        print("test_key_order = ", self.data["test_key_order"])
        print("test_key_shift = ", self.data["test_key_shift"])
        print("test_key_start_index = ", self.data["test_key_start_index"])

    def print_gematria_settings(self):
        print("print_gematria_settings")
        print("ct_use_gematria_forward = ", self.data["ct_use_gematria_forward"])
        print("ct_use_gematria_reverse = ", self.data["ct_use_gematria_reverse"])
        print("ct_gematria_forward_shifts = ", self.data["ct_gematria_forward_shifts"])
        print("ct_gematria_reverse_shifts = ", self.data["ct_gematria_reverse_shifts"])
        print("key_use_gematria_forward = ", self.data["key_use_gematria_forward"])
        print("key_use_gematria_reverse = ", self.data["key_use_gematria_reverse"])
        print("key_gematria_forward_shifts = ", self.data["key_gematria_forward_shifts"])
        print("key_gematria_reverse_shifts = ", self.data["key_gematria_reverse_shifts"])
