import csv # import csv library to work with excel files

file = open("Books.csv","a") #Open a file called Books.csv in append mode
title = input("Enter a title: ")#capture the book title
author = input("Enter author: ")#capture the author
year = input("Enter the year it was released: ")#capture the year the book was released
newrecord = title +", "+author+", "+year+"\n"#compile the new text we want to write
file.write(str(newrecord))#write changes to the file
file.close()#close the file

file = open("Books.csv","r") #Open a file called Books.csv in read mode
for row in file:#Peform the operation in the next line of code for each row of the CSV file.
    print(row)#print the data in the row of the csv file to console window
file.close()#close the file