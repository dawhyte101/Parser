import re
import sys
import Lex_Analyzer

program = ""

Current_Token = ""
Next_Token = ""
Current_Lexeme = ""

myVars = dict()
myVars["a"] = 0
myVars["b"] = 0
myVars["c"] = 0
myVars["w"] = ""
myVars["x"] = ""
myVars["y"] = ""
myVars["z"] = ""

def ProgramA ():
    global Next_Token
    global Current_Lexeme
    global Current_Token

    root = Leaf("Program")
    myLex()
    if Current_Token != 'START:':
        sys.exit("Error, no START")
    else:
        root.child.append(Leaf("Start"))
        myLex()
        statement_List(root)

    if Current_Token != ":END":
        print Current_Token
        print Next_Token
        sys.exit("Error, no END")
    else:
        root.child.append(Leaf("End"))
       #root.printTree(0)

def statement_List (Parent):
        root = Leaf("<Statement_List>")
        Parent.child.append(root)
        stmt(root)
        while(Current_Token == ";"):
            myLex()
            stmt(root)

def stmt(Parent):
    global myVars
    root = Leaf("<stmt>")
    Parent.child.append(root)
    if Current_Token == "var":
        v1 = var(Parent)
        if Current_Token != "=":
            sys.exit("Error, no =")
        else:
            Parent.child.append(Leaf("="))
            myLex()
            if Current_Token == ("Int_Literal"):
                Parent.child.append(Leaf("Int_Literal"))
                myVars[v1] = int(Current_Lexeme)
                myLex()

            elif Current_Token == "INPUT":
                Parent.child.append(Leaf("Input"))
                v2 = input()# make sure integer
                if type(v2) is int:
                    myVars[v1]=v2
                    myLex()
            else:
                v2=expr(root)
                myVars[v1]=v2

    elif Current_Token == "svar":
        v1 = svar(root)
        if Current_Token != "=":
            sys.exit("Error, no =")
        else:
            Parent.child.append(Leaf("="))
            myLex()
            if Current_Token == "svar":
                myVars[v1] = string(root)
            elif Current_Token == "String_Literal":
                Parent.child.append(Leaf("String_Literal"))
                myVars[v1] = str(Current_Lexeme)
                myLex()
            elif Current_Token == "INPUT":
                Parent.child.append(Leaf("Input"))
                v2 = raw_input()
                if type(v2) is str:
                    myVars[v1] = v2
                    myLex()

            else:
                sys.exit("Error, incorrect svar operation")

    elif Current_Token == "PRINT":
        root.child.append(Leaf("Print"))
        myLex()
        if Current_Token == "var" and Next_Token == "+":
            print str(expr(root))
        elif Current_Token == "svar" and Next_Token == "+":
            print myVars[string(root)]
        elif Current_Token == "var":
            print str(myVars[var(root)])
        elif Current_Token == "svar":
            print myVars[svar(root)]
        elif Current_Token == "String_Literal":
            root.child.append(Leaf("String_Literal"))
            print Current_Lexeme
            myLex()
        else:
            sys.exit("Error, incorrect Print")

    elif Current_Token != ":END":
        sys.exit("Error, Incorrect syntax")

def expr(Parent):
    root = Leaf("<expr>")
    Parent.child.append(root)

    if Current_Token == "var":#First var
        v1 = var(root)
        #print Current_Token
        if Current_Token == "+":#Read next variable if any
            root.child.append(Leaf(Current_Lexeme))
            myLex()
            if Current_Token == "var":
                v2 = var(root)
                #plus
                return myVars[v1] + myVars[v2]
            else:
                var(root)

        elif Current_Token == "-":
            root.child.append(Leaf(Current_Lexeme))
            myLex()
            if Current_Token == "var":
                v2 = var(root)
                #minus
                return myVars[v1]-myVars[v2]

        elif Current_Token == ";" or ":END":
            return

        else:
            sys.exit("Error, incorrect operator" + Next_Token)
    else:
        sys.exit("Error, incorrect variable")


def string(Parent): #Looks at the string to see if svar or var
    root = Leaf("<string>")
    #root.depth = Parent.depth +1
    Parent.child.append(root)
    v1= svar(root)
    if Next_Token == "svar" or "var":
        while Current_Token == "+":
            myLex()
            #root.child.append(Current_Lexeme)
            if Current_Token =="svar":
                v2 = svar(root)
                return myVars[v1] + myVars[v2]
            elif Current_Token =="var":
                v2 = var(root)
                return myVars[v1] + str(myVars[v2])


def var(Parent):
    root = Leaf("<var>")
    #root.depth = Parent.depth +1
    Parent.child.append(root)
    if Current_Lexeme == "a" or "b" or "c":
        root.child.append(Leaf(Current_Lexeme))
        temp = Current_Lexeme
        myLex()
        return temp

    else:
        sys.exit("Error, variable identifier")


def svar(Parent):
    root = Leaf("<svar>")
    #root.depth = Parent.depth +1
    Parent.child.append(root)
    if Current_Lexeme == "w" or "x" or "y" or "z":
         root.child.append(Leaf(Current_Lexeme))
         temp = Current_Lexeme #storing Current_Lexeme temporarily
         myLex()
         return temp #Return temp Current_Lexeme

    else:
            sys.exit("Error, string variable identifier")


#def input(Parent):

def myLex():
    global Current_Token
    global Current_Lexeme
    global Next_Token

    temp = myl.Lex()
    Current_Token = temp[0][0]
    Current_Lexeme = temp[0][1]
    Next_Token = temp[1][0]

class Leaf(object):

    def __init__(self, value):
        self.child = []
        self.value = value

    def printTree(self, depth):
        message = ""
        for i in range (0, depth, 1):
            message += "\t\t"
        print message, self.value
        for chi in self.child:
            chi.printTree(depth + 1)

if __name__ == "__main__":
    print ("<Program>")
    lang = list(program)

    #class TopDownParser:

    myl = Lex_Analyzer.Lex()
    ProgramA()