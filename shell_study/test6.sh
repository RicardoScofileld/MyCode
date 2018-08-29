#!/bin/bash
# test $@ and $*
# $*输出的参数是一个整体，$@是单个输出


echo 
count=1
for param in "$*"
do
    echo "\$* Parameter #$count = $param"
    count=$[ $count + 1 ]
done

echo 
count=1
for param in "$@"
do
    echo "\$@ Parameter #$count = $param"
    count=$[ $count + 1 ]
done

