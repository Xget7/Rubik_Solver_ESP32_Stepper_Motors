
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

            
fakeSol = "U R' D2 L2 F2 L U2 L F' U L U R2 B2 U' F2 D2 R2 D2 R2"
solutionList = list(fakeSol)
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
swichCaseCube(fin)

