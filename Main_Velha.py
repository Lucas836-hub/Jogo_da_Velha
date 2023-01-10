#aplicativo jogo da velha 11/12/2020sv

# VERSAO 0.9

#Para fazer : idioma e cor na frente ao iniciar pela primeira 0 
import tkinter as tk
from tkinter import *
import sqlite3
import run_back
from random import randint
import pygame
from datetime import datetime
from PIL import Image, ImageTk
import os

banco = sqlite3.connect("save_game.db")
cursor = banco.cursor()

try:
	cursor.execute("CREATE TABLE dados(bg integer,idioma integer)")
	
	cursor.execute(f"INSERT INTO dados(bg , idioma ) VALUES (0,0)")
	
	cursor.execute("CREATE TABLE nomes(meu char,dele char)")
	
	cursor.execute(f"INSERT INTO nomes(meu , dele ) VALUES ('Jogador 01','Jogador 02')")
	
	cursor.execute("CREATE TABLE sons(toque char,erro char,resultado char)")
	
	cursor.execute(f"INSERT INTO sons(toque , erro ,resultado ) VALUES ('True','True','True')")

	banco.commit()
except:
	pass
	

 
 #              GLOBAIS
 
cursor.execute("SELECT * FROM dados")
variavel_comando=cursor.fetchall()

def temporario():
	data_e_hora_atuais = datetime.now()
	hora_atual = data_e_hora_atuais.strftime("%H")
	hjsjs=[["black","white","black","green"],["white","black","gray","light green"],["white","gray","black","light green"]]
	#hora_atual=18
	if(int(hora_atual)>=6 and int(hora_atual)<=11):
		return hjsjs[0]
	if(int(hora_atual)>=12 and int(hora_atual)<=17):
		return hjsjs[2]
	if(int(hora_atual)>=18 or int(hora_atual)<=5):
		return hjsjs[1]



bg_geral=[["black","white","black","green"],["white","black","gray","light green"],["white","gray","black","light green"],temporario()]


# fg  bg   
idiom=[[" Jogar ", " Configurações ", " Sair ", "<- voltar " , " Salvar " , " Sozinho "," Normal "," Online "," Local "," Fácil "," Médio "," Difício "," Idioma "," Sobre "," Tema "," Português Br"," Espanhol "," Inglês "," Francês "," Branco "," Preto "," Autor : Lucas Gabriel da Silva Lima "," Inicio do projeto : 11/12/2020 ","Este aplicativo foi criado para conhecimento e ele engloba um jogo multiplay com host local , online ou contra boot. ", " Jogar novamente "," ERRO este lugar esta ocupado "," Ser o primeiro a jogar "," Empate "," Você ganhou "," Você perdeu "," Facil "," Medio "," Dificil "," Ganhou "," ERRO : nome inválido "," Máximo de 12 caracteres "," Jogador 1 "," Jogador 2 "," Sons "," Toque "," Erro "," Resultado "," Cinza "," Temporario "," Personalizado ","v : 0.9"]

,["Reproducir", "Configuración", "Salir", "<- atrás", "Guardar", "Solo", "Normal", "En línea", "Local", "Fácil", "Medio", "Agujero"  , "Idioma", "Acerca de", "Tema", "Portugués brasileño", "Español", "Inglés", "Francés", "Blanco", "Negro", "Autor: Lucas Gabriel da Silva Lima", "Inicio  del proyecto: 11/12/2020 "," Esta aplicación fue creada para el conocimiento y abarca un juego multijugador con host local, en línea o contra arranque. "," Jugar de nuevo "," ERROR este lugar es  ocupado "," Sé el primero en jugar "," Empate "," Ganaste "," Perdiste "," Fácil "," Medio "," Difícil "," Ganado "," ERROR: nombre no válido "," Máximo  12 caracteres "," Jugador 1 "," Jugador 2 "," Sonidos "," Tono de llamada "," Error "," Resultado ","v : 0.9"],

["Play", "Settings", "Exit", "<- back", "Save", "Alone", "Normal", "Online", "Local", "Easy", "Medium", "Hole"  , "Language", "About", "Theme", "Brazilian Portuguese", "Spanish", "English", "French", "White", "Black", "Author: Lucas Gabriel da Silva Lima", "Home  of the project: 11/12/2020 ","This application was created for knowledge and it encompasses a multiplayer game with local host,online or against boot. "," Play again "," ERROR this place is  busy "," Be the first to play "," Draw "," You won "," You lost "," Easy "," Medium "," Hard "," Won "," ERROR: invalid name "," Maximum  12 character "," Player 1 "," Player 2 "," Sounds "," Ringtone "," Error "," Result ","v : 0.9"],

["Lecture", "Paramètres", "Quitter", "<- retour", "Enregistrer", "Seul", "Normal", "En ligne", "Local", "Facile", "Moyen", "Trou"  , "Langue", "À propos de", "Thème", "Portugais brésilien", "Espagnol", "Anglais", "Français", "Blanc", "Noir", "Auteur: Lucas Gabriel da Silva Lima", "Accueil  du projet: 11/12/2020 ","Cette application a été créée pour la connaissance et elle englobe une partie multijoueur avec hôte local, en ligne ou contre le démarrage. "," Rejouer "," ERREUR cet endroit est  occupé "," Soyez le premier à jouer "," Dessiner "," Vous avez gagné "," Vous avez perdu "," Facile "," Moyen "," Difficile "," Gagné "," ERREUR: nom invalide "," Maximum  12 caractères "," Player 1 "," Player 2 "," Sounds "," Ringtone "," Error "," Result ","v : 0.9"]]

meu_icone=""
icone_adversario=""
minha_cor=""
cor_adversaria=""
tabuleiro=['','','','','','','','','']
iniciar_partida=False
nivel=""

nome_do_adversario=""
meu_nome=""
troca_icone=""
troca_cor=""
quem_comeca=0

icone_ganhador=""
posicao_final=['','','']
som_inicial=False

sec = None
master2=tk
resolucao=""

caminho_imagem_fundo='image/images (16).jpeg'


def porcento(comprimento,por):
	if comprimento <= 800:
		tela=(35 * comprimento)/comprimento
	else:
		tela=(75 * comprimento)/comprimento
	return int((por * tela)/100)
	
