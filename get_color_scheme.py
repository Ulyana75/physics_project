from matplotlib import pyplot as plt
from config import *
from get_vectors import *


def get_concrete_color_scheme(sample_name: str, color: str, type_normalise=1):
    x = []
    y = []

    for i in excel_filenames:
        x1, y1 = make_two_coordinates(sample_name, color, i, type_normalise)
        x.append(x1)
        y.append(y1)

    return x, y


def save_all_color_schemas(date_folder: str, type_normalise=1):
    for a in samples:
        for b in numbers:
            for c in colors:
                img = plt.imread('some_resources/Plotting_Plot_Chromaticity_Diagram_CIE1931.png')
                fig, ax = plt.subplots()
                ax.imshow(img, extent=[0, 1, 0, 1])
                data = get_concrete_color_scheme(a + b, c, type_normalise)
                c_list = get_colors_list(len(data[0]))
                ax.scatter(*data, s=10, c=c_list)
                plt.xlim(0, 1)
                plt.ylim(0, 1)
                plt.title(a + b + '-' + c)
                plt.show()
                fig.savefig('graphics/color_schemas/' + date_folder + '/normalise_white_noise/' + a + b + '-' + c)


def get_concrete_mix_scheme(sample_name: str, color1: str, color2: str, color3: str, type_normalise=1):
    EXCEL_FILENAME = 'new_data/5_05_2021.xlsx'
    x = []
    y = []

    x1, y1 = make_two_coordinates(sample_name, color1, EXCEL_FILENAME, type_normalise=type_normalise)
    x.append(x1)
    y.append(y1)

    x1, y1 = make_two_coordinates(sample_name, color2, EXCEL_FILENAME, type_normalise=type_normalise)
    x.append(x1)
    y.append(y1)

    x1, y1 = make_two_coordinates(sample_name, color3, EXCEL_FILENAME, type_normalise=type_normalise)
    x.append(x1)
    y.append(y1)

    return x, y


def save_all_mix_schemas(date_folder='mixes', type_normalise=1):
    for a in samples:
        for c in mixes.keys():
            b = '1'
            img = plt.imread('some_resources/Plotting_Plot_Chromaticity_Diagram_CIE1931.png')
            fig, ax = plt.subplots()
            ax.imshow(img, extent=[0, 1, 0, 1])
            data = get_concrete_mix_scheme(a + b, c, mixes[c][0], mixes[c][1], type_normalise)
            c_list = ['0', '0.5', '0.5']
            ax.scatter(*data, s=10, c=c_list)
            plt.xlim(0, 1)
            plt.ylim(0, 1)
            plt.title(a + b + '-' + c)
            plt.show()
            fig.savefig('graphics/color_schemas/' + date_folder + '/normalise_white_noise/' + a + b + '-' + c)


def get_colors_list(q):
    step = 1 / (q - 1)
    res = [str(1.0)]
    cur = 1.0
    for i in range(q - 2):
        cur -= step
        res.append(str(cur))
    res.append(str(0.0))
    return res


if __name__ == "__main__":
    # img = plt.imread('some_resources/Plotting_Plot_Chromaticity_Diagram_CIE1931.png')
    # fig, ax = plt.subplots()
    # ax.imshow(img, extent=[0, 1, 0, 1])
    # data = get_concrete_color_scheme('Акв1', 'Blue', 1)
    # c = get_colors_list(len(data[0]))
    # ax.scatter(*data, s=10, c=c)
    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    # plt.show()
    # save_all_color_schemas('5_05_2021', 3)
    save_all_mix_schemas()
