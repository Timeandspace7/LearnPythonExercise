
# brief :
# date  :
# by    : T7
def starts_with(str1, str2):
	print(str1[:len(str2)] == str2);
	
starts_with("apple","ace");

def starts_with_v1(long, short):
	for position in range(len(short)):
		if long[position] != short[position]:
			return False;
	return True;
	
print(starts_with_v1("apple","ace"));