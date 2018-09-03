#!/bin/bash
# simple demonstration of the getopts command


echo 
while getopts :ab:c opt
do 
    case "$opt" in 
        a) echo "Find the -a option";;
        b) echo "Found the -b option, with value $OPTAGR";;
        c) echo "Found the -c option,";;
        *) echo "Unknow option: $opt";;
    esac
done

