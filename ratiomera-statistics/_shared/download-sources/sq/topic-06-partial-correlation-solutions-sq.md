---
title: "Zgjidhjet e plota"
subtitle: "Korrelacioni i pjesshëm"
document-id: "topic-06-partial-correlation-solutions-sq"
topic-id: "topic-06-partial-correlation"
topic-number: "06"
topic-slug: "partial-correlation"
document-type: "solutions"
locale: "sq"
paired-document-id: "topic-06-partial-correlation-exercises-sq"
---

Këto zgjidhje të plota përdorin të njëjtat kode dhe të njëjtën renditje si Fleta e ushtrimeve. Vlerat ndërmjetëse ruhen deri te hapi i treguar i rrumbullakimit, prandaj aty ku shënohet pranohen dallime të vogla që vijnë nga rrumbullakimi më i hershëm. Të gjitha situatat, vlerat, të dhënat dhe rezultatet e programeve janë krijuar për mësim; nuk janë gjetje empirike.

# Pjesa I: Teoria

## A02: Krahasimi i korrelacionit bivariat me atë të pjesshëm

### T06-A02-V01: Ushtrimi, njohuritë paraprake dhe arsyetimi

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«njohuritë paraprake»** si me **«ushtrimi javor»**, ashtu edhe me **«rezultati i arsyetimit»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Njohuritë paraprake mund të lidhen pozitivisht si me ushtrimin javor, ashtu edhe me rezultatin e arsyetimit.

Prandaj, një pjesë e lidhjes bivariate mund të pasqyrojë lidhjen që të dyja ndryshoret kanë me njohuritë paraprake.

Koeficienti ndryshon nga 0.68 në 0.34.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e vogël.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«ushtrimi javor»** nga **«njohuritë paraprake»** dhe pastaj parashikohet ndryshorja **«rezultati i arsyetimit»** nga **«njohuritë paraprake»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«njohuritë paraprake»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V02: Koha e kërkimit, përvoja dhe saktësia

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«përvoja në arkiv»** si me **«koha e kërkimit»**, ashtu edhe me **«saktësia»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Përvoja në arkiv mund ta shkurtojë kohën e kërkimit dhe njëkohësisht ta rrisë saktësinë.

Kështu mund të krijohet një pjesë e lidhjes negative bivariate.

Koeficienti ndryshon nga -0.57 në -0.26.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e vogël.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«koha e kërkimit»** nga **«përvoja në arkiv»** dhe pastaj parashikohet ndryshorja **«saktësia»** nga **«përvoja në arkiv»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«përvoja në arkiv»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V03: Koha e leximit, ngarkesa dhe të kuptuarit

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«ngarkesa e kursit»** si me **«koha e leximit»**, ashtu edhe me **«të kuptuarit e tekstit»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Ngarkesa e lartë e kursit mund të shoqërohet me më shumë kohë leximi, por me të kuptuar më të ulët.

Kështu mund të fshihet një pjesë e lidhjes pozitive të përshtatur.

Koeficienti ndryshon nga 0.18 në 0.41.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e madhe.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«koha e leximit»** nga **«ngarkesa e kursit»** dhe pastaj parashikohet ndryshorja **«të kuptuarit e tekstit»** nga **«ngarkesa e kursit»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«ngarkesa e kursit»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V04: Njoftimet, ngarkesa e detyrave dhe përqendrimi

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«ngarkesa e detyrave»** si me **«numri i njoftimeve»**, ashtu edhe me **«përqendrimi»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Ngarkesa më e madhe e detyrave mund ta rrisë numrin e njoftimeve dhe ta ulë përqendrimin.

Kështu mund të krijohet një pjesë e lidhjes së papërshtatur negative.

Koeficienti ndryshon nga -0.49 në -0.20.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e vogël.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«numri i njoftimeve»** nga **«ngarkesa e detyrave»** dhe pastaj parashikohet ndryshorja **«përqendrimi»** nga **«ngarkesa e detyrave»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«ngarkesa e detyrave»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V05: Vizitat në muze, arsimimi dhe njohuritë

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«niveli i arsimimit»** si me **«vizitat në muze»**, ashtu edhe me **«njohuritë historike»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Niveli i arsimimit mund t'i nxisë vizitat në muze dhe t'i mbështesë njohuritë historike.

