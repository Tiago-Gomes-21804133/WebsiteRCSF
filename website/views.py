from django.shortcuts import render

from . import functions

from .forms import FormEspacoLivre
from .forms import FormProbabilidadeDeBloqueio
from .forms import FormQuantidadeDeCanais
from .forms import FormTamanhoMinimoCluster
from .forms import FormTrafegoOferecido
from .forms import FormOkumuraHata
from .forms import FormWalfischIkegami
from .forms import FormDiagramasAntenas
from .forms import FormTamanhoMinimoCluster
from .forms import FormGraficoCi


def index(request):
    return render(request, "website/index.html")


def umts(request):
    return render(request, "website/umts.html")


def lte(request):
    return render(request, "website/lte.html")


def espaco_livre(request):
    submetido = False
    form = FormEspacoLivre(request.POST or None)

    if form.is_valid():
        submetido = True
        functions.atenuacaoEspacoLivre_grafico(
            form.cleaned_data['f'],
            form.cleaned_data['ptx'],
            form.cleaned_data['prx_min']
        )

    context = {'form': form, 'submetido': submetido}

    return render(request, "website/espaco_livre.html", context)


def okumura_hata(request):
    submetido = False
    resultado = 0
    form = FormOkumuraHata(request.POST or None)

    if form.is_valid():
        submetido = True
        resultado = functions.okumura_hata(
            form.cleaned_data['frequencia'],
            form.cleaned_data['distancia'],
            form.cleaned_data['hbe'],
            form.cleaned_data['hm'],
            form.cleaned_data['tipoAmbiente']
        )

    context = {'form': form, 'submetido': submetido, 'resultado': resultado}

    return render(request, "website/okumura_hata.html", context)


def walfisch_ikegami(request):
    submetido = False
    resultado = 0
    form = FormWalfischIkegami(request.POST or None)

    if form.is_valid():
        submetido = True
        resultado = functions.walfisch_ikegami(
            form.cleaned_data['frequencia'],
            form.cleaned_data['distancia']
        )

    context = {'form': form, 'submetido': submetido, 'resultado': resultado}

    return render(request, "website/walfisch_ikegami.html", context)


def digramas_antenas(request):
    submetido = False
    form = FormDiagramasAntenas(request.POST or None)

    if form.is_valid():
        submetido = True
        functions.criar_diagrama(
            form.cleaned_data['antena'],
            form.cleaned_data['ganho_minimo'],
        )

    context = {'form': form, 'submetido': submetido}

    return render(request, "website/diagramas_antenas.html", context)


def tamanho_cluster(request):
    submetido = False
    resultado = 0
    form = FormTamanhoMinimoCluster(request.POST or None)

    if form.is_valid():
        submetido = True
        resultado = functions.tamanho_minimo_cluster(
            form.cleaned_data['c_i_db'],
            form.cleaned_data['n']
        )

    context = {'form': form, 'submetido': submetido, 'resultado': resultado}

    return render(request, "website/tamanho_cluster.html", context)


def grafico_ci_ncp(request):
    submetido = False
    form = FormGraficoCi(request.POST or None)

    if form.is_valid():
        submetido = True
        functions.grafico_CI_NCP(
            form.cleaned_data['n']
        )

    context = {'form': form, 'submetido': submetido}

    return render(request, "website/grafico_ci.html", context)


def probabilidade_bloqueio(request):
    submetido = False
    resultado = 0.0
    form = FormProbabilidadeDeBloqueio(request.POST or None)

    if form.is_valid():
        submetido = True
        resultado = functions.calcularProbabilidadeDeBloqueio(
            form.cleaned_data['t'],
            form.cleaned_data['n']
        )

    context = {'form': form, 'submetido': submetido, 'resultado': resultado}

    return render(request, "website/probabilidade_bloqueio.html", context)


def quantidade_canais(request):
    submetido = False
    resultado = 0.0
    form = FormQuantidadeDeCanais(request.POST or None)

    if form.is_valid():
        submetido = True
        resultado = functions.calcularQuantidadeCanais(
            form.cleaned_data['pb'],
            form.cleaned_data['t']
        )

    context = {'form': form, 'submetido': submetido, 'resultado': resultado}

    return render(request, "website/quantidade_canais.html", context)


def trafego_oferecido(request):
    submetido = False
    resultado = 0.0
    form = FormTrafegoOferecido(request.POST or None)

    if form.is_valid():
        submetido = True
        resultado = functions.calcularTrafegoOferecido(
            form.cleaned_data['pb'],
            form.cleaned_data['n']
        )

    context = {'form': form, 'submetido': submetido, 'resultado': resultado}

    return render(request, "website/trafego_oferecido.html", context)


def about(request):
    return render(request, "website/about.html")