# DES tables just reorder bits; they're from the original hardware design.

IP = [58,50,42,34,26,18,10,2, 60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6, 64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,  59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5, 63,55,47,39,31,23,15,7]

FP = [40,8,48,16,56,24,64,32, 39,7,47,15,55,23,63,31,
      38,6,46,14,54,22,62,30, 37,5,45,13,53,21,61,29,
      36,4,44,12,52,20,60,28, 35,3,43,11,51,19,59,27,
      34,2,42,10,50,18,58,26, 33,1,41,9,49,17,57,25]

# Expansion table: expands 32-bit R into 48 bits.

E = [32,1,2,3,4,5, 4,5,6,7,8,9, 8,9,10,11,12,13,
     12,13,14,15,16,17, 16,17,18,19,20,21,
     20,21,22,23,24,25, 24,25,26,27,28,29, 28,29,30,31,32,1]

# P-box: permutes the 32-bit S-box output.

P = [16,7,20,21,29,12,28,17, 1,15,23,26,5,18,31,10,
     2,8,24,14,32,27,3,9, 19,13,30,6,22,11,4,25]

# Key schedule: PC-1 drops parity bits; PC-2 picks 48 bits for each round.

PC1 = [57,49,41,33,25,17,9, 1,58,50,42,34,26,18,
       10,2,59,51,43,35,27, 19,11,3,60,52,44,36,
       63,55,47,39,31,23,15, 7,62,54,46,38,30,22,
       14,6,61,53,45,37,29, 21,13,5,28,20,12,4]

PC2 = [14,17,11,24,1,5, 3,28,15,6,21,10, 23,19,12,4,
       26,8,16,7,27,20,13,2, 41,52,31,37,47,55,
       30,40,51,45,33,48, 44,49,39,56,34,53,
       46,42,50,36,29,32]
# Key left-rotations for each round (C and D halves).

shifts = [1,1,2,2,2,2,2,2, 1,2,2,2,2,2,2,1]

# S-boxes: 6-bit input → 4-bit output; they add DES’s non-linear strength.

S = [
    # S1
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],

    # S2
    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
     [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
     [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
     [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],

    # S3
    [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
     [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
     [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
     [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],

    # S4
    [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
     [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
     [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
     [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],

    # S5
    [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
     [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
     [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
     [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],

    # S6
    [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
     [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
     [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
     [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],

    # S7
    [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
     [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
     [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
     [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],

    # S8
    [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
     [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
     [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
     [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]

def permute(block, table):
    return [block[i-1] for i in table]
#Takes a list of bits
#Rearranges them according to a permutation table.

def left_shift(bits, n):
    return bits[n:] + bits[:n]
#Rotates the list left by n positions.
#Used to rotate C and D in the key schedule.

def sbox_substitution(bits):
    output = []
    for i in range(8):
        block = bits[i*6:(i+1)*6]
        row = block[0]*2 + block[5]
        col = block[1]*8 + block[2]*4 + block[3]*2 + block[4]
        val = S[i][row][col]
        output += [int(x) for x in f"{val:04b}"]
    return output
#Splits the 48-bit input into 8 chunks of 6 bits.
#For each 6-bit chunk:
#row comes from first and last bit.
#col comes from the middle 4 bits.
#Looks up S-box value.
#Converts S-box output to 4 binary bits and adds to output.

def des_round(L, R, key):
    expanded = permute(R, E)
    xored = [a ^ b for a, b in zip(expanded, key)]
    sboxed = sbox_substitution(xored)
    permuted = permute(sboxed, P)
    new_R = [a ^ b for a, b in zip(L, permuted)]
    return R, new_R
#Expand R from 32 to 48 bits using table E.
#XOR the expanded R with the round key.
#Pass through S-boxes to go 48 to 32 bits.
#Apply permutation P.
#XOR this result with L to becomes the new R.
#Return (old R becomes new L, new_R becomes new R).

def generate_keys(key64):
    key = permute(key64, PC1)
    C = key[:28]
    D = key[28:]
    keys = []

    for shift in shifts:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        keys.append(permute(C + D, PC2))

    return keys
#Apply PC-1 table to compress 64-bit key to 56 bits.
#Split into C and D halves (28 bits each).
#For each of the 16 rounds:
#Left-shift C and D.
#Combine them.
#Apply PC-2 to get a 48-bit round key.
#Return list of 16 round keys.

def des_encrypt_block(plaintext64, key64):
    block = permute(plaintext64, IP)
    L = block[:32]
    R = block[32:]
    keys = generate_keys(key64)

    for i in range(16):
        L, R = des_round(L, R, keys[i])

    combined = R + L
    return permute(combined, FP)

#Initial Permutation (IP).
#Split into L and R (first 32 bits + last 32 bits).
#Generate round keys.
#Run 16 rounds.
#Swap L and R (Feistel rule).
#Apply Final Permutation (FP).
#Return encrypted 64-bit block.

def des_decrypt_block(ciphertext64, key64):
    block = permute(ciphertext64, IP)
    L = block[:32]
    R = block[32:]
    keys = generate_keys(key64)[::-1]

    for i in range(16):
        L, R = des_round(L, R, keys[i])

    combined = R + L
    return permute(combined, FP)
#Same as encryption but keys are reversed.

def hex_to_bits(h):
    return [int(b) for b in bin(int(h,16))[2:].zfill(64)]
#Takes a hex string.
#Converts it to binary.
#Pads it to 64 bits.
#Returns list of 0/1 bits.

def bits_to_hex(b):
    return hex(int("".join(str(x) for x in b), 2))[2:].upper()
#Turns list of bits into a string.
#Converts binary → hex.
#Removes "0x" and uppercases it.

# A standard DES test vector:
# •	Key: 133457799BBCDFF1
# •	Plaintext: 0123456789ABCDEF
# •	Expected Ciphertext: 85E813540F0AB405
pt = hex_to_bits("0123456789ABCDEF")
key = hex_to_bits("133457799BBCDFF1")

cipher = des_encrypt_block(pt, key)
print("Cipher:", bits_to_hex(cipher))

decrypted = des_decrypt_block(cipher, key)
print("Decrypted:", bits_to_hex(decrypted))

print("Key:", key)