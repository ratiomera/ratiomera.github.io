---
title: "Probabiliteti"
subtitle: "Një udhëzues për ngjarjet, arsyetimin e kushtëzuar dhe ndryshoret e rastësishme"
document-id: "topic-02-probability-summary-sq"
course-id: "intro-statistics"
topic-id: "topic-02-probability"
topic-number: "02"
topic-slug: "probability"
document-type: "summary"
locale: "sq"
figure-asset: "topic-02-probability-summary-figure-sq.png"
---

## Qëllimi dhe bazat

Probabiliteti ofron një gjuhë për situatat në të cilat rezultati nuk dihet paraprakisht. **Hapësira e rezultateve**, që zakonisht shënohet me $\Omega$, është bashkësia e të gjitha rezultateve të mundshme që po shqyrtohen. Një **ngjarje** është një grup rezultatesh nga kjo hapësirë. Çdo rezultat i vetëm ose i përket ngjarjes, ose nuk i përket. Kjo mënyrë e të menduarit përmes bashkësive ka rëndësi, sepse rregullat e probabilitetit veprojnë fillimisht mbi ngjarjet dhe vetëm pastaj mbi numrat.

Përfytyro se zgjedh një pllakë të shënuar me një numër nga 1 deri në 10. Hapësira e rezultateve është $\Omega=\{1,2,\ldots,10\}$. Ngjarja $A$ mund të përmbajë pllakat 1, 2 dhe 3, ndërsa ngjarja $D$ përmban pllakat 2, 3 dhe 7. Probabiliteti i cakton çdo ngjarjeje një numër nga 0 deri në 1. Zero do të thotë se ngjarja nuk mund të ndodhë brenda hapësirës së përcaktuar. Një do të thotë se ajo duhet të ndodhë. Vlerat mes zeros dhe njëshit shprehin shkallë pasigurie sipas modelit që po përdoret.

Probabilitetit mund t'i afrohesh përmes rezultateve njësoj të mundshme, frekuencave relative në afat të gjatë ose një modeli të deklaruar. Në secilën qasje, përkufizo procesin dhe hapësirën e rezultateve para se të llogaritësh. Probabiliteti nuk ndahet kurrë nga kushtet e tij. Mundësia e një ngjarjeje mund të ndryshojë kur merr informacion të ri, kur ndryshon mekanizmi i përzgjedhjes ose kur ndryshon popullata për të cilën po flitet.

| Ideja e bashkësisë | Shënimi | Kuptimi me fjalë |
|---|---|---|
| Bashkimi | $A\cup D$ | Rezultatet në $A$, në $D$ ose në të dyja |
| Prerja | $A\cap D$ | Rezultatet që u përkasin njëkohësisht $A$ dhe $D$ |
| Plotësuesja | $A^c$ | Rezultatet në hapësirën e rezultateve që nuk janë në $A$ |
| Ngjarje të papajtueshme | $A\cap B=\varnothing$ | Ngjarje pa asnjë rezultat të përbashkët |

## Idetë kryesore

Rregulli i plotësueses është i dobishëm kur ngjarja e kundërt numërohet më lehtë. Rregulli i mbledhjes parandalon numërimin dy herë të pjesës së përbashkët të dy ngjarjeve. Probabiliteti i kushtëzuar e ngushton grupin referues: $P(A\mid D)$ pyet për probabilitetin e $A$ mes situatave në të cilat dihet se ka ndodhur $D$. Vija vertikale lexohet «duke qenë se». Prandaj emëruesi është probabiliteti i kushtit dhe jo probabiliteti i të gjithë hapësirës së rezultateve.

Pavarësia ka një kuptim të saktë. Ngjarjet $A$ dhe $D$ janë të pavarura kur dijenia se ka ndodhur $D$ nuk e ndryshon probabilitetin e $A$. Kjo ndryshon nga të qenët të papajtueshme. Nëse dy ngjarje janë të papajtueshme dhe njëra ndodh, tjetra nuk mund të ndodhë, kështu që ky informacion ia ndryshon probabilitetin. Përveç rasteve të veçanta me probabilitet zero, ngjarjet e papajtueshme nuk janë të pavarura.

Teorema e Bayes-it e kthen drejtimin e një probabiliteti të kushtëzuar. Ajo ndërthur probabilitetin e një rezultati nën një kusht me shpeshtësinë paraprake të atij kushti. Normat bazë kanë rëndësi: edhe një rezultat që paraqitet më shpesh në një grup mund të shoqërohet me një probabilitet modest të përkatësisë në atë grup kur grupi është i rrallë. Shkruaje çdo ngjarje me fjalë para se të vendosësh numrat, në mënyrë që drejtimi i kushtit të mbetet i dukshëm.

