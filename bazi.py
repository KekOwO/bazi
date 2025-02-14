

class ConstiChi:
    def __init__(self, madeira, fogo, terra, metal, agua):
        self.madeira = madeira
        self.fogo = fogo
        self.terra = terra
        self.metal =metal
        self.agua = agua

mapa = ConstiChi(0,0,0,0,0)



MapaInput = []
i = 0
while i<8:
    MapaInput.insert(i, int(input("Olá, insira as informações do mapa")))
    print(MapaInput)
    i = i+1
#separar ramos de troncos

i = 0
l = 0
Troncos = []
while i<8:
    Troncos.insert(i, MapaInput[i])
    i = i+2
    l = l+1

l = 0
i = 1
Signos = []   
while i<8:
    Signos.insert(i, MapaInput[i])
    i = i+2
    l = l+1
print(MapaInput)
print(Troncos)
print(Signos)

def elementot():
    i = 0
    # Atribuição de valor a cada signo

    while i<4:
        if Troncos[i] in [1,2]: #madeira
            mapa.madeira = mapa.madeira + 50
        elif Troncos[i] in [3, 4]: #fogo
            mapa.fogo = mapa.fogo + 50
        elif Troncos[i] in [5,6]: #terra
            mapa.terra = mapa.terra + 50
        elif Troncos[i] in [7,8]: #metal
            mapa.metal = mapa.metal + 50
        elif Troncos[i] in [9,10]: #agua
            mapa.agua = mapa.agua + 50
        i = i+1
    print("____1____")
    print(mapa.madeira)
    print(mapa.metal)
    i = 0
    while i < len(Signos):
        if Signos[i] == 1: # tigre
            mapa.madeira = mapa.madeira + 30
            mapa.fogo = mapa.fogo + 15
            mapa.terra = mapa.terra + 5
        elif Signos[i] == 2: # coelho
            mapa.madeira = mapa.madeira + 50
        elif Signos[i] == 3: # dragão
            mapa.terra = mapa.terra + 30
            mapa.agua = mapa.agua + 8
            mapa.madeira = mapa.madeira + 12
        elif Signos[i] == 4: # serpente
            mapa.fogo = mapa.fogo + 30
            mapa.metal = mapa.metal + 15
            mapa.terra = mapa.terra + 5
        elif Signos[i] == 5: # cavalo
            mapa.fogo = mapa.fogo + 30
            mapa.madeira = mapa.madeira + 20
        elif Signos[i] == 6: # cabra
            mapa.terra = mapa.terra + 30
            mapa.fogo = mapa.fogo + 12
            mapa.madeira = mapa.madeira + 8
        elif Signos[i] == 7: # macaco
            mapa.metal = mapa.metal + 30
            mapa.agua = mapa.agua + 15
            mapa.terra = mapa.terra + 5
        elif Signos[i] == 8: # galo
            mapa.metal = mapa.metal + 50
        elif Signos[i] == 9: # cachorro
            mapa.terra = mapa.terra + 30
            mapa.fogo = mapa.fogo + 8
            mapa.metal = mapa.metal + 12
        elif Signos[i] == 10: # porco
            mapa.agua = mapa.agua + 30
            mapa.madeira = mapa.madeira + 20
        elif Signos[i] == 11: # rato
            mapa.agua = mapa.agua + 50
        elif Signos[i] == 12: # boi
            mapa.terra = mapa.terra + 30
            mapa.metal = mapa.metal + 8
            mapa.agua = mapa.agua + 12
        i += 1

    print("____2____")
    print(mapa.madeira)
    print(mapa.metal)

        # bonus por combinações de triade 
    i = 0
    podemsmsign=True
    combosfeitos = [0,0,0,0]
    while i<4:
        l=0
        cont=0
        

        if combosfeitos[i] in [0]:
            while l<4: 
                if podemsmsign and l != i and Signos[i] == Signos[l] or Signos[i] == (Signos[l]+4 or Signos[l]+8 or Signos[l]-4 or Signos[l]-8):
                    if Signos[i] == Signos[l]:
                        podemsmsign=False
                    cont=cont+1
                    combosfeitos[i] += 1
                    combosfeitos[l] += 1

                l = l+1
            if cont != 0:
                    if  Signos[i] in [1,5,9]:
                        if cont >2:
                            mapa.fogo = mapa.fogo + 100
                        else:
                            mapa.fogo = mapa.fogo + 50
                    elif  Signos[i] in [2,6,10]:
                        if cont >2:
                            mapa.madeira = mapa.madeira + 100
                        else:
                            mapa.madeira = mapa.madeira + 50
                    elif  Signos[i] in [3,7,11]:
                        if cont >2:
                            mapa.agua = mapa.agua + 100
                        else:
                            mapa.agua = mapa.agua + 50
                    elif Signos[i] in [4,8,12]:
                        if cont >2:
                            mapa.metal = mapa.metal + 100
                        else:
                            mapa.metal = mapa.metal + 50
                            print(mapa.metal)
                        print(combosfeitos)
        i = i + 1
        # Multiplicação por combinações de mes 
        
    print("____3____")
    print(mapa.madeira)
    print(mapa.metal)
    print(Signos[2])

    if Signos[2] == 1:
        mapa.fogo = mapa.fogo * 1.5
        mapa.madeira = mapa.madeira * 2
        mapa.terra = mapa.terra * 1.5
    elif Signos[2] == 2:
        mapa.madeira = mapa.madeira * 2
    elif Signos[2] == 3:
        mapa.terra = mapa.terra * 2
        mapa.madeira = mapa.madeira * 1.5
        mapa.agua = mapa.agua * 1.5
    elif Signos[2] == 4:
        mapa.fogo = mapa.fogo * 2
        mapa.metal = mapa.metal * 1.5
        mapa.terra = mapa.terra * 1.5
    elif Signos[2] == 5:
        mapa.terra = mapa.terra * 1.5
        mapa.fogo = mapa.fogo * 2
    elif Signos[2] == 6:
        mapa.terra = mapa.terra * 2
        mapa.madeira = mapa.madeira * 1.5
        mapa.fogo = mapa.fogo * 1.5
    elif Signos[2] == 7:
        mapa.metal = mapa.metal * 2
        mapa.agua = mapa.agua * 1.5
        mapa.terra = mapa.terra * 1.5
    elif Signos[2] == 8:
        mapa.metal = mapa.metal * 2
    elif Signos[2] == 9:
        mapa.terra = mapa.terra * 2
        mapa.fogo = mapa.fogo * 1.5
        mapa.metal = mapa.metal * 1.5
    elif Signos[2] == 10:
        mapa.agua = mapa.agua * 2
        mapa.madeira = mapa.madeira * 1.5
    elif Signos[2] == 11:
        mapa.agua = mapa.agua * 2
    elif Signos[2] == 12:
        mapa.terra = mapa.terra * 2
        mapa.metal = mapa.metal * 1.5
        mapa.agua = mapa.agua * 1.5
        print("!!!")
elementot()

print("____4____")

print(mapa.agua)
print(mapa.madeira)
print(mapa.fogo)
print(mapa.terra)
print(mapa.metal)

print("____5____")



def Tirarporcentagens (mapa):
    Total = mapa.madeira + mapa.fogo + mapa.terra + mapa.metal + mapa.agua
    porcentagens = []
    porcentagens.insert(1, (mapa.madeira*100) / Total)
    porcentagens.insert(2, (mapa.fogo*100) / Total)
    porcentagens.insert(3, (mapa.terra*100) / Total)
    porcentagens.insert(4, (mapa.metal*100) / Total)
    porcentagens.insert(5, (mapa.agua*100) / Total)
    print(porcentagens)
    print(Total)



Tirarporcentagens(mapa)
