#! /bin/bash

#Author: Connor Harris 23208009
#   This is a shell script designed to work with incedenceOfMalaria.csv and takes in 2 different kinds of input:
#   -year: enter a year between 2000-2018 and the script returns the country with the most cases per thousand that year
#   -Country: enter a country and it returns the year with the most cases from the specified country. 
#   -Country: Edge cases are created for commonly used names on some countries. These are lines 21-49
#   
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
        country=$1  #Lines 21-44 are edge cases for commonly used words
        if [[ "$country" == "Vietnam" ]]; then #Vietnam edge case
            country="Viet Nam"
        fi
        if [[ "$country" == "Ivory Coast" ]]; then #Ivory Coast edge case
            country="Côte d’Ivoire"
        fi
        if [[ "$country" == "DRC" ]]; then #DRC/Congo edge case
            country="Democratic Republic of the Congo"
        fi
        if [[ "$country" == "Laos" ]]; then #Laos edge case
            country="Lao People's Democratic Republic"
        fi
        if [[ "$country" == "North Korea" ]]; then #Nth Korea edge case
            country="Democratic People's Republic of Korea"
        fi
        if [[ "$country" == "South Korea" ]]; then #Sth Korea edge case
            country="Republic of Korea"
        fi
        if [[ "$country" == "Syria" ]]; then #Syria edge case 
            country="Syrian Arab Republic"
        fi
        if [[ "$country" == "UAE" ]]; then #UAE edge case
            country="United Arab Emirates"
        fi
        hardest_year_and_stats=$(cat incedenceOfMalaria.csv | grep -w "$country" | cut -d ',' -f 3,4 | tr ',' ':' | sort -k2 -t':' -nr | head -n 1)
        highest_stat=$(echo $hardest_year_and_stats | cut -f2 -d':')
        year=$(echo $hardest_year_and_stats | cut -f1 -d':')
        if [[ ! -z $year && $highest_stat > 0 ]] #Check if there was a return value
        then
            echo "$1's worst year was $year, with infection rates of $highest_stat per thousand."
            exit 0
        elif [[ ! -z $year ]]; then #The country is in the data set, but it had no data to report
            echo "$1 was in the dataset, but had no cases to report. "
        else
            echo "ERROR: $country is not in the dataset. " #Edge case for country not existing
            exit 1
        fi
    elif [[ $1 == [1-9]* ]] #Error case for invalid year
    then
        echo "ERROR: Script only takes years from 2000-2018. "
        exit 1
    fi 
else
    echo "ERROR: Please check your input and try again. "
    exit 1
fi