def tam_tela(m):
	res=f'{m.winfo_screenwidth()}x{m.winfo_screenheight()}'
	return res
	
	
class SampleApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self._frame = None
		self.switch_frame(StartGame)
	def switch_frame(self, frame_class):
		global sec
		sec=None
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()
		

class StartGame(tk.Frame):
	def __init__(self, master,*args, **kwargs):
		tk.Frame.__init__(self, master ,  *args, **kwargs)
		
		global variavel_comando ,bg_geral ,idiom,som_inicial,resolucao,master2,caminho_imagem_fundo
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		resolucao=f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}'
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		master2=master
		
		if(som_inicial):
			som_save()
		som_inicial=True
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
		
		self.time=tk.Label(self,height=10,bg=bg_geral[variavel_comando[0][0]][1])
	#	self.time.grid(row=0,column=0,stick="w")
		
		#idiom[variavel_comando[0][1]][0]
		tk.Button(master, text=idiom[variavel_comando[0][1]][0],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],width=12,font=('arial', 11),command=lambda: master.switch_frame(jogar)).place(x=184,y=350)
		
		tk.Button(master,  text=idiom[variavel_comando[0][1]][1],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],width=12,font=('arial', 11),command=lambda: master.switch_frame(configuracao)).place(x=184,y=450)
		
		tk.Button(master,  text=idiom[variavel_comando[0][1]][2],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],width=12,font=('arial', 11),command=self.sair).place(x=184,y=550)
		
		self.tick()

	def sair(self):
		global banco
		banco.commit()
		exit()     

	def tick(self):
	   global sec,master2,resolucao
	   if sec == None:
	   	sec = int(0)
	   if sec >1:
	   	sec = sec +1
	   	#self.time['text'] = sec
	   	gjj=f'{master2.winfo_screenwidth()}x{master2.winfo_screenheight()}'
	   	#self.time['text'] = f"{resolucao}\n{gjj}"#sec
	   	#sec = sec +1
	   	
	   	if(resolucao != gjj):
	   		resolucao=f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}'
	   		master2.switch_frame(StartGame)
	   		
	   	self.time.after(1000, self.tick)
	   else:
	   	sec = sec +1
	   	#self.time['text'] = sec
	   	self.time.after(100, self.tick)

class jogar(tk.Frame):
	def __init__(self, master,*args, **kwargs):
		tk.Frame.__init__(self, master ,  *args, **kwargs)
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		try:
			pygame.mixer.music.stop()
		except:
			pass
		
			
		som_save()
		global variavel_comando ,bg_geral ,idiom,master2,nome_do_adversario,meu_nome,caminho_imagem_fundo
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		limpar_tabela()
		master2=master
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
		tk.Button(master, text=idiom[variavel_comando[0][1]][3],relief="flat",width=porcento(int(master.winfo_screenwidth()),22),command=lambda: master.switch_frame(StartGame)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),38)).place(x=198,y=0)
		# porcento(int(master.winfo_screenwidth()),50)
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),30)).place(x=504,y=0)
		#porcento(int(master.winfo_screenwidth()),10)
	#	tk.Label(self,height=3,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)
		
		tk.Button(master,width=28,text=idiom[variavel_comando[0][1]][5],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=lambda: master.switch_frame(Sozinho)).place(x=70,y=300)
		
		tk.Button(master,width=28,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=idiom[variavel_comando[0][1]][6],command=self.normal).place(x=70,y=400)
		
		tk.Button(master,width=28,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=idiom[variavel_comando[0][1]][7]).place(x=70,y=500)
		
		tk.Button(master,width=28,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=idiom[variavel_comando[0][1]][8]).place(x=70,y=600)
		
		cursor.execute("SELECT * FROM nomes")
		sghjh=cursor.fetchall()
		nome_do_adversario=sghjh[0][1]
		meu_nome=sghjh[0][0]

		
		
	def normal(self):
		global master2,meu_icone,icone_adversario,minha_cor ,cor_adversaria,nivel,quem_comeca,troca_icone,troca_cor
				
		ic=randint(0,1)
		quem_comeca=randint(0,1)
		if(quem_comeca == 0):
			troca_icone="X"
			troca_cor=bg_geral[variavel_comando[0][0]][3]
		if(quem_comeca == 1):
			troca_icone="O"
			troca_cor="blue"
			
		if(ic == 0):
			meu_icone="X"
		if(ic == 1):
			meu_icone="O"	
			
		if(meu_icone == "X"):
			icone_adversario="O"
			minha_cor=bg_geral[variavel_comando[0][0]][3]
			cor_adversaria="blue"
		if(meu_icone == "O"):
			icone_adversario="X"
			minha_cor="blue"
			cor_adversaria=bg_geral[variavel_comando[0][0]][3]
			
					
		nivel="embate normal"
		master2.switch_frame(nome_normal)
		
		
