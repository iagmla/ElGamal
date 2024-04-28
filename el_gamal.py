from Crypto.Util import number

def gen_pub_params(psize):
    modulus = number.getPrime(psize)
    pub_point = number.getRandomRange(1, modulus - 1)
    #while not number.isPrime(pub_point):
    #    pub_point += 1
    return pub_point, modulus

def gen_priv_key(modulus):
    return number.getRandomRange(1, modulus - 1)

def gen_pub_key(priv_key, pub_point, modulus):
    return pow(pub_point, priv_key, modulus)

def encrypt(msg, pub_key, pub_point, modulus):
    ephemeral_key = number.getRandomRange(1, modulus - 1)
    ctxt1 = pow(pub_point, ephemeral_key, modulus)
    ctxt2 = (msg * pow(pub_key, ephemeral_key, modulus)) % modulus
    return ctxt1, ctxt2

def decrypt(ctxt1, ctxt2, priv_key, modulus):
    ptxt1 = pow(ctxt1, priv_key, modulus)
    ptxt3 = (ctxt2 * number.inverse(ptxt1, modulus)) % modulus
    return ptxt3

msg = 123
pub_point, modulus = gen_pub_params(128)
priv_key = gen_priv_key(modulus)
pub_key = gen_pub_key(priv_key, pub_point, modulus)

ctxt1, ctxt2 = encrypt(msg, pub_key, pub_point, modulus)
ptxt = decrypt(ctxt1, ctxt2, priv_key, modulus)
print(ptxt)
