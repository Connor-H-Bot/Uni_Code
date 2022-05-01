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
    