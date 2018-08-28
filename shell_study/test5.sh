#!/bin/bash
# 跳出内部多个循环


for (( a = 1; a < 4; a++ ))
do
    echo "Outer loop: $a"
    for (( b = 1; b < 100; b++ ))
    do
        if [ $b -eq 5 ]
        then
            break 2
        fi 
        echo "Inter loop: $b"
    done
done
