#!/usr/bin/env python
# encoding: utf-8

import math
import rand_generator

# Classe para geracao de numeros aleatorios segundos varias distribuicoes
# Apenas a distribuicao exponencial negativa esta definida

def exponencial(media,seed):
    # Gera um numero segundo uma distribuicao exponencial negativa de media m
    return (-media * math.log(rand_generator.rand(seed)))

class Random:

    stream_k = 0

    def __init__(self, seed):
        self.proxima_peca = 0
        self.existe_peca = False
        self.seed = seed
        self.stream = Random.stream_k

        rand_generator.randst(seed, self.stream)
        Random.stream_k += 1

    def normal(self, media,desvio):
        if self.existe_peca:
            self.existe_peca = False
            return self.proxima_peca

        v1 = 1
        v2 = 2
        
        while(v1**2 + v2**2 > 1):

            v1 = 2 * rand_generator.rand(self.stream) - 1
            v2 = 2 * rand_generator.rand(self.stream) - 1

        z = v1**2 + v2**2

        y1 = v1 * math.sqrt(-2 * math.log(z) / z)
        y2 = v2 * math.sqrt(-2 * math.log(z) / z)

        x1 = media + y1 * desvio
        x2 = media + y2 * desvio

        self.proxima_peca = x2
        self.existe_peca = True

        return (x1)
