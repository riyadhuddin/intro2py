# write function to perform text to hex conversion
def text2hex(text):
    """
    Convert text to hex
    :param text: text to convert
    :return: hex string
    """
    return ''.join(format(ord(c), 'x') for c in text)
hex = text2hex('Riyadh Uddin')
# write function to perform hex to text conversion
def hex2text(hex):
    """
    Convert hex to text
    :param hex: hex to convert
    :return: text string
    """
    return ''.join(chr(int(hex[i:i+2], 16)) for i in range(0, len(hex), 2))
text = hex2text(hex)
print(hex)
print(text)
# write function to perform hex to binary conversion
def hex2bin(hex):
    """
    Convert hex to binary
    :param hex: hex to convert
    :return: binary string
    """
    return ''.join(format(int(hex[i:i+2], 16), 'b') for i in range(0, len(hex), 2))
bin = hex2bin(hex)
# write function to perform binary to hex conversion
def bin2hex(bin):
    """
    Convert binary to hex
    :param bin: binary to convert
    :return: hex string
    """
    return ''.join(format(int(bin[i:i+8], 2), 'x') for i in range(0, len(bin), 8))
hexbin = bin2hex(bin)
print(bin)
print(hexbin)
# write function to perform hex to text conversion
def hexbin2text(hexbin):
    """
    Convert hex to text
    :param hex: hex to convert
    :return: text string
    """
    return ''.join(chr(int(hex[i:i+2], 16)) for i in range(0, len(hex), 2))
texthbin = hexbin2text(hexbin)
print(texthbin)