Një **ndryshore e rastësishme** i cakton një vlerë numerike çdo rezultati të një procesi rastësor. Një ndryshore e rastësishme diskrete ka vlera të ndara që mund të numërohen, si numri i përgjigjeve me ankth të lartë në një grup. Një ndryshore e rastësishme e vazhdueshme mund të marrë vlera në një interval, si një pikëzim i matur. Funksioni i masës së probabilitetit për një ndryshore diskrete u cakton probabilitet vlerave të veçanta. Dendësia e probabilitetit për një ndryshore të vazhdueshme përshkruan si shpërndahet probabiliteti nëpër intervale; probabiliteti i një intervali përfaqësohet nga sipërfaqja nën lakoren e dendësisë.

| Modeli ose ideja | Çfarë përshkruan | Pyetja kryesore gjatë leximit |
|---|---|---|
| Shpërndarja binomiale | Numrin e sukseseve në një numër të fiksuar provash të pavarura me probabilitet të pandryshueshëm suksesi | A mund të mbrohen numri i provave, dy rezultatet, pavarësia dhe probabiliteti i pandryshueshëm? |
| Shpërndarja normale | Një model simetrik në formë kambane, i përshkruar nga mesatarja dhe devijimi standard | A i përshtatet modeli ndryshores dhe pyetjes që po bëhet? |
| Shpërndarja e kampionimit | Si ndryshon një statistikë nëpër kampione të përsëritura nga i njëjti proces | Sa pasiguri nga kampioni në kampion duhet pritur? |
| Vlera e pritur | Qendrën afatgjatë të një ndryshoreje të rastësishme, të peshuar me probabilitet | Cila mesatare do të shfaqej pas shumë përsëritjesh të modelit? |

Shpërndarja e kampionimit nuk është shpërndarja e pikëzimeve individuale. Ajo është shpërndarja e një statistike, si mesatarja e kampionit, nëpër kampione të përsëritura hipotetike. Shpërhapja e saj matet me **gabimin standard**. Kampionet më të mëdha zakonisht prodhojnë mesatare kampioni më pak të ndryshueshme kur procesi bazë mbetet i njëjtë. Kjo ide e lidh probabilitetin me intervalet e besimit dhe testet e hipotezave.

## Udhëzuesi i formulave

Për çdo ngjarje $A$, plotësuesja e saj përmban të gjitha rezultatet jashtë $A$. Probabilitetet e tyre japin së bashku një:

$$
P(A^c)=1-P(A)
$$

Për dy ngjarje, mblidhi probabilitetet e tyre dhe zbrite një herë pjesën e përbashkët. Zbritja korrigjon numërimin e dyfishtë që krijohet kur pjesa e përbashkët përfshihet në të dy termat e parë:

$$
P(A\cup D)=P(A)+P(D)-P(A\cap D)
$$

Nëse ngjarjet janë të papajtueshme, prerja e tyre është boshe dhe termi i pjesës së përbashkët është zero. Mos e përdor rregullin e shkurtuar për ngjarje të papajtueshme para se hapësira e rezultateve të vërtetojë se të dyja ngjarjet nuk mund të ndodhin njëkohësisht.

Probabiliteti i kushtëzuar e kufizon vëmendjen te kushti $D$. Ai kërkon që $P(D)>0$:

$$
P(A\mid D)=\frac{P(A\cap D)}{P(D)}
$$

Rregulli i shumëzimit del nga e njëjta marrëdhënie. Ai tregon edhe kushtin e nevojshëm për pavarësi. Nëse $A$ dhe $D$ janë të pavarura, atëherë $P(A\mid D)=P(A)$ dhe probabiliteti i tyre i përbashkët faktorizohet:

$$
P(A\cap D)=P(A\mid D)P(D)=P(A)P(D)
$$

Teorema e Bayes-it e kthen kushtin duke përdorur ngjarjen e përbashkët në rend të kundërt:

$$
P(A\mid D)=\frac{P(D\mid A)P(A)}{P(D)}
$$

Kur $A$ dhe $A^c$ mbulojnë të gjitha mundësitë, emëruesi mund të ndërtohet me ligjin e probabilitetit të përgjithshëm:

$$
P(D)=P(D\mid A)P(A)+P(D\mid A^c)P(A^c).
$$

