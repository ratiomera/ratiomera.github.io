---
title: "Statistika përshkruese"
subtitle: "Një udhëzues i afërt për ndryshoret, shpërndarjet dhe përmbledhjet numerike"
document-id: "topic-01-descriptive-statistics-summary-sq"
course-id: "intro-statistics"
topic-id: "topic-01-descriptive-statistics"
topic-number: "01"
topic-slug: "descriptive-statistics"
document-type: "summary"
locale: "sq"
figure-asset: "topic-01-descriptive-statistics-summary-figure-sq.png"
---

## Qëllimi dhe bazat

Statistika përshkruese të jep një mënyrë të rregullt për ta kthyer një grup vrojtimesh në një përshkrim të kuptueshëm të asaj që është vrojtuar. Fillo duke përcaktuar **rastet**, pra njerëzit ose njësitë që përfaqësohen nga rreshtat e një grupi të dhënash, dhe **ndryshoret**, pra karakteristikat e regjistruara në kolonat e tij. Një vlerë është një rezultat i regjistruar për një ndryshore te një rast. Para se të llogaritësh, pyet çfarë do të thotë ndryshorja, si është matur dhe cilat vlera mund të marrë. Kjo e parandalon një llogaritje matematikisht të saktë të kthehet në një përshkrim çorientues.

Niveli i matjes udhëzon çfarë mund të bësh në mënyrë të arsyeshme me një ndryshore. Një ndryshore nominale i ndan rastet në kategori pa rend. Një ndryshore rendore ka kategori të renditura, por largësitë mes kategorive fqinje nuk dihet nëse janë të barabarta. Një ndryshore intervalore ka largësi të barabarta me kuptim, por nuk ka një zero absolute me kuptim. Një ndryshore e raportit ka largësi të barabarta dhe një zero me kuptim, prandaj mund të interpretohen edhe raportet. Niveli i matjes është veti e mënyrës si përkufizohet dhe matet ndryshorja. Ai nuk varet nga pamja që marrin vlerat e saj në një grup të vetëm të dhënash.

| Shkalla | Çfarë tregojnë vlerat | Përmbledhje të përshtatshme fillestare |
|---|---|---|
| Nominale | Nëse rastet i përkasin së njëjtës kategori apo kategorive të ndryshme | Frekuencat, përpjesëtimet, moda |
| Rendore | Përkatësinë në kategori dhe rendin | Frekuencat, përpjesëtimet, mediana, kuantilet |
| Interval/raport | Rendin dhe largësinë numerike me kuptim | Mesatarja, mediana, varianca, devijimi standard, kuantilet |

Disa nga grupet e të dhënave që përdoren në këtë rrjedhë mësimore janë **të dhëna të simuluara**, domethënë vlera të krijuara nga kompjuteri sipas rregullave të deklaruara dhe jo matje të mbledhura nga njerëz realë. **Simulimi** është procesi që i krijon këto vlera. Kompjuteri përdor një **gjenerator të numrave të rastësishëm**, pra një algoritëm të ndërtuar për të prodhuar vlera që sillen si rezultate rastësie. **Numri nisës** është vlera fillestare që i jepet atij algoritmi. Kur ripërdoret i njëjti numër nisës me të njëjtat udhëzime, rikrijohet i njëjti grup i të dhënave. Kjo e bën shembullin mësimor të riprodhueshëm: ti dhe një person tjetër që mëson mund të shqyrtoni të njëjtat vrojtime dhe të merrni të njëjtat rezultate. Simulimi e mbështet të nxënit, por nuk i shndërron vlerat e krijuara në evidencë për një popullatë reale.

## Idetë kryesore

Një shpërndarje përshkruan si shtrihen vlerat e një ndryshoreje në diapazonin e tyre të mundshëm. Për një ndryshore kategorike, fillo me një tabelë frekuencash. Frekuenca absolute është numri i rasteve në një kategori. Frekuenca relative është ky numër i pjesëtuar me numrin e përgjithshëm të rasteve të vlefshme. Frekuencat relative mund të paraqiten si përpjesëtime ose përqindje. Kontrollo gjithmonë nëse vlerat që mungojnë janë përjashtuar nga emëruesi, sepse një përqindje ka kuptim vetëm kur dihet totali i saj referues.

