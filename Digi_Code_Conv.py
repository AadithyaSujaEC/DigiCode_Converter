from tabulate import tabulate
import pandas as pd
import win32com.client as wc
def BtG(x):#binary to gray(BtG)
    g=list(x)
    h=len(x)
    k=[]
    i=1
    while i!=h:
        y=int(g[i])^int(g[i-1])
        k.append(str(y))
        i+=1
    i=1
    r=g[0]
    while i!=h:
        r+=k[i-1]
        i+=1
    return r

def GtB(x):#gray to binary(GtB)
    g=list(x)
    h=len(x)
    k=[]
    i=1
    y=int(g[0])
    while i!=h:
        y=y^int(g[i])
        k.append(str(y))
        i+=1
    i=1
    r=g[0]
    while i!=h:
        r+=k[i-1]
        i+=1
    return r


def DtB(x):#decimal to binary
    y=bin(int(x))
    r=y[2:]
    return r

def BtD(x):#binary to decimal
    g=list(str(x))
    k='0b'
    for i in g:
        k+=i
    k=str(int(k,2))
    return k

def BX3(x):#binary to xs3
    r= int(BtD(x))
    r+=3
    r=DtB(r)
    return r

def X3B(x):#XS3 to binary
    r= int(BtD(x))
    r-=3
    if  (r>=0):
         r=DtB(r)
         return r
    else:
        a='Invalid'
        return a

def DtG(x):#decimal to gray
    x=DtB(x)
    x=BtG(x)
    return x

def GtD(x):#gray to decimal
    x=GtB(x)
    x=BtD(x)
    return x

def DX3(x):#Decimal to XS3
    x=DtB(x)
    x=BX3(x)
    return x
def X3D(x):#XS3 to decimal
    x=X3B(x)
    x=BtD(x)
    return x

def g():
    print('--'*64)
def h():
    print()
    print()
def X3G(x):#XS3 to gray
    x=X3B(x)
    x=BtG(x)
    return x
def GX3(x):#Gray to XS3
    x=GtB(x)
    x=BX3(x)
    return x

l=['Decimal to Binary','Binary to Decimal','Binary to Gray','Gray to Binary','Binary to XS3','XS3 to Binary','Decimal to XS3','XS3 to Decimal','Decimal to Gray','Gray to Decimal','XS3 to Gray','Gray to XS3']
d={'FUNCTION      ':l,'KEY':[1,2,3,4,5,6,7,8,9,10,11,12]}
a=pd.DataFrame(d,index=['A','B','C','D','E','F','G','H','I','J','K','L'])
h()
print('     Welcome To My Code Converter System   ')
h()
g()
print(tabulate(a, headers = 'keys', tablefmt = 'psql'))
print ('13 to exit the system')
g()
h()
p=0
while True:
    t=int(input('Enter Your Key For The Function: '))
    if t==13:
        c=input('Are You Sure [Y/N]:')
        if c=='Y':
            sp = wc.Dispatch("SAPI.SpVoice")
            sp.Speak("Thank You and have a nice day")
            print('Thank You and have a nice day')
            quit()
        else:
            t=int(input('Enter Your Key For The Function: '))
    elif t==1:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Decimal:')
            print(DtB(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==2:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Binary:')
            print(BtD(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==3:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Binary:')
            print(BtG(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==4:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Gray:')
            print(GtB(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==5:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Binary:')
            print(BX3(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==6:
        while p!='N':
            print(l[t-1])
            x=input('Enter your XS3:')
            print(X3B(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==7:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Decimal:')
            print(DX3(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break

    elif t==8:
        while p!='N':
            print(l[t-1])
            x=input('Enter your XS3:')
            print(X3D(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==9:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Decimal:')
            print(DtG(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==10:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Gray:')
            print(GtD(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==11:
        while p!='N':
            print(l[t-1])
            x=input('Enter your XS3:')
            print(X3G(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    elif t==12:
        while p!='N':
            print(l[t-1])
            x=input('Enter your Gray:')
            print(GX3(x))
            p=input('Do you want to use same function [Y/N] : ')
            if p=='N':
                p=0
                break
    
    
        

    


