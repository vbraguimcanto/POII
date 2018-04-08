#!/usr/bin/env python
# -*- dfoding: utf-8 -*-
import numpy as np
from numpy import genfromtxt

def buscaProfundidade(df, matrizZeros, noInicio, noObjetivo):
        lista = [noInicio]
        aresta={noInicio:[]}
        if noInicio == noObjetivo:
                return aresta[noInicio]
        while(lista):
                x = lista.pop()
                for y in range(len(df)):
                        if(df[x][y]-matrizZeros[x][y]>0) and y not in aresta:
                                aresta[y] = aresta[x]+[(x,y)]
                                if y == noObjetivo:
                                        return aresta[y]
                                lista.append(y)
        return None

def fluxoMaximo(df, noInicio, noObjetivo):
        n = len(df) 
        matrizZeros = [[0] * n for i in range(n)]
        aresta = buscaProfundidade(df, matrizZeros, noInicio, noObjetivo)
        while aresta != None:
            fluxo = min(df[x][y] - matrizZeros[x][y] for x,y in aresta)
            for x,y in aresta:
                matrizZeros[x][y] += fluxo
                matrizZeros[y][x] -= fluxo
            aresta = buscaProfundidade(df,matrizZeros,noInicio,noObjetivo)
        return sum(matrizZeros[noInicio][i] for i in range(n))

def main():
    noInicio = 1
    noObjetivo = 4
    df = genfromtxt('base-custo-CSV.csv', delimiter=';')
    fluxoMaximoZ = fluxoMaximo(df, noInicio, noObjetivo)
    print "No de inicio:", noInicio
    print "No objetivo:", noObjetivo  
    print "\nZ* = ", fluxoMaximoZ

main()
