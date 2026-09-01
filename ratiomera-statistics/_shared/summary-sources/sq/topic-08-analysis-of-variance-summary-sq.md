---
title: "Analiza e variancës"
subtitle: "Krahasimi i mesatareve të grupeve duke ndarë ndryshueshmërinë e rezultatit"
document-id: "topic-08-analysis-of-variance-summary-sq"
course-id: "intro-statistics"
topic-id: "topic-08-analysis-of-variance"
topic-number: "08"
topic-slug: "analysis-of-variance"
document-type: "summary"
locale: "sq"
figure-asset: "topic-08-analysis-of-variance-summary-figure-sq.png"
---

## Qëllimi dhe bazat

Analiza e variancës, e shkurtuar ANOVA, i krahason rezultatet mesatare nëpër grupe duke studiuar ndryshueshmërinë. Emri mund të duket befasues, sepse pyetja kërkimore lidhet me mesataret. Metoda funksionon duke e ndarë ndryshueshmërinë e përgjithshme të rezultatit në një pjesë që lidhet me dallimet mes grupeve dhe një pjesë që mbetet mes rasteve brenda të njëjtave grupe. Nëse përbërësi që lidhet me grupin është i madh në raport me ndryshueshmërinë reziduale, të dhënat japin evidencë se jo të gjitha mesataret e grupeve në popullatë janë të barabarta.

Në një ANOVA njëfaktoriale mes grupeve, ka një faktor kategorial dhe një rezultat numerik. **Faktori** është ndryshore parashikuese kategoriale; kategoritë e tij quhen **nivele**. Çdo rast i përket një niveli dhe raste të ndryshme paraqiten në grupe të ndryshme. Hipoteza zero thotë se të gjitha mesataret e grupeve në popullatë janë të barabarta. Alternativa thotë se jo të gjitha mesataret e popullatës janë të barabarta, që do të thotë se të paktën dy prej tyre ndryshojnë. Hedhja poshtë e hipotezës zero nuk tregon cilat grupe ndryshojnë ose sa të mëdha janë dallimet.

Fillo me dizajnin. Identifiko njësinë vrojtuese ose eksperimentale, nivelet e faktorit, rezultatin dhe shkallën e tij, si dhe nëse vrojtimet janë të pavarura apo të përsëritura. Vizato rezultatin sipas grupit dhe raporto madhësitë e kampioneve të grupeve, mesataret, devijimet standarde dhe intervalet. Një statistikë testi nuk mund ta rregullojë një mospërputhje mes dizajnit dhe modelit.

| Madhësia e ANOVA-s | Çfarë regjistron | Shkallët e lirisë në një dizajn njëfaktorial |
|---|---|---|
| Shuma e përgjithshme e katrorëve | Devijimin e secilit rast të ngritur në katror nga mesatarja e përgjithshme | $N-1$ |
| Shuma e katrorëve të faktorit | Devijimet e mesatareve të grupeve nga mesatarja e përgjithshme, të peshuara sipas madhësisë së grupit | $k-1$ |
| Shuma e katrorëve të gabimit | Devijimet individuale nga mesatarja e grupit përkatës | $N-k$ |
| Mesatarja e katrorëve | Shuma e katrorëve e pjesëtuar me shkallët e saj të lirisë | Varet nga përbërësi |

## Idetë kryesore

**Mesatarja e përgjithshme** është mesatarja e të gjitha vrojtimeve. Shuma e përgjithshme e katrorëve mat sa larg gjendet secili rezultat nga ajo mesatare. Shuma e katrorëve të faktorit pyet sa larg gjendet mesatarja e secilit grup nga mesatarja e përgjithshme dhe e peshon këtë largësi të ngritur në katror me madhësinë e grupit. Shuma e katrorëve të gabimit mat sa larg gjendet secili vrojtim nga mesatarja e grupit të vet. Në modelin e zakonshëm njëfaktorial me konstantë, shumat e katrorëve të faktorit dhe gabimit japin saktësisht shumën e përgjithshme të katrorëve.

