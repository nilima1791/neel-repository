catnames = []

while True :
    print('enter the at name. Press " " to stop')
    name = input()
    if name==' ':
        break
    catnames = catnames + [name]
print('The name of cats are ' )
for name in catnames :
    print(' ' + name)
