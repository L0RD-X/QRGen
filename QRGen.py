# =============[ QRGEN App ]============#
# Author: @L0RD-X
# Version: Beta(0.1)

from PySimpleGUI import (Window, Button, Input,Text,
VSeparator,Push,theme,popup,FolderBrowse)
from os import getlogin
from lib.manager import generate
from lib.verify import viewer



theme("Dark")
Main = [
    [Text('Dado do QR:'),Push(),Input(size=53),Push()],
    [Text('Cor do Fundo'),Input(size=53),Push()],
    [Text('Cor'),Push(),Push(),Input(size=53)],
    [Text('Onde'),Push(),Input(size=45),FolderBrowse()],
    [Text('Nome'),Push(),Input(size=45),Push(),Push()],
    [Push(),Button('Gerar QR', size=20),Push(), Button('sair', size=20),Push()]
]

all = Window(
    title='Gerador de QRCode - COG(Beta)',
    size=(500, 250),
    layout=Main,
    icon=viewer()
)

while True:
    event, value = all.read()
    data_qr = value[0]
    bg_color = value[1]
    fg_color = value[2]
    save_as = value[3]
    name = value[4]
    out_put = f"{save_as}/{name}"

    match(event):
        case 'Gerar QR':
            if data_qr == '' or bg_color == '' or fg_color == '' or save_as == '' or name == '':
                popup('Preencha todos os campos, por favor!', icon=viewer())
            else:
                generate(data_qr, bg_color, fg_color, onde=out_put)
                popup(f'Imagem salva {out_put}.png')
        case "sair":
            break
        case None:
            break
            
all.close()
