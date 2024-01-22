def morse_translator(text):
  
  string=input(morse_code_equivalent)
  
  morse_code_dict={
   "A": ".-",
   "B": "-...",
   "C": "-.-.",
   "D": "-..",
   "E": ".",
   "F": "..-.",
   "G": "--.",
   "H": "....",
   "I": "..",
   "J": ".---",
   "K": "-.-",
   "L": ".-..",
   "M": "--",
   "N": "-.",
   "O": "---",
   "P": ".--.",
   "Q": "--.-",
   "R": ".-.",
   "S": "...",
   "T": "-",
   "U": "..-",
   "V": "...-",
   "W": ".--",
   "X": "-..-",
   "Y": "-.--",
   "Z": "--..",
}

morse_translator(string,morse_dict)

text_upper=text.upper()

morse_code_list=[]
for char in text_upper:
    if char.isalpha():
       morse_code_list.append(morse_code_list[char])
    elif char=="  ":
       morse_code_list.append("/")
morse_code_result=" ".join(morse_code_list)



print(
   morse_translator("HELLO WORLD")

)