Ky emërues e mban të dukshme normën bazë. Një tabelë me frekuenca natyrore e shpreh të njëjtin përditësim me numërime dhe shpesh është mënyra më e sigurt për të dalluar ndjeshmërinë, probabilitetin e një rezultati pozitiv të rremë dhe probabilitetin e $A$ pasi vrojtohet $D$.

Për një ndryshore të rastësishme diskrete, funksioni i masës së probabilitetit është $p(x)=P(X=x)$, ndërsa funksioni kumulativ i shpërndarjes është

$$
F(x)=P(X\leq x)=\sum_{u\leq x}p(u).
$$

Nëse vlerat e mundshme janë $x_1,\ldots,x_m$, vlera e pritur dhe varianca janë

$$
E(X)=\sum_{j=1}^{m}x_jp(x_j),
\qquad
Var(X)=\sum_{j=1}^{m}\bigl(x_j-E(X)\bigr)^2p(x_j).
$$

Vlera e pritur është pika e baraspeshës në afat të gjatë e modelit të probabilitetit. Ajo nuk është premtim se një vrojtim i vetëm do të jetë i barabartë me të.

Për një ndryshore të rastësishme të vazhdueshme me dendësi $f$, probabiliteti është sipërfaqja nën dendësi përmbi një interval. Funksioni kumulativ i shpërndarjes e jep atë probabilitet intervali pa pasur nevojë për shënimin e analizës matematike:

$$
P(a\lt X\leq b)=F(b)-F(a).
$$

Lartësia e dendësisë nuk është vetë probabilitet dhe, në një model të vazhdueshëm, $P(X=x)=0$ për një pikë të vetme të saktë.

Për një ndryshore të rastësishme binomiale $X$ me $n$ prova dhe probabilitet suksesi $p$, probabiliteti i saktësisht $k$ sukseseve është:

$$
P(X=k)={n\choose k}p^k(1-p)^{n-k}
$$

Koeficienti ${n\choose k}$ numëron sa renditje provash përmbajnë saktësisht $k$ suksese. Përdore këtë model vetëm pasi t'i kesh kontrolluar supozimet e tij dhe jo thjesht sepse rezultati është një numërim.

Modeli binomial jep gjithashtu

$$
E(X)=np,
\qquad
Var(X)=np(1-p).
$$

Një bisht i sipërm si $P(X>k)$ mund të llogaritet përmes plotësueses së tij, $1-P(X\leq k)$. Modeli kërkon një numër të fiksuar provash, dy rezultate në secilën provë, një $p$ të pandryshueshëm dhe prova të pavarura.

Për një ndryshore normale $X\sim N(\mu,\sigma^2)$, standardizo një kufi me

$$
Z=\frac{X-\mu}{\sigma}.
$$

Bishtat e poshtëm përdorin $P(X\leq x)=\Phi(z)$, bishtat e sipërm përdorin $1-\Phi(z)$, ndërsa për një interval zbriten dy sipërfaqe kumulative. Një pyetje e anasjelltë fillon me probabilitetin kumulativ $q$, gjen $z_q=\Phi^{-1}(q)$ dhe kthehet në shkallën fillestare me $x_q=\mu+z_q\sigma$.

Për vrojtime të pavarura me mesatare të popullatës $\mu$ dhe variancë $\sigma^2$, shpërndarja e kampionimit e mesatares së kampionit plotëson

$$
E(\bar X)=\mu,
\qquad
Var(\bar X)=\frac{\sigma^2}{n},
\qquad
SE(\bar X)=\frac{\sigma}{\sqrt n}.
$$

Kur $\sigma$ nuk dihet, $s/\sqrt n$ e vlerëson gabimin standard. Nëse popullata është normale, mesatarja e kampionit ka saktësisht shpërndarje normale. Për popullata të përshtatshme jonormale, shpërndarja e saj mund t'i afrohet normales ndërsa $n$ rritet. Përshtatshmëria e këtij përafrimi varet nga forma e popullatës. Asnjë kufi i vetëm për madhësinë e kampionit nuk e garanton atë.

| Objekti | Çfarë ndryshon | Shpërhapja që duhet raportuar |
|---|---|---|
| Shpërndarja e vlerave individuale | Vrojtimet individuale | Devijimi standard i popullatës ose i kampionit |
| Shpërndarja e kampionimit e $\bar X$ | Mesataret e kampionit nëpër kampione të përsëritura | Gabimi standard $\sigma/\sqrt n$ ose vlerësimi $s/\sqrt n$ |
| Kampioni i realizuar me anshmëri | Rastet e pranuara nga një kornizë ose proces përgjigjeje me të meta | Një gabim standard më i vogël nuk e korrigjon anshmërinë e përzgjedhjes |

