import PySimpleGUI as sg
import matplotlib.figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_figure(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x, y, 'r-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

sg.theme('DarkTeal6')
table_content = []
layout = [
    [sg.Table(
        headings=['Observation', 'Result'],
        values=table_content,
        expand_x=True,
        hide_vertical_scroll=True,
        key='-Table-')],
    [sg.Input(key='-Input-', expand_x=True), sg.Button('Submit')],
    [sg.Canvas(key='-Canvas-')]
]

window = sg.Window('Graph maker', layout, finalize=True)

# matplotlib graph
fig = matplotlib.figure.Figure(figsize=(5, 4))
fig.add_subplot(111).plot([], [])
figure_canvas_agg = FigureCanvasTkAgg(fig,window['-Canvas-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        new_value = values['-Input-']
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1, float(new_value)])
            window['-Table-'].update(table_content)
            window['-Input-'].update('')
            update_figure(table_content)

window.close()