class Sozinho(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral ,idiom,master2,caminho_imagem_fundo
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		master2=master
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		tk.Button(master, text=idiom[variavel_comando[0][1]][3],relief="flat",width=porcento(int(master.winfo_screenwidth()),22),command=lambda: master.switch_frame(jogar)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),38)).place(x=198,y=0)
		tk.Button(master,relief="flat", width=porcento(int(master.winfo_screenwidth()),30)).place(x=504,y=0)
		
	#	tk.Label(self,height=3,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)
		
		tk.Button(master,width=28,text=idiom[variavel_comando[0][1]][9],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=self.facil).place(x=70,y=200)
		
		tk.Button(master,width=28,text=idiom[variavel_comando[0][1]][10],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=self.medio).place(x=70,y=300)
		
		tk.Button(master,width=28,text=idiom[variavel_comando[0][1]][11],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=self.dificil).place(x=70,y=400)
		
		self.var = StringVar()
		self.icone=tk.Radiobutton(master, text="X",font=('arial', 11),fg="green",bg=bg_geral[variavel_comando[0][0]][1], variable=self.var, value="X")
		self.icone.place(x=140,y=500)
		
		self.icone_2=tk.Radiobutton(master, text="O",font=('arial', 11),fg="blue",bg=bg_geral[variavel_comando[0][0]][1], variable=self.var, value="O")
		self.icone_2.place(x=450,y=500)
		
		self.icone.select()
		
		self.bsbsb = IntVar()
		
		self.inci_p=tk.Checkbutton(master, text=idiom[variavel_comando[0][1]][26],fg=bg_geral[variavel_comando[0][0]][2],bg=bg_geral[variavel_comando[0][0]][1], variable=self.bsbsb,onvalue = 0, offvalue = 1)
		self.inci_p.place(x=160,y=600)
		
		self.erro=Label(self,bg=bg_geral[variavel_comando[0][0]][1])
		self.erro.place(x=70,y=700)
		
		
	def facil(self):
		global master2,meu_icone,icone_adversario,iniciar_partida,minha_cor ,cor_adversaria,nivel,troca_icone,nome_do_adversario
		
		meu_icone=self.var.get()
		if(meu_icone == "X"):
			icone_adversario="O"
			minha_cor=bg_geral[variavel_comando[0][0]][3]
			cor_adversaria="blue"
		else:
			icone_adversario="X"
			minha_cor="blue"
			cor_adversaria=bg_geral[variavel_comando[0][0]][3]
			
		if(self.bsbsb.get() == 0):
			iniciar_partida=True
		else:
			iniciar_partida=False
			
		nivel="facil"
		troca_icone=meu_icone
		nome_do_adversario=idiom[variavel_comando[0][1]][30]
		master2.switch_frame(partida)
		
		
	def dificil(self):
		global master2,meu_icone,icone_adversario,iniciar_partida,minha_cor ,cor_adversaria,nivel,troca_icone,nome_do_adversario
		
		meu_icone=self.var.get()
		if(meu_icone == "X"):
			icone_adversario="O"
			minha_cor=bg_geral[variavel_comando[0][0]][3]
			cor_adversaria="blue"
		else:
			icone_adversario="X"
			minha_cor="blue"
			cor_adversaria=bg_geral[variavel_comando[0][0]][3]
			
		if(self.bsbsb.get() == 0):
			iniciar_partida=True
		else:
			iniciar_partida=False
			
		nivel="dificil"
		troca_icone=meu_icone
		nome_do_adversario=idiom[variavel_comando[0][1]][32]
		master2.switch_frame(partida)
		
		
	def medio(self):
		global master2,meu_icone,icone_adversario,iniciar_partida,minha_cor ,cor_adversaria,nivel,troca_icone,nome_do_adversario
		
		meu_icone=self.var.get()
		if(meu_icone == "X"):
			icone_adversario="O"
			minha_cor=bg_geral[variavel_comando[0][0]][3]
			cor_adversaria="blue"
		else:
			icone_adversario="X"
			minha_cor="blue"
			cor_adversaria=bg_geral[variavel_comando[0][0]][3]
			
		if(self.bsbsb.get() == 0):
			iniciar_partida=True
		else:
			iniciar_partida=False
			
		nivel="medio"
		troca_icone=meu_icone
		nome_do_adversario=idiom[variavel_comando[0][1]][31]
		master2.switch_frame(partida)
		

class partida(tk.Frame):
	def __init__(self, master):
		som_save()
		try:
			pygame.mixer.music.stop()
		except:
			pass
			
		global variavel_comando ,bg_geral ,idiom,meu_icone,icone_adversario,minha_cor ,cor_adversaria,tabuleiro,master2,quem_comeca,troca_icone,nome_do_adversario,meu_nome,caminho_imagem_fundo
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		limpar_tabela()
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
		master2=master
		
		tk.Button(master, text=idiom[variavel_comando[0][1]][2],relief="flat",command=lambda: master.switch_frame(jogar),width=porcento(int(master.winfo_screenwidth()),24)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),50)).place(x=216,y=0)
		tk.Button(master,relief="flat", width=porcento(int(master.winfo_screenwidth()),10)).place(x=594,y=0)
	#	tk.Label(self,height=2,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=2,column=0)
		
		if(icone_adversario == troca_icone):
			self.bt_meu_adversario=tk.Button(master,text=icone_adversario,bg=bg_geral[variavel_comando[0][0]][1],fg=cor_adversaria,width=2,height=2)
			self.bt_meu_adversario.place(x=15,y=80)
			
			self.nome_adversario=tk.Label(master,text=nome_do_adversario,bg=bg_geral[variavel_comando[0][0]][1],fg=cor_adversaria,width=12)
			self.nome_adversario.place(x=128,y=105)
			
		else:
			
			self.bt_meu_adversario=tk.Button(master,text=icone_adversario,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2],width=2,height=2)
			self.bt_meu_adversario.place(x=15,y=80)
			
			self.nome_adversario=tk.Label(master,text=nome_do_adversario,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2],width=12)
			self.nome_adversario.place(x=128,y=105)
#			
			
		self.botoes=[0,0,0,0,0,0,0,0,0]
		# LINHA 1
		
		self.botoes[0]=tk.Button(master,text=tabuleiro[0],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_01_command)
		self.botoes[0].place(x=110,y=300)
		
		self.botoes[1]=tk.Button(master,text=tabuleiro[1],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_02_command)
		self.botoes[1].place(x=280,y=300)
		
		self.botoes[2]=tk.Button(master,text=tabuleiro[2],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_03_command)
		self.botoes[2].place(x=450,y=300)
		
#		# LINHA 2
#		
		self.botoes[3]=tk.Button(master,text=tabuleiro[3],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_04_command)
		self.botoes[3].place(x=110,y=450)
		
		self.botoes[4]=tk.Button(master,text=tabuleiro[4],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_05_command)
		self.botoes[4].place(x=280,y=450)
		
		self.botoes[5]=tk.Button(master,text=tabuleiro[5],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_06_command)
		self.botoes[5].place(x=450,y=450)
		
#		# LINHA 3
		
		self.botoes[6]=tk.Button(master,text=tabuleiro[6],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_07_command)
		self.botoes[6].place(x=110,y=600)
		
		self.botoes[7]=tk.Button(master,text=tabuleiro[7],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_08_command)
		self.botoes[7].place(x=280,y=600)
		
		self.botoes[8]=tk.Button(master,text=tabuleiro[8],bg=bg_geral[variavel_comando[0][0]][1],fg="light green",width=5,height=3,command=self.bt_09_command)
		self.botoes[8].place(x=450,y=600)
