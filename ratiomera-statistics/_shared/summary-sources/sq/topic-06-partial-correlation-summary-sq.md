---
title: "Korrelacioni i pjesshëm"
subtitle: "Të lexosh një lidhje pas përshtatjes lineare për një ndryshore të tretë"
document-id: "topic-06-partial-correlation-summary-sq"
course-id: "intro-statistics"
topic-id: "topic-06-partial-correlation"
topic-number: "06"
topic-slug: "partial-correlation"
document-type: "summary"
locale: "sq"
figure-asset: "topic-06-partial-correlation-summary-figure-sq.png"
---

## Qëllimi dhe bazat

Korrelacioni i pjesshëm përshkruan lidhjen lineare mes dy ndryshoreve pasi hiqet lidhja lineare e përshtatur që secila prej tyre ka me një ndryshore të tretë të matur. Me ndryshoret qendrore $X$ dhe $Y$ dhe ndryshoren e kontrollit $Z$, korrelacioni i pjesshëm i rendit të parë shënohet $r_{XY\cdot Z}$. Lexoje pikën si «duke kontrolluar për». Koeficienti pyet nëse rastet që janë më lart nga sa pritet në $X$, duke pasur parasysh $Z$, priren të jenë më lart nga sa pritet edhe në $Y$, duke pasur parasysh të njëjtën $Z$.

Shprehja **duke mbajtur $Z$ të pandryshuar** përshkruan një krahasim të bazuar në model. Ajo nuk do të thotë se rastet e vrojtuara kanë fjalë për fjalë një vlerë identike të $Z$. Regresioni linear përdoret për ta parashikuar $X$ nga $Z$ dhe $Y$ nga $Z$. Reziduali i çdo rasti shënon sa larg mbi ose nën atë parashikim ndodhet vlera e vrojtuar. Korrelacioni i pjesshëm është korrelacioni i zakonshëm i Pearson-it mes këtyre dy grupeve të rezidualeve.

Kjo metodë i përgjigjet një pyetjeje për lidhjen e kushtëzuar. Ajo mund të tregojë se një korrelacion i papërshtatur zvogëlohet, rritet ose ndryshon shenjë pas përshtatjes. Vetë metoda nuk mund të vendosë nëse $Z$ është ndryshore ngatërruese, ndërmjetësuese, përplasëse ose kontroll i përshtatshëm. Këto role lidhen me procesin që i krijon të dhënat dhe kërkojnë arsyetim përmbajtësor, rend kohor dhe dizajn kërkimor.

| Madhësia | Çfarë korrelon | Pyetja që merr përgjigje |
|---|---|---|
| Korrelacioni i papërshtatur $r_{XY}$ | $X$ e vrojtuar me $Y$ e vrojtuar | Si lidhen linearisht dy ndryshoret e matura? |
| Korrelacioni i pjesshëm $r_{XY\cdot Z}$ | $X$ e rezidualizuar me $Y$ e rezidualizuar | Si lidhen përbërësit e tyre të mbetur linearë pas përshtatjes për $Z$? |

## Idetë kryesore

Rezidualizimi kryhet në tre hapa të qartë. Së pari, regreso $X$ mbi $Z$ dhe ruaje çdo rezidual $e_{Xi}$. Së dyti, regreso $Y$ mbi $Z$ dhe ruaje çdo rezidual $e_{Yi}$. Së treti, llogarit korrelacionin e Pearson-it mes $e_X$ dhe $e_Y$. Vlerat mbi zero në një ndryshore të rezidualizuar do të thonë «më e lartë se parashikimi linear i bazuar në $Z$», ndërsa vlerat nën zero do të thonë «më e ulët se parashikimi».

Standardizimi i ndryshoreve fillestare nuk e kryen këtë përshtatje. Standardizimi zbret një mesatare dhe pjesëton me një devijim standard. Ai i përputh njësitë dhe pikat e referimit, ndërsa e ruan korrelacionin e Pearson-it. Rezidualizimi e heq përbërësin linear të përshtatur që lidhet me ndryshoren e kontrollit. Ky dallim ka rëndësi, sepse dy grafikë mund të kenë boshte të standardizuara njësoj, por korrelacione të ndryshme pas rezidualizimit.

