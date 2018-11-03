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
    cod = [i for i in plaintext]
    ciphertext = ''
    for i in range(len(cod)):
        symbol = ord(cod[i])
        if 65 <= symbol <= 87 or 97 <= symbol <= 119:
            cod[i] = chr(symbol + 3)
        elif 88 <= symbol <= 90 or 120 <= symbol <= 122:
            cod[i] = chr(symbol - 23)
        ciphertext += cod[i]
    return ciphertext


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
    cod1 = [i for i in ciphertext]
    plaintext = ''
    for i in range(len(cod1)):
        symbol1 = ord(cod1[i])
        if 68 <= symbol1 <= 90 or 100 <= symbol1 <= 122:
            cod1[i] = chr(symbol1 - 3)
        elif 65 <= symbol1 <= 67 or 97 <= symbol1 <= 99:
            cod1[i] = chr(symbol1 + 23)
        plaintext += cod1[i]
    return plaintext
