def encrypt(msg,key):
    result=""
    for ch in msg:
        base=ord('a')
        result+=chr((ord(ch)-base+key)%26+base)
    return result

def decrypt(s,k):
    res=""
    for c in s:
        base_val=ord('a')
        res+=chr((ord(c)-base_val-k)%26+base_val)
    return res

isnext=True


while isnext:
    user_choice=input("Type 'encode' to encrypt,type 'decode' to decrypt: ")
    user_message=input("Enter your message: ")
    key=int(input("Type the shift number: "))
    if user_choice=='encode':
        print(encrypt(user_message,key))
    if user_choice=='decode':
        print(decrypt(user_message,key))

    one_more=input("Type yes if you want to go again else no: ")
    if(one_more=='yes'):
        isnext=True
    else:
        isnext=False
