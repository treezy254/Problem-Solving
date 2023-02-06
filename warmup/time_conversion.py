from tkinter import E


def timeConversion(s):
    a = ''

    if s[:-2] == "AM":
        if  s[:2] == '12':
            a = str('00' + s[2:8])
    
        else:
            a = s[:-2]

    else:
        if s[:2] == '12':
            a = s[:-2]
        else:
            a = str(int(s[:2]) + 12) + s[2:8]
    return a

    