import pyperclip

while True:
	inp = input('Symbol to copy: ')
	inp = inp.lower()
	if inp in ['floor', 'fl']:
		pyperclip.copy('⌊ ⌋')
	elif inp in ['ceil', 'cl', 'ceiling']:
		pyperclip.copy('⌈ ⌉')
	elif inp in ['shrug', 'idk']:
		pyperclip.copy('¯\_(ツ)_/¯')
	elif inp in ['alpha', 'a']:
		pyperclip.copy('α')
	elif inp in ['beta', 'b']:
		pyperclip.copy('β')
	elif inp in ['epsilon', 'e']:
		pyperclip.copy('ε')
	elif inp in ['theta', 'th']:
		pyperclip.copy('θ')
	elif inp in ['mew', 'mu']:
		pyperclip.copy('μ')
	elif inp in ['pi']:
		pyperclip.copy('π')
	elif inp in ['func', 'f', 'function']:
		pyperclip.copy('ƒ')
	elif inp in ['all', 'univ','forall']:
		pyperclip.copy('∀')
	elif inp in ['exists', 'thereis', 'hay']:
		pyperclip.copy('∃')
	elif inp in ['subset']:
		pyperclip.copy('⊆')
	elif inp in ['empty', 'emptyset']:
		pyperclip.copy('∅')
	elif inp in ['element', 'in']:
		pyperclip.copy('∈')
	elif inp in ['sqr', 'root']:
		pyperclip.copy('√')
	elif inp in ['inf', 'infinity']:
		pyperclip.copy('∞')
