from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
# from .QTableWidgetOverload import QTableWidgetOverload
# from .QTextEditOverload import QTextEditOverload
from view.ui_view import Ui_mainView
from enc.gematria import gematria
from data.data import data
from enc.encryption_maps import encryption
from lp_data.LiberPrimusText import LiberPrimusText
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QPlainTextEdit
# from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QButtonGroup
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import os
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE = True

##http://www.patorjk.com/software/taag/#p=display&f=Runic&t=WORDS
class view(QtWidgets.QMainWindow, Ui_mainView):
    '''
        GUIs are a pain, the plan here is to make it work and get the user data / options into
        the main data class / dictionary. When things settle down and we get some suggestions /
        comments and user experience this will likely get refactored a lot
        TODO honestly, just a mess, but it will get tidied up
    '''

    def __init__(self):
        super(view, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.white = "#ffffff"
        self.red = "#ff5733"
        self.green = "#75ff33"

        self.data = data().data
        self.gem = gematria()
        self.LP = LiberPrimusText()
        # connect up some widgets
        self.key_display_format_bg = QButtonGroup()
        for w in (self.key_display_format_layout.itemAt(i).widget() for i in range(self.key_display_format_layout.count())):
            w.toggled.connect(self.handle_key_display_format)
            self.key_display_format_bg.addButton(w)
        # connect up some widgets
        self.ct_display_format_bg = QButtonGroup()
        for w in (self.ct_display_format_layout.itemAt(i).widget() for i in range(self.ct_display_format_layout.count())):
            w.toggled.connect(self.handle_processLPText)
            self.ct_display_format_bg.addButton(w)
        # connect up some widgets
        self.test_key_display_format_bg = QButtonGroup()
        for w in (self.test_key_display_format_layout.itemAt(i).widget() for i in range(self.test_key_display_format_layout.count())):
            w.toggled.connect(self.handle_test_key_display)
            self.test_key_display_format_bg.addButton(w)
        # connect up some widgets
        self.test_pt_display_format_bg = QButtonGroup()
        for w in (self.test_pt_display_format_layout.itemAt(i).widget() for i in range(self.test_pt_display_format_layout.count())):
            w.toggled.connect(self.handle_test_pt_display)
            self.test_pt_display_format_bg.addButton(w)
        # connect up some widgets
        self.ct_word_choice_layout_bg = QButtonGroup()
        for w in (self.ct_word_choice_layout.itemAt(i).widget() for i in range(self.ct_word_choice_layout.count())):
            w.toggled.connect(self.handle_wordSelection)
            self.ct_word_choice_layout_bg.addButton(w)
        # connect up some widgets
        for w in (self.lpSection.itemAt(i).widget() for i in range(self.lpSection.count())):
            w.stateChanged.connect(self.handle_lpSection)
        # connect up some widgets
        for w in (self.ct_shift_layout.itemAt(i).widget() for i in range(
                self.ct_shift_layout.count())):
            w.stateChanged.connect(self.handle_ct_order_shift)
        # connect up some widgets
        for w in (self.key_shift_layout.itemAt(i).widget() for i in range(self.key_shift_layout.count())):
            w.stateChanged.connect(self.handle_key_order_shift)
        # connect up some widgets
        for w in (self.redrunes.itemAt(i).widget() for i in range(self.redrunes.count())):
            w.stateChanged.connect(self.handle_redrunes)
        # connect up some widgets
        self.interrupter_map = {}
        for w in (self.interrupter.itemAt(i).widget() for i in range(self.interrupter.count())):
            w.stateChanged.connect(self.handle_interrupter)
            self.interrupter_map[w] = w.objectName().split('_')[0]  # this is the interrupter letter for this widget
        # set up interrupter
        self.test_interrupter.addItem("None")
        for i in range(0, 29):
            self.test_key_gem_shift.addItem(str(i))
            self.test_plaintext_gem_shift.addItem(str(i))
            self.test_interrupter.addItem(self.gem.latin_fragments[i])
        self.test_plaintext_gem_shift.setCurrentIndex(0)
        self.test_key_gem_shift.setCurrentIndex(0)
        self.test_interrupter.setCurrentIndex(0)
        self.handle_test_interrupter()

        # test tab
        self.test_key_entry.editingFinished.connect(self.handle_test_key_display)
        self.test_key_gem_order.currentIndexChanged.connect(self.handle_test_key_display)
        self.test_key_gem_shift.currentIndexChanged.connect(self.handle_test_key_display)

        self.test_plaintext_entry.editingFinished.connect(self.handle_test_pt_display)
        self.test_plaintext_gem_order.currentIndexChanged.connect(self.handle_test_pt_display)
        self.test_plaintext_gem_shift.currentIndexChanged.connect(self.handle_test_pt_display)
        # tets interrupter
        self.test_interrupter.currentIndexChanged.connect(self.handle_test_interrupter)
        self.test_key_start_index.valueChanged.connect(self.handle_test_key_start_index)

        self.enc_method_function_textbox.editingFinished.connect(self.handle_encryptionMapTextEntry)
        # main key tab
        self.key_entry_textedit.setOverwriteMode(True)
        self.processed_key_display_textedit.setEnabled(True)
        self.key_entry_textedit.focusOutEventSignal.connect(self.handle_key_entry)
        self.key_entry_textedit.enter_pressed.connect(self.handle_key_entry)
        self.handle_key_entry()
        self.key_runes_eng_radio.setChecked(True)
        self.load_key_file_button.clicked.connect(self.handle_loadKeyFile)
        self.save_key_file_button.clicked.connect(self.handle_saveKeyFile)
        # encryption tab
        self.encryption_map_text_entry.focusOutEventSignal.connect(self.handle_encryptionMapTableEntry)
        self.encryption_map_text_entry.enter_pressed.connect(self.handle_encryptionMapTableEntry)

        self.rune_key_sample.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.english_key_sample.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.number_key_sample.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.save_setup_button.clicked.connect(self.handle_saveSetup)
        self.load_setup_button.clicked.connect(self.handle_loadSetup)
        self.set_default_button.clicked.connect(self.handle_setDefault)

        self.four_gram_count_cut.editingFinished.connect(self.handle_FourGramCountCut)
        # cipher text tab
        self.cipherTextPad.focusOutEventSignal.connect(self.handle_manual_ct_entry)
        self.cipherTextPad.enter_pressed.connect(self.handle_manual_ct_entry)
        self.cipherTextPad.setToolTip("Alternatively edit text or paste in chosen cipher text matching chosen display format")

        self.undefined_answers_are_all.stateChanged.connect(self.handle_undefined_answers_are_all)
        self.use_reverse_keys.stateChanged.connect(self.handle_use_reverse_keys)
        self.score_reversed_decryption.stateChanged.connect(self.handle_score_reversed_decryption)
        self.handle_score_reversed_decryption()
        self.wrap_key_around_ct.stateChanged.connect(self.handle_wrap_key_around_ct)
        self.handle_wrap_key_around_ct()
        # scoring tab widgets
        self.min_score_per_4gram_offset.valueChanged.connect(self.handle_min_score_per_4gram_offset)
        self.handle_min_score_per_4gram_offset()
        self.min_score_per_4gram_gradient.valueChanged.connect(self.handle_min_score_per_4gram_gradient)
        self.handle_min_score_per_4gram_gradient()
        self.four_gram_log_prob_min.valueChanged.connect(self.handle_four_gram_log_prob_min)
        self.handle_four_gram_log_prob_min()
        self.four_gram_count_cut.valueChanged.connect(self.handle_four_gram_count_cut)
        self.handle_four_gram_count_cut()
        self.four_gram_max_num_zero_count.valueChanged.connect(self.handle_four_gram_max_num_zero_count)
        self.use_reverse_keys.stateChanged.connect(self.handle_use_reverse_keys)
        # self.undefined_answers_are_all.stateChanged.connect(self.handle_score_options)
        self.save_rejected_results.setEnabled(False)

        self.cipherTextOrderTextPad.focusOutEventSignal.connect(self.handle_custum_ct_order)
        self.cipherTextOrderTextPad.enter_pressed.connect(self.handle_custum_ct_order)
        self.cipherTextOrderTextPad.setToolTip("For custom orders, manually edit/paste indexing")
        self.tb_lr_ciphertext_order.toggled.connect(self.handle_ct_order)
        self.bt_rl_ciphertext_order.toggled.connect(self.handle_ct_order)
        self.custom_ciphertext_order.toggled.connect(self.handle_custum_ct_order)

        # self.custom_ciphertext_order.toggled.connect(self.handle_ct_order)

        self.setDefaultGuiSate()
        # set up encryption
        self.encryptor = encryption()
        #        self.handle_processEncryptionFile()

        self.handle_setDefault()

        self.pre_computed_encryption_map_combobox.currentIndexChanged.connect(self.handle_pre_computed_encryption_map_combobox)

        print("pre_computed_encryption_map_combobox ")
        self.pre_computed_encryption_map_combobox.setCurrentIndex(6)
        self.handle_pre_computed_encryption_map_combobox()

        self.pre_computed_encryption_map_load.clicked.connect(self.handle_pre_computed_encryption_map_load)


        # self.handle_testPlaintextEntry()

        self.setRunesOrEnglish()

        self.handle_test_key_start_index()

        self.handle_FourGramCountCut() # TODO moVE
        self.textWindowList = []

        self.fileMenu = self.menubar.addMenu("File")
        self.save = QAction("Load", self)
        self.save.setShortcut("Ctrl+L")
        self.fileMenu.addAction(self.save)
        self.save = QAction("Save", self)
        self.save.setShortcut("Ctrl+S")
        self.fileMenu.addAction(self.save)

        self.fileMenu.triggered[QAction].connect(self.handle_fileMenu)


        # todo loads of tool tips to write
        self.four_gram_count_cut.setToolTip("score to give a 4-gram that is not in the data (e.g not found in project Guttenburg")
        self.test_enc_method_4.setToolTip("score to give a 4-gram that is not in the project Guttenburg (or cut see above)")
        self.use_reverse_keys.setToolTip("Each key is reversed and used as a key")
        self.test_enc_method_14.setToolTip("Each key is reversed and used as a key")
        self.score_reversed_decryption.setToolTip("Each decrypted plaintext is also reversed and scored")
        self.test_enc_method_16.setToolTip("Each decrypted plaintext is also reversed and scored")
        self.four_gram_log_prob_min.setToolTip("score to give a 4-gram that is not in the data (e.g not found in project Guttenburg")
        self.log_prob_min_lab.setToolTip("score to give a 4-gram that is not in the project Guttenburg (or cut see above)")
        self.interrupterGroupBox.setToolTip("choose interrupter runes to be used")
        self.ct_shift_groupbox.setToolTip("choose order/shift to use for cipher text")
        self.key_shift_groupbox.setToolTip("choose order/shift to use for keys")
        self.lp_section1.setToolTip("0.jpg to 2.jpg")
        self.lp_section2.setToolTip("3.jpg")
        self.lp_section3.setToolTip("3.jpg to 6.jpg")
        self.lp_section4.setToolTip("6.jpg to 7.jpg")
        self.lp_section5.setToolTip("8.jpg to 14.jpg")
        self.lp_section6.setToolTip("15.jpg to 22.jpg")
        self.lp_section7.setToolTip("23.jpg to 26.jpg")
        self.lp_section8.setToolTip("27.jpg to 32.jpg")
        self.lp_section9.setToolTip("33.jpg")
        self.lp_section10.setToolTip("33.jpg to 39.jpg")
        self.lp_section11.setToolTip("39.jpg")
        self.lp_section12.setToolTip("40.jpg to 53.jpg")
        self.lp_section13.setToolTip("54.jpg to 55.jpg")

        self.min_distance_1rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_2rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_3rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_4rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_5rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_6rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_7rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_8rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_9rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_10rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_11rune.valueChanged.connect(self.handle_max_char_difference_values)
        self.min_distance_12rune.valueChanged.connect(self.handle_max_char_difference_values)


        self.tb_lr_ciphertext_order.setEnabled(False)
        self.bt_rl_ciphertext_order.setEnabled(False)
        self.custom_ciphertext_order.setEnabled(False)
        self.cipherTextOrderTextPad.setEnabled(False)

        # self.startWords.stateChanged.connect(self.handle_processLPText)
        # self.endWords.stateChanged.connect(self.handle_processLPText)
        # self.startAndEndWords.stateChanged.connect(self.handle_processLPText)
        # self.allWords.stateChanged.connect(self.handle_processLPText)

        self.custom_ciphertext_order.setToolTip("manually paste in an order")

        self.handle_test_key_display()
        self.handle_test_pt_display()

        self.results_table.cellClicked.connect(self.handle_results_cell_clicked)
        self.results_table.cellActivated.connect(self.handle_results_cell_active)
        # self.results_table.currentRowChanged.connect(self.handle_results_cell_active)
        # set button context menu policy

        self.results_model_item = self.results_table.selectionModel()

        self.results_table.reject_action.triggered.connect(self.handle_reject)
        self.results_table.move_to_top_action.triggered.connect(self.handle_move_to_top_action)
        self.results_table.copy_all_action.triggered.connect(self.handle_copy_all_action)
        self.results_table.copy_selection_action.triggered.connect(self.handle_copy_selection_action)

        self.pop_results_to_windows.clicked.connect(self.pop_answers)

        self.save_results_to_file.clicked.connect(self.save_answers)
        self.copy_results_to_file.clicked.connect(self.copy_answers)


        # setPlaceholderText("enter function")
        # setPlaceholderText("enter function name")
        self.handle_max_char_difference_values()

    def handle_pre_computed_encryption_map_load(self):
        print("handle_pre_computed_encryption_map_load")
        self.data["enc_map_folder"] = self.generic_file_dialog(path=self.data["enc_map_folder"],
                                                               type="dir")  #
        print("self.data[enc_map_folder]", self.data["enc_map_folder"])
        self.update_pre_computed_enc_map_combobox()

    def update_pre_computed_enc_map_combobox(self):
        print("update_pre_computed_enc_map_combobox")
        # get the file names
        file_path = self.data["enc_map_folder"]
        print("file_path = ",file_path)
        directories = os.listdir(file_path)
        print("directories = ", directories)
        self.pre_computed_encryption_map_combobox.clear()
        print("try")
        try:
            onlyfiles = [f for f in directories if os.path.isfile(os.path.join(file_path, f))]

            print("onlyfiles = ", onlyfiles)

            self.pre_computed_encryption_map_combobox.addItems(onlyfiles)
            self.pre_computed_encryption_map_combobox.setCurrentIndex(0)
        except:
            pass

    def handle_pre_computed_encryption_map_combobox(self):
        print("handle_pre_computed_encryption_map_combobox")
        if self.pre_computed_encryption_map_combobox.currentText() != '':
            print("success",self.pre_computed_encryption_map_combobox.currentText()  )
            fp = os.path.join(self.data["enc_map_folder"],
                              self.pre_computed_encryption_map_combobox.currentText())
            #fp = os.getcwd(), 'data','./enc_map_data/' + self.pre_computed_encryption_map_combobox.currentText()
            try:
                print("try 334")
                self.data["enc_data"] = self.encryptor.encryptionDataFromFile(fp)
                # for data saved in file the method names comes from the file name
                self.data["enc_map_name"] = self.data["enc_data"][0]
                # from the enc data get the enc map
                self.data["enc_map"] = self.encryptor.encryptionDataToEncryptionMap(self.data["enc_data"])
                self.getDecMapAndDisplay()
                ''' use some color, to show how its done, help make things more intuitive ? '''
                # TODO maybe add in a other color based gui hints
                self.pre_computed_encryption_map_combobox.setStyleSheet("color: black; "
                                                                        "background-color: " + self.green)
            except:
                print("except",)
                self.pre_computed_encryption_map_combobox.clear()
                self.pre_computed_encryption_map_combobox.setStyleSheet(
                    "color: black; background-color: " + self.red)
        else:
            print("else", self.pre_computed_encryption_map_combobox.currentText() )
            self.pre_computed_encryption_map_combobox.setStyleSheet("color: black; background-color: " + self.red)

    def handle_copy_all_action(self):
        print("handle_copy_all_action")
        str = ""
        print("rowCount() = ", self.results_table.rowCount())
        print("columnCount() = ", self.results_table.columnCount())
        input()
        for r in range(0, self.results_table.rowCount()):
            for c in range(0, self.results_table.columnCount()):
                str += self.results_table.item(r, c).text() + '\t'
            str += "\n"
        print("FIN")
        print(str)

    def handle_copy_selection_action(self):
        pass
    #         for item in self.results_model_item.selectedRows():
    #             r = item.row()
    # #           d

    def handle_max_char_difference_values(self):
        self.data["1_rune_char_dif"] = self.min_distance_1rune.value()
        self.data["2_rune_char_dif"] = self.min_distance_2rune.value()
        self.data["3_rune_char_dif"] = self.min_distance_3rune.value()
        self.data["4_rune_char_dif"] = self.min_distance_4rune.value()
        self.data["5_rune_char_dif"] = self.min_distance_5rune.value()
        self.data["6_rune_char_dif"] = self.min_distance_6rune.value()
        self.data["7_rune_char_dif"] = self.min_distance_7rune.value()
        self.data["8_rune_char_dif"] = self.min_distance_8rune.value()
        self.data["9_rune_char_dif"] = self.min_distance_9rune.value()
        self.data["10_rune_char_dif"] = self.min_distance_10rune.value()
        self.data["11_rune_char_dif"] = self.min_distance_11rune.value()
        self.data["12_rune_char_dif"] = self.min_distance_12rune.value()
        self.data["13_rune_char_dif"] = self.min_distance_13rune.value()
        self.data["14_rune_char_dif"] = self.min_distance_14rune.value()

    def handle_enc_method_load_data_path(self):
        print("handle_enc_method_load_data_path")

    def handle_move_to_top_action(self):
        print("handle_move_to_top_action")

        # for item in self.results_model_item.selectedRows():
        #     print("row = ", item.row() )
        for item in self.results_model_item.selectedRows():
            r = item.row()
            item1 = self.results_table.takeItem(r, 0)
            item2 = self.results_table.takeItem(r, 1)
            self.results_table.removeRow(r)
            self.results_table.insertRow(0)
            self.results_table.setItem(0, 0, item1)
            self.results_table.setItem(0, 1, item2)

    # print(1)
    # item1 = self.results_table.takeItem(1,0)
    # item2 = self.results_table.takeItem(1,1)
    # self.results_table.removeRow(1)
    # print(2)
    # self.results_table.insertRow(0)
    # self.results_table.setItem(0, 0, item1)
    # self.results_table.setItem(0, 1, item2)
    # print(3)

    def handle_reject(self):
        print("handle_reject")
        for item in reversed(self.results_model_item.selectedRows()):
            print("row = ", item.row())
            self.results_table.removeRow(item.row())

    def handle_results_cell_clicked(self, row, col):
        print("handle_results_cell_clicked, ", row, col)

    def handle_results_cell_active(self, row, col):
        print("handle_results_cell_active, ", row, col)

    def handle_min_score_per_4gram_offset(self):
        print("handle_min_score_per_4gram_offset")
        self.data["min_score_per_4gram_offset"] = self.min_score_per_4gram_offset.value()

    def handle_min_score_per_4gram_gradient(self):
        print("handle_min_score_per_4gram_gradient")
        self.data["min_score_per_4gram_gradient"] = self.min_score_per_4gram_gradient.value()

    def handle_four_gram_log_prob_min(self):
        print("handle_four_gram_log_prob_min")
        self.data["four_gram_log_prob_min"] = self.four_gram_log_prob_min.value()

    def handle_four_gram_count_cut(self):
        print("handle_four_gram_count_cut")
        self.data["four_gram_count_cut"] = self.four_gram_count_cut.value()

    def handle_four_gram_max_num_zero_count(self):
        print("handle_four_gram_max_num_zero_count")
        self.data["four_gram_max_num_zero_count"] = self.four_gram_max_num_zero_count.value()

    def handle_undefined_answers_are_all(self):
        print("handle_undefined_answers_are_all")
        if self.undefined_answers_are_all.isChecked():
            self.data["undefined_answers_are_all"] = True
        else:
            self.data["undefined_answers_are_all"] = False

    def handle_use_reverse_keys(self):
        print("handle_use_reverse_keys")
        if self.use_reverse_keys.isChecked():
            self.data["use_reverse_keys"] = True
        else:
            self.data["use_reverse_keys"] = False

    def handle_wrap_key_around_ct(self):
        if self.score_reversed_decryption.isChecked():
            self.data["wrap_key_around_ct"] = True
        else:
            self.data["wrap_key_around_ct"] = False


    def handle_score_reversed_decryption(self):
        print("handle_score_reversed_decryption")
        if self.score_reversed_decryption.isChecked():
            self.data["score_reversed_decryption"] = True
        else:
            self.data["score_reversed_decryption"] = False

    def handle_test_interrupter(self):
        print("\nhandle_test_interrupter")
        self.data["test_interrupter"] = self.test_interrupter.currentText()
        if self.data["test_interrupter"] == "None":
            self.data["test_interrupter_p"] = None
        else:
            # !!!!!!!!!!!!! we define the interrupter to be the letter in the un-shifted PT
            # however when we run decryptions we will add an option to assume it can be rotated
            self.data["test_interrupter_p"] = self.gem.encode_as_position([self.data["test_interrupter"]], "forward", 0)[
                0]  # shifted_interrupter = self.gem.encode_as_position( [self.gui.test_interrupter.currentText()],
            # self.gui.test_gem_order_pt.currentText(),  # self.gui.test_gem_shift_pt.currentText())[0]
        print("self.data[test_interrupter] = ", self.data["test_interrupter"])
        print("self.data[test_interrupter_p] = ", self.data["test_interrupter_p"])
        self.encrypt_test_data()

    def handle_test_key_display(self):
        print("\nhandle_test_key_display")
        self.data["test_key_order"] = self.test_key_gem_order.currentText()
        self.data["test_key_shift"] = int(self.test_key_gem_shift.currentText())
        self.data["test_key"] = self.gem.process_string_to_type_with_order_and_shift(self.test_key_entry.text(), "runes", self.data["test_key_order"],
                                                                                     self.data["test_key_shift"])
        print("self.data[test_key] ", self.data["test_key"])
        sender = self.test_key_display_format_bg.checkedButton()
        if sender == self.test_key_runes_radio:
            display_key_list = self.data["test_key"][0]
        elif sender == self.test_key_runes_eng_radio:
            display_key_list = self.gem.rune_to_eng(self.data["test_key"][0])
        elif sender == self.test_key_prime_radio:
            display_key_list = [str(x) for x in self.gem.rune_to_prime_value(self.data["test_key"][0])]
        elif sender == self.test_key_forward_position_radio:
            display_key_list = [str(x) for x in self.gem.encode_as_forward_position(self.data["test_key"][0])]
        elif sender == self.test_key_reverse_position_radio:
            display_key_list = [str(x) for x in self.gem.encode_as_reverse_position(self.data["test_key"][0])]
        else:
            print("else")
            display_key_list = self.data["test_key"][0]
        print(display_key_list)
        print([",".join(x) for x in display_key_list])
        self.test_key_out.setText(",".join(display_key_list))
        self.encrypt_test_data()

    def handle_test_pt_display(self):
        print("\nhandle_test_pt_display")
        self.data["test_pt_order"] = self.test_plaintext_gem_order.currentText()
        self.data["test_pt_shift"] = int(self.test_plaintext_gem_shift.currentText())
        # convert string to runes (NB we use a function that assumes this can be multiple items, so this is a nested list)
        self.data["test_pt"] = self.gem.process_string_to_type_with_order_and_shift(self.test_plaintext_entry.text(), "runes",
                                                                                    self.data["test_pt_order"], self.data["test_pt_shift"])
        print("self.data[test_pt] ", self.data["test_pt"])

        self.data["test_pt_word_Length"] = self.gem.process_string_to_type_word_length(self.test_plaintext_entry.text())
        print("self.data[test_pt_word_Length] ", self.data["test_pt_word_Length"])

        self.set_pt_index_range_key_can_be_applied()

        sender = self.test_pt_display_format_bg.checkedButton()
        disp = []
        if sender == self.test_pt_runes_radio:
            display_key_list = self.data["test_pt"][0]
            for item in self.ragged_partition(display_key_list, self.data["test_pt_word_Length"][0]):
                disp.append("".join(item))
        elif sender == self.test_pt_runes_eng_radio:
            display_key_list = self.gem.rune_to_eng(self.data["test_pt"][0])
            for item in self.ragged_partition(display_key_list, self.data["test_pt_word_Length"][0]):
                disp.append(" ".join(item))
        elif sender == self.test_pt_prime_radio:
            display_key_list = [str(x) for x in self.gem.rune_to_prime_value(self.data["test_pt"][0])]
            for item in self.ragged_partition(display_key_list, self.data["test_pt_word_Length"][0]):
                disp.append(" ".join(item))
        elif sender == self.test_pt_forward_position_radio:
            display_key_list = [str(x) for x in self.gem.encode_as_forward_position(self.data["test_pt"][0])]
            for item in self.ragged_partition(display_key_list, self.data["test_pt_word_Length"][0]):
                disp.append(" ".join(item))
        elif sender == self.test_pt_reverse_position_radio:
            display_key_list = [str(x) for x in self.gem.encode_as_reverse_position(self.data["test_pt"][0])]
            for item in self.ragged_partition(display_key_list, self.data["test_pt_word_Length"][0]):
                disp.append(" ".join(item))
        else:
            print("else")
            display_key_list = [self.gem.eng_to_rune(x) for x in self.data["test_pt"][0]]
            for item in self.ragged_partition(display_key_list, self.data["test_pt_word_Length"][0]):
                disp.append("".join(item))
        print("display_key_list = ", display_key_list)

        self.test_plain_text_runes.setText("  ".join(disp))
        self.encrypt_test_data()

    def ragged_partition(self, list, wordlen):
        decryption3 = []
        for length in wordlen:
            decryption3.append(list[:length])
            del list[:length]
        # print(decryption3)
        return decryption3

    def set_pt_index_range_key_can_be_applied(self):
        self.test_key_start_index.setRange(0, len(self.data["test_pt"][0]))

    def handle_test_key_start_index(self):
        '''
            sets the index of the test plaintest that the first test key rune is applied to
        '''
        self.data["test_key_start_index"] = self.test_key_start_index.value()
        print("self.data[test_key_start_index] = ", self.data["test_key_start_index"])
        self.encrypt_test_data()

    def can_run_test_encrypt(self):
        '''
            test that all entries required to run a test encryption have been set
        :return: if test encrypt can be run
        '''
        if None in [self.data["test_pt"], self.data["test_key"], self.data["test_key_start_index"], self.data["test_pt_shift"],
                    self.data["test_pt_order"], self.data["test_key_order"], self.data["test_key_shift"]]:
            return False
        return True

    def encrypt_test_data(self):
        '''
            encrypt the test data stored in data, taken from the gui,
        '''
        print("\nencrypt_test_data")
        if self.can_run_test_encrypt():
            ''' ref to PT index to start the encryption, set in gui  '''
            key_start_index = self.data["test_key_start_index"]
            # print("self.data[test_key_start_index] = ", self.data["test_key_start_index"])
            # self.data_obj.print_test_encryption_settings()
            ''' test key from gui '''
            self.data["test_key_string"] = self.test_key_entry.text()

            self.data["test_key_eng"] = self.gem.process_string_to_type_with_order_and_shift(
                self.data["test_key_string"], "latin", "forward", 0)

            key_runes_p = self.gem.process_string_to_type_with_order_and_shift(
                self.test_key_entry.text(), "f_pos", self.data["test_key_order"],
                self.data["test_key_shift"])

            # print("key_runes_p = ", key_runes_p)

            # To handle interrupters, we need the plaintext in normal gematria
            # This is because we are choosing to define the interrupter as the PT rune in normal
            # gem encoding
            pt_runes_N = self.gem.process_string_to_type_with_order_and_shift(
                self.test_plaintext_entry.text(), "f_pos", "forward", 0)

            pt_runes_p = self.gem.process_string_to_type_with_order_and_shift(
                self.test_plaintext_entry.text(), "f_pos", self.data["test_pt_order"],
                self.data["test_pt_shift"])

            print("pt_runes_N = ", pt_runes_N)
            print("pt_runes_p = ", pt_runes_p)
            # rotate the PT so that the first elemEnt is the start of the key
            print(key_start_index, key_start_index, key_start_index)
            pt_runes_p_rot = pt_runes_p[0][key_start_index:] + pt_runes_p[0][:key_start_index]
            pt_runes_N_rot = pt_runes_N[0][key_start_index:] + pt_runes_N[0][:key_start_index]
            print("pt_runes_N_rot = ", pt_runes_N_rot)
            print("pt_runes_p_rot = ", pt_runes_p_rot)
            print("interrupter = ", self.data["test_interrupter_p"])
            # encrypt
            key_index = 0
            ct_rot = []
            for pt_rune, pt_rune_N in zip(pt_runes_p_rot, pt_runes_N_rot):
                # print("encrypt pt_rune = ", pt_rune )
                if pt_rune_N == self.data["test_interrupter_p"]:
                    # print("interrupter ")
                    ct_rot.append(self.data["test_interrupter_p"])
                elif key_index == len(key_runes_p[0]):
                    # print("key finished")
                    ct_rot.append(pt_rune)
                else:
                    # print("encrypt, ", pt_rune, " ,", key_runes_p[0][key_index])
                    ct_rot.append(self.data["enc_map"][(pt_rune, key_runes_p[0][key_index])])
                    key_index += 1
            # now rotate left to return PT adn CT to original psoitions
            # pt_runes = pt_runes[-key_start_index:] + pt_runes[:-key_start_index]
            ct = ct_rot[-key_start_index:] + ct_rot[:-key_start_index]
            print("ct = ", ct)
            # convert the CT into the different possible display formats and display them all

            # TODO this breaks if there are FALSE answers in the ct,
            # TODO in general its not clear what to do with functions that can give undefined
            # output
            ct_eng = self.gem.pos_to_eng(ct)
            ct_rune = self.gem.eng_to_rune(ct_eng)
            ct_prime = [str(x) for x in self.gem.eng_to_prime_value(ct_eng)]
            ct_fpos = [str(x) for x in self.gem.encode_as_forward_position(ct_eng)]
            ct_rpos = [str(x) for x in self.gem.encode_as_reverse_position(ct_eng)]

            # TODO: display the ct as words with spaces, better formatting 
            print([ct_eng, ct_rune, ct_prime, ct_fpos, ct_rpos])
            self.test_ct_out_eng.setText(",".join(ct_eng))
            self.test_ct_out_rune.setText(",".join(ct_rune))
            self.test_ct_out_prime.setText(",".join(ct_prime))
            self.test_ct_out_fpos.setText(",".join(ct_fpos))
            self.test_ct_out_rpos.setText(",".join(ct_rpos))

            self.data["test_ct"] = [self.ragged_partition(ct_rune, self.data["test_pt_word_Length"][0])]
            print("self.data[test_ct] = ", self.data["test_ct"])

    def handle_encryptionMapTableEntry(self):
        print("handle_encryptionMapTextEntry")
        text = self.encryption_map_text_entry.toPlainText().replace(",", " ").replace("\t", " ")
        # print(text)
        # print("enc_map_name = ",  text.splitlines()[0])
        # print("enc_map_name = ",  self.data["enc_map_name"])
        # print("enc_map_text = ",  self.data["enc_map_text"])
        # print("enc_map_text = ",  "\n".join(text.splitlines()[1:]))
        self.data["enc_map_text"] = "\n".join(text.splitlines()[1:])
        self.data["enc_map_name"] = text.splitlines()[0]
        self.data["enc_data"] = self.encryptor.encryptionDatFromString(self.data["enc_map_text"], self.data["enc_map_name"])
        # self.data["enc_map"] = self.encryptor.encryptionDatFromString(self.data["enc_map_text"],
        #                                                               self.data["enc_map_name"])
        self.getDecMapAndDisplay()

    def handle_key_entry(self):
        '''
            the main text entry widget in the KEY table, write or copy keys into this pad for processing
            TODO: get rid of this function and join with the one it calls
        '''
        print("handle_key_entry")
        text = self.key_entry_textedit.toPlainText()
        self.data["keys"] = self.gem.process_string_to_latin_forward(self.key_entry_textedit.toPlainText())
        #print("self.data[keys]  = ", self.data["keys"])
        self.handle_key_display_format()

    def handle_key_display_format(self):
        '''
            convert self.data["keys"] to the requested format and display in processed_key_display_textpad
            TODO: functionality from here could go in general function, as the conversion is required in other functions
        '''
        print("handle_key_display_format")
        #print("self.data[keys] = ", self.data["keys"])
        sender = self.key_display_format_bg.checkedButton()
        display_key_list = []
        if sender == self.key_runes_radio:
            display_key_list = [self.gem.eng_to_rune(x) for x in self.data["keys"]]
        elif sender == self.key_runes_eng_radio:
            display_key_list = self.data["keys"]
        elif sender == self.key_prime_radio:
            for key in [self.gem.eng_to_prime_value(x) for x in self.data["keys"]]:
                display_key_list.append([str(x) for x in key])
        elif sender == self.key_forward_position_radio:
            for key in [self.gem.encode_as_forward_position(x) for x in self.data["keys"]]:
                display_key_list.append([str(x) for x in key])
        elif sender == self.key_reverse_position_radio:
            for key in [self.gem.encode_as_reverse_position(x) for x in self.data["keys"]]:
                display_key_list.append([str(x) for x in key])
        else:
            display_key_list = [self.gem.eng_to_rune(x) for x in self.data["keys"]]
        # display to gui, adn count keys
        display_key_list = [self.flatten(x) for x in display_key_list if x is not None]
        self.processed_key_display_textedit.setPlainText("\n".join([",".join(x) for x in display_key_list]))
        self.key_count_label.setText(str(len(self.data["keys"])) + " Keys")
        self.number_of_keys.setText(str(len(self.data["keys"])))

    def handle_fileMenu(self, q):
        print("menuAct")
        print(q.text() + " is triggered")

    def pop_answers(self):
        print("pop_answers")
        # print('pop_answers  pop_answers')
        textWindow = QPlainTextEdit()
        textWindow.setReadOnly(False)
        # get column headers
        # col_headers = [""]
        # for i in range(0,self.results_table.columnCount()):
        #     #print("col_headers = ", col_headers)
        #     #print("item text = ", self.results_table.horizontalHeaderItem(i).text())
        #     col_headers.append(self.results_table.horizontalHeaderItem(i).text())
        # #print(col_headers)
        # print_data = []
        # for r in range(0,self.results_table.rowCount()):
        #     row_data = [str(r)]
        #     for c in range(0,self.results_table.columnCount()):
        #         row_data.append(self.results_table.item(r,c).text())
        #     print_data.append(row_data)
        #print(tabulate(print_data, headers=col_headers))

        fileText = self.data["results_table_string"]
        textWindow.setPlainText(fileText)
        textWindow.resize(1750, 500)
        textWindow.selectAll()
        font = QFont("Consolas", 8)
        textWindow.setFont(font)
        tc = QTextCursor()
        tc.setPosition(textWindow.document().characterCount())
        textWindow.setTextCursor(tc)
        textWindow.setWindowTitle("Cropped Answers")
        self.textWindowList.append(textWindow)
        self.textWindowList[-1].show()
        self.textWindowList[-1].activateWindow()


    def save_answers(self):
        fn = self.generic_file_dialog(path=self.data["save_results"], type="save")
        if fn:
            f = open(fn, mode="w", encoding='utf-8')
            f.write(self.data["results_table_string"])
            f.close()

    def copy_answers(self):
        QApplication.clipboard().setText(self.data["results_table_string"])

    def pop_results(self):
        print(' pop_results')
        # results_window.setupUi()
        self.results_table.clearContents()
        # print("len(self.data[answers]) = ", len(self.data["answers"]))
        # print("len(self.data[answers][0]) = ", len(self.data["answers"][0]))
        # print("len(self.data[answers][0]) = ", len(self.data["answers"][0]))
        # EncryptionData = namedtuple('EncryptionData', 'method k_shift c_shift
        # ciphertext interrupter interrupter_pos_set')
        # AnswerData = namedtuple('AnswerData', 'decryption score decryption_string
        # encryptiondata')
        #a = self.data["answers"][0]
        # col_headers = ["score_per_ngram", "decryption_string", "method",
        #                "ciphertext", "key", "ct_start_index",
        #     "total_score", "min_score_count", "decryption", "k_shift", "c_shift", "interrupter",
        #     "interrupter_pos_set"]
        col_headers = ["score/4gram", "decryption", "method", "key",
                       "index", "score", "# min score", "decryption", "key shift",
                       "ct shift", "int", "int pos", "ciphertext"]
        # fa= [
        #     a.score.score_per_ngram,
        #     a.decryption_string,
        #     a.encryptiondata.method,
        #     ' '.join(a.encryptiondata.key),
        #     a.encryptiondata.ct_start_index,
        #     a.score.total_score,
        #     a.score.min_score_count,
        #     ','.join([str(x) for x in a.decryption]),
        #     a.encryptiondata.k_shift,
        #     a.encryptiondata.c_shift,
        #     '{}, {}, {}'.format( a.encryptiondata.interrupter, self.gem.pos_to_eng(
        #         a.encryptiondata.interrupter), self.gem.pos_to_rune(
        #         a.encryptiondata.interrupter)),
        #     ','.join([str(x) for x in a.encryptiondata.interrupter_pos_set]),
        #     #','.join(list(a.encryptiondata.interrupter_pos_set))
        #     ' '.join([''.join(x) for x in a.encryptiondata.ciphertext]),
        #
        # ]
        #
        # for head, item in zip(col_headers,fa):
        #     print(head,item)
        ''' when all the containers are rationalized this will be easier, for now, hardcode ans'''
        self.results_table.setColumnCount(len(col_headers))
        self.results_table.setRowCount(len(self.data["answers"]))
        #
        # results_window.tableView.setHorizontalHeaderLabels(headers)
        # header = self.results_table.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        #print(1)
        for i,header in enumerate(col_headers):
            item = QTableWidgetItem()
            item.setText(header)
            self.results_table.setHorizontalHeaderItem(i, item)
        #fileText = ""
        for i, item in enumerate(self.data["answers"]):

            a = item

            fa = [a.score.score_per_ngram,
                  a.decryption_string,
                  a.encryptiondata.method,
                  ' '.join(a.encryptiondata.key),
                  a.encryptiondata.ct_start_index,
                  a.score.total_score,
                  a.score.min_score_count,
                  ','.join([str(x) for x in a.decryption if x is not '_']),
                  "{}, {}".format(*a.encryptiondata.k_shift),
                  "{}, {}".format(*a.encryptiondata.c_shift),
                  '{}, {}'.format(a.encryptiondata.interrupter,
                                      self.gem.pos_to_eng(a.encryptiondata.interrupter)),
                  ','.join([str(x) for x in a.encryptiondata.interrupter_pos_set]),
                  ' '.join([''.join(x) for x in a.encryptiondata.ciphertext]),
                  # ','.join(list(a.encryptiondata.interrupter_pos_set))
            ]
            # for head, item in zip(col_headers, fa):
            #     print(head, item)
            self.addTableItem(self.results_table, i, 0, fa[0])
            self.addTableItem(self.results_table, i, 1, fa[1])
            self.addTableItem(self.results_table, i, 2, fa[2])
            self.addTableItem(self.results_table, i, 3, fa[3])
            self.addTableItem(self.results_table, i, 4, fa[4])
            self.addTableItem(self.results_table, i, 5, fa[5])
            self.addTableItem(self.results_table, i, 6, fa[6])
            self.addTableItem(self.results_table, i, 7, fa[7])
            self.addTableItem(self.results_table, i, 8, fa[8])
            self.addTableItem(self.results_table, i, 9, fa[9])
            self.addTableItem(self.results_table, i, 10,fa[10] )
            self.addTableItem(self.results_table, i, 11, fa[11] )
            self.addTableItem(self.results_table, i, 12, fa[12] )
            # # print("adding ",str(item[1][0]), str(item[-1]))
            # # self.addTableItem(self.results_table, i, 0, str(item[1][0]))
            # # self.addTableItem(self.results_table, i, 1, str(item[-1]))
            # self.addTableItem(self.results_table, i, 0, str(item.score.score_per_ngram))
            # self.addTableItem(self.results_table, i, 1, str(item.decryption_string))
            item = QTableWidgetItem()
            item.setText(str(i))
            self.results_table.setVerticalHeaderItem(i, item)
        self.results_table.resizeColumnsToContents()



        #print(col_headers)
        print_data = []
        for r in range(0,self.results_table.rowCount()):
            row_data = [str(r)]
            for c in range(0,self.results_table.columnCount()):
                row_data.append(self.results_table.item(r,c).text())
            print_data.append(row_data)
        # print(tabulate(print_data, headers=col_headers))


        # make a copy of the data as a text string, to copy to file or clpiboard
        self.data["results_table_string"] = tabulate(print_data, headers=col_headers,
                                                     tablefmt="presto", showindex=False,
                                                     colalign=("right", "left"))

        # header = self.results_table.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.results_table.setWindowTitle("Cropped Answers")
        self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, "results_tab"))

        self.pop_answers()

    def addTableItem(self, table, row, col, s):
        a = QtWidgets.QTableWidgetItem(str(s))
        a.setFlags(Qt.NoItemFlags | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        a.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        table.setItem(row, col, a)

    def handle_FourGramCountCut(self):
        self.data["4gram_count_cut"] = self.four_gram_count_cut.value()
        print("self.data[4gram_count_cut] = ", self.data["4gram_count_cut"])

    # def handle_testPlaintextEntry(self):
    #     '''
    #         convert text in test_plain_text to rune, display result in test_plain_text_runes
    #     '''
    #     self.test_decrypt.setEnabled(False)
    #     pt_runes = self.gem.translate_phrase_to_gematria(self.test_plain_text_runes.text().replace(",", " "))
    #     pt_to_print = ''
    #     for item in pt_runes:
    #         pt_to_print += ','.join(item) + ' '
    #     self.test_plain_text_runes.setText(pt_to_print)
    #     self.data["test_pt_runes"] = pt_runes
    #     self.set_testKeyStartIndexRange()

    def handle_testKeyEntry(self):
        print(
            "handle_testKeyEntry")  # self.test_decrypt.setEnabled(False)  # text = self.test_key.toPlainText().replace(" ", "")  # sep = ",
        # "  # key_is_numbers = False  # for char in sep:  #     if char in text:  #         key_is_numbers =  True  #         break  # if  #
        # key_is_numbers:  #     print("key_is_numbers!!")  #     key_runes = [elem for elem in text.split(",") if elem != '']  #     print(  #
        # key_runes)  # elif self.gem.areRunes(text):  #     print("key_is_runes")  #     key_runes = list(text)  # else:  #     print(  #
        # "key_is_english")  #     key_runes = self.gem.translate_to_gematria(text)  # self.test_key_out.setText(','.join(key_runes))  # self.data[
        # "test_key_runes"] = key_runes  # print(self.data["test_key_runes"] )  # print(key_runes)

    def handle_setDefault(self):
        # default words
        self.startWords.setChecked(True)
        self.endWords.setChecked(False)
        self.startAndEndWords.setChecked(False)
        self.allWords.setChecked(False)
        # default interrupters
        self.all_interrupters.setChecked(True)
        # default CT_rotations
        self.ct_forward_gematria.setChecked(True)
        self.ct_reverse_gematria.setChecked(True)
        self.ct_all_forward_gematria.setChecked(False)
        self.ct_all_reverse_gematria.setChecked(False)
        self.ct_all_gematria.setChecked(False)
        # self.key_all_gematria.setChecked(True)

        # default rotations
        self.key_forward_gematria.setChecked(True)
        self.key_reverse_gematria.setChecked(True)
        self.key_all_forward_gematria.setChecked(False)
        self.key_all_reverse_gematria.setChecked(False)
        self.key_all_gematria.setChecked(False)
        # default cipher text
        self.handle_lpSection()
        self.handle_processLPText()
        print("handle_setDefault")

    def handle_saveSetup(self):
        print('handle_saveSetup')

    def handle_loadSetup(self):
        print('handle_loadSetup')

    # |\    /|   |   |    |~\  |~~-__  |\  /   /|\   |  /~\    |
    # | \  / | \ |   |    |  \ |     | | \/   / | \  | /   \ \ |
    # |  \/  |  \|   |    |  / |_____| |     /  |  \ | \   /  \|
    # |      |   |\  |\   |_/  |  |  | |        |    |  \ /    |\
    # |      |   | \ | \  | \  |  |  | | /\     |    |  / \    | \
    # |      |   |   |  \ |  \ |  |  | |/  \    |    | /   \   |

    def getDecMapAndDisplay(self):
        print("\ngetDecMapAndDisplay")
        self.data["dec_map"] = self.encryptor.encryptionDataToDecryptionMap(self.data["enc_data"])
        # print("self.data[enc_map] = ", self.data["enc_map"])
        # print("self.data[dec_map] = ", self.data["dec_map"])
        self.setEncryptionTable()
        self.setDecryptionTable()
        self.enc_method_name.setText(self.data["enc_map_name"])
        self.test_enc_method.setText(self.data["enc_map_name"])
        self.test_enc_method_8.setText(self.data["enc_map_name"])

    def handle_encryptionMapTextEntry(self):
        print("handle_encryptionMapTextEntry")
        self.data["enc_map_text"] = self.enc_method_function_textbox.text()
        self.data["enc_map_name"] = self.enc_method_name_textbox.text()
        print("enc_map_name = ", self.data["enc_map_name"])
        print("enc_map_text = ", self.data["enc_map_text"])
        self.data["enc_data"] = self.encryptor.encryptionDatFromStringExpression(self.data["enc_map_text"], self.data["enc_map_name"])
        self.getDecMapAndDisplay()

    def setEncryptionTable(self):
        self.formatTable(self.encryption_table, ['Plain-Text Rune', 'Key Rune', 'Cipher Rune'])
        for row in range(0, 841):
            data = self.data["enc_data"][1][row]
            self.addTableItem(self.encryption_table, row, 0, str(data[0]))
            self.addTableItem(self.encryption_table, row, 1, str(data[1]))
            self.addTableItem(self.encryption_table, row, 2, str(data[2]))

        # todo set column widths to lok nice

    def setDecryptionTable(self):
        print("Format Table ")
        self.formatTable(self.decryption_table, ['Key\nRune', 'Cipher\nRune', 'Plain-Text\nRune(s)'])
        row = 0
        for key in range(0, 29):
            for ct in range(0, 29):
                data = self.data["dec_map"][tuple([key, ct])]
                # print("Dec tabel new (key,ct, data) = ", key, ct, str(data))
                self.addTableItem(self.decryption_table, row, 0, str(key))
                self.addTableItem(self.decryption_table, row, 1, str(ct))
                self.addTableItem(self.decryption_table, row, 2, str(data))
                row += 1

    def formatTable(self, table, headers):
        table.clear()
        table.setRowCount(841)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(headers)
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)  # | Qt.AlignLeft



    def flatten(self, li):
        return sum(([x] if not isinstance(x, list) else self.flatten(x) for x in li), [])

    #    / |\    /| |~~-__    /
    #   /  | \  / | |     |  /
    #  /   |  \/  | |_____| /____
    #  \   |      | |  |  |     /
    #   \  |      | |  |  |    /
    #    \ |      | |  |  |   /
    #
    # def handle_processKeys(self):
    #     print("handle_processKeys")
    #     text = self.keyTextPad.toPlainText()
    #
    #     self.data["keys"] = self.gem.process_string_to_latin_forward(self.keyTextPad.toPlainText())
    #
    #
    #
    #
    #
    #     # print(text)
    #     if self.data["key_type"] == "runes":
    #         print("key-type = runes")
    #         test = self.keyTextPad.toPlainText().replace("\n", "").split(",")
    #         #print(test)
    #         self.data["keys"] = []
    #         for key in test:
    #             # print(key)
    #             # print(list(key))
    #             self.data["keys"].append( [self.gem.r2e[x] for x in list(key)])
    #     elif self.data["key_type"] == "english":
    #         print("key-type = english")
    #         string = self.keyTextPad.toPlainText().replace("\n", "").split(",")
    #         # print(string)
    #         self.data["keys"] = [self.flatten(self.gem.translate_phrase_to_gematria(x)) for x in
    #                                  string]  # # print(self.data["keys"])  # TODO  have to make a version that
    #         # you can print to the output text pad
    #     elif self.data["key_type"] == "numbers":
    #         print("key-type = numbers")
    #         keylist = []
    #         for key in text.split("\n"):
    #             #print("next key = ",key)
    #             #keylist.append([int(e) if e else e for e in self.keyTextPad.toPlainText().split(',')])
    #             keylist.append([int(e) if e else e for e in key.split(',')])
    #             #print(keylist[-1])
    #         self.data["keys"] = [self.gem.positions_to_latin_forward(x) for x in keylist]
    #     # # this is broke needs checkignadn fixing
    #     # # also test for numbers, runes and chars so don;t need check boxes
    #     # a = "\n".join([",".join(x) for x in self.data["keys"]])
    #     # self.processed_key_display_textpad.setPlainText(a)
    #     # self.key_count_label.setText(str(len(self.data["keys"])) + " Keys")
    #     # self.number_of_keys.setText(str(len(self.data["keys"])) )

    # |   |     /|\   |\    /| |~\  |~\  |\    |\  /   /|\   |\    /| |~\    /
    # | \ |    / | \  | \  / | |  \ |  \ | \   | \/   / | \  | \  / | |  \  /
    # |  \|   /  |  \ |  \/  | |  / |  / |  \  |     /  |  \ |  \/  | |  / /____
    # |   |\     |    |      | |_/  |_/  |   | |        |    |      | |_/      /
    # |   | \    |    |      | | \  | \  |   | | /\     |    |      | | \     /
    # |   |      |    |      | |  \ |  \ |   | |/  \    |    |      | |  \   /
    def handle_interrupter(self):
        print("handle_interrupter")
        self.data["chosen_interrupters"] = []
        if self.all_interrupters.isChecked():
            for w in (self.interrupter.itemAt(i).widget() for i in range(self.interrupter.count())):
                #w.setChecked(True)
                #print(self.interrupter_map[w])
                self.data["chosen_interrupters"].append(self.interrupter_map[w])
        else:
            for w in (self.interrupter.itemAt(i).widget() for i in range(self.interrupter.count())):
                d = self.interrupter_map[w]
                if w.isChecked():
                    self.data["chosen_interrupters"].append(d)
                else:
                    if d in self.data["chosen_interrupters"]:
                        self.data["chosen_sections"].remove(d)
        if "all" in self.data["chosen_interrupters"]:
            self.data["chosen_interrupters"].remove("all")
        print("self.data[chosen_interrupters] = ", self.data["chosen_interrupters"])
        # update gui
        if len(self.data["chosen_interrupters"]) == 29:
            self.interrupters.setText("All")
            font = QtGui.QFont()
            font.setPointSize(12)
            self.interrupters.setFont(font)
            self.estimated_combinations_2.setFont(font)
        else:
            self.interrupters.setText(", ".join(self.data["chosen_interrupters"]))
        #


    # |~\   /~\    /|\   |\    /|\   |  /~\    |
    # |  \ /   \  / | \  | \  / | \  | /   \ \ |
    # |  / \   / /  |  \ |\  /  |  \ | \   /  \|
    # |_/   \ /     |    | \    |    |  \ /    |\
    # | \   / \     |    |      |    |  / \    | \
    def handle_key_order_shift(self):
        ''' TODO cancer logic for possible gematria rotation options '''
        if self.sender() == self.key_all_gematria:
            if self.key_all_gematria.isChecked():
                self.key_forward_gematria.setChecked(False)
                self.key_reverse_gematria.setChecked(False)
                self.key_all_forward_gematria.setChecked(False)
                self.key_all_reverse_gematria.setChecked(False)
        elif self.sender() == self.key_all_forward_gematria:
            if self.key_all_forward_gematria.isChecked():
                self.key_forward_gematria.setChecked(False)
                self.key_all_gematria.setChecked(False)
        elif self.sender() == self.key_all_reverse_gematria:
            if self.key_all_reverse_gematria.isChecked():
                self.key_reverse_gematria.setChecked(False)
                self.key_all_gematria.setChecked(False)

        elif self.sender() == self.key_forward_gematria:
            if self.key_forward_gematria.isChecked():
                self.key_all_forward_gematria.setChecked(False)
                self.key_all_gematria.setChecked(False)

        elif self.sender() == self.key_reverse_gematria:
            if self.key_reverse_gematria.isChecked():
                self.key_all_reverse_gematria.setChecked(False)
                self.key_all_gematria.setChecked(False)

        text_string = ""
        self.data["key_gematria_forward_shifts"] = []
        self.data["key_gematria_reverse_shifts"] = []

        if self.key_forward_gematria.isChecked() or self.key_all_forward_gematria.isChecked():
            self.data["key_use_gematria_forward"] = True
            if self.key_forward_gematria.isChecked():
                self.data["key_gematria_forward_shifts"] = [0]
                text_string += "forward "
            elif self.key_all_forward_gematria.isChecked():
                self.data["key_gematria_forward_shifts"] = list(range(0, 29))
                text_string += "all forward "
        else:
            self.data["key_use_gematria_forward"] = False

        if self.key_reverse_gematria.isChecked() or self.key_all_reverse_gematria.isChecked():
            self.data["key_use_gematria_reverse"] = True
            if self.key_reverse_gematria.isChecked():
                self.data["key_gematria_reverse_shifts"] = [0]
                text_string += "reverse"
            elif self.key_all_reverse_gematria.isChecked():
                self.data["key_gematria_reverse_shifts"] = list(range(0, 29))
                text_string += "all reverse"
        else:
            self.data["key_use_gematria_reverse"] = False

        if self.key_all_gematria.isChecked():
            self.data["key_use_gematria_forward"] = True
            self.data["key_use_gematria_reverse"] = True
            self.data["key_gematria_forward_shifts"] = list(range(0, 29))
            self.data["key_gematria_reverse_shifts"] = list(range(0, 29))
            text_string = "all"

        self.key_gematria_rotations.setText(text_string)

    def handle_ct_order_shift(self):
        ''' TODO cancer logic for possible gematria roation options '''
        if self.sender() == self.ct_all_gematria:
            if self.ct_all_gematria.isChecked():
                self.ct_forward_gematria.setChecked(False)
                self.ct_reverse_gematria.setChecked(False)
                self.ct_all_forward_gematria.setChecked(False)
                self.ct_all_reverse_gematria.setChecked(False)
        elif self.sender() == self.ct_all_forward_gematria:
            if self.ct_all_forward_gematria.isChecked():
                self.ct_forward_gematria.setChecked(False)
                self.ct_all_gematria.setChecked(False)
        elif self.sender() == self.ct_all_reverse_gematria:
            if self.ct_all_reverse_gematria.isChecked():
                self.ct_reverse_gematria.setChecked(False)
                self.ct_all_gematria.setChecked(False)

        elif self.sender() == self.ct_forward_gematria:
            if self.ct_forward_gematria.isChecked():
                self.ct_all_forward_gematria.setChecked(False)
                self.ct_all_gematria.setChecked(False)

        elif self.sender() == self.ct_reverse_gematria:
            if self.ct_reverse_gematria.isChecked():
                self.ct_all_reverse_gematria.setChecked(False)
                self.ct_all_gematria.setChecked(False)
        self.data["chosen_rotation"] = []
        text_string = ""

        self.data["ct_gematria_forward_shifts"] = []
        self.data["ct_gematria_reverse_shifts"] = []

        if self.ct_forward_gematria.isChecked() or self.ct_all_forward_gematria.isChecked():
            self.data["ct_use_gematria_forward"] = True
            if self.ct_forward_gematria.isChecked():
                self.data["ct_gematria_forward_shifts"] = [0]
                text_string += "forward "
            elif self.ct_all_forward_gematria.isChecked():
                self.data["ct_gematria_forward_shifts"] = list(range(0, 29))
                text_string += "all forward "
        else:
            self.data["ct_use_gematria_forward"] = False

        if self.ct_reverse_gematria.isChecked() or self.ct_all_reverse_gematria.isChecked():
            self.data["ct_use_gematria_reverse"] = True
            if self.ct_reverse_gematria.isChecked():
                self.data["ct_gematria_reverse_shifts"] = [0]
                text_string += "reverse"
            elif self.ct_all_reverse_gematria.isChecked():
                self.data["ct_gematria_reverse_shifts"] = list(range(0, 29))
                text_string += "all reverse"
        else:
            self.data["ct_use_gematria_reverse"] = True

        if self.ct_all_gematria.isChecked():
            self.data["ct_use_gematria_forward"] = True
            self.data["ct_use_gematria_reverse"] = True
            self.data["ct_gematria_forward_shifts"] = list(range(0, 29))
            self.data["ct_gematria_reverse_shifts"] = list(range(0, 29))
            text_string = "all"

        # if self.ct_forward_gematria.isChecked():
        #     #self.data["chosen_rotation"].append("f")
        #     self.data["chosen_rotation"].append(1)
        #     text_string += "forward"
        #     self.data["ct_use_gematria_forward"] = True
        #
        # if self.ct_reverse_gematria.isChecked():
        #     #self.data["chosen_rotation"].append("r")
        #     text_string += "reverse"
        #     self.data["chosen_rotation"].append(-1)
        #     self.data["ct_use_gematria_forward"] = True
        #
        # if self.all_forward_gematria.isChecked():
        #     #self.data["chosen_rotation"].append("a_f")
        #     #self.data["chosen_rotation"].append(range(1,30))
        #     [self.data["chosen_rotation"].append(i) for i in range(1,30)]
        #     text_string += " all forward"
        # if self.ct_all_reverse_gematria.isChecked():
        #     #self.data["chosen_rotation"].append("all_r")
        #     self.data["chosen_rotation"].append(list(range(-29,0)))
        #     text_string += " all reverse"
        #
        # if self.ct_all_gematria.isChecked():
        #     #self.data["chosen_rotation"].append("all")
        #     self.data["chosen_rotation"].append(list(range(-29,0)))
        #     self.data["chosen_rotation"].append(list(range(1,30)))
        #     text_string = "all"

        # the above old method need stidying up and teh etxt boxes to the test page etc ...
        # how we enable that buttun will be itneresting
        # neeed to create a seperate fucnitgon that looks at all teh criteria and enabels / disbales everytime
        # something changes!!

        self.gematria_rotations.setText(
            text_string)  # self.data["chosen_rotation"] = self.flatten(self.data["chosen_rotation"])  # print(self.data["chosen_rotation"])  #  #
        # #self.data["chosen_rotation"] = " ".join(self.data["chosen_rotation"])  # if len(self.data["chosen_rotation"]) == 0:  #  #
        # self.run_decryption_button.setEnabled(False)  # else:  #     self.run_decryption_button.setEnabled(True)

    # |\   |\  /        /   |\    /| |      /|\   |  /~\    |
    # | \  | \/        /    | \  / | |     / | \  | /   \ \ |
    # |  \ |       _  /____ |  \/  | |    /  |  \ | \   /  \|
    # |    |      |_|     / |      | |\      |    |  \ /    |\
    # |    | /\          /  |      | | \     |    |  / \    | \
    # |    |/  \        /   |      | |  \    |    | /   \   |
    def handle_lpSection(self):
        '''
            sets which LP sections are checked in lpSectionBox in Cipher-Text Tab
        '''
        #print("\nHANDLE_LPSECTION")
        for count, w in enumerate((self.lpSection.itemAt(i).widget()) for i in range(
                self.lpSection.count())):
            #print("c = ", count)
            #print("c = ", count, w.isChecked())
            if w.isChecked():
                self.data["chosen_sections"].append(count)
            else:
                if count in self.data["chosen_sections"]:
                    self.data["chosen_sections"].remove(count)
        if len(self.data["chosen_sections"]) > 0:
            self.data["chosen_sections"] = list(set(self.data["chosen_sections"]))
        #print("self.data[chosen_sections] = ", self.data["chosen_sections"])
        self.handle_processLPText()

    # |~\  |\    /| |\    /|      |~\  |\      |   |\    /|   /
    # |  \ | \  / | | \  / |      |  \ | \   \ |   | \  / |  /
    # |  / |  \/  | |  \/  |   _  |  / |  \   \|   |  \/  | /____
    # |_/  |      | |  /\  |  |_| |_/  |   |   |\  |      |     /
    # | \  |      | | /  \ |      | \  |   |   | \ |      |    /
    # |  \ |      | |/    \|      |  \ |   |   |   |      |   /
    def handle_redrunes(self):
        print("\nhandle_redrunes")
        num = int(''.join(c for c in self.sender().objectName() if c.isdigit()))
        if self.sender().isChecked():
            self.data["chosen_redrunes"].append(num)
        else:
            self.data["chosen_redrunes"].remove(num)

        if len(self.data["chosen_redrunes"]) > 0:
            self.data["chosen_redrunes"].sort()
        self.handle_processLPText()

    def handle_processLPText(self):  # TODO better name
        print("\nhandle_processLPText")
        section_choices = redrune_choices = []
        print("self.data[chosen_sections] = ", self.data["chosen_sections"])
        print("self.data[chosen_words] = ", self.data["chosen_words"])
        print("self.data[chosen_redrunes] = ", self.data["chosen_redrunes"])
        if len(self.data["chosen_sections"]) != 0:
            section_choices = self.LP.getStartOrEndWords(self.data["chosen_sections"], self.data["chosen_words"])
        if len(self.data["chosen_redrunes"]) != 0:
            redrune_choices = self.LP.getRedRunes(self.data["chosen_redrunes"])
        # gymnastics to display to screen
        print("section_choices = ",section_choices)
        print("redrune_choices = ",redrune_choices)
        print("self.data[cipher_text]  = ", self.data["cipher_text"] )
        self.data["cipher_text"] = section_choices + redrune_choices
        # format for display TODO make into generic function, similar work is done in multiple functions (?)
        ct_rune_eng = []
        for ct in self.data["cipher_text"]:
            words = []
            for item in ct:
                # l = list(item)
                words.append(self.gem.rune_to_eng(list(item)))
            ct_rune_eng.append(words)
        display_ct_list = []
        for item in ct_rune_eng:
            phrase = []
            if self.ct_runes_radio.isChecked():
                phrase = [self.gem.eng_to_rune(x) for x in item]
            elif self.ct_runes_eng_radio.isChecked():
                phrase = item
            elif self.ct_prime_radio.isChecked():
                for key in [self.gem.eng_to_prime_value(x) for x in item]:
                    phrase.append([str(x) for x in key])
            elif self.ct_forward_position_radio.isChecked():
                for key in [self.gem.encode_as_forward_position(x) for x in item]:
                    phrase.append([str(x) for x in key])
            elif self.ct_reverse_position_radio.isChecked():
                for key in [self.gem.encode_as_reverse_position(x) for x in item]:
                    phrase.append([str(x) for x in key])
            else:
                phrase = [self.gem.eng_to_rune(x) for x in item]
            display_ct_list.append(phrase)  # display to gui, adn count keys
        ct_to_print = ""
        for ct in display_ct_list:
            words = []
            for item in ct:
                words.append(','.join(item))
            ct_to_print += '  '.join([''.join(word) for word in words]) + '\n'
        self.cipherTextPad.setPlainText(ct_to_print)
        # get order lists
        # TODO not yet implemented during decryption
        self.handle_ct_order()
        self.handle_custum_ct_order()

        # TODO work with single format for cipher_text all the way through
        # now set up cipher_text suitable for decrypting
        self.data["num_cipher_text"] = len(self.data["cipher_text"])
        # get ct word lengths
        print(1)
        self.data["cipher_text_lengths"] = []

        ct_in_decryptign_fromat = []
        for ct in self.data["cipher_text"]:
            ct_in_decryptign_fromat.append([list(x) for x in ct])
        self.data["cipher_text"] = ct_in_decryptign_fromat
        for ct in self.data["cipher_text"]:
            self.data["cipher_text_lengths"].append([len(list(x)) for x in ct])
        print("self.data[cipher_text] = ", self.data["cipher_text"])
        print("self.data[cipher_text_lengths] = ", self.data["cipher_text_lengths"])

    def handle_manual_ct_entry(self):
        print("handle_manual_ct_entry - coming soon")

    def handle_ct_order(self):
        print("\nHANDLE_CT_ORDER")
        if len(self.data["cipher_text"]) > 0:
            ct_order_list_str = ""

            if self.tb_lr_ciphertext_order.isChecked() or self.bt_rl_ciphertext_order.isChecked():
                #print("tb_lr_ciphertext_order or bt_rl_ciphertext_order")
                #print("data[cipher_text]", self.data["cipher_text"])
                self.data["ct_order_list"] = []
                for item in self.data["cipher_text"]:
                    #print(item)
                    if self.tb_lr_ciphertext_order.isChecked():
                        #print("tb_lr_ciphertext_order, item = ", ''.join(item))
                        self.data["ct_order_list"].append(list(range(0, len(list(''.join(item))))))
                    elif self.bt_rl_ciphertext_order.isChecked():
                        #print("bt_rl_ciphertext_order, item = ", ''.join(item))
                        self.data["ct_order_list"].append(list(reversed(list(range(0, len(list(''.join(item))))))))
                    ct_order_list_str += ' '.join([str(x) for x in self.data["ct_order_list"][-1]])
                    ct_order_list_str += '\n'
                self.cipherTextOrderTextPad.setPlainText(ct_order_list_str)
                order_check = self.cipherTextOrderTextPad.toPlainText()
                #print("order_check  = ", order_check)
                return
            #print("custom_ciphertext_order")

    def handle_custum_ct_order(self):
        """
            bit too complex atm, but working (?)
            on return or lostfocus of cipherTextOrderTextPad,  reads cipherTextOrderTextPad contents as custom orders
            parsing invovles checking the custom orders contain exactly the same numbers as in the left-right top-bottom order
            on parsing success,
                sets the data["ct_order_list"]  = to the passed values (as lists of integers),
            on fail,
                attempts sone error messages
                sets data["ct_order_list"] = None
        """
        print("\nHANDLE_CUSTUM_CT_ORDER")
        # go through each entry in the text pad and compare the numbers entered to what we expect
        if self.custom_ciphertext_order.isChecked():
            passed_custom_order = self.cipherTextOrderTextPad.toPlainText()
            print("passed_custom_order = ", passed_custom_order)

            # get expectations
            ct_order_list = []
            ct_order_list_str = []
            # thing scan have gone wrong last tite thsi fucntion was claaed, if so reset the main data. dict ct_order_list
            reset_ct_order_list = False
            if self.data["ct_order_list"] is None:
                reset_ct_order_list = True
                print("reset_ct_order_list = True, resetting ct_order_list to default")
                self.data["ct_order_list"] = []

            # get the definitive number of runes in each cipher text element, for cross-checking against passed order
            for item in self.data["cipher_text"]:
                print(item)
                order = list(range(0, len(list(''.join(item)))))
                ct_order_list.append(order)
                ct_order_list_str.append(' '.join([str(x) for x in ct_order_list[-1]]))
                # if updating main list, do that
                if reset_ct_order_list:
                    self.data["ct_order_list"].append(order)
            print("START data[ct_order_list]", self.data["ct_order_list"])
            print("ct_order_list = ", ct_order_list)
            print("ct_order_list_str = ", ct_order_list_str)
            custom_order_str = list(filter(None, passed_custom_order.split("\n")))
            print("custom_order_str = ", custom_order_str)
            custom_order_str = [x for x in custom_order_str if x[0] != "#"]
            print("custom_order_str = ", custom_order_str)
            ct_len = len(self.data["cipher_text"])
            co_len = len(custom_order_str)
            print("ct_len, co_len ", ct_len, co_len)
            custum_ord_str_to_display = ""
            custum_order_passed = True
            if ct_len != co_len:
                custum_ord_str_to_display = "#Custom Order is Incorrect number of orders should be {} instead of {}\n".format(ct_len, co_len)
                custum_order_passed = False
            else:
                for i, (co_line, ct) in enumerate(zip(custom_order_str, self.data["ct_order_list"])):
                    a = set([int(x) for x in co_line.split()])
                    b = set(ct)
                    print("a = ", a)
                    print("b = ", b)
                    if a != b:
                        print("Custom Order entry {} is incorrect ".format(i))
                        custum_ord_str_to_display = "#Custom Order entry {} is incorrect\n".format(i) + custum_ord_str_to_display
                        custum_order_passed = False
                    else:
                        print("Custom Order entry {} is correct".format(i))

            # if passed order was good, update main data order for using in decrytping
            if custum_order_passed:
                custum_ord_str_to_display = "#Custom order passed parsing test\n" + custum_ord_str_to_display
                # if the custon order passed, set the data dict ct_order_list
                self.data["ct_order_list"] = []
                for item in custom_order_str:
                    self.data["ct_order_list"].append([int(x) for x in item.split()])
            else:
                # the custom order failed, so set the data dict ct_order_list to None
                self.data["ct_order_list"] = None

            print("NEW data[ct_order_list]", self.data["ct_order_list"])
            # Finally update gui
            custum_ord_str_to_display += "\n".join(custom_order_str)
            print("custum_ord_str_to_display = ", custum_ord_str_to_display)
            self.cipherTextOrderTextPad.setPlainText(custum_ord_str_to_display)

            print("HANDLE_CUSTUM_CT_ORDER FIN")

    # |\   /~\  |~\  |\    /|   /
    # | > /   \ |  \ | \  / |  /
    # |/  \   / |  / |  \/  | /____
    # |    \ /  |_/  |  /\  |     /
    # |    / \  | \  | /  \ |    /
    # |   /   \ |  \ |/    \|   /
    def handle_wordSelection(self):
        # TODO cancer but works, tidy up later
        if self.startAndEndWords.isChecked():
            self.data["chosen_words"] = "startAndEndWords"
        elif self.endWords.isChecked():
            self.data["chosen_words"] = "endWords"
        elif self.startWords.isChecked():
            self.data["chosen_words"] = "startWords"
        elif self.allWords.isChecked():
            self.data["chosen_words"] = "allWords"
        self.handle_processLPText()

    def setDefaultGuiSate(self):
        self.update_pre_computed_enc_map_combobox()

        # ct choice radio buttos
        self.startWords.setChecked(True)
        self.endWords.setChecked(False)
        self.startAndEndWords.setChecked(False)
        self.allWords.setChecked(False)
        self.lp_section1.setChecked(False)
        self.lp_section2.setChecked(False)
        self.lp_section3.setChecked(False)
        self.lp_section4.setChecked(False)
        self.lp_section5.setChecked(False)
        self.lp_section6.setChecked(False)
        self.lp_section7.setChecked(False)
        self.lp_section8.setChecked(False)
        self.lp_section9.setChecked(False)
        self.lp_section10.setChecked(False)
        self.lp_section11.setChecked(False)
        self.lp_section12.setChecked(False)
        self.lp_section13.setChecked(True)
        self.all_interrupters.setChecked(True)

    def update_no_iterations(self):
        count = 0
        for ct in self.ct_rune_chars:
            for key in self.crypt_model.all_keys:
                # print(ct, key)
                c_len = len(ct)
                k_len = len(key)
                if k_len >= c_len:
                    count += 0
                else:
                    count += c_len  # print("shifts key","shifts key", "int", "num ct", "num_key" )

    def setRunesOrEnglish(self):
        ''' TODO set up switch between different encodings in gui text ???'''
        self.y_interrupter.setText("y")
        self.j_interrupter.setText("j")
        self.t_interrupter.setText("t")
        self.i_interrupter.setText("i")
        self.x_interrupter.setText("x")
        self.o_interrupter.setText("o")
        self.ing_interrupter.setText("ing")
        self.s_interrupter.setText("s")
        self.w_interrupter.setText("w")
        self.g_interrupter.setText("g")
        self.oe_interrupter.setText("oe")
        self.eo_interrupter.setText("eo")
        self.r_interrupter.setText("r")
        self.th_interrupter.setText("th")
        self.l_interrupter.setText("l")
        self.h_interrupter.setText("h")
        self.p_interrupter.setText("p")
        self.u_interrupter.setText("u")
        self.m_interrupter.setText("m")
        self.f_interrupter.setText("f")
        self.io_interrupter.setText("io")
        self.n_interrupter.setText("n")
        self.c_interrupter.setText("c")
        self.b_interrupter.setText("b")
        self.e_interrupter.setText("e")
        self.d_interrupter.setText("d")
        self.a_interrupter.setText("a")
        self.ae_interrupter.setText("ae")
        self.ea_interrupter.setText("ea")

    def generic_file_dialog(self, path, type="open"):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if type == 'open':
            t = "QFileDialog.getOpenFileName()"
            fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", path, "All Files (*)", options=options)
        elif type == 'save':
            print("SAVE")
            fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", path, "All Files (*)", options=options)
        elif type == 'dir':
            print("dir")
            fileName = QFileDialog.getExistingDirectory(parent=self, caption="Open Direct",
                                                           options=QFileDialog.ShowDirsOnly)
        else:
            fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", path, "All Files (*)", options=options)

        if fileName:
            return fileName
        return None


    def handle_loadKeyFile(self):
        fn = self.generic_file_dialog(path=self.data["key_folder"], type="open")
        if fn:
            f = open(fn, mode="r", encoding='utf-8')
            text = f.read()
            f.close()
            self.key_entry_textedit.clear()
            self.key_entry_textedit.insertPlainText(text)
            self.handle_key_entry()
            self.handle_key_display_format()

    def handle_saveKeyFile(self):
        fn = self.generic_file_dialog(path=self.data["key_folder"], type="save")
        if fn:
            f = open(fn, mode="w", encoding='utf-8')
            f.write(self.key_entry_textedit.toPlainText())
            f.close()
