# Author: IBN (AMDG) 1/25/2022
def comes_after(st, l):
    result = []
    l = l.lower()
    try:
        for i in range(len(st)):
            if st[i].lower() == l and st[i+1].isalpha():
                result.append(st[i+1])
    except:
        pass
    return "".join(result)