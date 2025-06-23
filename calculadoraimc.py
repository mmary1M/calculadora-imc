from tkinter import *
from tkinter import messagebox

# Cores
co1 = "#000000"
co2 = '#6f9fbd'
co3 = '#38576b'
fundo = '#e8e6e6'
texto = '#363434'

# janela
janela = Tk()
janela.title('IMC')
janela.geometry('300x350')
janela.configure(bg=fundo)
janela.resizable(False, False)

# Função de cálculo do IMC
def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura * altura)
        imc = round(imc, 2)

        if imc < 18.5:
            resultado = 'Abaixo do peso'
        elif 18.5 <= imc < 24.9:
            resultado = 'Peso normal'
        elif 25 <= imc < 29.9:
            resultado = 'Sobrepeso'
        elif 30 <= imc < 34.9:
            resultado = 'Obesidade Grau I'
        elif 35 <= imc < 39.9:
            resultado = 'Obesidade Grau II'
        else:
            resultado = 'Obesidade Grau III ou Mórbida'

        label_resultado['text'] = f'Seu IMC é {imc}\n{resultado}'

    except:
        messagebox.showerror('Erro', 'Digite valores válidos!')

# Título
label_titulo = Label(janela, text='IMC', bg=fundo, fg=texto, font=('Arial 16 bold'))
label_titulo.pack(pady=10)

# Peso
label_peso = Label(janela, text='Peso (kg):', bg=fundo, fg=texto, font=('Arial 12'))
label_peso.pack(pady=5)
entrada_peso = Entry(janela, width=10, font=('Arial 12'))
entrada_peso.pack()

# Altura
label_altura = Label(janela, text='Altura (m):', bg=fundo, fg=texto, font=('Arial 12'))
label_altura.pack(pady=5)
entrada_altura = Entry(janela, width=10, font=('Arial 12'))
entrada_altura.pack()

# Botão calcular
botao_calcular = Button(janela, text='Calcular IMC', command=calcular_imc, bg=co1, fg='white', font=('Arial 12 bold'))
botao_calcular.pack(pady=15)

# Resultado
label_resultado = Label(janela, text='', bg=fundo, fg=texto, font=('Arial 12'))
label_resultado.pack(pady=10)

janela.mainloop()