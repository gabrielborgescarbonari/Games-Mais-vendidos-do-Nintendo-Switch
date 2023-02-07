
```{r}
library(lattice)
library("RColorBrewer")
library(dplyr)

# importa dados, string como fatores(dados categóricos c/ domínio)
dados <- read.csv("best_selling_switch_games.csv", stringsAsFactors = FALSE) #força os dados categóricos a serem caracteres.

# traz um resumo dos dados, aqui podemos conhecê-los melhor
summary(dados) 
```

```{r}
# primeiro problema é dar nomes as colunas
colnames(dados) <- c("Jogos" , "Copias_Vendidas" , "Genero","Desenvolvedor" ,"Publicador" ,"Desde" ,"Data de Lançamento")

#Ordena por ordem de mais vendido
dados <- dados[order(-dados$Copias_Vendidas),]
```

```{r}
# EXPLORAR DADOS CATEGÓRICOS

# genero (Agrupar mesmos)
gen = table(dados$Genero)
barplot(gen, main="Gêneros", xlab="Gêneros")
```

```{r}
# desenvolvedor (agrupar mesmos)
des = table(dados$Desenvolvedor)
barplot(des, main="Desenvolvedores", xlab="Desenvolvedores")
```

```{r}
# publicador (agrupar mesmos)
pub = table(dados$Publicador)
barplot(pub, main="Publicadora", xlab="Publicadora")
```

```{r}
#EXPLORAR COLUNAS NUMÉRICAS

# Copias Vendidas (procurar padrão dos que venderam muito)
summary(dados$Copias_Vendidas)
boxplot(dados$Copias_Vendidas)
hist(dados$Copias_Vendidas)
```

```{r}
# TRATAMENTO DE DADOS CATEGÓRICOS

# padroniza de acordo com o dominio (GENERO)
dados[dados$Genero == "Action-adventure"|dados$Genero == "Action puzzle" |dados$Genero == "Action role-playing" |dados$Genero == "Action-adventure, Hack and Slash",]$Genero = "Action"
dados[dados$Genero == "Exergamerhythm"|dados$Genero == "Exergamerole-playing",]$Genero = "Exergame"
dados[dados$Genero == "Hack and slashRole-playing",]$Genero = "Hack and slash"
dados[dados$Genero == "Kart racing"|dados$Genero == "Kart racingaugmented reality",]$Genero = "Kart"
dados[dados$Genero == "Partysocial deduction",]$Genero = "Party"
dados[dados$Genero == "PlatformerLevel editor"|dados$Genero == "Platformercompilation",]$Genero = "Platformer"
dados[dados$Genero == "Role-playingaction-adventure"|dados$Genero == "Simulationrole-playing" |dados$Genero == "Tactical role-playing",]$Genero = "Role-playing"
dados[dados$Genero == "Real-time strategypuzzle",]$Genero = "Puzzle"
dados[dados$Genero == "Sandboxsurvival"|dados$Genero == "Survival horror",]$Genero = "Survival"
dados[dados$Genero == ""|dados$Genero == "Board game" |dados$Genero == "Bullet hell" |dados$Genero == "Construction kit"|dados$Genero == "Photography" |dados$Genero == "Programming" |dados$Genero == "Rhythm"|dados$Genero == "Roguelike" |dados$Genero == "Social simulation" |dados$Genero == "Stealth"|dados$Genero == "Tabletop game",]$Genero = "Others"

# visualiza o resultado dos 10 generos que mais venderam
g <-aggregate(dados[,-c(1,4,5,6,7)]$Copias_Vendidas, by=list(dados[,-c(1,4,5,6,7)]$Genero), FUN=sum)
head(g[order(-g$x),],10)
```

