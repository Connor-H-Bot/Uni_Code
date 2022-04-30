#!/usr/bin/env python
# Convert input string to title case
# v0.2 capitalises after hyphen

import sys

common_words = set(["a", "about", "after", "against", "all", "also", "an", "and", "another", "any",
        "are", "as", "at", "back", "be", "because", "been", "before", "being", "between", "both",
        "but", "by", "came", "can", "come", "could", "day", "did", "do", "down", "each", "even",
        "first", "for", "from", "get", "go", "good", "great", "had", "has", "have", "he", "her",
        "here", "him", "his", "how", "i", "if", "in", "into", "is", "it", "its", "just", "know",
        "last", "life", "like", "little", "long", "made", "make", "man", "many", "may", "me", "men",
        "might", "more", "most", "mr", "much", "must", "my", "never", "new", "no", "not", "now",
        "of", "off", "old", "on", "one", "only", "or", "other", "our", "out", "over", "own", "people",
        "right", "said", "same", "see", "she", "should", "since", "so", "some", "state", "still",
        "such", "take", "than", "that", "the", "their", "them", "then", "there", "these", "they",
        "this", "those", "three", "through", "time", "to", "too", "two", "under", "up", "us", "used",
        "very", "was", "way", "we", "well", "were", "what", "when", "where", "which", "while", "who",
        "will", "with", "work", "world", "would", "year", "years", "you", "your"])

def convert() :
  args = sys.argv
  if len(args) != 2 :
    sys.stdout.write("Usage: {0} <input string or -, if being used as a pipe>\n".format(args[0]))
    sys.exit(0)

  if args[1] != '-' :
    sys.stdout.write("{0}\n".format(convert_string(args[1])))
    return
    

  line = sys.stdin.readline()
  while line != "" :
    sys.stdout.write("{0}\n".format(convert_string(line)))
    line = sys.stdin.readline()
  return

# capitalise simple words and word pairs
def capitalise_word(word) :
  words = word.split('-')
  new_word_list = []
  for w in words :
    new_word_list.append(w.capitalize())
  if len(words) == 1 :
    return(new_word_list[0])
  return("-".join(new_word_list))

# converts string to title case
def convert_string(instring) :
  words = instring.split()
  new_words = [capitalise_word(words[0])]
  for w in words[1:] :
    if w in common_words :
      new_words.append(w)
    else :
      new_words.append(capitalise_word(w.lower()))
  return(" ".join(new_words))

if __name__ == "__main__" :
  convert()