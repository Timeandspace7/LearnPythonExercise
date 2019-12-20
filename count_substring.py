#!/usr/bin/env python3
#
# Number Guessing Game!

# brief: 寻找子字符串
# by   : T7
# date : 2019.12.20
def count_substring(str1, str2):
    length = len(str1);
    count = 0;
    for i in range(len(str2)):
        if(str2[i:length + i] == str1):
            count += 1;

    print(count);


# 注意这里特别有意思，原因是 “avc”[2:2] 为 0    
count_substring('', 'balloon')

# brief: 寻找子字符串
# by   : udacity
# date : 2019.12.20
def count_substring_v1(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
        index += 1    # <- look here
    return count

# brief: 这里不计算重复匹配
def count_substring_v2(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
            index += len(target)   # <- look here
        else:
            index += 1
    return count
