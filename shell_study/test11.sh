#!/bin/bash
# Extract command lines options and values with getopt


set -- $(getopt -q ab:cd "$0")

echo 
while [ -n "$1" ]
do 
    case "$1" in
        -a ) echo "Find the -a options";;
        -b ) param="$2"
            echo "Find the -b options with parameter value $param"
            shift ;;
        -c) echo "Find the -c options";;
        --) shift
            break ;;
        * ) echo "$1 is not options";;
    esac
    shift 
done

count=1
for param in "$1"
do 
    echo "Parameter #$count: $param"
    count=$[ count + 1 ]
done

