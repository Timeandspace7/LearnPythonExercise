# brief : 计算字符长度是否大于 140
# date  : 2019.12.16
# by    : udacity

def too_long(s):
    # Complete this function!
    # It should return True when s is longer than 140.
    # It should return False when s is shorter than 140.
	return len(s) > 140;
    
# Test a short string
print("This should be False:")
print(too_long("I'm a short string!"))

# Test a long string
print("This should be True:")
print(too_long("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."))
