#1 /bin/bash
cut cool_online_game.csv -d ',' -f 1,2 --output-delimiter=' ' | sort -n -r -k2
