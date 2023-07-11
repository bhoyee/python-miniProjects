import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

 #encode data into qrcode 
def _encode_():
    data = 'Don\'t forget to subscribe'
    qr = qrcode.QRCode(version = 1, box_size=10, border=5)

    qr.add_data(data)

    qr.make(fit=True)

    img = qr.make_image(fill_color = 'red', back_color = 'white')

    #path to save the qrcode
    img.save('C:/Users/Bhoyee-pc/Documents/python-demo/demo/qrcode/myqrcode.png')
    print('ENcode successfully')

 #decode data in qrcode
def _decode_():
    img = Image.open('C:/Users/Bhoyee-pc/Documents/python-demo/demo/qrcode/myqrcode.png')

    result = decode(img)

    print(result)


_encode_()
_decode_()