```{r}
# padroniza de acordo com o dominio (DESENVOLVEDORA)
dados[dados$Desenvolvedor == "Bandai Namco StudiosSora Ltd.",]$Desenvolvedor = "Bandai Namco Studios"
dados[dados$Desenvolvedor == "Intelligent SystemsKoei Tecmo",]$Desenvolvedor = "Intelligent Systems"
dados[dados$Desenvolvedor == "Nintendo EPD"|dados$Desenvolvedor == "Nintendo EPD, indieszero"|dados$Desenvolvedor == "Nintendo EPDIntelligent Systems"|dados$Desenvolvedor == "MercurySteamNintendo EPD"|dados$Desenvolvedor == "Nintendo EPDEighting"|dados$Desenvolvedor == "Retro Studios",]$Desenvolvedor = "Nintendo"
dados[dados$Desenvolvedor == "Arc System Works"|dados$Desenvolvedor == "Atlus"|dados$Desenvolvedor == "CyberConnect2"|dados$Desenvolvedor == "Dimps"|dados$Desenvolvedor == "Dodge Roll"|dados$Desenvolvedor == "Good-Feel"|dados$Desenvolvedor == "ILCA"|dados$Desenvolvedor == "Innersloth"|dados$Desenvolvedor == "Konami"|dados$Desenvolvedor == "Marvelous"|dados$Desenvolvedor == "Mojang"|dados$Desenvolvedor == "Noble Muffins"|dados$Desenvolvedor == "Spike Chunsoft"|dados$Desenvolvedor == "Square EnixAcquire"|dados$Desenvolvedor == "Tantalus Media"|dados$Desenvolvedor == "Team Ninja"|dados$Desenvolvedor == "Ubisoft ParisUbisoft Milan"|dados$Desenvolvedor == "Velan Studios",]$Desenvolvedor = "Others"

# visualiza o resultado das 10 desenvolvedoras que mais venderam
d<-aggregate(dados[,-c(1,3,5,6,7)]$Copias_Vendidas, by=list(dados[,-c(1,3,5,6,7)]$Desenvolvedor), FUN=sum)
head(d[order(-d$x),],10)
```

```{r}
# padroniza de acordo com o dominio (PUBLICADORA (nintendo anuncia a cada trimestrs, outras não))
dados[dados$Publicador == ".mw-parser-output .plainlist ol,.mw-parser-output .plainlist ul{line-height:inherit;list-style:none;margin:0;padding:0}.mw-parser-output .plainlist ol li,.mw-parser-output .plainlist ul li{margin-bottom:0}JP: Koei TecmoNA/PAL: Nintendo"|dados$Publicador == "JP: AtlusNA: SegaPAL: Nintendo"|dados$Publicador == "JP: ImagineerNA/PAL: Nintendo"|dados$Publicador == "JP: Koei TecmoNA/PAL: Nintendo"|dados$Publicador == "JP: Square EnixNA/PAL: Nintendo"|dados$Publicador == "JP: The Pokémon CompanyNA/PAL: Nintendo"|dados$Publicador == "NA/PAL: UbisoftJP/KOR: Nintendo[18]"|dados$Publicador == "The Pokémon CompanyNintendo",]$Publicador = "Nintendo"
dados[dados$Publicador == "Devolver Digital"|dados$Publicador == "Forever Entertainment"|dados$Publicador == "Innersloth"|dados$Publicador == "JP: Konami"|dados$Publicador == "JP: Xbox Game StudiosNA/PAL: Mojang"|dados$Publicador == "Xseed Games",]$Publicador = "Others"

# visualiza o resultado das publicadoras em ordem
p<-aggregate(dados[,-c(1,4,3,6,7)]$Copias_Vendidas, by=list(dados$Publicador), FUN=sum)
head(p[order(-p$x),],10)
```

```{r}
# ANÁLISE DOS DADOS

# GENEROS
srtgen <- dados[order(dados$Genero),]

# Mais vendidos de Ação
a <- srtgen[1:14,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
c<-srtgen[1:14,][order(-dados$Copias_Vendidas),]$Jogos
barplot(a[1:14], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos de Ação")
legend("topright",inset = c(-0, 0),legend=c[1:14],col = brewer.pal(n = 10, name = "RdBu"), pch = c(11,12),cex=0.8, ncol = 1,lwd=2 )
box()

legend("topright", inset = c(0.4, 1.2),                   
       legend = c("Group 1","Group 2","Group 3"),
       pch = c(11,12,13), col = 1:3)
```

```{r}
# Mais vendidos de Role-playing
r <- srtgen[55:65,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
o<-srtgen[55:65,][order(-dados$Copias_Vendidas),]$Jogos
barplot(r[1:11], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos de Role-Playing")
legend("topright",legend=o[1:11],inset = c(-0, 0),col = brewer.pal(n = 10, name = "RdBu"), pch = c(11,12),cex=0.8, ncol = 1,lwd=2)
box()
```

