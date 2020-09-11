from os.path import splitext
from os.path import basename


class encryption(object):
    '''
        The basis of this method assumes a three column string as the input
        This string can be passed in, read from file, or can be generated from an expression
        assumes the file formatting is:
        each lines: three space/tab separated columns, of numbers, 0,1,...,27,28  representing
        runes,
        (use what ever convention you prefer for assigning the runes a number between 0 and 28,
        just be consistent, however in other classes an order is assumed (e.g. text scoring))
        column 1 is plaintext rune  column 2 is Key rune    column 3 is cipher rune
        for example, file for plus: encryption function plaintext + key % 29 = cipher_text
        plus
        0   0   0
        0   1   1
        0   2   2
        ...
        28  27  26
        28  28  27

        This string is then converted into the encryption data as nested arrays
        These arrays are then re=arranged to get the decryption data, which is stored in a
        dictionary,
        This is used to decrypt text with a given key
        Encryption Methods have an associated name and are stored as tuples
        enc_data  =  (name, data ) # name is a string, data is an array defined above
        The name is passed on or taken from the filename

    '''

    # TODO replace MAP with dict

    def __init__(self):
        self.enc_data = None
        self.dec_data = None
        self.dec_map = None
        self.enc_map = None

    def m29(self, k):
        '''
            mod 29 todo: memoize might be faster over millions of calls to this
        '''
        if isinstance(k, int):
            return k % 29
        return k

    def encryptionDatFromStringExpression(self, f, name="encryption_name"):
        '''
        converts a 'simple' python expression passed as a string into encryption data as a string
        results will automatically be calculated mod 29
        :param f: encryption function of two variables (must be letters p and k )
        :param name: the name of the encryption function,
        :return: string for the encryption data
        '''
        r = range(0, 29)
        s = "".join(
            [str(p) + "\t" + str(k) + "\t" + str(self.m29(eval(f))) + "\n" for p in r for k in
             r]).rstrip('\r\n')
        return self.encryptionDatFromString(s, name)

    def encryptionDataFromFile(self, file):
        '''
        reads file data as string , assumes it is
        :param file: input file to parse
        :return: enc_data as nested array of integers
        '''
        with open(file, "r") as f:
            s = f.read()
        return self.encryptionDatFromString(s, splitext(basename(file))[0])

    def encryptionDatFromString(self, s, name="encryption_name"):
        '''
        correctly formatted string is parsed into encryption array data
        :param s: input string
        :param name: name of encryption function
        :return: enc_data as nested array of integers
        '''
        return self.encryptionDataFromStringArray(s.split('\n'), name)

    def int_or_false(self, string):

        if string == "False":
            return string
        return int(string)

    def encryptionDataFromStringArray(self, s, name="encryption_name"):
        '''
        We do a bit of checking here, you must pass in 841 values (any mro ewill be ignored)
        :param s: a list of strings that will be converted to numbers for the map
        :param name: the name of this method
        :return: a dictionary of tuple input and the resultant cipher_text  (pt_i, key_j) :
        cipher_text_ij
        '''
        assert len(s) >= 841
        a = s[0:841]
        result = []
        for item in a:
            result.append(
                [self.m29(self.int_or_false(numeric_string)) for numeric_string in item.split()])
        self.enc_data = (name, result)
        self.dec_data = None  # reset dec data now we have new enc_data
        return self.enc_data

    def encryptionDataToDecryptionMap(self, enc_data, undefined_answers_are_all=False):
        '''
        using enc_data: find all cipher_runes that can be generated from each possible input
        Loop over all combinations of key rune and cipher rune, whilst finding items in the
        passed data that match each
        possibility. This method means some cipher text might not be possible with the passed
        data, or some cipher
        text might be able to be generated with mulitple plaintext runes
        We can quantify "how reversible" the passed method is by counting the number of different
        runes in eahc row /
        column
        of the "encryption table" TODO add a link
        :param enc_data:
        :param undefined_answers_are_all: flag for undefined results, (e.g. x/ 0 = undefined
        :return: the dec_data map    (key_j, cipher_text_ij) : pt_i
        '''
        (name, data) = enc_data
        r = range(0, 29)
        results = {}
        for i in r:
            for j in r:
                # TODO need to handle false
                # print("looking for ", i, j)
                ans = [x[0] for x in data if (x[2] == i) and (x[1] == j)]
                # print("ans = ", ans)
                results[(i, j)] = [x[0] for x in data if (x[2] == i) and (x[1] == j)]
                if results[(i, j)] == []:
                    results[(i, j)] = [False]
        self.dec_map = (name, results)
        # todo calculate "how reversible" the method is (column / row sum of unique elements)

        return results

    def encryptionDataToEncryptionMap(self, enc_data):
        '''
        using enc_data: to create an enc-dict
        :param enc_data:
        :return: the enc_dict (plaintext_j, key_i ): cipher_text_ij
        '''
        (name, d) = enc_data
        self.enc_map = {}
        for i in d:
            self.enc_map[tuple([i[0], i[1]])] = i[2]
        return self.enc_map  #
