#!/bin/python3


def encrypt_char(c, k):
    ci = ord(c)
    l = 'Z' if c.isupper() else 'z'
    o = 'A' if c.isupper() else 'a'

    if ci + k > ord(l):
        return chr(ord(o) + (ci + k - ord(l)) - 1)

    return chr(ci + k)

def caesar_cipher(text, key, decrypt = False):
    if key == 0 or key % 26 == 0:
        return text

    K = key % 26
    return ''.join([encrypt_char(x, K) if x.isalpha() else x for x in text])

_ = int(input().strip())
s = input().strip()
k = int(input().strip())

print(caesar_cipher(s, k))
