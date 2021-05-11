from new_main import get_normalise_data
from utilits import get_XYZ


def get_coordinates(sample_name: str, color: str, filename, type_normalise=1):
    l, data = get_normalise_data(sample_name, color, type_normalise, filename)
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


def make_two_coordinates(sample_name: str, color: str, filename, type_normalise=1):
    x, y, z = get_coordinates(sample_name, color, filename, type_normalise)
    new_x = x / (x + y + z)
    new_y = y / (x + y + z)
    return new_x, new_y
