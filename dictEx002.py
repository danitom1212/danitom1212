import collections

# !1 ex 001

str1 = input('Put your string please\n')##input from user
str1 = sorted(str1)##sory by String letters
list1 = collections.Counter(str1)
newList={}

for key, value in list1.items():
    newList[key] = value
    print(key,"-", value)

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

list1 = [11, 7, 5, 37, 11,5]
list2 = [22, 8, 10, 1, 11]
list3 = [71, 3, 22, 8, 2,14,1]
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




"""
    EX 2 Home work 2
"""
import collections

# function for checking common values
def checkRepeatDigits(lst):
    """
    Check if list have repeat values
    :param lst: list
    :return: True/False
    """
    count_repeat_digit = collections.Counter(lst)
    for k,v in count_repeat_digit.items():
        if v > 1 :
            return True
    return False

# function for returning common values with "and"
def repeated_values(lst):
    """
    Return repeated values from list
    :param lst: list
    :return: repeated values
    """
    dict = collections.Counter(lst)
    result = " "
    for k,v in dict.items():
        if v > 1:
            result+=str(k) +" and "
    return result


def mainFunction (d):
    """
    Search only those lists that have at least one repeating organ
    Find common values (found in all) from all the lists you found
    in section a. If one list remains - all its organs are common,
    if no list remains - the answer will be empty
    :param d: dictionary
    :return: print the results
    """
    #create variables
    dict  = collections.Counter(d) # create dictionary
    array ,true_arr= [] ,[]# create array for adding to it values
    str_result = "" # create string for print result
    true_counter = 0 # count arrays with common values

    # main loop
    for k,v in dict.items():
        # if value is repeat in array print appropriate message, and +1 to true counter
        if(checkRepeatDigits(v)==True):
            print(f"{k} includes the values",repeated_values(v)[:-5],"more then once")
            true_counter+=1
        else:
            array.append(v) # add values to array
            str_result+= k +" and " # creating string for printing results

    # checking main conditions (Part B)
    if (true_counter==len(dict)): # all arrays have common values the answer is "empty answer"
        print(" ")
    if(true_counter==2):
        # this case for case if have one list without common values
        # according to the requirements this values must be output
        # trim "[]"
        print(f"list {str_result[:-5]} doesn't have common values ",str(array)[2:-2])

    if (len(dict)-true_counter>1): # several arrays doesnt have common digits

        res = str(set.intersection(*map(set,array)))
        if res == 'set()':
            print(" ")
        else:
            print(f"the common values (of {str_result[:-5]}) are : ",res)


list1_n = [11, 7, 5, 37, 11,5]
list2_n = [22, 8, 10, 1, 11]
list3_n = [71, 3, 22, 8, 2,14,1]
dict={"1L": list1_n,"2L" : list2_n, "3L" : list3_n}

mainFunction(dict)


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



