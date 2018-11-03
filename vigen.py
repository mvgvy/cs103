def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    w = [i for i in plaintext]
    k = [i for i in keyword*(len(plaintext)//len(keyword)+1)]
    ciphertext = ''
    for i in range(len(w)):
        cs = ord(w[i])
        ck = ord(k[i])
        if 65 <= ck <= 90:
            ck -= 65
        elif 97 <= ck <= 122:
            ck -= 97
        if 65 <= cs <= 90 - ck or 97 <= cs <= 122 - ck:
            w[i] = chr(cs + ck)
        elif 90 - ck < cs <= 90 or 122 - ck < cs <= 122:
            w[i] = chr(cs + ck - 26)
        ciphertext += w[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    w1 = [i for i in ciphertext]
    k1 = [i for i in keyword * (len(ciphertext) // len(keyword) + 1)]
    ciphertext = ''
    for i in range(len(w1)):
        cs1 = ord(w1[i])
        ck1 = ord(k1[i])
        if 65 <= ck1 <= 90:
            ck1 -= 65
        elif 97 <= ck1 <= 122:
            ck1 -= 97
        if 65 + ck1 <= cs1 <= 90 or 97 + ck1 <= cs1 <= 122:
            w1[i] = chr(cs1 - ck1)
        elif 65 <= cs1 < 65 + ck1 or 97 <= cs1 < 97 + ck1:
            w1[i] = chr(cs1 - ck1 + 26)
        ciphertext += w1[i]
    return ciphertext
