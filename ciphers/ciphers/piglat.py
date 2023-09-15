# igpay atinlay

def piglat(cmd: str, mode: bool):
  """pig latin."""
  # divide input by words
  u_input = cmd.split()
  result = ""
  if mode:
    # encrypt word by word
    for i in u_input:
      shift = i[-2:]
      i_sub = i[:-2]
      i_enc = ''.join(shift) + i_sub + "ay"
      result += i_enc + " "
    return result
  else:
    # decrypt
    for i in u_input:
        i_sub = i[:-2]
        i_move = i[:2]
        i_dec = i_sub[2:] + i_move
        result += i_dec + " "

    return result
