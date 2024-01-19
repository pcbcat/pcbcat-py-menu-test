import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('Some text on Row 1')],
    [sg.Text('Enter something on Row 2'), sg.InputText(key='input_field')],
    [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Back to menu')]  # Use sg.Button() for 'Back to menu'
]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    elif event == 'Back to menu':
        window.close()  # Close the current window
        import menu
        menu  # This will navigate back to the menu as per your requirement

    input_text = values['input_field']  # Access the input value using its key
    if input_text.strip() == '':  # Check if input is empty
        sg.popup('Please Enter Something')
    else:
        sg.popup('You entered: ' + input_text)

window.close()
