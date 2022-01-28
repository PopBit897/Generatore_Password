# encyption and decryptor (ead)
# code name is :ctv0.1-a(Cesare test version 0.1-Alpha)
# code by RDAITA2
import string
from typing import MutableSequence
def encryption_cesare(msg,key=7):
    msg_encryption=""
    for car in msg:
        if car in string.ascii_uppercase and string.digits and string.punctuation:
            index = ord(car)+ key
            if index >ord('Z')and(100)and('@'):
                index=index - 26
            msg_encryption+=chr(index)
        else:
            msg_encryption+= car
    return msg_encryption

def decryptor_cesare(msg,key=7):
    msg_decryptor=""
    for car in msg:
        if car in string.ascii_uppercase and string.digits and string.punctuation:
            index = ord(car)- key
            if index <  ord('A')and(100)and('@'):
                index=index +26
            msg_decryptor+=chr(index)
        else:
             msg_decryptor+=car
    return msg_decryptor