#		
#		tk.Label(self,height=2,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=6,column=0)
#		
		if(meu_icone ==  troca_icone):
			self.bt_meu_icone=tk.Button(master,text=meu_icone,bg=bg_geral[variavel_comando[0][0]][1],fg=minha_cor,width=2,height=2)
			self.bt_meu_icone.place(x=330,y=860)
			
			self.meu_nome=tk.Label(master,text=meu_nome,bg=bg_geral[variavel_comando[0][0]][1],fg=minha_cor,width=12)
			self.meu_nome.place(x=450,y=890)
			
		else:
			self.bt_meu_icone=tk.Button(master,text=meu_icone,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2],width=2,height=2)
			self.bt_meu_icone.place(x=330,y=860)
			
			self.meu_nome=tk.Label(master,text=meu_nome,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2],width=12)
			self.meu_nome.place(x=450,y=890)
		
		self.erro=tk.Label(master,text="",bg=bg_geral[variavel_comando[0][0]][1],fg="red")
		self.erro.place(x=140,y=1000)
		
		
		if(nivel == "facil" and iniciar_partida == False):
			ksbs=run_back.boot_easy(tabuleiro)
			self.botoes[ksbs]["text"]=f"{icone_adversario}"
			self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
			tabuleiro[ksbs]=icone_adversario
			
		if(nivel == "medio" and iniciar_partida == False):
			ksbs=run_back.boot_medio(tabuleiro,meu_icone)
			self.botoes[ksbs]["text"]=f"{icone_adversario}"
			self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
			tabuleiro[ksbs]=icone_adversario
		
		if(nivel == "dificil" and iniciar_partida == False):
			ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
			self.botoes[ksbs]["text"]=f"{icone_adversario}"
			self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
			tabuleiro[ksbs]=icone_adversario
		
	def bt_01_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,quem_comeca,troca_icone,nivel,troca_cor
	#	self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[0] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[0]["text"]=f"{troca_icone}"
					self.botoes[0]["fg"]=f"{troca_cor}"
					tabuleiro[0] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[0]["text"]=f"{meu_icone}"
				self.botoes[0]["fg"]=f"{minha_cor}"
				tabuleiro[0] = meu_icone
			
			if(ganhador() != "ninguem"):
				#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
					#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
			
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
			

	def bt_02_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,quem_comeca,troca_icone,nivel,troca_cor
		#self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[1] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[1]["text"]=f"{troca_icone}"
					self.botoes[1]["fg"]=f"{troca_cor}"
					tabuleiro[1] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[1]["text"]=f"{meu_icone}"
				self.botoes[1]["fg"]=f"{minha_cor}"
				tabuleiro[1] = meu_icone
			
			if(ganhador() != "ninguem"):
				#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
					#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
				
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
		

	def bt_03_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,quem_comeca,troca_icone,nivel,troca_cor
	#	self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[2] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[2]["text"]=f"{troca_icone}"
					self.botoes[2]["fg"]=f"{troca_cor}"
					tabuleiro[2] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[2]["text"]=f"{meu_icone}"
				self.botoes[2]["fg"]=f"{minha_cor}"
				tabuleiro[2] = meu_icone
			
			if(ganhador() != "ninguem"):
				#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
					#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
				
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
		
				
	def bt_04_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,quem_comeca,troca_icone,nivel,troca_cor
		#self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[3] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[3]["text"]=f"{troca_icone}"
					self.botoes[3]["fg"]=f"{troca_cor}"
					tabuleiro[3] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[3]["text"]=f"{meu_icone}"
				self.botoes[3]["fg"]=f"{minha_cor}"
				tabuleiro[3] = meu_icone
			
			if(ganhador() != "ninguem"):
				#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
					#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
				
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
			
						
	def bt_05_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,quem_comeca,troca_icone,nivel,troca_cor
		#self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[4] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[4]["text"]=f"{troca_icone}"
					self.botoes[4]["fg"]=f"{troca_cor}"
					tabuleiro[4] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[4]["text"]=f"{meu_icone}"
				self.botoes[4]["fg"]=f"{minha_cor}"
				tabuleiro[4] = meu_icone
			
			if(ganhador() != "ninguem"):
				#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
				#	self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
				
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
		
						
	def bt_06_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,quem_comeca,troca_icone,nivel,troca_cor
		#self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[5] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[5]["text"]=f"{troca_icone}"
					self.botoes[5]["fg"]=f"{troca_cor}"
					tabuleiro[5] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[5]["text"]=f"{meu_icone}"
				self.botoes[5]["fg"]=f"{minha_cor}"
				tabuleiro[5] = meu_icone
			
			if(ganhador() != "ninguem"):
				#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
					#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
			
						
	def bt_07_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,quem_comeca,troca_icone,nivel,troca_cor
	#	self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[6] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[6]["text"]=f"{troca_icone}"
					self.botoes[6]["fg"]=f"{troca_cor}"
					tabuleiro[6] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[6]["text"]=f"{meu_icone}"
				self.botoes[6]["fg"]=f"{minha_cor}"
				tabuleiro[6] = meu_icone
			
			if(ganhador() != "ninguem"):
			#	self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
			#		self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
				
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
			
						
	def bt_08_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,icone_adversario,quem_comeca,troca_icone,nivel,troca_cor
		
		#self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[7] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[7]["text"]=f"{troca_icone}"
					self.botoes[7]["fg"]=f"{troca_cor}"
					tabuleiro[7] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[7]["text"]=f"{meu_icone}"
				self.botoes[7]["fg"]=f"{minha_cor}"
				tabuleiro[7] = meu_icone
			
			if(ganhador() != "ninguem"):
				#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
					#self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
				
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
			
						
	def bt_09_command(self):
		global tabuleiro,meu_icone,minha_cor,master2,quem_comeca,troca_icone,nivel,troca_cor
		#self.erro["text"]=f"{tabuleiro}"
		if(tabuleiro[8] == ''):
			som_save()
			self.erro["text"]=""
			if(nivel == "embate normal"):
				while True:
					self.botoes[8]["text"]=f"{troca_icone}"
					self.botoes[8]["fg"]=f"{troca_cor}"
					tabuleiro[8] = troca_icone
					
					if(troca_icone == "X" and meu_icone == "X"):
						troca_icone = "O"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
					if(troca_icone == "O" and meu_icone == "O"):
						troca_icone = "X"
						troca_cor=cor_adversaria
						self.meu_nome["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_icone["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.nome_adversario["fg"]=cor_adversaria
						self.bt_meu_adversario["fg"]=cor_adversaria
						break
						
					if(troca_icone == "X" and icone_adversario == "X"):
						troca_icone = "O"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
					if(troca_icone == "O" and icone_adversario =="O"):
						troca_icone = "X"
						troca_cor=minha_cor
						self.meu_nome["fg"]=minha_cor
						self.bt_meu_icone["fg"]=minha_cor
						self.nome_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						self.bt_meu_adversario["fg"]=bg_geral[variavel_comando[0][0]][2]
						break
				
			if(nivel != "embate normal"):
				self.botoes[8]["text"]=f"{meu_icone}"
				self.botoes[8]["fg"]=f"{minha_cor}"
				tabuleiro[8] = meu_icone
			
			if(ganhador() != "ninguem"):
			#	self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
				master2.switch_frame(vencedor)
				
			else:
				if(nivel == "facil"):
					ksbs=run_back.boot_easy(tabuleiro)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "medio"):
					ksbs=run_back.boot_medio(tabuleiro,meu_icone)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(nivel == "dificil"):
					ksbs=run_back.boot_dificil(tabuleiro,meu_icone,icone_adversario)
					self.botoes[ksbs]["text"]=f"{icone_adversario}"
					self.botoes[ksbs]["fg"]=f"{cor_adversaria}"
					tabuleiro[ksbs]=icone_adversario
					
				if(ganhador() != "ninguem"):
				#	self.erro["text"]=f"{ganhador()}\n{tabuleiro}"
					master2.switch_frame(vencedor)
				
		else:
			self.erro["text"]=idiom[variavel_comando[0][1]][25]
			som_erro()
			
				
