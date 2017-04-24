import random
insperdex=[]

def batalha(inspermon_casa,inspermon_visitante):
	while inspermon_casa["vida"] > 0 and inspermon_visitante["vida"] > 0:

		if inspermon_casa["vida"] <= 0:
			acabou_jogo = print("Seu inspermon morreu na batalha...")
			return acabou_jogo

		if inspermon_visitante["vida"] <=0:
			ganhou = print("Você ganhou a batalha!!!")
			print("Voce capturou este inspermon!!!")
			insperdex.append(inspermon_visitante)
			return insperdex.append(inspermon_visitante)


		batalha_passeio = input("{0}, você deseja atacar ou fugir de {1}? ".format(escolha_inspermon,inspermon_visitante["nome"]))

		if batalha_passeio == "atacar":
			print("{0}, prepare o {1} para o ataque contra o inspèrmon {2}".format(escolha_inspermon,inspermon_casa["nome"],inspermon_visitante["nome"]))
			ataque = inspermon_casa["ataque"] - inspermon_visitante["defesa"]
			vida_inspermon_visitante = inspermon_visitante["vida"] - ataque
			inspermon_visitante["vida"] = vida_inspermon_visitante
			print("O novo valor de vida de seu oponente {0} é {1}".format(inspermon_visitante["nome"],inspermon_visitante["vida"]))
			if inspermon_visitante["vida"] <=0:
				ganhou = print("Você ganhou a batalha")
				return ganhou
			volta_ataque = print("{0} prepare-se para receber o contra-ataque do {1}!!!".format(escolha_inspermon,inspermon_visitante["nome"]))
			contra_ataque = inspermon_visitante["ataque"] - inspermon_casa["defesa"]
			vida_inspermon_casa = inspermon_casa["vida"] - contra_ataque
			inspermon_casa["vida"] = vida_inspermon_casa
			print("{0} o novo valor de vida de seu inspèrmon {1} é {2}".format(escolha_inspermon,inspermon_casa["nome"],inspermon_casa["vida"]))
			if inspermon_casa["vida"] <= 0:
				acabou_jogo = print("Se fudeu")
				return acabou_jogo
			z = input("Você deseja fugir ou atacar? ")
			if z == "fugir":
				break
			if z == "atacar":
				continue

		if batalha_passeio == "fugir":
			fugiu_atacado = random.choice(lista_fugiu_atacado)
				
			if fugiu_atacado in lista_fugiu_atacado[0]:
				fugiu = print(lista_fugiu_atacado[0])
				return fugiu

			if fugiu_atacado in lista_fugiu_atacado[1]:
				print("{0}, você não conseguiu fugir e o inspèrmon {1} te viu".format(escolha_inspermon,inspermon_visitante["nome"]))
				print("Prepare-se para ser atacado")
				print("Critical Hit!!!")
				ataque_fugiu = inspermon_visitante["ataque"] - inspermon_casa["defesa"]
				vida_inspermon_casa_fugiu = inspermon_casa["vida"] - ataque_fugiu
				inspermon_casa["vida"] = vida_inspermon_casa_fugiu
				print(inspermon_casa["vida"])


Inspermon = print("Bem vindo ao jogo...")

#Inspèrmons iniciais
inspermon_quatamander = {"nome":"QuataMander", "ataque":50, "vida": 180,"defesa": 18}
inspermon_torichu = {"nome":"Torichu","ataque":70,"vida":90,"defesa":30}
inspermon_danissaur = {"nome":"Danissaur","ataque":80,"vida":120,"defesa":10}

#Inspèrmons selvagens
inspermon_drymartini = {"nome":"DryMartini", "ataque":45,"vida": 180,"defesa": 18}
inspermon_mew = {"nome":"Mew","ataque":70,"vida":200,"defesa":12}
inspermon_papanjo = {"nome":"Papanjo","ataque":80,"vida":120,"defesa":10}

escolha_inspermon = input("Qual o seu nome de aventureiro? ")

lista_nomes_inspermon = ["QuataMander", "Torichu", "Danissaur"]

inspermon_escolha = input("Qual inspèrmon você deseja escolher para o jogo? {0}, {1} ou {2}: ".format(lista_nomes_inspermon[0],
																										lista_nomes_inspermon[1],
																										lista_nomes_inspermon[2]))
insperdex.append(inspermon_escolha)
print (insperdex)
if inspermon_escolha in lista_nomes_inspermon[0]:
	inspermon_casa = inspermon_quatamander
if inspermon_escolha in lista_nomes_inspermon[1]:
	inspermon_casa = inspermon_torichu
if inspermon_escolha in lista_nomes_inspermon[2]:
	inspermon_casa = inspermon_danissaur

lista_encontrou = ["Você encontrou o inspèrmon DryMartini","Você encontrou o inspèrmon Mew",
					"Você encontrou o inspèrmon Papanjo","Você não encontrou um inspèrmon",
					"Você não encontrou um inspèrmon"]

lista_fugiu_atacado = ["Você conseguiu fugir com sucesso!","Sua tentativa de fugir fracassou!"]

while True:
	passear_dormir = input("{0}, você deseja passear, dormir ou ver insperdéx: ".format(escolha_inspermon))

	if passear_dormir == "passear":
		batalha_passeio = random.choice(lista_encontrou)

		if batalha_passeio in lista_encontrou[0]:
			inspermon_visitante = inspermon_drymartini
			batalha = batalha(inspermon_casa,inspermon_visitante)
			

		if batalha_passeio in lista_encontrou[1]:
			inspermon_visitante = inspermon_mew
			batalha = batalha(inspermon_casa,inspermon_visitante)
			

		if batalha_passeio in lista_encontrou[2]:
			inspermon_visitante = inspermon_papanjo
			batalha = batalha(inspermon_casa,inspermon_visitante)
			

		if batalha_passeio in lista_encontrou[3] or lista_encontrou[4]:
			continue
			

	if passear_dormir == "dormir":
		print("Bons sonhos")
		break

