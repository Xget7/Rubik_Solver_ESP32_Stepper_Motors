#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


import sys
import kociemba
import argparse
from video import webcam
import i18n
import os
from constants import (
    ROOT_DIR,
    E_INCORRECTLY_SCANNED,
    E_ALREADY_SOLVED
)

# Init i18n.
i18n.load_path.append(os.path.join(ROOT_DIR, 'translations'))
i18n.set('filename_format', '{locale}.{format}')
i18n.set('file_format', 'json')
i18n.set('locale', 'en')
i18n.set('fallback', 'en')

class Qbr:

    def __init__(self, normalize):
        self.normalize = normalize

    def swichCaseCube(solution = []):
        for i in solution:
            index = 0
            if i[index] == 'R':
                if(len(i) > 1 ):
                    if(i[index + 1] == '2'): 
                        print("R2 ");
                        #myCube.R2();
                    elif (i[index + 1] == "'"):
                        #// ASCII "'": apostrophe character
                        print("R' ");
                        # myCube.Rp()
                else:
                    print("R ")
                    # myCube.R()
            elif i[index] == 'L':
                if(len(i) > 1):
                    if(i[index + 1] == '2'): 
                        print("L2 ")
                        # myCube.L2()
                    elif(i[index + 1] == "'"):
                        #// ASCII "'": apostrophe character
                        print("L' ")
                        # myCube.Lp()
                else:
                    print("L ")
                    # myCube.L()
            elif i[index] == 'U':
                if(len(i) > 1):
                    if(i[index + 1] == '2'): 
                        print("U2 ")
                        # myCube.U2()
                        # return
                    elif(i[index + 1] == "'"):
                        #// ASCII "'": apostrophe character
                        print("U' ")
                        # myCube.Up()
                        # return
                else:
                    print("U ")
                    # myCube.U()
                    # return
            elif i[index] == 'D':
                if(len(i) > 1):
                    if(i[index + 1] == '2'): 
                        print("D2 ")
                        # myCube.D2()
                        # return
                    elif(i[index + 1] == "'"):
                        #// ASCII "'": apostrophe character
                        print("D' ")
                        # myCube.Dp()
                        # return
                else:
                    print("D ")
                    # myCube.D()
                    # return
            elif i[index] == 'F':
                if(len(i) > 1):
                    if(i[index + 1] == '2'): 
                        print("F2 ")
                        # myCube.F2()
                        # return
                    elif(i[index + 1] == "'"):
                        #// ASCII "'": apostrophe character
                        print("F' ")
                        # myCube.Fp()
                        # return
                else:
                    print("F ")
                    # myCube.F()
                    # return
            elif i[index] == 'B':
                if(len(i) > 1):
                    if(i[index + 1] == '2'): 
                        print("B2 ")
                        # myCube.B2()
                        # return
                    elif(i[index + 1] == "'"):
                        #// ASCII "'": apostrophe character
                        print("B' ")
                        # myCube.Bp()
                        # return
                else:
                    print("B ")
                    # myCube.B()
                    # return
            else:
                print("Error")
                return

    def run(self):
        """The main function that will run the Qbr program."""
        state = webcam.run()
        #cubeMove.begin(1)

        # If we receive a number then it's an error code.
        if isinstance(state, int) and state > 0:
            self.print_E_and_exit(state)

        try:
            algorithm = kociemba.solve(state)
            length = len(algorithm.split(' '))
        except Exception:
            self.print_E_and_exit(E_INCORRECTLY_SCANNED)

        print(i18n.t('startingPosition'))
        print(i18n.t('moves', moves=length))
        print(i18n.t('solution', algorithm=algorithm))
        return algorithm

        #la TECA es aca
                

    def print_E_and_exit(self, code):
        """Print an error message based on the code and exit the program."""
        if code == E_INCORRECTLY_SCANNED:
            print('\033[0;33m[{}] {}'.format(i18n.t('error'), i18n.t('haventScannedAllSides')))
            print('{}\033[0m'.format(i18n.t('pleaseTryAgain')))
        elif code == E_ALREADY_SOLVED:
            print('\033[0;33m[{}] {}'.format(i18n.t('error'), i18n.t('cubeAlreadySolved')))
        sys.exit(code)


    

if __name__ == '__main__':
    # Define the application arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--normalize',
        default=False,
        action='store_true',
        help='Shows the solution normalized. For example "R2" would be: \
              "Turn the right side 180 degrees".'
    )
    args = parser.parse_args()
    # Run Qbr with all arguments.
    qbr = Qbr(args.normalize)

    solution = qbr.run()
    
    solutionList = list(solution)
    solutionList.append(" ")
    sol = []
    fin = []
        
    for i in solutionList:
        if i in ["U","R","D","L","F","B"]:
            sol.append(i)
        elif i in ["2","'"]:
            sol.append(i)
        elif i in " ":
            print
            fin.append(sol)
            sol = []


    qbr.swichCaseCube(fin)
  
    