Për një ndryshore numerike, përshkruaj së bashku katër veçori: qendrën, ndryshueshmërinë, formën dhe vrojtimet e pazakonta. Mesatarja përdor çdo vlerë dhe përfaqëson pikën e baraspeshës së shpërndarjes. Mediana është vlera e mesit pasi vlerat renditen dhe i ndan të dhënat në dy gjysma. Moda është vlera ose kategoria më e shpeshtë. Amplituda shtrihet nga vlera më e vogël te vlera më e madhe. Diapazoni ndërkuartilor përfshin gjysmën e mesme të vrojtimeve të renditura. Varianca dhe devijimi standard përmbledhin sa larg priren të jenë vlerat nga mesatarja.

| Pyetja | Evidencë e dobishme | Zakon i dobishëm leximi |
|---|---|---|
| Ku gjendet qendra e shpërndarjes? | Mesatarja, mediana dhe ndonjëherë moda | Krahaso mesataren me medianën në vend që të raportosh vetëm një numër |
| Sa ndryshojnë vrojtimet? | Amplituda, diapazoni ndërkuartilor, varianca, devijimi standard | Trego njësitë dhe vëzhgo vlerat e pazakonta |
| Çfarë forme krijojnë vlerat? | Histogrami, diagrami kuti-me-mustaqe, frekuencat, asimetria | Kërko simetri, anim, boshllëqe, grumbullime dhe më shumë se një kulm |
| A ka vlera befasuese? | Vlerat e papërpunuara, grafiku, kontrollet e të dhënave, pikëzimet e standardizuara | Heto para se të vendosësh nëse një vlerë është gabim |

Forma ndikon në interpretim. Në një shpërndarje afërsisht simetrike, mesatarja dhe mediana shpesh janë të ngjashme. Një bisht i gjatë djathtas priret ta tërheqë mesataren lart, ndërsa një bisht i gjatë majtas priret ta tërheqë poshtë. **Modaliteti** përshkruan numrin dhe modelin e kulmeve ose grumbullimeve kryesore që dallohen qartë. Një shpërndarje mund të jetë unimodale, me një kulm kryesor, ose multimodale, me më shumë se një grumbullim. **Kurtoza** përshkruan sa lehtë shfaqen vlerat larg në bishta, krahasuar me një shpërndarje referuese simetrike në formë kambane me të njëjtën shpërhapje të përgjithshme. Vetëm lartësia e kulmit nuk e përcakton kurtozën. Një numër i vetëm si mesatarja nuk mund t'i tregojë këto veçori, prandaj grafiku dhe përmbledhjet numerike duhen lexuar së bashku.

Një vrojtim i pazakontë nuk është automatikisht gabim. Mund të jetë rast i vlefshëm por i rrallë, gabim kodimi, problem matjeje ose shenjë se janë bashkuar grupe të ndryshme. Kontrollo përkufizimin fillestar dhe procesin e regjistrimit para se të përjashtosh diçka. Nëse një vendim analitik ndryshon pasi hiqet një vrojtim, raportoje këtë ndjeshmëri dhe mos e fshih.

## Udhëzuesi i formulave

Për kategorinë ose intervalin $j$, le të jetë $n_j$ frekuenca e tij absolute dhe $n$ numri i vrojtimeve të vlefshme. Frekuenca relative e tij është

$$
f_j=\frac{n_j}{n}.
$$

Për kategori të renditura ose intervale numerike, frekuenca relative kumulative deri te kategoria $j$ është

$$
F_j=\sum_{h=1}^{j}f_h.
$$

Frekuencat absolute duhet të japin gjithsej $n$, frekuencat relative duhet të japin 1 me përjashtim të ndryshimeve nga rrumbullakimi, ndërsa frekuenca relative kumulative e fundit duhet të jetë 1. Frekuencat kumulative kanë kuptim vetëm kur kategoritë kanë një rend që mund të arsyetohet.

Le të jenë $x_1, x_2, \ldots, x_n$ vlerat e vrojtuara të një ndryshoreje numerike. Mesatarja e kampionit i mbledh të gjitha vlerat dhe e pjesëton shumën me numrin e vrojtimeve:

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
$$

