#! /bin/bash

#Test if there is input
if [[ ! -z $1 ]]
then
    if [[ 1999 < $1 && $1 < 2019 && $1 < 0 ]] #Checks the input is within the year range && $1 < 2019, and is actually a number
    then
        unluckiest_country=$(cat incedenceOfMalaria.csv | grep $1 | cut -d ',' -f 1,4 | tr ',' ':' | sort -k2 -t':' -nr  | head -n 1)
        country_figure=$(echo $unluckiest_country | cut -f2 -d':')
        country_name=$(echo $unluckiest_country | cut -f1 -d':')
        if [[ ! -z $country_name && 0 < $country_figure ]] #Makes sure there is data in country name and a number for the figure
        then
            echo "The hardest hit country in $1 was $country_name with $country_figure infections per thousand. "
        else
            echo "ERROR: The file does not contain data for this year. "
            exit 1
        fi
    elif [[ 0 == 0 ]]
        echo "OKAY"
    fi
    else
        echo "ERROR: Data only ranges from 2000-2018. "
        exit 1
    fi
else
    echo "ERROR: Please check your input and try again. "
    exit 1
fi

#   cat incedenceOfMalaria.csv | grep 2007 | cut -d ',' -f 1,4 | tr ',' ':' | sort -k2 -t':' -nr  | head -n 1