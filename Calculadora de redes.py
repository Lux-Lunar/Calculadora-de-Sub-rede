#Calculadora de sub-rede

import customtkinter as ctk

rede = []

#converte o valor de hosts para bits e vice versa seguindo o principio da escalabilidade
def conversor_bits_hosts(hosts, escolha: int, rede: list):
    quantidade = 0
    #cria a lista de bits
    bit = 1
    bit_list = [] * 31
    for i in range(1, 31):
        bit *= 2
        bit_list.insert(i, bit)
    bit_list.sort(reverse = True)

    if escolha == 3 or escolha == 2:
        if escolha == 3: 
            hosts = hosts.split(".")
            for i in range(3):
                hosts[i] = int(hosts[i])
                hosts[i] = bin(hosts[i])
                hosts[i] = str(hosts[i])
                quantidade += hosts[i].count("1")
            hosts = quantidade
        #isso só converte os bits para hosts
        return(rede.append(bit_list[hosts - 2]), rede.append(hosts))
    elif escolha == 1:
        if hosts in bit_list:
            #isso vai pegar os numeros que estão na lista bits e transformar no proximo host disponivel
            return(rede.append(bit_list[bit_list.index(hosts) - 1]), rede.append(bit_list.index(hosts) + 1))  
        else:
            for j in range(1, 32):
                #isso pega qualquer valor entre dois num. dentro da lista bits e salta para o valor maior mais proximo
                if bit_list[j] < hosts and bit_list[j-1] > hosts:
                    return(rede.append(bit_list[j-1]), rede.append(bit_list.index(bit_list[j-1]) + 2))

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

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Programa no terminal-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

pegar_opcao = ["hosts", "bits", "máscara"]
pegar_opcao_ABC = ["A", "B", "C"]

while True:
    opcao_rede = int(input("Digite o tipo de rede que deseja ([1] A 10.0.0.0) ([2] B 172.16.0.0) ([3] C 192.168.0.0): "))
    if opcao_rede > 0 and opcao_rede < 4:
        break
while True:
    opcao_host = int(input("Qual tipo de host deseja ([1] Hosts) ([2] Bits) ([3] Mask): ")) 
    if opcao_host == 3:
        usuarios = str(input(f"Digite o valor correspondente a {pegar_opcao[opcao_host - 1]}: "))
        break
    elif opcao_host == 1 or opcao_host == 2:
        while True:
            usuarios = int(input(f"Digite o valor correspondente aos {pegar_opcao[opcao_host - 1]}: "))
            if opcao_host == 2 and usuarios <= 31 and usuarios > 0 :
                break
            elif opcao_host == 1 and usuarios >= 2 and usuarios < 1073741824:
                break
        break
conversor_bits_hosts(usuarios, opcao_host, rede)
conversor_bits_sub(rede)

print("")
print(f"Tipo da rede ({pegar_opcao_ABC[opcao_rede - 1]})")
print(f"A quantidade de hosts {rede[0]}")
print(f"A quantidade de bits {rede[1]}")
print(f"A máscara {rede[2]}")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=tela-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Por hora essa parte só funciona no design, na parte de usabilidade ainda não avancei

"""ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de redes LAN")
        self.geometry("400x600")

        def selecao_A(choice):
            tipo_de_rede = choice
            print(tipo_de_rede)

        def selecao_host(choice):
            tipo_host = choice
            return(tipo_host)

        pergunta = ctk.CTkLabel(self, text="Calculadora de LANs", font=ctk.CTkFont(size=25, weight="bold")).pack(pady = (25, 50))

        #Seleção do tipo de rede

        pergunta = ctk.CTkLabel(self, text="Qual o tipo de rede", font=ctk.CTkFont(size=15, weight="bold")).pack(pady = (0, 25))

        botao_A = ctk.CTkOptionMenu(self, values=["Tipo A (10.0.0.0)","Tipo B (172.16.0.0)","Tipo C (192.168.0.0)"], font=ctk.CTkFont(weight="bold"), command=selecao_A).pack(pady = (0, 25))

        #Seleção de máscara

        pergunta = ctk.CTkLabel(self, text="Qual a forma da máscara", font=ctk.CTkFont(size=15, weight="bold")).pack(pady = (0, 0))

        botao_user = ctk.CTkOptionMenu(self, values=["Usuários", "Bits", "Máscara"], font=ctk.CTkFont(weight="bold"), command=selecao_host).pack(pady = (25, 0))

        campo_valor = ctk.CTkEntry(self, placeholder_text= "Digite aqui!").pack(pady = 10)

        #Realizar o calculo

        botao_calc = ctk.CTkButton(self, text="Calcular", font=ctk.CTkFont(size=25, weight="bold")).pack(pady = (35, 25))

janela = app()
janela.mainloop()"""
