"""
todo message&&key -> cipher, cipher&&key -> message 
todo need ciper interpretor -- and gates two binary strings together
"""

from operator import truediv
import random

message = [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0]


key = []
trial = 0

def random_bit():
    return random.randint(0, 1)

def random_basis():
    basis_boolean = bool(random.getrandbits(1))
    if(basis_boolean):
        return "HV basis"
    return "+- basis"

def measure(sender_basis, receiver_basis, bit):
    if(sender_basis == receiver_basis):
        return bit
    return random.randint(0, 1) # If bases are different, random value will be measured

def should_keep(sender_basis, receiver_basis):
    if(sender_basis == receiver_basis):
        return True
    return False

def get_cipher(msg, key):
    out = []
    for i in range(len(msg)):
        out[i] = (msg[i] == 1) and (key[i] == 1)
    return out



while len(key) < 11:
    trial += 1
    print("trial #", trial)

    # Random bit that Alice chooses
    alice_bit_value = random_bit()
    print("alice random bit: ", alice_bit_value)

    # Random basis that Alice chooses
    # True = horizontal/vertical basis
    # False = diagonal/anti-diagonal basis
    alice_basis = random_basis() 
    print("alice basis: ", alice_basis)

    # Random basis that Bob chooses
    # True = horizontal/vertical basis
    # False = diagonal/anti-diagonal basis
    bob_basis = random_basis()
    print("bob basis: ", bob_basis)

    # Bob measures the basis
    measured_bit = measure(alice_basis, bob_basis, alice_bit_value)
    print("bob's measured bit: ", measured_bit)

    # Alice announces basis; Bob chooses whether to keep bit or not
    print("alice announces her basis as ", alice_basis)
    if(should_keep(alice_basis, bob_basis)):
        print("bob keeps the bit!")
        key.append(measured_bit)
    else:
        print("bob did not keep the bit!")
    print("\n")

print(key)

