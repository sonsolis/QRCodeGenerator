import qrcode

def createQRCode(link, filename="qr_code.png"):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    my_link = "https://discord.gg/HekAARY5CM"
    createQRCode(my_link)
