import AppTeste2
from tkinter import *
class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7['padx'] = 20
        self.container7['pady'] = 5

        self.titulo = Label(self.container1,text='Bem Vindo, Faça o Login!')
        self.titulo.pack(side=TOP)
        self.pack()

        self.usuario = Label(self.container2, text="Usuário:")
        self.usuario.pack (side=LEFT)
        self.pack()

        self.lblusuario = Entry(self.container2)
        self.lblusuario["width"] = 25
        self.lblusuario["font"] = self
        self.lblusuario.pack(side=RIGHT)

        self.senha = Label(self.container3, text= 'Senha:')
        self.senha.pack(side=LEFT)
        self.pack()

        self.lblsenha = Entry(self.container3)
        self.lblsenha['width'] = 25
        self.lblsenha["show"] = "*"
        self.lblsenha['font'] = self
        self.lblsenha.pack(side=RIGHT)

        self.btnLogin = Button(self.container4, text="Login", font=self.fonte, width=10)
        self.btnLogin["command"] = self.VerificarSenha
        self.btnLogin.pack(side=LEFT)

        self.bntCadastreSe = Button(self.container4, text = 'Cadastre-se', font=self.fonte, width=10)
        self.bntCadastreSe.pack(side=LEFT)

        self.bntSair = Button(self.container5, text='Sair', font=self.fonte, width=10,fg = 'red', command=self.ClickSair)
        self.bntSair.pack(side=BOTTOM)

        self.mensagem = Label(self.container6, text="", font=self.fonte)
        self.mensagem.pack()

    def ClickSair(self):
        exit(0)


    def VerificarSenha(self):
        usuario = self.lblusuario.get()
        senha = self.lblsenha.get()
        if usuario=='nadson' and senha=='123' or usuario=='admin' and senha=='123':
            self.mensagem["text"] = "Senha Correta!"
            self.inicio(Frame)

        else:
            self.mensagem["text"] = "Senha Invalisa, Tente Novamente."

        class inicio(Frame):
            def TelaInicio(self):
                def __init__(self, master=None):
                    Frame.__init__(self, master)

                    self.fonte = ("Verdana", "8")
                    self.container7 = Frame(master)
                    self.container7['padx'] = 20
                    self.container7['pady'] = 5
                    self.container7.pack()

        app = inicio()
        app.master.title("Incio")
        app.master.geometry("700x700+100+100")
        mainloop()


app = Application()
app.master.title("Programa")
app.master.geometry("350x320+100+100")
mainloop()