## Si lexohet figura shpjeguese

![Katër panele përdorin pllaka me numra për të treguar bashkimin, prerjen, plotësuesen dhe ngjarjet e papajtueshme brenda së njëjtës hapësirë me dhjetë rezultate.](assets/topic-02-probability-summary-figure-sq.png){#fig-summary-t02 width=92%}

Fillo me panelin lart majtas. Ngjarja $A$ përmban 1, 2 dhe 3, ndërsa ngjarja $D$ përmban 2, 3 dhe 7. Bashkimi i tyre thekson 1, 2, 3 dhe 7, sepse «ose» përfshin rezultatet që shfaqen në cilëndo ngjarje dhe rezultatet e përbashkëta. Paneli lart djathtas tregon prerjen. Vetëm 2 dhe 3 janë theksuar, sepse këto janë rezultatet e përbashkëta.

Paneli poshtë majtas tregon plotësuesen e $A$. Pllakat nga 4 deri në 10 janë theksuar, sepse çdo rezultat në hapësirën e rezultateve duhet të jetë ose në $A$, ose jashtë $A$. Paneli poshtë djathtas paraqet ngjarjen $B$, e cila përmban 4, 5, 6 dhe 7. $A$ dhe $B$ nuk kanë pllaka të përbashkëta, prandaj janë të papajtueshme. Ngjyrat tregojnë përkatësinë dhe jo madhësinë e probabilitetit. Nëse dhjetë pllakat do të ishin njësoj të mundshme, numri i pllakave të theksuara mund të pjesëtohej me dhjetë. Nëse rezultatet nuk do të ishin njësoj të mundshme, numërimi i pllakave nuk do të mjaftonte dhe do të duheshin probabilitetet që u janë caktuar.

Kjo figurë të ndihmon ta kontrollosh shënimin para se të përdorësh një formulë. Identifiko fillimisht pllakat përkatëse dhe pastaj ktheje atë bashkësi në një probabilitet. Ky rend zvogëlon gabimet e zakonshme, si trajtimi i «ose»-s si përjashtuese, harrimi i pjesës së përbashkët në rregullin e mbledhjes ose ngatërrimi i papajtueshmërisë me pavarësinë.

## Lista e kontrollit për interpretim

Përkufizo procesin rastësor, hapësirën e rezultateve dhe secilën ngjarje me fjalë. Kontrollo nëse rezultatet janë njësoj të mundshme para se të përdorësh numërimet. Për probabilitetin e kushtëzuar, emërto kushtin dhe përdore si grup referues. Vizato një bashkësi, tabelë ose pemë probabiliteti kur drejtimi i kushtit të duket i paqartë. Dallo ngjarjet e papajtueshme nga ngjarjet e pavarura. Për një ndryshore të rastësishme, thuaj nëse është diskrete apo e vazhdueshme dhe përcakto çfarë përfaqëson një vlerë.

Kur zgjedh një shpërndarje, përputhi supozimet e saj me procesin. Raporto nëse probabiliteti vjen nga një model teorik, një frekuencë relative e vrojtuar ose një simulim. Kujto se simulimi përafron pasojat e rregullave të deklaruara; ai nuk i rregullon supozimet e papërshtatshme. Për një shpërndarje kampionimi, mbaji vrojtimet individuale të ndara nga statistikat e kampionit dhe thuaj çfarë do të ndryshonte nëpër kampione të përsëritura.

## Si lidhet kjo temë me të tjerat

Statistika përshkruese e përmblodhi grupin e vrojtuar të të dhënave. Probabiliteti tani përshkruan si mund të ndryshojnë rezultatet nën një proces rastësor. Inferenca statistikore i bashkon këto ide: ajo përdor shpërndarjen e kampionimit të një statistike për të gjykuar sa pajtohet një rezultat i vrojtuar me një pohim për popullatën dhe për të shprehur pasigurinë rreth një vlerësimi.

Edhe modelet e mëvonshme mbështeten te probabiliteti. Një koeficient korrelacioni ose regresioni ndryshon nga një kampion në tjetrin. Intervalet e besimit dhe testet e përshkruajnë këtë ndryshueshmëri me modele probabiliteti. Analiza e variancës krahason ndryshueshmërinë sistematike dhe reziduale përmes një shpërndarjeje $F$. Shënimi bëhet më i pasur, por pyetjet qendrore mbeten të njohura: Cilat janë rezultatet e mundshme, cilat kushte po supozohen dhe cilën pasiguri përfaqëson probabiliteti?
