#! /bin/bash
cut arcade.csv -d ',' -f 1,2,6 --output-delimiter=' '|sort -n -r -k 3 |awk '{print $1,$3}'
