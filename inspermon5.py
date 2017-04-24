import random
import time


def batalha(inspermon,inspermon_selvagem):

	inspermon_vida = inspermon["vida"]
	inspermon_selvagem_vida = inspermon_selvagem["vida"]

	while inspermon_vida and inspermon_selvagem_vida > 0:

		print("Valor de vida atual de seu inspèrmon {0} é {1}".format(inspermon["nome"],inspermon_vida))
		atacar_fugir = input("{0}, você deseja atacar ou fugir do inspèrmon {1}? ".format(nome,inspermon_selvagem["nome"]))


		if atacar_fugir == "atacar":
			print("Prepare o inspèrmon {0} para o ataque contra o inspèrmon {1}\n".format(inspermon["nome"],inspermon_selvagem["nome"]))
			time.sleep(2)
			print("O valor de vida atual do inspèrmon oponente {0} é {1}\n".format(inspermon_selvagem["nome"],inspermon_selvagem_vida))
			time.sleep(2)
			print(random.choice(lista_onoma))
			time.sleep(1)
			ataque = inspermon["ataque"] - inspermon_selvagem["defesa"]
			inspermon_selvagem_vida = inspermon_selvagem_vida - ataque
			print("{0} tirou {1} de vida do inspèrmon {2} e o novo valor de vida do oponente eh {3}\n".format(inspermon["nome"],ataque,inspermon_selvagem["nome"],inspermon_selvagem_vida))
			time.sleep(2)
			if inspermon_selvagem_vida < 0:
				venceu = "Você venceu a batalha"
				insperdex.append(inspermon_selvagem)
				return venceu

			print("{0} prepare-se para receber o contra-ataque do inspèrmon {1}\n".format(inspermon["nome"],inspermon_selvagem["nome"]))
			time.sleep(2)
			print(random.choice(lista_onoma))
			contra_ataque = inspermon_selvagem["ataque"] - inspermon["defesa"]
			inspermon_vida = inspermon_vida - contra_ataque
			print("{0} tirou {1} de vida de seu inspèrmon {2} e seu novo valor de vida ficou {3}\n".format(inspermon_selvagem["nome"],contra_ataque,inspermon["nome"],inspermon_vida))
			time.sleep(2)
			if inspermon_vida < 0:
				gameover = "GAME OVER"
				return gameover

		if atacar_fugir == "fugir":
			fugiu_atacado = random.choice(lista_fugiu_atacado)

			if fugiu_atacado in lista_fugiu_atacado[0]:
				fugiu = "Você fugiu com sucesso"
				return fugiu

			if fugiu_atacado in lista_fugiu_atacado[1]:
				print("{0}, você não conseguiu fugir e o inspèrmon {1} te viu\n".format(nome,inspermon_selvagem["nome"]))
				time.sleep(3)
				print("ATAQUE SURPRESA!\n")
				time.sleep(1)
				print("Ataque do adversário multiplicado por 2x\n")
				time.sleep(1)
				ataque_fugiu = inspermon_selvagem["ataque"]*2 - inspermon["defesa"]
				print(random.choice(lista_onoma))
				inspermon_vida = inspermon_vida - ataque_fugiu
				print("{0} tirou {1} de vida de seu inspèrmon {2} e seu novo valor de vida ficou {3}\n".format(inspermon_selvagem["nome"],ataque_fugiu,inspermon["nome"],inspermon_vida))
				time.sleep(4)
				if inspermon_vida < 0:
					gameover = "GAME OVER"
					return gameover

#Inspèrmon listas e dicionários

lista_onoma = ["Slash","Critical Hit!!!!","What a shot!!","Boom"]

lista_fugiu_atacado = ["Você conseguiu fugir com sucesso!","Você fracassou na tentativa de fugir"]

lista_inspermon = ["Quatamander", "Torichu", "Danissaur"]

lista_encontrou = ["Você encontrou o inspèrmon DryMartini","Você encontrou o inspèrmon Mew",
					"Você encontrou o inspèrmon Papanjo","Você não encontrou um inspèrmon",
					"Você não encontrou um inspèrmon","Você encontrou o inspèrmon Inspee",
					"Você encontrou o inspèrmon Birinite"]
insperdex = []

#Inspèrmons iniciais

inspermon_quatamander = {"nome":"Quatamander", "ataque":90, "vida": 180,"defesa": 18}
inspermon_torichu = {"nome":"Torichu","ataque":70,"vida":90,"defesa":30}
inspermon_danissaur = {"nome":"Danissaur","ataque":80,"vida":120,"defesa":10}

#Inspèrmons selvagens

inspermon_drymartini = {"nome":"DryMartini", "ataque":45,"vida": 180,"defesa": 18}
inspermon_mew = {"nome":"Mew","ataque":70,"vida":200,"defesa":12}
inspermon_papanjo = {"nome":"Papanjo","ataque":80,"vida":120,"defesa":10}
inspermon_inspee = {"nome":"Inspee","ataque":65,"vida":80,"defesa":35}
inspermon_birinite = {"nome":"Birinite","ataque":70,"vida":100,"defesa":18}

