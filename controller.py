from view.gui import view
from enc.DecryptModel import DecryptModel
from enc.DecryptModel import DecryptionSetup
from enc.gematria import gematria
from PyQt5.QtCore import QTimer, QThreadPool
from PyQt5.QtWidgets import QApplication
from data.data import data
from PyQt5.QtCore import *  # meh
from Workers import WorkerSignals
from Workers import Worker


# TODO atm encryption/decryption maps are done in the gui, it needs to move out of there
# from enc.encryption_maps import encryption


class controller(object):
    '''
        Holds all the main objects,
        data:
            the main dictionary with values used throughout the app
        gui (view):
            set options and data (cipher text, keys, decryption / encryption maps
        crypt_model:
            handles decrypting and scoring
        worker signals:
            for communication from the decrypting thread
        gem:
            gematria object for encoding and text conversion to runes

    TODO atm encryption/decryption maps are done in the gui, it needs to move out of there

    '''

    def __init__(self, argv):
        self.argv = argv
        ''' standard data object '''
        self.data_obj = data()
        self.data = self.data_obj.data
        ''' DecryptModel handles decrypting, all data must be passed in '''
        self.crypt_model = DecryptModel()
        ''' signals from workers to pass back progress '''
        self.crypt_model.decrypt_finished.connect(self.handle_decrypt_finished)
        self.crypt_model.decrypt_progress.connect(self.handle_decrypt_progress)
        ''' decrypting takes place in a worker object in a qthread, '''
        # TODO multi-threading isn't actually used, data is too messy atm,
        self.signals = WorkerSignals()
        ''' gematria object '''
        self.gem = gematria()
        # TODO atm encryption is done in the gui, it needs to move out of there
        # self.encryptor = encryption()
        # TODO much work happens in the gui, which should probably move out to here and other
        #  objects
        self.gui = view()
        self.gui.show()
        self.gui.run_decryption_button.clicked.connect(self.handle_main_run)
        self.gui.test_decrypt.clicked.connect(self.handle_test_run)
        self.gui.cancel_test_decrypt.clicked.connect(self.handle_cancelTestDecrypt)
        # this doesn't do much atm, but in the future can add in mutiple threads
        self.threadpool = QThreadPool()
        # print(__name__," Multithreading with maximum %d threads" %
        # self.threadpool.maxThreadCount())
        ''' used to update the gui while decrypting '''
        # todo, yeah, so, then, do the gui updating sometime? yawn still waiting
        self.widgetUpdateTimer = QTimer()
        self.widgetTimerUpdateTime_ms = 1000
        self.widgetUpdateTimer.timeout.connect(self.guiUpdate)
        ''' passed arg to run test on start-up  '''
        if "-test" in argv:
            self.handle_test_run()

    def handle_cancelTestDecrypt(self):
        '''
            called when the cancel test decrypt button is clicked
            TODO: implement thread cancelling
        '''
        self.data["cancel_thread"] = True
        print(__name__, "how to cancel a thread?")

    def handle_decrypt_progress(self):
        '''
            worker signal
            todo will update gui with time counters and time estimates
        '''
        print(__name__, "handle_decrypt_progress")
        print(__name__, "DecryptModel emitted decrypt_progress signal??")

    def handle_decrypt_finished(self):
        '''
            worker signal
            todo print answers, clean up gui, reset objects, etc.
        '''
        print(__name__, "handle_decrypt_finished")
        self.widgetUpdateTimer.stop()
        if len(self.data["answers"]) > 0:
            self.gui.pop_results()

    def handle_test_run(self):
        '''
            sets up the data for the decryption run  main_loop, data is the main decrypting data,
            using key and cipher text from test tab. Then runs main_loop in a Qthread (or
            something close to that) data is converted to "nominal units", keys in eng, or runes, or position etc
        '''
        print(__name__, " handle_test_run")
        dec_setup = self.set_up_decryption(self.data["test_key_eng"], self.data["test_ct"],
                                           self.data["test_pt_word_Length"])
        self.run_main_loops(dec_setup)

    def handle_main_run(self):
        '''
            sets up the data for the decryption run  main_loop, data is the main decrypting data,
            using key and cipher text definied in key adn cipher rtext tabs. Then
            runs main_loop in a 'Qthread' data is converted to "nominal units", keys in eng,
            or runes, or position etc
        '''
        print(__name__, " handle_main_rune")
        dec_setup = self.set_up_decryption(self.data["keys"], self.data["cipher_text"],
                                           self.data["cipher_text_lengths"])
        # start timer for 200 ms
        self.run_main_loops(dec_setup)

    def set_up_decryption(self, key_eng, ct, ct_rune_word_len):
        '''
             sets up the data for the decryption run  main_loop, data is the main decyrpting data,
             using key and cipher text from test tab. Then runs main_loop in a Qthread
             data is converted to "nominal units", keys in eng, or runes, or position etc
             to "drag" the key over each possible ct, we rotate it using rightRotate
         '''
        print("\nSET_UP_DECRYPTION")
        '''  keys in latin runes normal Gematria '''
        key_lengths = []
        for key in key_eng:
            key_lengths.append(len(key))
        print("key_eng = ", key_eng)
        print("key_lengths = ", key_lengths)
        '''  get the list of rune words,  parse each ct into lists of ct characters, lengths of 
        ct, and each possible rotation index '''
        ct_rune_chars = []
        ct_lengths = []
        ct_rot = []
        for item in ct:
            ct_rune_chars.append(self.flatten(item))
            ct_lengths.append(len(ct_rune_chars[-1]))
            ct_rot.append(list(range(0, ct_lengths[-1])))

        # TODD some of these should be calculated in the decrypert
        print("keys_runeglish = ", key_eng)
        print("key_lengths = ", key_lengths)
        print("ct_rune_words = ", ct)
        print("ct_rune_chars = ", ct_rune_chars)
        print("ct_lengths = ", ct_lengths)
        print("ct_rot = ", ct_rot)
        print("ct_rune_word_len = ", ct_rune_word_len)
        print("dec_map = ", self.data["dec_map"])
        print("interrupters = ", self.data["chosen_interrupters"])
        #print("interrupters_p = ", self.gem.runes_to_pos(self.data["chosen_interrupters"]))
        print("interrupters_p = ", self.gem.encode_as_position(self.data["chosen_interrupters"],
                                                               'forward',0))
        print("use_gematria_forward = ", self.data["ct_use_gematria_forward"])
        print("use_gematria_reverse = ", self.data["ct_use_gematria_reverse"])
        print("gematria_forward_shifts = ", self.data["ct_gematria_forward_shifts"])
        print("gematria_reverse_shifts = ", self.data["ct_gematria_reverse_shifts"])

        dec_setup = DecryptionSetup(keys_runeglish=key_eng, key_lengths=key_lengths,
                                    ct_rune_words=ct, ct_rune_chars=ct_rune_chars,
                                    ct_lengths=ct_lengths, ct_rot=ct_rot,
                                    ct_rune_word_len=ct_rune_word_len, dec_map=self.data["dec_map"],
                                    interrupters=self.data["chosen_interrupters"],
                                    interrupters_p=self.gem.encode_as_position(
                                        self.data["chosen_interrupters"],'forward',0),
                                    ct_use_gematria_forward=self.data["ct_use_gematria_forward"],
                                    ct_use_gematria_reverse=self.data["ct_use_gematria_reverse"],
                                    ct_gematria_forward_shifts=self.data[
                                        "ct_gematria_forward_shifts"],
                                    ct_gematria_reverse_shifts=self.data[
                                        "ct_gematria_reverse_shifts"],
                                    key_use_gematria_forward=self.data["key_use_gematria_forward"],
                                    key_use_gematria_reverse=self.data["key_use_gematria_reverse"],
                                    key_gematria_forward_shifts=self.data[
                                        "key_gematria_forward_shifts"],
                                    key_gematria_reverse_shifts=self.data[
                                        "key_gematria_reverse_shifts"],
                                    undefined_answers_are_all=self.data[
                                        "undefined_answers_are_all"],
                                    use_reverse_keys=self.data["use_reverse_keys"],
                                    wrap_key_around_ct=self.data["wrap_key_around_ct"],
                                    score_reversed_decryption=self.data["score_reversed_decryption"]

                                    )
        return dec_setup

    def run_main_loops(self, dec_setup):
        '''
            called by test_run or main_run, creates a thread, connects signals, and starts worker
            create QRunnable "worker" object, pass in required data,
            then run it in out thread pool taking up 1 threads to start,
            TODO figure out the threads, data separation, etc ... ??
        '''
        '''  Pass the function to execute '''
        worker = Worker(
            self.crypt_model.main_loop_rune)  # Any other args, kwargs are passed to the run
        ''' sketchy, this is how data is passed to the thread, tbh, meh '''
        worker.kwargs["dec_data"] = dec_setup
        # worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.thread_progress)
        self.widgetUpdateTimer.start(self.widgetTimerUpdateTime_ms)
        self.threadpool.start(worker)
        print("run_main_loops fin")

    def thread_progress(self, val):
        print(__name__, "thread_progress!")
        self.crypt_model.decrypt_progress.emit()
        print(__name__, "DecryptModel emitted decrypt_progress signal??")

    def thread_complete(self):
        print(__name__, "DecryptModel THREAD COMPLETE!")
        self.crypt_model.decrypt_finished.emit()
        print(__name__, "DecryptModel emitted decrypt_finished signal??")

    def flatten(self, li):
        return sum(([x] if not isinstance(x, list) else self.flatten(x) for x in li), [])

    def guiUpdate(self):
        # check what data has changed since last call
        # print("guiUpdate")
        QApplication.processEvents()
        # TODO need to get data from crypt_model to the gui
