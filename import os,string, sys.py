import os,string, sys

print('Current Working Directory: ', os.getcwd())

pt = open('파이썬기말과제.txt', 'rt', encoding='UTF8')
pt_msg = pt.read().lower()
pt.close()
Alphabet = 'abcdefghijklmnopqrstuvwxyz'

pt_freq = [0] * 26
freq_dict = {}
#평문 파일에 대한 알파벳 빈도수 계산
for ch in pt_msg:
    if ch in Alphabet:
        idx = Alphabet.find(ch)
        pt_freq[idx] += 1
#pt_freq.sort(reverse=True)
#빈도수에 의한 알파벳 정렬
for i in range(0,26):
    freq_dict[Alphabet[i]] = pt_freq[i]
    sorted_freq = sorted(freq_dict.items(),key = lambda item: item[1], reverse=True)

print("파일에 대한 알파벳 빈도수")
print(sorted_freq)
f = open('test.txt', 'w',encoding='UTF8')
print(sorted_freq,file=f)# 정렬된 알파벳 텍스트 파일에 저장
f.close()

dict_list = dict(sorted_freq)
list(dict_list.keys())#정렬된 리스트에서 키값만 추출

from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)#알파벳a-z리스트 만들기

decbook = dict(zip(dict_list,alphabet_list))#키값과 알파벳, a-z리스트화
decbook['@'] = ' '# 띄어쓰기에 대한 암호화 리스트에 추가
print(decbook)


#암호화 시작

def makecodebook():#암호화로makecodebook만들기

    encbook = {}
    for k in decbook:
        val=decbook[k]
        encbook[val] = k

    return encbook, decbook

def encrypt(msg, encbook):#메세지를 받아서 암호화
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c])
    return msg

def decrypt(msg, decbook):#메세지를 받아서 복호화
    for c in msg:
        if c in decbook:
            msg  = msg.replace(c, decbook[c])
    return msg

if __name__=='__main__':#
    files = open('파이썬기말과제.txt','rt')
    filecontent=files.read()
    files.close() #미리 입력된 텍스트 파일을 불러와서filecontent에 저장

encbook, decbook = makecodebook()
filecontent = encrypt(filecontent, encbook)#불러온 텍스트 파일에 텍스트 암호화

files = open('파이썬기말과제.txt', 'wt+')
files.write(filecontent)
files.close()#암호화된 텍스트를 새로운 텍스트 파일을 만들어서 저장

filecontent = decrypt(filecontent, decbook)#복호화를 위한 함수 사용

files = open('파이썬기말과제.txt', 'wt+')
files.write(filecontent)
files.close()#복호화된 텍스트를 새로운 텍스트 파일을 만들어서 저장