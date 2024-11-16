ciphertext = open("C:/Users/LG/OneDrive/바탕 화면/컴퓨터 네트워크/ciphertext.txt","r",encoding="UTF-8")
deciphertext = open("C:/Users/LG/OneDrive/바탕 화면/컴퓨터 네트워크/deciphertext.txt","w")

ciphertext_read = ciphertext.read()

table = str.maketrans('qzjxkwvybfupgmhdclsortnaie', 'abcdefghijklmnopqrstuvwxyz')
deciphertext_read = ciphertext_read.translate(table)
print(deciphertext_read, file = deciphertext, flush = True)

ciphertext.close()
deciphertext.close()
