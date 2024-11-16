class Visnere:
    def __init__(self,d,s):         # 대문자로 변경, 띄어쓰기 삭제
        self.password = d.upper()
        self.password = self.password.replace(' ','')
        self.keyword = s.upper()
        self.keyword = self.keyword.replace(' ','')


    def encoding(self):     #암호화 함수
        encoded = ''
        kw_t = ''
        cnt = 0
        pw_len = len(self.password)
        kw_len = len(self.keyword)

        for i in range(0,pw_len):     #kw_t 값 안에 키 값의 알파벳을 원문 길이만큼 저장
            if cnt == kw_len:          # 키 값의 길이가 입력한 수만큼 되면 초기화
                cnt = 0
            kw_t = kw_t + self.keyword[cnt]       # 키 값을 평문의 길이만큼 이어 붙여서 저장
            cnt += 1
       

        for i in range(0,pw_len):     #encoded 변수에 원문에서 암호화가 되는 알파벳을 하나하나씩 중첩하여 저장
            encoded = encoded + mKey(self.password[i],kw_t[i])    # 평문과 키 값 저장

        print('<암호문> : ',end='')
        print(encoded)          #암호화 완성

        self.password = encoded     # 암호화 문장 저장

    def decoding(self): #복호화 함수 
        decoded = ''
        kw_t = ''
        self.keyword = ip_key.upper()         # 입력한 키 값 대문자로 변경 
        self.keyword = self.keyword.replace(' ', '')    # 같은  값 입력 !!
        pw_len = len(self.password)
        kw_len = len(self.keyword)
        cnt = 0

        for i in range(0, pw_len):
            if cnt == kw_len:
                cnt = 0
            kw_t = kw_t + self.keyword[cnt]
            cnt+=1

        for i in range(0, pw_len):    #decoded 변수에 암호화문장에서 복호화가 되는 알파벳을 하나하나 중첩하여 저장
            decoded = decoded + bKey(self.password[i],kw_t[i])   #암호문과 키값 넘김


        print('<복호문> : ',end='')
        print(decoded)

def mKey(src,key):       #비즈네르 암호화 알고리즘
    tmp = ord(src) + ord(key) - 65  # 아스키코드로 계산

    if tmp > 90:
        tmp = tmp - 26

    return chr(tmp)     # 문자로 출력 

def bKey(src,key):       #비즈네르 복호화 알고리즘 (복호화는 암호화의 역순)
    tmp = ord(src) - ord(key) + 65

    if tmp < 65:
        tmp = tmp + 26

    return chr(tmp)



while (True):

                                   #암호화 시작
        textfile = open("파이썬기말과제.txt",'r')
        original = textfile.read()          # 텍스트 파일 읽기
        print('<평문> : ',end='')
        print(original)
        ip_key = input('암호화를 시작합니다. 키를 입력하세요 : ')    #키 값 입력

        som = Visnere(original,ip_key)
        som.encoding()
        textfile.close()
                #복호화
        ip_key = input('복호화를 시작합니다. 키를 입력하세요 : ')   # !! 암호화 키 와 종일 한 키 입력
        som.decoding()         #복호화 함수

        break



    

    
   
