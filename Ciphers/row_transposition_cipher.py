import random
import collections

enctxt = collections.namedtuple('Encrypted_Text', ['key', 'cipher', 'extra'])
	
def ciphering(plain_text, columns):
	matrix = list()
	row = list()

	dex = 0

	for ch in message:
		#print(ch)
		row.append(ch)
		
		dex += 1
		
		if dex == columns:
			dex = 0
			matrix.append(row)
			
			row = list()
			
	extra = 0
			
	if len(row) > 0:
		while len(row) < columns:
			row.append(alphabets[random.randint(0, 25)])
			extra += 1
			
	matrix.append(row)
	 
	for i in matrix:
		print(i)
		
	key = ""
		
	for i in range(1, columns+1):
		key += str(i)
		
	key = ''.join(random.sample(key, len(key)))
	
	#print("Key: " + key)
	
	cipher = ""
	
	for i in key:
		for j in range(0, len(matrix)):
			cipher += str(matrix[j][int(i)-1])
	
	#print("Cipher text: " + cipher)
	
	encrypted = enctxt(key, cipher, extra)
	
	return encrypted
	
def deciphering(encrypted, columns):
	original_text = ""
	matrix = list()
	
	rows = int(len(encrypted.cipher)/columns)
	
	for i in range(0, rows):
		n = list()
		
		for j in range(0, columns):
			n.append('-')
			
		matrix.append(n)
		
	dex = 0
		
	for i in encrypted.key:
		for j in range(0, rows):
			matrix[j][int(i)-1] = encrypted.cipher[dex]
			dex += 1
		
	for i in range(0, rows):
		for j in range(0, columns):
			original_text += matrix[i][j]
			
	return original_text[:-encrypted.extra]
	
message = "attackpostponeduntiltwoam"

alphabets = list()

for i in range(97, 123):
    alphabets.append(chr(i))

columns = int(input("Enter number of columns for Rail Fence Cipher: "))

encrypted = ciphering(message, columns)

print("Key: " + encrypted.key)
print("Encrypted Message: " + encrypted.cipher)

original_text = deciphering(encrypted, columns)

print("Original Message: " + original_text)
