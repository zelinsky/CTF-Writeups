import itertools

def string_xor(s, key):
    key = key * (len(s) / len(key) + 1)
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in itertools.izip(s, key)) 


f = 'dHNkdktUAFMBA1MIBglWBgkFCFEGBQlUCQRRBAgIBgQAVVRUAwkEBFEAAVRVVVRTBFRWBQdUBlMAB1YJVQYIBwIIBFVSTQ=='
