# 1.Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
user_input = input("write a name: ")
text_file = open('name.txt', 'w')
text_file.write(user_input)
text_file.close()

# 2.Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
text_file = open('name.txt', 'r')
content = text_file.read()
print("\nYour name is", content)
text_file.close()

# 3.Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
# which should be... 59.
text_file = open('numbers.txt', 'r')
first_line = text_file.readline()
second_line = text_file.readline()
total = int(first_line) + int(second_line)
print("\nTotal of the first two numbers: ", total)
text_file.close()

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a
# file with any number of numbers.
total = 0
text_file = open('numbers.txt', 'r')
for content in text_file:
    total += int(content)

text_file.seek(0)
full_content = text_file.readlines()
print("\nList of all lines in numbers.txt: ", full_content)

print("\nThe total for all lines in numbers.txt is", total)
text_file.close()
