a = '''A: Hi miss, how are you today? Are you checking in?

B: Yes, I had a room reserved under the name Rebecca

A: Oh ok, let me check. Oh great I found your reservation, you are in room 207.

B: Great so here are your keys and we have a complimentary continental breakfast between 7am and 10am in the lobby. Would you like a hand bringing those bags up to your room? Our bellhop can take those for you.

A: Sure, that would be great.

B: Enjoy your stay with us.

A: Hi, what’s your name?

B: I’m Jenny. You?

A: Oh I’m Akiko. It’s great to meet you. So where are you from?

B: I’m from New York. I am in Tokyo for a 10-day work trip.

A: How do you like Japan so far?

B: Oh my gosh, I never imagined the food would be this great and I’m having a blast.

A: Cool!  Are you getting a lot of time to explore outside of work?

B: Yeah, I am in the office during the day, we have a Tokyo office but I get out around 5pm every evening so I have been going all around the city on my own.

A: Well some friends and I are having a cherry blossom party this weekend at Yoyogi Park. Would you be interested in joining us?

B: That sounds awesome. Do you want to send me a text later in the week and let me know the time and the address?

A: Will do.  See you this weekend!

A: Lindsay, what are you doing?

B: Oh I’m trying to figure out how to make this microphone work better. It sounds kind of strange.

A: What do you mean?  I think it sounds fine.

B: Do you know what my friend said? He’s an audio expert and he said that we need to improve it. I don’t know, what do you think?

A: I think it’s OK.'''


from aat import AAT
from os import remove
from os import path
from time import sleep

print()
print('*'*60)
input('Welcome to Vigenère Cipher: Please press "Enter" to continue')

#remove old files
if path.isfile('MsgServer\meandyou.txt'):
  remove('MsgServer\meandyou.txt')
if path.isfile('MsgServer\davidandracheal.txt'):
  remove('MsgServer\davidandracheal.txt')

#capture conversaton between David and Racheal(in codeword)
aatt = AAT(a)
print('Capturing Conversation...')
aatt.simulateConversation(a)

#Get the KEY (in codeword) using CPT Attack
input('Press Enter to use CPTAttack')
print('Initaiting Chosen Plain Text Attack to find the KEY:')
aatt.chosenPTAttack()
aatt.decode_key()

#decipher the conversation
input('Press Enter to decode the messages!')
print('\n')
print('*'*20,'Messages','*'*20)
aatt.decode_message()
print('*'*20,'Messages','*'*20)
