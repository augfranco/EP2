import random
import time
insperdex = []

print("Bem-vindo ao mundo dos inspermons, um lugar cheio de aventuras...")
print("Carregando...")
time.sleep(4)
print("Pronto")
time.sleep(1)

nome = input("Digite o nome de seu personagem: ")
print("{}, aqui estao os tres inspermons iniciais disponiveis...".format(nome))
time.sleep(2)



#Inspèrmons iniciais
quatamander = {"nome":"Quatamander", "ataque":90, "vida": 180,"defesa": 18, "xp": 0}
torichu = {"nome":"Torichu","ataque":70,"vida":90,"defesa":30, "xp": 0}
danissaur = {"nome":"Danissaur","ataque":80,"vida":120,"defesa":10, "xp": 0}

print(quatamander)
time.sleep(2)
print(torichu)
time.sleep(2)
print(danissaur)
time.sleep(2)

lista_nomes_inspermon = ["quatamander", "torichu", "danissaur"]

#Escolha inspermon
inspermon_escolha = input("Qual inspèrmon você deseja escolher para o jogo? {0}, {1} ou {2}: ".format(lista_nomes_inspermon[0],
																										lista_nomes_inspermon[1],
																										lista_nomes_inspermon[2]))

if inspermon_escolha in lista_nomes_inspermon[0]:
	inspermon_real = quatamander
if inspermon_escolha in lista_nomes_inspermon[1]:
	inspermon_real = torichu
if inspermon_escolha in lista_nomes_inspermon[2]:
	inspermon_real = danissaur

insperdex.append(inspermon_escolha)

#Inspèrmons selvagens
drymartini = {"nome":"DryMartini", "ataque":45,"vida": 180,"defesa": 18}
mew = {"nome":"Mew","ataque":70,"vida":200,"defesa":12}
papanjo = {"nome":"Papanjo","ataque":80,"vida":120,"defesa":10}
inspee = {"nome":"Inspee","ataque":65,"vida":80,"defesa":35}
birinite = {"nome":"Birinite","ataque":70,"vida":100,"defesa":18}

def batalha(inspermon_real, inspermon_maquina):
	while inspermon_real["vida"] > 0 or inspermon_maquina["vida"] > 0:
		if inspermon_real["vida"] <= 0:
			print("Voce perdeu a batalha")
		if inspermon_maquina["vida"] <= 0:
			print ("voce ganhou a batalha!")
			insperdex.append(inspermon_maquina)

		if passeio_insperdex_dormir == "atacar":
			print("{0}, prepare o {1} para o ataque contra o inspèrmon {2}".format(nome,inspermon_real["nome"],inspermon_maquina["nome"]))
			ataque = inspermon_real["ataque"] - inspermon_maquina["defesa"]
			nova_vida_inspermon_maquina = inspermon_maquina["vida"] - ataque
			inspermon_maquina["vida"] = nova_vida_inspermon_maquina
			time.sleep(1)
			print("A vida do seu oponete passou de {0} para {1}...".format())





lista_encontrou = ["Você encontrou o inspèrmon DryMartini","Você encontrou o inspèrmon Mew",
					"Você encontrou o inspèrmon Papanjo","Você não encontrou um inspèrmon",
					"Você não encontrou um inspèrmon","Você encontrou o inspèrmon Inspee",
					"Você encontrou o inspèrmon Birinite"]


while True:
	passeio_insperdex_dormir = input("voce deseja passear (p), consultar sua insperdex (i), ou dormir (d)? ")
	if passeio_insperdex_dormir == "p":
		achou_ou_nao = random.choice(lista_encontrou)
		print (achou_ou_nao)

	if passeio_insperdex_dormir == "i":
		print (insperdex)

	if passeio_insperdex_dormir == "d":
		print ("Bons sonhos...")
		break







