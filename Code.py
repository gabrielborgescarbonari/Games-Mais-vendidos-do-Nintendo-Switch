import pandas as pd  # tratar dados como framework
import seaborn as srn  # alguns gráficos
import statistics as sts  # substituir valores faltantes com mediana e desvio padrão

# importar dados
dataset = pd.read_csv("best_selling_switch_games.csv")
# visulizar
dataset.head()
# tamanho
dataset.shape
# primeiro problema é dar nomes as colunas
dataset.columns = ["Nome", "Copias_Vendidas", "Genero",
                   "Desenvolvedor", "Publicador", "Desde", "Data de Lançamento"]

# EXPLORAR DADOS CATEGÓRICOS
# nome (Nada a se fazer)
nom = dataset.groupby(['Nome']).size()
nom
nom.plot.bar(color='gray')

# genero (Agrupar mesmos)
gen = dataset.groupby(['Genero']).size()
gen
gen.plot.bar(color='gray')

# desenvolvedor (agrupar mesmos)
des = dataset.groupby(['Desenvolvedor']).size()
des
des.plot.bar(color='gray')

# publicador (agrupar mesmos)
pub = dataset.groupby(['Publicador']).size()
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
    ['Kart racing', 'Kart racingaugmented reality']), 'Genero'] = "Kart"
dataset.loc[dataset['Genero'].isin(
    ['Sandboxsurvival', 'Survival horror']), 'Genero'] = "Survival"
dataset.loc[dataset['Genero'].isin(['Board game', 'Bullet hell', 'Construction kit', 'Photography', 'Programming',
                                   'Rhythm', 'Roguelike', 'Social simulation', 'Stealth', 'Tabletop game']), 'Genero'] = "Others"
# visualiza o resultado
gen = dataset.groupby(['Genero']).size()
gen

# padroniza de acordo com o dominio (DESENVOLVEDORA)

dataset.loc[dataset['Desenvolvedor'] == 'Bandai Namco StudiosSora Ltd.',
            'Desenvolvedor'] = "Bandai Namco Studios"
dataset.loc[dataset['Desenvolvedor'] == 'Intelligent SystemsKoei Tecmo',
            'Desenvolvedor'] = "Intelligent Systems"
dataset.loc[dataset['Desenvolvedor'].isin(['Nintendo EPD', 'Nintendo EPD, indieszero', 'Nintendo EPDIntelligent Systems',
                                          'MercurySteamNintendo EPD', 'Nintendo EPDEighting']), 'Desenvolvedor'] = "Nintendo"
dataset.loc[dataset['Desenvolvedor'].isin(['Arc System Works', 'Atlus', 'CyberConnect2', 'Dimps', 'Dodge Roll', 'Good-Feel', 'ILCA', 'Innersloth', 'Konami', 'Marvelous', 'Mojang',
                                          'Noble Muffins', 'Retro Studios', 'Spike Chunsoft', 'Square EnixAcquire', 'Tantalus Media', 'Team Ninja', 'Ubisoft ParisUbisoft Milan', 'Velan Studios']), 'Desenvolvedor'] = "Others"

# visualiza o resultado
des = dataset.groupby(['Desenvolvedor']).size()
des

# padroniza de acordo com o dominio (PUBLICADORA (nintendo anuncia a cada trimestrs, outras não))

dataset.loc[dataset['Publicador'].isin(['.mw-parser-output .plainlist ol,.mw-parser-output .plainlist ul{line-height:inherit;list-style:none;margin:0;padding:0}.mw-parser-output .plainlist ol li,.mw-parser-output .plainlist ul li{margin-bottom:0}JP: Koei TecmoNA/PAL: Nintendo',
                                       'JP: AtlusNA: SegaPAL: Nintendo', 'JP: ImagineerNA/PAL: Nintendo', 'JP: Koei TecmoNA/PAL: Nintendo', 'JP: Square EnixNA/PAL: Nintendo', 'JP: The Pokémon CompanyNA/PAL: Nintendo', 'NA/PAL: UbisoftJP/KOR: Nintendo[18]', 'The Pokémon CompanyNintendo']), 'Publicador'] = "Nintendo"
dataset.loc[dataset['Publicador'].isin(['Devolver Digital', 'Forever Entertainment', 'Innersloth',
                                       'JP: Konami', 'JP: Xbox Game StudiosNA/PAL: Mojang', 'Xseed Games']), 'Publicador'] = "Others"

# visualiza o resultado
pub = dataset.groupby(['Publicador']).size()
pub

# TRATAMENTO DE DADOS NUMÉRICOS
