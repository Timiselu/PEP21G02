"""
Take text from input: any text
# I will revert the change

"""


input1 = input("Write a text: ")
result = ''
previous = ''
for letter in input1:
    if previous == '':
        previous = letter
        result = result + letter
    else:
        l = chr(ord(letter) + ord(previous))
        result = result + l
        previous = letter
print(result)

k = input1[0]
result2 = k
for letter in result[1:]:
    new_k = chr(ord(letter) - ord(k))
    result2 += new_k
    k = new_k
print(result2)

# True and True

# False or False

XOR

a = 'a'
b = 'b'
print(a and b)
if a:
    print(b)
else:
    print(a)
a = False
b = True
print(a or b)
if a:
    print(a)
else:
    print(b)