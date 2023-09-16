frutes = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(frutes[1])
# print(frutes[:4])
# print(frutes[2:])
# print(frutes[-4:-1])
#
# if "apple" in frutes:
#     print("Yes, 'apple' is in the frutes tuple")


#################################################################################

# x = list(frutes)
#
# x[1] = "Watermelon"
#
# frutes = tuple(x)
# print(frutes)

##################################################################################

x = list(frutes)
x.append("watermelon")
frutes = tuple(x)
print(frutes)

#########################################LooP#########################################

for x in frutes:
    print(x)