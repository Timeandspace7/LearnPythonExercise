#!/usr/bin/env python3
#
# Number Guessing Game!

# brief : 寻找匹配字符串位置
# by    : T7
# date  : 20219.12.20
def locate_all(str2, str1):
    length = len(str1);
    location = [];
    count = 0;
    for i in range(len(str2)):
        if(str2[i:length + i] == str1):
            location.append(i);
            count += 1;

    print(count);
    print(location)
    if(not location):
        print("no matches");
    else:
        print(location[0]);

# 注意这里特别有意思，原因是 “avc”[2:2] 为 0    
locate_all('the upside down','barb')

# brief : 寻找匹配字符串位置
# by    : udacity
# date  : 20219.12.20
def locate_first(string, sub): 
    index = 0
    while index < (len(string) - len(sub) + 1):
        if string[index : index + len(sub)] == sub:
            return index
        index += 1
    return -1

# brief : 寻找匹配字符串位置
# by    : udacity
# date  : 20219.12.20
def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string) - len(sub) + 1:
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches
