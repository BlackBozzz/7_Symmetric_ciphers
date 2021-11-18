from collections import Counter


#-----------------------------------------------------------1-----------------------------------------------------------

def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))


def decrypt(k, c):
    return ''.join(map(chr, [x - k for x in map(ord, c)]))

print("Encripted: ", encrypt(4, "Hello!"))
print("Decripted: ", decrypt(4, encrypt(4, 'Hello!')))


#-----------------------------------------------------------2-----------------------------------------------------------

def hack(c):
    return ''.join(map(chr, [x - abs(ord(" ") - ord(Counter(c).most_common()[0][0])) for x in map(ord, c)]))

print(hack(encrypt(2, "Hello! My name is George, and I like programming")))

#-----------------------------------------------------------3-----------------------------------------------------------

def encryptV(k, m):
    if len(m) > len(k):
        k *= int(len(m) / len(k)) + 1

    k = [ord(char) for char in k]

    return ''.join(map(chr, [x + k[i] for i, x in enumerate(map(ord, m))]))


def decryptV(k, c):
    if len(c) > len(k):
        k *= int(len(c) / len(k)) + 1

    k = [ord(char) for char in k]

    return ''.join(map(chr, [x - k[i] for i, x in enumerate(map(ord, c))]))


print(decryptV("qwerty", encryptV("qwerty", 'Hello, World!')))