Shenja $\sum$ do të thotë «mblidh vlerat e treguara». Indeksi $i$ identifikon nga një vrojtim, duke filluar nga vrojtimi i parë e deri te vrojtimi $n$. Devijimi $x_i-\bar{x}$ tregon sa larg mbi ose nën mesatare gjendet një vlerë. Kur mblidhen, devijimet pozitive dhe negative e anulojnë njëra-tjetrën. Prandaj, për variancën ato ngrihen fillimisht në katror. Varianca e kampionit përdor $n-1$ në emërues:

$$
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

Varianca përkatëse e popullatës përdor mesataren e popullatës $\mu$ dhe pjesëton me madhësinë e popullatës $N$:

$$
\sigma^2=\frac{1}{N}\sum_{i=1}^{N}(x_i-\mu)^2.
$$

Mbaji të ndara dy madhësitë që synohen. Emëruesi $n-1$ i përket variancës së korrigjuar të kampionit, e cila përdoret për të vlerësuar ndryshueshmërinë e popullatës. Pjesëtimi me $N$ përshkruan vetë vlerat e popullatës së plotë.

Meqë varianca shprehet në njësi të ngritura në katror, marrim rrënjën e saj katrore për t'u kthyer te njësia fillestare e matjes. Prandaj devijimi standard i kampionit është:

$$
s=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

Një pikëzim i standardizuar e shpreh një vlerë në njësi të devijimit standard. Ai zbret mesataren e kampionit dhe pjesëton me devijimin standard të kampionit:

$$
z_i=\frac{x_i-\bar{x}}{s}
$$

Një $z_i$ pozitiv e vendos vlerën mbi mesatare, një $z_i$ negativ e vendos nën mesatare, ndërsa madhësia e tij tregon largësinë në devijime standarde. Standardizimi ndryshon njësinë dhe pikën e referimit, por nuk ndryshon rendin ose formën e vrojtimeve.

Mediana dhe kuantilet fillojnë nga vrojtimet e renditura. Kuartili i parë $Q_1$ shënon çerekun e poshtëm, mediana $Q_2$ shënon pikën e mesit dhe kuartili i tretë $Q_3$ shënon tre të katërtat e poshtme. Amplituda dhe diapazoni ndërkuartilor janë

$$
\text{amplituda}=x_{\max}-x_{\min},
\qquad
IQR=Q_3-Q_1.
$$

Konventat për kuantilet e kampionit mund të ndërfusin vlera në mënyra të ndryshme, prandaj programet mund të raportojnë kuartile paksa të ndryshme për një grup të vogël të dhënash. Një kontroll i zakonshëm në diagramin kuti-me-mustaqe përdor kufijtë e brendshëm

$$
Q_1-1.5(IQR)
\qquad\text{dhe}\qquad
Q_3+1.5(IQR).
$$

Vlerat përtej një kufiri janë vlera të mundshme të veçuara që duhen shqyrtuar, jo gabime që duhen fshirë automatikisht. Mustaqet ndalen te vlerat më skajore të vrojtuara që ende gjenden brenda kufijve. Ato nuk përfundojnë domosdoshmërisht pikërisht te vlerat e kufijve.

Për një transformim linear $Y=a+bX$, qendra dhe shpërhapja ndryshojnë sipas

$$
\bar y=a+b\bar x,
\qquad
s_y^2=b^2s_x^2,
\qquad
s_y=|b|s_x.
$$

Zhvendosja $a$ e ndryshon vendndodhjen, por jo shpërhapjen. Shumëzuesi $b$ i ndryshon largësitë me $|b|$, prandaj varianca ndryshon me $b^2$. Standardizimi është rasti i veçantë që zbret mesataren dhe pjesëton me devijimin standard.

Lartësia e histogramit kërkon një kontroll të fundit. Nëse intervali $j$ ka frekuencë relative $f_j$ dhe gjerësi $w_j$, lartësia e dendësisë është

$$
h_j=\frac{f_j}{w_j}.
$$

Atëherë sipërfaqja e shtyllës është $h_jw_j=f_j$. Kur intervalet kanë gjerësi të barabartë, lartësia mund ta pasqyrojë drejtpërdrejt frekuencën. Kur gjerësitë ndryshojnë, duhen përdorur lartësitë e dendësisë, në mënyrë që sipërfaqja dhe jo vetëm lartësia të vazhdojë ta përfaqësojë frekuencën.

## Si lexohet figura shpjeguese