| Ndryshimi i vrojtuar i koeficientit | Lexim i mundshëm | Çfarë duhet kontrolluar ende |
|---|---|---|
| Koeficienti i pjesshëm është më i vogël | Një pjesë e mbivendosjes së papërshtatur ishte e përbashkët me $Z$ | Nëse $Z$ është kontroll i mbrojtshëm dhe modelet janë të përshtatshme |
| Koeficienti i pjesshëm është i ngjashëm | Përshtatja lineare për $Z$ ndryshoi pak | Efektet jolineare, matja, diapazoni dhe pasiguria e kampionimit |
| Koeficienti i pjesshëm është më i madh | Përshtatja zbuloi një lidhje të fshehur më parë | Nëse shtypja ka kuptim përmbajtësor dhe nuk është model i rastësishëm |

Përshtatja është lineare. Nëse $Z$ ka marrëdhënie të lakuar me $X$ ose $Y$, një rezidualizim në vijë të drejtë mund të lërë pas strukturë sistematike. Metoda trashëgon gjithashtu nga korrelacioni i Pearson-it dhe regresioni ndjeshmërinë ndaj vrojtimeve me ndikim dhe kufizimit të diapazonit. Shqyrto marrëdhëniet e papërshtatura të $X$ me $Y$, $X$ me $Z$ dhe $Y$ me $Z$, pastaj shqyrto marrëdhënien e rezidualizuar.

Korrelacioni i pjesshëm ka lidhje të ngushtë konceptuale me regresionin e shumëfishtë. Të dyja bëjnë pyetje lineare të kushtëzuara pasi merret parasysh informacion tjetër i matur. Koeficientët e tyre numerikë kanë shkallë të ndryshme: korrelacioni i pjesshëm standardizohet në intervalin nga $-1$ deri në $1$, ndërsa pjerrësia e mëvonshme e regresionit shpreh një dallim të përshtatur në rezultat për një njësi parashikuese. Tema 7 e zhvillon këtë kornizë më të gjerë me disa ndryshore parashikuese.

## Udhëzuesi i formulave

Rezidualizimi i $X$ kundrejt $Z$ fillon me një vijë të përshtatur dhe ruan atë që vija nuk shpjegon:

$$
e_{Xi}=x_i-(a_X+b_Xz_i)
$$

Kryeje veprimin përkatës për $Y$:

$$
e_{Yi}=y_i-(a_Y+b_Yz_i)
$$

Pastaj korrelacioni i pjesshëm është korrelacioni i Pearson-it i dy ndryshoreve reziduale:

$$
r_{XY\cdot Z}=r(e_X,e_Y)
$$

Kur kontrollohet saktësisht një ndryshore $Z$, koeficienti mund të llogaritet edhe nga tre korrelacionet dyshe:

$$
r_{XY\cdot Z}=\frac{r_{XY}-r_{XZ}r_{YZ}}{\sqrt{(1-r_{XZ}^2)(1-r_{YZ}^2)}}
$$

Kjo formulë është e përmbledhur, por metoda e rezidualeve shpesh kuptohet dhe diagnostikohet më lehtë, sepse i tregon drejtpërdrejt dy modelet e përshtatjes. Dy rrugët japin të njëjtin rezultat kur përdorin të njëjtat raste të plota, regresione lineare të zakonshme me konstante dhe të njëjtat tri ndryshore të matura. Kjo përputhje kontrollon llogaritjen; ajo nuk vërteton se kontrolli ishte i përshtatshëm në kuptimin shkakor.

Emëruesi tregon gjithashtu kur përkufizohet formula e drejtpërdrejtë. Nëse $|r_{XZ}|=1$ ose $|r_{YZ}|=1$, njëra ndryshore qendrore e rezidualizuar nuk ka më ndryshueshmëri dhe emëruesi është zero. Korrelacioni nuk mund të llogaritet për një ndryshore pa shpërhapje. Marrëdhëniet pothuajse të përsosura me $Z$ mund ta bëjnë po ashtu rezultatin e përshtatur shumë të ndjeshëm ndaj ndryshimeve të vogla ose rrumbullakimit.

| Lloji i kontrollit | Çfarë ndryshon | Çfarë përfundimi mund të mbështesë |
|---|---|---|
| Kontrolli eksperimental | Dizajni i studimit i cakton ose i mban kushtet para se të vrojtohen rezultatet | Mund ta forcojë një krahasim shkakor kur dizajni dhe supozimet e arsyetojnë |
| Kontrolli statistikor | Analiza përfaqëson marrëdhëniet lineare të përshtatura me $Z$ të matur | Jep një lidhje të përshtatur dhe jo caktim të rastësishëm |
| Ndryshorja e tretë e pamatur | Asgjë në llogaritje nuk e përfaqëson | Kontributi i saj i mundshëm mbetet i pazgjidhur |

Rezidualizimi heq vetëm përbërësin linear të përshtatur që lidhet me versionin e matur të $Z$. Ai nuk prodhon ndryshore pa gabime, nuk i heq automatikisht marrëdhëniet jolineare dhe nuk garanton se $Z$ ishte kontroll i përshtatshëm.

