def substitution_codebook():
    encbook = {'a':'q','b':'z','c':'j','d':'x','e':'k','f':'w','g':'v','h':'y','i':'b','j':'f','k':'u','l':'p',
               'm':'g','n':'m','o':'h','p':'d','q':'c','r':'l','s':'s','t':'o','u':'r','v':'t','w':'n','x':'a',
               'y':'i','z':'e',' ':' ','0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',
               '9':'9','[':'[',']':']','&':'&','(':'(',')':')','-':'-','_':'_','|':'|',':':':',';':';','"':'"',
               ',':',','.':'.','/':'/','?':'?','\n':'\n','%':'%',"'":"'",'=':'=','+':'+','{':'{','}':'}','\\':'\\',
               '$':'$','\t':'\t','@':'@','®':'®'}

    decbook = {}

    for k in encbook:
        temp = encbook[k]
        decbook[temp] = k

    return encbook, decbook


def encrypt(msg1, encbook):
    temp = ""
    for c in msg1:
        c = encbook[c]
        temp += c
    return temp


def decrypt(msg2, decbook):
    temp = ""
    for c in msg2:
        c = decbook[c]
        temp += c
    return temp


if __name__ == '__main__':
    original = open("파이썬기말과제.txt","r",encoding="UTF-8")
    plaintext = original.read().lower()
    original.close()

    encbook, decbook = substitution_codebook()

    ciphertext = encrypt(plaintext, encbook)
    print("암호화 : ", ciphertext)

    deciphertext = decrypt(ciphertext, decbook)
    print("복호화 : ", deciphertext)