Shumat e katrorëve rriten me madhësinë e kampionit dhe nuk marrin parasysh sa pjesë të pavarura informacioni janë përdorur. Pjesëtimi i secilit përbërës me shkallët e tij të lirisë jep një mesatare katrorësh. Statistika $F$ e pjesëton mesataren e katrorëve të faktorit me mesataren e katrorëve të gabimit. Nën hipotezën zero dhe supozimet e modelit, të dyja e vlerësojnë të njëjtën variancë gabimi në mënyra të ndryshme, prandaj një raport pranë njëshit është i arsyeshëm. Një raport i madh tregon se ndarja e mesatareve të grupeve është e madhe në raport me ndryshueshmërinë tipike brenda grupeve.

| Pyetja vijuese | Mjeti i përshtatshëm | Fokusi i interpretimit |
|---|---|---|
| A ndryshoi një krahasim shkencor i planifikuar? | Kontrasti i planifikuar | Krahasimi i përcaktuar dhe i peshuar i mesatareve dhe pasiguria e tij |
| Cilat çifte ndryshojnë pas një rezultati të përgjithshëm? | Krahasimet dyshe të përshtatura për shumëfishësinë | Dallimet mes çifteve me kontroll të njëkohshëm të gabimit |
| Si duhet dokumentuar analiza e përgjithshme? | Tabela e plotë ANOVA | Shumat e katrorëve, shkallët e lirisë, mesataret e katrorëve, $F$ dhe vlera p |
| A varet modeli i një faktori nga një tjetër? | ANOVA faktoriale me ndërveprim | Dallimet e dallimeve në vend të efekteve kryesore të veçuara |

Testet e shumta të papërshtatura e rrisin probabilitetin e të paktën një gabimi të llojit I në një familje krahasimesh. Një ANOVA e përgjithshme kontrollon një pyetje të përgjithshme, por nuk i zëvendëson krahasimet pasuese të zgjedhura me kujdes. Kontrastet e planifikuara duhet të vijnë nga pyetja kërkimore. Procedurat dyshe pas analizës përdorin një përshtatje të ndërtuar për familjen që po interpretohet. Raporto dallimet ose kontrastet e vlerësuara mes mesatareve, pasigurinë e tyre dhe vlerat p të përshtatura.

ANOVA faktoriale përmban më shumë se një faktor. Efektet kryesore përmbledhin dallimet mesatare për një faktor nëpër nivelet e faktorit tjetër. Ndërveprimi pyet nëse efekti i një faktori ndryshon nëpër nivelet e faktorit tjetër. Kur ndërveprimi ka kuptim, interpreto mesataret dhe kontrastet e kushtëzuara të grupeve në vend që të mbështetesh vetëm te efektet kryesore.

Të dhënat me matje të përsëritura kërkojnë një model që pranon se disa vrojtime i përkasin të njëjtit person ose të njëjtës njësi. Këto vrojtime janë të korreluara dhe nuk mund të trajtohen si grupe të pavarura. Sfericiteti është një kusht i matjeve të përsëritura që lidhet me variancat e dallimeve dyshe mes niveleve. Kur ky kusht nuk është i arsyeshëm, kërkohet korrigjimi i shkallëve të lirisë ose një model i përshtatshëm për të dhëna të përsëritura. Këndvështrimi i efekteve të rastësishme e ndan ndryshueshmërinë mes grupeve ose njerëzve nga ndryshueshmëria brenda tyre; koeficienti i korrelacionit brenda klasës përmbledh sa fort ngjajnë me njëra-tjetrën vrojtimet nga i njëjti grup.

Modeli i zakonshëm mes grupeve supozon vrojtime të pavarura, strukturë të përshtatshme të mesatares dhe varianca reziduale të përshtatshme për inferencën e synuar $F$. Diagnostika e rezidualeve dhe paraqitjet e grupeve kanë rëndësi. Kur variancat dhe madhësitë e grupeve janë të pabarabarta, testi standard me gabim të bashkuar mund të jetë i papërshtatshëm. Përgjigjja duhet të ndjekë dizajnin dhe procedurën e deklaruar në material, jo një transformim automatik ose heqje automatike të rasteve.

## Udhëzuesi i formulave

Modeli njëfaktorial e shkruan secilin rezultat si mesatare të përgjithshme, efekt të grupit dhe gabim individual:

$$
Y_{ij}=\mu+\alpha_j+\varepsilon_{ij}
$$

Këtu $i$ identifikon një rast brenda grupit $j$, $\mu$ është referenca e përgjithshme, $\alpha_j$ është përbërësi i grupit dhe $\varepsilon_{ij}$ është ndryshueshmëria reziduale. Shuma e përgjithshme e katrorëve është:

