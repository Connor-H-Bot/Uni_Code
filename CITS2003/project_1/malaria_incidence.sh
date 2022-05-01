#! /bin/bash

if [[ ! -z $1 ]] #Test if there is input
then
    if [[ $1 == 20** && $1 < 2019 ]] #Checks the input is an int between 2000-2018
    then
        unluckiest_country=$(cat incedenceOfMalaria.csv | grep $1 | cut -d ',' -f 1,4 | tr ',' ':' | sort -k2 -t':' -nr  | head -n 1)
        country_figure=$(echo $unluckiest_country | cut -f2 -d':')
        country_name=$(echo $unluckiest_country | cut -f1 -d':')
        if [[ ! -z $country_name && 0 < $country_figure ]] #Makes sure there is data in country name and a number for the figure
        then
            echo "The hardest hit country in $1 was $country_name with $country_figure infections per thousand. "
            exit 0
        else
            echo "ERROR: This year does not have valid data. " 
            exit 1
        fi
    elif [[ $1 == [a-z]* || $1 == [A-Z]* ]] #Check if input is a string
    then
        echo "This works: $1 "
        hardest_year_and_stats=$(cat incedenceOfMalaria.csv | grep "$1" | cut -d ',' -f 3,4 | tr ',' ':' | sort -k2 -t':' -nr | head -n 1)
        highest_stat=$(echo $hardest_year_and_stats | cut -f2 -d':')
        year=$(echo $hardest_year_and_stats | cut -f1 -d':')
        echo "$1's worst year was $year, with infection rates of $highest_stat per thousand."
        exit 0
    elif [[ $1 == [1-9]* ]] #Error case for invalid year
    then
        echo "ERROR: Script only takes years from 2000-2018. "
        exit 1
    fi 
else
    echo "ERROR: Please check your input and try again. "
    exit 1
fi

#   cat incedenceOfMalaria.csv | grep 2007 | cut -d ',' -f 1,4 | tr ',' ':' | sort -k2 -t':' -nr  | head -n 1
