#!/bin/bash
# extracting options and paramters 


echo 
while [ -n "$1" ]
do
    case "$1" in 
        -a) echo "Found the -a options";;
        -b) echo "Found the -b options";;
        -c) echo "Found the -c options";;
        --) shift
            break ;;
        *) echo "$1 is not an options";;
    esac
    shift
done
# 
count=1
for param in $@
do
    echo "Parameter #$count: $param"
    count=$[ count + 1 ]
done