#Inspèrmon input's, print's e title's

print("Bem-vindo ao Inspèrmon\n")
time.sleep(1)
print("Prepare-se para um mundo cheio de aventuras e desafios...")
time.sleep(2)
nome = input("Qual o nome de seu personagem? \n")

print("Estes sao os Inspèrmons iniciais disponíveis: \n")

time.sleep(2)

print("Nome do inspèrmon: {0}".format(inspermon_quatamander["nome"]))
print("Ataque do inspèrmon: {0}".format(inspermon_quatamander["ataque"]))
print("Defesa do inspèrmon: {0}".format(inspermon_quatamander["defesa"]))
print("Vida do inspèrmon: {0}\n ".format(inspermon_quatamander["vida"]))

time.sleep(3)

print("Nome do inspèrmon: {0}".format(inspermon_torichu["nome"]))
print("Ataque do inspèrmon: {0}".format(inspermon_torichu["ataque"]))
print("Defesa do inspèrmon: {0}".format(inspermon_torichu["defesa"]))
print("Vida do inspèrmon: {0}\n".format(inspermon_torichu["vida"]))

time.sleep(3)

print("Nome do inspèrmon: {0}".format(inspermon_danissaur["nome"]))
print("Ataque do inspèrmon: {0}".format(inspermon_danissaur["ataque"]))
print("Defesa do inspèrmon: {0}".format(inspermon_danissaur["defesa"]))
print("Vida do inspèrmon: {0}\n".format(inspermon_danissaur["vida"]))

time.sleep(3)

inspermon_escolha = input("Com qual inspèrmon inicial você deseja jogar?\n {0}\n {1}\n {2}\n".format(lista_inspermon[0],
																								lista_inspermon[1],
																								lista_inspermon[2]))

inspermon_escolha_title = inspermon_escolha.title()

#Inspèrmon jogo

if inspermon_escolha_title in lista_inspermon[0]:
	inspermon_casa = inspermon_quatamander
	insperdex.append(inspermon_quatamander)
if inspermon_escolha_title in lista_inspermon[1]:
	inspermon_casa = inspermon_torichu
	insperdex.append(inspermon_torichu)
if inspermon_escolha_title in lista_inspermon[2]:
	inspermon_casa = inspermon_danissaur
	insperdex.append(inspermon_danissaur)

while True:

	passear_dormir = input("{0}, você deseja passear(p) , dormir (d) ou ver insperdéx (i): ".format(nome))

	if passear_dormir == "p":
		
		batalha_passeio = random.choice(lista_encontrou)
		print(batalha_passeio)

		if batalha_passeio in lista_encontrou[0]:
			inspermon_visitante = inspermon_drymartini
			luta = batalha(inspermon_casa,inspermon_visitante)
			if luta == "Você venceu a batalha":
				print("Você venceu a batalha")
				continue
			if luta == "GAME OVER":
				print("GAME OVER")
				break
			if luta == "Você fugiu com sucesso":
				print("Você fugiu com sucesso")
				continue

		if batalha_passeio in lista_encontrou[1]:
			inspermon_visitante = inspermon_mew
			luta = batalha(inspermon_casa,inspermon_visitante)
			if luta == "Você venceu a batalha":
				print("Você venceu a batalha")
				continue
			if luta == "GAME OVER":
				print("GAME OVER")
				break
			if luta == "Você fugiu com sucesso":
				print("Você fugiu com sucesso")
				continue

		if batalha_passeio in lista_encontrou[2]:
			inspermon_visitante = inspermon_papanjo
			luta = batalha(inspermon_casa,inspermon_visitante)
			if luta == "Você venceu a batalha":
				print("Você venceu a batalha")
				continue
			if luta == "GAME OVER":
				print("GAME OVER")
				break
			if luta == "Você fugiu com sucesso":
				print("Você fugiu com sucesso")
				continue

		if batalha_passeio in lista_encontrou[5]:
			inspermon_visitante = inspermon_inspee
			luta = batalha(inspermon_casa,inspermon_visitante)
			if luta == "Você venceu a batalha":
				print("Você venceu a batalha")
				continue
			if luta == "GAME OVER":
				print("GAME OVER")
				break
			if luta == "Você fugiu com sucesso":
				print("Você fugiu com sucesso")
				continue

		if batalha_passeio in lista_encontrou[6]:
			inspermon_visitante = inspermon_birinite
			luta = batalha(inspermon_casa,inspermon_visitante)
			if luta == "Você venceu a batalha":
				print("Você venceu a batalha")
				continue
			if luta == "GAME OVER":
				print("GAME OVER")
				break
			if luta == "Você fugiu com sucesso":
				print("Você fugiu com sucesso")
				continue

		if batalha_passeio in lista_encontrou[3] or lista_encontrou[4]:
			continue

	
	if passear_dormir == "i":
		print(insperdex)

	if passear_dormir == "d":
		print("Bons sonhos")
		break