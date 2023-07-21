import PySimpleGUI as sg
from convertor import convert
label1 = sg.Text("Enter feet    ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter Inches")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Converter",
                   layout = [[label1,input1],
                             [label2,input2],
                             [convert_button,output_label]])
while True:
    event,value = window.read()
    print((event,value))
    if event == sg.WINDOW_CLOSED:
        exit()
    feet = float(value["feet"])
    inches = float(value["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result}metres",text_color="white")

window.close()