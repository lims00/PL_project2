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

            if(lexem=='call' or lexem=="print_ari" or lexem=="variable"): #예약어 찾기
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
        elif (symbol=='T2'):  # { 찾기
            next_token.append(2)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T3'): # } 찾기
            next_token.append(3)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T4'): # , 찾기
            next_token.append(4)
            token_string.append(lexem)
            i += 1
        elif (symbol=='T5'): # ; 찾기
            next_token.append(5)
            token_string.append(lexem)
            i += 1
        elif(symbol=="end"):
            i += 1
        elif (symbol=="T0"):
            print("error")


def start():
    global indexnum
    functions()
    print('Syntax O.K.')

def functions():
    global indexnum
    function()
    if(indexnum<len(next_token) and next_token[indexnum]==1):
        functions()



def function():
    global indexnum,value_list
    identifier()
    funcname=token_string[indexnum-1]
    f_index[funcname]=indexnum-1
    if(next_token[indexnum]==2):
        indexnum+=1

        if(funcname=='main'):
            value_list=[]
        else:
            value_list=[0]
        function_body()
        f_stack[funcname]=value_list #함수 이름 key로 하고 value로 ARI저장
    else:
        print("function1 syntax error")
        exit()

    if(next_token[indexnum]==3):
        indexnum+=1
        pass
    else:
        print("function2 syntax error")
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
        print("var definition1 syntax error")
        exit()

    if(next_token[indexnum]==5):
        indexnum+=1
    else:
        print("var definition2 syntax error")
        exit()



def var_list():
    global indexnum,var_list
    identifier()
    value_list.append(token_string[indexnum-1]) # 함수선언하는 곳 이름과 index값으로 저장
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
            print("statement1 error")
            exit()
    elif(next_token[indexnum]==7):
        indexnum+=1
        if(next_token[indexnum]==5):
            indexnum+=1
        else:
            print("statment2 syntax error")
            exit()
    elif(next_token[indexnum]==1):
        identifier()
        if(next_token[indexnum]==5):
            indexnum+=1
            pass
        else:
            print("statement 3syntax error")
            exit()

    else:
        print("statmentsyntax4 error")
        exit()

def identifier():
    global indexnum
    if(next_token[indexnum]==1):
        pass
    else:
        print("identi syntax error")
        exit()
    indexnum+=1

def function_order(): #함수 call하는 순서
    funcname="main" #처음 시작은 main이니까 caller의 함수를 main으로 한다.
    call_index=0
    return_num=0
    call_order.append('main')
    while(True):
        try:
            return_addr=[]
            caller_index=f_index[funcname] #caller의 index 저장
            right_paren_index=token_string.index('}',caller_index) #func(caller)의 '}' 위치
            call_index=token_string.index('call',caller_index,right_paren_index) #callee의 index
            return_num=token_string[caller_index:call_index].count(';')
            #return address찾기위해서 함수 선언부터 call전까지의 ;로 문장의 개수 세기
            if('variable' in token_string[caller_index:call_index]):
                return_num-=1 #앞에서 센 문장개수에서 변수 선언문의 개수는 빼준다.
            return_addr.append(funcname) #retrun할 함수의 이름 저장
            return_addr.append(return_num+1) #func(caller)의 이름 위치와 '}'의 위치 사이에서 call 하는 거 위치 찾기 그럼 그거 +1한게 함수 이름 위치
            funcname=token_string[call_index+1] #caller에서 call한 함수의 이름(callee 이름)
            call_order.append(funcname) #callee 저장
            f_stack[funcname].insert(0,return_addr)#f_stack에 return address의 값을 리스트로 넣어준다.
        except:
            break
    for i in range(len(call_order)):
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
        i=f_index[call_order[len(call_order)-k-1]]#함수 선언한 위치
        func=call_order[len(call_order)-1-k]
        while(next_token[i]!=3):
            if(next_token[i]==5 or next_token[i]==2):
                #변수;를 찾기 위함.그러나 함수 시작부분에 위치할 수 있음을 고려해 ' ; 변수 ; ' 또는 ' { 변수 ; ' 의 패턴을 갖는 것을 찾는다.
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
            elif (next_token[i] == 7):   # print_ari 만나고
                if (next_token[i + 1] == 5): # ;만나면 print ari 실행
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
next_token = [] #token 저장
token_string = []
indexnum=0 #리스트내 현재 위치
f_stack={} #ARI를 저장할 정보
value_list=[] #각 함수의 variable 선언시 변수들을 일시적으로 저장하는 곳
f_index={} #함수 선언 index위치
return_addr=[] #return할 addr를 일시적으로 저장하는 곳
call_order=[] #함수를 실행하는 순서

def main():
    global input_string
    #inputfile = sys.argv[1]
    #f = open(inputfile,'r')
    f = open('hello.txt', 'r')
    data = f.readlines()
    f.close()
    for line in data:
        input_string=input_string+line.strip()+' '
    lexical(input_string)#lexcal
    start()  #구문 분석
    function_order() #함수 call되는 순서 파악
    execute() #실행부분

if __name__=="__main__":
    main()