class nome_normal(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral ,idiom,master2,nome_do_adversario,meu_nomecaminho_imagem_fundo
		
		limpar_tabela()
		master2=master
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
		tk.Button(master, text=idiom[variavel_comando[0][1]][3],relief="flat",command=lambda: master.switch_frame(jogar),width=porcento(int(master.winfo_screenwidth()),22)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),38)).place(x=198,y=0)
		tk.Button(master,relief="flat", width=porcento(int(master.winfo_screenwidth()),30)).place(x=504,y=0)
		
		
		tk.Label(master,text=idiom[variavel_comando[0][1]][36],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).place(x=20,y=150)
		
		self.m=tk.Entry(master,width=20,text=v(meu_nome),fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1])
		self.m.place(x=200,y=150)
		
			
		tk.Label(master,text=idiom[variavel_comando[0][1]][37],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1]).place(x=20,y=220)
		
		self.a=tk.Entry(master,width=20,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=v(nome_do_adversario))
		self.a.place(x=200,y=220)
		
		tk.Button(master,width=28,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=idiom[variavel_comando[0][1]][0],command=self.salvar).place(x=80,y=400)
		
		self.erro=tk.Label(master,fg="red",text=idiom[variavel_comando[0][1]][35],bg=bg_geral[variavel_comando[0][0]][1])
		self.erro.place(x=150,y=300)
		
		
	def salvar(self):
		global cursor , banco,master2,nome_do_adversario,meu_nome
		if(len(self.m.get().strip()) > 12 or len(self.a.get().strip()) > 12 or len(self.m.get().strip()) == 0 or len(self.a.get().strip()) == 0):
			self.erro["text"]=f"{idiom[variavel_comando[0][1]][34]}"
			som_erro_2()
	
		else:		
			cursor.execute(f"UPDATE nomes SET meu = ? , dele = ?",(self.m.get(),self.a.get()))
			
			banco.commit()
			cursor.execute("SELECT * FROM nomes")
			sghjh=cursor.fetchall()
			nome_do_adversario=sghjh[0][1]
			meu_nome=sghjh[0][0]
			master2.switch_frame(partida)		

			
def v(t):
    i = tk.StringVar()
    i.set(t)
    return i			
			
def ganhador():
	global tabuleiro,icone_ganhador,posicao_final
	
	#  Colunas
	if(tabuleiro[0] == tabuleiro[1]  and tabuleiro[1] == tabuleiro[2] and tabuleiro[1] != "" ):
		icone_ganhador = f"{tabuleiro[1]} ganhou"
		posicao_final[0]=0
		posicao_final[1]=1
		posicao_final[2]=2
		return f"{tabuleiro[1]} ganhou"
		
	if(tabuleiro[3] == tabuleiro[4] and tabuleiro[4] == tabuleiro[5] and tabuleiro[4] != ""):
		icone_ganhador = f"{tabuleiro[4]} ganhou"
		posicao_final[0]=3
		posicao_final[1]=4
		posicao_final[2]=5
		return f"{tabuleiro[4]} ganhou"
		
	if(tabuleiro[6] == tabuleiro[7] and tabuleiro[7] == tabuleiro[8]  and tabuleiro[7] != ""):
		icone_ganhador = f"{tabuleiro[7]} ganhou"
		posicao_final[0]=6
		posicao_final[1]=7
		posicao_final[2]=8
		return f"{tabuleiro[7]} ganhou"
		
	# linhas
		
	if(tabuleiro[0] == tabuleiro[3]  and tabuleiro[3] == tabuleiro[6] and tabuleiro[3] != ""):
		icone_ganhador = f"{tabuleiro[3]} ganhou"
		posicao_final[0]=0
		posicao_final[1]=3
		posicao_final[2]=6
		return f"{tabuleiro[3]} ganhou"

		
	if(tabuleiro[1] == tabuleiro[4] and tabuleiro[4] == tabuleiro[7] and tabuleiro[4] != ""):
		icone_ganhador = f"{tabuleiro[4]} ganhou"
		posicao_final[0]=1
		posicao_final[1]=4
		posicao_final[2]=7
		return f"{tabuleiro[4]} ganhou"
		
		
	if(tabuleiro[2] == tabuleiro[5] and tabuleiro[5] == tabuleiro[8] and tabuleiro[5] != ""):
		icone_ganhador = f"{tabuleiro[5]} ganhou"
		posicao_final[0]=2
		posicao_final[1]=5
		posicao_final[2]=8
		return f"{tabuleiro[5]} ganhou"
		
	
	#   Laterais
	
	if(tabuleiro[0] == tabuleiro[4]  and tabuleiro[4] == tabuleiro[8] and tabuleiro[4] != ""):
		icone_ganhador = f"{tabuleiro[4]} ganhou"
		posicao_final[0]=0
		posicao_final[1]=4
		posicao_final[2]=8
		return f"{tabuleiro[4]} ganhou"
		
	if(tabuleiro[2] == tabuleiro[4] and tabuleiro[4] == tabuleiro[6] and tabuleiro[4] != ""):
		icone_ganhador = f"{tabuleiro[4]} ganhou"
		posicao_final[0]=2
		posicao_final[1]=4
		posicao_final[2]=6
		return f"{tabuleiro[4]} ganhou"
		
	if( "" not in tabuleiro):
		icone_ganhador = "empate"
		return "empate"
	else:
		return "ninguem"
		
	
		
