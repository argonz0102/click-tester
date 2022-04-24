import PySimpleGUI as sg
from time import time

theme_menu = ['menu',['LightGrey1','dark','DarkGray8']]


def create_window(theme):

    sg.theme(theme)
    sg.set_options(font = 'Calibri 20')
    button_size = (7,5)
    layout = [
    [sg.VPush()],
    [sg.Text('Clicking game', right_click_menu = theme_menu)],
    [sg.VPush()],
    [sg.Text(click_count, key = 'count', expand_x = True, justification = 'center'), sg.Button('Click', expand_x = True)],
    [sg.VPush()],
    [sg.Text('Tid', key = '-Tid-', expand_x = True, justification = 'center'), sg.Button('Reset', expand_x = True)],
    [sg.VPush()]

    ]
    return sg.Window('Clicking game',layout, size = (600,250), no_titlebar = False, element_justification = 'center')

    
click_count = 0
window = create_window('dark')
start_time = time()
active = False
elapsed_time = 0


while True:
    event, values = window.read(timeout = 10)
    if event == sg.WIN_CLOSED:
        break

    if event == 'Click':
        click_count += 1
        window['count'].update(click_count)
        active = True

        if active == False:
            start_time = time()
            active = True
 

    if active:
        elapsed_time = round(time() - start_time,1)

        window['-Tid-'].update(str(elapsed_time))

    if event == 'Reset':
        click_count = 0
        window.close()
        window = create_window('dark')
        active = False
        start_time = time()

        

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)


       

window.close()