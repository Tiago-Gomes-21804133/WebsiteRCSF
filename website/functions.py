import math
from math import log10
from math import log
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib
import os
import json
import seaborn as sns

sns.set()

matplotlib.use('agg')


def atenuacaoEspacoLivre_grafico(f: "frequencia [GHz]", ptx: "potencia [dBm]", prx_min: "potencia minima [dBm]"):
    l_d = []
    l_prx = []
    l_prx_min = []

    d = 0
    l = 0
    while (ptx - l > prx_min - 2):
        d += 1
        l = 32.44 + 20 * math.log10(d / 1000000) + 20 * math.log10(f * 1000)
        l_prx.append(ptx - l)

    l_d = list(range(1, d + 1))
    l_prx_min = [prx_min for i in range(1, d + 1)]

    plt.style.use('seaborn-bright')
    plt.plot(l_d, l_prx, label="Prx")
    plt.plot(l_d, l_prx_min, label="Prx_min")

    plt.xlabel('distância [m]')
    plt.ylabel('Potência recebida [dBm]')
    plt.title(f'Nível de sinal recebido (Ptx = {ptx} dBm e f = {f} GHz)')
    plt.legend()
    plt.savefig('website/static/website/images/free-space.jpg')
    plt.close()


def hmu(hm, f, tipoAmbiente):
    if tipoAmbiente == "urbano":
        return (1.10 * log(f) - 0.70) * hm - (1.56 * log(f) - 0.80)
    elif tipoAmbiente == "suburbano":
        return (1.10 * log(f) - 0.70) * hm - (1.56 * log(f) - 0.80)
    elif tipoAmbiente == "rural":
        return 3.20 * (log(11.75 * hm) ** 2) - 4.97
    else:
        return


def okumura_hata(f, d, hbe, hm, tipoAmbiente):
    if 150 < f < 1500 and 1 < d < 20 and 30 < hbe < 200 and 1 < hm < 10:
        try:
            Hmu = hmu(hm, f, tipoAmbiente)
            lp = 69.55 + 26.16 * log(f) - 13.82 * log(hbe) + (44.90 - 6.55 * log(hbe)) * log(d) - Hmu
            return "{:.2f}".format(lp)
        except:
            return "Erro ao calcular."
    elif f < 150 or f > 1500 and 1 < d < 20 and 30 < hbe < 200 and 1 < hm < 10:
        return "Frequência inválida."
    elif 150 < f < 1500 and d < 1 or d > 20 and 30 < hbe < 200 and 1 < hm < 10:
        return "Distância inválida."
    elif 150 < f < 1500 and 1 < d < 20 and hbe < 30 or hbe > 200 and 1 < hm < 10:
        return "Hbe inválido."
    elif 150 < f < 1500 and 1 < d < 20 and 30 < hbe < 200 and hm < 1 or hm > 10:
        return "Hm inválido."
    else:
        return "Inputs inválidos."


def walfisch_ikegami(f, d):
    if d <= 0.02 and f < 800 or f > 2000:
        return "Inputs inválidos."
    elif d <= 0.02 and 800 < f < 2000:
        return "Distância inválida."
    elif d > 0.02 and 800 < f < 2000:
        lp = 42.6 + 26 * log10(d) + 20 * log10(f)
        return "{:.2f}".format(lp)
    else:
        return "Frequência inválida."


def criar_diagrama(ficheiro_antena, ganho_minimo):
    with open(os.path.join(f'website/static/website/Antenas/{ficheiro_antena}')) as file:
        dados = file.readlines()

        indice_horizontal = dados.index("HORIZONTAL 360\n")

        indice_vertical = dados.index("VERTICAL 360\n")

        print(indice_horizontal, indice_vertical)

        angulos = []

        horizontal = []

        for linha in dados[indice_horizontal + 1: indice_vertical]:
            angulo, ganho = linha.split()
            angulos.append(float(angulo) / 360 * 2 * math.pi)
            horizontal.append(max(-float(ganho), ganho_minimo))

        vertical = [max(-float(linha.split()[1]), ganho_minimo) for linha in dados[indice_vertical + 1:]]

        h = plt.subplot(projection="polar")
        h.plot(angulos, horizontal, "red", label="horizontal")

        h.set_title('Diagrama Horizontal', pad=20, size=16)
        h.set_rgrids([r for r in range(0, ganho_minimo, -5)])
        h.set_thetagrids([r for r in range(0, 360, 15)])
        h.set_theta_direction(-1)
        h.set_theta_offset(math.pi / 2)
        h.set_rmin(ganho_minimo)

        plt.savefig('website/static/website/images/diagramaHorizontal.png')
        plt.close()

        v = plt.subplot(projection="polar")
        v.plot(angulos, vertical, "green", label="vertical")

        v.set_title('Diagrama Vertical', pad=20, size=16)
        v.set_rgrids([r for r in range(0, ganho_minimo, -5)])
        v.set_thetagrids([r for r in range(0, 360, 15)])
        v.set_theta_direction(-1)
        v.set_rmin(ganho_minimo)

        plt.savefig('website/static/website/images/diagramaVertical.png')
        plt.close()


def tamanho_minimo_cluster(c_i_db, n):
    c_i = 10 ** (c_i_db / 10)
    rcc = pow(c_i * 6, (1 / n))
    n_cp = int(math.ceil((rcc ** 2) / 3))
    return n_cp


def grafico_CI_NCP(n):
    n_cp = [3, 4, 7, 12, 13, 19]
    lista_c_i = []
    for i in n_cp:
        rcc = math.sqrt(3 * i)
        c_i = (rcc ** n) / 6
        c_i_db = 10 * math.log10(c_i)
        lista_c_i.append(c_i_db)
    plt.bar(n_cp, lista_c_i)
    plt.xlabel('N_CP')
    plt.ylabel('C/I [dB]')
    plt.title('C/I vs N_CP')
    plt.savefig('website/static/website/images/CIvsNCP.jpg')
    plt.close()


def calcularProbabilidadeDeBloqueio(t, n):
    pb = 1.0
    for i in range(1, n + 1):
        pb = 1.0 + pb * (i / t)
    return 1.0 / pb


def calcularQuantidadeCanais(pb, t):
    for i in range(1, 100):
        pb_procura = calcularProbabilidadeDeBloqueio(t, i)
        if pb + 0.001 >= pb_procura >= pb - 0.01:
            return i
    return 0


def calcularTrafegoOferecido(pb, n):
    for i in range(1, 100):
        pb_procura = calcularProbabilidadeDeBloqueio(i, n)
        if pb + 0.001 >= pb_procura >= pb - 0.01:
            return i
    return 0
