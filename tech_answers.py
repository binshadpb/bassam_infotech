
# 1. Consider two variables ‘var1’, ‘var2’ with integer values. Without the use of a third variable, swap the values of these two variables.

x = 6
y = 15

print("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

x = x + y
y = x - y
x = x - y

print("After swapping: ")
print("Value of x : ", x, " and y : ", y)




# 2. The user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. String letters are case sensitive.


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

string = input("Enter the String").strip()
sub_string = input("Enter the Substring").strip()

count = count_substring(string, sub_string)
print(count)







