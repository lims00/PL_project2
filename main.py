import sys

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

            if(lexem=='call' or lexem=="print_ari" or lexem=="variable"): #????????? ??????
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
        elif (symbol=='T2'):  # { ??????
            next_token.append(2)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T3'): # } ??????
            next_token.append(3)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T4'): # , ??????
            next_token.append(4)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T5'): # ; ??????
            next_token.append(5)
            token_string.append(lexem)
            i += 1
        elif(symbol=="end"):
            i += 1
        elif (symbol=="T0"):
            print("Syntax Error")


def start():
    global indexnum
    functions()
    for i in all_list:
        if (all_list.count(i)>=2):
            all_list.remove(i)
    for k in list(f_stack.keys()):
        all_list.append(k)

    for j in all_list:
        if (all_list.count(j)>=2):
            print("Duplicate declaration of the identifier or the function name:%s/%s()"%(j,j))
            exit()
    print('Syntax O.K.')

def functions():
    global indexnum
    function()
    if(indexnum<len(next_token) and next_token[indexnum]==1):
        functions()

all_list=[]

def function():
    global indexnum,value_list
    identifier()
    funcname=token_string[indexnum-1]
    f_index[funcname]=indexnum-1

    if funcname in f_stack.keys():
        print("Duplicate declaration of the function name: %s"%funcname)
        exit()
    if(next_token[indexnum]==2):
        indexnum+=1

        if(funcname=='main'):
            value_list=[]
        else:
            value_list=[0]
        function_body()
        for i in value_list:
            if(i!=0 and value_list.count(i)==2):
                value_list.remove(i)
                print("Duplicate declaration of the identifier:%s"%i)
        f_stack[funcname]=value_list #?????? ?????? key??? ?????? value??? ARI??????
    else:
        print("Syntax Error")
        exit()

    if(next_token[indexnum]==3):
        indexnum+=1
        pass
    else:
        print("Syntax Error")
        exit()



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
        print("Syntax Error")
        exit()

    if(next_token[indexnum]==5):
        indexnum+=1
    else:
        print("Syntax Error")
        exit()



def var_list():
    global indexnum
    identifier()
    value_list.append(token_string[indexnum-1])
    all_list.append(token_string[indexnum-1])

    if(next_token[indexnum]==4):
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
            indexnum+=1
        else:
            print("Syntax Error")
            exit()
    elif(next_token[indexnum]==7):
        indexnum+=1
        if(next_token[indexnum]==5):
            indexnum+=1
        else:
            print("Syntax Error")
            exit()
    elif(next_token[indexnum]==1):
        identifier()
        if(next_token[indexnum]==5):
            indexnum+=1
            pass
        else:
            print("Syntax Error")
            exit()

    else:
        print("Syntax Error")
        exit()

def identifier():
    global indexnum
    if(next_token[indexnum]==1):
        pass
    else:
        print("Syntax Error")
        exit()
    indexnum+=1

def function_order(): #?????? call?????? ??????
    global flag
    funcname="main" #?????? ????????? main????????? caller??? ????????? main?????? ??????.
    if "main" not in f_stack.keys():
        print("No starting function.")
        exit()

    call_index=0
    return_num=0
    call_order.append('main')
    while(True):
        try:
            return_addr=[]
            caller_index=f_index[funcname] #caller??? index ??????
            right_paren_index=token_string.index('}',caller_index) #func(caller)??? '}' ??????
            call_index=token_string.index('call',caller_index,right_paren_index) #callee??? index
            return_num=token_string[caller_index:call_index].count(';')
            #return address??????????????? ?????? ???????????? call???????????? ;??? ????????? ?????? ??????
            if(token_string[caller_index:call_index].count('variable')>0):
                return_num-= token_string[caller_index:call_index].count('variable')
                #????????? ??? ?????????????????? ?????? ???????????? ????????? ?????????.
            return_addr.append(funcname) #retrun??? ????????? ?????? ??????
            return_addr.append(return_num+1) #func(caller)??? ?????? ????????? '}'??? ?????? ???????????? call ?????? ??? ?????? ?????? ?????? ?????? +1?????? ?????? ?????? ??????
            funcname=token_string[call_index+1] #caller?????? call??? ????????? ??????(callee ??????)
            flag=0
            if funcname not in f_stack.keys():
                print("\nCall to undefined function: %s"%funcname)
                flag=1
                sys.exit()

            call_order.append(funcname) #callee ??????
            f_stack[funcname].insert(0,return_addr)#f_stack??? return address??? ?????? ???????????? ????????????.
        except:
            break
    for i in range(len(call_order)):#???????????? ???????????? ??????
        if(i==0):
            pass
        else:
            if(f_stack[call_order[i]][0][0]=='main'):
                f_stack[call_order[i]][1]=0
            else:
                sum=0
                temp=i
                while((temp-2)>=0):
                    sum+=len(f_stack[call_order[temp- 2]])
                    temp-=1
                f_stack[call_order[i]][1] = sum

