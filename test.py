def get_cipher(msg, key):
    out = []
    for i in range(len(msg)):
        out.append((msg[i] == 1) and (key[i] == 1))
    return out

message_list = [0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
key_list = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
cipher_list = get_cipher(message_list, key_list)
print(cipher_list)