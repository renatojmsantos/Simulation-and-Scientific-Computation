#!/usr/bin/env python
# encoding: utf-8

import peca
import aleatorio

class Evento:
    """Classe de onde vão ser derivados todos os eventos.
    # Contem apenas os atributos e métodos comuns a todos os eventos.
    # Não haverá instâncias desta classe num simulador."""

    # Construtor
    def __init__(self, i, sim, seccao):
        self.instant = i  # Instante de ocorrencia do evento
        self.simulator = sim  # Simulador onde ocorre o evento
        self.seccao = seccao

    def __lt__(self,other):
        """Método de comparação entre dois eventos.
        
        # Determina se o evento corrente ocorre primeiro, ou não, do que o evento e1
        # Se sim, devolve true; se não, devolve false
        # Usado para ordenar por ordem crescente de instantes de ocorrência a lista de eventos do simulador"""

        return self.instant < other.instant


class Chegada(Evento):
    """Classe que representa a chegada de uma peça. Deriva de Evento."""

    # Construtor
    def __init__(self, i, sim, media_Chegada, seccao,seed):
        Evento.__init__(self, i, sim, seccao)
        self.media_Chegada = media_Chegada

        self.seed = seed

    def __str__(self):
        """Método que descreve o evento.
        Para ser usado na listagem da lista de eventos."""

        return "Chegada\t [" + str(self.instant) + " ]"

    def executa(self):
        """Método que executa as accoes correspondentes a chegada de uma peça"""

        # Coloca peça na seccao - na fila ou a ser atendida, conforme o caso
        self.seccao.inserePeca(peca.Peca(), self.seccao.proxima)

        # Agenda nova chegada para daqui a aleatorio.exponencial(self.simulator.media_Chegada) instantes
        self.simulator.insereEvento(Chegada(
            self.simulator.instant + aleatorio.exponencial(self.media_Chegada,self.seed), self.simulator, self.media_Chegada, self.seccao,self.seed))

class Saida(Evento):
    """ Classe que representa a saida de uma peça. Deriva de Evento """

    def __init__(self, i, sim, tipo_seccao, peca, seccao):
        Evento.__init__(self, i, sim, seccao)
        self.tipo_seccao = tipo_seccao
        self.peca = peca

    def __str__(self):
        """ Método que descreve o evento.
        # Para ser usado na listagem da lista de eventos. """

        return "Saida\t [ " + str(self.instant) + " ]"

    def executa(self):
        """ Metodo que executa as acoes correspondentes à saida de uma peça"""

        if self.seccao.proxima != None: # se houver peça em fila de espera
            self.seccao.removePeca(self.tipo_seccao)  # Retira peça da seccao
            self.seccao.proxima.inserePeca(self.peca, self.tipo_seccao)  # insere nova peça na secçao

        else:
            self.seccao.removePeca(self.tipo_seccao)  # Retira peça da seccao