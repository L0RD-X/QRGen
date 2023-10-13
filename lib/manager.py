# =============[ QRGEN LIB ]============#
# Author: @L0RD-X
# Version: 1.0

from qrcode import QRCode, ERROR_CORRECT_L


def generate(dado, bg='#FFFFFF', fg='#000000', onde='./undefined'):
    name_image = onde
    qr = QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=25,
        border=4, 
    )

    qr.add_data(dado)
    qr.make(fit=True)
    end = qr.make_image(fill_color=fg, back_color=bg)
    end.save(f"{name_image}.png")

    return "ok"