Prandaj, lidhja e papërshtatur mund të pasqyrojë pjesërisht të dyja këto lidhje.

Koeficienti ndryshon nga 0.54 në 0.29.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e vogël.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«vizitat në muze»** nga **«niveli i arsimimit»** dhe pastaj parashikohet ndryshorja **«njohuritë historike»** nga **«niveli i arsimimit»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«niveli i arsimimit»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V06: Njohja e rrugës, gjatësia dhe koha e udhëtimit

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«gjatësia e rrugës»** si me **«njohja e rrugës»**, ashtu edhe me **«koha e udhëtimit»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Rrugët më të gjata mund të njihen më mirë, por prapë të kërkojnë më shumë kohë udhëtimi.

Kështu mund të fshihet një pjesë e lidhjes negative mes njohjes së rrugës dhe kohës së udhëtimit.

Koeficienti ndryshon nga -0.21 në -0.48.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e madhe.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«njohja e rrugës»** nga **«gjatësia e rrugës»** dhe pastaj parashikohet ndryshorja **«koha e udhëtimit»** nga **«gjatësia e rrugës»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«gjatësia e rrugës»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V07: Pjesëmarrja, vetëbesimi fillestar dhe ai përfundimtar

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«vetëbesimi fillestar»** si me **«pjesëmarrja në seminar»**, ashtu edhe me **«vetëbesimi përfundimtar»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Ata që fillojnë me më shumë vetëbesim mund të marrin pjesë më shpesh në seminar dhe ta përfundojnë atë me më shumë vetëbesim.

Koeficienti ndryshon nga 0.61 në 0.25.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e vogël.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«pjesëmarrja në seminar»** nga **«vetëbesimi fillestar»** dhe pastaj parashikohet ndryshorja **«vetëbesimi përfundimtar»** nga **«vetëbesimi fillestar»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«vetëbesimi fillestar»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V08: Kalimi mes detyrave, ngarkesa dhe përfundimi

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«ngarkesa e punës»** si me **«kalimi mes detyrave»**, ashtu edhe me **«rezultati i përfundimit»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Ngarkesa e madhe e punës mund ta shtojë kalimin mes detyrave dhe ta vështirësojë përfundimin.

Kështu mund të krijohet një pjesë e lidhjes së papërshtatur negative.

Koeficienti ndryshon nga -0.52 në -0.28.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e vogël.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«kalimi mes detyrave»** nga **«ngarkesa e punës»** dhe pastaj parashikohet ndryshorja **«rezultati i përfundimit»** nga **«ngarkesa e punës»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«ngarkesa e punës»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V09: Postimet në diskutim, angazhimi dhe arsyetimi

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«angazhimi i përgjithshëm»** si me **«numri i postimeve në diskutim»**, ashtu edhe me **«rezultati i arsyetimit»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Angazhimi i përgjithshëm mund të sjellë si më shumë postime në diskutim, ashtu edhe rezultate më të larta arsyetimi.

Koeficienti ndryshon nga 0.59 në 0.19.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e vogël.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«numri i postimeve në diskutim»** nga **«angazhimi i përgjithshëm»** dhe pastaj parashikohet ndryshorja **«rezultati i arsyetimit»** nga **«angazhimi i përgjithshëm»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«angazhimi i përgjithshëm»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

### T06-A02-V10: Rregullsia, koha totale e studimit dhe mbajtja mend

**Përcakto çështjen**

Një diagram i besueshëm është **Z → X, Z → Y dhe X ↔ Y**.

Ai e lidh ndryshoren **«koha totale e studimit»** si me **«rregullsia e ushtrimit»**, ashtu edhe me **«mbajtja mend»**; lidhja e veçantë $X$-$Y$ mbetet një marrëdhënie më vete.