```{r}
# Mais vendidos de Plataformer
p <- srtgen[43:51,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
l<-srtgen[43:51,][order(-dados$Copias_Vendidas),]$Jogos
barplot(p[1:9], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos de Plataforma")
legend("topright",inset = c(-0, 0),legend=l[1:9],col = brewer.pal(n = 10, name = "RdBu"), pch = c(11,12),cex=0.8, ncol = 1,lwd=2)
box()
```

```{r}
# Mais vendidos de Outros generos
o <- srtgen[28:37,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
u<-srtgen[28:37,][order(-dados$Copias_Vendidas),]$Jogos
barplot(o[1:10], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos de Outros Gêneros")
legend("topright",inset = c(-0, 0),legend=u[1:10],col = brewer.pal(n = 10, name = "RdBu"), pch = c(11,12),cex=0.8, ncol = 1,lwd=2)
box()
```

```{r}
#DESENVOLVEDORA
srtdes <- dados[order(dados$Desenvolvedor),]

# Mais vendidos da Nintendo
n <- srtdes[29:51,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
i<-srtdes[29:51,][order(-dados$Copias_Vendidas),]$Jogos
barplot(n[1:23], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos da Nintendo")
legend("topright",inset = c(-0.6, 0),legend=i[1:23],col = brewer.pal(n = 10, name = "RdBu"), pch = c(11,12),cex=0.8, ncol = 1,lwd=2)
box()
```

```{r}
# Mais vendidos da Bandai
b <- srtdes[1:4,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
d<-srtdes[1:4,][order(-dados$Copias_Vendidas),]$Jogos
barplot(n[1:4], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos da Bandai")
legend("topright",legend=i[1:4],col = brewer.pal(n = 10, name = "RdBu"), lty=1:2, cex=0.8, ncol = 2,lwd=4)
box()
```

```{r}
# Mais vendidos da Game Freak
g <- srtdes[9:12,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
f<-srtdes[9:12,][order(-dados$Copias_Vendidas),]$Jogos
barplot(g[1:4], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos da Game Freak")
legend("topright",legend=f[1:4],col = brewer.pal(n = 10, name = "RdBu"), lty=1:2, cex=0.8, ncol = 2,lwd=4)
box()
```

```{r}
# Mais vendidos de Outras desenvolvedoras
ou <- srtdes[54:71,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
tr<-srtdes[54:71,][order(-dados$Copias_Vendidas),]$Jogos
barplot(ou[1:18], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos de outras Desenvolvedoras")
legend("topright",legend=tr[1:18],col = brewer.pal(n = 10, name = "RdBu"), lty=1:2, cex=0.8, ncol = 2,lwd=4)
box()
```

```{r}
#Publicadora
srtpub <- dados[order(dados$Publicador),]

# Mais vendidos da Nintendo
nin <- srtpub[7:30,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
ten<-srtpub[7:30,][order(-dados$Copias_Vendidas),]$Jogos
barplot(nin[1:23], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos publicados pela Nintendo")
legend("topright",legend=ten[1:23],col = brewer.pal(n = 10, name = "RdBu"), lty=1:2, cex=0.8, ncol = 2,lwd=4)
box()
```

```{r}
# Mais vendidos da Bandai
ban <- srtpub[1:4,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
dai<-srtpub[1:4,][order(-dados$Copias_Vendidas),]$Jogos
barplot(ban[1:4], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos publicados pela Bandai")
legend("topright",legend=dai[1:4],col = brewer.pal(n = 10, name = "RdBu"), lty=1:2, cex=0.8, ncol = 2,lwd=4)
box()
```

```{r}
# Mais vendidos da Capcom
cap <- srtpub[5:6,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
com<-srtpub[5:6,][order(-dados$Copias_Vendidas),]$Jogos
barplot(cap[1:2], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos publicados pela Capcom")
legend("topright",legend=com[1:2],col = brewer.pal(n = 10, name = "RdBu"), lty=1:2, cex=0.8, ncol = 2,lwd=4)
box()
```

```{r}
# Mais vendidos de outras Publicadoras
outr <- srtpub[68:73,][order(-dados$Copias_Vendidas),]$Copias_Vendidas
os<-srtpub[68:73,][order(-dados$Copias_Vendidas),]$Jogos
barplot(outr[1:6], col=brewer.pal(n = 10, name = "RdBu"),las=2,main = "Jogos mais vendidos publicados por outras Publicadoras")
legend("topright",legend=os[1:6],col = brewer.pal(n = 10, name = "RdBu"), lty=1:2, cex=0.8, ncol = 2,lwd=4)
box()
```
