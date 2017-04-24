import random 

import json

with open("Inspermon.json") as arquivo:
	lista_de_inspermon = json.load(arquivo)


t=0

print("Inspèrmon")

nome_personagem = input("Comece seu jogo escolhendo o nome de seu personagem: ")

passeie_durma = input("{}, você deseja: Passear(P) Dormir(D) Ver o insperdéx(I) ".format(nome_personagem))

title_passeie_durma = passeie_durma.title()

lista_passeie = ["Passear","passear", "P", "p"]

lista_1_2 = ["Um", "Dois", "1", "2"]

lista_batalha = ["Você encontrou um inspèrmon selvagem", "Você não encontrou um inspèrmon selvagem"]

lista_inspèrdex = ["Augusto", "Torichu", "Danissauro", "Aaras"]

lista_atacar = ["Atacar","atacar","A","a"]

lista_fugir = ["Fugir", "fugir", "F", "f"]

lista_fugiu_atacado = ["Você conseguiu fugir com sucesso", "O inspérmon selvagem conseguiu te atacar"]

lista_selvagem = [150,180,300]

while True:

	if title_passeie_durma in lista_passeie:
		batalha_passeio = random.choice(lista_batalha)

		if batalha_passeio in lista_batalha[0]:
			inspèrmon = print(lista_batalha[0])
			batalhar_fugir = input("{}, você deseja: Atacar(A) Fugir(F) ".format(nome_personagem))

			if batalhar_fugir in lista_fugir:
				print(lista_fugiu_atacado[0])
		
			if batalhar_fugir in lista_atacar:
				escolha_inspèrmon = input("Com qual inspèrmon do seu insperdéx você quer batalhar com o inspèrmon selvagem? {}, {}, {}, {}: ".format(lista_inspèrdex[0],lista_inspèrdex[1],lista_inspèrdex[2], lista_inspèrdex[3]))
				inspèrmon_title = escolha_inspèrmon.title()
				if escolha_inspèrmon in lista_inspèrdex[0]:
					batalha = lista_selvagem[0] - lista_de_inspermon[0]
					print("O inspèrmon selvagem tirou {} de sua vida".format(batalha))
					perdeuvida = lista_augusto[2] - batalha
					lista_augusto[2] = perdeuvida
					print(lista_augusto)