![Histogram i pikëzimeve të simuluara të ankthit nga provimi prej zeros deri në dyzet, me shtyllat më të larta pranë qendrës dhe bishta më të rrallë në të dy skajet.](assets/topic-01-descriptive-statistics-summary-figure-sq.png){#fig-summary-t01 width=92%}

Lexo fillimisht boshtin horizontal. Ai jep pikëzimet e ankthit nga provimi në një shkallë nga 0 deri në 40. Boshti vertikal jep numrin e studentëve, prandaj lartësia e secilës shtyllë është një frekuencë. Shtyllat rreth pikëzimeve 18 deri në 22 janë më të lartat, gjë që e vendos grumbullimin kryesor pranë qendrës së shkallës. Në skajin e poshtëm dhe të sipërm ka më pak vrojtime. Një shtyllë pranë 40 tregon se ka të paktën një vlerë të lartë, por vetëm grafiku nuk tregon nëse ajo vlerë është e gabuar. Para se ta gjykosh, duhet të kthehesh te përkufizimi i të dhënave dhe procesi i regjistrimit.

Shtyllat prekin njëra-tjetrën sepse një shkallë numerike vazhdon përmes intervaleve fqinje. Gjerësia e tyre ka rëndësi: ndryshimi i kufijve të intervaleve mund t'i bëjë të njëjtat vrojtime të duken më shumë ose më pak të hollësishme. Prandaj figura duhet lexuar si pamje e një shpërndarjeje dhe jo si grup kategorish të ndara. Ajo mbështet pohime për qendrën, shpërhapjen, formën dhe vrojtimet e pazakonta. Nuk tregon një shkak të ankthit, nuk krahason një popullatë me një tjetër dhe nuk vërteton se modeli i simuluar ndodh te studentët realë.

## Lista e kontrollit për interpretim

Fillo çdo përshkrim me rastet, ndryshoren, nivelin e saj të matjes dhe diapazonin e vlefshëm. Trego numrin e vrojtimeve të vlefshme dhe atyre që mungojnë. Për një ndryshore kategorike, raporto frekuencat bashkë me emëruesin dhe përpjesëtimet. Për një ndryshore numerike, bashko një grafik me masa të qendrës dhe ndryshueshmërisë. Përdor mesataren dhe devijimin standard kur interpretimi i tyre i përshtatet shpërndarjes. Shqyrto edhe medianën dhe diapazonin ndërkuartilor kur kanë rëndësi animi ose vrojtimet e pazakonta.

Mbaje të dukshme njësinë. Një devijim standard prej pesë pikësh do të thotë diçka tjetër nga pesë orë. Mos e përshkruaj një grup si homogjen ose të ndryshueshëm pa një referencë që e bën krahasimin me kuptim. Kontrollo nëse një tabelë e rrumbullakosur ende jep totalin e pritur. Shënoji të dhënat e simuluara si të simuluara. Në fund, ndaj përshkrimin nga shpjegimi: një model në vlerat e vrojtuara tregon çfarë përmban grupi i të dhënave, ndërsa një shpjegim shkakor kërkon dizajn kërkimor dhe arsyetim përtej statistikës përshkruese.

## Si lidhet kjo temë me të tjerat

Statistika përshkruese siguron gjuhën që përdoret në tërë kursin. Probabiliteti shton rregulla për arsyetimin mbi rezultate të pasigurta. Inferenca statistikore përdor pastaj një kampion dhe ndryshueshmërinë e tij për të bërë pohime të kujdesshme për një popullatë. Kovarianca dhe korrelacioni pyesin si ndryshojnë së bashku dy ndryshore. Regresioni e shpreh një ndryshore rezultati si funksion të një ose më shumë ndryshoreve parashikuese, ndërsa korrelacioni i pjesshëm studion një lidhje pas përshtatjes lineare. Analiza e variancës krahason mesataret e grupeve duke e ndarë ndryshueshmërinë e përgjithshme në përbërës me kuptim.

Zakoni qendror mbetet i pandryshuar: kupto ndryshoret, shqyrto shpërndarjen, llogarit një përmbledhje të përshtatshme dhe interpretoje në kontekst. Metodat e mëvonshme shtojnë pasiguri dhe modele, por nuk e heqin kurrë nevojën për një përshkrim të besueshëm të të dhënave që hynë në analizë.
