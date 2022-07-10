import collections

# !1 ex 001

str1 = input('Put your string please\n')##input from user
str1 = sorted(str1)##sory by String letters
list1 = collections.Counter(str1)
newList={}

for key, value in list1.items():
    newList[key] = value
    print(key, value)

print(newList)
str2 = {}


for key, value in newList.items():##crate the final dictionary
    if value not in str2:##Check if there is another signal if an equal number of repetitions
        str2[value] = [key]
    else:
        str2[value].append(key)
print("final dictionary", str2)


# !2 ex 002
print("_____________________________________________")

list1 = [1, 112, 33, 47, 5,1]
list2 = [2, 3, 4, 6, 8]
list3 = [11, 12, 31, 88, 59,2]
list4={"1L": list1,"2L" : list2, "3L" : list3}

def showReturn(list):
    listSet = set(list)
    checkDuplicates = len(list) != len(listSet)##Check with the new dictionary length  if they are copies
    result = "list : " + str(list) + " : There are duplicates more than once >>> "
    if checkDuplicates :#  if they are copies
        listKeyValue = collections.Counter(list)
        for k, v in listKeyValue.items():
            if v > 1:
                result += str(k)
        print(result)
        return True
    else:
        print("list:" + str(list) +"There is no duplicate value!!")
        return False


def checkAll(allList):##Check the remaining strings
    dict1 = {}
    newToCheck=[]

    for k, v in allList.items():
        if not showReturn(v):##If there are not copies
            dict1 [k] = [v]
            newToCheck +=v
    showReturn(newToCheck)##Returns existing copies of all list if they exist
checkAll(list4)


# !3 ex 003
print("_____________________________________________")

# Python 3 code to demonstrate
# removing duplicated from list
# using naive methods


my_list = [1,1,2,3,2,2222222,4,5,6,2,1]

def checkNumStr(num,orderBy):
    s = ''.join(str(x) for x in my_list)
    res = []
    res[:0] = s
    my_final_list = set(res)
    if orderBy =="asc":
        result= sorted(my_final_list)
    if orderBy =="desc":
        result = sorted(my_final_list,reverse=True)
    return (result)
def checkNumStrLoop(n1):
    orderBy = input('What is order?\n')
    print(checkNumStr(n1,orderBy))
checkNumStrLoop(my_list)