$$
SS_{\text{total}}=\sum_{j=1}^{k}\sum_{i=1}^{n_j}(y_{ij}-\bar{y})^2
$$

Ndarja e saj e saktë është:

$$
SS_{\text{total}}=SS_{\text{factor}}+SS_{\text{error}}
$$

Dy përbërësit llogariten si:

$$
SS_{\text{factor}}=\sum_{j=1}^{k}n_j(\bar{y}_j-\bar{y})^2,\qquad
SS_{\text{error}}=\sum_{j=1}^{k}\sum_{i=1}^{n_j}(y_{ij}-\bar{y}_j)^2
$$

Mesataret e katrorëve pjesëtohen me shkallët përkatëse të lirisë dhe testi i përgjithshëm i krahason:

$$
F=\frac{MS_{\text{factor}}}{MS_{\text{error}}}
=\frac{SS_{\text{factor}}/(k-1)}{SS_{\text{error}}/(N-k)}
$$

Me saktësisht dy grupe të pavarura, ky test njëfaktorial me efekte fikse dhe testi t i dyanshëm për kampione të pavarura me variancë të bashkuar janë të barasvlershëm vetëm kur përdorin të njëjtin model me varianca të barabarta:

$$
F(1,N-2)=t(N-2)^2.
$$

Rezultati i përgjithshëm e bashkërendon krahasimin e grupeve, por nuk i identifikon mesataret që ndryshojnë. Një **kontrast** i përqendruar i bashkon mesataret e grupeve me pesha që japin shumën zero:

$$
D=\sum_{i=1}^{k}c_i\bar y_i,
\qquad
\sum_{i=1}^{k}c_i=0.
$$

Peshat pozitive dhe negative i vendosin nivelet në anë të kundërta të krahasimit të synuar. Për një dizajn të balancuar me $n$ raste në secilin nivel, llogaritja e kontrastit që përdoret në materialin e dhënë është

$$
SS_D=\frac{nD^2}{\sum_i c_i^2},
\qquad
F_D=\frac{SS_D}{MS_{\text{error}}},
$$

me 1 shkallë lirie në numërues dhe shkallët e lirisë të gabimit të ANOVA-s së përgjithshme në emërues. Një krahasim quhet i planifikuar vetëm kur peshat e tij janë zgjedhur para se të shqyrtohen rezultatet.

Numri i çifteve të ndryshme mes $k$ niveleve është

$$
m=\frac{k(k-1)}{2}.
$$

Për $m$ teste reciprokisht të pavarura, secili me probabilitet testor të gabimit të llojit I $\alpha_{\text{test}}$, norma e saktë e gabimit për familjen e testeve është

$$
\alpha_{\text{family}}
=1-(1-\alpha_{\text{test}})^m.
$$

Zgjidhja e kësaj marrëdhënieje për një nivel familjar të synuar jep pragun Sidak, ndërsa Bonferroni jep një kufi që nuk kërkon teste të pavarura:

$$
\alpha_{\text{test,Sidak}}
=1-(1-\alpha_{\text{family}})^{1/m},
\qquad
\alpha_{\text{test,Bonferroni}}
=\frac{\alpha_{\text{family}}}{m}.
$$

Barazia Sidak është e saktë vetëm për teste reciprokisht të pavarura. Krahasimet dyshe që kanë grupe të përbashkëta zakonisht janë të varura. Bonferroni e kontrollon gabimin familjar përmes një kufiri të sipërm pa këtë kërkesë për pavarësi, megjithëse mund të jetë konservativ.

Një ANOVA me dy faktorë fiksë e shkruan rezultatin e një qelize si mesatare të përgjithshme, dy përbërës të efekteve kryesore, ndërveprimin e tyre dhe gabimin individual:

$$
y_{ijm}
=\mu+\alpha_i+\beta_j+(\alpha\beta)_{ij}+\varepsilon_{ijm}.
$$

Një **mesatare qelize** i përket një kombinimi të saktë të niveleve të faktorëve. Një **mesatare margjinale** është mesatarja nëpër qelizat që i përkasin një niveli të një faktori. Efektet kryesore krahasojnë mesataret margjinale. Ndërveprimi pyet nëse efekti i një faktori ndryshon nëpër nivelet e faktorit tjetër, pra bën një pyetje për dallimin e dallimeve. Profilet joparalele të mesatareve tregojnë një model ndërveprimi; vijat nuk kanë pse të kryqëzohen.

