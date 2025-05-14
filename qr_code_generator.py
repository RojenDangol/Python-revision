import qrcode


def qrlink():
    link = input("Enter the text or URL: ").strip()
    filename = input("Enter the filename ").strip()
    generateQr(link, filename)

def generateQr(link, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img.save(f'{filename}.png')
    img.show()

qrlink()
