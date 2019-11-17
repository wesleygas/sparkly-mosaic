import argparse
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from joblib import dump, Parallel, delayed
import pandas as pd
import pymysql
from sqlalchemy import create_engine

parser = argparse.ArgumentParser(
    description="""
        @@@@@ Sparkly Mosaic @@@@

        Este projeto integra o pocesso de montagem de um mosaico de imagens
        em uma pipeline spark, buscando uma maior velocidade de processamento
        e melhor aproveitamento dos recursos de hardware.

        O usuário deverá primeiramente montar o banco de imagens, indicando um
        diretório contendo apenas imagens. Estas imagens serão utilizadas para preencher
        o mosaico.
    """
)


parser.add_argument("action", help="Acao a ser executada", choices=["index","build"])
parser.add_argument("input", help="Quando \"index\" indica o caminho do diretorio contendo APENAS imagens para indexagem\
.\tQuando \"build\" - indica o caminho DA IMAGEM a ser pesquisada ou, escrevendo \"camera\", abre uma janela para captura de imagem")

args = parser.parse_args()

action = args.action
input = args.input

if(action == "index"):
    if(os.path.isfile(input)):
        raise Exception("Caminho fornecido precisa ser de um diretorio")
    ##Coloque o código para criar o DB de imagens

elif(action == "build"):
    if(input.lower() == "camera"):
        print("Abrindo camera.")
    
    if(not os.path.isfile(input)):
        print("Ô meu consagrado, você leu o help ou quer que eu te ajude? Esse troço que você me mandou procurar nem arquivo é!")
        raise Exception("Caminho fornecido precisa ser de um arquivo de imagem")
    
    print("Pipeline de montagem do mosaico #Activate.")
    ##Coloque o código para criar o mosaico