def execute():
    for k in range(len(call_order)):
        i=f_index[call_order[len(call_order)-k-1]]#?????? ????????? ??????
        func=call_order[len(call_order)-1-k]
        while(next_token[i]!=3):
            if(next_token[i]==5 or next_token[i]==2):
                #??????;??? ?????? ??????.????????? ?????? ??????????????? ????????? ??? ????????? ????????? ' ; ?????? ; ' ?????? ' { ?????? ; ' ??? ????????? ?????? ?????? ?????????.
                if(next_token[i+1]==1):
                    if(next_token[i+2]==5):
                        count = 0
                        where = 0
                        for j in range(call_order.index(func)+1):
                            try:
                                where=f_stack[call_order[call_order.index(func)-j]].index(token_string[i+1])
                                print("\n%s:%s => %d,%d"%(func,token_string[i+1],count,where))
                                count=0
                                where=0
                            except:
                                count+=1
                        i+=3
                    else:
                        i+=1
                else:
                    i+=1
            elif (next_token[i] == 7):   # print_ari ?????????
                if (next_token[i + 1] == 5): # ;????????? print ari ??????
                    call_order_reverse = list(reversed(call_order))
                    for m in call_order_reverse:
                        print("\n%s:" % m, end='')
                        for j in range(len(f_stack[m])):
                            k = len(f_stack[m]) - j - 1
                            if (m!= 'main'):
                                if (k ==len(f_stack[m])-1):
                                    print("Local variable: %s" %f_stack[m][k])
                                elif(k>1):
                                    print(" "*(len(m)+1),end='')
                                    print("Local variable: %s" % f_stack[m][k])
                                elif (k == 1):
                                    print(" " * (len(m)+1), end='')
                                    print("Dynamic Link:",end='')
                                    print(f_stack[m][k])
                                elif(k==0):
                                    print(" " * (len(m)+1), end='')
                                    print("Return Address: %s: %d"%(f_stack[m][0][0],f_stack[m][0][1]))
                            else:
                                if(k!=len(f_stack[m])-1):
                                    print(" " * (len(m)+1), end='')
                                print("Local variable: %s" %f_stack[m][k])
                    i+=1
                else:
                    i += 1
            else:
                i+=1

input_string=""
next_token = [] #token ??????
token_string = []
indexnum=0 #???????????? ?????? ??????
f_stack={} #ARI??? ????????? ??????
value_list=[] #??? ????????? variable ????????? ???????????? ??????????????? ???????????? ???
f_index={} #?????? ?????? index??????
return_addr=[] #return??? addr??? ??????????????? ???????????? ???
call_order=[] #????????? ???????????? ??????

def main():
    global input_string,flag
    #inputfile = sys.argv[1]
    #f = open(inputfile,'r')
    f = open('hello.txt', 'r')
    data = f.readlines()
    f.close()
    for line in data:
        input_string=input_string+line.strip()+' '
    lexical(input_string)#lexcal
    start()  #?????? ??????
    function_order() #?????? call?????? ?????? ??????
    if(flag==0):
        execute() #????????????


if __name__=="__main__":
    main()