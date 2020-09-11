#!/usr/bin/env python3
'''
/*

---------------------------------------------------------------------------
    lp-decrypter
    Main file to run
---------------------------------------------------------------------------

    Author: mortlach
    Started: April 2020


*/
'''
''' for convenience add some directories to path '''
import os
import sys

''' cheat, add som paths '''
sys.path.append(os.path.join(sys.path[0], 'text_ranking'))
sys.path.append(os.path.join(sys.path[0], 'view'))
sys.path.append(os.path.join(sys.path[0], 'enc'))
sys.path.append(os.path.join(sys.path[0], 'data'))
sys.path.append(os.path.join(sys.path[0]))
''' QApplication is the top-level class we create, '''
from PyQt5.QtWidgets import QApplication

''' Import the controller class, everything specific to this app starts from there '''
from controller import controller


class LP_Decrypter(QApplication):
    '''
        top level QApplication object
    '''

    def __init__(self, argv):
        QApplication.__init__(self, argv)
        # Everything is handled by the controller
        self.controller = controller(argv)


if __name__ == '__main__':
    print("Starting, good luck")
    app = LP_Decrypter(sys.argv)
    sys.exit(app.exec_())