Për një model njëfaktorial të balancuar me faktor të rastësishëm dhe $n$ vrojtime në secilin nivel të kampionuar, materiali i dhënë i vlerëson përbërësit e variancës mes niveleve dhe brenda niveleve me

$$
\widehat{\sigma}_A^2=\frac{MS_A-MS_{\text{error}}}{n},
\qquad
\widehat{\sigma}_{\text{error}}^2=MS_{\text{error}},
$$

dhe e përmbledh ngjashmërinë brenda niveleve me

$$
ICC=
\frac{\widehat{\sigma}_A^2}
{\widehat{\sigma}_A^2+\widehat{\sigma}_{\text{error}}^2}.
$$

Këto ekuacione i përkasin atij modeli njëfaktorial të balancuar me faktor të rastësishëm. Ato nuk përbëjnë një formulë universale të ICC-së për çdo dizajn të grupuar ose me matje të përsëritura.

Për një faktor të përsëritur, termi i personit e ruan lidhjen mes matjeve të të njëjtit person:

$$
y_{im}=\mu+\alpha_i+\pi_m+\varepsilon_{im},
$$

ku $\alpha_i$ është përbërësi fiks i rastit të matjes ose kushtit dhe $\pi_m$ është përbërësi i rastësishëm i personit. Ndarja përkatëse e ndryshueshmërisë është

$$
SS_{\text{total}}
=SS_{\text{condition}}+SS_{\text{person}}+SS_{\text{error}}.
$$

Për dy nivele të përsëritura $j$ dhe $k$, varianca e dallimit brenda personit është

$$
Var(Y_j-Y_k)
=Var(Y_j)+Var(Y_k)-2\,Cov(Y_j,Y_k).
$$

Sfericiteti kërkon që variancat në popullatë të të gjitha rezultateve të tilla të dallimeve dyshe të jenë të barabarta. Kur përdoret procedura e deklaruar Greenhouse-Geisser, vlerësimi i saj $\widehat\varepsilon\leq1$ i zvogëlon të dyja shkallët referuese të lirisë:

$$
df_{\text{condition}}^*=\widehat\varepsilon\,df_{\text{condition}},
\qquad
df_{\text{error}}^*=\widehat\varepsilon\,df_{\text{error}}.
$$

Statistika e vrojtuar $F$ nuk ndryshon. Ndryshojnë shkallët referuese të lirisë dhe vlera p ose vlera kritike që del prej tyre.

| Pyetja e dizajnit | Madhësia ose krahasimi | Kufizimi thelbësor |
|---|---|---|
| A janë të barabarta të gjitha mesataret fikse të grupeve në popullatë? | $F$ i përgjithshëm njëfaktorial | Hedhja poshtë nuk tregon se cilat mesatare ndryshojnë |
| Cilat mesatare të peshuara e të përcaktuara paraprakisht ndryshojnë? | Kontrasti i planifikuar $D$ dhe $F_D$ | Planifikimi duhet të bëhet para shqyrtimit të rezultateve |
| A varet efekti i një faktori nga një tjetër? | Ndërveprimi faktorial | Vetëm efektet kryesore mund ta fshehin modelin e qelizave |
| Sa ndryshueshmëri u përket niveleve të kampionuara? | Përbërësi i variancës së faktorit të rastësishëm dhe ICC | Formula varet nga dizajni i deklaruar me efekte të rastësishme |
| A ndryshojnë rastet e lidhura të matjes? | Efekti i kushtit në matjet e përsëritura | Varësia brenda personit dhe procedura për sfericitetin kanë rëndësi |

## Si lexohet figura shpjeguese

