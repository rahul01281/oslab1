file = open('sample.txt', 'r') #open a file

print(file.read()) #read a file

print(file.read(5)) #print first 5 characters of the file

#creating a file
file2 = open('sample2.txt', 'w')
file2.write('writing something in this file')
file.close()

#adding to a existing file
file = open('sample2.txt', 'a')
file.write('\nadding to a line')
file.write('\nadding second line')
file.close()

#creating a list with words from each line
with open("sample2.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)