Një shpjegim i mundshëm është ky: Koha totale e studimit mund të lidhet pozitivisht me të dyja ndryshoret.

Kjo mund ta fshehë pjesërisht lidhjen e veçantë mes një orari të rregullt ushtrimi dhe mbajtjes mend.

Koeficienti ndryshon nga 0.33 në 0.47.

**Arsyeto hap pas hapi nga evidenca**

Vlera e tij absolute pas përshtatjes është më e madhe.

Gjatë rezidualizimit, fillimisht parashikohet ndryshorja **«rregullsia e ushtrimit»** nga **«koha totale e studimit»** dhe pastaj parashikohet ndryshorja **«mbajtja mend»** nga **«koha totale e studimit»**.

Korrelacioni i pjesshëm është korrelacioni mes shmangieve që mbeten në këto dy kolona rezidualesh.

Një vlerë absolute më e vogël sugjeron se ndryshorja e kontrollit përshkruan një pjesë të modelit bivariat.

Një vlerë absolute më e madhe sugjeron shtypje: përshtatja nxjerr në pah një lidhje që më parë ishte pjesërisht e fshehur.

**Jep përfundimin dhe kufijtë e tij**

Asnjëri rezultat nuk vendos rendin kohor, nuk përjashton ndryshore të pamatura, nuk ndreq gabimet e matjes dhe nuk zëvendëson kontrollin eksperimental.

Arsyetimi i **«koha totale e studimit»** si ndryshore kontrolli kërkon arsye nga fusha dhe plani i studimit, duke përfshirë një rend kohor të besueshëm dhe një rol të qartë për ndryshoren.

Vetëm koeficientët nuk e japin këtë arsyetim.

Përshtatja lineare heq vetëm pjesën lineare të përshtatur në modelin e deklaruar.

Struktura jolineare, problemet e matjes dhe ndryshoret përkatëse të pamatura mund të mbeten.

# Pjesa II: Praktika me kalkulator

## A01: Korrelacioni i pjesshëm me rezidualizim dhe me formulën e drejtpërdrejtë

### T06-A01-V01: Ushtrimi dhe arsyetimi pas përshtatjes për rezultatin paraprak

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=15.4000$, ndërsa $\sum e_X^2=28.0000$ dhe $\sum e_Y^2=12.1171$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=15.4000/\sqrt{28.0000(12.1171)}=0.8361$.

Formula e drejtpërdrejtë jep $[0.8761-(0.5200)(0.4800)]/\sqrt{[1-(0.5200)^2][1-(0.4800)^2]}=0.8361$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V02: Koha e kërkimit dhe saktësia pas përshtatjes për përvojën në arkiv

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=-12.1000$, ndërsa $\sum e_X^2=28.0000$ dhe $\sum e_Y^2=9.6200$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=-12.1000/\sqrt{28.0000(9.6200)}=-0.7373$.

Formula e drejtpërdrejtë jep $[-0.7997-(-0.4600)(0.5500)]/\sqrt{[1-(-0.4600)^2][1-(0.5500)^2]}=-0.7373$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V03: Koha e leximit dhe të kuptuarit pas përshtatjes për njohuritë paraprake

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=13.8000$, ndërsa $\sum e_X^2=42.0000$ dhe $\sum e_Y^2=8.6971$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=13.8000/\sqrt{42.0000(8.6971)}=0.7220$.

Formula e drejtpërdrejtë jep $[0.7834-(0.5800)(0.4400)]/\sqrt{[1-(0.5800)^2][1-(0.4400)^2]}=0.7220$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V04: Njoftimet dhe përqendrimi pas përshtatjes për ngarkesën e punës

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=-9.9000$, ndërsa $\sum e_X^2=28.0000$ dhe $\sum e_Y^2=7.4800$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=-9.9000/\sqrt{28.0000(7.4800)}=-0.6841$.