![Dy shtylla tregojnë shumën e përgjithshme të katrorëve pranë një shtylle po aq të lartë të ndarë në shumat e katrorëve të faktorit dhe gabimit, me etiketa numerike.](assets/topic-08-analysis-of-variance-summary-figure-sq.png){#fig-summary-t08 width=92%}

Shtylla e majtë përmban shumën e përgjithshme të katrorëve, 11,350.4. Ajo përfaqëson devijimet e ngritura në katror të secilit pikëzim të vrojtuar nga mesatarja e përgjithshme. Shtylla e djathtë ka të njëjtën lartësi të përgjithshme, por ndahet në pjesë. Segmenti i poshtëm blu është shuma e katrorëve të faktorit, 2,093.5, dhe përfaqëson ndarjen e mesatareve të grupeve. Segmenti i sipërm gri është shuma e katrorëve të gabimit, 9,256.9, dhe përfaqëson dallimet e rasteve rreth mesatareve të grupeve përkatëse.

Dy etiketat në të djathtë japin së bashku totalin në të majtë. Kjo barazi pamore është identiteti qendror i ANOVA-s. Përbërësi i gabimit është më i madh në këtë grup të dhënash, por testi $F$ nuk i krahason drejtpërdrejt lartësitë e papërpunuara të segmenteve. Secila shumë katrorësh pjesëtohet fillimisht me shkallët e saj të lirisë. Pastaj raporti i mesatareve të katrorëve vlerësohet kundrejt një shpërndarjeje $F$ nën modelin zero.

Shtyllat nuk tregojnë cila mesatare grupi është më e lartë, cilat çifte ndryshojnë, nëse supozimet për rezidualet janë të arsyeshme ose nëse dizajni mbështet shkakësinë. Këto pyetje kërkojnë grafikun e grupeve, tabelën përshkruese, diagnostikën dhe kontrastet e planifikuara. Vlerat e paraqitura vijnë nga të dhëna mësimore të simuluara dhe prandaj ilustrojnë llogaritjen në vend që të japin evidencë për një popullatë reale.

## Lista e kontrollit për interpretim

Identifiko faktorin, nivelet, rezultatin, njësinë e analizës dhe strukturën mes grupeve ose të përsëritur. Raporto numërimet e grupeve, mesataret, devijimet standarde dhe një paraqitje të qartë të grupeve. Trego hipotezën zero dhe alternativën e përgjithshme. Kontrollo pavarësinë nga dizajni dhe shqyrto ndryshueshmërinë e rezidualeve dhe vrojtimet e pazakonta. Raporto tabelën e plotë ANOVA me shumat e katrorëve, shkallët e lirisë, mesataret e katrorëve, $F$ dhe vlerën p, të ndjekura nga vlerësimet dhe pasiguria për krahasimet e planifikuara ose të përshtatura.

Pas një rezultati të përgjithshëm, përgjigju pyetjes përmbajtësore me krahasime të planifikuara ose të përshtatura për shumëfishësinë. Për një dizajn faktorial, interpreto ndërveprimet para se t'i mesatarizosh ato. Për matjet e përsëritura, ruaje varësinë brenda personit dhe trajto procedurën e dokumentuar për sfericitetin. Shmang pohimin se një rezultat jo i rëndësishëm vërteton mesatare të barabarta ose se një rezultat i rëndësishëm vërteton një dallim të rëndësishëm apo shkakor.

## Si lidhet kjo temë me të tjerat

ANOVA e përmbyll rrjedhën mësimore duke u kthyer te varianca, madhësia e paraqitur në statistikën përshkruese. Probabiliteti dhe inferenca shpjegojnë shpërndarjen referuese $F$ dhe procesin e vendimmarrjes. Kovarianca dhe korrelacioni tregojnë si ndajnë ndryshueshmëri lineare ndryshoret. Regresioni i thjeshtë e ndan ndryshueshmërinë e rezultatit në pjesë të përshtatur dhe reziduale. Korrelacioni i pjesshëm dhe regresioni i shumëfishtë shpjegojnë lidhjet e kushtëzuara pasi merret parasysh informacion tjetër.

Përkatësia në grup në ANOVA mund të kodohet si ndryshore treguese në një model regresioni. Shuma e katrorëve të faktorit është ndryshueshmëri që lidhet me modelin; shuma e katrorëve të gabimit është ndryshueshmëri reziduale; testi i përgjithshëm $F$ e krahason modelin e plotë të grupeve me një model vetëm me konstantë. Ndërveprimet faktoriale përputhen me ndërveprimet e regresionit dhe kontrastet e planifikuara janë krahasime lineare të synuara të mesatareve të përshtatura. Kjo kornizë e përbashkët kuptohet më mirë si **lidhja me modelin e përgjithshëm linear**: temat e mëvonshme janë pamje të ndryshme të mënyrës si informacioni i strukturuar parashikues përdoret për të shpjeguar ndryshueshmërinë e rezultatit, ndërsa pasiguria dhe ndryshueshmëria reziduale mbeten të dukshme.
