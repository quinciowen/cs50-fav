str = input("camelCase: ")

newText=""
for i in range(len(str)):
    if str[i].isupper():
        newText = newText +"_" +str[i].lower()
    else:
        newText = newText + str[i]
print("snake_case:",newText)
