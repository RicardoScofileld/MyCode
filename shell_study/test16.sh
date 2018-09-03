#!/bin/bash
# using the return command in a function


db1 () {
    read -p "Enter a value: " value
    echo "doubiling the value"
    return $[ $value * 2 ]
}

db1 
echo "status code is:$?. value is $value"
