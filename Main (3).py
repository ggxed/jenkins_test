import math

import av

from av.video.stream import VideoStream

from PIL import Image
from av.video.stream import VideoStream
import numpy
from PIL import Image
from fractions import Fraction
import libpcap




def rgb_to_y(pics, width, height):
    if pics < 0 or width < 0 or height < 0:
        raise ValueError ("variables cannot be negative")
    y = []

    for k, pic in enumerate(pics):
        y.append([])
        print(k)
        for i in range(0, height):
            y[k].append([])
            for j in range(0, width):
                blue, green, red = (pic[i* height + j])
                value = (int)(0.299 * red + 0.587 * green + 0.114 * blue)
                y[k][i].append(value)

    return y



def expected_value(y, a, height, width):
    value = 0
    for i in range(0, height):
        for j in range(0, width):
            value += y[a][i][j]
    return (float)(value / (height * width))

def sigma(y, a , height, width): # возвращает сигму и мат ожидание, чтоб 2 раза не считать мат ожидание
    value = 0
    expected_val = expected_value(y, a , height, width)
    for i in range(0, height):
        for j in range(0, width):
            value += (y[a][i][j] - expected_val) ** 2
    return math.sqrt(value / (height * width-1)), expected_val

def correlation(y, a, b, sigma_a, ev_a, sigma_b, ev_b, height, width): #ev_a - expected value
    val = 0
    for i in range(0, height):
        for j in range(0, width):
            val += (y[a][i][j] - ev_a) * (y[b][i][j] - ev_b)
    return (float) (val/ (width * height *sigma_a * sigma_b))





def auto_correlation(y, height, width):
    correlation_coeff = []
    #----------------------------
    expected_values = []
    sigmas = []
    for i in range(0, len(y)):
        sig, expected_val = sigma(y, i, height, width)
        sigmas.append(sig)
        expected_values.append(expected_val)
    # вычисление мат ожидания и сигмы для каждого кадра
    print("progress (" + str(len(y)) + ") = ", end =' ')
    for a in range (0, len(y)):
        correlation_coeff.append([])
        print(a,end=' ')
        for b in range(0, len(y)):
            value = correlation(y, a, b, sigmas[a],expected_values[a] ,sigmas[b],expected_values[b], height, width)
            correlation_coeff[a].append(value)
    return correlation_coeff


def task1(filename):
    # В этом списке будем хранить кадры в виде numpy-векторов.
    array_list = []
    # Откроем контейнер на чтение
    input_container = av.open(filename)
    # Применим «инверсное мультиплексирование» =)
    # Получим пакеты из потока.
    input_packets = input_container.demux()
    #print(input_packets.stream.codec)
    # Получии все кадры видео и положим их в `array_list`.
    mas_of_pixels = []
    width = 0
    height = 0
    for packet in input_packets:
        if isinstance(packet.stream, VideoStream):
            # Получим все кадры пакета
            frames = packet.decode()
            for raw_frame in frames:
                cur_image = raw_frame.to_rgb().to_image()
                mas_of_pixels.append(list(cur_image.getdata()))  # массив пикселей для всех картинок
                width, height = cur_image.size
    y = rgb_to_y(mas_of_pixels, width, height)
    correl = auto_correlation(y, height, width)
    file = open('task1/correlation3.txt', 'w')
    min = 1
    for i in range(0, len(correl)):
        for j in range(0, len(correl[i]) - 1):
            file.write(str(correl[i][j]) + ',')
            if correl[i][j] < min:
                min = correl[i][j]
        file.write(str(correl[i][j]))
        file.write('\n')
    file.close()
    print(min)




def main(filename):
    task1('LR1_1.AVI')





if __name__ == '__main__':
    main('LR1_1.AVI')




