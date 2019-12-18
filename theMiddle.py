
# by :T7
def middle(str1,str2,str3):
	if(str1 < str2):
		if(str2 < str3):
			return str2;
		elif(str1 < str3):
			return str3;
		else:
			return str1;
	elif(str1 < str3):
		return str1;
	elif(str2 < str3):	
		return str3;
	else:
		return str2;
		
print(middle('Apple', 'applE', 'aPple'))

# by :udacity
def middle1(str1,str2,str3):
	if str1 < str2 < str3 or str3 < str2 < str1:
		return str2;
	if str2 < str1 < str3 or str3 < str1 < str2:
		return str1;
	if str1 < str3 < str2 or str2 < str3 < str1:
		return str3;
print(middle1('Apple', 'applE', 'aPple'))