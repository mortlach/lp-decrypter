#!/usr/bin/env python3
from lp_data.lp_section_data import lp_sections_by_red_runes
from lp_data.lp_section_data import section1
from lp_data.lp_section_data import section2
from lp_data.lp_section_data import section3
from lp_data.lp_section_data import section4
from lp_data.lp_section_data import section5
from lp_data.lp_section_data import section6
from lp_data.lp_section_data import section7
from lp_data.lp_section_data import section8
from lp_data.lp_section_data import section9
from lp_data.lp_section_data import section10
from lp_data.lp_section_data import section11
from lp_data.lp_section_data import section12
from lp_data.lp_section_data import section13
from lp_data.lp_section_data import rr1
from lp_data.lp_section_data import rr2
from lp_data.lp_section_data import rr3
from lp_data.lp_section_data import rr4
from lp_data.lp_section_data import rr5
from lp_data.lp_section_data import rr6
from lp_data.lp_section_data import rr7
from lp_data.lp_section_data import rr8
from lp_data.lp_section_data import rr9
from lp_data.lp_section_data import rr10
from lp_data.lp_section_data import rr11
from lp_data.lp_section_data import rr12
from lp_data.lp_section_data import rr13
from lp_data.lp_section_data import rr14
from lp_data.lp_section_data import rr15
from lp_data.lp_section_data import rr16
import os


class LiberPrimusText(object):
    '''
        holds the text of the LP, divided into sections (defined by red runes (rr) or side art (section) )
        Then simple functions to get the data
    '''
    lp_start_end_data = {'1': section1, '2': section2, '3': section3, '4': section4, '5': section5, '6': section6, '7': section7, '8': section8,
                         '9': section9, '10': section10, '11': section11, '12': section12, '13': section13, 1: section1, 2: section2, 3: section3,
                         4: section4, 5: section5, 6: section6, 7: section7, 8: section8, 9: section9, 10: section10, 11: section11, 12: section12,
                         13: section13}

    lp_rr = {'1': rr1, 1: rr1, '2': rr2, 2: rr2, '3': rr3, 3: rr3, '4': rr4, 4: rr4, '5': rr5, 5: rr5, '6': rr6, 6: rr6, '7': rr7, 7: rr7, '8': rr8,
             8: rr8, '9': rr9, 9: rr9, '10': rr10, 10: rr10, '11': rr11, 11: rr11, '12': rr12, 12: rr12, '13': rr13, 13: rr13, '14': rr14, 14: rr14,
             '15': rr15, 15: rr15, '16': rr16, 16: rr16}

    filedata = open(os.path.join(os.getcwd(), os.path.dirname(__file__), "liber-primus__transcription--master.txt"), encoding="utf8").read()
    intus = "\n".join(filedata.split('\n')[9:196])
    fiftyeightpages = "\n".join(filedata.split('\n')[196:])

    def __init__(self):
        self.fiftyeightlines = self.getLines(LiberPrimusText.fiftyeightpages)
        self.intuslines = self.getLines(LiberPrimusText.intus)

    def getText(self):
        '''

        :return:
        '''
        filedata = open(os.path.join(os.getcwd(), os.path.dirname(__file__), "liber-primus__transcription--master.txt"), encoding="utf8").read()
        # delimters = filedata.split('\n')[:7]
        # t1 = filedata.split('\n')[9:]
        self.intus = "\n".join(filedata.split('\n')[9:196])
        self.fiftyeightpages = "\n".join(filedata.split('\n')[196:])

    def getSection(self, part):
        return lp_sections_by_red_runes[part]

    def getSections(self, parts):
        r = []
        for section in parts:
            r.append(LiberPrimusText.lp_start_end_data[section]["all_words"])
        return r

    def getSectionWords(self, part):
        result = []
        for word in lp_sections_by_red_runes[part]:
            result.append(self.splitString(word))
        return result

    def getStartWords(self, sections):
        r = []
        for section in sections:
            r.append(LiberPrimusText.lp_start_end_data[section]["start_words"])
        print(r)
        return r

    def getEndWords(self, sections):
        r = []
        for section in sections:
            r.append(LiberPrimusText.lp_start_end_data[section]["end_words"])
        return r

    def getRedRunes(self, sections):
        r = []
        for section in sections:
            r.append(LiberPrimusText.lp_rr[section]["words"])
        return r

    def getStartEndWords(self, sections):
        r = []
        for section in sections:
            r.append(self.getStartWords([section])[0])
            r.append(self.getEndWords([section])[0])
        return r

    def getStartOrEndWords(self, sections, start_or_end_or_all):
        if start_or_end_or_all == "startAndEndWords":
            return self.getStartEndWords(sections)
        elif start_or_end_or_all == "startWords":
            return self.getStartWords(sections)
        elif start_or_end_or_all == "endWords":
            return self.getEndWords(sections)
        elif start_or_end_or_all == "allWords":
            return self.getSections(sections)
        return None

    def splitString(self, word):
        return [char for char in word]

    def getPages(self):
        pass

    def getLines(self, string):
        result = []
        result.append([item for item in string.split('\n') if item[-1] == '/'])
