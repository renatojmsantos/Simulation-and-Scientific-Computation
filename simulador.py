#!/usr/bin/env python
# encoding: utf-8

import seccao
import lista
import eventos
from tkinter import *

class Simulador:

    def insereEvento(self, event):
        self.event_list.insert_event(event)

    # Construtor
    def __init__(self,ts,mca,mcb,mdpea,dpea,mdpoa,dpoa,mdpeb,dpeb,mdpob,dpob,mde,de,mpea,mpoa,mpeb,mpob,me):

        self.tempo_simulacao = ts   # 8H diárias * 20 dias por mes = 160 H * 60  = 9600 min  /mes

        # Medias das distribuicoes de chegadas e de atendimento na seccao

        # medias e desvios em minutos

        media_ChegadaA = mca
        media_ChegadaB = mcb

        media_PerfA = mdpea
        desvio_PerfA = dpea

        media_PolA = mdpoa
        desvio_PolA = dpoa

        media_PerfB = mdpeb
        desvio_PerfB = dpeb

        media_PolB = mdpob
        desvio_PolB = dpob

        media_Env = mde
        desvio_Env = de


        # Relogio de simulacao - variavel que contem o valor do tempo em cada instante
        self.instant = 0  # valor inicial a zero

        # filas de espera
        # (self,sim,n_maquinas,media_seccao,desvio,proxima,seed)

        # distribuicoes normais ( media, desvio)

        self.fila_Env = seccao.seccao(self, me, media_Env, desvio_Env, None,60)  # SEED = 60

        self.fila_PolA = seccao.seccao(self, mpoa, media_PolA, desvio_PolA, self.fila_Env,50) # Seed = 50
        self.fila_PolB = seccao.seccao(self, mpob, media_PolB, desvio_PolB, self.fila_Env,70) # seed = 70

        self.fila_PerfA = seccao.seccao(self, mpea, media_PerfA, desvio_PerfA, self.fila_PolA,40) # seed = 40
        self.fila_PerfB = seccao.seccao(self, mpeb, media_PerfB, desvio_PerfB, self.fila_PolB,30) # seed = 30

        # Lista de eventos - onde ficam registados todos os eventos que vao ocorrer na simulacao
        self.event_list = lista.Lista(self)

        # Agendamento da primeira chegada.
        #  Se nao for feito, o simulador nao tem eventos para simular

        # Distribuicoes exponenciais negativas
        self.insereEvento(eventos.Chegada(self.instant, self, media_ChegadaA, self.fila_PerfA,10))  # SEED = 10
        self.insereEvento(eventos.Chegada(self.instant, self, media_ChegadaB, self.fila_PerfB,20))  # seed = 20

    def executa(self):

        """Método executivo do simulador"""

        # Enquanto nao atender todos as peças
        while (self.instant <= self.tempo_simulacao):
            #print(self.event_list)  # Mostra lista de eventos - desnecessario; e apenas informativo

            event = self.event_list.remove_event()  # Retira primeiro evento (e o mais iminente) da lista de eventos
            self.instant = event.instant  # Actualiza relogio de simulacao
            self.act_stats()  # Actualiza valores estatisticos

            event.executa()  # Executa evento
        self.relat()  # Apresenta resultados de simulacao finais

    def act_stats(self):
        """Método que actualiza os valores estatisticos do simulador"""

        self.fila_PerfA.act_stats()
        self.fila_PolA.act_stats()

        self.fila_PerfB.act_stats()
        self.fila_PolB.act_stats()

        self.fila_Env.act_stats()

    def relat(self):
        """Método que apresenta os resultados de simulacao finais"""

        """Método que apresenta os resultados de simulacao finais"""

        interface = Tk()
        interface.title('---------- FINAL RESULTS ----------')


        Label(interface, text="\n----------- PERFURAÇÃO A --------------\n").grid(row=1, column=1)
        print("\n------------ PERFURAÇÃO A ------------\n")
        self.fila_PerfA.relat()
        Label(interface, text="Tempo medio de espera: %s" % str(self.fila_PerfA.relat()[0])).grid(row=2, column=1)
        Label(interface, text="Comp. medio da fila: %s" % str(self.fila_PerfA.relat()[1])).grid(row=3, column=1)
        Label(interface, text="Utilizacao da seccao: %s" % str(self.fila_PerfA.relat()[2])).grid(row=4, column=1)
        Label(interface, text="Tempo de simulacao: %s" % str(self.fila_PerfA.relat()[3])).grid(row=5, column=1)
        Label(interface, text="Numero de peças atendidas: %s" % str(self.fila_PerfA.relat()[4])).grid(row=6, column=1)
        Label(interface, text="Numero de peças na fila: %s" % str(self.fila_PerfA.relat()[5])).grid(row=7, column=1)


        Label(interface, text="\n------------ POLIMENTO A ------------\n").grid(row=8, column=1)
        print("\n------------ POLIMENTO A ------------\n")
        self.fila_PolA.relat()
        Label(interface, text="Tempo medio de espera: %s" % str(self.fila_PolA.relat()[0])).grid(row=9, column=1)
        Label(interface, text="Comp. medio da fila: %s" % str(self.fila_PolA.relat()[1])).grid(row=10, column=1)
        Label(interface, text="Utilizacao da seccao: %s" % str(self.fila_PolA.relat()[2])).grid(row=11, column=1)
        Label(interface, text="Tempo de simulacao: %s" % str(self.fila_PolA.relat()[3])).grid(row=12, column=1)
        Label(interface, text="Numero de peças atendidas: %s" % str(self.fila_PolA.relat()[4])).grid(row=13, column=1)
        Label(interface, text="Numero de peças na fila: %s\n" % str(self.fila_PolA.relat()[5])).grid(row=14, column=1)


        Label(interface, text="\n------------ PERFURAÇÃO B ------------\n").grid(row=1, column=2)
        print("\n------------ PERFURAÇÃO B ------------\n")
        self.fila_PerfB.relat()
        Label(interface, text="Tempo medio de espera: %s" % str(self.fila_PerfB.relat()[0])).grid(row=2, column=2)
        Label(interface, text="Comp. medio da fila: %s" % str(self.fila_PerfB.relat()[1])).grid(row=3, column=2)
        Label(interface, text="Utilizacao da seccao: %s" % str(self.fila_PerfB.relat()[2])).grid(row=4, column=2)
        Label(interface, text="Tempo de simulacao: %s" % str(self.fila_PerfB.relat()[3])).grid(row=5, column=2)
        Label(interface, text="Numero de peças atendidas: %s" % str(self.fila_PerfB.relat()[4])).grid(row=6, column=2)
        Label(interface, text="Numero de peças na fila: %s" % str(self.fila_PerfB.relat()[5])).grid(row=7, column=2)


        Label(interface, text="\n------------ POLIMENTO B ------------\n").grid(row=8, column=2)
        print("\n------------ POLIMENTO B ------------\n")
        self.fila_PolB.relat()
        Label(interface, text="Tempo medio de espera: %s" % str(self.fila_PolB.relat()[0])).grid(row=9, column=2)
        Label(interface, text="Comp. medio da fila: %s" % str(self.fila_PolB.relat()[1])).grid(row=10, column=2)
        Label(interface, text="Utilizacao da seccao: %s" % str(self.fila_PolB.relat()[2])).grid(row=11, column=2)
        Label(interface, text="Tempo de simulacao: %s" % str(self.fila_PolB.relat()[3])).grid(row=12, column=2)
        Label(interface, text="Numero de peças atendidas: %s" % str(self.fila_PolB.relat()[4])).grid(row=13, column=2)
        Label(interface, text="Numero de peças na fila: %s\n" % str(self.fila_PolB.relat()[5])).grid(row=14, column=2)


        Label(interface, text="\n------------ ENVERNIZAMENTO ------------\n").grid(row=1, column=3)
        print("\n------------ ENVERNIZAMENTO ------------\n")
        self.fila_Env.relat()
        Label(interface, text="Tempo medio de espera: %s" % str(self.fila_Env.relat()[0])).grid(row=2, column=3)
        Label(interface, text="Comp. medio da fila: %s" % str(self.fila_Env.relat()[1])).grid(row=3, column=3)
        Label(interface, text="Utilizacao da seccao: %s" % str(self.fila_Env.relat()[2])).grid(row=4, column=3)
        Label(interface, text="Tempo de simulacao: %s" % str(self.fila_Env.relat()[3])).grid(row=5, column=3)
        Label(interface, text="Numero de peças atendidas: %s" % str(self.fila_Env.relat()[4])).grid(row=6, column=3)
        Label(interface, text="Numero de peças na fila: %s" % str(self.fila_Env.relat()[5])).grid(row=7, column=3)

        Button(interface, text='QUIT SIMULATOR', command=interface.quit).grid(row=20, column=20, sticky=W, pady=6)  #sair