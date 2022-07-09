import time

helloList = ['H','e','l','l','o',' ','w','o','r','l','d']

runOrNot = True

while runOrNot == True:
    for i in range(len(helloList)):
        print(helloList[i])
        time.sleep(0.1)
    print(" ")