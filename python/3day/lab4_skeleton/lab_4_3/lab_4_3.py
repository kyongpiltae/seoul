## 알파벳 소문자와 빈칸만 iuput으로 주어진다 가정합니다.
import numpy as np

# ========== EDIT HERE ==========
# TODO : 인코딩, 디코딩 할때 쓸 자료형
alphabet = np.arange(0,27)
I_alphabet = np.identity(26)

abc = "abcdefghijklmn"
char_to_int = dict(((k,v)for k,v in enumerate(abc)))
int_to_char = dict(((k,v)for k,v in enumerate(abc)))
# ===============================

def encoding(data):
    ######################################
    # TODO :  encoding 함수를 구현하시오.  
    #         [Input]
    #         - data : (type : string)  
    #  
    #         [output]
    #         - encoded : (type : array, size of [len(data), len(alphabet)]) encoding result.  
    # ========== EDIT HERE ==========
    rlist = list()
    for d in data:
        t = ord(d)-ord('a')
        if(t < 0):
            t= 26
      
        rlist.append(t)
    

    encoded=np.zeros((len(data),len(alphabet)))
    index = 0
    for r in rlist:
        encoded[index,r]=1
        index += 1

    # ===============================
    return encoded

def decoding(data):
    ######################################
    # TODO :  decoding 함수를 구현하시오.  
    #         [Input]
    #         - data : (type : array, size : [len(data), len(alphabet)])  
    #  
    #         [output]
    #         - decoded : (type : string) decoding result.  
    # ========== EDIT HERE ==========
  
    # ===============================
    decoded = []
    for row in data:
        temp = np.argmax(row)
        ch=""
        if temp == 26:
            ch = " "
        else:
            ch = chr(temp+ord('a'))
        print("ch == " , ch," ", temp)
        decoded.append(ch)
         
    return decoded
    
if __name__ == '__main__':
    data = 'data scientist'
    
    encoded = encoding(data)
    decoded = decoding(encoded)

    print(encoded)
    print(decoded)

