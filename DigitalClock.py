import time
import datetime

list = [
    '''
     ____
    |    |
    |    |
    |    |
     ____''',
    '''
    
    |
    |
    |
    |''',

    '''
    ____
        |
    ____|
   |
   |____
   ''',
    '''
    ____
        |
    ____|
        |
    ____|    
        ''',
    '''
   
   |    |
   |____|
        |
        |
   ''',
    '''
     _____
    |
    |____
         |
     ____|
         ''',
    '''
    ____
   |
   |____
   |    |
   |____|
    ''',
    '''
    ____
        |
        |
        |
        |''',
    '''
     ____
    |    |
    |____|
    |    |
    |____|''',
    '''
    ____
   |    |
   |____|
        |
        |'''
]
colon = '''


o

o'''

done = True
while (done):

    ti = str(datetime.datetime.now())
    ti = ti[11:19]

    lines = ["", "", "", "", "", "", "", "", ""]
    line = 0

    numbers = [[], [], [], [], [], [], [], []]
    for x in range(8):
        if ti[x].isdigit():
            numbers[x] = list[int(ti[x])].splitlines()
        elif ti[x] == ":":
            numbers[x] = colon.splitlines()

    for x in range(9):
        temp = ""
        for i in range(9):
            try:
                if i != 8:
                    temp += str(numbers[i][line]).ljust(10)
            except:
                temp += "    "
        lines[x] += temp
        line += 1

    for x in range(9):
        print(lines[x])

    time.sleep(1)