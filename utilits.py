
def get_XYZ():
    l = [0.0] * 471
    x = [0.0] * 471
    y = [0.0] * 471
    z = [0.0] * 471
    with open('some_resources/xyz.txt') as f:
        for s in f:
            s = s.replace(',', '.')
            s = list(map(float, s.split()))
            ind1 = int(s[0]) - 360
            l[ind1] = s[0]
            x[ind1] = s[1]
            y[ind1] = s[2]
            z[ind1] = s[3]
            if len(s) > 4:
                ind2 = int(s[4]) - 360
                l[ind2] = s[4]
                x[ind2] = s[5]
                y[ind2] = s[6]
                z[ind2] = s[7]
    return l, x, y, z
