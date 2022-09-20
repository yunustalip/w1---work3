import numpy as np
repeat = False
b = np.zeros((6,8),dtype='int32')
for i in range(0,6):
    for j in range(0,8):
        a = np.random.randint(1,50)
        if(a in b.T[j]):
            repeat = True
        while repeat == True:
            if(a in b.T[j]):
                a = np.random.randint(1,50)
                repeat = True
            else:
                repeat = False
        b[i][j] = a
            
print(b)