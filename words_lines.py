f_name=input("Enter file name:-- ")
words=0
lines=  0
with open(f_name ,'r') as f_n:
	for line in f_n:
		n_words  = line.split()
		words += len(n_words)
		lines += 1   
print(" Number of words:-- " ,words )
print("Number of Lines: " ,lines)