expr = "START:PRINT \"Enter your Name\" ; w = INPUT ; PRINT \"Enter your favorite Number!\" ; a = INPUT ; PRINT \"Enter your street address\" ; x = INPUT ; PRINT \"Enter your City, state, zip-code\" ; y = INPUT ; b = 44 ; c = b + a ; PRINT w ; PRINT x ; PRINT y ; z = \"Your favorite number + 44 is \" ; z = z + c; PRINT z:END"
#expr ="START:a=10;PRINT a:END"
#expr = "START:z=\"Your favorite number + 44 is \" ; z = z + c; PRINT z:END"
#expr = "START: w = \"hi\" ; w = w + c; PRINT w:END"

current = 0
LA = []
class Lex():

    def __init__(self):
        tok = ""
        state = 0
        string = ""
        numstate = False
        numstring = ""

        lang = list(expr)
        for char in expr:
            tok += char
            if numstate == True and tok.isdigit() == False:
                print "INT_LIT " + numstring
                LA.append(("Int_Literal", numstring))
                numstring = ""
                numstate = False

            if tok == " ":
                if state == 0:
                   tok = ""
                else:
                    string += " "
                    tok=""
            elif tok == "INPUT":
                print "INPUT_COMMAND " + tok
                LA.append(("INPUT", tok))
                tok = ""
            elif tok == "PRINT":
                print "PRINT_COMMAND " + tok
                LA.append(("PRINT", tok))
                tok = ""
            elif tok == "\"":
                if state == 0:
                    state = 1
                    tok = ""
                else:
                    print " STING_LIT " + string
                    LA.append(("String_Literal", string))
                    string = ""
                    state = 0
                    tok = ""


            elif state == 1:
                string += char
                tok = ""
            elif tok == "+":
                print "ADD_OP " + tok
                LA.append(("+", tok))
                tok = ""
            elif tok == "-":
                print "SUB_OP " + tok
                LA.append(("-", tok))
                tok = ""
            elif tok == "=":
                print "ASSIGNMENT_OP " + tok
                LA.append(("=", tok))
                tok = ""
            elif tok == "START:":
                print "START " + tok
                LA.append(("START:", tok))
                tok = ""
            elif tok == ":END":
                print "END " + tok
                LA.append((":END", tok))
                tok = ""
            elif tok == ";":
                print "SEMI_COLON " + tok
                LA.append((";", tok))
                tok = ""
            elif tok == "a" or tok == "b" or tok == "c":
                print "INT_VARIABLE " + tok
                LA.append(("var", tok))
                tok = ""
            elif tok == "w" or tok == "x" or tok == "y" or tok == "z":
                print "STR_VARIABLE " + tok
                LA.append(("svar", tok))
                tok = ""
            elif tok.isdigit():
                numstring += tok
                numstate = True
                tok = ""
        LA.append(("eof", "eof"))

    def Lex(self):
        global current
        global LA
        Temp = [LA[current], LA[current +1]]
        current +=1
        return Temp

#l = Lex()

#for temp in LA:
#    print temp[0] + "," + temp[1]