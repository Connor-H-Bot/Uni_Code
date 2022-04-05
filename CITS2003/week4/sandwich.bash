#!/bin/bash
if [[ -z $1 ]] #is $1 0 length
then 
    1>&2 echo "Error: please write something lol"
    exit 1
fi
if [[ -z $2 ]]
then
    bread="[==============================]"
else
    bread="[ $2 ]"
fi
echo $bread
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
echo " ------------------------------ "
echo " " $1
echo " ()()()()()()()()()()()()()()() "
echo " {}{}{}{}{}{}{}{}{}{}{}{}{}{}{} "
echo $bread