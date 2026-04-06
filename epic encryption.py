
def pad(data :bytes) ->bytes :
    blocksize = 16
    padding = blocksize - (len(data) % blocksize)
    lil = bytes([padding] * padding)
    return data + lil

def unpad(data :bytes) -> bytes:
    blocksize =16



