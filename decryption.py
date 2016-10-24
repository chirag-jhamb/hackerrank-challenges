# Complete the function below. Decrypt the e_msg by reducing it's ascii value by K, given that input is only A-Z.


def  decrypt(e_msg, k):
    k=k%26
    a=[]
    #o=list(e_msg)
    for i in e_msg:
        i=ord(i)
        i=i-k
        if i<65:
            i=i+26

        i=chr(i)
        a.append(i)
    x=''.join(i for i in a)
    return x
