# =============[ QRGEN LIB ]============#
# Author: @L0RD-X
# Version: 1.0

from os import getlogin, path, makedirs
from requests import get



def image(url, where='.\icone.png'):
    result = get(url).content
  
    with open(where, 'wb') as imagem:
        imagem.write(result)


def viewer():
    main = rf'C:\Users\{getlogin()}\.qrgen'
    icones =rf'C:\Users\{getlogin()}\.qrgen\icon'
    logo = rf'C:\Users\{getlogin()}\.qrgen\icon\logo.png'
    url = 'https://raw.githubusercontent.com/L0RD-X/QRGen/main/icones/logo.ico'

    if path.isdir(main) == True:
        if path.isdir(icones) == True:
            if path.isfile(logo) == True:
                return
            else:
                image(url, logo)
        else:
            makedirs(icones)
            image(url, logo)
    else:
        makedirs(main)
        makedirs(icones)
        image(url, logo)
viewer()