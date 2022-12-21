
idetifier=1
left_paren=2
right_paren=3
comma=4
semi_colon=5
call=6
print_ari=7
variable=8

def lexical(inputs):
    checkdic={'T0': {"a": "T1", "b": "T1", "c": "T1", "d": "T1", "e": "T1", "f": "T1", "g": "T1", "h": "T1", "i": "T1",
            "j": "T1", "k": "T1","l": "T1", "m": "T1", "n": "T1", "o": "T1", "p": "T1", "q": "T1", "r": "T1", "s": "T1", "t": "T1",
            "u": "T1", "v": "T1", "w": "T1", "x": "T1", "y": "T1", "z": "T1",
            "A": "T1", "B": "T1", "C": "T1", "D": "T1", "E": "T1", "F": "T1", "G": "T1", "H": "T1",
            "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N": "T1", "O": "T1", "P": "T1",
            "Q": "T1", "R": "T1", "S": "T1", "T": "T1", "U": "T1", "V": "T1", "W": "T1", "X": "T1", "Y": "T1",
            "Z": "T1","_":"T1",
            "0": "T0", "1": "T0", "2": "T0", "3": "T0", "4": "T0", "5": "T0", "6": "T0", "7": "T0",
            "8": "T0", "9": "T0", ';': "T5", '{': "T2",'}':"T3",',':"T4",' ':"end"
            },
          'T1': {"a": "T1", "b": "T1", "c": "T1", "d": "T1", "e": "T1", "f": "T1", "g": "T1", "h": "T1", "i": "T1",
            "j": "T1", "k": "T1","l": "T1", "m": "T1", "n": "T1", "o": "T1", "p": "T1", "q": "T1", "r": "T1", "s": "T1", "t": "T1",
            "u": "T1", "v": "T1", "w": "T1", "x": "T1", "y": "T1", "z": "T1",
            "A": "T1", "B": "T1", "C": "T1", "D": "T1", "E": "T1", "F": "T1", "G": "T1", "H": "T1",
            "I": "T1", "J": "T1", "K": "T1", "L": "T1", "M": "T1", "N": "T1", "O": "T1", "P": "T1",
            "Q": "T1", "R": "T1", "S": "T1", "T": "T1", "U": "T1", "V": "T1", "W": "T1", "X": "T1", "Y": "T1",
            "Z": "T1","_":"T1",
            "0": "T1", "1": "T1", "2": "T1", "3": "T1", "4": "T1", "5": "T", "6": "T1", "7": "T1",
            "8": "T1", "9": "T1", ';': "T5", '{': "T2",'}':"T3",',':"T4",' ':"end"}
          }
    i=0
    while(i<len(inputs)):
        lexem=inputs[i]
        symbol=checkdic["T0"][inputs[i]]
        if (symbol=='T1'):
            i+=1
            while(checkdic[symbol][inputs[i]]=='T1'):
                lexem+=inputs[i]
                symbol = checkdic[symbol][inputs[i]]
                i += 1

            if(lexem=='call' or lexem=="print_ari" or lexem=="variable"):
                if(lexem=="call"):
                    token_string.append("call")
                    next_token.append(6)
                elif(lexem=="print_ari"):
                    token_string.append("print_ari")
                    next_token.append(7)
                else:
                    token_string.append("variable")
                    next_token.append(8)
            else:
                token_string.append(lexem)
                next_token.append(1)
        elif (symbol=='T2'):
            next_token.append(2)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T3'):
            next_token.append(3)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T4'):
            next_token.append(4)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T5'):
            next_token.append(5)
            token_string.append(lexem)
            i += 1
        elif(symbol=="end"):
            i += 1
        elif (symbol=="T0"):
            print("error")

indexnum=0

def start():
    global indexnum
    functions()

def functions():
    global indexnum
    function()
    if(next_token[indexnum]==1):
        functions()



def function():
    global indexnum
    identifier()
    if(next_token[indexnum]==2):
        indexnum+=1
        function_body()
    else:
        print("function1 syntax error")

    if(next_token[indexnum]==3):
        indexnum+=1
        pass
    else:
        print("function2 syntax error")


def function_body():
    global indexnum
    if(next_token[indexnum]==8):
        var_definitions()
    statements()

def var_definitions():
    global indexnum
    var_definition()
    if(next_token[indexnum]==8):
        var_definitions()


def var_definition():
    global indexnum
    if(next_token[indexnum]==8):
        indexnum+=1
        var_list()
    else:
        print("var definition1 syntax error")

    if(next_token[indexnum]==5):
        indexnum+=1
    else:
        print("var definition2 syntax error")


def var_list():
    global indexnum
    identifier()
    if(next_token==4):
        indexnum+=1
        var_list()


def statements():
    global indexnum
    statement()
    if(next_token[indexnum]==6 or next_token[indexnum]==7 or next_token[indexnum]==1):
        statements()


def statement():
    global indexnum
    if(next_token[indexnum]==6):
        indexnum+=1
        identifier()
        if (next_token[indexnum]==5):
            pass
        else:
            print("statement1 error")

    elif(next_token[indexnum]==7):
        indexnum+=1
        if(next_token[indexnum]==8):
            indexnum+=1
            pass
        else:
            print("statment2 syntax error")


    elif(next_token[indexnum]==6):
        identifier()
        if(next_token[indexnum]==5):
            indexnum+=1
            pass
        else:
            print("statement 3syntax error")

    else:
        print("statmentsyntax4 error")

def identifier():
    global indexnum
    if(next_token[indexnum]==1):
        pass
    else:
        print("identi syntax error")
    indexnum+=1





next_token = []
token_string = []
input_string=""
def main():
    global input_string
    #inputfile = sys.argv[1]
    #f = open(inputfile,'r')
    f = open('hello.txt', 'r')
    data = f.readlines()
    f.close()
    for line in data:
        input_string=input_string+line.strip()+' '
    lexical(input_string)
    print(next_token)
    print(token_string)

    start()


if __name__=="__main__":
    main()