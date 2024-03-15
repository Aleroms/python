def encrypt(text, shift):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    #check boundaries
    if new_position > len(alphabet):
      new_position = new_position - len(alphabet)
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"Here is the encoded result: {cipher_text}")

def decrypt(text, shift):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift
    #check boundaries
    if new_position < 0:
      new_position = new_position + len(alphabet)
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"Here is the decoded result: {cipher_text}")

def validateInput(text,prompt,options):
  while True:
    choice = input(prompt).lower()
    if choice in options:
      return choice
    else:
      print("Invalid input")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continueCypher = "yes"
continueCypherPrompt = "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
directionPrompt = "Type 'encode' to encrypt, type 'decode' to decrypt:\n"

while continueCypher == "yes":
  direction = validateInput("",directionPrompt,["encode","decode"])
  text = input("Type your message:\n").lower()
  
  shift = int(input("Type the shift number:\n"))

  if direction == "encode":
    encrypt(text, shift)
  else:
    decrypt(text, shift)
  continueCypher = input(continueCypherPrompt)
  continueCypher = validateInput(continueCypher,continueCypherPrompt,["yes","no"])
