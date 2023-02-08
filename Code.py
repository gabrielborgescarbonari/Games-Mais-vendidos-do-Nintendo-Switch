import pandas as pd
import seaborn as srn
import statistics as sts
import numpy as np
import matplotlib.pyplot as plt

# importar dados
dataset = pd.read_csv("best_selling_switch_games.csv")
# visulizar
dataset.head()
# tamanho
dataset.shape
# primeiro problema é dar nomes as colunas
dataset.columns = ["Jogos", "Copias_Vendidas", "Genero",
                   "Desenvolvedor", "Publicador", "Desde", "Data de Lançamento"]

# EXPLORAR DADOS CATEGÓRICOS
# genero (Agrupar mesmos)
gen = dataset['Genero'].value_counts()
gen
gen.plot.bar(color='gray')

# desenvolvedor (agrupar mesmos)
des = dataset['Desenvolvedor'].value_counts()
des
des.plot.bar(color='gray')

# publicador (agrupar mesmos)
pub = dataset['Publicador'].value_counts()
pub
pub.plot.bar(color='gray')

# EXPLORAR COLUNAS NUMÉRICAS
# Copias Vendidas (procurar padrão dos que venderam muito)
dataset['Copias_Vendidas'].describe()
srn.boxplot(dataset['Copias_Vendidas']).set_title('Copias_Vendidas')
srn.histplot(dataset['Copias_Vendidas']).set_title('Copias_Vendidas')

# procurar valores nulos (0)
dataset.isnull().sum()

# TRATAMENTO DE DADOS CATEGÓRICOS
# padroniza de acordo com o dominio (GENERO)
dataset.loc[dataset['Genero'].isin(['Action puzzle', 'Action role-playing',
                                   'Action-adventure', 'Action-adventure, Hack and Slash']), 'Genero'] = "Action"
dataset.loc[dataset['Genero'].isin(
    ['Exergamerhythm', 'Exergamerole-playing']), 'Genero'] = "Exergame"
dataset.loc[dataset['Genero'] ==
            'Hack and slashRole-playing', 'Genero'] = "Hack and slash"
dataset.loc[dataset['Genero'].isin(
    ['Kart racing', 'Kart racingaugmented reality']), 'Genero'] = "Kart"
dataset.loc[dataset['Genero'] == 'Partysocial deduction', 'Genero'] = "Party"
dataset.loc[dataset['Genero'].isin(
    ['PlatformerLevel editor', 'Platformercompilation']), 'Genero'] = "Platformer"
dataset.loc[dataset['Genero'].isin(
    ['Role-playingaction-adventure', 'Simulationrole-playing', 'Tactical role-playing']), 'Genero'] = "Role-playing"
dataset.loc[dataset['Genero'] ==
            'Real-time strategypuzzle', 'Genero'] = "Puzzle"
dataset.loc[dataset['Genero'].isin(
    ['Sandboxsurvival', 'Survival horror']), 'Genero'] = "Survival"
dataset.loc[dataset['Genero'].isin(['Board game', 'Bullet hell', 'Construction kit', 'Photography', 'Programming',
                                   'Rhythm', 'Roguelike', 'Social simulation', 'Stealth', 'Tabletop game']), 'Genero'] = "Others"
# visualiza o resultado
gen = dataset['Genero'].value_counts()
gen

# padroniza de acordo com o dominio (DESENVOLVEDORA)

dataset.loc[dataset['Desenvolvedor'] == 'Bandai Namco StudiosSora Ltd.',
            'Desenvolvedor'] = "Bandai Namco Studios"
dataset.loc[dataset['Desenvolvedor'] == 'Intelligent SystemsKoei Tecmo',
            'Desenvolvedor'] = "Intelligent Systems"
dataset.loc[dataset['Desenvolvedor'].isin(['Nintendo EPD', 'Nintendo EPD, indieszero', 'Nintendo EPDIntelligent Systems',
                                          'MercurySteamNintendo EPD', 'Nintendo EPDEighting', 'Retro Studios']), 'Desenvolvedor'] = "Nintendo"
dataset.loc[dataset['Desenvolvedor'].isin(['Arc System Works', 'Atlus', 'CyberConnect2', 'Dimps', 'Dodge Roll', 'Good-Feel', 'ILCA', 'Innersloth', 'Konami', 'Marvelous', 'Mojang',
                                          'Noble Muffins', 'Spike Chunsoft', 'Square EnixAcquire', 'Tantalus Media', 'Team Ninja', 'Ubisoft ParisUbisoft Milan', 'Velan Studios']), 'Desenvolvedor'] = "Others"

