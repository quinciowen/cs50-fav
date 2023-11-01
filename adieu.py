import inflect
p = inflect.engine()

names = []

done = False
while done == False:
    try:
        n = input("Name: ")
        names.append(n)
        done = False
    except EOFError:
        child = p.join(names)
        print("Adieu, adieu, to" , child)
        break
