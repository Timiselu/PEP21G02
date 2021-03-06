# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower-case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become ("1234567A", "_ext_to_te_t")

def tsplit(text):
    final_tuple = ()
    splitted_text = text.split(sep=' ', maxsplit=1)
    splitted_text[0] = splitted_text[0].upper()
    for i in splitted_text[1]:
        if i.islower() is False:
            splitted_text[1] = splitted_text[1].replace(i, '_')
    final_tuple = tuple(splitted_text)
    return final_tuple

print(tsplit('1234567a Text to te5t'))
