# Uses enhanced skew tent map 
def rand(x,b):
    assert((0<x<1) and (0<b<0.5 or 0.5<b<1))
    while True:
        yield x
        if x<=b:
            x=((x/b)*(10**5))%1
        else:
            x=(((1-x)/(1-b))*(10**5))%1


def key(x,b,n):
    R=rand(x,b)
    while True:
        arr=[next(R) for _ in range(n)]
        s=sorted(arr)
        seed=s.index(arr[0])
        keys=[arr.index(s[i]) for i in range(n)]

        yield (keys,seed)


def encryptChannel(keyGen,p):
    keys,seed=next(keyGen)
    cipher=[0]*len(p)
    new_index=seed^p[0]

    for i in range(len(p)):
        cipher[i]=keys[new_index]
        if i<len(p)-1: 
            new_index=p[i+1]^cipher[i]

    return cipher


def decryptChannel(keyGen, cipher):
    imgLen=len(cipher)
    keys,seed=next(keyGen)
    p=[0]*imgLen

    for i in range(imgLen-1,0,-1):
        new_index=keys.index(cipher[i])
        p[i]=new_index^cipher[i-1]
    p[0]=(keys.index(cipher[0]))^seed

    return p

def split_image(imgData):
    i0 = list(map(lambda x: (x[0]&63,x[1]&63,x[2]&63),imgData))
    i1 = list(map(lambda x: (x[0]&192,x[1]&192,x[2]&192),imgData))
    return (i0,i1)



if __name__ == "__main__":
    k=key(0.6877,0.2667,4)
    kD=key(0.6877,0.2667,4)
    o_p=[1,2,3,0]
    print("Original P: ",o_p)
    c=encryptChannel(k,o_p)
    print("Cipher: ",c)
    p=decryptChannel(kD,c)
    print("Decrypted P: ",p)