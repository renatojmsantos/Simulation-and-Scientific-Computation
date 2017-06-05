#!/usr/bin/env python
# encoding: utf-8

import eventos
import aleatorio

class seccao:
    """ Classe que representa uma seccao com uma fila de espera associada """

    # Construtor
    def __init__(self,sim,n_maquinas,media_seccao,desvio,proxima,seed):
        
        self.fila = []  # Fila de espera do seccao
        self.simulator = sim  # Referencia para o simulador a que pertence o seccao
        self.estado = 0  # Variavel que regista o estado do seccao: 0 - livre; 1 - ocupado
        self.temp_last = sim.instant  # Tempo que passou desde o ultimo evento. Neste caso 0, pq a sim ainda nao comecou
        self.atendidos = 0  # Numero de peças atendidas ate ao momento
        self.soma_temp_esp = 0
        self.soma_temp_serv = 0

        self.n_maquinas = n_maquinas
        self.media_seccao = media_seccao
        self.desvio = desvio
        self.proxima = proxima  #proxima peça da seccao X
        self.random_generator = aleatorio.Random(seed)

    def inserePeca(self, peca, tipo_seccao):
        """Método que insere peça na secção"""

        if self.estado < self.n_maquinas:  # Se seccao livre
            self.estado = self.estado + 1  # Fica ocupado e agenda saida da peça para daqui a "media_seccao" instantes
            self.simulator.insereEvento(
                eventos.Saida(self.simulator.instant + self.random_generator.normal(self.media_seccao,self.desvio), self.simulator, tipo_seccao, peca, self))
        else:
            self.fila.append(peca)  # Se seccao ocupado, a peça vai para a fila de espera

    def removePeca(self, tipo_seccao):
        """Método que remove peça da secção"""

        self.atendidos = self.atendidos + 1  # Regista que acabou de atender mais uma peça

        if not self.fila:  # Se a fila esta vazia,
            self.estado = self.estado - 1  # liberta a seccao X

        else:
            # vai à fila de espera e traz a próxima peça
            self.simulator.insereEvento(
                eventos.Saida(self.simulator.instant + self.random_generator.normal(self.media_seccao,self.desvio), self.simulator, tipo_seccao, self.fila.pop(0), self))

    def act_stats(self):
        """Método que calcula valores para estatísticas, em cada passo da simulação ou evento"""

        # Calcula tempo que passou desde o ultimo evento
        temp_desd_ult = self.simulator.instant - self.temp_last

        # Actualiza variavel para o proximo passo/evento
        self.temp_last = self.simulator.instant

        # Contabiliza tempo de espera na fila
        # para todos as peças que estiveram na fila durante o intervalo
        self.soma_temp_esp += (len(self.fila) * temp_desd_ult)

        # Contabiliza tempo de atendimento
        self.soma_temp_serv += (self.estado * temp_desd_ult)


    def relat(self):
        """Método que calcula valores finais estatísticos"""

        # Tempo medio de espera na fila
        temp_med_fila = self.soma_temp_esp / (self.atendidos + len(self.fila))

        # Comprimento medio da fila de espera
        # self.simulator.instant neste momento e o valor do tempo de simulacao,
        # uma vez que a simulacao comecou em 0 e este metodo so e chamado no fim da simulacao
        comp_med_fila = self.soma_temp_esp / self.simulator.instant

        # Tempo medio de atendimento na seccao
        utilizacao_serv = (self.soma_temp_serv / self.simulator.instant) / self.n_maquinas

        # Apresenta resultados
        print("Tempo medio de espera: ", temp_med_fila)
        print("Comp. medio da fila: ", comp_med_fila)
        print("Utilizacao da seccao: ", utilizacao_serv)
        print("Tempo de simulacao: ", self.simulator.instant)
        print("Numero de peças atendidas: ", self.atendidos)
        print("Numero de peças na fila: ", len(self.fila))

        return [temp_med_fila, comp_med_fila, utilizacao_serv, self.simulator.instant, self.atendidos, len(self.fila)]
