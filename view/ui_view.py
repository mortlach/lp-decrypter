# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainView(object):
    def setupUi(self, mainView):
        mainView.setObjectName("mainView")
        mainView.resize(537, 917)
        mainView.setMinimumSize(QtCore.QSize(0, 0))
        mainView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        mainView.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainView)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.Ciphertext_2 = QtWidgets.QWidget()
        self.Ciphertext_2.setObjectName("Ciphertext_2")
        self.run_decryption_button = QtWidgets.QPushButton(self.Ciphertext_2)
        self.run_decryption_button.setGeometry(QtCore.QRect(0, 370, 261, 23))
        self.run_decryption_button.setObjectName("run_decryption_button")
        self.layoutWidget = QtWidgets.QWidget(self.Ciphertext_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 374, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.enc_method_name_2 = QtWidgets.QLabel(self.layoutWidget)
        self.enc_method_name_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enc_method_name_2.setFont(font)
        self.enc_method_name_2.setObjectName("enc_method_name_2")
        self.gridLayout_4.addWidget(self.enc_method_name_2, 0, 0, 1, 1)
        self.number_of_keys = QtWidgets.QLabel(self.layoutWidget)
        self.number_of_keys.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_of_keys.setFont(font)
        self.number_of_keys.setObjectName("number_of_keys")
        self.gridLayout_4.addWidget(self.number_of_keys, 1, 1, 1, 1)
        self.interrupters_2 = QtWidgets.QLabel(self.layoutWidget)
        self.interrupters_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.interrupters_2.setFont(font)
        self.interrupters_2.setObjectName("interrupters_2")
        self.gridLayout_4.addWidget(self.interrupters_2, 6, 0, 2, 1)
        self.interrupters = QtWidgets.QLabel(self.layoutWidget)
        self.interrupters.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.interrupters.setFont(font)
        self.interrupters.setWordWrap(True)
        self.interrupters.setObjectName("interrupters")
        self.gridLayout_4.addWidget(self.interrupters, 6, 1, 2, 1)
        self.cipherTextPad_2 = QtWidgets.QLabel(self.layoutWidget)
        self.cipherTextPad_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cipherTextPad_2.setFont(font)
        self.cipherTextPad_2.setObjectName("cipherTextPad_2")
        self.gridLayout_4.addWidget(self.cipherTextPad_2, 9, 1, 1, 1)
        self.cipher_text_set = QtWidgets.QLabel(self.layoutWidget)
        self.cipher_text_set.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cipher_text_set.setFont(font)
        self.cipher_text_set.setObjectName("cipher_text_set")
        self.gridLayout_4.addWidget(self.cipher_text_set, 2, 1, 1, 1)
        self.cipher_text_set_2 = QtWidgets.QLabel(self.layoutWidget)
        self.cipher_text_set_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cipher_text_set_2.setFont(font)
        self.cipher_text_set_2.setObjectName("cipher_text_set_2")
        self.gridLayout_4.addWidget(self.cipher_text_set_2, 2, 0, 1, 1)
        self.estimated_time_2 = QtWidgets.QLabel(self.layoutWidget)
        self.estimated_time_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.estimated_time_2.setFont(font)
        self.estimated_time_2.setObjectName("estimated_time_2")
        self.gridLayout_4.addWidget(self.estimated_time_2, 9, 0, 1, 1)
        self.enc_method_name = QtWidgets.QLabel(self.layoutWidget)
        self.enc_method_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enc_method_name.setFont(font)
        self.enc_method_name.setObjectName("enc_method_name")
        self.gridLayout_4.addWidget(self.enc_method_name, 0, 1, 1, 1)
        self.estimated_combinations = QtWidgets.QLabel(self.layoutWidget)
        self.estimated_combinations.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.estimated_combinations.setFont(font)
        self.estimated_combinations.setObjectName("estimated_combinations")
        self.gridLayout_4.addWidget(self.estimated_combinations, 8, 1, 1, 1)
        self.gematria_rotations = QtWidgets.QLabel(self.layoutWidget)
        self.gematria_rotations.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gematria_rotations.setFont(font)
        self.gematria_rotations.setObjectName("gematria_rotations")
        self.gridLayout_4.addWidget(self.gematria_rotations, 3, 1, 1, 1)
        self.estimated_combinations_2 = QtWidgets.QLabel(self.layoutWidget)
        self.estimated_combinations_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.estimated_combinations_2.setFont(font)
        self.estimated_combinations_2.setObjectName("estimated_combinations_2")
        self.gridLayout_4.addWidget(self.estimated_combinations_2, 8, 0, 1, 1)
        self.number_of_keys_2 = QtWidgets.QLabel(self.layoutWidget)
        self.number_of_keys_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_of_keys_2.setFont(font)
        self.number_of_keys_2.setObjectName("number_of_keys_2")
        self.gridLayout_4.addWidget(self.number_of_keys_2, 1, 0, 1, 1)
        self.gematria_rotations_2 = QtWidgets.QLabel(self.layoutWidget)
        self.gematria_rotations_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gematria_rotations_2.setFont(font)
        self.gematria_rotations_2.setObjectName("gematria_rotations_2")
        self.gridLayout_4.addWidget(self.gematria_rotations_2, 3, 0, 1, 1)
        self.gematria_rotations_3 = QtWidgets.QLabel(self.layoutWidget)
        self.gematria_rotations_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gematria_rotations_3.setFont(font)
        self.gematria_rotations_3.setObjectName("gematria_rotations_3")
        self.gridLayout_4.addWidget(self.gematria_rotations_3, 4, 0, 1, 1)
        self.key_gematria_rotations = QtWidgets.QLabel(self.layoutWidget)
        self.key_gematria_rotations.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.key_gematria_rotations.setFont(font)
        self.key_gematria_rotations.setObjectName("key_gematria_rotations")
        self.gridLayout_4.addWidget(self.key_gematria_rotations, 4, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.Ciphertext_2)
        self.widget.setGeometry(QtCore.QRect(10, 250, 111, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.set_default_button = QtWidgets.QPushButton(self.widget)
        self.set_default_button.setObjectName("set_default_button")
        self.verticalLayout_5.addWidget(self.set_default_button)
        self.save_setup_button = QtWidgets.QPushButton(self.widget)
        self.save_setup_button.setObjectName("save_setup_button")
        self.verticalLayout_5.addWidget(self.save_setup_button)
        self.load_setup_button = QtWidgets.QPushButton(self.widget)
        self.load_setup_button.setObjectName("load_setup_button")
        self.verticalLayout_5.addWidget(self.load_setup_button)
        self.tabWidget.addTab(self.Ciphertext_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.test_key_entry = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_key_entry.setFont(font)
        self.test_key_entry.setObjectName("test_key_entry")
        self.verticalLayout_10.addWidget(self.test_key_entry)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_7.addWidget(self.label_31)
        self.test_key_gem_order = QtWidgets.QComboBox(self.groupBox_2)
        self.test_key_gem_order.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_key_gem_order.setFont(font)
        self.test_key_gem_order.setObjectName("test_key_gem_order")
        self.test_key_gem_order.addItem("")
        self.test_key_gem_order.addItem("")
        self.horizontalLayout_7.addWidget(self.test_key_gem_order)
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_7.addWidget(self.label_30)
        self.test_key_gem_shift = QtWidgets.QComboBox(self.groupBox_2)
        self.test_key_gem_shift.setMinimumSize(QtCore.QSize(50, 0))
        self.test_key_gem_shift.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_key_gem_shift.setFont(font)
        self.test_key_gem_shift.setObjectName("test_key_gem_shift")
        self.horizontalLayout_7.addWidget(self.test_key_gem_shift)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.key_display_format_box_2 = QtWidgets.QGroupBox(self.groupBox_2)
        self.key_display_format_box_2.setObjectName("key_display_format_box_2")
        self.test_key_display_format_layout = QtWidgets.QHBoxLayout(self.key_display_format_box_2)
        self.test_key_display_format_layout.setContentsMargins(0, 4, 0, 4)
        self.test_key_display_format_layout.setSpacing(0)
        self.test_key_display_format_layout.setObjectName("test_key_display_format_layout")
        self.test_key_runes_radio = QtWidgets.QRadioButton(self.key_display_format_box_2)
        self.test_key_runes_radio.setObjectName("test_key_runes_radio")
        self.test_key_display_format_layout.addWidget(self.test_key_runes_radio)
        self.test_key_runes_eng_radio = QtWidgets.QRadioButton(self.key_display_format_box_2)
        self.test_key_runes_eng_radio.setChecked(True)
        self.test_key_runes_eng_radio.setObjectName("test_key_runes_eng_radio")
        self.test_key_display_format_layout.addWidget(self.test_key_runes_eng_radio)
        self.test_key_prime_radio = QtWidgets.QRadioButton(self.key_display_format_box_2)
        self.test_key_prime_radio.setObjectName("test_key_prime_radio")
        self.test_key_display_format_layout.addWidget(self.test_key_prime_radio)
        self.test_key_forward_position_radio = QtWidgets.QRadioButton(self.key_display_format_box_2)
        self.test_key_forward_position_radio.setObjectName("test_key_forward_position_radio")
        self.test_key_display_format_layout.addWidget(self.test_key_forward_position_radio)
        self.test_key_reverse_position_radio = QtWidgets.QRadioButton(self.key_display_format_box_2)
        self.test_key_reverse_position_radio.setObjectName("test_key_reverse_position_radio")
        self.test_key_display_format_layout.addWidget(self.test_key_reverse_position_radio)
        self.verticalLayout_10.addWidget(self.key_display_format_box_2)
        self.test_key_out = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_key_out.setFont(font)
        self.test_key_out.setToolTip("")
        self.test_key_out.setObjectName("test_key_out")
        self.verticalLayout_10.addWidget(self.test_key_out)
        self.verticalLayout_13.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.test_plaintext_entry = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_plaintext_entry.setFont(font)
        self.test_plaintext_entry.setObjectName("test_plaintext_entry")
        self.verticalLayout_11.addWidget(self.test_plaintext_entry)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_14.addWidget(self.label_32)
        self.test_plaintext_gem_order = QtWidgets.QComboBox(self.groupBox_3)
        self.test_plaintext_gem_order.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_plaintext_gem_order.setFont(font)
        self.test_plaintext_gem_order.setObjectName("test_plaintext_gem_order")
        self.test_plaintext_gem_order.addItem("")
        self.test_plaintext_gem_order.addItem("")
        self.horizontalLayout_14.addWidget(self.test_plaintext_gem_order)
        self.label_33 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_14.addWidget(self.label_33)
        self.test_plaintext_gem_shift = QtWidgets.QComboBox(self.groupBox_3)
        self.test_plaintext_gem_shift.setMinimumSize(QtCore.QSize(50, 0))
        self.test_plaintext_gem_shift.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_plaintext_gem_shift.setFont(font)
        self.test_plaintext_gem_shift.setObjectName("test_plaintext_gem_shift")
        self.horizontalLayout_14.addWidget(self.test_plaintext_gem_shift)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.test_pt_display_format_box = QtWidgets.QGroupBox(self.groupBox_3)
        self.test_pt_display_format_box.setObjectName("test_pt_display_format_box")
        self.test_pt_display_format_layout = QtWidgets.QHBoxLayout(self.test_pt_display_format_box)
        self.test_pt_display_format_layout.setContentsMargins(0, 4, 0, 4)
        self.test_pt_display_format_layout.setSpacing(0)
        self.test_pt_display_format_layout.setObjectName("test_pt_display_format_layout")
        self.test_pt_runes_radio = QtWidgets.QRadioButton(self.test_pt_display_format_box)
        self.test_pt_runes_radio.setChecked(False)
        self.test_pt_runes_radio.setObjectName("test_pt_runes_radio")
        self.test_pt_display_format_layout.addWidget(self.test_pt_runes_radio)
        self.test_pt_runes_eng_radio = QtWidgets.QRadioButton(self.test_pt_display_format_box)
        self.test_pt_runes_eng_radio.setChecked(True)
        self.test_pt_runes_eng_radio.setObjectName("test_pt_runes_eng_radio")
        self.test_pt_display_format_layout.addWidget(self.test_pt_runes_eng_radio)
        self.test_pt_prime_radio = QtWidgets.QRadioButton(self.test_pt_display_format_box)
        self.test_pt_prime_radio.setObjectName("test_pt_prime_radio")
        self.test_pt_display_format_layout.addWidget(self.test_pt_prime_radio)
        self.test_pt_forward_position_radio = QtWidgets.QRadioButton(self.test_pt_display_format_box)
        self.test_pt_forward_position_radio.setObjectName("test_pt_forward_position_radio")
        self.test_pt_display_format_layout.addWidget(self.test_pt_forward_position_radio)
        self.test_pt_reverse_position_radio = QtWidgets.QRadioButton(self.test_pt_display_format_box)
        self.test_pt_reverse_position_radio.setObjectName("test_pt_reverse_position_radio")
        self.test_pt_display_format_layout.addWidget(self.test_pt_reverse_position_radio)
        self.verticalLayout_11.addWidget(self.test_pt_display_format_box)
        self.test_plain_text_runes = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_plain_text_runes.setFont(font)
        self.test_plain_text_runes.setObjectName("test_plain_text_runes")
        self.verticalLayout_11.addWidget(self.test_plain_text_runes)
        self.verticalLayout_13.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.test_enc_method_2 = QtWidgets.QLabel(self.groupBox_4)
        self.test_enc_method_2.setMinimumSize(QtCore.QSize(0, 25))
        self.test_enc_method_2.setMaximumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_enc_method_2.setFont(font)
        self.test_enc_method_2.setObjectName("test_enc_method_2")
        self.horizontalLayout_16.addWidget(self.test_enc_method_2)
        self.test_enc_method = QtWidgets.QLabel(self.groupBox_4)
        self.test_enc_method.setMinimumSize(QtCore.QSize(0, 25))
        self.test_enc_method.setMaximumSize(QtCore.QSize(999999, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_enc_method.setFont(font)
        self.test_enc_method.setObjectName("test_enc_method")
        self.horizontalLayout_16.addWidget(self.test_enc_method)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_6.addWidget(self.label_28)
        self.test_key_start_index = QtWidgets.QSpinBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_key_start_index.setFont(font)
        self.test_key_start_index.setMaximum(500)
        self.test_key_start_index.setObjectName("test_key_start_index")
        self.horizontalLayout_6.addWidget(self.test_key_start_index)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_15.addWidget(self.label_27)
        self.test_interrupter = QtWidgets.QComboBox(self.groupBox_4)
        self.test_interrupter.setMinimumSize(QtCore.QSize(60, 0))
        self.test_interrupter.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_interrupter.setFont(font)
        self.test_interrupter.setObjectName("test_interrupter")
        self.horizontalLayout_15.addWidget(self.test_interrupter)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_15)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_12.addWidget(self.label_23)
        self.test_ct_out_eng = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_ct_out_eng.setFont(font)
        self.test_ct_out_eng.setObjectName("test_ct_out_eng")
        self.verticalLayout_12.addWidget(self.test_ct_out_eng)
        self.test_ct_out_rune = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_ct_out_rune.setFont(font)
        self.test_ct_out_rune.setObjectName("test_ct_out_rune")
        self.verticalLayout_12.addWidget(self.test_ct_out_rune)
        self.test_ct_out_prime = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_ct_out_prime.setFont(font)
        self.test_ct_out_prime.setObjectName("test_ct_out_prime")
        self.verticalLayout_12.addWidget(self.test_ct_out_prime)
        self.test_ct_out_fpos = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_ct_out_fpos.setFont(font)
        self.test_ct_out_fpos.setObjectName("test_ct_out_fpos")
        self.verticalLayout_12.addWidget(self.test_ct_out_fpos)
        self.test_ct_out_rpos = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_ct_out_rpos.setFont(font)
        self.test_ct_out_rpos.setObjectName("test_ct_out_rpos")
        self.verticalLayout_12.addWidget(self.test_ct_out_rpos)
        self.verticalLayout_13.addWidget(self.groupBox_4)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.test_decrypt = QtWidgets.QPushButton(self.tab)
        self.test_decrypt.setObjectName("test_decrypt")
        self.horizontalLayout_18.addWidget(self.test_decrypt)
        self.cancel_test_decrypt = QtWidgets.QPushButton(self.tab)
        self.cancel_test_decrypt.setObjectName("cancel_test_decrypt")
        self.horizontalLayout_18.addWidget(self.cancel_test_decrypt)
        self.verticalLayout_13.addLayout(self.horizontalLayout_18)
        self.tabWidget.addTab(self.tab, "")
        self.results_tab = QtWidgets.QWidget()
        self.results_tab.setObjectName("results_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.results_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.test_enc_method_7 = QtWidgets.QLabel(self.results_tab)
        self.test_enc_method_7.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_enc_method_7.setFont(font)
        self.test_enc_method_7.setObjectName("test_enc_method_7")
        self.horizontalLayout_10.addWidget(self.test_enc_method_7)
        self.test_enc_method_8 = QtWidgets.QLabel(self.results_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_enc_method_8.setFont(font)
        self.test_enc_method_8.setObjectName("test_enc_method_8")
        self.horizontalLayout_10.addWidget(self.test_enc_method_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.copy_results_to_file = QtWidgets.QPushButton(self.results_tab)
        self.copy_results_to_file.setObjectName("copy_results_to_file")
        self.horizontalLayout.addWidget(self.copy_results_to_file)
        self.save_results_to_file = QtWidgets.QPushButton(self.results_tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_results_to_file.setFont(font)
        self.save_results_to_file.setObjectName("save_results_to_file")
        self.horizontalLayout.addWidget(self.save_results_to_file)
        self.pop_results_to_windows = QtWidgets.QPushButton(self.results_tab)
        self.pop_results_to_windows.setObjectName("pop_results_to_windows")
        self.horizontalLayout.addWidget(self.pop_results_to_windows)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.results_table = QTableWidgetOverload(self.results_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_table.sizePolicy().hasHeightForWidth())
        self.results_table.setSizePolicy(sizePolicy)
        self.results_table.setMinimumSize(QtCore.QSize(20, 195))
        self.results_table.setMaximumSize(QtCore.QSize(600, 3000))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.results_table.setFont(font)
        self.results_table.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.results_table.setLineWidth(-2)
        self.results_table.setAutoScrollMargin(5)
        self.results_table.setAlternatingRowColors(True)
        self.results_table.setRowCount(842)
        self.results_table.setColumnCount(2)
        self.results_table.setObjectName("results_table")
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setItem(1, 0, item)
        self.results_table.horizontalHeader().setDefaultSectionSize(191)
        self.results_table.horizontalHeader().setMinimumSectionSize(30)
        self.results_table.verticalHeader().setDefaultSectionSize(23)
        self.results_table.verticalHeader().setMinimumSectionSize(17)
        self.verticalLayout_4.addWidget(self.results_table)
        self.tabWidget.addTab(self.results_tab, "")
        self.ciphertext_tab = QtWidgets.QWidget()
        self.ciphertext_tab.setMinimumSize(QtCore.QSize(6, 0))
        self.ciphertext_tab.setObjectName("ciphertext_tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.ciphertext_tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lpSectionBox = QtWidgets.QGroupBox(self.ciphertext_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lpSectionBox.setFont(font)
        self.lpSectionBox.setFlat(False)
        self.lpSectionBox.setCheckable(False)
        self.lpSectionBox.setObjectName("lpSectionBox")
        self.lpSection = QtWidgets.QGridLayout(self.lpSectionBox)
        self.lpSection.setObjectName("lpSection")
        self.lp_section1 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section1.setObjectName("lp_section1")
        self.lpSection.addWidget(self.lp_section1, 0, 0, 1, 1)
        self.lp_section2 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section2.setObjectName("lp_section2")
        self.lpSection.addWidget(self.lp_section2, 0, 1, 1, 1)
        self.lp_section3 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section3.setObjectName("lp_section3")
        self.lpSection.addWidget(self.lp_section3, 0, 2, 1, 1)
        self.lp_section4 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section4.setObjectName("lp_section4")
        self.lpSection.addWidget(self.lp_section4, 0, 3, 1, 1)
        self.lp_section5 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section5.setObjectName("lp_section5")
        self.lpSection.addWidget(self.lp_section5, 0, 4, 1, 1)
        self.lp_section6 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section6.setObjectName("lp_section6")
        self.lpSection.addWidget(self.lp_section6, 0, 5, 1, 1)
        self.lp_section7 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section7.setObjectName("lp_section7")
        self.lpSection.addWidget(self.lp_section7, 0, 6, 1, 1)
        self.lp_section8 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section8.setObjectName("lp_section8")
        self.lpSection.addWidget(self.lp_section8, 1, 0, 1, 1)
        self.lp_section9 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section9.setObjectName("lp_section9")
        self.lpSection.addWidget(self.lp_section9, 1, 1, 1, 1)
        self.lp_section10 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section10.setObjectName("lp_section10")
        self.lpSection.addWidget(self.lp_section10, 1, 2, 1, 1)
        self.lp_section11 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section11.setObjectName("lp_section11")
        self.lpSection.addWidget(self.lp_section11, 1, 3, 1, 1)
        self.lp_section12 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section12.setObjectName("lp_section12")
        self.lpSection.addWidget(self.lp_section12, 1, 4, 1, 1)
        self.lp_section13 = QtWidgets.QCheckBox(self.lpSectionBox)
        self.lp_section13.setChecked(False)
        self.lp_section13.setObjectName("lp_section13")
        self.lpSection.addWidget(self.lp_section13, 1, 5, 1, 2)
        self.verticalLayout_9.addWidget(self.lpSectionBox)
        self.lpWordSelection = QtWidgets.QGroupBox(self.ciphertext_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lpWordSelection.setFont(font)
        self.lpWordSelection.setObjectName("lpWordSelection")
        self.wordSelection = QtWidgets.QHBoxLayout(self.lpWordSelection)
        self.wordSelection.setObjectName("wordSelection")
        self.ct_word_choice_layout = QtWidgets.QHBoxLayout()
        self.ct_word_choice_layout.setObjectName("ct_word_choice_layout")
        self.startWords = QtWidgets.QRadioButton(self.lpWordSelection)
        self.startWords.setObjectName("startWords")
        self.ct_word_choice_layout.addWidget(self.startWords)
        self.endWords = QtWidgets.QRadioButton(self.lpWordSelection)
        self.endWords.setObjectName("endWords")
        self.ct_word_choice_layout.addWidget(self.endWords)
        self.startAndEndWords = QtWidgets.QRadioButton(self.lpWordSelection)
        self.startAndEndWords.setObjectName("startAndEndWords")
        self.ct_word_choice_layout.addWidget(self.startAndEndWords)
        self.allWords = QtWidgets.QRadioButton(self.lpWordSelection)
        self.allWords.setObjectName("allWords")
        self.ct_word_choice_layout.addWidget(self.allWords)
        self.wordSelection.addLayout(self.ct_word_choice_layout)
        self.verticalLayout_9.addWidget(self.lpWordSelection)
        self.lpRedRunesBox = QtWidgets.QGroupBox(self.ciphertext_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lpRedRunesBox.setFont(font)
        self.lpRedRunesBox.setFlat(False)
        self.lpRedRunesBox.setCheckable(False)
        self.lpRedRunesBox.setObjectName("lpRedRunesBox")
        self.redrunes = QtWidgets.QGridLayout(self.lpRedRunesBox)
        self.redrunes.setObjectName("redrunes")
        self.rr_7 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_7.setObjectName("rr_7")
        self.redrunes.addWidget(self.rr_7, 0, 6, 1, 1)
        self.rr_1 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_1.setObjectName("rr_1")
        self.redrunes.addWidget(self.rr_1, 0, 0, 1, 1)
        self.rr_3 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_3.setObjectName("rr_3")
        self.redrunes.addWidget(self.rr_3, 0, 2, 1, 1)
        self.rr_8 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_8.setObjectName("rr_8")
        self.redrunes.addWidget(self.rr_8, 0, 7, 1, 1)
        self.rr_2 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_2.setObjectName("rr_2")
        self.redrunes.addWidget(self.rr_2, 0, 1, 1, 1)
        self.rr_6 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_6.setObjectName("rr_6")
        self.redrunes.addWidget(self.rr_6, 0, 5, 1, 1)
        self.rr_5 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_5.setObjectName("rr_5")
        self.redrunes.addWidget(self.rr_5, 0, 4, 1, 1)
        self.rr_4 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_4.setObjectName("rr_4")
        self.redrunes.addWidget(self.rr_4, 0, 3, 1, 1)
        self.rr_9 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_9.setObjectName("rr_9")
        self.redrunes.addWidget(self.rr_9, 1, 0, 1, 1)
        self.rr_10 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_10.setObjectName("rr_10")
        self.redrunes.addWidget(self.rr_10, 1, 1, 1, 1)
        self.rr_11 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_11.setObjectName("rr_11")
        self.redrunes.addWidget(self.rr_11, 1, 2, 1, 1)
        self.rr_12 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_12.setObjectName("rr_12")
        self.redrunes.addWidget(self.rr_12, 1, 3, 1, 1)
        self.rr_13 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_13.setMaximumSize(QtCore.QSize(16777215, 16777207))
        self.rr_13.setChecked(False)
        self.rr_13.setObjectName("rr_13")
        self.redrunes.addWidget(self.rr_13, 1, 4, 1, 1)
        self.rr_14 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_14.setObjectName("rr_14")
        self.redrunes.addWidget(self.rr_14, 1, 5, 1, 1)
        self.rr_15 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_15.setObjectName("rr_15")
        self.redrunes.addWidget(self.rr_15, 1, 6, 1, 1)
        self.rr_16 = QtWidgets.QCheckBox(self.lpRedRunesBox)
        self.rr_16.setObjectName("rr_16")
        self.redrunes.addWidget(self.rr_16, 1, 7, 1, 1)
        self.verticalLayout_9.addWidget(self.lpRedRunesBox)
        self.ct_display_format_box = QtWidgets.QGroupBox(self.ciphertext_tab)
        self.ct_display_format_box.setObjectName("ct_display_format_box")
        self.ct_display_format_layout = QtWidgets.QHBoxLayout(self.ct_display_format_box)
        self.ct_display_format_layout.setContentsMargins(2, 4, 2, 4)
        self.ct_display_format_layout.setSpacing(4)
        self.ct_display_format_layout.setObjectName("ct_display_format_layout")
        self.ct_runes_radio = QtWidgets.QRadioButton(self.ct_display_format_box)
        self.ct_runes_radio.setChecked(True)
        self.ct_runes_radio.setObjectName("ct_runes_radio")
        self.ct_display_format_layout.addWidget(self.ct_runes_radio)
        self.ct_runes_eng_radio = QtWidgets.QRadioButton(self.ct_display_format_box)
        self.ct_runes_eng_radio.setObjectName("ct_runes_eng_radio")
        self.ct_display_format_layout.addWidget(self.ct_runes_eng_radio)
        self.ct_prime_radio = QtWidgets.QRadioButton(self.ct_display_format_box)
        self.ct_prime_radio.setObjectName("ct_prime_radio")
        self.ct_display_format_layout.addWidget(self.ct_prime_radio)
        self.ct_forward_position_radio = QtWidgets.QRadioButton(self.ct_display_format_box)
        self.ct_forward_position_radio.setObjectName("ct_forward_position_radio")
        self.ct_display_format_layout.addWidget(self.ct_forward_position_radio)
        self.ct_reverse_position_radio = QtWidgets.QRadioButton(self.ct_display_format_box)
        self.ct_reverse_position_radio.setObjectName("ct_reverse_position_radio")
        self.ct_display_format_layout.addWidget(self.ct_reverse_position_radio)
        self.verticalLayout_9.addWidget(self.ct_display_format_box)
        self.ct_display_box = QtWidgets.QGroupBox(self.ciphertext_tab)
        self.ct_display_box.setObjectName("ct_display_box")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.ct_display_box)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.cipherTextPad = QTextEditOverload(self.ct_display_box)
        self.cipherTextPad.setObjectName("cipherTextPad")
        self.verticalLayout_18.addWidget(self.cipherTextPad)
        self.verticalLayout_9.addWidget(self.ct_display_box)
        self.groupBox_5 = QtWidgets.QGroupBox(self.ciphertext_tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.tb_lr_ciphertext_order = QtWidgets.QRadioButton(self.groupBox_5)
        self.tb_lr_ciphertext_order.setChecked(True)
        self.tb_lr_ciphertext_order.setObjectName("tb_lr_ciphertext_order")
        self.horizontalLayout_19.addWidget(self.tb_lr_ciphertext_order)
        self.bt_rl_ciphertext_order = QtWidgets.QRadioButton(self.groupBox_5)
        self.bt_rl_ciphertext_order.setObjectName("bt_rl_ciphertext_order")
        self.horizontalLayout_19.addWidget(self.bt_rl_ciphertext_order)
        self.custom_ciphertext_order = QtWidgets.QRadioButton(self.groupBox_5)
        self.custom_ciphertext_order.setObjectName("custom_ciphertext_order")
        self.horizontalLayout_19.addWidget(self.custom_ciphertext_order)
        self.horizontalLayout_19.setStretch(0, 3)
        self.horizontalLayout_19.setStretch(1, 3)
        self.horizontalLayout_19.setStretch(2, 1)
        self.verticalLayout_15.addLayout(self.horizontalLayout_19)
        self.cipherTextOrderTextPad = QTextEditOverload(self.groupBox_5)
        self.cipherTextOrderTextPad.setObjectName("cipherTextOrderTextPad")
        self.verticalLayout_15.addWidget(self.cipherTextOrderTextPad)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        self.tabWidget.addTab(self.ciphertext_tab, "")
        self.Keys_Tab = QtWidgets.QWidget()
        self.Keys_Tab.setObjectName("Keys_Tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Keys_Tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.key_display_format_box = QtWidgets.QGroupBox(self.Keys_Tab)
        self.key_display_format_box.setObjectName("key_display_format_box")
        self.key_display_format_layout = QtWidgets.QHBoxLayout(self.key_display_format_box)
        self.key_display_format_layout.setContentsMargins(0, 4, 0, 4)
        self.key_display_format_layout.setSpacing(0)
        self.key_display_format_layout.setObjectName("key_display_format_layout")
        self.key_runes_radio = QtWidgets.QRadioButton(self.key_display_format_box)
        self.key_runes_radio.setObjectName("key_runes_radio")
        self.key_display_format_layout.addWidget(self.key_runes_radio)
        self.key_runes_eng_radio = QtWidgets.QRadioButton(self.key_display_format_box)
        self.key_runes_eng_radio.setObjectName("key_runes_eng_radio")
        self.key_display_format_layout.addWidget(self.key_runes_eng_radio)
        self.key_prime_radio = QtWidgets.QRadioButton(self.key_display_format_box)
        self.key_prime_radio.setObjectName("key_prime_radio")
        self.key_display_format_layout.addWidget(self.key_prime_radio)
        self.key_forward_position_radio = QtWidgets.QRadioButton(self.key_display_format_box)
        self.key_forward_position_radio.setObjectName("key_forward_position_radio")
        self.key_display_format_layout.addWidget(self.key_forward_position_radio)
        self.key_reverse_position_radio = QtWidgets.QRadioButton(self.key_display_format_box)
        self.key_reverse_position_radio.setObjectName("key_reverse_position_radio")
        self.key_display_format_layout.addWidget(self.key_reverse_position_radio)
        self.verticalLayout.addWidget(self.key_display_format_box)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.rune_key_sample_4 = QtWidgets.QLabel(self.Keys_Tab)
        self.rune_key_sample_4.setAlignment(QtCore.Qt.AlignCenter)
        self.rune_key_sample_4.setIndent(10)
        self.rune_key_sample_4.setObjectName("rune_key_sample_4")
        self.gridLayout.addWidget(self.rune_key_sample_4, 5, 0, 1, 2)
        self.rune_key_sample_5 = QtWidgets.QLabel(self.Keys_Tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rune_key_sample_5.setFont(font)
        self.rune_key_sample_5.setAlignment(QtCore.Qt.AlignCenter)
        self.rune_key_sample_5.setIndent(10)
        self.rune_key_sample_5.setObjectName("rune_key_sample_5")
        self.gridLayout.addWidget(self.rune_key_sample_5, 2, 0, 1, 2)
        self.rune_key_sample = QtWidgets.QLabel(self.Keys_Tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rune_key_sample.setFont(font)
        self.rune_key_sample.setIndent(10)
        self.rune_key_sample.setObjectName("rune_key_sample")
        self.gridLayout.addWidget(self.rune_key_sample, 3, 2, 1, 1)
        self.rune_key_sample_6 = QtWidgets.QLabel(self.Keys_Tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rune_key_sample_6.setFont(font)
        self.rune_key_sample_6.setAlignment(QtCore.Qt.AlignCenter)
        self.rune_key_sample_6.setIndent(10)
        self.rune_key_sample_6.setObjectName("rune_key_sample_6")
        self.gridLayout.addWidget(self.rune_key_sample_6, 2, 2, 1, 1)
        self.key_entry_textedit = QTextEditOverload(self.Keys_Tab)
        self.key_entry_textedit.setMinimumSize(QtCore.QSize(0, 0))
        self.key_entry_textedit.setOverwriteMode(False)
        self.key_entry_textedit.setObjectName("key_entry_textedit")
        self.gridLayout.addWidget(self.key_entry_textedit, 1, 0, 1, 2)
        self.processed_key_display_textedit = QtWidgets.QPlainTextEdit(self.Keys_Tab)
        self.processed_key_display_textedit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.processed_key_display_textedit.setFont(font)
        self.processed_key_display_textedit.setToolTip("")
        self.processed_key_display_textedit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.processed_key_display_textedit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.processed_key_display_textedit.setObjectName("processed_key_display_textedit")
        self.gridLayout.addWidget(self.processed_key_display_textedit, 1, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.Keys_Tab)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.key_count_label = QtWidgets.QLabel(self.Keys_Tab)
        self.key_count_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.key_count_label.setObjectName("key_count_label")
        self.horizontalLayout_2.addWidget(self.key_count_label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.number_key_sample = QtWidgets.QLabel(self.Keys_Tab)
        self.number_key_sample.setIndent(10)
        self.number_key_sample.setObjectName("number_key_sample")
        self.gridLayout.addWidget(self.number_key_sample, 5, 2, 1, 1)
        self.rune_key_sample_2 = QtWidgets.QLabel(self.Keys_Tab)
        self.rune_key_sample_2.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rune_key_sample_2.setFont(font)
        self.rune_key_sample_2.setAlignment(QtCore.Qt.AlignCenter)
        self.rune_key_sample_2.setIndent(10)
        self.rune_key_sample_2.setObjectName("rune_key_sample_2")
        self.gridLayout.addWidget(self.rune_key_sample_2, 3, 0, 1, 2)
        self.english_key_sample = QtWidgets.QLabel(self.Keys_Tab)
        self.english_key_sample.setIndent(10)
        self.english_key_sample.setObjectName("english_key_sample")
        self.gridLayout.addWidget(self.english_key_sample, 4, 2, 1, 1)
        self.rune_key_sample_3 = QtWidgets.QLabel(self.Keys_Tab)
        self.rune_key_sample_3.setAlignment(QtCore.Qt.AlignCenter)
        self.rune_key_sample_3.setIndent(10)
        self.rune_key_sample_3.setObjectName("rune_key_sample_3")
        self.gridLayout.addWidget(self.rune_key_sample_3, 4, 0, 1, 2)
        self.save_key_file_button = QtWidgets.QPushButton(self.Keys_Tab)
        self.save_key_file_button.setObjectName("save_key_file_button")
        self.gridLayout.addWidget(self.save_key_file_button, 7, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.Keys_Tab)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.Keys_Tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 2)
        self.load_key_file_button = QtWidgets.QPushButton(self.Keys_Tab)
        self.load_key_file_button.setObjectName("load_key_file_button")
        self.gridLayout.addWidget(self.load_key_file_button, 7, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.Keys_Tab, "")
        self.encryption_tab4 = QtWidgets.QWidget()
        self.encryption_tab4.setObjectName("encryption_tab4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.encryption_tab4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_72 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)
        self.label_72.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.label_72.setAlignment(QtCore.Qt.AlignCenter)
        self.label_72.setObjectName("label_72")
        self.verticalLayout_2.addWidget(self.label_72)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pre_computed_encryption_map_load = QtWidgets.QPushButton(self.encryption_tab4)
        self.pre_computed_encryption_map_load.setObjectName("pre_computed_encryption_map_load")
        self.horizontalLayout_3.addWidget(self.pre_computed_encryption_map_load)
        self.pre_computed_encryption_map_combobox = QtWidgets.QComboBox(self.encryption_tab4)
        self.pre_computed_encryption_map_combobox.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pre_computed_encryption_map_combobox.setFont(font)
        self.pre_computed_encryption_map_combobox.setObjectName("pre_computed_encryption_map_combobox")
        self.horizontalLayout_3.addWidget(self.pre_computed_encryption_map_combobox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_4 = QtWidgets.QFrame(self.encryption_tab4)
        self.line_4.setLineWidth(2)
        self.line_4.setMidLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_74 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.verticalLayout_2.addWidget(self.label_74)
        self.label_108 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_108.setFont(font)
        self.label_108.setScaledContents(True)
        self.label_108.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_108.setWordWrap(True)
        self.label_108.setObjectName("label_108")
        self.verticalLayout_2.addWidget(self.label_108)
        self.enc_method_function_textbox = QtWidgets.QLineEdit(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enc_method_function_textbox.setFont(font)
        self.enc_method_function_textbox.setObjectName("enc_method_function_textbox")
        self.verticalLayout_2.addWidget(self.enc_method_function_textbox)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_122 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_122.setFont(font)
        self.label_122.setScaledContents(True)
        self.label_122.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_122.setWordWrap(True)
        self.label_122.setObjectName("label_122")
        self.gridLayout_2.addWidget(self.label_122, 1, 0, 1, 1)
        self.label_110 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_110.setFont(font)
        self.label_110.setScaledContents(True)
        self.label_110.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_110.setWordWrap(True)
        self.label_110.setObjectName("label_110")
        self.gridLayout_2.addWidget(self.label_110, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_111 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_111.setFont(font)
        self.label_111.setScaledContents(True)
        self.label_111.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_111.setWordWrap(True)
        self.label_111.setObjectName("label_111")
        self.gridLayout_2.addWidget(self.label_111, 1, 3, 1, 1)
        self.label_117 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_117.setFont(font)
        self.label_117.setObjectName("label_117")
        self.gridLayout_2.addWidget(self.label_117, 0, 0, 1, 1)
        self.enc_method_name_textbox = QtWidgets.QLineEdit(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enc_method_name_textbox.setFont(font)
        self.enc_method_name_textbox.setObjectName("enc_method_name_textbox")
        self.gridLayout_2.addWidget(self.enc_method_name_textbox, 0, 1, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.line_5 = QtWidgets.QFrame(self.encryption_tab4)
        self.line_5.setLineWidth(2)
        self.line_5.setMidLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_119 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_119.setFont(font)
        self.label_119.setAlignment(QtCore.Qt.AlignCenter)
        self.label_119.setObjectName("label_119")
        self.gridLayout_9.addWidget(self.label_119, 1, 2, 1, 1)
        self.label_118 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_118.setFont(font)
        self.label_118.setAlignment(QtCore.Qt.AlignCenter)
        self.label_118.setObjectName("label_118")
        self.gridLayout_9.addWidget(self.label_118, 0, 2, 1, 1)
        self.encryption_table = QtWidgets.QTableWidget(self.encryption_tab4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encryption_table.sizePolicy().hasHeightForWidth())
        self.encryption_table.setSizePolicy(sizePolicy)
        self.encryption_table.setMinimumSize(QtCore.QSize(0, 0))
        self.encryption_table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encryption_table.setFont(font)
        self.encryption_table.setAutoScrollMargin(5)
        self.encryption_table.setAlternatingRowColors(True)
        self.encryption_table.setRowCount(842)
        self.encryption_table.setColumnCount(2)
        self.encryption_table.setObjectName("encryption_table")
        item = QtWidgets.QTableWidgetItem()
        self.encryption_table.setItem(1, 0, item)
        self.gridLayout_9.addWidget(self.encryption_table, 2, 2, 1, 1)
        self.label_120 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_120.setFont(font)
        self.label_120.setAlignment(QtCore.Qt.AlignCenter)
        self.label_120.setObjectName("label_120")
        self.gridLayout_9.addWidget(self.label_120, 3, 2, 1, 1)
        self.label_104 = QtWidgets.QLabel(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_104.setFont(font)
        self.label_104.setAlignment(QtCore.Qt.AlignCenter)
        self.label_104.setObjectName("label_104")
        self.gridLayout_9.addWidget(self.label_104, 0, 0, 2, 1)
        self.decryption_table = QtWidgets.QTableWidget(self.encryption_tab4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decryption_table.sizePolicy().hasHeightForWidth())
        self.decryption_table.setSizePolicy(sizePolicy)
        self.decryption_table.setMinimumSize(QtCore.QSize(0, 0))
        self.decryption_table.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decryption_table.setFont(font)
        self.decryption_table.setAlternatingRowColors(True)
        self.decryption_table.setRowCount(842)
        self.decryption_table.setColumnCount(2)
        self.decryption_table.setObjectName("decryption_table")
        item = QtWidgets.QTableWidgetItem()
        self.decryption_table.setItem(1, 0, item)
        self.gridLayout_9.addWidget(self.decryption_table, 4, 2, 1, 1)
        self.encryption_map_text_entry = QTextEditOverload(self.encryption_tab4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encryption_map_text_entry.setFont(font)
        self.encryption_map_text_entry.setObjectName("encryption_map_text_entry")
        self.gridLayout_9.addWidget(self.encryption_map_text_entry, 2, 0, 3, 1)
        self.line_6 = QtWidgets.QFrame(self.encryption_tab4)
        self.line_6.setLineWidth(20)
        self.line_6.setMidLineWidth(20)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_9.addWidget(self.line_6, 0, 1, 5, 1)
        self.gridLayout_9.setColumnStretch(0, 3)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setColumnStretch(2, 10)
        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_9.setRowStretch(1, 1)
        self.gridLayout_9.setRowStretch(2, 15)
        self.gridLayout_9.setRowStretch(3, 1)
        self.gridLayout_9.setRowStretch(4, 15)
        self.verticalLayout_2.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.encryption_tab4, "")
        self.options_tab = QtWidgets.QWidget()
        self.options_tab.setObjectName("options_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.options_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.options_tab)
        self.groupBox.setToolTipDuration(5)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setContentsMargins(-1, 4, 4, 2)
        self.gridLayout_6.setHorizontalSpacing(4)
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.test_enc_method_17 = QtWidgets.QLabel(self.groupBox)
        self.test_enc_method_17.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_enc_method_17.setFont(font)
        self.test_enc_method_17.setObjectName("test_enc_method_17")
        self.gridLayout_6.addWidget(self.test_enc_method_17, 2, 0, 1, 1)
        self.test_enc_method_4 = QtWidgets.QLabel(self.groupBox)
        self.test_enc_method_4.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_enc_method_4.setFont(font)
        self.test_enc_method_4.setObjectName("test_enc_method_4")
        self.gridLayout_6.addWidget(self.test_enc_method_4, 2, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_6.addWidget(self.checkBox_2, 0, 0, 1, 4)
        self.log_prob_min_lab = QtWidgets.QLabel(self.groupBox)
        self.log_prob_min_lab.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log_prob_min_lab.setFont(font)
        self.log_prob_min_lab.setToolTip("")
        self.log_prob_min_lab.setToolTipDuration(-1)
        self.log_prob_min_lab.setStatusTip("")
        self.log_prob_min_lab.setWhatsThis("")
        self.log_prob_min_lab.setObjectName("log_prob_min_lab")
        self.gridLayout_6.addWidget(self.log_prob_min_lab, 1, 2, 1, 1)
        self.test_enc_method_18 = QtWidgets.QLabel(self.groupBox)
        self.test_enc_method_18.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_enc_method_18.setFont(font)
        self.test_enc_method_18.setObjectName("test_enc_method_18")
        self.gridLayout_6.addWidget(self.test_enc_method_18, 1, 0, 1, 1)
        self.min_score_per_4gram_gradient = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.min_score_per_4gram_gradient.setToolTip("")
        self.min_score_per_4gram_gradient.setToolTipDuration(-1)
        self.min_score_per_4gram_gradient.setMinimum(-1000.0)
        self.min_score_per_4gram_gradient.setMaximum(0.0)
        self.min_score_per_4gram_gradient.setProperty("value", -5.7)
        self.min_score_per_4gram_gradient.setObjectName("min_score_per_4gram_gradient")
        self.gridLayout_6.addWidget(self.min_score_per_4gram_gradient, 2, 1, 1, 1)
        self.min_score_per_4gram_offset = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.min_score_per_4gram_offset.setToolTip("")
        self.min_score_per_4gram_offset.setToolTipDuration(-1)
        self.min_score_per_4gram_offset.setMinimum(-100.0)
        self.min_score_per_4gram_offset.setMaximum(0.0)
        self.min_score_per_4gram_offset.setProperty("value", -3.25)
        self.min_score_per_4gram_offset.setObjectName("min_score_per_4gram_offset")
        self.gridLayout_6.addWidget(self.min_score_per_4gram_offset, 1, 1, 1, 1)
        self.four_gram_count_cut = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.four_gram_count_cut.setFont(font)
        self.four_gram_count_cut.setMinimum(1)
        self.four_gram_count_cut.setMaximum(1000000000)
        self.four_gram_count_cut.setProperty("value", 1000)
        self.four_gram_count_cut.setObjectName("four_gram_count_cut")
        self.gridLayout_6.addWidget(self.four_gram_count_cut, 2, 3, 1, 1)
        self.four_gram_log_prob_min = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.four_gram_log_prob_min.setToolTip("")
        self.four_gram_log_prob_min.setToolTipDuration(-1)
        self.four_gram_log_prob_min.setMinimum(-1000.0)
        self.four_gram_log_prob_min.setMaximum(-7.0)
        self.four_gram_log_prob_min.setProperty("value", -20.0)
        self.four_gram_log_prob_min.setObjectName("four_gram_log_prob_min")
        self.gridLayout_6.addWidget(self.four_gram_log_prob_min, 1, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_6 = QtWidgets.QGroupBox(self.options_tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.undefined_answers_are_all = QtWidgets.QCheckBox(self.groupBox_6)
        self.undefined_answers_are_all.setMinimumSize(QtCore.QSize(18, 0))
        self.undefined_answers_are_all.setMaximumSize(QtCore.QSize(20, 16777215))
        self.undefined_answers_are_all.setText("")
        self.undefined_answers_are_all.setIconSize(QtCore.QSize(16, 16))
        self.undefined_answers_are_all.setObjectName("undefined_answers_are_all")
        self.gridLayout_7.addWidget(self.undefined_answers_are_all, 1, 1, 1, 1)
        self.score_reversed_decryption = QtWidgets.QCheckBox(self.groupBox_6)
        self.score_reversed_decryption.setMinimumSize(QtCore.QSize(18, 0))
        self.score_reversed_decryption.setMaximumSize(QtCore.QSize(20, 16777215))
        self.score_reversed_decryption.setText("")
        self.score_reversed_decryption.setObjectName("score_reversed_decryption")
        self.gridLayout_7.addWidget(self.score_reversed_decryption, 1, 4, 1, 1)
        self.test_enc_method_13 = QtWidgets.QLabel(self.groupBox_6)
        self.test_enc_method_13.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_13.setFont(font)
        self.test_enc_method_13.setObjectName("test_enc_method_13")
        self.gridLayout_7.addWidget(self.test_enc_method_13, 1, 0, 1, 1)
        self.test_enc_method_16 = QtWidgets.QLabel(self.groupBox_6)
        self.test_enc_method_16.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_16.setFont(font)
        self.test_enc_method_16.setObjectName("test_enc_method_16")
        self.gridLayout_7.addWidget(self.test_enc_method_16, 1, 3, 1, 1)
        self.save_rejected_results = QtWidgets.QCheckBox(self.groupBox_6)
        self.save_rejected_results.setMinimumSize(QtCore.QSize(18, 0))
        self.save_rejected_results.setMaximumSize(QtCore.QSize(20, 16777215))
        self.save_rejected_results.setText("")
        self.save_rejected_results.setObjectName("save_rejected_results")
        self.gridLayout_7.addWidget(self.save_rejected_results, 0, 1, 1, 1)
        self.use_reverse_keys = QtWidgets.QCheckBox(self.groupBox_6)
        self.use_reverse_keys.setMinimumSize(QtCore.QSize(18, 0))
        self.use_reverse_keys.setMaximumSize(QtCore.QSize(20, 16777215))
        self.use_reverse_keys.setText("")
        self.use_reverse_keys.setObjectName("use_reverse_keys")
        self.gridLayout_7.addWidget(self.use_reverse_keys, 0, 4, 1, 1)
        self.test_enc_method_14 = QtWidgets.QLabel(self.groupBox_6)
        self.test_enc_method_14.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_14.setFont(font)
        self.test_enc_method_14.setObjectName("test_enc_method_14")
        self.gridLayout_7.addWidget(self.test_enc_method_14, 0, 3, 1, 1)
        self.test_enc_method_6 = QtWidgets.QLabel(self.groupBox_6)
        self.test_enc_method_6.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_6.setFont(font)
        self.test_enc_method_6.setObjectName("test_enc_method_6")
        self.gridLayout_7.addWidget(self.test_enc_method_6, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_6)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 2, 0, 1, 1)
        self.four_gram_max_num_zero_count = QtWidgets.QSpinBox(self.groupBox_6)
        self.four_gram_max_num_zero_count.setMaximumSize(QtCore.QSize(20, 16777215))
        self.four_gram_max_num_zero_count.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.four_gram_max_num_zero_count.setMaximum(9)
        self.four_gram_max_num_zero_count.setProperty("value", 3)
        self.four_gram_max_num_zero_count.setObjectName("four_gram_max_num_zero_count")
        self.gridLayout_7.addWidget(self.four_gram_max_num_zero_count, 2, 1, 1, 1)
        self.test_enc_method_23 = QtWidgets.QLabel(self.groupBox_6)
        self.test_enc_method_23.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_23.setFont(font)
        self.test_enc_method_23.setObjectName("test_enc_method_23")
        self.gridLayout_7.addWidget(self.test_enc_method_23, 2, 3, 1, 1)
        self.wrap_key_around_ct = QtWidgets.QCheckBox(self.groupBox_6)
        self.wrap_key_around_ct.setMinimumSize(QtCore.QSize(18, 0))
        self.wrap_key_around_ct.setMaximumSize(QtCore.QSize(20, 16777215))
        self.wrap_key_around_ct.setText("")
        self.wrap_key_around_ct.setObjectName("wrap_key_around_ct")
        self.gridLayout_7.addWidget(self.wrap_key_around_ct, 2, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.options_tab)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.test_enc_method_22 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_22.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_22.setFont(font)
        self.test_enc_method_22.setObjectName("test_enc_method_22")
        self.gridLayout_3.addWidget(self.test_enc_method_22, 3, 4, 1, 1)
        self.test_enc_method_9 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_9.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_9.setFont(font)
        self.test_enc_method_9.setObjectName("test_enc_method_9")
        self.gridLayout_3.addWidget(self.test_enc_method_9, 1, 2, 1, 1)
        self.min_distance_9rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_9rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_9rune.setMaximum(8)
        self.min_distance_9rune.setProperty("value", 4)
        self.min_distance_9rune.setObjectName("min_distance_9rune")
        self.gridLayout_3.addWidget(self.min_distance_9rune, 3, 5, 1, 1)
        self.min_distance_10rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_10rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_10rune.setMaximum(10)
        self.min_distance_10rune.setProperty("value", 4)
        self.min_distance_10rune.setObjectName("min_distance_10rune")
        self.gridLayout_3.addWidget(self.min_distance_10rune, 4, 1, 1, 1)
        self.min_distance_5rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_5rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_5rune.setMaximum(5)
        self.min_distance_5rune.setSingleStep(1)
        self.min_distance_5rune.setProperty("value", 2)
        self.min_distance_5rune.setObjectName("min_distance_5rune")
        self.gridLayout_3.addWidget(self.min_distance_5rune, 2, 3, 1, 1)
        self.test_enc_method_11 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_11.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_11.setFont(font)
        self.test_enc_method_11.setObjectName("test_enc_method_11")
        self.gridLayout_3.addWidget(self.test_enc_method_11, 2, 0, 1, 1)
        self.test_enc_method_21 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_21.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_21.setFont(font)
        self.test_enc_method_21.setObjectName("test_enc_method_21")
        self.gridLayout_3.addWidget(self.test_enc_method_21, 3, 2, 1, 1)
        self.test_enc_method_10 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_10.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_10.setFont(font)
        self.test_enc_method_10.setObjectName("test_enc_method_10")
        self.gridLayout_3.addWidget(self.test_enc_method_10, 1, 4, 1, 1)
        self.min_distance_2rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_2rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_2rune.setMaximum(2)
        self.min_distance_2rune.setProperty("value", 1)
        self.min_distance_2rune.setObjectName("min_distance_2rune")
        self.gridLayout_3.addWidget(self.min_distance_2rune, 1, 3, 1, 1)
        self.min_distance_7rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_7rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_7rune.setMaximum(7)
        self.min_distance_7rune.setProperty("value", 3)
        self.min_distance_7rune.setObjectName("min_distance_7rune")
        self.gridLayout_3.addWidget(self.min_distance_7rune, 3, 1, 1, 1)
        self.min_distance_3rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_3rune.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.min_distance_3rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_3rune.setProperty("value", 1)
        self.min_distance_3rune.setObjectName("min_distance_3rune")
        self.gridLayout_3.addWidget(self.min_distance_3rune, 1, 5, 1, 1)
        self.test_enc_method_15 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_15.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_15.setFont(font)
        self.test_enc_method_15.setObjectName("test_enc_method_15")
        self.gridLayout_3.addWidget(self.test_enc_method_15, 2, 4, 1, 1)
        self.test_enc_method_25 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_25.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_25.setFont(font)
        self.test_enc_method_25.setObjectName("test_enc_method_25")
        self.gridLayout_3.addWidget(self.test_enc_method_25, 4, 2, 1, 1)
        self.test_enc_method_20 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_20.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_20.setFont(font)
        self.test_enc_method_20.setObjectName("test_enc_method_20")
        self.gridLayout_3.addWidget(self.test_enc_method_20, 3, 0, 1, 1)
        self.test_enc_method_24 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_24.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_24.setFont(font)
        self.test_enc_method_24.setObjectName("test_enc_method_24")
        self.gridLayout_3.addWidget(self.test_enc_method_24, 4, 0, 1, 1)
        self.min_distance_1rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_1rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_1rune.setMaximum(1)
        self.min_distance_1rune.setProperty("value", 1)
        self.min_distance_1rune.setObjectName("min_distance_1rune")
        self.gridLayout_3.addWidget(self.min_distance_1rune, 1, 1, 1, 1)
        self.min_distance_8rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_8rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_8rune.setMaximum(8)
        self.min_distance_8rune.setProperty("value", 3)
        self.min_distance_8rune.setObjectName("min_distance_8rune")
        self.gridLayout_3.addWidget(self.min_distance_8rune, 3, 3, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 6)
        self.min_distance_4rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_4rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_4rune.setMaximum(4)
        self.min_distance_4rune.setProperty("value", 1)
        self.min_distance_4rune.setObjectName("min_distance_4rune")
        self.gridLayout_3.addWidget(self.min_distance_4rune, 2, 1, 1, 1)
        self.test_enc_method_19 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_19.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_19.setFont(font)
        self.test_enc_method_19.setObjectName("test_enc_method_19")
        self.gridLayout_3.addWidget(self.test_enc_method_19, 1, 0, 1, 1)
        self.min_distance_6rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_6rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_6rune.setProperty("value", 2)
        self.min_distance_6rune.setObjectName("min_distance_6rune")
        self.gridLayout_3.addWidget(self.min_distance_6rune, 2, 5, 1, 1)
        self.min_distance_11rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_11rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_11rune.setMaximum(11)
        self.min_distance_11rune.setProperty("value", 5)
        self.min_distance_11rune.setObjectName("min_distance_11rune")
        self.gridLayout_3.addWidget(self.min_distance_11rune, 4, 3, 1, 1)
        self.test_enc_method_12 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_12.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_12.setFont(font)
        self.test_enc_method_12.setObjectName("test_enc_method_12")
        self.gridLayout_3.addWidget(self.test_enc_method_12, 2, 2, 1, 1)
        self.test_enc_method_26 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_26.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_26.setFont(font)
        self.test_enc_method_26.setObjectName("test_enc_method_26")
        self.gridLayout_3.addWidget(self.test_enc_method_26, 4, 4, 1, 1)
        self.min_distance_12rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_12rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_12rune.setMinimum(0)
        self.min_distance_12rune.setMaximum(12)
        self.min_distance_12rune.setProperty("value", 5)
        self.min_distance_12rune.setObjectName("min_distance_12rune")
        self.gridLayout_3.addWidget(self.min_distance_12rune, 4, 5, 1, 1)
        self.test_enc_method_27 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_27.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_27.setFont(font)
        self.test_enc_method_27.setObjectName("test_enc_method_27")
        self.gridLayout_3.addWidget(self.test_enc_method_27, 5, 0, 1, 1)
        self.test_enc_method_28 = QtWidgets.QLabel(self.groupBox_7)
        self.test_enc_method_28.setSizeIncrement(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test_enc_method_28.setFont(font)
        self.test_enc_method_28.setObjectName("test_enc_method_28")
        self.gridLayout_3.addWidget(self.test_enc_method_28, 5, 2, 1, 1)
        self.min_distance_13rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_13rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_13rune.setMaximum(13)
        self.min_distance_13rune.setProperty("value", 6)
        self.min_distance_13rune.setObjectName("min_distance_13rune")
        self.gridLayout_3.addWidget(self.min_distance_13rune, 5, 1, 1, 1)
        self.min_distance_14rune = QtWidgets.QSpinBox(self.groupBox_7)
        self.min_distance_14rune.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.min_distance_14rune.setMaximum(14)
        self.min_distance_14rune.setProperty("value", 6)
        self.min_distance_14rune.setObjectName("min_distance_14rune")
        self.gridLayout_3.addWidget(self.min_distance_14rune, 5, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.ct_shift_groupbox = QtWidgets.QGroupBox(self.options_tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ct_shift_groupbox.setFont(font)
        self.ct_shift_groupbox.setObjectName("ct_shift_groupbox")
        self.ct_shift_layout = QtWidgets.QHBoxLayout(self.ct_shift_groupbox)
        self.ct_shift_layout.setObjectName("ct_shift_layout")
        self.ct_forward_gematria = QtWidgets.QCheckBox(self.ct_shift_groupbox)
        self.ct_forward_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.ct_forward_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ct_forward_gematria.setFont(font)
        self.ct_forward_gematria.setObjectName("ct_forward_gematria")
        self.ct_shift_layout.addWidget(self.ct_forward_gematria)
        self.ct_reverse_gematria = QtWidgets.QCheckBox(self.ct_shift_groupbox)
        self.ct_reverse_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.ct_reverse_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ct_reverse_gematria.setFont(font)
        self.ct_reverse_gematria.setObjectName("ct_reverse_gematria")
        self.ct_shift_layout.addWidget(self.ct_reverse_gematria)
        self.ct_all_forward_gematria = QtWidgets.QCheckBox(self.ct_shift_groupbox)
        self.ct_all_forward_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.ct_all_forward_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ct_all_forward_gematria.setFont(font)
        self.ct_all_forward_gematria.setObjectName("ct_all_forward_gematria")
        self.ct_shift_layout.addWidget(self.ct_all_forward_gematria)
        self.ct_all_reverse_gematria = QtWidgets.QCheckBox(self.ct_shift_groupbox)
        self.ct_all_reverse_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.ct_all_reverse_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ct_all_reverse_gematria.setFont(font)
        self.ct_all_reverse_gematria.setObjectName("ct_all_reverse_gematria")
        self.ct_shift_layout.addWidget(self.ct_all_reverse_gematria)
        self.ct_all_gematria = QtWidgets.QCheckBox(self.ct_shift_groupbox)
        self.ct_all_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.ct_all_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ct_all_gematria.setFont(font)
        self.ct_all_gematria.setChecked(False)
        self.ct_all_gematria.setObjectName("ct_all_gematria")
        self.ct_shift_layout.addWidget(self.ct_all_gematria)
        self.verticalLayout_3.addWidget(self.ct_shift_groupbox)
        self.key_shift_groupbox = QtWidgets.QGroupBox(self.options_tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.key_shift_groupbox.setFont(font)
        self.key_shift_groupbox.setObjectName("key_shift_groupbox")
        self.key_shift_layout = QtWidgets.QHBoxLayout(self.key_shift_groupbox)
        self.key_shift_layout.setObjectName("key_shift_layout")
        self.key_forward_gematria = QtWidgets.QCheckBox(self.key_shift_groupbox)
        self.key_forward_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.key_forward_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.key_forward_gematria.setFont(font)
        self.key_forward_gematria.setObjectName("key_forward_gematria")
        self.key_shift_layout.addWidget(self.key_forward_gematria)
        self.key_reverse_gematria = QtWidgets.QCheckBox(self.key_shift_groupbox)
        self.key_reverse_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.key_reverse_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.key_reverse_gematria.setFont(font)
        self.key_reverse_gematria.setObjectName("key_reverse_gematria")
        self.key_shift_layout.addWidget(self.key_reverse_gematria)
        self.key_all_forward_gematria = QtWidgets.QCheckBox(self.key_shift_groupbox)
        self.key_all_forward_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.key_all_forward_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.key_all_forward_gematria.setFont(font)
        self.key_all_forward_gematria.setObjectName("key_all_forward_gematria")
        self.key_shift_layout.addWidget(self.key_all_forward_gematria)
        self.key_all_reverse_gematria = QtWidgets.QCheckBox(self.key_shift_groupbox)
        self.key_all_reverse_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.key_all_reverse_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.key_all_reverse_gematria.setFont(font)
        self.key_all_reverse_gematria.setObjectName("key_all_reverse_gematria")
        self.key_shift_layout.addWidget(self.key_all_reverse_gematria)
        self.key_all_gematria = QtWidgets.QCheckBox(self.key_shift_groupbox)
        self.key_all_gematria.setMinimumSize(QtCore.QSize(0, 0))
        self.key_all_gematria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.key_all_gematria.setFont(font)
        self.key_all_gematria.setChecked(False)
        self.key_all_gematria.setObjectName("key_all_gematria")
        self.key_shift_layout.addWidget(self.key_all_gematria)
        self.verticalLayout_3.addWidget(self.key_shift_groupbox)
        self.interrupterGroupBox = QtWidgets.QGroupBox(self.options_tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.interrupterGroupBox.setFont(font)
        self.interrupterGroupBox.setObjectName("interrupterGroupBox")
        self.interrupter = QtWidgets.QGridLayout(self.interrupterGroupBox)
        self.interrupter.setObjectName("interrupter")
        self.m_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.m_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.m_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.m_interrupter.setFont(font)
        self.m_interrupter.setObjectName("m_interrupter")
        self.interrupter.addWidget(self.m_interrupter, 2, 0, 1, 1)
        self.ing_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.ing_interrupter.setMinimumSize(QtCore.QSize(40, 0))
        self.ing_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ing_interrupter.setFont(font)
        self.ing_interrupter.setObjectName("ing_interrupter")
        self.interrupter.addWidget(self.ing_interrupter, 2, 2, 1, 1)
        self.s_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.s_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.s_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.s_interrupter.setFont(font)
        self.s_interrupter.setObjectName("s_interrupter")
        self.interrupter.addWidget(self.s_interrupter, 1, 6, 1, 1)
        self.ea_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.ea_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.ea_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ea_interrupter.setFont(font)
        self.ea_interrupter.setObjectName("ea_interrupter")
        self.interrupter.addWidget(self.ea_interrupter, 2, 9, 1, 1)
        self.j_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.j_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.j_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.j_interrupter.setFont(font)
        self.j_interrupter.setObjectName("j_interrupter")
        self.interrupter.addWidget(self.j_interrupter, 1, 2, 1, 1)
        self.e_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.e_interrupter.setFont(font)
        self.e_interrupter.setObjectName("e_interrupter")
        self.interrupter.addWidget(self.e_interrupter, 1, 9, 1, 1)
        self.n_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.n_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.n_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.n_interrupter.setFont(font)
        self.n_interrupter.setObjectName("n_interrupter")
        self.interrupter.addWidget(self.n_interrupter, 1, 0, 1, 1)
        self.r_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.r_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.r_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.r_interrupter.setFont(font)
        self.r_interrupter.setObjectName("r_interrupter")
        self.interrupter.addWidget(self.r_interrupter, 0, 5, 1, 1)
        self.u_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.u_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.u_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.u_interrupter.setFont(font)
        self.u_interrupter.setObjectName("u_interrupter")
        self.interrupter.addWidget(self.u_interrupter, 0, 2, 1, 1)
        self.i_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.i_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.i_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.i_interrupter.setFont(font)
        self.i_interrupter.setObjectName("i_interrupter")
        self.interrupter.addWidget(self.i_interrupter, 1, 1, 1, 1)
        self.all_interrupters = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.all_interrupters.setMinimumSize(QtCore.QSize(30, 0))
        self.all_interrupters.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.all_interrupters.setFont(font)
        self.all_interrupters.setObjectName("all_interrupters")
        self.interrupter.addWidget(self.all_interrupters, 0, 0, 1, 1)
        self.d_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.d_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.d_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.d_interrupter.setFont(font)
        self.d_interrupter.setObjectName("d_interrupter")
        self.interrupter.addWidget(self.d_interrupter, 2, 4, 1, 1)
        self.g_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.g_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.g_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.g_interrupter.setFont(font)
        self.g_interrupter.setObjectName("g_interrupter")
        self.interrupter.addWidget(self.g_interrupter, 0, 7, 1, 1)
        self.eo_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.eo_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.eo_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.eo_interrupter.setFont(font)
        self.eo_interrupter.setObjectName("eo_interrupter")
        self.interrupter.addWidget(self.eo_interrupter, 1, 3, 1, 1)
        self.l_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.l_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.l_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.l_interrupter.setFont(font)
        self.l_interrupter.setObjectName("l_interrupter")
        self.interrupter.addWidget(self.l_interrupter, 2, 1, 1, 1)
        self.x_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.x_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.x_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.x_interrupter.setFont(font)
        self.x_interrupter.setObjectName("x_interrupter")
        self.interrupter.addWidget(self.x_interrupter, 1, 5, 1, 1)
        self.h_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.h_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.h_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.h_interrupter.setFont(font)
        self.h_interrupter.setObjectName("h_interrupter")
        self.interrupter.addWidget(self.h_interrupter, 0, 9, 1, 1)
        self.oe_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.oe_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.oe_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.oe_interrupter.setFont(font)
        self.oe_interrupter.setObjectName("oe_interrupter")
        self.interrupter.addWidget(self.oe_interrupter, 2, 3, 1, 1)
        self.th_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.th_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.th_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.th_interrupter.setFont(font)
        self.th_interrupter.setObjectName("th_interrupter")
        self.interrupter.addWidget(self.th_interrupter, 0, 3, 1, 1)
        self.w_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.w_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.w_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.w_interrupter.setFont(font)
        self.w_interrupter.setObjectName("w_interrupter")
        self.interrupter.addWidget(self.w_interrupter, 0, 8, 1, 1)
        self.o_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.o_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.o_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.o_interrupter.setFont(font)
        self.o_interrupter.setObjectName("o_interrupter")
        self.interrupter.addWidget(self.o_interrupter, 0, 4, 1, 1)
        self.b_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.b_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.b_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.b_interrupter.setFont(font)
        self.b_interrupter.setObjectName("b_interrupter")
        self.interrupter.addWidget(self.b_interrupter, 1, 8, 1, 1)
        self.a_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.a_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.a_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.a_interrupter.setFont(font)
        self.a_interrupter.setObjectName("a_interrupter")
        self.interrupter.addWidget(self.a_interrupter, 2, 5, 1, 1)
        self.y_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.y_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.y_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.y_interrupter.setFont(font)
        self.y_interrupter.setObjectName("y_interrupter")
        self.interrupter.addWidget(self.y_interrupter, 2, 7, 1, 1)
        self.t_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.t_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.t_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.t_interrupter.setFont(font)
        self.t_interrupter.setObjectName("t_interrupter")
        self.interrupter.addWidget(self.t_interrupter, 1, 7, 1, 1)
        self.io_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.io_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.io_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.io_interrupter.setFont(font)
        self.io_interrupter.setObjectName("io_interrupter")
        self.interrupter.addWidget(self.io_interrupter, 2, 8, 1, 1)
        self.c_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.c_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.c_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.c_interrupter.setFont(font)
        self.c_interrupter.setObjectName("c_interrupter")
        self.interrupter.addWidget(self.c_interrupter, 0, 6, 1, 1)
        self.f_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.f_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.f_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.f_interrupter.setFont(font)
        self.f_interrupter.setObjectName("f_interrupter")
        self.interrupter.addWidget(self.f_interrupter, 0, 1, 1, 1)
        self.p_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.p_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.p_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.p_interrupter.setFont(font)
        self.p_interrupter.setObjectName("p_interrupter")
        self.interrupter.addWidget(self.p_interrupter, 1, 4, 1, 1)
        self.ae_interrupter = QtWidgets.QCheckBox(self.interrupterGroupBox)
        self.ae_interrupter.setMinimumSize(QtCore.QSize(30, 0))
        self.ae_interrupter.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ae_interrupter.setFont(font)
        self.ae_interrupter.setObjectName("ae_interrupter")
        self.interrupter.addWidget(self.ae_interrupter, 2, 6, 1, 1)
        self.verticalLayout_3.addWidget(self.interrupterGroupBox)
        self.tabWidget.addTab(self.options_tab, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        mainView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        mainView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainView)
        self.statusbar.setObjectName("statusbar")
        mainView.setStatusBar(self.statusbar)

        self.retranslateUi(mainView)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(mainView)

    def retranslateUi(self, mainView):
        _translate = QtCore.QCoreApplication.translate
        mainView.setWindowTitle(_translate("mainView", "MainWindow"))
        self.run_decryption_button.setText(_translate("mainView", "Run Decryption"))
        self.enc_method_name_2.setText(_translate("mainView", "Encryption"))
        self.number_of_keys.setText(_translate("mainView", "Number of Keys"))
        self.interrupters_2.setText(_translate("mainView", "Interrupters"))
        self.interrupters.setText(_translate("mainView", "Interrupters"))
        self.cipherTextPad_2.setText(_translate("mainView", "Estimated Time (minutes)"))
        self.cipher_text_set.setText(_translate("mainView", "Cipher Text"))
        self.cipher_text_set_2.setText(_translate("mainView", "Cipher Text"))
        self.estimated_time_2.setText(_translate("mainView", "Estimated Time (minutes)"))
        self.enc_method_name.setText(_translate("mainView", "Encryption"))
        self.estimated_combinations.setText(_translate("mainView", "Estimated Combinations"))
        self.gematria_rotations.setText(_translate("mainView", "Gematria Rotation"))
        self.estimated_combinations_2.setText(_translate("mainView", "Estimated Combinations"))
        self.number_of_keys_2.setText(_translate("mainView", "Number of Keys"))
        self.gematria_rotations_2.setText(_translate("mainView", "CT Gematria Rotation"))
        self.gematria_rotations_3.setText(_translate("mainView", "Key Gematria Rotation"))
        self.key_gematria_rotations.setText(_translate("mainView", "Gematria Rotation"))
        self.set_default_button.setText(_translate("mainView", "Set Default"))
        self.save_setup_button.setText(_translate("mainView", "Save Setup"))
        self.load_setup_button.setText(_translate("mainView", "Load Setup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ciphertext_2), _translate("mainView", "Tab 1"))
        self.groupBox_2.setTitle(_translate("mainView", "Test Key Setup"))
        self.label.setText(_translate("mainView", "Enter test key as runes, english or comma seperated forward position.\n"
"Choose Gematria order and shift (rotation) for encoding"))
        self.test_key_entry.setToolTip(_translate("mainView", "<html><head/><body><p>Enter test key to use here</p></body></html>"))
        self.test_key_entry.setText(_translate("mainView", "intelligence"))
        self.label_31.setText(_translate("mainView", "Gematria Order"))
        self.test_key_gem_order.setItemText(0, _translate("mainView", "Forward"))
        self.test_key_gem_order.setItemText(1, _translate("mainView", "Reverse"))
        self.label_30.setText(_translate("mainView", "Gematria Shift"))
        self.key_display_format_box_2.setTitle(_translate("mainView", "Display Format For Test Key"))
        self.test_key_runes_radio.setText(_translate("mainView", "Runes"))
        self.test_key_runes_eng_radio.setText(_translate("mainView", "Runes (Eng)"))
        self.test_key_prime_radio.setText(_translate("mainView", "Prime"))
        self.test_key_forward_position_radio.setText(_translate("mainView", "Forward Position"))
        self.test_key_reverse_position_radio.setText(_translate("mainView", "Reverse Position"))
        self.test_key_out.setText(_translate("mainView", "intelligence"))
        self.groupBox_3.setTitle(_translate("mainView", "Test Plaintext Setup"))
        self.label_8.setText(_translate("mainView", "Enter test plaintext as runes, english or comma seperated forward position.\n"
"Choose Gematria order and (shift) rotation for encoding"))
        self.test_plaintext_entry.setText(_translate("mainView", "for all that lives is holy"))
        self.label_32.setText(_translate("mainView", "Gematria Order"))
        self.test_plaintext_gem_order.setItemText(0, _translate("mainView", "Forward"))
        self.test_plaintext_gem_order.setItemText(1, _translate("mainView", "Reverse"))
        self.label_33.setText(_translate("mainView", "Gematria Shift"))
        self.test_pt_display_format_box.setTitle(_translate("mainView", "Display Format For Plaintext"))
        self.test_pt_runes_radio.setText(_translate("mainView", "Runes"))
        self.test_pt_runes_eng_radio.setText(_translate("mainView", "Runes (Eng)"))
        self.test_pt_prime_radio.setText(_translate("mainView", "Prime"))
        self.test_pt_forward_position_radio.setText(_translate("mainView", "Forward Position"))
        self.test_pt_reverse_position_radio.setText(_translate("mainView", "Reverse Position"))
        self.test_plain_text_runes.setText(_translate("mainView", "for all that lives is holy"))
        self.groupBox_4.setTitle(_translate("mainView", "Encryption"))
        self.test_enc_method_2.setText(_translate("mainView", "Encryption Method:"))
        self.test_enc_method.setText(_translate("mainView", "Encryption Method:"))
        self.label_28.setText(_translate("mainView", "Key Start Index:"))
        self.label_27.setText(_translate("mainView", "Interrupter:"))
        self.label_23.setText(_translate("mainView", "Cipher Text in Runes (Eng), Runes, Rune Primes, Forward pos, Reverse pos:"))
        self.test_decrypt.setText(_translate("mainView", "Test Decryption"))
        self.cancel_test_decrypt.setText(_translate("mainView", "Cancel Text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainView", "Test"))
        self.test_enc_method_7.setText(_translate("mainView", "Encryption Method:"))
        self.test_enc_method_8.setText(_translate("mainView", "Encryption Method:"))
        self.copy_results_to_file.setText(_translate("mainView", "Copy results"))
        self.save_results_to_file.setText(_translate("mainView", "Save Results"))
        self.pop_results_to_windows.setText(_translate("mainView", "Pop Results"))
        __sortingEnabled = self.results_table.isSortingEnabled()
        self.results_table.setSortingEnabled(False)
        self.results_table.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), _translate("mainView", "Results"))
        self.lpSectionBox.setTitle(_translate("mainView", "Choose LP section (defined by Red Rune Sections / Side Art)"))
        self.lp_section1.setText(_translate("mainView", "1"))
        self.lp_section2.setText(_translate("mainView", "2"))
        self.lp_section3.setText(_translate("mainView", "3"))
        self.lp_section4.setText(_translate("mainView", "4"))
        self.lp_section5.setText(_translate("mainView", "5"))
        self.lp_section6.setText(_translate("mainView", "6"))
        self.lp_section7.setText(_translate("mainView", "7"))
        self.lp_section8.setText(_translate("mainView", "8"))
        self.lp_section9.setText(_translate("mainView", "9"))
        self.lp_section10.setText(_translate("mainView", "10"))
        self.lp_section11.setText(_translate("mainView", " 11"))
        self.lp_section12.setText(_translate("mainView", "12"))
        self.lp_section13.setText(_translate("mainView", "13"))
        self.lpWordSelection.setTitle(_translate("mainView", "For each section, choose which words to include"))
        self.startWords.setText(_translate("mainView", "Start"))
        self.endWords.setText(_translate("mainView", "End"))
        self.startAndEndWords.setText(_translate("mainView", "Start and End"))
        self.allWords.setText(_translate("mainView", "All"))
        self.lpRedRunesBox.setTitle(_translate("mainView", "Add Red Rune Cipher Text From Unsolved Pages"))
        self.rr_7.setText(_translate("mainView", "7"))
        self.rr_1.setText(_translate("mainView", "1"))
        self.rr_3.setText(_translate("mainView", "3"))
        self.rr_8.setText(_translate("mainView", "8"))
        self.rr_2.setText(_translate("mainView", "2"))
        self.rr_6.setText(_translate("mainView", "6"))
        self.rr_5.setText(_translate("mainView", "5"))
        self.rr_4.setText(_translate("mainView", "4"))
        self.rr_9.setText(_translate("mainView", "9"))
        self.rr_10.setText(_translate("mainView", "10"))
        self.rr_11.setText(_translate("mainView", " 11"))
        self.rr_12.setText(_translate("mainView", "12"))
        self.rr_13.setText(_translate("mainView", "13"))
        self.rr_14.setText(_translate("mainView", "14"))
        self.rr_15.setText(_translate("mainView", "15"))
        self.rr_16.setText(_translate("mainView", "16"))
        self.ct_display_format_box.setTitle(_translate("mainView", "Display Format For Chosen Cipher-Text"))
        self.ct_runes_radio.setText(_translate("mainView", "Runes"))
        self.ct_runes_eng_radio.setText(_translate("mainView", "Runes (Eng)"))
        self.ct_prime_radio.setText(_translate("mainView", "Prime"))
        self.ct_forward_position_radio.setText(_translate("mainView", "Forward Position"))
        self.ct_reverse_position_radio.setText(_translate("mainView", "Reverse Position"))
        self.ct_display_box.setTitle(_translate("mainView", "Chosen Cipher-Text"))
        self.cipherTextPad.setHtml(_translate("mainView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.groupBox_5.setTitle(_translate("mainView", "Cipher-Text Order (rune indexes are given in Top-To-Bottom Left-To-Right)"))
        self.tb_lr_ciphertext_order.setText(_translate("mainView", "Top-Bottom, Left-Right"))
        self.bt_rl_ciphertext_order.setText(_translate("mainView", "Bottom-Top, Right-Left"))
        self.custom_ciphertext_order.setText(_translate("mainView", "Custum"))
        self.cipherTextOrderTextPad.setHtml(_translate("mainView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ciphertext_tab), _translate("mainView", "Cipher Text"))
        self.key_display_format_box.setTitle(_translate("mainView", "Display Format For Processed Keys"))
        self.key_runes_radio.setText(_translate("mainView", "Runes"))
        self.key_runes_eng_radio.setText(_translate("mainView", "Runes (Eng)"))
        self.key_prime_radio.setText(_translate("mainView", "Prime"))
        self.key_forward_position_radio.setText(_translate("mainView", "Forward Position"))
        self.key_reverse_position_radio.setText(_translate("mainView", "Reverse Position"))
        self.rune_key_sample_4.setText(_translate("mainView", "Comma Separated \n"
"Forward Posiiton Numbers\n"
"New line separates keys"))
        self.rune_key_sample_5.setText(_translate("mainView", "   Key Format  "))
        self.rune_key_sample.setText(_translate("mainView", "ᛈᚪᚱᚪᛒᛚᛖ,ᛚᛁᚳᛖ ᚦᛖ ᛁᚾᛋᛏᚪᚱ,ᛏᚢᚾᚾᛖᛚᛝ ᛏᚩ ᚦᛖ,\n"
"ᛋᚢᚱᚠᚪᚳᛖ ᚹᛖ ᛗᚢᛋᛏ,ᛋᚻᛖᛞ ᚩᚢᚱ ᚩᚹᚾ,\n"
"ᚳᛁᚱᚳᚢᛗᚠᛖᚱᛖᚾᚳᛖᛋ,ᚠᛁᚾᛞ ᚦᛖ ᛞᛁᚢᛁᚾᛁᛏᚣ,\n"
"ᚹᛁᚦᛁᚾ ᚪᚾᛞ ᛖᛗᛖᚱᚷᛖ"))
        self.rune_key_sample_6.setText(_translate("mainView", "Example                   "))
        self.key_entry_textedit.setHtml(_translate("mainView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Parable,Like the instar,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">tunneling to the,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">surface We must,shed our own,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">circumferences,Find the divinity, </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">within and emerge</span></p></body></html>"))
        self.label_6.setText(_translate("mainView", "Processed keys"))
        self.key_count_label.setText(_translate("mainView", "0 Keys"))
        self.number_key_sample.setText(_translate("mainView", "1,2,3,4,5,7,8,9\n"
"2,3,5,7,11,13,17\n"
"0,1,1,2,3,5,8,13"))
        self.rune_key_sample_2.setText(_translate("mainView", "Comma Separated Runes"))
        self.english_key_sample.setText(_translate("mainView", "Parable,Like the instar,\n"
"tunneling to the,\n"
"surface We must,shed our own,\n"
"circumferences,Find the divinity, \n"
"within and emerge"))
        self.rune_key_sample_3.setText(_translate("mainView", "Comma Separated English"))
        self.save_key_file_button.setText(_translate("mainView", "Save Entry"))
        self.label_5.setText(_translate("mainView", "Type, paste or load keys\n"
"(format options below)"))
        self.load_key_file_button.setText(_translate("mainView", "Load File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Keys_Tab), _translate("mainView", "Keys"))
        self.label_72.setText(_translate("mainView", "3 Ways to Define the Encryption Method"))
        self.pre_computed_encryption_map_load.setText(_translate("mainView", "Load New Data "))
        self.label_74.setText(_translate("mainView", "Encryption Formula "))
        self.label_108.setText(_translate("mainView", "Define function of p (plaintext) and k (key), using Python\'s \'eval\' method\n"
"https://docs.python.org/3/library/functions.html"))
        self.enc_method_function_textbox.setText(_translate("mainView", "p + k"))
        self.label_122.setText(_translate("mainView", "Examples: "))
        self.label_110.setText(_translate("mainView", "plus: p + k"))
        self.label_2.setText(_translate("mainView", "xor: p ^ k"))
        self.label_111.setText(_translate("mainView", "multiply: p * k"))
        self.label_117.setText(_translate("mainView", "Method Name:"))
        self.enc_method_name_textbox.setText(_translate("mainView", "plus"))
        self.label_119.setText(_translate("mainView", "Encryption Table"))
        self.label_118.setText(_translate("mainView", "Processed Results"))
        __sortingEnabled = self.encryption_table.isSortingEnabled()
        self.encryption_table.setSortingEnabled(False)
        self.encryption_table.setSortingEnabled(__sortingEnabled)
        self.label_120.setText(_translate("mainView", "Decryption Table"))
        self.label_104.setText(_translate("mainView", "Table with\n"
"PT Key Cipher"))
        __sortingEnabled = self.decryption_table.isSortingEnabled()
        self.decryption_table.setSortingEnabled(False)
        self.decryption_table.setSortingEnabled(__sortingEnabled)
        self.encryption_map_text_entry.setHtml(_translate("mainView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">plus</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 0 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 1 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 2 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 3 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 4 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 5 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 6 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 7 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 8 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 9 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 10 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 11 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 12 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 13 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 14 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 15 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 16 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 17 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 18 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 19 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 20 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 21 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 22 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 23 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 24 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 25 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 26 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 27 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0 28 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 0 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 1 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 3 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 4 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 5 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 6 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 7 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 8 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 9 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 10 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 11 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 12 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 13 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 14 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 15 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 16 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 17 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 18 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 19 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 20 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 21 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 22 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 23 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 24 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 25 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 26 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 27 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 28 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 0 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 1 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 2 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 3 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 4 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 5 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 6 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 7 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 8 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 9 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 10 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 11 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 12 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 13 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 14 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 15 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 16 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 17 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 18 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 19 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 20 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 21 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 22 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 23 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 24 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 25 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 26 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 27 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 28 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 0 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 1 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 2 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 3 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 4 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 5 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 6 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 7 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 8 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 9 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 10 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 11 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 12 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 13 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 14 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 15 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 16 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 17 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 18 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 19 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 20 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 21 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 22 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 23 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 24 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 25 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 26 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 27 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 28 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 0 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 1 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 2 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 3 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 4 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 5 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 6 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 7 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 8 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 9 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 10 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 11 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 12 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 13 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 14 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 15 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 16 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 17 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 18 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 19 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 20 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 21 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 22 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 23 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 24 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 25 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 26 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 27 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 28 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 0 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 1 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 2 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 3 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 4 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 5 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 6 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 7 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 8 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 9 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 10 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 11 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 12 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 13 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 14 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 15 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 16 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 17 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 18 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 19 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 20 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 21 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 22 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 23 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 24 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 25 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 26 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 27 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 28 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 0 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 1 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 2 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 3 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 4 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 5 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 6 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 7 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 8 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 9 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 10 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 11 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 12 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 13 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 14 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 15 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 16 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 17 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 18 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 19 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 20 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 21 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 22 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 23 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 24 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 25 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 26 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 27 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6 28 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 0 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 1 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 2 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 3 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 4 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 5 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 6 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 7 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 8 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 9 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 10 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 11 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 12 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 13 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 14 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 15 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 16 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 17 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 18 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 19 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 20 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 21 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 22 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 23 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 24 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 25 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 26 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 27 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7 28 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 0 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 1 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 2 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 3 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 4 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 5 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 6 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 7 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 8 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 9 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 10 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 11 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 12 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 13 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 14 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 15 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 16 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 17 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 18 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 19 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 20 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 21 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 22 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 23 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 24 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 25 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 26 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 27 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8 28 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 0 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 1 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 2 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 3 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 4 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 5 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 6 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 7 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 8 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 9 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 10 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 11 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 12 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 13 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 14 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 15 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 16 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 17 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 18 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 19 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 20 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 21 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 22 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 23 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 24 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 25 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 26 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 27 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9 28 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 0 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 1 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 2 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 3 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 4 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 5 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 6 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 7 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 8 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 9 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 10 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 11 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 12 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 13 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 14 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 15 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 16 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 17 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 18 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 19 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 20 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 21 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 22 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 23 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 24 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 25 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 26 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 27 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 28 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 0 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 1 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 2 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 3 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 4 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 5 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 6 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 7 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 8 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 9 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 10 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 11 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 12 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 13 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 14 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 15 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 16 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 17 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 18 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 19 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 20 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 21 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 22 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 23 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 24 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 25 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 26 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 27 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 28 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 0 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 1 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 2 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 3 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 4 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 5 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 6 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 7 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 8 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 9 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 10 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 11 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 12 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 13 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 14 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 15 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 16 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 17 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 18 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 19 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 20 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 21 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 22 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 23 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 24 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 25 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 26 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 27 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12 28 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 0 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 1 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 2 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 3 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 4 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 5 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 6 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 7 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 8 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 9 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 10 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 11 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 12 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 13 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 14 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 15 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 16 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 17 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 18 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 19 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 20 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 21 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 22 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 23 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 24 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 25 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 26 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 27 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13 28 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 0 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 1 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 2 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 3 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 4 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 5 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 6 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 7 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 8 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 9 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 10 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 11 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 12 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 13 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 14 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 15 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 16 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 17 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 18 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 19 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 20 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 21 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 22 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 23 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 24 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 25 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 26 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 27 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14 28 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 0 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 1 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 2 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 3 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 4 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 5 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 6 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 7 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 8 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 9 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 10 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 11 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 12 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 13 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 14 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 15 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 16 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 17 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 18 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 19 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 20 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 21 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 22 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 23 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 24 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 25 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 26 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 27 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 28 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 0 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 1 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 2 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 3 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 4 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 5 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 6 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 7 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 8 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 9 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 10 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 11 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 12 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 13 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 14 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 15 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 16 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 17 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 18 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 19 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 20 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 21 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 22 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 23 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 24 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 25 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 26 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 27 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">16 28 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 0 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 1 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 2 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 3 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 4 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 5 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 6 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 7 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 8 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 9 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 10 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 11 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 12 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 13 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 14 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 15 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 16 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 17 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 18 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 19 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 20 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 21 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 22 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 23 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 24 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 25 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 26 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 27 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">17 28 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 0 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 1 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 2 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 3 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 4 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 5 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 6 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 7 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 8 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 9 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 10 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 11 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 12 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 13 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 14 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 15 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 16 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 17 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 18 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 19 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 20 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 21 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 22 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 23 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 24 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 25 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 26 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 27 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">18 28 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 0 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 1 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 2 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 3 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 4 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 5 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 6 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 7 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 8 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 9 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 10 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 11 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 12 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 13 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 14 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 15 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 16 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 17 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 18 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 19 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 20 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 21 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 22 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 23 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 24 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 25 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 26 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 27 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">19 28 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 0 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 1 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 2 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 3 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 4 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 5 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 6 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 7 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 8 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 9 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 10 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 11 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 12 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 13 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 14 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 15 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 16 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 17 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 18 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 19 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 20 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 21 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 22 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 23 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 24 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 25 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 26 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 27 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 28 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 0 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 1 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 2 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 3 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 4 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 5 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 6 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 7 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 8 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 9 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 10 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 11 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 12 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 13 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 14 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 15 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 16 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 17 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 18 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 19 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 20 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 21 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 22 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 23 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 24 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 25 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 26 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 27 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">21 28 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 0 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 1 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 2 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 3 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 4 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 5 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 6 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 7 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 8 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 9 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 10 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 11 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 12 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 13 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 14 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 15 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 16 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 17 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 18 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 19 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 20 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 21 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 22 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 23 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 24 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 25 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 26 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 27 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">22 28 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 0 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 1 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 2 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 3 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 4 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 5 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 6 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 7 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 8 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 9 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 10 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 11 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 12 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 13 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 14 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 15 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 16 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 17 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 18 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 19 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 20 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 21 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 22 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 23 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 24 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 25 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 26 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 27 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">23 28 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 0 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 1 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 2 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 3 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 4 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 5 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 6 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 7 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 8 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 9 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 10 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 11 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 12 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 13 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 14 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 15 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 16 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 17 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 18 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 19 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 20 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 21 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 22 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 23 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 24 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 25 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 26 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 27 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24 28 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 0 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 1 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 2 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 3 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 4 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 5 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 6 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 7 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 8 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 9 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 10 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 11 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 12 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 13 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 14 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 15 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 16 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 17 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 18 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 19 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 20 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 21 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 22 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 23 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 24 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 25 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 26 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 27 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25 28 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 0 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 1 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 2 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 3 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 4 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 5 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 6 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 7 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 8 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 9 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 10 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 11 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 12 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 13 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 14 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 15 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 16 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 17 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 18 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 19 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 20 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 21 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 22 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 23 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 24 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 25 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 26 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 27 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">26 28 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 0 27</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 1 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 2 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 3 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 4 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 5 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 6 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 7 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 8 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 9 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 10 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 11 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 12 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 13 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 14 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 15 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 16 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 17 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 18 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 19 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 20 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 21 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 22 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 23 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 24 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 25 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 26 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 27 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">27 28 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 0 28</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 1 0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 2 1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 3 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 4 3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 5 4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 6 5</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 7 6</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 8 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 9 8</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 10 9</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 11 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 12 11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 13 12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 14 13</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 15 14</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 16 15</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 17 16</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 18 17</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 19 18</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 20 19</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 21 20</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 22 21</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 23 22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 24 23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 25 24</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 26 25</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 27 26</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28 28 27</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encryption_tab4), _translate("mainView", "Encryption"))
        self.groupBox.setToolTip(_translate("mainView", "<html><head/><body><p>Entre numbers to set the 4-gram score </p><p>cuts. Lower numbers cut more data but </p><p>give less output to check</p></body></html>"))
        self.groupBox.setTitle(_translate("mainView", "4-gram probablity settings"))
        self.test_enc_method_17.setText(_translate("mainView", "Min Score Gradient/4-gram"))
        self.test_enc_method_4.setText(_translate("mainView", "Count Cut"))
        self.checkBox_2.setText(_translate("mainView", "Set nominal values "))
        self.log_prob_min_lab.setText(_translate("mainView", "Min Score"))
        self.test_enc_method_18.setText(_translate("mainView", "Min Score Offset/4-gram"))
        self.groupBox_6.setTitle(_translate("mainView", "Options When Scoring "))
        self.test_enc_method_13.setText(_translate("mainView", "Undefined gives any answer"))
        self.test_enc_method_16.setText(_translate("mainView", "Score Reversed Decryption"))
        self.test_enc_method_14.setText(_translate("mainView", "Use Reverse Keys as well"))
        self.test_enc_method_6.setText(_translate("mainView", "Save Rejected (!!RAM hungry!!)"))
        self.label_24.setText(_translate("mainView", "Max zero count 4-grams"))
        self.test_enc_method_23.setText(_translate("mainView", "Wrap Key around Cipher Text"))
        self.groupBox_7.setTitle(_translate("mainView", "Allowed Char Differences from Cribs for Decrypted Words "))
        self.test_enc_method_22.setText(_translate("mainView", "9 Rune Words"))
        self.test_enc_method_9.setText(_translate("mainView", "2 Rune Words"))
        self.test_enc_method_11.setText(_translate("mainView", "4 Rune Words"))
        self.test_enc_method_21.setText(_translate("mainView", "8 Rune Words"))
        self.test_enc_method_10.setText(_translate("mainView", "3 Rune Words"))
        self.test_enc_method_15.setText(_translate("mainView", "6 Rune Words"))
        self.test_enc_method_25.setText(_translate("mainView", "11 Rune Words"))
        self.test_enc_method_20.setText(_translate("mainView", "7 Rune Words"))
        self.test_enc_method_24.setText(_translate("mainView", "10 Rune Words"))
        self.checkBox.setText(_translate("mainView", "Set maximim values (turns this ranking off, increases output)"))
        self.test_enc_method_19.setText(_translate("mainView", "1 Rune Words"))
        self.test_enc_method_12.setText(_translate("mainView", "5 Rune Words"))
        self.test_enc_method_26.setText(_translate("mainView", "12 Rune Words"))
        self.test_enc_method_27.setText(_translate("mainView", "13 Rune Words"))
        self.test_enc_method_28.setText(_translate("mainView", "14 Rune Words"))
        self.ct_shift_groupbox.setTitle(_translate("mainView", "Gematria Order/Shifts For Cipher-Text When Decyrpting"))
        self.ct_forward_gematria.setText(_translate("mainView", "Forward"))
        self.ct_reverse_gematria.setText(_translate("mainView", "Reverse"))
        self.ct_all_forward_gematria.setText(_translate("mainView", "All Forward"))
        self.ct_all_reverse_gematria.setText(_translate("mainView", "All Reverse"))
        self.ct_all_gematria.setText(_translate("mainView", "All"))
        self.key_shift_groupbox.setTitle(_translate("mainView", "Gematria Order/Shifts For Keys When Decyrpting"))
        self.key_forward_gematria.setText(_translate("mainView", "Forward"))
        self.key_reverse_gematria.setText(_translate("mainView", "Reverse"))
        self.key_all_forward_gematria.setText(_translate("mainView", "All Forward"))
        self.key_all_reverse_gematria.setText(_translate("mainView", "All Reverse"))
        self.key_all_gematria.setText(_translate("mainView", "All"))
        self.interrupterGroupBox.setTitle(_translate("mainView", "Choose Possible Interrupter Runes"))
        self.m_interrupter.setText(_translate("mainView", "ᛗ"))
        self.ing_interrupter.setText(_translate("mainView", "ᛝ"))
        self.s_interrupter.setText(_translate("mainView", "ᛋ"))
        self.ea_interrupter.setText(_translate("mainView", "ᛠ"))
        self.j_interrupter.setText(_translate("mainView", "ᛂ"))
        self.e_interrupter.setText(_translate("mainView", "ᛖ"))
        self.n_interrupter.setText(_translate("mainView", "ᚾ"))
        self.r_interrupter.setText(_translate("mainView", "ᚱ"))
        self.u_interrupter.setText(_translate("mainView", "ᚢ"))
        self.i_interrupter.setText(_translate("mainView", "ᛁ"))
        self.all_interrupters.setText(_translate("mainView", "All"))
        self.d_interrupter.setText(_translate("mainView", "ᛞ"))
        self.g_interrupter.setText(_translate("mainView", "ᚷ"))
        self.eo_interrupter.setText(_translate("mainView", "ᛇ"))
        self.l_interrupter.setText(_translate("mainView", "ᛚ"))
        self.x_interrupter.setText(_translate("mainView", "ᛉ"))
        self.h_interrupter.setText(_translate("mainView", "ᚻ"))
        self.oe_interrupter.setText(_translate("mainView", "ᛟ"))
        self.th_interrupter.setText(_translate("mainView", "ᚦ"))
        self.w_interrupter.setText(_translate("mainView", "ᚹ"))
        self.o_interrupter.setText(_translate("mainView", "ᚩ"))
        self.b_interrupter.setText(_translate("mainView", "ᛒ"))
        self.a_interrupter.setText(_translate("mainView", "ᚪ"))
        self.y_interrupter.setText(_translate("mainView", "ᚣ"))
        self.t_interrupter.setText(_translate("mainView", "ᛏ"))
        self.io_interrupter.setText(_translate("mainView", "ᛡ"))
        self.c_interrupter.setText(_translate("mainView", "ᚳ"))
        self.f_interrupter.setText(_translate("mainView", "ᚠ"))
        self.p_interrupter.setText(_translate("mainView", "ᛈ"))
        self.ae_interrupter.setText(_translate("mainView", "ᚫ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.options_tab), _translate("mainView", "Options"))
from QTableWidgetOverload import QTableWidgetOverload
from QTextEditOverload import QTextEditOverload
