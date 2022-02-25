version = '1.0.0'
def mrange(start=0,end=0,jump=1):
    a=[]
    if ((isinstance(start,str)==True and isinstance(end,str)==False) or (isinstance(start,str)==False and isinstance(end,str)==True)):
        raise NameError(f"Can't not run {type(start)} to {type(end)} be cause range of 'char'")
    if (jump<=0):
        i=start
        while i>end:
            a.append(i)
            i+=jump
        return a
    else:
        i=start
        while i<end:
            a.append(i)
            i+=jump
        return tuple(a)
def rangefloat(start=0.0,end=0.0, jump=1.0):
    a=[]
    if (not(isinstance(start,float)==True and isinstance(end,float)==True)):
        raise ValueError("'rangefloat' must return 'float'")
    if (jump<=0):
        i=start
        while i>end:
            a.append(i)
            i+=jump
    else:
        i=start
        while i<end:
            a.append(i)
            i+=jump
    return tuple(a)
def rangechar(start=' ',end=' ',jump=1):
    if (not (isinstance(start,str)==True and isinstance(end,str)==True)):
        raise ValueError("'start' and 'end' must be 'char'")
    elif (not (isinstance(jump,int)==True)):
        raise ValueError("'jump' must be 'int'")
    if (not (len(start)==1 and len(end)==1)):
        raise ValueError("'start' and 'end' must be 'char' not 'str'")
    start=ord(start)
    end=ord(end)
    a=[]
    if (jump<=0):
        i=start
        while i>end:
            a.append(chr(i))
            i+=jump
    else:
        i=start
        while i<end:
            a.append(chr(i))
            i+=jump
    return tuple(a)





