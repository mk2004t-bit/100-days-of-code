from assentials import logo
from assentials import alphabet

print(logo)
rerun = "yes"

def caesar(message,key,encode_or_decode):
      output_text=""
      if encode_or_decode=="decode":
           key*=-1
      for letter in message: 
          if letter not in alphabet:
            output_text+=letter
          else:
            shifted_location = alphabet.index(letter)+key
            shifted_location%=len(alphabet)
            output_text+=alphabet[shifted_location]
      print(f"Here is the {encode_or_decode}d result:  {output_text}\n")

while rerun == "yes":
  type = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
  message = input("Type your message:\n").lower()
  key = int(input("Enter your key:\n"))
  caesar(message,key,encode_or_decode=type)
  rerun=input("Do you want to run it again, say 'yes' or 'no' :\n").lower()
