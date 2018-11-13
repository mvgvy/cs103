def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    num: int = 0
    text: str = ''
    a = []
    b = []
    for i in plaintext:
        i: int = ord(i)
        a.append(i)
    for i in keyword:
        i: int = ord(i)
        if i <= 96:
            i = i - 65  
            b.append(i)
        else:
            i = i - 97  
            b.append(i)
    for i in range(len(a)):
        if a[i] < 91 and a[i] + b[num] > 90:
            a[i] += b[num] - 26
        elif a[i] < 123 and a[i] + b[num] > 122:
            a[i] += b[num] - 26
        else:
            a[i] += b[num]
        num += 1
        if num == len(b):
            num = 0
        a[i] = chr(a[i])
    for i in range(len(a)):
        text += a[i]
    return text


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    num: int = 0
    text: str = ''
    a = []
    b = []
    for i in ciphertext:
        i: int = ord(i)
        a.append(i)
    for i in keyword:
        i: int = ord(i)
        if i <= 96:
            i = i - 65  
            b.append(i)
        else:
            i = i - 97  
            b.append(i)
    for i in range(len(a)):
        if a[i] > 64 and a[i] - b[num] < 65:
            a[i] = a[i]-b[num] + 26
        elif a[i] > 96 and a[i] - b[num] < 97:
            a[i] = a[i]-b[num] + 26
        else:
            a[i] = a[i] - b[num]
        num += 1
        if num == len(b):
            num = 0
        a[i] = chr(a[i])
    for i in range(len(a)):
        text += a[i]
    return text
