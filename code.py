from math import*
inp1= int(input("inp1:"))
inp2= int(input("inp2:"))
reg = int(input("register size :"))


'''
Return Type - Boolean
This function takes an input and check whether it is in binary or not '''
def isBinary(inp):
    inp=  str(inp)
    a= '01'
    flag=0
    for i in inp:
        if i not in a :
            flag=1
            break
        else:
            pass
    if flag:
        return False
    else:
        return True
'''
Retunn Type- String
This function takes an integer which are not in binary after isBinary check and convert it into binary and if the binary is not a n-bit string, add zeroes .if the number 
is negative,it will returns two's complemenet of that number'''   
def binary(num):
    b= bin(abs(num))[2:]
    b='0'*(len1-len(b))+b 
    if(num<0):
        return twosComplement(b)
    else :
        return b

'''Return Type- String
This function takes string as an arguement and converts the given binary string to its twos complement form. This is 
needed only in the case of negative numbers.
'''
def twosComplement(b):
    n= len(b)
    i =n-1
    while(i>=0):
        if(b[i] == '1'):
            break
        i =i-1
    k=i-1
    while(k>=0):
        if(b[k]== '0') :
            b = list(b) 
            b[k] = '1'
            b = ''.join(b) 
        else :
            b = list(b) 
            b[k] = '0'
            b= ''.join(b) 
        k=k-1

    if (i == -1):
        return '1'+str
    

    return b

'''
Return Type- String
This function takes string as an arguement and perform arithmetic right shift operation on the given input string.
'''
def ARM(bin):
    shift =bin[0]
    for i in range(0,len(bin)-1):
        shift=shift+bin[i]
    return shift



'''
Return Type- String
This function takes 2 strings as an arguement and perform binary addition of strings and returns the answer. In case of
overflow, it ignores the extra bits present on the left side.
'''
def add(n1, n2):
    sum=int(n1,2)+int(n2,2)
    c=bin(sum)[2:]
    # print(c)
    if len(c)<= len1:
        # print("y")
        c='0'*(len1-len(c))+c
    else:
        # print("n")
        c=c[1:]
    
    return c

'''
Return Type- (String, String)
This function takes two integers as an arguement and perform booth's multiplucation and returns decimal and binary form of
the answer obtained.
'''
def boothMul(inp1, inp2):
    global reg
    global len1
    len1=reg
    a = isBinary(inp1)
    if(a):
        inp1=str(inp1)
        inp1='0'*(len1-len(inp1))+inp1

    else :
        inp1 = binary(inp1)
    b =isBinary(inp2)
    if(b):
        # print("y")
        inp2=str(inp2)
        inp2='0'*(len1-len(inp2))+inp2

    else :
        inp2 = binary(inp2)
    # print(inp2)
    # a=add(inp1, inp2)

    # print(a)
    print("ACC","    Q","     q","    operation","    step count")
    _M = twosComplement(inp1)
    # print(_M)
    M = inp1
    # print(M)
    Q= inp2
    # print(Q)
    acc='0'*len1
    q='0'
    print(acc+ "    "+Q+"   "+q+"   "+"initial"+"           "+str(reg) )
    
    while reg!=0:
        if(Q[-1]+q=='10'):
            # print("minus")
            acc=add(acc,_M)
            res=ARM(acc+Q+q)
            # print(acc)
            print(acc+ "    "+Q+"   "+q+"   "+"A= A-M"+"    ")
            
        elif(Q[-1]+q=='01'):
            # print("add")
            acc=add(acc,M)
            res=ARM(acc+Q+q)
            # print(acc)
            print(acc+ "    "+Q+"   "+q+"   "+"A= A+M"+"    ")
        elif(Q[-1]+q=='00'):
            res=ARM(acc+Q+q)
        
        elif(Q[-1]+q=='11'):
            res=ARM(acc+Q+q)  
     
        
        # print(res)
        acc=res[:len1]
        # print(acc)
        Q=res[len1:len1*2]
        # print(Q)
        q=res[-1]
        # print(q)
        reg=reg-1
        print(acc+ "    "+Q+"   "+q+"   "+"rightShift"+"        "+str(reg))
    ans=acc+Q
    # print(ans)prin
    if(acc[0]=='1'):
        decimal=-int(twosComplement(ans),2)
    else:
        decimal= int(ans,2)
    print("In decimal:", str(decimal))
    print("In binary:" , ans)










boothMul(inp1,inp2)
# print(n)
