
# by :T7
def word_triangle_1(string):
	i = 0;
	for char in string:
		print(string[:len(string) - i]);
		i+=1;



# by :udacity
def word_triangle(word):
  length = len(word)
  for n in range(length):
    print(word[:length - n])

word_triangle_1("kitten");
print();
word_triangle("kitten");
