#Q1
def get_name(name_dict, id_num):
    if id_num in name_dict:
        return name_dict[id_num]
    else:
        return None

#2 Count occurences of each word
def word_counter(input_str):
    sentence = input_str.lower().split()
    ls = []  
    for i in sentence:

        word_count = sentence.count(i)  
        ls.append((i,word_count))       

    ls.sort(key=lambda x: x[1])
    dict_ = dict(ls)
    return dict_

#3 Swaps dictionary key and values and looks for match
def find_key(input_dict, value):
    dict = {value:key for key, value in input_dict.items()}
    if value in dict:
        return dict[value]
    else:
        return None
        
#4 
def make_index(words_on_page):
    return 

#5
def make_dictionary(filename):
    return 

#6
def isbn_dictionary(filename):
    return 

#7
def long_enough(strings, min_length):
    return 

#8
def my_enumerate(items):
    return

#9
def run_length_encode(nums):
    return 

#10
def composite2(N):
    return 

#11
def series(x):
    return 

#12
def nextRound(k,scores):
    return 

#13
def singleDigit(N):
    return 

#14
def sequence(n):
    return 