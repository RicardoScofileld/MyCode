#!/bin/bash
# 使用break跳出单个循环


for var in 1 2 3 4 5 6 7 8 9 10
do 
    if [ $var -eq 5 ]
    then
        break
    fi
    echo "Interation number: $var"
done
echo "The for loop is complete"