# visualiza o resultado
des = dataset['Desenvolvedor'].value_counts()
des

# padroniza de acordo com o dominio (PUBLICADORA (nintendo anuncia a cada trimestrs, outras não))

dataset.loc[dataset['Publicador'].isin(['.mw-parser-output .plainlist ol,.mw-parser-output .plainlist ul{line-height:inherit;list-style:none;margin:0;padding:0}.mw-parser-output .plainlist ol li,.mw-parser-output .plainlist ul li{margin-bottom:0}JP: Koei TecmoNA/PAL: Nintendo',
                                        'JP: AtlusNA: SegaPAL: Nintendo', 'JP: ImagineerNA/PAL: Nintendo', 'JP: Koei TecmoNA/PAL: Nintendo', 'JP: Square EnixNA/PAL: Nintendo', 'JP: The Pokémon CompanyNA/PAL: Nintendo', 'NA/PAL: UbisoftJP/KOR: Nintendo[18]', 'The Pokémon CompanyNintendo']), 'Publicador'] = "Nintendo"
dataset.loc[dataset['Publicador'].isin(['Devolver Digital', 'Forever Entertainment', 'Innersloth',
                                       'JP: Konami', 'JP: Xbox Game StudiosNA/PAL: Mojang', 'Xseed Games']), 'Publicador'] = "Others"

# visualiza o resultado
pub = dataset['Publicador'].value_counts()
pub

# ANÁLISE DOS DADOS
# Generos
print(gen)

# Mais vendidos de Ação
acao = dataset.loc[dataset['Genero'] == 'Action']
acao.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#2ce87a'])
plt.title("Jogos mais vendidos de Ação")

# Mais vendidos de Role-playing
role = dataset.loc[dataset['Genero'] == 'Role-playing']
role.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#2ce2e8'])
plt.title("Jogos mais vendidos de Role-playing")

# Mais vendidos de Plataformer
plat = dataset.loc[dataset['Genero'] == 'Role-playing']
plat.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#9ed128'])
plt.title("Jogos mais vendidos de Plataforma")

# Mais vendidos de Outros generos
ou = dataset.loc[dataset['Genero'] == 'Others']
ou.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#d14128'])
plt.title("Jogos mais vendidos de outros gêneros")

# Desenvolvedor
print(des)

# Mais vendidos da Nintendo
nin = dataset.loc[dataset['Desenvolvedor'] == 'Nintendo']
nin.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#2ce87a'])
plt.title("Jogos mais vendidos da Nintendo")

# Mais vendidos da Bandai
ban = dataset.loc[dataset['Desenvolvedor'] == 'Bandai Namco Studios']
ban.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#2ce2e8'])
plt.title("Jogos mais vendidos da Bandai")

# Mais vendidos da Game Freak
gaF = dataset.loc[dataset['Desenvolvedor'] == 'Game Freak']
gaF.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#9ed128'])
plt.title("Jogos mais vendidos da Game Freak")

# Mais vendidos de Outras desenvolvedoras
out = dataset.loc[dataset['Desenvolvedor'] == 'Others']
out.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#d14128'])
plt.title("Jogos mais vendidos de outras desenvolvedoras")

# Publicadora
print(pub)

# Mais vendidos da Nintendo
nint = dataset.loc[dataset['Publicador'] == 'Nintendo']
nint.iloc[:, 0:2].head(24).plot.bar(
    x='Jogos', y='Copias_Vendidas', color=['#2ce87a'])
plt.title("Jogos mais vendidos publicados pela Nintendo")

# Mais vendidos da Bandai
band = dataset.loc[dataset['Publicador'] == 'Bandai Namco Entertainment']
band.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#2ce2e8'])
plt.title("Jogos mais vendidos publicados pela Bandai")

# Mais vendidos da Capcom
cap = dataset.loc[dataset['Publicador'] == 'Capcom']
cap.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#9ed128'])
plt.title("Jogos mais vendidos publicados pela Capcom")

# Mais vendidos de Outras publicadoras
outr = dataset.loc[dataset['Publicador'] == 'Others']
outr.iloc[:, 0:2].plot.bar(x='Jogos', y='Copias_Vendidas', color=['#d14128'])
plt.title("Jogos mais vendidos publicados por outras publicadoras")
