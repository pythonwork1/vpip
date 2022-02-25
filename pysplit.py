version = '1.0.0'
def tachso(xau):
    mang=''
    for  i in xau:
        if (i>='0' and i<='9'):
            mang+=i
        else:
            mang+=' ' 
    mang=mang.split()
    if (len(mang)>0):
        return mang
    else:
        return False
def ghep(xau1,xau2):
    mang=xau1+xau2
    return mang
def tachchu(xau):
    mang=''
    for  i in xau:
        if not(i>='0' and i<='9'):
            mang+=i
        else:
            mang+=' ' 
    mang=mang.split()
    if (len(mang)>0):
        return mang
    else:
        return False
def dem(xau,kitu):
    s=0
    for i in xau:
        if (i!=kitu):
            s+=1
    if (s<len(xau)):
        return s
    else:
        return False
def delete(xau,kitucanxoa):
    mang=''
    for i in xau:
        if (i!=kitucanxoa):
            mang+=i
    if (len(xau)>len(mang)):
        return mang
    else:
        return False
def dechu(xau):
    mang=xau.split()
    return len(mang)
def doixung(xau):
    mang=True
    for i in range (len(xau)//2):
        if not(xau[i]==xau[len(xau)-i-1]):
            mang=False
    return mang
def them(xau,kitu,vitri):
    if (vitri<len(xau)):
        manga=''
        mangb=''
        for i in range (len(xau)):
            if (i<=vitri-1):
                manga+=xau[i]
            else:
                mangb+=xau[i]
        mangc=manga+kitu+mangb
        return mangc
    else:
        return False
