#!/bin/bash
# using a function in script


function explame {
    echo "This is a test use function"
}
count=1
while [ $count -lt 10 ]
do
    explame
    count=$[ $count + 1 ]
done

