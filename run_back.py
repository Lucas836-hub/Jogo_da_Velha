# Funcos jogoda velha

# por enquanto ,tocar quando o sol chegar ,  o gago , temos todo o tempo do mundo , 

from random import randint

def boot_easy(tabuleiro):
	while True:
		ran=randint(0,8)
		if (tabuleiro[ran] == ""):
			return ran

def boot_medio(tabuleiro,icone):
	tabuleiro=tabuleiro
	#  Colunas
	bloc=[[0,1,2],[0,2,1],[1,2,0] , [3,4,5],[3,5,4],[4,5,3]  ,[6,7,8],[6,8,7],[7,8,6] , [0,3,6],[0,6,3],[3,6,0]  ,  [1,4,7],[1,7,4],[4,7,1] ,[2,5,8],[2,8,5],[5,8,2],[0,4,8],[0,8,4],[4,8,0],[2,4,6],[2,6,4],[4,6,2]]
	
	for c in range(0,24):
		if(tabuleiro[bloc[c][0]] == tabuleiro[bloc[c][1]] and tabuleiro[bloc[c][1]] == icone and tabuleiro[bloc[c][0]] == icone):
			if (tabuleiro[bloc[c][2]] == ""):
				return bloc[c][2]	
	return boot_easy(tabuleiro)
	
		
def boot_dificil(tabuleiro,icone,meu_icone):
	tabuleiro=tabuleiro
	#  Colunas
	bloc=[[0,1,2],[0,2,1],[1,2,0] , [3,4,5],[3,5,4],[4,5,3]  ,[6,7,8],[6,8,7],[7,8,6] , [0,3,6],[0,6,3],[3,6,0]  ,  [1,4,7],[1,7,4],[4,7,1] ,[2,5,8],[2,8,5],[5,8,2],[0,4,8],[0,8,4],[4,8,0],[2,4,6],[2,6,4],[4,6,2]]
	
	for hdh in range(0,24):
		if(tabuleiro[bloc[hdh][0]] == tabuleiro[bloc[hdh][1]] and tabuleiro[bloc[hdh][1]] == meu_icone and tabuleiro[bloc[hdh][0]] == meu_icone):
			
			if (tabuleiro[bloc[hdh][2]] == ""):
				return bloc[hdh][2]	
	
	for c in range(0,24):
		if(tabuleiro[bloc[c][0]] == tabuleiro[bloc[c][1]] and tabuleiro[bloc[c][1]] == icone and tabuleiro[bloc[c][0]] == icone):
			if (tabuleiro[bloc[c][2]] == ""):
				return bloc[c][2]	
	
	if (tabuleiro[4] == ""):
		return 4
	
	#estrategia=(0,2,6,8)
#	if (tabuleiro[4] == meu_icone):
#		for hdie in range(0,4):
#			if (tabuleiro[estrategia[hdie]] == ""):
#				return tabuleiro[estrategia[hdie]]
				
	return boot_easy(tabuleiro)
	
	
	
	
	
#	TIME
	
	
	
#from tkinter import*

#root = Tk()

#sec = None

#def tick():
#    global sec
#    if sec == None:
#        sec = int(inicio.get())
#    if sec == 30:
#        time['text'] = 'TEMPO ESGOTADO'
#        sec = None
#    else:
#        sec = sec + 1
#        time['text'] = sec
#        time.after(1000, tick)

#label = Label(root, text="Quanto tempo você tem para realizar suas  tarefas?")
#label.grid(row=0, column=0)
#inicio = Entry(root, textvariable=0)
#inicio.grid(row=1, column=0)
#time = Label(root, fg='green')
#time.grid(row=2, column=0)
#Button(root, fg='blue', text='Start', command=tick).grid(row=3, column=0)

#root.mainloop()
#	