## Si lexohet figura shpjeguese

![Dy diagrame shpërndarjeje krahasojnë lidhjen e papërshtatur të standardizuar me lidhjen mes rezidualeve të standardizuara pas përshtatjes lineare për një masë të tretë.](assets/topic-06-partial-correlation-summary-figure-sq.png){#fig-summary-t06 width=92%}

Paneli i majtë paraqet masat e standardizuara të praktikës dhe vlerësimit. Njësitë e devijimit standard e vendosin zeron te mesatarja e secilës ndryshore dhe e bëjnë një njësi të barabartë me një devijim standard të kampionit. Vija e dukshme në rritje dhe korrelacioni dysh i raportuar prej 0.607 përshkruajnë një lidhje lineare të papërshtatur mesatarisht pozitive në këto vlera të simuluara.

Paneli i djathtë paraqet rezidualet e standardizuara pasi të dyja ndryshoret janë parashikuar nga masa e kontrollit. Tani çdo koordinatë horizontale tregon sa larg mbi ose nën vlerën e parashikuar nga kontrolli ndodhet vlera e praktikës e një rasti. Çdo koordinatë vertikale tregon largimin përkatës të vlerësimit. Vija ende ngrihet, por më pak në njësitë e standardizuara, dhe korrelacioni i pjesshëm është 0.337. Pra përshtatja e zvogëloi lidhjen e matur, por la një marrëdhënie pozitive reziduale.

Nëntitulli i figurës thekson se vetëm standardizimi nuk e ndryshon asnjërin korrelacion. Koeficienti ndryshon sepse paneli i dytë përdor reziduale, jo sepse boshtet e tij janë standardizuar. Dallimi mes 0.607 dhe 0.337 është një shenjë përshkruese se një pjesë e bashkëndryshimit të papërshtatur përputhej me ndryshoren e kontrollit. Ai nuk është diagnozë e shkakësisë dhe duhet interpretuar bashkë me tre diagramet dyshe të papërshtatura dhe rolin përmbajtësor të kontrollit.

## Lista e kontrollit për interpretim

Emërto $X$, $Y$ dhe çdo ndryshore kontrolli dhe shpjego pse secili kontroll i përket analizës. Përshkruaje me fjalë rendin e supozuar kohor ose shkakor para se të përshtatësh. Shqyrto të gjitha diagramet dyshe të papërshtatura, modelet e të dhënave që mungojnë, diapazonin dhe vrojtimet me ndikim. Kontrollo nëse marrëdhëniet e përshtatjes janë në mënyrë të arsyeshme lineare. Raporto së bashku korrelacionet e papërshtatura dhe të pjesshme, në mënyrë që të shihet çfarë ndryshoi.

Përshkruaje koeficientin si lidhje pas përshtatjes lineare për ndryshoren e tretë të emërtuar. Raporto madhësinë e kampionit, tre korrelacionet dyshe dhe korrelacionin e pjesshëm që rezulton, në mënyrë që llogaritja të mund të ndiqet. Mos e interpreto zvogëlimin e koeficientit si provë automatike të ngatërrimit, rritjen si provë automatike të shtypjes ose një vlerë pranë zeros si provë të mungesës së marrëdhënies. Mbaji parasysh gjatë gjithë kohës cilësinë e matjes dhe pasigurinë e kampionimit.

## Si lidhet kjo temë me të tjerat

Kovarianca dhe korrelacioni i Pearson-it paraqitën bashkëndryshimin linear të çiftuar. Regresioni i thjeshtë e ndau më pas çdo rezultat në një vlerë të përshtatur dhe një rezidual. Korrelacioni i pjesshëm i bashkon këto ide: përdor dy regresione për t'i hequr përbërësit që lidhen linearisht me $Z$ dhe pastaj korrelon përbërësit që mbeten.

Regresioni i shumëfishtë është hapi i natyrshëm vijues. Ai vlerëson kontributin e kushtëzuar të disa ndryshoreve parashikuese në një model të vetëm të rezultatit dhe jep pjerrësi në njësitë e tyre fillestare. Këndvështrimi i korrelacionit të pjesshëm mbetet i dobishëm, sepse shpjegon çfarë do të thotë «duke mbajtur të pandryshuara ndryshoret e tjera»: krahaso rastet përmes pjesëve të një ndryshoreje parashikuese dhe të rezultatit që mbeten pas përshtatjes lineare. Kjo lidhje e kthen një shprehje teknike në një krahasim konkret të rezidualeve.
