
# This is a work Python script.
# list of numbers


myList=[1,2,3,4,5,3,1,2]
#numbers = (0,) * 5  we use the comma to denote that this is a single valued tuple and not an #expression

# new array
ls = []
# check if list contains only numbers
for value in myList:
    try:
       ls.append(('*')*int(value))
    except ValueError:
        print("is not int")

print(ls)

#2
#combine 2 array str
#
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst




lis =["a","d","c"];
lis1 =["x","y","z"];
finList= []

for x in range(len(lis)):
    finList.append(str(lis[x]) + (str(Reverse(lis1)[x])))

print(finList)

# Reversing a list using slicing technique
def add(num1:int=2,num2:int=3)-> int:
    """
    :param num1:
    :param num2:
    :return:
    """
    if not isinstance(num1,int)or not isinstance(num2,int):
        raise TypeError("at least one of params")
    return num2+num1

print(add())


lst1 = [11,  7, 5,  8, 5,  37,  11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 14, 1]

all_lists_dic = {"lst1": lst1, "lst2": lst2, "lst3": lst3}
fit_dic = {}

for name, lst in all_lists_dic.items():
    tmp_set = set(lst)
    if len(tmp_set) == len(lst):
        fit_dic[name] = tmp_set

print(fit_dic)
common_values = set.intersection(*fit_dic.values())

print(common_values, " ".join(fit_dic.keys()))

# lst = [10, 20, 30, 40]
# s = " ".join([str(v) for v in lst])
# print(s, lst)

# initialize list
test_list = ['gfg', 'is', 'befgfhgfht', 'ffasdfdsfjnnjlnsdfsor', 'geeks']
def maxStrlist(test):

    print("The original list : " + str(test))

# Longest String in list
# using loop
    max_len = -1
    for ele in test:
     if len(ele) > max_len:
        max_len = len(ele)
        res = ele

# printing result
    print("111 Maximum length string is : " + min(res))


maxStrlist(test_list)
def prinAllMax(test):
# Longest String in list
# using max() + key

# printing original list
    print("The original list : " +str(test))

# Longest String in list
# using max() + key
    res = max(test, key = len)

# printing result
    print("222 Maximum length string is : " + min(res))


prinAllMax(test_list)


lst = ["foo", "hello", "python", "barskjhflskhjlj", "goodday", "a", "xy"]
print(max(lst))