#  0 1 2
#  3 4 5
#  6 7 8			

def limpar_tabela():
	global tabuleiro,posicao_final
	for c in range(0,9):
		tabuleiro[c]=""
	posicao_final[0]=""
	posicao_final[1]=""
	posicao_final[2]=""
					
class vencedor(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral ,idiom,meu_icone,icone_ganhador,minha_cor,cor_adversaria,meu_nome,nome_do_adversario,caminho_imagem_fundo
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
	#	tk.Button(self, text="                  ",relief="flat").grid(row=0,column=0)
#		
#		tk.Button(self,relief="flat",width=18).grid(row=0,column=1)
#		tk.Button(self,relief="flat", text="            ").grid(row=0,column=2)
#		tk.Label(self,height=3,bg=bg_geral[variavel_comando[0][0]][1]).grid(row=1,column=0)
		
		bdhd=list(icone_ganhador)
		if(nivel == "embate normal"):
			
			if(meu_icone == str(bdhd[0])):
				if(randint(0,1) == 0):
					som_ganhou()
				else:
					som_perdeu()
				tk.Label(master,text=f"{meu_nome} {idiom[variavel_comando[0][1]][33]}",font=("arial",12),bg=bg_geral[variavel_comando[0][0]][1], fg=minha_cor,anchor="w").place(x=70,y=100)
				
			if(meu_icone != str(bdhd[0]) and bdhd[0] != "e"):
				if(randint(0,1) == 0):
					som_ganhou()
				else:
					som_perdeu()
				tk.Label(master,text=f"{nome_do_adversario} {idiom[variavel_comando[0][1]][33]}",font=("arial",12),bg=bg_geral[variavel_comando[0][0]][1], fg=cor_adversaria,anchor="w").place(x=200,y=100)
				
			if(bdhd[0] == "e"):
				som_resultado()
				tk.Label(master,text=idiom[variavel_comando[0][1]][27],font=("arial",12),bg=bg_geral[variavel_comando[0][0]][1], fg="yellow",anchor="w").place(x=200,y=100)
				
		#	tk.Label(self,text=f"",bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][0],anchor="w").grid(row=3,column=0,columnspan=3,stick="w")
			
		else:
			if(meu_icone == str(bdhd[0])):
				som_ganhou()
				tk.Label(master,text=idiom[variavel_comando[0][1]][28],font=("arial",12),bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][3],anchor="w").place(x=200,y=100)
				
			if(meu_icone != str(bdhd[0]) and bdhd[0] != "e"):
				som_perdeu()
				tk.Label(master,text=idiom[variavel_comando[0][1]][29],font=("arial",12),bg=bg_geral[variavel_comando[0][0]][1], fg="red",anchor="w").place(x=200,y=100)
				
			if(bdhd[0] == "e"):
				som_resultado()
				tk.Label(master,text=idiom[variavel_comando[0][1]][27],font=("arial",12),bg=bg_geral[variavel_comando[0][0]][1], fg="yellow",anchor="w").place(x=200,y=100)
				

#		
		# linha 1
		if(0 not in posicao_final):
			bt_00=tk.Button(master,text=tabuleiro[0],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=170,y=200)
		else:
			bt_00=tk.Button(master,text=tabuleiro[0],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=170,y=200)
		
		if(1 not in posicao_final):
			bt_01=tk.Button(master,text=tabuleiro[1],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=290,y=200)
		else:
			bt_01=tk.Button(master,text=tabuleiro[1],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=290,y=200)
		
		if(2 not in posicao_final):
			bt_02=tk.Button(master,text=tabuleiro[2],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=410,y=200)
		else:
			bt_02=tk.Button(master,text=tabuleiro[2],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=410,y=200)
			
		# linha 2
		
		if(3 not in posicao_final):
			bt_03=tk.Button(master,text=tabuleiro[3],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=170,y=313)
		else:
			bt_03=tk.Button(master,text=tabuleiro[3],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=170,y=313)
		
		if(4 not in posicao_final):
			bt_04=tk.Button(master,text=tabuleiro[4],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=290,y=313)
		else:
			bt_04=tk.Button(master,text=tabuleiro[4],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=290,y=313)
		
		if(5 not in posicao_final):
			bt_05=tk.Button(master,text=tabuleiro[5],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=410,y=313)
		else:
			bt_05=tk.Button(master,text=tabuleiro[5],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=410,y=313)
		
#		# linha 3
#		
		if(6 not in posicao_final):
			bt_06=tk.Button(master,text=tabuleiro[6],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=170,y=426)
		else:
			bt_06=tk.Button(master,text=tabuleiro[6],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=170,y=426)
		
		if(7 not in posicao_final):
			bt_07=tk.Button(master,text=tabuleiro[7],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=290,y=426)
		else:
			bt_07=tk.Button(master,text=tabuleiro[7],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=290,y=426)
		
		if(8 not in posicao_final):
			bt_08=tk.Button(master,text=tabuleiro[8],bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][0],width=2,height=2).place(x=410,y=426)
		else:
			bt_08=tk.Button(master,text=tabuleiro[8],bg=bg_geral[variavel_comando[0][0]][1],fg="red",width=2,height=2).place(x=410,y=426)
			
		tk.Button(master, text=idiom[variavel_comando[0][1]][24],command=lambda: master.switch_frame(partida)).place(x=70,y=590)
		
		tk.Button(master, text=idiom[variavel_comando[0][1]][2],command=lambda: master.switch_frame(jogar)).place(x=410,y=590)
		
																												
