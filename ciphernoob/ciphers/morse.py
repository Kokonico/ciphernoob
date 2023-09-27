from ciphernoob import __utils


def morse(message, mode):
  translations  = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E": ".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    " ": "/ ",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----"
    
  }
  result = []

  if mode:
    # encryption
    for i in message.upper():
      result.append(translations[i])
    return ' '.join(result)
  else:
    # decryption
    words = message.split("/ ")
    for i in words:
      letters = i.split()
      word = []
      for n in letters:
        word.append(__utils.find_key(translations, n))
      result.append(''.join(word))
    return ' '.join(result).lower()