'''
Autora: Anaid Jimenez
Rainbow Table
'''

import hashlib
import numpy as np
import pandas as pd

'''
Autora: Anaid Jimenez Moreano
Mucc Ciberseguridad 2023
'''

def sacaletras(hash):
    arr=[]
    x = list(hash)

    '''condicion = np.x '0','1','2','3','4','5','6','7','8','9'
    arr= np.extract(condicion, x)
    print(arr)'''

    for xi in x:
        if xi in ['0','1','2','3','4','5','6','7','8','9']:
            arr.append(xi)

    var = arr[0:8]
    varb = ''.join(var)
    #print(arr)
    return varb


def comparahash(hashe):
    df = pd.read_csv('pashash.txt', sep=",", names=['Iteracion','Password','Hash','Reduccion'])
    #print(df)
    #aa= print(df.where(df['Hash'] == hashe))
    aa=print(df.loc[df['Hash'] == hashe])

    return aa

if __name__ == '__main__':

    password = "12345678"
    for i in range (10):
        a=hashlib.md5(password.encode()).hexdigest()
        b=sacaletras(a)
        #print(''.join(varb))
        vara = a
        varb = b
        #print(b+"\n")
        lines = varb
        with open('pashash.txt', 'a') as f:
            #f.writelines("Iteracion: "+str(i)+", Password:"+password+","+ "\nHash: "+vara+" Reduccion: "+lines+"\n")
            f.writelines(str(i) + "," + password + "," + vara + "," + lines + "\n")
        password=varb

    print("Listo tabla Rainbow\n")

    hasabuscar='dcb6e421398149b95a024de987d335f0'
    print("Buscar hash: "+ hasabuscar)
    comparahash(hasabuscar)