#!/bin/bash
# trying to pass an array variable


function testit {
    echo "The parameters is $@"
    thisarray=$1
    echo "The recieve array is: ${thisarray[*]}"
}

myarray=(1 2 3 4 5)
echo "The original array is: ${myarray[*]}"
testit $myarray

