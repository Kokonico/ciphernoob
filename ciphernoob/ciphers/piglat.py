from ciphernoob import __utils

# igpay atinlay


def piglat(cmd: str, mode: bool):
    """pig latin."""
    # divide input by words
    u_input = cmd.split()
    result = []
    if mode:
        # encrypt
        for i in u_input:
            result.append(i[1:] + i[0] + "ay")
    else:
        # decrypt
        for i in u_input:
            result.append(i[-3] + i[:-3])
    
    return ' '.join(result)
