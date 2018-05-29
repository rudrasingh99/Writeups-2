enc = [0xD0, 0xE0, 0xAB, 0x9C, 0xCD, 0x78, 0x5B, 0x54, 0x3D, 0xE4, 0xEA, 0x33, 0x51, 0x44, 0x6D, 0x3C, 0x4E, 0xCE, 0xDF, 0xB5, 0x41, 0x00, 0x1C, 0xEC, 0xE3, 0x1B, 0xC3, 0x8C, 0x91, 0x25, 0x7F, 0x1B, 0x60, 0xFE, 0x35, 0x9C, 0xEA, 0x04, 0x4C, 0x87, 0x8D, 0x97, 0x93, 0x5C, 0xB8, 0x9A, 0x70, 0x75]

for i in range(0, len(enc)):
    enc[i] = hex((119 - i) ^ enc[i] ^ (8 - i % 8))

dec = []

for i in range(0, len(enc)/8):
    char = '0x'
    for j in range(8):
        tmp = enc[i*8+j][2:]
        if len(tmp) == 1: tmp = '0' + tmp
        char += tmp
    dec.append(char)

print dec

# Output: ['0xaf91d8edba092825', '0x5a8d815a3e2d0655', '0x21afbcd426617f8d', '0xb44298d5ce7c2442', '0x3faf66cdbd551fd6', '0xcaded815f7d33b3c']