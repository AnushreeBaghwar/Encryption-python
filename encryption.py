# msg = "Hi there, How are you?"
# key  = "x"
# chr = int to text
# ord = text to int

def enc(msg,key):
	m=""
	i=0
	for char in msg:
		m+=chr(ord(char)+ord(key[i]))
		i+=1
		if(i==len(key)):
			i=0
	return m

def dc(cptext,key):
	m=""
	i = 0
	for char in cptext:
		m+=chr(ord(char)-ord(key[i]))
		i+=1
		if(i==len(key)):
			i=0
	return m

def bitEnc(text,key):
	m=""
	for char in text:
		for k in key:
			char = chr(ord(char)+ord(k))
		m+=char
	return m

def bitDec(cipherText,key):
	m=""
	for char in cipherText:
		for k in key:
			char = chr(ord(char)-ord(k))
		m+=char
	return m





import io
filename = "how to hack dino.txt"
def encryptFile(filename,key):
	file = open(filename,"r")
	filedata= file.read()
	filedata = bitEnc(str(filedata),key)
	file.close()
	with io.open(filename,"w",encoding = "utf-8") as f:
		f.write(filedata)


def decryptFile(filename,key):
	with io.open(filename,"r",encoding="utf-8") as f:
		filedata = f.read()
	with io.open(filename,"w",encoding="utf-8") as f:
		f.write(bitDec(filedata,key))
def readFile(filename):
	with io.open(filename,"r",encoding = "utf-8") as f:
		print(f.read())
readFile(filename)

encryptFile(filename,"key")
decryptFile(encryptFile,"key")

readFile(filename)





# print("text before encryption ",msg)

# eText = enc(msg,"text")

# print("encrypted text",eText)

# dText = dc(eText,"text")

# print("text after decryption ",dText)