class configuracao(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral ,idiom,caminho_imagem_fundo
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		
		tk.Button(master, text=idiom[variavel_comando[0][1]][3],relief="flat",command=lambda: master.switch_frame(StartGame),width=porcento(int(master.winfo_screenwidth()),22)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),38)).place(x=198,y=0)
		tk.Button(master,relief="flat", width=porcento(int(master.winfo_screenwidth()),30)).place(x=504,y=0)
		
		tk.Button(master,width=28,text=idiom[variavel_comando[0][1]][12],fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],command=lambda: master.switch_frame(idiomas)).place(x=80,y=300)
		
		tk.Button(master,width=28,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=idiom[variavel_comando[0][1]][13],command=lambda: master.switch_frame(sobre)).place(x=80,y=400)
		
		tk.Button(master,width=28,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=idiom[variavel_comando[0][1]][14],command=lambda: master.switch_frame(aparencia)).place(x=80,y=500)
		
		tk.Button(master,width=28,fg=bg_geral[variavel_comando[0][0]][0],bg=bg_geral[variavel_comando[0][0]][1],text=idiom[variavel_comando[0][1]][38],command=lambda: master.switch_frame(sons)).place(x=80,y=600)
		
		
class idiomas(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral ,idiom,master2,caminho_imagem_fundo
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		master2=master
		tk.Button(master, text=idiom[variavel_comando[0][1]][3],relief="flat",command=lambda: master.switch_frame(configuracao),width=porcento(int(master.winfo_screenwidth()),22)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),38)).place(x=198,y=0)
		tk.Button(master,relief="flat", width=porcento(int(master.winfo_screenwidth()),30)).place(x=504,y=0)
		
		self.var = IntVar()
		port=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][15],font=('arial', 8), variable=self.var, value=0,command=self.salvar)#,command=sel)
		port.place(x=80,y=200)
		
		ingl=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2], text=idiom[variavel_comando[0][1]][16],font=('arial', 8), variable=self.var, value=1,command=self.salvar)#,command=sel)
		ingl.place(x=80,y=300)
		
		espanhol=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][17],font=('arial', 8), variable=self.var, value=2,command=self.salvar)#,command=sel)
		espanhol.place(x=80,y=400)
		
		fraces=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][18],font=('arial', 8), variable=self.var, value=3,command=self.salvar)#,command=sel)
		fraces.place(x=80,y=500)
		
		if(variavel_comando[0][1] == 0):
			port.select()
		if(variavel_comando[0][1] == 1):
			ingl.select()
		if(variavel_comando[0][1] == 2):
			espanhol.select()
		if(variavel_comando[0][1] == 3):
			fraces.select()
		

	def salvar(self):
		global cursor , banco,variavel_comando,master2
		cursor.execute(f"UPDATE dados SET idioma = ? ",(self.var.get(),))
		
		banco.commit()
		cursor.execute("SELECT * FROM dados")
		variavel_comando=cursor.fetchall()
		som_save()
		master2.switch_frame(idiomas)


class sons(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral ,idiom,master2,caminho_imagem_fundo
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		master2=master
		tk.Button(master, text=idiom[variavel_comando[0][1]][3],relief="flat",command=lambda: master.switch_frame(configuracao),width=porcento(int(master.winfo_screenwidth()),22)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),38)).place(x=198,y=0)
		tk.Button(master,relief="flat", width=porcento(int(master.winfo_screenwidth()),30)).place(x=504,y=0)
		
		self.var_1 = StringVar()
		self.var_2= StringVar()
		self.var_3= StringVar()
		
		port=tk.Checkbutton(master,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][39],font=('arial', 8), variable=self.var_1, onvalue = "True", offvalue = "False",command=self.salvar)#,command=sel)
		port.place(x=80,y=200)
		
		ingl=tk.Checkbutton(master,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2], text=idiom[variavel_comando[0][1]][40],font=('arial', 8), variable=self.var_2,  onvalue = "True", offvalue = "False",command=self.salvar)#,command=sel)
		ingl.place(x=80,y=290)
		
		espanhol=tk.Checkbutton(master,bg=bg_geral[variavel_comando[0][0]][1],fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][41],font=('arial', 8), variable=self.var_3,  onvalue = "True", offvalue = "False",command=self.salvar)#,command=sel)
		espanhol.place(x=80,y=380)
		
		
		cursor.execute("SELECT * FROM sons")
		vshjej=cursor.fetchall()
		
		if(vshjej[0][0] == "True"):
			port.select()
		if(vshjej[0][1] == "True"):
			ingl.select()
		if(vshjej[0][2] == "True"):
			espanhol.select()
#		if(vshjej[0][1] == True):
#			fraces.select()
		

	def salvar(self):
		global cursor , banco,variavel_comando,master2
		cursor.execute(f"UPDATE sons SET toque = ? ,erro = ?,resultado = ?",(self.var_1.get(),self.var_2.get(),self.var_3.get(),))
		
		banco.commit()
		cursor.execute("SELECT * FROM dados")
		variavel_comando=cursor.fetchall()
		som_save()
		master2.switch_frame(sons)
		
						
