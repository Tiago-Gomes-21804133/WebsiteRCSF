from django import forms


class FormEspacoLivre(forms.Form):
    f = forms.IntegerField(label="Frequencia [GHz]")
    ptx = forms.IntegerField(label="Potencia [dB]")
    prx_min = forms.IntegerField(label="Potencia minima [dBm]")


class FormOkumuraHata(forms.Form):
    ambientes = (
        ("urbano", "Urbano"),
        ("suburbano", "Suburbano"),
        ("rural", "Rural"),
    )
    frequencia = forms.IntegerField(label="Frequência [MHz]")
    hbe = forms.IntegerField(label="Altura efectiva da estação base (Hbe) [m]")
    distancia = forms.IntegerField(label="Distância do móvel à base [Km]")
    hm = forms.IntegerField(label="Altura do móvel ao solo (Hm) [m]")
    tipoAmbiente = forms.TypedChoiceField(label="Tipo de Ambiente", choices=ambientes)


class FormWalfischIkegami(forms.Form):
    frequencia = forms.IntegerField(label="Frequência [MHz]")
    distancia = forms.FloatField(label="Distância [Km]")


class FormDiagramasAntenas(forms.Form):
    antenas = (
        ("741620_0948_X_CO.msi", "741620_0948_X_CO.msi"),
        ("739662_0948_X_CO_P45.msi", "739662_0948_X_CO_P45.msi"),
        ("737906_0948_X_CO_15T.msi", "737906_0948_X_CO_15T.msi"),
    )

    ganho_minimo = forms.IntegerField(label="Ganho mínimo")
    antena = forms.TypedChoiceField(label="Antena", choices=antenas)


class FormTamanhoMinimoCluster(forms.Form):
    c_i_db = forms.FloatField(label="C/I [dB]")
    n = forms.FloatField(label="Coeficiente de Atenuação (n)")


class FormGraficoCi(forms.Form):
    n = forms.FloatField(label="Coeficiente de Atenuação (n)")


class FormProbabilidadeDeBloqueio(forms.Form):
    t = forms.IntegerField(label="Tráfego Oferecido (t)")
    n = forms.IntegerField(label="Quantidade De Canais (n)")


class FormQuantidadeDeCanais(forms.Form):
    t = forms.IntegerField(label="Tráfego Oferecido (t)")
    pb = forms.FloatField(label="Probabilidade De Bloqueio (Pb)")


class FormTrafegoOferecido(forms.Form):
    n = forms.IntegerField(label="Quantidade De Canais (n)")
    pb = forms.FloatField(label="Probabilidade De Bloqueio (Pb)")