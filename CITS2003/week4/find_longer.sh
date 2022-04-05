#!/bin/bash 

#if two inputs are not put in for comparison...
if [[ $# -ne 2 ]]
then 
    echo "ERROR: Script requires 2x arguments"
    exit 1

#If one input doesnt exist
[elif [[ ! -f $# ]]
then 
    echo "ERROR: One or more arguments don't exist"
    exit 1]

#Finally, if it does exist
[else 
    file_1_len=$(cat $1 | wc -l)
    file_2_len=$(cat $2 | wc -l)
    if [[ file_1_len -eq file_2_len ]] 
        echo "Equal length!"
        exit 0
    [elif [[ file_1_len -gt file_2_len ]]
        echo "$1 is bigger!"
        exit 0]
    [else
        echo "$2 is bigger!"
        exit 0]
]
fi
