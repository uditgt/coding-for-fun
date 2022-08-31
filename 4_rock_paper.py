symbols = {
'rock':
		"""
		    _______
		---'   ____)
		      (_____)
		      (_____)
		      (____)
		---.__(___)
		""",
'paper':
		"""
		     _______
		---'    ____)____
		           ______)
		          _______)
		         _______)
		---.__________)
		""",
'scissor':
		"""
		    _______
		---'   ____)____
		          ______)
		       __________)
		      (____)
		---.__(___)
		"""
}

import numpy as np

user = input('Choose "rock", "paper" or "scissor"?')
if user not in ['rock', 'paper', 'scissor']:
	print('wrong input!')
else:
	print(f'You picked {user}', symbols[user])

	pc = np.random.choice(['rock', 'paper', 'scissor'],1)[0]
	print(f'Computer picked {pc}', symbols[pc])

	if (user=='rock' and pc=='scissor') or \
	   (user=='paper' and pc=='rock') or \
	   (user=='scissor' and pc=='paper'):
	   print('You win!')
	elif user == pc:
		print('Draw')
	else:
		print('You lose!')