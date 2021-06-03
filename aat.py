from algo import Message,alpha,l
from random import randint
from time import sleep

   
class AAT:
  def __init__(self,a):
    self.algorithm=Message()
    self.a=a



  def break_cipher(self,cipher_text):
    for i in range(1, len(cipher_text)):
      if cipher_text[:i] == cipher_text[i:i+i]:
        return i

  #Simulate Conversation between Radcheal and David
  def simulateConversation(self, a):
    a = self.a.replace('A: ', '').replace('B: ', '').split('\n')
    a = [word for word in a if word]


    m = Message()
    f = 'racheal'
    t = 'david'
    for _ in range(10):
        m.createMsg(a[randint(0, len(a)-1)], f, t)
        f, t = t, f
        sleep(3)

    print('Done. Conversation Intercepted..!!!\n')

  #Send 'AAAA...' to the server to get codeworded key
  def chosenPTAttack(self):
    self.m = Message()
    self.msg = 'A'*100
    print("Sending Message 'AAAAAAAAAAA...' from  me->you\n")
    self.m.createMsg(self.msg, 'me', 'you')

  #read codeword from 'meandyou.txt' and get the keyword
  def decode_key(self):
    f = open('MsgServer\meandyou.txt', 'r')
    self.cipher = f.read()
    f.close()
    _, self.cipher = self.cipher.split(':')

    # Key is here
    self.key = self.cipher[:self.break_cipher(self.cipher)]
    sleep(3)
    print('Succesfully retreived key: ',self.key,'\n')
  
  # Read the codeworded message between racheal and david + decode it
  def decode_message(self):
    # Read msges of Others
    # a = 'racheal'
    # b = 'david'
    # filename = 'MsgServer\{}and{}.txt'.format(*sorted([a, b]))
    filename = 'MsgServer\davidandracheal.txt'
    f = open(filename, 'r')
    cipher = f.read()
    f.close()

    for msg in cipher.split('\n'):    
      if not msg:
        break
      f, m = msg.split(':')
      print(f,':', self.algorithm.originalText(m, self.algorithm.generateKey(m ,self.key)), '\n')
