
import sys

import os

passUser = "MyP00!0sswrd"
os.system("")


def checkLud(l, u, d, str):
    res = {}
    i = 1
    if (l == 0):
        res[i] = " no upper "
        i += 1
    if (u == 0):
        res[i] = " no lower case  "
        i += 1
    if (d == 0):
        res[i] = " no digits "
        i += 1
    if (str > 0):
        res[i] = "no spaces"
        i += 1
    return res


def validPass(passWord):
    l, u, d, s = 0, 0, 0, 0
    capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    str = " "
    output = passWord

    if (len(passWord) >= 10):

        for i in passWord:
            # counting lowercase alphabets
            if (i in smallalphabets):
                l += 1
            # counting uppercase alphabets
            if (i in capitalalphabets):
                u += 1
            # counting digits
            if (i in digits):
                d += 1

            if (i in str):
                s += 1

        if (len(passWord) == 0):
            print("input please input minimum 10")
        if (len(passWord) < 10):
            print( "input please input minimum 10")
            return 0
        if (l >= 1 and u >= 1 and d >= 1 and s == 0):
            file = open("Password.txt", "a")
            file.write(output)
            file.close()

            print('\033[0;32m', "password is valid", '\033[0m')
            return 0
        else:
            print('\033[91m', "password is invalid", '\033[0m')
            print(checkLud(l, u, d, s))
            return 1
    else:
        print( "input please input minimum 10")
        return 1

def main(value):
    if value == "-f":
        if (len(sys.argv[2]) > 0):
            f = open(sys.argv[2], 'r')
            save_pass = str(f.readline());
        return validPass(save_pass)
    else:
        return validPass(value)


main(sys.argv[1])





