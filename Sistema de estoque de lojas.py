#recebe os dados de estoque de uma loja de calças
estoque = int((input("Insira a quantidade de peças no estoque: ")))
#esabelece uma meta de vendas para a loja
meta_venda = int((input("meta de vendas: ")))
#quantidas de vendas mensais ou semanais da determinada loja. 
calcas_vendidas = int(input("Calças vendidas: "))

'''estabelece que se a meta for alcançada imprimir uma mensagem 
caso a meta não for alcançada a mensagem será outra'''
if meta_venda <= calcas_vendidas:
    print("Meta de vendas batidas")
else:
    meta_nao_alcancada = meta_venda <= calcas_vendidas
    print("a meta não foi alcançada")

#faz o calculo para determinar se há peças no estoque ainda.
estoque_atual = estoque - calcas_vendidas

#imprime para o usuário se há peças no estoque ou há faltas de peças 
if calcas_vendidas <= estoque:
    print("Há: %s, no estoque." % estoque_atual)
else:
    estoque_em_falta = estoque_atual >= estoque
    print("O estoque pode estar em falta")
