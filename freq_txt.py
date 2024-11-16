inFile = open("C:/Users/LG/OneDrive/바탕 화면/파이썬 기말 과제/파이썬기말과제.txt","r", encoding="UTF-8")
inFile_read = inFile.read().lower()
inFile.close()

Alphabet = 'abcdefghijklmnopqrstuvwxyz'

inFile_freq = [0] * 26

for ch in inFile_read:
    if ch in Alphabet:
        idx = Alphabet.find(ch)
        inFile_freq[idx] += 1

print("원문 파일에 대한 알파벳 빈도수")
for i in range(0,26):
    print(Alphabet[i], ":", inFile_freq[i])

print("원문 파일에 대한 알파벳 빈도수 오름차순 정렬")

freqPairs = list(zip(Alphabet, inFile_freq))
freqPairs.sort(key = lambda _ : _ [1], reverse=False)

outFile = open("C:/Users/LG/OneDrive/바탕 화면/컴퓨터 네트워크/key.txt","w")
for letter, count in freqPairs:
    print(letter, ':', count, file=outFile, flush=True)
outFile.close()

##letter, count = zip(*freqPairs)  ## list(zip(Alphabet, inFile_freq) 묶은 거 다시 풀어줘서
##print(letter)  ## letter만 출력

##letter_List = list(letter)  ## 튜플이었던 letter를 리스트로 변환
##print(letter_List)

##letter_str = str(letter_List)

##for i in range(0,26):
    ##print(letter_List[i])  ## 기존 letter_List[i] 출력
    ##letter_List[i] = Alphabet[i]
    ##print(letter_List[i])  ## 변환 후 letter_List[i] 출력




