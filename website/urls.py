from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index, name='index'),
    path('umts/', views.umts, name='umts'),
    path('lte/', views.lte, name='lte'),
    path('espaco_livre/', views.espaco_livre, name='espaco_livre'),
    path('okumura_hata/', views.okumura_hata, name='okumura_hata'),
    path('walfisch_ikegami/', views.walfisch_ikegami, name='walfisch_ikegami'),
    path('digramas_antenas', views.digramas_antenas, name='digramas_antenas'),
    path('tamanho_cluster', views.tamanho_cluster, name='tamanho_cluster'),
    path('grafico_ci_ncp/', views.grafico_ci_ncp, name='grafico_ci_ncp'),
    path('probabilidade_bloqueio/', views.probabilidade_bloqueio, name='probabilidade_bloqueio'),
    path('quantidade_canais/', views.quantidade_canais, name='quantidade_canais'),
    path('trafego_oferecido/', views.trafego_oferecido, name='trafego_oferecido'),
    path('about/', views.about, name='about'),
]
