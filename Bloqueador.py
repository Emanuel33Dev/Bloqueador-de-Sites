# Importanto Tkinter
from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
# Importando pillow
from PIL import Image, ImageTk

import csv

# Cores
co0 = "#fof3f5" # Preta
co1 = "#feffff" # Branca
co2 = "#3fb5a3" # Verde
co3 = "#fc766d" # Vermelho
co4 = "#403d3d" #Letra
co5 = "#4a88e8" # Azul

# Criando Janela

janela = Tk()
janela.title("")
janela.geometry("390x350")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# Fremes
frame_logo = Frame(janela, width=400, height=60, bg=co1, relief="flat")
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=400, height=400, bg=co1, relief="flat")
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando frame logo
imagem = Image.open('icone.png')
imagem = imagem.resize((50, 50))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_logo, height=60, image=imagem, bg=co1)
l_imagem.place(x=20, y=1)

l_logo = Label(frame_logo, text='Bloqueador de Sites', height=1, anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_logo.place(x=70, y=10)

l_linha = Label(frame_logo, text='', width=445, height=1, anchor=NW, font=('Ivy 1'), bg=co2)
l_linha.place(x=0, y=57)

# Criando funções
global iniciar
global websites

iniciar = BooleanVar()

# Função ver Site
def ver_site():
    listabox.delete(0, END)

    # acessando arquivo csv
    with open('sites.csv') as file:
        ler_csv = csv.reader(file)
        for row in ler_csv:
            listabox.insert(END,row)



# Função salvar site
def salvar_site(i):
    #acessando arquivo csv
    with open('sites.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i])
        messagebox.showinfo('Site', 'O site foi adicionado')

    ver_site()

# Função eliminar sites
def deletar_site(i):

    def adicionar(i):
        with open('sites.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(i)
            messagebox.showinfo('Site', 'O site foi removido')

        ver_site()
    nova_lista = []
    with open('sites.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            nova_lista.append(row)
            for campo in row:
                if campo == i:
                    print(f'Sites romovidos '
                          f'\n{campo}')
                    nova_lista.remove(row)

    adicionar(nova_lista)


# Função adicionar
def adicionar_site():
    site = e_site.get()
    if site == '':
        pass
    else:
        listabox.insert(END, site)
        e_site.delete(0, END)
        listabox.insert(END, site)
        e_site.delete(0, END)
        salvar_site(site)

# Função romover
def romever_site():
    site = listabox.get(ACTIVE)
    sites = []
    for i in site:
        sites.append(i)
    deletar_site(sites[0])


# Função Bloqueador Sites
def desbloquear_site():
    iniciar.set(False)
    messagebox.showinfo('Site', 'Os sites na lista foram Desbloqueados')
    bloqueador_site()

def bloquear_site():
    iniciar.set(True)
    messagebox.showinfo('Site', 'Os sites na lista foram Bloqueados')
    bloqueador_site()



def bloqueador_site():
    # Caminho do arquivo hots do windows
    local_do_host = r"C:\\Windows\\System32\\drivers\\etc\\hosts"
    redicionar = '127.0.0.1'

    websites = []

    #Acessando o ficheiro CSV
    with open('sites.csv') as file:
        ler_csv = csv.reader(file)
        for row in ler_csv:
            websites.append(row[0])

    if iniciar.get() == True:
        with open(local_do_host, 'r+') as arquivo:
            conteudo = arquivo.read()

            for site in websites:
                if site in conteudo:
                    pass
                else:
                    arquivo.write(redicionar+" "+site+"\n")
    else:
        with open(local_do_host, 'r+') as arquivo:
            conteudo = arquivo.readlines()
            arquivo.seek(0)

            for line in conteudo:
                if not any(site in line for site in websites):
                    arquivo.write(line)
            arquivo.truncate()




# Configurando frame corpo
l_site = Label(frame_corpo, text='Digite o site que deseja bloquear no campo abaixo * ', height=1, anchor=NE, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_site.place(x=23, y=20)
e_site = Entry(frame_corpo, width=21, justify='left', font=(' ', 15), highlightthickness=1, relief=SOLID)
e_site.place(x=23, y=50)

b_adicionar = Button(frame_corpo, command=adicionar_site, text='Adicionar', width=10, height=1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1)
b_adicionar.place(x=267, y=50)

b_remover = Button(frame_corpo, command=romever_site, text='Remover', width=10, height=1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1)
b_remover.place(x=267, y=100)

b_desbloquear = Button(frame_corpo, command=desbloquear_site, text='Desbloquear', width=10, height=1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co2, fg=co1)
b_desbloquear.place(x=267, y=150)

b_bloquear = Button(frame_corpo,command=bloquear_site, text='Bloquear', width=10, height=1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=co3, fg=co1)
b_bloquear.place(x=267, y=200)

listabox = Listbox(frame_corpo, font=('Arial 9 bold'), width=33, height=10)
listabox.place(x=23, y=100)

ver_site()
# Manter a jenela aberta
input("Pressione Enter para sair...")

janela.mainloop()
