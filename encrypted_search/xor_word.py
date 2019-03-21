def xor_word(enc_w: bytes, t_stream: bytes):
    xor_list = []
    for w, t in zip(enc_w, t_stream):
        xor_list.append(w ^ t)

    return bytes(xor_list)
