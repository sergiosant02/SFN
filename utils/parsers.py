def parse_str_to_bin(text: str):
    return [format(ord(i), '08b') for i in text]

def convert_to_four_bits(data: list):
    data_txt = ''.join(str(i) for i in data)
    bits_array = [ data_txt[i:i+4] for i in range(0,len(data_txt), 4)]
    return bits_array