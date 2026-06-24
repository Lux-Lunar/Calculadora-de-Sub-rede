#Calculadora de sub-rede

import customtkinter as ctk

rede = []

#converte o valor de hosts para bits e vice versa seguindo o principio da escalabilidade
def conversor_bits_hosts(hosts: int, escolha: int, rede: list):
    #cria a lista de bits
    bit = 1
    bit_list = [] * 31
    for i in range(1, 31):
        bit *= 2
        bit_list.insert(i, bit)
    bit_list.sort(reverse = True)
    if escolha == 1:
        if hosts in bit_list:
            #isso vai pegar os numeros que estão na lista bits e transformar no proximo host disponivel
            return(rede.append(bit_list[bit_list.index(hosts) - 1]), rede.append(bit_list.index(hosts) + 1))  
        else:
            for j in range(1, 32):
                #isso pega qualquer valor entre dois num. dentro da lista bits e salta para o valor maior mais proximo
                if bit_list[j] < hosts and bit_list[j-1] > hosts:
                    return(rede.append(bit_list[j-1]), rede.append(bit_list.index(bit_list[j-1]) + 2))
    else:
        #isso só converte os bits para hosts
        return(rede.append(bit_list[hosts - 2]), rede.append(hosts))

#converte os bits para numerico seguindo o padrão de sub-mask 255.255.255.255
def conversor_bits_sub(rede: list):
    bina = [] * 32
    bina_oito = [] * 8
    bina_oct = ""
    bina_dec = [] * 4
    x = 0
    #essa parte faz o trabalho de converter os numeros em um grande binario com 32 bits
    for i in range(rede[1]):
        bina.append(1)
    while True:
        if len(bina) == 32:
            break
        bina.append(0)
    #essa outra parte separa os 32 bits em 4 partes de 8 e depois calcula o valor binario de cada 1/4
    for i in range(4):
        for f in range(0, 8):
            bina_oito.append(bina[f+x])
            bina_oct = bina_oct + str(bina_oito[f+x])
        bina_dec.append(int(bina_oct, 2))
        bina_oct = ""
        x += 8
    #Falta criar parte que faz o processo inverso 255.255.255.255 para usuarios e bits
    return(rede.append(bina_dec))

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=tela-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class app(ctk.CTk):
    #executa oque tinha ctk.CTk
    def __init__(self):
        super().__init__()
        #executa os meu cod. self seria janela
        self.title("Calculadora de redes LAN")
        self.geometry("400x600")

        self.pergunta = ctk.CTkLabel(self, text="Calculadora de LANs", font=ctk.CTkFont(size=25, weight="bold")).pack(pady = (25, 50))

        #Seleção do tipo de rede

        self.pergunta = ctk.CTkLabel(self, text="Qual o tipo de rede", font=ctk.CTkFont(size=15, weight="bold")).pack(pady = (0, 25))

        self.botao_A = ctk.CTkOptionMenu(self, values=["Tipo A (10.0.0.0)","Tipo B (172.16.0.0)","Tipo C (192.168.0.0)"], font=ctk.CTkFont(weight="bold")).pack(pady = (0, 25))

        #Seleção de máscara

        self.pergunta = ctk.CTkLabel(self, text="Qual a forma da máscara", font=ctk.CTkFont(size=15, weight="bold")).pack(pady = (0, 0))

        self.botao_user = ctk.CTkOptionMenu(self, values=["Usuários", "Bits", "Máscara"], font=ctk.CTkFont(weight="bold")).pack(pady = (25, 0))

        self.campo_valor = ctk.CTkEntry(self, placeholder_text= "Digite aqui").pack(pady = 10)

        #Realizar o calculo

        self.botao_calc = ctk.CTkButton(self, text="Calcular", font=ctk.CTkFont(size=25, weight="bold")).pack(pady = (35, 25))

        def tipo_rede(self):
            if self.botao_A.get() == "Tipo A (10.0.0.0)":
                print("Tipo A")
            elif self.botao_A.get() == "Tipo B (172.16.0.0)":
                print("Tipo B")
            else:
                print("Tipo C")

janela = app()

janela.mainloop()

#conversor_bits_hosts(usuarios, opcao_de_host, rede)
#conversor_bits_sub(rede)
#print(rede)