Formula e drejtpërdrejtë jep $[-0.7628-(-0.5100)(0.4900)]/\sqrt{[1-(-0.5100)^2][1-(0.4900)^2]}=-0.6841$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V05: Vizitat në muze dhe njohuritë pas përshtatjes për nivelin e arsimimit

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=9.2000$, ndërsa $\sum e_X^2=42.0000$ dhe $\sum e_Y^2=5.3743$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=9.2000/\sqrt{42.0000(5.3743)}=0.6124$.

Formula e drejtpërdrejtë jep $[0.7074-(0.4700)(0.5300)]/\sqrt{[1-(0.4700)^2][1-(0.5300)^2]}=0.6124$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V06: Njohja e rrugës dhe koha e udhëtimit pas përshtatjes për gjatësinë e rrugës

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=-11.6000$, ndërsa $\sum e_X^2=28.0000$ dhe $\sum e_Y^2=7.8400$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=-11.6000/\sqrt{28.0000(7.8400)}=-0.7829$.

Formula e drejtpërdrejtë jep $[-0.8235-(-0.4300)(0.6000)]/\sqrt{[1-(-0.4300)^2][1-(0.6000)^2]}=-0.7829$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V07: Pjesëmarrja në seminar dhe vetëbesimi pas përshtatjes për nivelin fillestar

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=15.0000$, ndërsa $\sum e_X^2=42.0000$ dhe $\sum e_Y^2=8.1771$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=15.0000/\sqrt{42.0000(8.1771)}=0.8094$.

Formula e drejtpërdrejtë jep $[0.8300-(0.6200)(0.4000)]/\sqrt{[1-(0.6200)^2][1-(0.4000)^2]}=0.8094$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V08: Kalimi mes detyrave dhe përfundimi pas përshtatjes për ngarkesën e detyrave

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=-9.5000$, ndërsa $\sum e_X^2=28.0000$ dhe $\sum e_Y^2=6.7800$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=-9.5000/\sqrt{28.0000(6.7800)}=-0.6895$.

Formula e drejtpërdrejtë jep $[-0.7617-(-0.5500)(0.4500)]/\sqrt{[1-(-0.5500)^2][1-(0.4500)^2]}=-0.6895$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V09: Postimet në diskutim dhe arsyetimi pas përshtatjes për angazhimin

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=13.2000$, ndërsa $\sum e_X^2=42.0000$ dhe $\sum e_Y^2=6.6743$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=13.2000/\sqrt{42.0000(6.6743)}=0.7884$.

Formula e drejtpërdrejtë jep $[0.8460-(0.5000)(0.5700)]/\sqrt{[1-(0.5000)^2][1-(0.5700)^2]}=0.7884$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.

### T06-A01-V10: Rregullsia e ushtrimit dhe mbajtja mend pas përshtatjes për kohën e studimit

**Përgatit llogaritjen**

Përveç rrumbullakimit të paraqitur, të dyja kolonat e rezidualeve kanë mesatare zero.

Shuma e prodhimeve të kryqëzuara është $\sum e_Xe_Y=9.4000$, ndërsa $\sum e_X^2=28.0000$ dhe $\sum e_Y^2=6.6686$.

**Zhvillo llogaritjen**

Prandaj $r(e_X,e_Y)=9.4000/\sqrt{28.0000(6.6686)}=0.6879$.

Formula e drejtpërdrejtë jep $[0.7637-(0.5600)(0.4600)]/\sqrt{[1-(0.5600)^2][1-(0.4600)^2]}=0.6879$.

**Interpreto dhe kontrollo rezultatin**

Mund të shfaqen dallime të vogla nëse korrelacionet e paraqitura rrumbullakosen para se të zëvendësohen në formulë. Çdo rezidual është diferenca mes vlerës së vrojtuar dhe vlerës së përshtatur nga regresioni linear mbi $Z$ për të njëjtën ndryshore.

Korrelacioni mes dy kolonave të rezidualeve përshkruan si lëvizin së bashku këto shmangie të mbetura.

Ai mbetet një lidhje e përshtatur dhe nuk është vetvetiu efekt shkakor.
