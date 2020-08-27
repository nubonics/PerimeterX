import base64


def payload(event, value):
    e = ''
    n = 50
    if event == 'decode':
        value = base64.b64decode(value).decode('utf-8')
    for r, letter in enumerate(value):
        e += chr(n ^ ord(letter))
    if event == 'decode':
        return e
    else:
        databytes = str(e).encode('utf-8')
        encoded = base64.b64encode(databytes)
        return encoded.decode('utf-8')
        
        
# payload("decode", "payload_here")
# payload("encode", "payload_here")
# written by https://vk.com/gerogiewna21
