import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft
from utilits import get_XYZ

STR_QUANTITY = 3587
F = 700 / (400 * 10 ** (-6))


def get_lambda():
    with open('../data/two_columns.txt') as f:
        waves = []
        for i in range(STR_QUANTITY):
            s = f.readline()
            s = s.replace(',', '.')
            waves.append(float(s))
        return waves


def get_data(filename, k):
    data = [0] * STR_QUANTITY
    for i in range(1, k + 1):
        file = 'data/' + filename + str(i) + '.txt'
        with open(file) as f:
            for j in range(STR_QUANTITY):
                s = f.readline()
                s = s.replace(',', '.')
                data[j] += float(s)
    for i in range(STR_QUANTITY):
        data[i] = data[i] / k
    return data


def get_single_data(filename):
    with open('data/' + filename) as f:
        data = []
        for i in range(STR_QUANTITY):
            s = f.readline()
            s = s.replace(',', '.')
            data.append(float(s))
    return data


def get_coordinates_of_list(l: list, data: list):
    new_data = [0.0] * 471
    i = 0
    while i < len(l) - 1:
        ind = int(l[i]) - 360
        new_data[ind] = data[i]
        n = 1
        while i < len(l) - 1 and int(l[i]) == int(l[i + 1]):
            new_data[ind] += data[i + 1]
            n += 1
            i += 1
        i += 1
        new_data[ind] /= n
    l, x, y, z = get_XYZ()
    x_c = 0
    y_c = 0
    z_c = 0
    for i in range(len(y)):
        x_c += (x[i] * new_data[i])
        y_c += (y[i] * new_data[i])
        z_c += (z[i] * new_data[i])
    return x_c, y_c, z_c


def make_two_coordinates(l: list, data: list):
    x, y, z = get_coordinates_of_list(l, data)
    new_x = x / (x + y + z)
    new_y = y / (x + y + z)
    return new_x, new_y


def get_two_coordinates(filename_white, filename_black, filename_other):
    l = get_lambda()
    data = get_normalise_data(filename_white, filename_black, filename_other)
    x, y, z = get_coordinates_of_list(l, data)
    new_x = x / (x + y + z)
    new_y = y / (x + y + z)
    return new_x, new_y


def get_normalise_data(filename_white, filename_black, filename_other):
    black = get_data(filename_black, 5)
    white = get_data(filename_white, 5)
    other = get_data(filename_other, 5)
    y = []
    for i in range(len(black)):
        y.append((other[i] - black[i]) / (white[i] - black[i]))
    return y


# f = 'АквКрас'
# # x = fftfreq(STR_QUANTITY)
# # y = fft(get_data(f, 5))
# # plt.subplot(2, 2, 1)
# # plt.plot(x, y)
# # plt.ylim(0, 2000)
# # for i in range(len(x)):
# #     if 0.48 <= abs(x[i]) < 0.6:
# #         y[i] = 0
# #
# # plt.subplot(2, 2, 2)
# # plt.plot(x, y)
# # plt.ylim(0, 2000)
# # #plt.title(f)
# # plt.subplot(2, 2, 4)
# # plt.plot(get_lambda(), ifft(y))
# # plt.subplot(2, 2, 3)
# # plt.plot(get_lambda(), get_data(f, 5))
# # plt.show()
# plt.plot(get_lambda(), get_data('ГБелый', 5), 'r', get_lambda(), get_data('ГСин', 5), 'b',
#          get_lambda(), get_data('ГЧерный', 5), '#000000')
# plt.show()
