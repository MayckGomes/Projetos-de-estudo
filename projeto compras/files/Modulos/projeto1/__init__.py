import os

def menu(tipo=1,titulo='MENU PRINCIPAL',topicos:list=['nao infomado']):
    """
    mostra um menu na tela
    tipo=1 menu principal[em lista]
    tipo=2 cabecario

    topicos= digite em uma lista os topicos se tipo 1,
    se tipo 2 não é necessario
    """


    if tipo == 1:
        tam = len(titulo) + 4

        print('=' * tam)
        print(f'  {titulo.upper()}')
        print('=' * tam)

        for n,p in enumerate(topicos):
            
            print(f'{n+1} - {p.title()}')
            
        print(f'='* tam)
    
    elif tipo == 2:
        tam = len(titulo) + 4

        print('=' * tam)
        print(f'  {titulo.upper()}')
        print('=' * tam)


def leiaint(txt:str):
    num = input(txt)

    if num.isnumeric() == False:
        
        while True:
            
            print(f'ERRO!, é apenas aceito números')
            num = input(txt)

            if num.isnumeric():
                break

        return int(num)
    else:
        return int(num)
    

def lerArquivo(nome):
    try:
        a = open(nome, 'rt',)
        
    except FileNotFoundError:
        criarArquivo(nome)
    else:
        return a


def mostrarArquivo(arq,enum=False):
    """
    mostra o arquivo , com a linhas numeradas ou não
    arq:str = nome do arquivo
    enum:bool = definido originalmente como false, mas quando mudado para true,mostra as linhas numeradas
    """
    if enum == False:
        arquivo = open(arq,'rt')
        print(arquivo.read())
    else:
        arquivo = open(arq,'rt')
        for i,l in enumerate(arquivo):
            print(f'{i} - {l}'if i > 0 else l)


def encontrarArquivo(nome):
    try:
        arquivo = open(nome)
    except FileNotFoundError or FileExistsError:
        return False
    else:
        return True


def criarArquivo(nome,escreva=''):
        a1 = open(nome, 'wt+')
        a1.write(f'{escreva}\n')
        a1.close() 
        return a1


def escreverArquivo(arq:str ='',espacos:str =' ',item:str ='',quantidade:str =''):
    try:
       a = open(arq,'at')
    except FileNotFoundError:
        criarArquivo(arq)
    else:
        caixadeespc =''
        quantespacos = 20
        quantespacos -= len(item)

        for c in range(0,quantespacos):
            caixadeespc += espacos 

        a.write(f'{item}{caixadeespc}{quantidade}\n')
        a.close()


def excluirArquivo(arq:str):
    try:
        os.remove(str(arq))
    except:
        return 'ocorreu um problema', False
    else:
        return True

#===================== DESATIVADO ===================
# def cor(color):
#     """
#     cores:
#     0 » branco;
#     1 » vermelho;
#     2 » verde;
#     3 » amarelo;
#     4 » azul;
#     5 » magenta;
#     6 » cinza;
#     """

#     cores = ['\033[m','\033[31;1m','\033[32;1m','\033[33;1m','\033[34;1m','\033[35;1m','\033[36;1m']

#     for i,c in enumerate(cores):
#         if color == i:
#             return c
#         else:
#             continue