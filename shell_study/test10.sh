#!/bin/bash
# extract command line options and parameter


while [ -n "$1" ]
do
    case $1 in 
        -a) echo "Found the -a options";;
        -b) param="$2"
            echo "Found the -b options with paramter value $param"
            shift ;;
        -c) echo "Found the -c options";;
        --) shift 
            break ;;
        *)  echo "$1 is not an options";;
    esac 
    shift
done

count=1
for param in $1
do
    echo "Parameter #$count: $param"
    count=[ $count + 1 ]
done
