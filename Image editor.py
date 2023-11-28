import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

def update_Image(original, blur, contrast, emboss, contour, flipx, flipy):
    global image
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image = image.filter(ImageFilter.CONTOUR())
    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.flip(image)

    bio = BytesIO()
    image.save(bio, format='GIF')

    window['-Image-'].update(data=bio.getvalue())

image_path = 'bird.gif'

control_col = sg.Column([
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-Blur-')]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-Contrast-')]])],
    [sg.Checkbox('Emboss', key='-Emboss-'), sg.Checkbox('Contour', key='-Contour-')],
    [sg.Checkbox('Flip X', key='-Flipx-'), sg.Checkbox('Flip Y', key='-Flipy-')],
    [sg.Button('Save Image', key='-Save')],
])
Image_col = sg.Column([[sg.Image(image_path, key='-Image-')]])

layout = [[control_col, Image_col]]

original = Image.open(image_path)
window = sg.Window('Image editor', layout)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    update_Image(original,
                 values['-Blur-'],
                 values['-Contrast-'],
                 values['-Emboss-'],
                 values['-Contour-'],
                 values['-Flipx-'],
                 values['-Flipy-']
    )

    if event == '-Save-':
        save_path = sg.popup_get_file('Save', save_as=True, no_window=True) + '.png'
        image.save(save_path, 'PNG')

window.close()