from random import shuffle
from string import punctuation

alphabet = "abcdefghijklmnopqrstuvwxyz" + punctuation + "0123456789"
List = list(alphabet)
shuffle(List)


def HashLetter(args):
    encode_trans = str.maketrans(dict(zip(alphabet,List)))
    decode_trans = str.maketrans(dict(zip(List,alphabet)))
    
    translate_text= args.translate(encode_trans)
    decode_letter = translate_text.translate(decode_trans)
    
    return [translate_text,decode_letter]