class aparencia(tk.Frame):
	def __init__(self, master):
		som_save()
		global variavel_comando ,bg_geral ,idiom,master2,caminho_imagem_fundo
		
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		master2=master
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		tk.Button(master, text=idiom[variavel_comando[0][1]][3],relief="flat",command=lambda: master.switch_frame(configuracao),width=porcento(int(master.winfo_screenwidth()),22)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),38)).place(x=198,y=0)
		tk.Button(master,relief="flat", width=porcento(int(master.winfo_screenwidth()),30)).place(x=504,y=0)
		
		self.var = IntVar()
		
		self.b=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][19],font=('arial', 8), variable=self.var, value=0,command=self.salvar)
		self.b.place(x=60,y=200)
		
		self.p=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][20],font=('arial', 8), variable=self.var, value=1,command=self.salvar)
		self.p.place(x=60,y=270)
		
		self.q=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][42
		],font=('arial', 8), variable=self.var, value=2,command=self.salvar)
		self.q.place(x=60,y=340)
		
		self.k=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][43
		],font=('arial', 8), variable=self.var, value=3,command=self.salvar)
		self.k.place(x=60,y=410)
		
		self.pers=tk.Radiobutton(master,bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][2],text=idiom[variavel_comando[0][1]][44
		],font=('arial', 8), variable=self.var, value=4,command=self.salvar)
		self.pers.place(x=60,y=480)
		
		if(variavel_comando[0][0] == 0):
			self.b.select()
		if(variavel_comando[0][0] == 1):
			self.p.select()
		if(variavel_comando[0][0] == 2):
			self.q.select()
		if(variavel_comando[0][0] == 3):
			self.k.select()
		if(variavel_comando[0][0] == 4):
			self.pers.select()
			
	def salvar(self):
		global cursor , banco,variavel_comando,master2
		cursor.execute(f"UPDATE dados SET bg = ? ",(self.var.get(),))
		
		banco.commit()
		cursor.execute("SELECT * FROM dados")
		variavel_comando=cursor.fetchall()
		som_save()
		master2.switch_frame(aparencia)


class sobre(tk.Frame): 
	def __init__(self, master):
		global variavel_comando ,bg_geral ,idiom,caminho_imagem_fundo
		som_save()
		tk.Frame.__init__(self, master)
		master["bg"]=bg_geral[variavel_comando[0][0]][1]
		tk.Frame.__init__(self, master)
		tk.Frame.configure(self,bg=bg_geral[variavel_comando[0][0]][1])
		
		master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
		
		self.image_2 = Image.open(caminho_imagem_fundo)
		
		self.photo_2 = ImageTk.PhotoImage(self.image_2.resize((master.winfo_screenwidth(),master.winfo_screenheight())))#master.winfo_screenwidth(),master.winfo_screenheight())))
		self.imagem = tk.Label(master,image = self.photo_2)
		self.imagem.image = self.photo_2
		self.imagem.place(x=0,y=0)
		
		tk.Button(master, text=idiom[variavel_comando[0][1]][3],relief="flat",command=lambda: master.switch_frame(configuracao),width=porcento(int(master.winfo_screenwidth()),22)).place(x=0,y=0)
		
		tk.Button(master,relief="flat",width=porcento(int(master.winfo_screenwidth()),38)).place(x=198,y=0)
		tk.Button(master,relief="flat", width=porcento(int(master.winfo_screenwidth()),30)).place(x=504,y=0)
		
		
		tk.Label(master,text=idiom[variavel_comando[0][1]][21],bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][0],anchor="w").place(x=20,y=200)
		
		tk.Label(master,text=idiom[variavel_comando[0][1]][22],bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][0],anchor="w").place(x=20,y=270)
		
		tk.Label(master,wraplength=int(master.winfo_screenwidth())-40,text=idiom[variavel_comando[0][1]][23],bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][0]).place(x=20,y=350)
		
		tk.Label(master,wraplength=int(master.winfo_screenwidth())-20,text=idiom[variavel_comando[0][1]][45],bg=bg_geral[variavel_comando[0][0]][1], fg=bg_geral[variavel_comando[0][0]][0]).place(x=20,y=500)
		

def som_erro():
		cursor.execute("SELECT * FROM sons")
		vshjej=cursor.fetchall()
		if(vshjej[0][1] == "True"):
			pygame.init()
			pygame.mixer.music.load('sons/som_erro(2).mp3')
			pygame.mixer.music.play()
			pygame.event.wait()
		
def som_erro_2():
		cursor.execute("SELECT * FROM sons")
		vshjej=cursor.fetchall()
		if(vshjej[0][1] == "True"):
			pygame.init()
			pygame.mixer.music.load('sons/erro.mp3')
			pygame.mixer.music.play()
			pygame.event.wait()
		
def som_ganhou():
		cursor.execute("SELECT * FROM sons")
		vshjej=cursor.fetchall()
		if(vshjej[0][2] == "True"):
			audio=os.listdir('sons/audio interativo/ganhou')
			audio_selec='sons/audio interativo/ganhou/'+str(audio[randint(0,len(audio)-1)])
			pygame.init()
			pygame.mixer.music.load(audio_selec)
			pygame.mixer.music.play()
			pygame.event.wait()
		
def som_perdeu():
		cursor.execute("SELECT * FROM sons")
		vshjej=cursor.fetchall()
		if(vshjej[0][2] == "True"):
			audio=os.listdir('sons/audio interativo/perdeu')
			audio_selec='sons/audio interativo/perdeu/'+str(audio[randint(0,len(audio)-1)])
			pygame.init()
			pygame.mixer.music.load(audio_selec)
			pygame.mixer.music.play()
			pygame.event.wait()
		
def som_save():
		cursor.execute("SELECT * FROM sons")
		vshjej=cursor.fetchall()
		if(vshjej[0][0] == "True"):
			pygame.init()
			pygame.mixer.music.load('sons/som_save.mp3')
			pygame.mixer.music.play()
			pygame.event.wait()
		
def som_resultado():
		cursor.execute("SELECT * FROM sons")
		vshjej=cursor.fetchall()
		if(vshjej[0][2] == "True"):
			audio=os.listdir('sons/audio interativo/empate')
			audio_selec='sons/audio interativo/empate/'+str(audio[randint(0,len(audio)-1)])
			pygame.init()
			pygame.mixer.music.load(audio_selec)
			pygame.mixer.music.play()
			pygame.event.wait()
		
if __name__ == "__main__":
    app = SampleApp()
    app.title("Jogo da Velha")
    try:
    	imagem = Image.open('images (1).ico')
    	dgh=imagem.load()
    	twstg=ImageTk.PhotoImage(imagem)
    	app.iconbitmap(imagem)
    except:
    	pass
    app.mainloop()
    
# criar adaptavel
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()
