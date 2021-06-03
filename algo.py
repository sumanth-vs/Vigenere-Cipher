# Use this script to send encoded msges to user
alpha = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ?.,!-0123456789"\''''
l = len(alpha)

class Message:
	def __init__(self):
		self.keyword = "ThisIsTheKey"
    

	def generateKey(self, string, key):
		key = list(key)
		if len(string) == len(key):
			return(key)
		else:
			for i in range(len(string) -
						len(key)):
				key.append(key[i % len(key)])
		#print(key)print('')
		return("" . join(key))

	def cipherText(self, string, key):
		cipher_text = []
		for i in range(len(string)):
			x = (alpha.find(string[i]) + alpha.find(key[i])) % l
			cipher_text.append(alpha[x])
		#print(cipher_text)
		return("" . join(cipher_text))
		

	def originalText(self, cipher_text, key):
		orig_text = []
		for i in range(len(cipher_text)):
			x = (alpha.find(cipher_text[i]) - alpha.find(key[i]) + l) % l
			orig_text.append(alpha[x])
		return("".join(orig_text))
		

	def createMsg(self, msg, from_person, to_person):
		key = self.generateKey(msg, self.keyword)
		cipher_text = self.cipherText(msg, key)

		a, b = sorted([from_person, to_person])
		f = open('MsgServer\{}and{}.txt'.format(a, b), 'a')
		f.write('{}:'.format(from_person) + cipher_text + '\n')
		f.close()
		#print("Ciphertext :", cipher_text)
		#print("Original/Decrypted Text :", self.originalText(cipher_text, key))

  
