from Crypto.Cipher import Blowfish

from struct import pack
from base64 import b64encode
import json
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

bs = Blowfish.block_size
key = b'An arbitaryily long key'
cipher = Blowfish.new(key, Blowfish.MODE_CTR)
plaintext = b'docendo discimus'
plen = bs - len(plaintext) % bs
padding = [plen]*plen
padding = pack('b'plen, *padding)
ct_bytes = cipher.encrypt(data)
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'nonce':nonce, 'ciphertext':ct})
print(result)









