#!/bin/bash 
#check if theres any input and whether the file exists
if [[ ! -z $1 ]]
then
    if [[ -s $1 ]]
    then
        #declare variable that = ammount of lines
        longest_line=$(wc -lL $1) #| cut -d ' ' -f 1,2) 
        echo $longest_line
    else
        echo "ERROR: File $1 may be written wrong dummy"
        exit 1
    fi
else    
    echo "ERROR: No input"
    exit 1
fi