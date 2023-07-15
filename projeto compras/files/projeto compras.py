#modulos
from Modulos.projeto1 import *
import time
import datetime

#variaveis
usu = 0
des = item = quantidade = pegarlinha = ''
main = 'arquivos.txt'
filename = 'nada'
listatxt = []
itemtxt = []

#programa principal

while True:
    #verificar main

    arquivo = encontrarArquivo(main)
    if arquivo == False:
        criarArquivo(main,'Cod  Nome                    Data')

    print('Carregando...')
    time.sleep(1)
    
    #se não houver lista carregada
    if filename == 'nada':
        try:
            menu(topicos=['Nova lista','carregar Lista','excluir lista','encerrar progama'])    
            usu = int(input('Digite a opção: '))
        
        except:
        
            print(f'Erro!, é apenas aceito números')
        
        else:
            #criar lista
            if usu == 1:
                #nova lista
                while True:
                    filename = input('Digite o nome da lista: ').strip()
                    filename.replace(' ','')

                    if '.txt' not in filename:
                            filename = filename + '.txt'
                        
                    #verificar se existe outro arquivo com o mesmo nome para nao dar conflito
                    procurar = encontrarArquivo(filename)
                    if procurar:

                        print(f'ja existe um arquivo com esse nome!')
                        continue
                    
                    else:
                        #criou o arquivo
                        escreverArquivo(arq=main ,item=filename ,quantidade=str(datetime.datetime.now()))
                        criarArquivo(filename,'item                unidade')
                        break
        
            #carregar lista
            if usu == 2:                          
                menu(2,'Mostrando listas')

                cont = 0
                txtmain = open(main,'rt')
                for x in txtmain:
                    cont += 1

                if cont > 1:
                    mostrarArquivo(main,enum=True)#mostrou o arquivo numerado
                    
                    txtmain = open(main)#o reabriu
                    codigotxt = int(input('Digite o codigo da lista: '))#pegou o codigo da lista

                    for ind,linha in enumerate(txtmain):
                        if codigotxt == ind:
                            print(f'foi carregado a lista {linha.split()[0]}')#pegou o nome do arquivo da lista
                            filename = linha.split()[0]
                            lerArquivo(filename)# abriu o arquivo
                            time.sleep(0.5)
                            print('=' * 15)
                else:
                    print('não ha listas para carregar')
            
            #excluir lista
            elif usu == 3:
                txtmain = open(main,'rt')
                
                #verificar quantas listas ha no arquivo
                cont = 0
                for l in txtmain:
                    cont += 1
                    
                if cont > 1:
                    mostrarArquivo(main,True)

                    #armazenou o nome das listas em uma lista
                    txtmain = open(main,'rt')
                    for l in txtmain:
                        listatxt.append(l)
                    
                    txtmain = open(main,'wt')#apagou conteudo

                    codigotxt = int(input('Digite o codigo da lista: '))#pegou o codigo da lista

                    #pegou nome do arquivo
                    filename = listatxt[codigotxt]
                    filename = filename.split()[0]

                    #excluiu nome da lista
                    listatxt.pop(codigotxt)

                    #reescreveu main
                    txtmain = open(main,'rt')
                    for listas in listatxt:
                        txtmain = open(main,'at')
                        txtmain.write(listas)
                  
                    listatxt.clear()
                    excluirArquivo(filename)
                    filename = 'nada'
                    print(f'A lista foi excluida com sucesso!')# e o excluiu
                    time.sleep(1.5)

                else:
                    print('não ha arquivos para apagar')

            #encerrar programa
            elif usu == 4:
                menu(2,'encerrado o programa...')
                break

            #erros
            elif usu > 4 or usu <= 0:
                print(f'indice invalido')
    
    #se houver lista carregada
    else:
        while True:
                menu(1,f'Editando {filename}',['Adicionar item','excluir item','mostrar lista','fechar lista'])
                try:
                    usu = int(input('Digite sua opcão: '))
                except:
                    leiaint('Digite sua opcão: ')
                else:
                    #adicionar item na lista
                    if usu == 1:
                        while True:
                            item = input('Digite o nome do item("fim" para finalizar): ').title().strip()
                            
                            if item in 'Fim':
                                break
                            
                            else:
                                quantidade = input('Digite a quantidade: ')

                                escreverArquivo(filename,espacos='.', item=item, quantidade=quantidade)
                                print('=' * 15)

                    #excluir item
                    elif usu == 2:
                        txtlista = open(filename,'rt')
                        
                        #verificar quantas listas ha no arquivo
                        cont = 0
                        for l in txtlista:
                            cont += 1
                            
                        if cont > 1:
                            mostrarArquivo(filename,True)

                            #armazenou o conteudo do txt em uma lista
                            itemstxt = open(filename,'rt')
                            for l in itemstxt:
                                listatxt.append(l)

                            itemstxt = open(filename,'wt')#apagou conteudo do txt
                            
                            codexclu = int(input('Digite o codigo do item: '))#pegou o codigo do item

                            listatxt.pop(codexclu)#excluiu o item na lista
                            
                            #reescrevendo txt
                            itemstxt = open(filename,'rt')
                            for items in listatxt:
                                itemstxt = open(filename,'at')
                                itemstxt.write(items)

                            listatxt.clear()
                            print('o item foi excluido com sucesso')
                            input()
                        else:
                            print('não ha items para excluir')
                            
                    #mostrar lista
                    elif usu == 3:
                        itemstxt = open(filename,'rt')

                        cont = 0
                        for x in itemstxt:
                            cont += 1
                        
                        if cont > 1:
                            mostrarArquivo(filename)
                            input()

                        else:
                            print('não ha items para mostrar')
                            time.sleep(1.5)

                    #fechar lista
                    elif usu == 4:
                        #fechar edicao
                        filename = 'nada'
                        break
                    
                    #erros
                    elif usu > 4 or usu < 1:
                        print(f'indice invalido')
                        continue
