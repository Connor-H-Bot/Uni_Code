#!/bin/bash 

# if two inputs are not put in for comparison...
if [[ -z $1 ]] || [[ -z $2 ]] 
then
    1>&2 echo "ERROR: Script requires 2x arguments"
    exit 2
elif [[ ! -f $1 ]]
then
    1>&2 echo "ERROR: Cannot find $1"
    exit 1
elif [[ ! -f $2 ]]
then
    1>&2 echo "ERROR: Cannot find $2"
    exit 1
else
    # both exist so record lengths
    file_1_len=$(cat $1 | wc -l)
    file_2_len=$(cat $2 | wc -l)
    if [[ $file_1_len -eq $file_2_len ]]
    then
        echo "Equal length!"
    elif [[ $file_1_len -gt $file_2_len ]]
    then
        echo "$1 is bigger!"
    else
        echo "$2 is bigger!"
    fi
fi
