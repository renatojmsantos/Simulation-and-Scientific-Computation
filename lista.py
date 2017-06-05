#!/usr/bin/env python
# encoding: utf-8

import operator

class Lista:
    """Classe que contem, em cada instante, os eventos a serem executados, ordenados por instantes de ocorrencia crescentes.
    Funciona como uma agenda."""

    # Construtor
    def __init__(self, sim):
        self.simulator = sim  # Simulador a que pertence a lista de eventos
        self.list = []

    def __str__(self):
        """Metodo informativo apenas. Imprime o conteudo da lista de eventos em cada instante"""

        s = "[" + str(self.simulator.instant) + "] List:\n"

        for i in range(len(self.list)):
            s = s + "\t[" + str(i+1) + "] " + str(self.list[i]) + "\n"

        return s

    # Metodo para inserir um evento na lista de eventos
    def insert_event(self, event):
        self.list.append(event)
        self.list.sort(key=operator.attrgetter('instant'))  # ordena para um atributo especifico
        #self.list.sort()

    def remove_event(self):
        return self.list.pop(0)
