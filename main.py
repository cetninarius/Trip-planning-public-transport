from math import radians, cos, sin, asin, sqrt

# putanja do foldera sa zadatim linijama
PATH = 'ulaz/'

# sufiksi za imena fajlova npr. 46_dirA.txt
SUFIXA = '_dirA.txt'
SUFIXB = '_dirB.txt'


def haversine(lat1, lon1, lat2, lon2):
    # Funkcija za izracunavanje udaljenosti
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r


def read_coords():
    # Cita koordinate sa standardnog ulaza
    crd = input('Pocetne i krajnje koordinate odvojene blanko karakterima: ')
    coords = list(map(float, crd.split()))
    return coords


def get_line_data(line, sufix):
    # Za datu liniju i smer ucitava informacije o stajalistima
    data = []
    with open(PATH + line + sufix, 'r') as file:
        for l in file:
            data.append(l.split('!'))
    return data


def read_lines():
    # Cita linije prevoza za koje je korisnik zainteresovan sa std ulaza
    lines = input('Nazivi linija: ').split()
    line_data = []
    for line in lines:
        line_data.append(get_line_data(line, SUFIXA))

    return line_data, lines


def min_distance_index(line, lat1, lon1):
    # Racuna i vraca index stajalista sa najmanjom udaljenoscu po haversine formuli
    distances = []
    for stop in line:
        lat2 = float(stop[2])
        lon2 = float(stop[3])

        distances.append(haversine(lat1, lon1, lat2, lon2))
    return distances.index(min(distances))


def calculate(coords, line_data, line_names):
    # Koordinate pocetka
    lat1_start = float(coords[0])
    lon1_start = float(coords[1])

    # Koordinate kraja
    lat1_end = float(coords[2])
    lon1_end = float(coords[3])

    results = []

    for line, line_name in zip(line_data, line_names):
        # indeks najblize stanice pocetku
        min_start = min_distance_index(line, lat1_start, lon1_start)

        # indeks najblize stanice kraju
        min_end = min_distance_index(line, lat1_end, lon1_end)

        output = []

        if min_start <= min_end:
            output.append([line_name, 'A\n'])
            output.extend(line[min_start : min_end + 1])

        else:
            output.append([line_name, 'B\n'])

            # Samo ako je pogresan smer ucitavam fajl za smer B
            tmp = get_line_data(line_name, SUFIXB)

            min_start = min_distance_index(tmp, lat1_start, lon1_start)
            min_end = min_distance_index(tmp, lat1_end, lon1_end)

            output.extend(tmp[min_start:min_end + 1])

        results.append(output)

    return results


def write(path, result):
    with open(outpath, 'w') as file:
        for result in results:
            for line in result:
                print(line)
                if len(line)==2:
                    file.write('!'.join(line))
                else:
                    formated = line
                    formated[2] = '{:.6f}'.format(round(float(formated[2]), 6))
                    formated[3] = '{:.6f}'.format(round(float(formated[3]), 6))
                    file.write('!'.join(formated))


outpath = input('Path do izlaznog fajla: ')
try:
    coords = read_coords()
    line_data, lines = read_lines()
    results = calculate(coords, line_data, lines)
    write(outpath, results)

except ValueError:
    print('PODACI_GRESKA', end='')

except FileNotFoundError:
    print('DAT_GRESKA', end='')
