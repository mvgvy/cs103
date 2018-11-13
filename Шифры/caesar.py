def encrypt_caesar(plaintext: str) -> str: 
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    text:str = ''
    for symbol in plaintext:
        scode:int = ord(symbol)
        if 64 < scode < 91:
            if scode + num > 90:
                text += chr((scode + num - 90) + 64)
            else:
                text += chr(scode + num)
        elif 96 < scode < 123:
            if scode + 3 > 122:
                text += chr((scode + num - 122) + 96)
            else:
                text += chr(scode + num)
        else:
            text += symbol
    return text



def decrypt_caesar(ciphertext: str) -> str:
    """
    Decrypt the message with Caesar cipher
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    text:str = ''
    for sym in ciphertext:
        scode:int = ord(sym)
        if 64 < scode < 91:
            if scode - num < 65:
                text += chr(91 - (65 - scode + num))
            else:
                text += chr(scode - num)
        elif 96 < char < 123:
            if scode - num < 97:
                text += chr(123 - (97 - scode + num))
            else:
                text += chr(scode - num)
        else:
            text += sym
    return text
