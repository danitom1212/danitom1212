import string
import sys

import os
passUser = "MyP00!0sswrd"
os.system("")



##if (any(x.isupper() for x in s) and any(x.islower() for x in s)
##  and any(x.isdigit() for x in s) and len(s) >= 7)
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
    output =passWord

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
            print('\033[91m', 0, "input please input minimum 10", '\033[0m')
        if (len(passWord) < 10):
            return print('\033[91m', 0, "input please input minimum 10", '\033[0m')
        if (l >= 1 and u >= 1 and d >= 1 and s == 0):

            file = open("Password.txt", "a")

            file.write(output)
            file.close()
            print('\033[0;32m', (0), '\033[0m')
            return 0
        else:
            print('\033[91m', 1, checkLud(l, u, d,  s), '\033[0m')
            return 0
    else:
        print('\033[91m', 1, "input please input minimum 10", '\033[0m')
        return 1


def main(pass1):
    if pass1>=sys.argv[0]:
        return validPass(sys.argv[0])
    else:
        return  validPass(pass1)


main("addada")
