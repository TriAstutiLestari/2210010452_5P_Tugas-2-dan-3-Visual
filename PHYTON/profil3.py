import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.theme_text_color("#0000CC")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("NPM       : 2210010452")],
                            [sg.Text("Nama      : Tri Astuti Lestari")],
                            [sg.Text("Kelas     : 5P Regular Banjarmasin")],
                            [sg.Text("Matkul    : Pemrograman Visual 3")],
                            ],
                    size=(400,200))
window()
window.close()