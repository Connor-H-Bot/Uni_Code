#2
def count_word(sentence, word):
    y = sentence.count(word)
    return y

#3
def is_a_number(string):
    y = string.isdigit()
    return y

#4
def find_word(sentence, word):
    y = sentence.index(word)
    return y

#5
def top_and_tail(string):
    y = string[1:len(string)]
    return y

#6
def half_string(string):
    y = len(string)//2
    x = string[0:y]
    return x

#7
def second_half_string(string):
    y = len(string)//2
    x = string[y:len(string)]
    return x

#8
def first_nth_string(string, n):
    y = string[0:n]
    return y

#9
def full_name(first_name, last_name):
    
#10
def insert_item(data, item, ind):
    data.insert(ind, item)
    return data

#11
def count_items(data):
    return len(data)

#12
def third(data):
    return data[2]

#13
def insert_item_end(data, item):
    data.append(item)
    return data

#14
def append_list_new(data1, data2):
    data3 = []
    data3.extend(data1)
    data3.extend(data2)
    return data3

#15
def append_lists(data1, data2):
    data3 = []
    data3.extend(data1)
    data3.extend(data2)
    return data3

#16
def last(data):
    return data[len(data) - 1]

#17
def remove(data):
    del data[1]
    return data

#18
def nth_item(data, n):
    return data[n]

#19
def repeat_last(data):
    data2 = []
    data2.extend(data)
    data2.append(data[-1])
    return data2

#20
def cubed_tuple(number):
    squared_num = number**number
    if number == 0:
        squared_num = 0
    mytup = (number, squared_num)
    return mytup

#21
def list_swap(lst):
    isOdd = False
    x = 0
    if (len(lst) % 2) > 0:
        lst.append(1)
        isOdd = True
    while x < len(lst):
        lst[x], lst[x + 1] = lst[x + 1], lst[x]
        x += 2
    if isOdd == True:
        del lst[-2]
    return lst

#22
def num_words(string):
    x = string.split(' ')
    return len(x)

#23
def list_sorting(lst1,lst2):
    length = len(lst1)
    list_2d = [[0]*2]*length
    index = 0
    while index < length:
        list_2d[index][0] = lst1[index]
        list_2d[index][1] = lst2[index]
        index += 1
    print(sorted(list_2d, key=lambda l:l[1]), reverse=True)

print(list_sorting(["Tom", "Luke", "Harry",], [12, 13, 15]))
