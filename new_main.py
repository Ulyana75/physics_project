import pandas as pd
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft
from utilits import get_XYZ
from config import *

EXCEL_FILENAME = "new_data/5_05_2021.xlsx"
STR_QUANTITY = 3587
MS1 = 700
MS2 = 1000


def get_concrete_single_data(list_name: str, filename=EXCEL_FILENAME):
    df = pd.read_excel(filename, sheet_name=list_name)
    l = df['λ'].tolist()
    col_names = df.columns.tolist()
    data = []
    final_data = [0] * STR_QUANTITY
    for i in col_names[1:]:
        data.append(df[i].tolist())
    for i in range(STR_QUANTITY):
        for j in range(len(data)):
            final_data[i] += data[j][i]
        final_data[i] /= len(col_names[1:])
    return l, final_data


def get_normalise_data(sample_name: str, color: str, type_normalise=1, filename=EXCEL_FILENAME):
    """
    1 - white/black,
    0 - noise/paper,
    2 - black/paper
    3 - noise/white
    """

    ms = MS1

    try:
        other = get_concrete_single_data(sample_name + '-' + color + '-' + str(ms) + 'ms', filename)[1]
    except ValueError:
        ms = MS2
        other = get_concrete_single_data(sample_name + '-' + color + '-' + str(ms) + 'ms', filename)[1]

    if type_normalise == 1:
        l, white = get_concrete_single_data(sample_name + '-White-' + str(ms) + 'ms', filename)
        black = get_concrete_single_data(sample_name + '-Black-' + str(ms) + 'ms', filename)[1]

    elif type_normalise == 0:
        l, white = get_concrete_single_data('Гля2-White-700ms', filename)
        black = noise_data[1]

    elif type_normalise == 3:
        l, white = get_concrete_single_data(sample_name + '-White-' + str(ms) + 'ms', filename)
        black = noise_data[1]

    else:
        l, white = get_concrete_single_data('Гля1-White-700ms', filename)
        black = get_concrete_single_data(sample_name + '-Black-' + str(ms) + 'ms', filename)[1]

    data = []

    for i in range(STR_QUANTITY):
        data.append((other[i] - black[i]) / (white[i] - black[i]))

    return l, data


def save_graphics(date_folder: str):
    for a in samples:
        for b in numbers:
            for c in colors:
                fig, ax = plt.subplots()
                plt.plot(*get_normalise_data(a + b, c, 1))
                plt.title(a + b + '-' + c)
                plt.show()
                fig.savefig('graphics/' + date_folder + '/normalise_white_black/' + a + b + '-' + c)


noise_data = get_concrete_single_data('Dark-noise-700ms', "new_data/5_05_2021.xlsx")

if __name__ == "__main__":

    # save_graphics("28_04_2021")

    # other = get_concrete_single_data('lol' + '-' + 'lol' + '-' + str(MS1) + 'ms')[1]
    # xl = pd.ExcelFile('new_data/31_03_2021.xlsx')
    # print(*xl.sheet_names, sep='\n')

    # list_name = input('Enter list name: ')

    # white = get_concrete_single_data('Гля1-White-700ms')
    # black = noise_data
    # color = get_concrete_single_data('Г2-Red-700ms')
    # plt.plot(white[0], white[1], 'r',
    #          black[0], black[1], '#000000',
    #          color[0], color[1], 'g')
    # plt.show()

    # fig, ax = plt.subplots()
    save_graphics('5_05_2021')
    # plt.plot(*get_normalise_data('Г2', 'Red', type_normalise=0))
    # plt.show()
    # plt.title('Mirror-mirror2-700ms')
    # plt.show()

    # data = get_normalise_data('Г2', 'Green')
    # x = fftfreq(STR_QUANTITY)
    # y = fft(data[1])
    # plt.subplot(2, 2, 1)
    # plt.plot(x, y)
    # plt.ylim(0, 10)
    # for i in range(len(x)):
    #     if 0.48 <= abs(x[i]) < 0.6:
    #         y[i] = 0
    #
    # plt.subplot(2, 2, 2)
    # plt.plot(x, y)
    # plt.ylim(0, 10)
    # #plt.title(f)
    # plt.subplot(2, 2, 4)
    # plt.plot(data[0], ifft(y))
    # plt.subplot(2, 2, 3)
    # plt.plot(*data)
    # plt.show()


"""
Акв2-White-1000ms
Г2-White-1000ms
Акр2-White-1000ms
М2-White-1000ms
Акр2-Black-1000ms
М2-Black-1000ms
Г2-Black-1000ms
Акв2-Black-1000ms
Акв2-Yellow-1000ms
Акр2-Yellow-1000ms
М2-Yellow-1000ms
Г2-Yellow-1000ms
М2-Green-1000ms
Г2-Green-1000ms
Акр2-Green-1000ms
Акв2-Green-1000ms
Акр2-Blue-1000ms
Г2-Blue-1000ms
М2-Blue-1000ms
Акв2-Blue-1000ms
Г2-Red-1000ms
Акр2-Red-1000ms
М2-Red-1000ms
Акв2-Red-1000ms
Г1-White-1000ms
Акв1-White-1000ms
Акр1-White-1000ms
М1-White-1000ms
Акр1-Black-1000ms
М1-Black-1000ms
Г1-Black-1000ms
Акв1-Black-1000ms
Г1-Green-1000ms
Акв1-Green-1000ms
М1-Green-1000ms
Акр1-Green-1000ms
Г1-Blue-1000ms
М1-Blue-1000ms
Акр1-Blue-1000ms
Акв1-Blue-1000ms
Акв1-Red-1000ms
Г1-Red-1000ms
Акр1-Red-1000ms
М1-Red-1000ms
Акв1-Yellow-1000ms
М1-Yellow-1000ms
Г1-Yellow-1000ms
Акр1-Yellow-1000ms
"""