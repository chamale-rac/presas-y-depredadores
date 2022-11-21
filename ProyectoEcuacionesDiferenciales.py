import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from random import randrange


def cm_to_inch(value):
    return value/2.54


font = ("Segoe UI", 20)
sg.theme('BrownBlue')

prey_options = [[sg.Text('Tasa de nacimientos:', size=(20, 0)), sg.Slider(
    orientation='horizontal', key='prey_birthrate', range=(0, 2), resolution=.1, enable_events=True)],
    [sg.Text('Tasa de mortalidad:', size=(20, 0)), sg.Slider(
        orientation='horizontal', key='prey_mortality', range=(0, 2), resolution=.1, enable_events=True)],
    [sg.Text('Población inicial:', size=(20, 0)), sg.Slider(
        orientation='horizontal', key='initial_prey', range=(0, 5), resolution=.1, enable_events=True)]]

predator_options = [[sg.Text('Tasa de nacimientos:', size=(20, 0)), sg.Slider(
    orientation='horizontal', key='predator_birthrate', range=(0, 2), resolution=.1, enable_events=True)],
    [sg.Text('Tasa de mortalidad:', size=(20, 0)), sg.Slider(
        orientation='horizontal', key='predator_mortality', range=(0, 2), resolution=.1, enable_events=True)],
    [sg.Text('Población inicial:', size=(20, 0)), sg.Slider(
        orientation='horizontal', key='initial_predator', range=(0, 5), resolution=.1, enable_events=True)]]

simulator_options = [[sg.Text('Diferencial de tiempo:', size=(20, 0)), sg.Slider(
    orientation='horizontal', key='differential', range=(0.01, 0.1), resolution=.01, enable_events=True)],
    [sg.Text('Tiempo:', size=(20, 0)), sg.Slider(
        orientation='horizontal', key='max_time', range=(50, 100), enable_events=True)]]

first_column = [[sg.Frame(layout=prey_options, title='Presas', border_width=1)],
                [sg.Frame(layout=predator_options,
                          title='Depredadores', border_width=1)],
                [sg.Frame(layout=simulator_options,
                          title='Opciones del simulador', border_width=1)]]


second_column = [[sg.Canvas(key='canvasGraph', size=(800, 800))]]

body = [
    [sg.Column(first_column),
     sg.VerticalSeparator(),
     sg.Column(second_column)]
]

buttons = [[sg.Button('Graficar'), sg.Button(
    'Cancel')]]

layout = [[sg.Text('Simulador Presa-Depredador del modelo Lotka Volterra')],
          [sg.HorizontalSeparator()],
          [sg.Frame(layout=body, title='', border_width=0)], [buttons]]

window = sg.Window(
    'Simulador Presa-Depredador del modelo Lotka Volterra', layout, font=font)

window.finalize()

# Obtención del canvas
canvas = window['canvasGraph'].TKCanvas
fig = plt.figure()
fig.set_figheight(10)
fig.set_figwidth(10)
fig, ax = plt.subplots(2)
figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)


def plot_frequency(prey_birthrate=0,
                   prey_mortality=0,
                   initial_prey=0,
                   predator_birthrate=0,
                   predator_mortality=0,
                   initial_predator=0,
                   differential=0.01,
                   max_time=50):

    a = prey_birthrate
    b = prey_mortality
    c = predator_mortality
    e = predator_birthrate

    dt = differential
    time = max_time

    t = 0
    x = initial_prey
    y = initial_predator

    t_list = []
    x_list = []
    y_list = []

    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

    while (t < time):
        t = t + dt
        x = x + (a*x - b*x*y)*dt
        y = y + (-c*y + e*x*y)*dt

        t_list.append(t)
        x_list.append(x)
        y_list.append(y)

    ax[0].cla()
    ax[0].plot(t_list, x_list, label='Presa')
    ax[0].plot(t_list, y_list, label='Depredador')
    ax[0].set_xlabel('Tiempo')
    ax[0].set_ylabel('Población')
    ax[0].set_title("Población contra tiempo")
    ax[0].legend()

    ax[1].cla()
    ax[1].plot(y_list, x_list)
    ax[1].set_xlabel('Presa')
    ax[1].set_ylabel('Depredador')
    ax[1].set_title("Población de presas contra población de depredadores")
    ax[1].legend()

    fig.tight_layout(pad=2.0)

    figure_canvas_agg.draw()


plot_frequency()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Graficar':
        plot_frequency(prey_birthrate=values['prey_birthrate'],
                       prey_mortality=values['prey_mortality'],
                       initial_prey=values['initial_prey'],
                       predator_birthrate=values['predator_birthrate'],
                       predator_mortality=values['predator_mortality'],
                       initial_predator=values['initial_predator'],
                       differential=values['differential'],
                       max_time=values['max_time'])

    if event == 'Caso1':
        plot_frequency(prey_birthrate=0,
                       prey_mortality=0,
                       initial_prey=0,
                       predator_birthrate=0,
                       predator_mortality=0,
                       initial_predator=0,
                       differential=0.01,
                       max_time=50)

    if event == 'Caso2':
        plot_frequency(prey_birthrate=0,
                       prey_mortality=0,
                       initial_prey=0,
                       predator_birthrate=0,
                       predator_mortality=0,
                       initial_predator=0,
                       differential=0.01,
                       max_time=50)

    if event == 'Caso3':
        plot_frequency(prey_birthrate=0,
                       prey_mortality=0,
                       initial_prey=0,
                       predator_birthrate=0,
                       predator_mortality=0,
                       initial_predator=0,
                       differential=0.01,
                       max_time=50)
window.close()
