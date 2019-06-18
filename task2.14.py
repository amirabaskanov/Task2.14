line = input("Write your text: ")

number_of_f = line.count('f')
A = line.index('f')
d = line[::-1]
B = d.index('f')
print("Number of f's: " + str(number_of_f))
print("First f index: " + str(A))
print("Last f index: " + str(-(B+1)))
print("String length: " + str(len(line)))
