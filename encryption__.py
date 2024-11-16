original = open("C:/Users/LG/OneDrive/바탕 화면/컴퓨터 네트워크/파이썬학습후과제를위한텍스트파일.txt","r", encoding="UTF-8")
ciphertext = open("C:/Users/LG/OneDrive/바탕 화면/컴퓨터 네트워크/ciphertext.txt","w")

original_read = original.read().lower()

table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'qzjxkwvybfupgmhdclsortnaie')
ciphertext_read = original_read.translate(table)
print(ciphertext_read, file = ciphertext, flush = True)

original.close()
ciphertext.close()