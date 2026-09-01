---
title: "Zgjidhjet e plota"
subtitle: "Probabiliteti"
document-id: "topic-02-probability-solutions-sq"
topic-id: "topic-02-probability"
topic-number: "02"
topic-slug: "probability"
document-type: "solutions"
locale: "sq"
paired-document-id: "topic-02-probability-exercises-sq"
---

Këto zgjidhje të plota përdorin të njëjtat kode dhe të njëjtën renditje si Fleta e ushtrimeve. Vlerat ndërmjetëse ruhen deri te hapi i treguar i rrumbullakimit, prandaj aty ku shënohet pranohen dallime të vogla që vijnë nga rrumbullakimi më i hershëm. Të gjitha situatat, vlerat, të dhënat dhe rezultatet e programeve janë krijuar për mësim; nuk janë gjetje empirike.

# Pjesa I: Teoria

## A08: Funksionet e masës së probabilitetit dhe dendësitë

### T02-A08-V01: Nga numri i ekspozitave të vizituara te koha e kaluar në muze

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i ekspozitave të vizituara** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **koha e kaluar në muze** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V02: Nga numri i mesazheve të marra te vonesa deri te mesazhi tjetër

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i mesazheve të marra** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **vonesa deri te mesazhi tjetër** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V03: Nga numri i gabimeve të transkriptimit te kohëzgjatja e një segmenti audio

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i gabimeve të transkriptimit** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **kohëzgjatja e një segmenti audio** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V04: Nga numri i librave të huazuar te masa e një pakoje të kthyer

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i librave të huazuar** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **masa e një pakoje të kthyer** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V05: Nga numri i kujtesave të anketës te koha e plotësimit nga një person që përgjigjet

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i kujtesave të anketës** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **koha e plotësimit nga një person që përgjigjet** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V06: Nga numri i ndryshimeve të rrugës te largësia e përshkuar

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i ndryshimeve të rrugës** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **largësia e përshkuar** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V07: Nga numri i fushave që mungojnë te mosha e një pjesëmarrësi e matur me saktësi

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i fushave që mungojnë** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **mosha e një pjesëmarrësi e matur me saktësi** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V08: Nga numri i seancave të punëtorisë te niveli i zërit në dhomë

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i seancave të punëtorisë** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **niveli i zërit në dhomë** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V09: Nga numri i fotografive të konservuara te temperatura e arkivit

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i fotografive të konservuara** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **temperatura e arkivit** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

### T02-A08-V10: Nga numri i kontrolleve të suksesshme te koha e saktë e reagimit në një detyrë

**Përcakto çështjen, pjesa (a)**

Ndryshorja $X$ = **numri i kontrolleve të suksesshme** ka bashkësi mbështetëse të numërueshme dhe PMF-ja mund t'i caktojë masën $P(X=x)$ secilit numërim të mundshëm. Ndryshorja $Y$ = **koha e saktë e reagimit në një detyrë** matet në një shkallë të vazhdueshme, prandaj një model ideal i vazhdueshëm e paraqet atë me dendësinë $f_Y(y)$.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

$P(X=x)$ mund të jetë pozitiv për një numërim të vetëm, ndërsa $P(Y=y)=0$ në çdo pikë të saktë edhe kur vlerat pranë saj janë të besueshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Për $X$, probabiliteti i intervalit është shuma e masave të përfshira. Për $Y$, ai është sipërfaqe nën dendësi, për shembull $P(a<Y\leq b)=\int_a^b f_Y(y)\,dy$.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Në të dyja rastet, CDF-ja regjistron probabilitetin e grumbulluar: $F_X(x)=P(X\leq x)$ kërcen në numërimet e mbështetura, ndërsa $F_Y(y)=P(Y\leq y)$ e grumbullon vazhdimisht sipërfaqen nën dendësi.

## A14: Popullata, kampioni dhe anshmëria e përzgjedhjes

### T02-A14-V01: Anketa me kod QR për përdorimin e parkut

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjithë banorët e qytetit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: personat që hyjnë në parkun më të madh qendror gjatë periudhës së afishimit, e vërejnë kodin dhe mund ta skanojnë. Kampioni i arritur: 640 vizitorët e parkut që skanuan kodin dhe e dorëzuan anketën. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: përpjesëtimi i të gjithë banorëve të qytetit që përdorin cilindo park çdo javë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: përpjesëtimi i 640 të anketuarve që raportojnë përdorim javor të parkut. Kërcënimet kryesore lidhen me këtë dizajn: Përdoruesit e shpeshtë të parqeve kanë më shumë gjasa të hyjnë në këtë park. Personat që vërejnë dhe skanojnë një kod mund të dallojnë nga të tjerët për nga interesi ose qasja digjitale. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të merret një kampion probabilitar nga një kornizë e banorëve të qytetit dhe të kontaktohen përsëri të përzgjedhurit që nuk përgjigjen përmes më shumë se një mënyre kontakti.

### T02-A14-V02: Anketa e udhëtimit mes mbajtësve të lejeve të parkimit

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjithë studentët e regjistruar.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: lista e universitetit me studentët që kanë leje parkimi. Kampioni i arritur: 820 mbajtësit e lejeve të parkimit që u përgjigjën. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: koha mesatare e udhëtimit për të gjithë studentët e regjistruar.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: koha mesatare e udhëtimit për 820 personat që u përgjigjën. Kërcënimet kryesore lidhen me këtë dizajn: Korniza lë jashtë studentët që ecin, përdorin biçikletën ose transportin publik, si dhe ata pa leje parkimi. Gatishmëria për t'u përgjigjur mund të varet edhe nga vështirësia e udhëtimit. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të merret kampion nga regjistri i plotë i studentëve, të shtresëzohet sipas mënyrës së mundshme të udhëtimit kur kjo ndihmon dhe të kontaktohen përsëri studentët e përzgjedhur.

### T02-A14-V03: Kënaqësia pas një ekspozite me të gjitha biletat e shitura

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjithë vizitorët e muzeut gjatë sezonit të synuar.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: vizitorët që dolën nga ekspozita e mbrëmjes dhe të cilëve iu ofrua anketa në dalje. Kampioni i arritur: 510 të pranishmit që e plotësuan atë anketë në dalje. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: rezultati mesatar i kënaqësisë mes të gjithë vizitorëve në sezonin e synuar.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: rezultati mesatar i kënaqësisë mes 510 personave që u përgjigjën. Kërcënimet kryesore lidhen me këtë dizajn: Një mbrëmje jashtëzakonisht e pëlqyer mund të mos përfaqësojë data ose ekspozita të tjera. Plotësimi i anketës mund të varet edhe nga një përvojë veçanërisht e mirë ose e keqe. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të përzgjidhen vizita në ekspozita, ditë dhe orare të ndryshme, pastaj të ftohet një kampion probabilitar i vizitorëve në dalje dhe të dokumentohet mospërgjigjja.

### T02-A14-V04: Anketa e qasjes digjitale brenda një aplikacioni

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjithë përdoruesit e bibliotekës.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: përdoruesit e bibliotekës që përdorin aplikacionin dhe mund ta shihnin njoftimin e anketës. Kampioni i arritur: 430 përdoruesit e aplikacionit që dhanë përgjigje vullnetarisht. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: përpjesëtimi i të gjithë përdoruesve të bibliotekës që kanë nevojë për qasje më të mirë digjitale.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: përpjesëtimi i 430 të anketuarve që raportojnë këtë nevojë. Kërcënimet kryesore lidhen me këtë dizajn: Përdoruesit pa pajisje të përshtatshme ose pa qasje në aplikacion nuk mund të hyjnë në kornizë. Personat që i përgjigjen vullnetarisht një ankete për qasjen mund të kenë nevoja ose angazhim jashtëzakonisht të madh. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të merret kampion nga regjistri i plotë i përdoruesve dhe të ofrohen mënyra të qasshme përgjigjeje në internet, me telefon, në letër dhe ballë për ballë.

### T02-A14-V05: Orët vullnetare nga listat e organizatave të mëdha bamirëse

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjithë vullnetarët në rajon.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: listat e anëtarëve të dhëna nga organizata të mëdha bamirëse të regjistruara. Kampioni i arritur: 760 anëtarët e listuar, regjistrimet e të cilëve u përdorën. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: orët mesatare javore të punës vullnetare mes të gjithë vullnetarëve në rajon.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: orët mesatare javore të regjistruara për këta 760 anëtarë të listuar. Kërcënimet kryesore lidhen me këtë dizajn: Listat lënë jashtë vullnetarët joformalë dhe anëtarët e grupeve të vogla ose të paregjistruara. Regjistrimet e anëtarësisë formale mund të mbipërfaqësojnë vullnetarët e rregullt dhe afatgjatë. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të ndërtohet një kornizë më e gjerë nga lloje të ndryshme organizatash dhe burime komunitare, pastaj të bëhet përzgjedhje probabilitare brenda shtresave të përcaktuara të vullnetarëve.

### T02-A14-V06: Anketa e ngarkesës së kursit pas notave

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjithë studentët e regjistruar në kurs.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: studentët e regjistruar, llogaritë e të cilëve mbetën aktive në platformë pas publikimit të notave. Kampioni i arritur: 390 studentët ende aktivë që dhanë të dhëna për ngarkesën. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: ngarkesa mesatare e perceptuar mes të gjithë studentëve të regjistruar.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: ngarkesa mesatare e raportuar nga 390 personat që u përgjigjën. Kërcënimet kryesore lidhen me këtë dizajn: Studentët që u shkëputën, u çregjistruan ose ndaluan së përdoruri platformën mungojnë. Gatishmëria për t'u përgjigjur pas vlerësimit mund të lidhet me ngarkesën ose rezultatet e kursit. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të përzgjidhet nga lista fillestare e kursit, studentët të kontaktohen pavarësisht aktivitetit të mëvonshëm në platformë dhe të ndiqen rastet e mospërgjigjes.

### T02-A14-V07: Vonesat e transportit nga komentet me hashtag

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjitha udhëtimet e pasagjerëve gjatë periudhës së synuar.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: komentet publike në media sociale që mund të merren dhe që përdorin hashtagun e fushatës. Kampioni i arritur: 1 240 komentet e marra me hashtag. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: përpjesëtimi i të gjitha udhëtimeve të përjetuara si të vonuara.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: përpjesëtimi i 1 240 komenteve që përshkruajnë një vonesë. Kërcënimet kryesore lidhen me këtë dizajn: Personat me përvoja skajore kanë më shumë gjasa të postojnë, një person mund të japë disa komente, dhe njësitë e vëzhguara janë komentet në vend të udhëtimeve. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të përzgjidhen udhëtime nga regjistrimet operative dhe të merret një përgjigje për secilin udhëtim të zgjedhur, duke e mbajtur udhëtimin si njësi analize.

### T02-A14-V08: Formularët e interesit të lagjes pas shfaqjeve

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjithë banorët e lagjes përreth.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: mbajtësit e biletave që dolën nga shfaqjet e zgjedhura dhe të cilëve iu ofrua një formular. Kampioni i arritur: 570 mbajtësit e biletave që qëndruan dhe plotësuan formularin. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: përpjesëtimi i banorëve të lagjes që interesohen për programe të ardhshme.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: përpjesëtimi i 570 të anketuarve që shprehën interes. Kërcënimet kryesore lidhen me këtë dizajn: Banorët që nuk marrin tashmë pjesë në aktivitete me bileta mungojnë në kornizë. Qëndrimi për të plotësuar formularin mund të lidhet me entuziazmin për qendrën. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të përdoret një kornizë adresash të lagjes, banorët të përzgjidhen pavarësisht pjesëmarrjes dhe të ofrohen disa mënyra përgjigjeje.

### T02-A14-V09: Regjistrimet e gjumit nga përdoruesit vjetorë të pajisjeve që vishen

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjithë përdoruesit në popullatën e synuar të pajisjes gjatë vitit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: përdoruesit e pajisjes me llogari të aktivizuara në fillim të periudhës së vëzhgimit. Kampioni i arritur: 680 përdoruesit që qëndruan një vit të plotë me regjistrime të plota gjumi. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: kohëzgjatja mesatare e gjumit gjatë natës në popullatë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: kohëzgjatja mesatare e regjistruar e gjumit te përdoruesit që qëndruan. Kërcënimet kryesore lidhen me këtë dizajn: Qëndrimi për një vit lë jashtë përdoruesit e ndërprerë ose ata që hoqën dorë. Qëndrimi ose përdorimi i plotë i pajisjes mund të varet nga zakonet e gjumit, shëndeti ose kënaqësia me pajisjen. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: përdoruesit të përzgjidhen në regjistrim, të ruhen të dhënat e pjesshme sipas një plani të paracaktuar për të dhënat që mungojnë dhe të krahasohen pjesëmarrësit e mbetur me ata të humbur.

### T02-A14-V10: Komentet për arkivin të shfaqura vetëm pas shkarkimit

**Përcakto çështjen, pjesa (a)**

Popullata e synuar: të gjitha përpjekjet e kërkimit në arkiv gjatë periudhës së synuar.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Korniza operative e kampionimit: përpjekjet e kërkimit që arritën të paktën një shkarkim dhe prandaj morën kërkesën për koment. Kampioni i arritur: 450 formularët e dorëzuar të komenteve nga kjo kornizë e kufizuar. Kjo ndarje ka rëndësi: korniza përshkruan kush ose çfarë kishte rrugë për t'u përzgjedhur, ndërsa kampioni përmban njësitë që u vëzhguan vërtet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Parametri përkatës i popullatës: përpjesëtimi i të gjitha kërkimeve që përfundojnë me gjetje të suksesshme.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Statistika e kampionit: përpjesëtimi i 450 formularëve, dërguesit e të cilëve raportojnë sukses. Kërcënimet kryesore lidhen me këtë dizajn: Kërkesa shfaqet vetëm pas një rezultati të suksesshëm, kështu që kërkimet e dështuara nuk kanë rrugë për të hyrë në kornizë. Mes personave që shkarkojnë mund të ketë edhe vetëpërzgjedhje. Një kampion më i madh nga i njëjti mekanizëm do ta zvogëlonte ndryshueshmërinë e rastësishme të kampionimit rreth vlerës së kornizës së këtij mekanizmi, por nuk do t'i rregullonte mekanizmat sistematikë të mbulimit ose përzgjedhjes. Një qasje më e mbrojtshme është: të përzgjidhen kërkimet në fillim, të kërkohet koment pavarësisht nëse ndodh shkarkimi dhe çdo kërkimi të përzgjedhur t'i lidhet një mundësi e vetme përgjigjeje.

## A15: Gabimi i mbulimit dhe popullata pas një përqindjeje

### T02-A15-V01: Nivelet e arsimit mes përkrahësve të futbollit

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë personat që përkrahin Northport FC.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë anëtarët e platformës që e shënojnë Northport FC në një profil të dukshëm dhe japin të dhëna për arsimin.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Përkrahësit që nuk e përdorin platformën profesionale, nuk shënojnë klub ose nuk japin arsimimin nuk mund të hyjnë në përqindje. Anëtarësia në platformë lidhet edhe me arsimin dhe punësimin. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes profileve të analizuara që shënonin Northport FC dhe përmbanin të dhëna për arsimin, 64% raportonin diplomë universitare.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të përcaktohet fillimisht statusi i përkrahësit, të merret kampion përmes një kornize që nuk lidhet me anëtarësinë në platformën profesionale dhe të kontaktohen përsëri të përzgjedhurit që nuk përgjigjen. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V02: Zakonet e leximit nga një komunitet lexuesish elektronikë

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë të rriturit në vend.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë anëtarët e forumit që e panë ftesën dhe zgjodhën të përgjigjen.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Të rriturit që nuk përdorin lexues elektronik ose forum mungojnë. Lexuesit shumë aktivë kanë veçanërisht shumë gjasa të anëtarësohen dhe të përgjigjen. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes anëtarëve të këtij forumi që u përgjigjën, 71% raportuan se përfundojnë të paktën dy libra në muaj.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të merret një kampion probabilitar nga një kornizë popullate e të rriturve dhe të ofrohen disa mënyra përgjigjeje. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V03: Shpeshtësia e çiklizmit nga një aplikacion për planifikimin e rrugës

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë banorët e qytetit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë përdoruesit aktivë të aplikacionit që lejojnë regjistrimin e udhëtimeve.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Banorët që nuk përdorin biçikletë ose aplikacion, si dhe ata që e çaktivizojnë regjistrimin, mungojnë. Çiklistët e shpeshtë kanë më shumë gjasa të mbeten përdorues aktivë. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes përdoruesve aktivë me regjistrimin e udhëtimeve të aktivizuar, 58% regjistruan të paktën tri udhëtime në javë.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të merret kampion nga regjistri i qytetit dhe të matet shpeshtësia e çiklizmit pavarësisht përdorimit të aplikacionit. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V04: Interesi për muzeun nga abonentët e buletinit

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë banorët e rajonit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë abonentët e buletinit që e hapën mesazhin dhe e plotësuan anketën.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Personat që tashmë interesohen për muzeun kanë më shumë gjasa të abonohen, ta hapin mesazhin dhe t'i përgjigjen anketës. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes abonentëve të buletinit që u përgjigjën, 82% thanë se planifikonin ta vizitonin ekspozitën.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të merret kampion i banorëve të rajonit pavarësisht abonimit në buletin dhe të regjistrohet mospërgjigjja. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V05: Parapëlqimi për punën nga larg në një platformë bashkëpunimi

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë të rriturit e punësuar në rajonin e synuar.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë mbajtësit e llogarive në platformë që morën dhe plotësuan pyetësorin.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Platforma mbipërfaqëson personat me punë që mund të bëhen nga larg. Vullnetarët me parapëlqime të forta mund të përgjigjen më shpesh. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes mbajtësve të llogarive në këtë platformë që u përgjigjën, 76% parapëlqenin punën nga larg në shumicën e ditëve të javës.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të merret kampion i të rriturve të punësuar në profesione dhe forma pune të ndryshme nga një kornizë e përshtatshme e fuqisë punëtore. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V06: Përdorimi i gjuhëve nga fushat e profileve publike

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë banorët e vendit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë anëtarët e platformës me profile publike që zgjodhën të listojnë të paktën një gjuhë.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Qasja në platformë dhe zgjedhjet për profilin publik ndryshojnë mes banorëve. Listimi i një gjuhe nuk vërteton përdorim të përditshëm. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Nga profilet publike me fushë gjuhësh në të dhënat e analizuara, 43% listonin të paktën tri gjuhë.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të merret kampion nga një kornizë e popullatës dhe të bëhet një pyetje e përcaktuar qartë për përdorimin e përditshëm të gjuhëve. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V07: Mirëqenia e studentëve nga një aplikacion planifikimi

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë studentët e regjistruar në universitetet me interes.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë përdoruesit e aplikacionit që e vunë re dhe iu përgjigjën pyetjes për mirëqenien.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Studentët që përdorin një aplikacion planifikimi mund të dallojnë në ngarkesë ose organizim. Gatishmëria për t'u përgjigjur mund të lidhet me stresin aktual. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes përdoruesve të aplikacionit që u përgjigjën, 61% raportuan stres të lartë akademik.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të merret kampion nga listat e plota të regjistrimit dhe studentët e përzgjedhur të kontaktohen në më shumë se një mënyrë. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V08: Pjesëmarrja në koncerte nga profilet e llogarive të biletave

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë banorët në popullatën e synuar.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë llogaritë e regjistruara me aktivitet të dukshëm në ndjekjen e faqeve.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Banorët pa llogari mungojnë, një person mund të ketë disa llogari, dhe ndjekja e një faqeje nuk është i njëjti rezultat si pjesëmarrja në koncert. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes llogarive të vëzhguara, 67% ndoqën të paktën një faqe koncerti vitin e kaluar.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të përzgjidhen persona në vend të llogarive dhe të pyetet ose verifikohet një rezultat pjesëmarrjeje i përcaktuar qartë. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V09: Kënaqësia me transportin publik nga një kampion biletash celulare

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë pasagjerët që përdorin sistemin e transportit gjatë periudhës së synuar.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë pasagjerët që blenë biletë celulare dhe morën pyetjen në aplikacion.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Përdoruesit e parave të gatshme, biletave në letër, aboneve dhe shërbimeve të qasshmërisë nuk mund të hyjnë në kornizë. Kënaqësia mund të ndikojë edhe në përgjigjen ndaj pyetjes. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes përdoruesve të biletave celulare që iu përgjigjën pyetjes në aplikacion, 74% raportuan kënaqësi.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të përzgjidhen udhëtime në lloje biletash, rrugë dhe orare të ndryshme, pastaj pasagjerët e zgjedhur të ftohen përmes mënyrave të qasshme të përgjigjes. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

### T02-A15-V10: Pjesëmarrja vullnetare nga faqet e organizatave

**Përcakto çështjen, pjesa (a)**

Pretendimi i gjerë emërton të gjithë vullnetarët formalë dhe joformalë në rajon.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Njësitë me rrugë për të hyrë në llogaritje janë vullnetarët e listuar publikisht nga organizatat e mëdha bamirëse të përfshira në kërkimin në internet.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Gabimi i mbulimit lind për këtë arsye: Mungojnë vullnetarët joformalë, organizatat e vogla dhe vullnetarët pa profile publike. Personat që kontribuojnë rregullisht kanë më shumë gjasa të paraqiten në faqe. Përqindja mund të llogaritet saktë për regjistrimet e vëzhguara dhe prapëseprapë të mos e vlerësojë përqindjen në popullatën më të gjerë.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Një pohim i sinqertë përshkrues është: «Mes vullnetarëve të listuar publikisht nga organizatat e mëdha bamirëse të përfshira, 69% përshkruheshin si kontribues të përmuajshëm.» Një studim më i mbrojtshëm do të ndiqte këtë plan: të ndërtohet një kornizë më e gjerë me organizata të madhësive të ndryshme dhe punë joformale në komunitet, pastaj të merret kampion vullnetarësh brenda saj. Rritja e numrit të regjistrimeve nga e njëjta rrugë e kufizuar do ta bënte më të saktë përqindjen për atë kornizë, por nuk do të shtonte llojet e njerëzve që nuk hynë kurrë në të.

## A16: Anshmëria e mbijetesës dhe rezultatet që mungojnë

### T02-A16-V01: Modelet e dëmtimit te dronët e kthyer të dërgesave

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban dronët që u dëmtuan, por megjithatë u kthyen dhe mund të shqyrtoheshin.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë dronët që nuk u kthyen, përfshirë ata që mund të kenë pësuar dëmtim kritik të njësisë së navigimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Dëmtimi i njësisë së navigimit mund ta pengojë kthimin. Prandaj numri i ulët i shenjave të vëzhguara aty mund të tregojë përzgjedhje të fortë, jo siguri. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: të shqyrtohen regjistrimet e fluturimeve të dështuara dhe dronët e pakthyer që janë gjetur para se të vendoset se ku ka më shumë vlerë përforcimi. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V02: Zakonet e studimit mes personave që përfunduan kursin

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban personat e regjistruar që qëndruan deri në përfundim dhe pranuan të intervistoheshin.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë studentët që u çregjistruan, ndaluan së hyrë në platformë ose nuk pranuan intervistën.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Zakonet e planifikimit mund të lidhen me këmbënguljen. Përzgjedhja sipas përfundimit mund ta bëjë zakonin e vëzhguar të duket jashtëzakonisht i shpeshtë. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: të ndiqet grupi fillestar i të regjistruarve dhe të mblidhen të dhëna të krahasueshme nga ata që e përfunduan dhe ata që nuk e përfunduan kursin. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V03: Besueshmëria mes pajisjeve ende në përdorim

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban sensorët që mbijetuan në përdorim për dy vjet dhe ishin ende të disponueshëm për shqyrtim.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë sensorët e hequr, hedhur ose zëvendësuar më herët, ndoshta sepse korrozioni shkaktoi defekt.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Rezultati me interes mund të përcaktojë nëse sensori mbetet i vëzhgueshëm, duke lënë në grupin e shqyrtuar njësitë më pak të dëmtuara. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: të përdoren regjistrimet e mirëmbajtjes dhe zëvendësimit për të gjithë grupin fillestar të sensorëve, përfshirë njësitë që dështuan. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V04: Kënaqësia mes vizitorëve që kthehen në muze

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban vizitorët që ishin mjaft të kënaqur ose të motivuar për t'u kthyer të paktën katër herë dhe për të ardhur përsëri.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë vizitorët që erdhën vetëm një herë dhe personat që vendosën të mos kthehen.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Kënaqësia e mëparshme mund të ndikojë në kthim. Përzgjedhja në një vizitë të mëvonshme filtron shumë përvoja më pak të kënaqshme. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: të merret kampion në vizitën e parë dhe këta vizitorë të ndiqen pavarësisht nëse kthehen. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V05: Raportet e ngarkesës nga punonjësit që qëndruan

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban punonjësit nga grupi i të punësuarve që qëndruan pesë vjet dhe u përgjigjën.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë punonjësit që dhanë dorëheqje, u larguan nga puna ose nuk mund të kontaktoheshin pasi u larguan.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Ngarkesa e vitit të parë mund të ndikojë në largim. Punonjësit që qëndruan mund të raportojnë përvoja sistematikisht të ndryshme. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: të mblidhen të dhëna për ngarkesën në mënyrë prospektive nga i gjithë grupi fillestar dhe të ruhen të dhënat e largimit. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V06: Shërimi mes pacientëve që erdhën në kontrollin përfundimtar

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban pacientët e trajtuar që erdhën në kontrollin përfundimtar dhe dhanë rezultat.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë pacientët që munguan sepse gjendja u përkeqësua, u shëruan diku tjetër, u zhvendosën ose u shkëputën.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Pjesëmarrja në kontroll mund të varet nga shërimi. Prandaj përqindja e vëzhguar nuk ka pse t'i përfaqësojë të gjithë pacientët e trajtuar. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: të gjurmohet i gjithë grupi i trajtuar dhe të përdoren disa mënyra të përshtatshme për të marrë rezultatet e personave që mungojnë në kontroll. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V07: Qëndrueshmëria mes skedarëve të mbijetuar të arkivit

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban skedarët që mbijetuan, mbetën të gjetshëm dhe mund të hapeshin ende.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë skedarët e humbur, dëmtuar ose të pagjetshëm, metadatat e të cilëve mund të kenë ndikuar në zhdukjen e tyre.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Kushti që një skedar duhet të gjendet dhe të hapet mund të heqë pikërisht dështimet që nevojiten për të vlerësuar ruajtjen. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: të auditohet inventari fillestar dhe skedarët që mungojnë ose janë dëmtuar të numërohen si rezultate në vend që të përjashtohen. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V08: Siguria mes finalistëve të një gare

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban garuesit që kaluan çdo raund të mëparshëm dhe arritën në finale.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë garuesit që u eliminuan në raunde të mëparshme ose u tërhoqën.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Siguria fillestare mund të ndikojë në paraqitje dhe tërheqje. Finalistët përbëjnë kështu një nëngrup të përzgjedhur. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: të matet siguria e të gjithë garuesve para raundit të parë dhe të ruhet statusi i tyre i mëvonshëm në garë. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V09: Kohët e udhëtimit nga rrugët e përfunduara në aplikacion

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban udhëtimet e regjistruara që mbetën aktive derisa aplikacioni regjistroi përfundimin.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë udhëtimet e ndërprera, braktisura ose jashtëzakonisht të vonuara, seancat e të cilave përfunduan herët.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Udhëtimet e gjata ose problematike mund të mbyllen më shpesh para kohe, duke i bërë rrugët e përfunduara të duken më të shpejta. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: çdo udhëtim i nisur të përcaktohet si pjesë e grupit dhe të shqyrtohen regjistrimet e paplota në vend që të hiqen pa shpjegim. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

### T02-A16-V10: Përparimi në lexim mes abonentëve aktivë

**Përcakto çështjen, pjesa (a)**

Grupi i vëzhguar përmban abonentët që mbetën aktivë gjatë gjithë vitit dhe kishin të dhëna të lexueshme për përparimin.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Nga ky grup mungojnë personat që e anuluan abonimin ose llogaritë e të cilëve u bënë joaktive gjatë vitit.

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Procesi i përzgjedhjes lidhet me rezultatin: Angazhimi në lexim mund të ndikojë në anulim. Abonentët aktivë mund të shfaqin përparim jashtëzakonisht të lartë. Kjo është anshmëri e mbijetesës. Një rast duhet të mbetet i disponueshëm që të vëzhgohet, edhe pse pikërisht mungesa e tij nga të dhënat mund të mbartë informacion të rëndësishëm.

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Vëzhgimi vetëm i rasteve të dukshme e kushtëzon analizën mbi mbijetesën, përfundimin, kthimin ose qëndrimin. Kjo mund t'i fshehë dështimet dhe ta përmbysë mësimin praktik. Hapi tjetër është: grupi fillestar i abonentëve të mbahet në analizë dhe përparimi të regjistrohet deri në anulim ose të ndiqen ish-abonentët. Qëllimi nuk është të hamendësohen rezultatet që mungojnë, por të ridizajnohet mbledhja që rastet që vazhdojnë dhe ato që nuk vazhdojnë të japin prova.

# Pjesa II: Praktika me kalkulator

## A01: Probabiliteti i kushtëzuar në një varg etapash

### T02-A01-V01: Përfundimi i një kërkimi në arkiv

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.62\times 0.81=0.5022$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.62\times 0.81\times 0.74=0.3716$. Pra modeli thotë se përpjesëtimi 0.3716 e përfundon gjithë vargun deri te etapa «të përcaktosh letrën përkatëse».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.74=0.26$. Prandaj $P(A\cap B\cap C')=0.62\times 0.81\times 0.26=0.1306$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V02: Kalimi i një vlerësimi gjuhësor me tri etapa

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.68\times 0.77=0.5236$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.68\times 0.77\times 0.84=0.4398$. Pra modeli thotë se përpjesëtimi 0.4398 e përfundon gjithë vargun deri te etapa «të kalosh intervistën».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.84=0.16$. Prandaj $P(A\cap B\cap C')=0.68\times 0.77\times 0.16=0.0838$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V03: Përfundimi i një regjistrimi digjital

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.73\times 0.86=0.6278$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.73\times 0.86\times 0.79=0.4960$. Pra modeli thotë se përpjesëtimi 0.4960 e përfundon gjithë vargun deri te etapa «të dërgosh formularin e pëlqimit».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.79=0.21$. Prandaj $P(A\cap B\cap C')=0.73\times 0.86\times 0.21=0.1318$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V04: Përfundimi i një vargu hapash në terren

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.57\times 0.83=0.4731$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.57\times 0.83\times 0.91=0.4305$. Pra modeli thotë se përpjesëtimi 0.4305 e përfundon gjithë vargun deri te etapa «ta ngarkosh regjistrimin saktë».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.91=0.09$. Prandaj $P(A\cap B\cap C')=0.57\times 0.83\times 0.09=0.0426$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V05: Përfundimi i një kërkimi bibliotekar

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.66\times 0.72=0.4752$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.66\times 0.72\times 0.88=0.4182$. Pra modeli thotë se përpjesëtimi 0.4182 e përfundon gjithë vargun deri te etapa «t'i vlerësosh saktë metodat e tij».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.88=0.12$. Prandaj $P(A\cap B\cap C')=0.66\times 0.72\times 0.12=0.0570$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V06: Kalimi i etapave të një audicioni muzikor

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.71\times 0.69=0.4899$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.71\times 0.69\times 0.82=0.4017$. Pra modeli thotë se përpjesëtimi 0.4017 e përfundon gjithë vargun deri te etapa «të kalosh provën e leximit të notave në çast».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.82=0.18$. Prandaj $P(A\cap B\cap C')=0.71\times 0.69\times 0.18=0.0882$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V07: Përfundimi i një protokolli laboratorik

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.64\times 0.87=0.5568$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.64\times 0.87\times 0.76=0.4232$. Pra modeli thotë se përpjesëtimi 0.4232 e përfundon gjithë vargun deri te etapa «ta etiketosh rezultatin saktë».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.76=0.24$. Prandaj $P(A\cap B\cap C')=0.64\times 0.87\times 0.24=0.1336$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V08: Përfundimi i një kursi në internet për sigurinë

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.78\times 0.75=0.5850$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.78\times 0.75\times 0.89=0.5206$. Pra modeli thotë se përpjesëtimi 0.5206 e përfundon gjithë vargun deri te etapa «të dorëzosh reflektimin përfundimtar».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.89=0.11$. Prandaj $P(A\cap B\cap C')=0.78\times 0.75\times 0.11=0.0643$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V09: Përfundimi i një sfide për leximin e hartës

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.59\times 0.82=0.4838$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.59\times 0.82\times 0.85=0.4112$. Pra modeli thotë se përpjesëtimi 0.4112 e përfundon gjithë vargun deri te etapa «të dallosh pikën e fundit orientuese».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.85=0.15$. Prandaj $P(A\cap B\cap C')=0.59\times 0.82\times 0.15=0.0726$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

### T02-A01-V10: Kalimi i një kontrolli të futjes së të dhënave

**Përgatit llogaritjen, pjesa (a)**

$A$, $B$ dhe $C$ tregojnë me radhë suksesin në tri etapat.

Sipas rregullit të vargut, $P(A\cap B)=P(A)P(B\mid A)=0.69\times 0.84=0.5796$.

**Zhvillo llogaritjen, pjesa (b)**

$P(A\cap B\cap C)=P(A)P(B\mid A)P(C\mid A\cap B)=0.69\times 0.84\times 0.73=0.4231$. Pra modeli thotë se përpjesëtimi 0.4231 e përfundon gjithë vargun deri te etapa «ta dorëzosh regjistrimin e pastruar».

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Pas dy sukseseve të para, probabiliteti i kushtëzuar i dështimit në etapën e tretë është $1-0.73=0.27$. Prandaj $P(A\cap B\cap C')=0.69\times 0.84\times 0.27=0.1565$. Ky është përpjesëtimi i modeluar që arrin në etapën e tretë, por nuk e përfundon. Probabilitetet e etapave të mëvonshme i referohen grupeve tashmë të kufizuara nga sukseset e mëparshme. Zëvendësimi i tyre me probabilitete margjinale do t'i humbte kushtet e situatës.

## A02: Ngjarje të përbashkëta të pavarura

### T02-A02-V01: Dy kontrolle të pavarura të cilësisë

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.78\times 0.64=0.4992$. Ky është probabiliteti i modeluar që një faqe e skanuar e kalon kontrollin e figurës dhe e njëjta faqe e kalon kontrollin e metadatave. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.78+0.64-0.4992=0.9208$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.78(1-0.64)=0.2808$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V02: Pjesëmarrje e pavarur në punëtori

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.55\times 0.72=0.3960$. Ky është probabiliteti i modeluar që një banor merr pjesë në seancën e mëngjesit dhe i njëjti banor merr pjesë në seancën e mbrëmjes. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.55+0.72-0.3960=0.8740$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.55(1-0.72)=0.1540$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V03: Dy sinjale të pavarura sensorësh

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.18\times 0.27=0.0486$. Ky është probabiliteti i modeluar që aktivizohet sensori i temperaturës dhe aktivizohet sensori i dridhjeve. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.18+0.27-0.0486=0.4014$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.18(1-0.27)=0.1314$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V04: Veçori të pavarura të librave të zgjedhur

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.36\times 0.41=0.1476$. Ky është probabiliteti i modeluar që një libër i zgjedhur është përkthim dhe ai ka kopertinë të fortë. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.36+0.41-0.1476=0.6224$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.36(1-0.41)=0.2124$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V05: Ngjarje të pavarura në një anketë

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.22\times 0.63=0.1386$. Ky është probabiliteti i modeluar që një përgjigje arrin të hënën dhe ajo dërgohet nga një pajisje celulare. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.22+0.63-0.1386=0.7114$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.22(1-0.63)=0.0814$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V06: Dy ngjarje të pavarura udhëtimi

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.74\times 0.58=0.4292$. Ky është probabiliteti i modeluar që një autobus arrin brenda pesë minutash dhe një tren lidhës ka vend të lirë. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.74+0.58-0.4292=0.8908$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.74(1-0.58)=0.3108$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V07: Kontrolle të pavarura të kodimit

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.83\times 0.69=0.5727$. Ky është probabiliteti i modeluar që një regjistrim ka datë të vlefshme dhe ai ka kod të vlefshëm kategorie. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.83+0.69-0.5727=0.9473$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.83(1-0.69)=0.2573$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V08: Dy zgjedhje të pavarura

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.45\times 0.32=0.1440$. Ky është probabiliteti i modeluar që një pullë e zgjedhur është blu dhe në një zgjedhje të dytë me rikthim del një trekëndësh. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.45+0.32-0.1440=0.6260$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.45(1-0.32)=0.3060$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V09: Ngjarje të pavarura studimi

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.67\times 0.88=0.5896$. Ky është probabiliteti i modeluar që një pjesëmarrës e plotëson ditarin dhe skedari i laboratorit ngarkohet me sukses. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.67+0.88-0.5896=0.9604$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.67(1-0.88)=0.0804$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

### T02-A02-V10: Veçori të pavarura të katalogut

**Përgatit llogaritjen, pjesa (b)**

Pavarësia lejon $P(A\cap B)=P(A)P(B)=0.39\times 0.76=0.2964$. Ky është probabiliteti i modeluar që një objekt është digjitalizuar dhe fusha e krijuesit të tij është e plotë. Për

, rregulla e përgjithshme e mbledhjes jep $P(A\cup B)=0.39+0.76-0.2964=0.8536$. Ky është probabiliteti që të ndodhë të paktën njëra nga dy ngjarjet. Për

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

, nga pavarësia e $A$ dhe $B$ rrjedh edhe pavarësia e $A$ dhe $B'$. Prandaj $P(A\cap B')=0.39(1-0.76)=0.0936$. Pavarësia përdoret për të zëvendësuar probabilitetet e përbashkëta me prodhime. Rregulla e mbledhjes vlen pavarësisht nëse ngjarjet janë të pavarura.

## A03: Tabelat e kontingjencës dhe marrëdhëniet mes ngjarjeve

### T02-A03-V01: Formati i leximit dhe përfundimi i kursit

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Audio, $P(Y\mid G)=12/30=0.4000$, ndërsa për rreshtin Tekst, $P(Y\mid G^c)=28/70=0.4000$. Këto përpjesëtime të kushtëzuara janë të barabarta, prandaj ndryshoret janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Audio dhe Përfunduar përmban 12 nga 100 vëzhgimet, prandaj $P(G\cap Y)=12/100=0.1200$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V02: Anëtarësia në muze dhe pjesëmarrja në aktivitet

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Anëtar, $P(Y\mid G)=24/40=0.6000$, ndërsa për rreshtin Joanëtar, $P(Y\mid G^c)=18/60=0.3000$. Këto përpjesëtime të kushtëzuara janë të ndryshme, prandaj ndryshoret nuk janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Anëtar dhe Mori pjesë përmban 24 nga 100 vëzhgimet, prandaj $P(G\cap Y)=24/100=0.2400$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V03: Vendi i studimit dhe respektimi i afatit

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Bibliotekë, $P(Y\mid G)=21/35=0.6000$, ndërsa për rreshtin Shtëpi, $P(Y\mid G^c)=27/45=0.6000$. Këto përpjesëtime të kushtëzuara janë të barabarta, prandaj ndryshoret janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Bibliotekë dhe Në kohë përmban 21 nga 80 vëzhgimet, prandaj $P(G\cap Y)=21/80=0.2625$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V04: Përdorimi i titrave dhe përfundimi i kuizit

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Me titra, $P(Y\mid G)=30/50=0.6000$, ndërsa për rreshtin Pa titra, $P(Y\mid G^c)=18/30=0.6000$. Këto përpjesëtime të kushtëzuara janë të barabarta, prandaj ndryshoret janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Me titra dhe Përfunduar përmban 30 nga 80 vëzhgimet, prandaj $P(G\cap Y)=30/80=0.3750$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V05: Abonimi i transportit dhe vizitat në kampus

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Me abonim, $P(Y\mid G)=16/40=0.4000$, ndërsa për rreshtin Pa abonim, $P(Y\mid G^c)=14/60=0.2333$. Këto përpjesëtime të kushtëzuara janë të ndryshme, prandaj ndryshoret nuk janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Me abonim dhe Të shpeshta përmban 16 nga 100 vëzhgimet, prandaj $P(G\cap Y)=16/100=0.1600$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V06: Kujtesa dhe përgjigjja

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Me kujtesë, $P(Y\mid G)=27/40=0.6750$, ndërsa për rreshtin Pa kujtesë, $P(Y\mid G^c)=33/60=0.5500$. Këto përpjesëtime të kushtëzuara janë të ndryshme, prandaj ndryshoret nuk janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Me kujtesë dhe U përgjigj përmban 27 nga 100 vëzhgimet, prandaj $P(G\cap Y)=27/100=0.2700$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V07: Drejtimi i punëtorisë dhe certifikimi

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Metoda, $P(Y\mid G)=18/30=0.6000$, ndërsa për rreshtin Shkrim, $P(Y\mid G^c)=24/60=0.4000$. Këto përpjesëtime të kushtëzuara janë të ndryshme, prandaj ndryshoret nuk janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Metoda dhe Certifikuar përmban 18 nga 90 vëzhgimet, prandaj $P(G\cap Y)=18/90=0.2000$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V08: Lloji i pajisjes dhe plotësimi i formularit

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Tablet, $P(Y\mid G)=14/35=0.4000$, ndërsa për rreshtin Laptop, $P(Y\mid G^c)=30/45=0.6667$. Këto përpjesëtime të kushtëzuara janë të ndryshme, prandaj ndryshoret nuk janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Tablet dhe I plotë përmban 14 nga 80 vëzhgimet, prandaj $P(G\cap Y)=14/80=0.1750$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V09: Roli vullnetar dhe vizita e përsëritur

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Ciceron, $P(Y\mid G)=22/40=0.5500$, ndërsa për rreshtin Arkiv, $P(Y\mid G^c)=11/40=0.2750$. Këto përpjesëtime të kushtëzuara janë të ndryshme, prandaj ndryshoret nuk janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Ciceron dhe U kthye përmban 22 nga 80 vëzhgimet, prandaj $P(G\cap Y)=22/80=0.2750$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

### T02-A03-V10: Formati i tutorialit dhe dorëzimi i ushtrimit

**Arsyeto para llogaritjes, pjesa (a)**

Për rreshtin Drejtpërdrejt, $P(Y\mid G)=26/40=0.6500$, ndërsa për rreshtin I regjistruar, $P(Y\mid G^c)=39/60=0.6500$. Këto përpjesëtime të kushtëzuara janë të barabarta, prandaj ndryshoret janë të pavarura në këtë tabelë empirike. Ky është përshkrim i shpërndarjes empirike të paraqitur, jo provë se e njëjta marrëdhënie vlen në një popullatë më të gjerë.

**Zhvillo llogaritjen, pjesa (b)**

Prerja e Drejtpërdrejt dhe Dorëzuar përmban 26 nga 100 vëzhgimet, prandaj $P(G\cap Y)=26/100=0.2600$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$G$ dhe $Y$ nuk e përjashtojnë njëra-tjetrën, sepse kjo prerje nuk është bosh. Ngjarjet që përjashtojnë njëra-tjetrën do të kishin numërim zero në prerje.

## A04: Teorema e Bayes-it dhe normat bazë

### T02-A04-V01: Depistimi i nevojave për mbështetje në qasshmëri

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.91=0.09$.

Kur prevalenca është 0.02, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.72\times 0.02=0.0144$ dhe $P(+\cap D')=0.09\times 0.98=0.0882$. Prandaj $P(D\mid +)=0.0144/(0.0144+0.0882)=0.1404$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.11, rrugët përkatëse janë 0.0792 dhe 0.0801, duke dhënë $P(D\mid +)=0.0792/(0.0792+0.0801)=0.4972$. Ky probabilitet pasues tregon mundësinë që «një nevojë për mbështetje në qasshmëri» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V02: Zbulimi i gabimeve të rralla të transkriptimit

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.93=0.07$.

Kur prevalenca është 0.01, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.84\times 0.01=0.0084$ dhe $P(+\cap D')=0.07\times 0.99=0.0693$. Prandaj $P(D\mid +)=0.0084/(0.0084+0.0693)=0.1081$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.08, rrugët përkatëse janë 0.0672 dhe 0.0644, duke dhënë $P(D\mid +)=0.0672/(0.0672+0.0644)=0.5106$. Ky probabilitet pasues tregon mundësinë që «një gabim transkriptimi» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V03: Depistimi i rrezikut të konservimit

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.88=0.12$.

Kur prevalenca është 0.04, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.79\times 0.04=0.0316$ dhe $P(+\cap D')=0.12\times 0.96=0.1152$. Prandaj $P(D\mid +)=0.0316/(0.0316+0.1152)=0.2153$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.16, rrugët përkatëse janë 0.1264 dhe 0.1008, duke dhënë $P(D\mid +)=0.1264/(0.1264+0.1008)=0.5563$. Ky probabilitet pasues tregon mundësinë që «një objekt në rrezik konservimi» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V04: Zbulimi i regjistrimeve të dyfishta

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.86=0.14$.

Kur prevalenca është 0.03, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.90\times 0.03=0.0270$ dhe $P(+\cap D')=0.14\times 0.97=0.1358$. Prandaj $P(D\mid +)=0.0270/(0.0270+0.1358)=0.1658$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.14, rrugët përkatëse janë 0.1260 dhe 0.1204, duke dhënë $P(D\mid +)=0.1260/(0.1260+0.1204)=0.5114$. Ky probabilitet pasues tregon mundësinë që «një regjistrim të dyfishtë» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V05: Depistimi i nevojës për mbështetje gjuhësore

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.94=0.06$.

Kur prevalenca është 0.05, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.76\times 0.05=0.0380$ dhe $P(+\cap D')=0.06\times 0.95=0.0570$. Prandaj $P(D\mid +)=0.0380/(0.0380+0.0570)=0.4000$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.19, rrugët përkatëse janë 0.1444 dhe 0.0486, duke dhënë $P(D\mid +)=0.1444/(0.1444+0.0486)=0.7482$. Ky probabilitet pasues tregon mundësinë që «një nevojë për mbështetje gjuhësore» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V06: Zbulimi i figurave të dëmtuara

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.90=0.10$.

Kur prevalenca është 0.02, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.88\times 0.02=0.0176$ dhe $P(+\cap D')=0.10\times 0.98=0.0980$. Prandaj $P(D\mid +)=0.0176/(0.0176+0.0980)=0.1522$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.12, rrugët përkatëse janë 0.1056 dhe 0.0880, duke dhënë $P(D\mid +)=0.1056/(0.1056+0.0880)=0.5455$. Ky probabilitet pasues tregon mundësinë që «një figurë të dëmtuar» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V07: Depistimi i integritetit kërkimor

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.96=0.04$.

Kur prevalenca është 0.01, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.81\times 0.01=0.0081$ dhe $P(+\cap D')=0.04\times 0.99=0.0396$. Prandaj $P(D\mid +)=0.0081/(0.0081+0.0396)=0.1698$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.07, rrugët përkatëse janë 0.0567 dhe 0.0372, duke dhënë $P(D\mid +)=0.0567/(0.0567+0.0372)=0.6038$. Ky probabilitet pasues tregon mundësinë që «një dorëzim që kërkon shqyrtim të integritetit» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V08: Paralajmërimi për defekt të pajisjes

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.89=0.11$.

Kur prevalenca është 0.06, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.85\times 0.06=0.0510$ dhe $P(+\cap D')=0.11\times 0.94=0.1034$. Prandaj $P(D\mid +)=0.0510/(0.0510+0.1034)=0.3303$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.21, rrugët përkatëse janë 0.1785 dhe 0.0869, duke dhënë $P(D\mid +)=0.1785/(0.1785+0.0869)=0.6726$. Ky probabilitet pasues tregon mundësinë që «një defekt të afërt të pajisjes» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V09: Zbulimi i anomalive të katalogimit

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.92=0.08$.

Kur prevalenca është 0.03, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.74\times 0.03=0.0222$ dhe $P(+\cap D')=0.08\times 0.97=0.0776$. Prandaj $P(D\mid +)=0.0222/(0.0222+0.0776)=0.2224$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.15, rrugët përkatëse janë 0.1110 dhe 0.0680, duke dhënë $P(D\mid +)=0.1110/(0.1110+0.0680)=0.6201$. Ky probabilitet pasues tregon mundësinë që «një regjistrim me anomali katalogimi» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

### T02-A04-V10: Klasifikimi sipas përparësisë së mbështetjes

**Arsyeto para llogaritjes, pjesa (a)**

Probabiliteti i rezultatit gabimisht pozitiv është $1-0.95=0.05$.

Kur prevalenca është 0.04, rrugët drejt rezultatit pozitiv janë $P(+\cap D)=0.87\times 0.04=0.0348$ dhe $P(+\cap D')=0.05\times 0.96=0.0480$. Prandaj $P(D\mid +)=0.0348/(0.0348+0.0480)=0.4203$.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

Kur prevalenca është 0.18, rrugët përkatëse janë 0.1566 dhe 0.0410, duke dhënë $P(D\mid +)=0.1566/(0.1566+0.0410)=0.7925$. Ky probabilitet pasues tregon mundësinë që «një rast që ka vërtet përparësi të lartë mbështetjeje» të jetë vërtet e pranishme pas një rezultati pozitiv. Ndjeshmëria kushtëzohet mbi praninë e gjendjes që në fillim. Norma bazë më e lartë e rrit pjesën e rezultateve pozitive që janë vërtet pozitive.

## A05: Vlera e pritur, varianca, PMF-ja dhe CDF-ja për ndryshore diskrete

### T02-A05-V01: Numri i pyetjeve pasuese

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.20+0.35+0.30+0.15=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=0(0.20)+1(0.35)+3(0.30)+5(0.15)=2.0000$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 2.0000. Më pas, $E(X^2)=0^2(0.20)+1^2(0.35)+3^2(0.30)+5^2(0.15)=6.8000$, kështu që $\operatorname{Var}(X)=6.8000-2.0000^2=2.8000$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(0)=0.20$, $F(1)=0.55$, $F(3)=0.85$, $F(5)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V02: Kërkesat ditore në arkiv

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.25+0.40+0.20+0.15=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=1(0.25)+2(0.40)+4(0.20)+6(0.15)=2.7500$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 2.7500. Më pas, $E(X^2)=1^2(0.25)+2^2(0.40)+4^2(0.20)+6^2(0.15)=10.4500$, kështu që $\operatorname{Var}(X)=10.4500-2.7500^2=2.8875$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(1)=0.25$, $F(2)=0.65$, $F(4)=0.85$, $F(6)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V03: Seritë e përfunduara të ushtrimeve

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.10+0.30+0.45+0.15=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=0(0.10)+2(0.30)+3(0.45)+7(0.15)=3.0000$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 3.0000. Më pas, $E(X^2)=0^2(0.10)+2^2(0.30)+3^2(0.45)+7^2(0.15)=12.6000$, kështu që $\operatorname{Var}(X)=12.6000-3.0000^2=3.6000$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(0)=0.10$, $F(2)=0.40$, $F(3)=0.85$, $F(7)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V04: Ndryshimet e raportuara të rrugës

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.45+0.25+0.20+0.10=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=0(0.45)+1(0.25)+2(0.20)+4(0.10)=1.0500$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 1.0500. Më pas, $E(X^2)=0^2(0.45)+1^2(0.25)+2^2(0.20)+4^2(0.10)=2.6500$, kështu që $\operatorname{Var}(X)=2.6500-1.0500^2=1.5475$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(0)=0.45$, $F(1)=0.70$, $F(2)=0.90$, $F(4)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V05: Takimet javore të komunitetit

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.30+0.25+0.35+0.10=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=1(0.30)+3(0.25)+4(0.35)+8(0.10)=3.2500$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 3.2500. Më pas, $E(X^2)=1^2(0.30)+3^2(0.25)+4^2(0.35)+8^2(0.10)=14.5500$, kështu që $\operatorname{Var}(X)=14.5500-3.2500^2=3.9875$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(1)=0.30$, $F(3)=0.55$, $F(4)=0.90$, $F(8)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V06: Rikuperimet e suksesshme të skedarëve

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.15+0.25+0.40+0.20=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=0(0.15)+2(0.25)+5(0.40)+6(0.20)=3.7000$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 3.7000. Më pas, $E(X^2)=0^2(0.15)+2^2(0.25)+5^2(0.40)+6^2(0.20)=18.2000$, kështu që $\operatorname{Var}(X)=18.2000-3.7000^2=4.5100$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(0)=0.15$, $F(2)=0.40$, $F(5)=0.80$, $F(6)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V07: Dhomat e vizituara të muzeut

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.20+0.30+0.35+0.15=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=2(0.20)+4(0.30)+5(0.35)+9(0.15)=4.7000$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 4.7000. Më pas, $E(X^2)=2^2(0.20)+4^2(0.30)+5^2(0.35)+9^2(0.15)=26.5000$, kështu që $\operatorname{Var}(X)=26.5000-4.7000^2=4.4100$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(2)=0.20$, $F(4)=0.50$, $F(5)=0.85$, $F(9)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V08: Leximet plotësuese të përfunduara

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.25+0.30+0.25+0.20=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=0(0.25)+1(0.30)+4(0.25)+6(0.20)=2.5000$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 2.5000. Më pas, $E(X^2)=0^2(0.25)+1^2(0.30)+4^2(0.25)+6^2(0.20)=11.5000$, kështu që $\operatorname{Var}(X)=11.5000-2.5000^2=5.2500$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(0)=0.25$, $F(1)=0.55$, $F(4)=0.80$, $F(6)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V09: Segmentet e verifikuara të historisë gojore

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.15+0.35+0.30+0.20=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=1(0.15)+2(0.35)+3(0.30)+5(0.20)=2.7500$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 2.7500. Më pas, $E(X^2)=1^2(0.15)+2^2(0.35)+3^2(0.30)+5^2(0.20)=9.2500$, kështu që $\operatorname{Var}(X)=9.2500-2.7500^2=1.6875$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(1)=0.15$, $F(2)=0.50$, $F(3)=0.80$, $F(5)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

### T02-A05-V10: Paralajmërimet për cilësinë e të dhënave

**Përgatit llogaritjen, pjesa (a)**

Të gjitha masat janë jonegative dhe shuma e tyre është 0.40+0.25+0.20+0.15=1.00, prandaj tabela është PMF e vlefshme.

**Zhvillo llogaritjen, pjesa (b)**

$E(X)=\sum xP(X=x)=0(0.40)+2(0.25)+4(0.20)+7(0.15)=2.3500$. Në shumë vëzhgime të krahasueshme, mesatarja afatgjatë e madhësisë së emërtuar më sipër do t'i afrohej 2.3500. Më pas, $E(X^2)=0^2(0.40)+2^2(0.25)+4^2(0.20)+7^2(0.15)=11.5500$, kështu që $\operatorname{Var}(X)=11.5500-2.3500^2=6.0275$; kjo variancë shprehet në njësi numërimi në katror.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Vlerat kumulative janë $F(0)=0.40$, $F(2)=0.65$, $F(4)=0.85$, $F(7)=1.00$. Grafiku i PMF-së vendos një shtyllë ose masë të veçantë në secilën vlerë mbështetëse. CDF-ja është funksion shkallëzues jozbritës, i vazhdueshëm nga e djathta, që i grumbullon masat dhe përfundon në 1.

## A06: Probabilitetet e sakta binomiale

### T02-A06-V01: Kontrollet e përfunduara të pëlqimit

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(8,0.62)$.

$P(X=5)=\binom{8}{5}0.62^{5}(1-0.62)^{3}=0.2815$. Ky është probabiliteti i modeluar që saktësisht 5 nga 8 kontrolle pëlqimi ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=7)=\binom{8}{7}0.62^{7}(1-0.62)^{1}=0.1071$. Ky është probabiliteti përkatës për saktësisht 7.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=8(0.62)=4.9600$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=8(0.62)(0.38)=1.8848$. Në grupe të përsëritura me 8 njësi, numri mesatar do t'i afrohej 4.9600.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 8. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse përfundohet. Probabiliteti i suksesit duhet të mbetet 0.62, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V02: Figurat e klasifikuara saktë

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(9,0.74)$.

$P(X=6)=\binom{9}{6}0.74^{6}(1-0.74)^{3}=0.2424$. Ky është probabiliteti i modeluar që saktësisht 6 nga 9 figura ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=8)=\binom{9}{8}0.74^{8}(1-0.74)^{1}=0.2104$. Ky është probabiliteti përkatës për saktësisht 8.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=9(0.74)=6.6600$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=9(0.74)(0.26)=1.7316$. Në grupe të përsëritura me 9 njësi, numri mesatar do t'i afrohej 6.6600.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 9. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse klasifikohet saktë. Probabiliteti i suksesit duhet të mbetet 0.74, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V03: Kërkesat e kthyera të ditarit

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(7,0.58)$.

$P(X=3)=\binom{7}{3}0.58^{3}(1-0.58)^{4}=0.2125$. Ky është probabiliteti i modeluar që saktësisht 3 nga 7 kërkesa ditari ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=5)=\binom{7}{5}0.58^{5}(1-0.58)^{2}=0.2431$. Ky është probabiliteti përkatës për saktësisht 5.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=7(0.58)=4.0600$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=7(0.58)(0.42)=1.7052$. Në grupe të përsëritura me 7 njësi, numri mesatar do t'i afrohej 4.0600.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 7. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse kthehet. Probabiliteti i suksesit duhet të mbetet 0.58, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V04: Kërkimet e suksesshme në arkiv

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(10,0.43)$.

$P(X=4)=\binom{10}{4}0.43^{4}(1-0.43)^{6}=0.2462$. Ky është probabiliteti i modeluar që saktësisht 4 nga 10 kërkime në arkiv ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=6)=\binom{10}{6}0.43^{6}(1-0.43)^{4}=0.1401$. Ky është probabiliteti përkatës për saktësisht 6.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=10(0.43)=4.3000$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=10(0.43)(0.57)=2.4510$. Në grupe të përsëritura me 10 njësi, numri mesatar do t'i afrohej 4.3000.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 10. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse ka sukses. Probabiliteti i suksesit duhet të mbetet 0.43, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V05: Leximet e përdorshme të sensorit

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(6,0.81)$.

$P(X=4)=\binom{6}{4}0.81^{4}(1-0.81)^{2}=0.2331$. Ky është probabiliteti i modeluar që saktësisht 4 nga 6 lexime sensori ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=6)=\binom{6}{6}0.81^{6}(1-0.81)^{0}=0.2824$. Ky është probabiliteti përkatës për saktësisht 6.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=6(0.81)=4.8600$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=6(0.81)(0.19)=0.9234$. Në grupe të përsëritura me 6 njësi, numri mesatar do t'i afrohej 4.8600.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 6. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse është i përdorshëm. Probabiliteti i suksesit duhet të mbetet 0.81, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V06: Dorëzimet në kohë të tutorialit

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(12,0.67)$.

$P(X=8)=\binom{12}{8}0.67^{8}(1-0.67)^{4}=0.2384$. Ky është probabiliteti i modeluar që saktësisht 8 nga 12 dorëzime tutoriali ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=10)=\binom{12}{10}0.67^{10}(1-0.67)^{2}=0.1310$. Ky është probabiliteti përkatës për saktësisht 10.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=12(0.67)=8.0400$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=12(0.67)(0.33)=2.6532$. Në grupe të përsëritura me 12 njësi, numri mesatar do t'i afrohej 8.0400.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 12. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse arrin në kohë. Probabiliteti i suksesit duhet të mbetet 0.67, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V07: Regjistrimet e verifikuara të katalogut

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(9,0.52)$.

$P(X=4)=\binom{9}{4}0.52^{4}(1-0.52)^{5}=0.2347$. Ky është probabiliteti i modeluar që saktësisht 4 nga 9 regjistrime katalogu ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=7)=\binom{9}{7}0.52^{7}(1-0.52)^{2}=0.0853$. Ky është probabiliteti përkatës për saktësisht 7.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=9(0.52)=4.6800$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=9(0.52)(0.48)=2.2464$. Në grupe të përsëritura me 9 njësi, numri mesatar do t'i afrohej 4.6800.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 9. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse verifikohet. Probabiliteti i suksesit duhet të mbetet 0.52, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V08: Takimet e përfunduara të intervistës

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(11,0.76)$.

$P(X=8)=\binom{11}{8}0.76^{8}(1-0.76)^{3}=0.2539$. Ky është probabiliteti i modeluar që saktësisht 8 nga 11 takime interviste ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=9)=\binom{11}{9}0.76^{9}(1-0.76)^{2}=0.2680$. Ky është probabiliteti përkatës për saktësisht 9.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=11(0.76)=8.3600$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=11(0.76)(0.24)=2.0064$. Në grupe të përsëritura me 11 njësi, numri mesatar do t'i afrohej 8.3600.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 11. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse përfundohet. Probabiliteti i suksesit duhet të mbetet 0.76, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V09: Zgjedhjet e sakta të rrugës

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(8,0.35)$.

$P(X=2)=\binom{8}{2}0.35^{2}(1-0.35)^{6}=0.2587$. Ky është probabiliteti i modeluar që saktësisht 2 nga 8 zgjedhje rruge ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=4)=\binom{8}{4}0.35^{4}(1-0.35)^{4}=0.1875$. Ky është probabiliteti përkatës për saktësisht 4.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=8(0.35)=2.8000$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=8(0.35)(0.65)=1.8200$. Në grupe të përsëritura me 8 njësi, numri mesatar do t'i afrohej 2.8000.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 8. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse është e saktë. Probabiliteti i suksesit duhet të mbetet 0.35, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

### T02-A06-V10: Transkriptimet e suksesshme të audios

**Përgatit llogaritjen, pjesa (a)**

Modeli është $X\sim B(10,0.69)$.

$P(X=6)=\binom{10}{6}0.69^{6}(1-0.69)^{4}=0.2093$. Ky është probabiliteti i modeluar që saktësisht 6 nga 10 transkriptime audioje ta plotësojnë përkufizimin e suksesit.

**Zhvillo llogaritjen, pjesa (b)**

$P(X=8)=\binom{10}{8}0.69^{8}(1-0.69)^{2}=0.2222$. Ky është probabiliteti përkatës për saktësisht 8.

**Zhvillo llogaritjen, pjesa (c)**

$E(X)=n\pi=10(0.69)=6.9000$ dhe $\operatorname{Var}(X)=n\pi(1-\pi)=10(0.69)(0.31)=2.1390$. Në grupe të përsëritura me 10 njësi, numri mesatar do t'i afrohej 6.9000.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Numri i provave duhet të mbetet fiks në 10. Secila njësi klasifikohet vetëm si sukses ose dështim sipas asaj nëse ka sukses. Probabiliteti i suksesit duhet të mbetet 0.69, ndërsa rezultatet e provave duhet të jenë të pavarura. Nëse ndonjë kusht dështon, kjo llogaritje binomiale nuk arsyetohet.

## A07: Probabilitetet e skajit binomial përmes komplementit

### T02-A07-V01: Më shumë se 3 regjistrime që kërkojnë shqyrtim manual

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(40,0.04)$, ndërsa komplementi i $X>3$ është $X\leq 3$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>3)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)]=1-[0.1954+0.3256+0.2646+0.1396]\approx 1-0.9252=0.0748$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.9252 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.0748 rastit me më shumë se 3 suksese mes 40 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi kërkon shqyrtim manual. Komplementi përdor 4 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 4 deri në 40.

### T02-A07-V02: Më shumë se 5 vizitorë që kërkojnë audiociceron

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(25,0.12)$, ndërsa komplementi i $X>5$ është $X\leq 5$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>5)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)]=1-[0.0409+0.1395+0.2283+0.2387+0.1790+0.1025]\approx 1-0.9291=0.0709$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.9291 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.0709 rastit me më shumë se 5 suksese mes 25 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi kërkon audiociceron. Komplementi përdor 6 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 6 deri në 25.

### T02-A07-V03: Më shumë se 4 lidhje të pavlefshme të anketës

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(30,0.06)$, ndërsa komplementi i $X>4$ është $X\leq 4$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>4)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)]=1-[0.1563+0.2992+0.2769+0.1650+0.0711]\approx 1-0.9685=0.0315$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.9685 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.0315 rastit me më shumë se 4 suksese mes 30 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi kthehet si e pavlefshme. Komplementi përdor 5 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 5 deri në 30.

### T02-A07-V04: Më shumë se 6 objekte që kërkojnë konservim

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(35,0.09)$, ndërsa komplementi i $X>6$ është $X\leq 6$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>6)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)+P(X=6)]=1-[0.0369+0.1276+0.2145+0.2333+0.1846+0.1132+0.0560]\approx 1-0.9660=0.0340$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.9660 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.0340 rastit me më shumë se 6 suksese mes 35 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi kërkon punë konservimi. Komplementi përdor 7 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 7 deri në 35.

### T02-A07-V05: Më shumë se 4 pjesëmarrës që humbin një kujtesë

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(28,0.08)$, ndërsa komplementi i $X>4$ është $X\leq 4$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>4)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)]=1-[0.0968+0.2358+0.2768+0.2086+0.1134]\approx 1-0.9314=0.0686$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.9314 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.0686 rastit me më shumë se 4 suksese mes 28 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi humb një kujtesë. Komplementi përdor 5 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 5 deri në 28.

### T02-A07-V06: Më shumë se 5 ngarkime që kërkojnë një përpjekje të dytë

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(32,0.07)$, ndërsa komplementi i $X>5$ është $X\leq 5$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>5)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)]=1-[0.0981+0.2362+0.2755+0.2074+0.1132+0.0477]\approx 1-0.9780=0.0220$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.9780 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.0220 rastit me më shumë se 5 suksese mes 32 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi kërkon një përpjekje të dytë. Komplementi përdor 6 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 6 deri në 32.

### T02-A07-V07: Më shumë se 5 faqe të zgjedhura që përmbajnë shënime

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(20,0.15)$, ndërsa komplementi i $X>5$ është $X\leq 5$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>5)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)]=1-[0.0388+0.1368+0.2293+0.2428+0.1821+0.1028]\approx 1-0.9327=0.0673$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.9327 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.0673 rastit me më shumë se 5 suksese mes 20 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi përmban shënime. Komplementi përdor 6 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 6 deri në 20.

### T02-A07-V08: Më shumë se 4 intervista që kërkojnë ricaktim

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(24,0.11)$, ndërsa komplementi i $X>4$ është $X\leq 4$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>4)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)]=1-[0.0610+0.1810+0.2572+0.2331+0.1513]\approx 1-0.8835=0.1165$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.8835 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.1165 rastit me më shumë se 4 suksese mes 24 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi kërkon ricaktim. Komplementi përdor 5 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 5 deri në 24.

### T02-A07-V09: Më shumë se 3 vëzhgime të rrugës që tregojnë vonesë

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(36,0.05)$, ndërsa komplementi i $X>3$ është $X\leq 3$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>3)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)]=1-[0.1578+0.2990+0.2753+0.1642]\approx 1-0.8963=0.1037$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.8963 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.1037 rastit me më shumë se 3 suksese mes 36 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi tregon vonesë. Komplementi përdor 4 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 4 deri në 36.

### T02-A07-V10: Më shumë se 5 formularë që përmbajnë koment fakultativ

**Përgatit llogaritjen, pjesa (a)**

Këtu $X\sim B(18,0.18)$, ndërsa komplementi i $X>5$ është $X\leq 5$.

**Zhvillo llogaritjen, pjesa (b)**

Prandaj $P(X>5)=1-[P(X=0)+P(X=1)+P(X=2)+P(X=3)+P(X=4)+P(X=5)]=1-[0.0281+0.1110+0.2071+0.2425+0.1996+0.1227]\approx 1-0.9111=0.0889$. Shenja e përafrimit nevojitet sepse termat e paraqitur janë rrumbullakosur. Vlera 0.9111 u llogarit nga termat e parrumbullakosur.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Modeli i cakton probabilitetin 0.0889 rastit me më shumë se 5 suksese mes 18 njësive të shqyrtuara. Këtu një sukses do të thotë se një njësi përmban një koment fakultativ. Komplementi përdor 6 terma të skajit të poshtëm, ndërsa një shumë e drejtpërdrejtë do të kërkonte vlerat 6 deri në 18.

## A09: Probabilitetet e shpërndarjes normale standarde

### T02-A09-V01: Zonat e shpërndarjes normale standarde, grupi 1

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -0.45)=\Phi(-0.45)=0.3264$. Ngjyrose zonën majtas nga -0.45.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>1.36)=1-\Phi(1.36)=0.0869$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-0.80<Z\leq 0.95)=\Phi(0.95)-\Phi(-0.80)=0.6171$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V02: Zonat e shpërndarjes normale standarde, grupi 2

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -1.12)=\Phi(-1.12)=0.1314$. Ngjyrose zonën majtas nga -1.12.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>0.84)=1-\Phi(0.84)=0.2005$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-0.35<Z\leq 1.42)=\Phi(1.42)-\Phi(-0.35)=0.5590$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V03: Zonat e shpërndarjes normale standarde, grupi 3

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq 0.28)=\Phi(0.28)=0.6103$. Ngjyrose zonën majtas nga 0.28.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>1.74)=1-\Phi(1.74)=0.0409$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-1.05<Z\leq 0.62)=\Phi(0.62)-\Phi(-1.05)=0.5855$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V04: Zonat e shpërndarjes normale standarde, grupi 4

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -0.93)=\Phi(-0.93)=0.1762$. Ngjyrose zonën majtas nga -0.93.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>1.18)=1-\Phi(1.18)=0.1190$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-0.44<Z\leq 1.27)=\Phi(1.27)-\Phi(-0.44)=0.5680$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V05: Zonat e shpërndarjes normale standarde, grupi 5

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq 0.67)=\Phi(0.67)=0.7486$. Ngjyrose zonën majtas nga 0.67.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>2.05)=1-\Phi(2.05)=0.0202$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-1.33<Z\leq 0.71)=\Phi(0.71)-\Phi(-1.33)=0.6694$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V06: Zonat e shpërndarjes normale standarde, grupi 6

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -1.48)=\Phi(-1.48)=0.0694$. Ngjyrose zonën majtas nga -1.48.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>0.56)=1-\Phi(0.56)=0.2877$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-0.92<Z\leq 1.08)=\Phi(1.08)-\Phi(-0.92)=0.6811$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V07: Zonat e shpërndarjes normale standarde, grupi 7

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq 0.14)=\Phi(0.14)=0.5557$. Ngjyrose zonën majtas nga 0.14.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>1.51)=1-\Phi(1.51)=0.0655$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-0.68<Z\leq 1.19)=\Phi(1.19)-\Phi(-0.68)=0.6347$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V08: Zonat e shpërndarjes normale standarde, grupi 8

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -0.76)=\Phi(-0.76)=0.2236$. Ngjyrose zonën majtas nga -0.76.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>1.89)=1-\Phi(1.89)=0.0294$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-1.21<Z\leq 0.37)=\Phi(0.37)-\Phi(-1.21)=0.5312$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V09: Zonat e shpërndarjes normale standarde, grupi 9

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq 0.91)=\Phi(0.91)=0.8186$. Ngjyrose zonën majtas nga 0.91.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>1.24)=1-\Phi(1.24)=0.1075$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-0.57<Z\leq 1.63)=\Phi(1.63)-\Phi(-0.57)=0.6641$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

### T02-A09-V10: Zonat e shpërndarjes normale standarde, grupi 10

**Përgatit llogaritjen, pjesa (a)**

Shkruaj $\Phi(z)=P(Z\leq z)$.

$P(Z\leq -0.22)=\Phi(-0.22)=0.4129$. Ngjyrose zonën majtas nga -0.22.

**Zhvillo llogaritjen, pjesa (b)**

$P(Z>2.17)=1-\Phi(2.17)=0.0150$. Ngjyrose skajin e djathtë.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

$P(-1.46<Z\leq 0.88)=\Phi(0.88)-\Phi(-1.46)=0.7384$. Ngjyrose zonën mes dy kufijve. Për një shpërndarje të vazhdueshme, përfshirja e kufirit nuk e ndryshon probabilitetin.

## A10: Probabilitetet për një shpërndarje normale të përgjithshme

### T02-A10-V01: Modeli normal: Rezultati i rrjedhshmërisë në lexim

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{100}=10.00$.

$z=(79-72)/10.00\approx 0.7000$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 79)=\Phi((79-72)/10.00)=0.7580$. Pra modeli vendos përpjesëtimin 0.7580 të vlerave të ndryshores në ose nën 79 pikë. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(68-72)/10.00\approx -0.4000$ dhe $P(X>68)=1-\Phi((68-72)/10.00)=0.6554$. Ky është përpjesëtimi i modeluar mbi 68 pikë, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V02: Modeli normal: Koha e përpunimit në arkiv

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{64}=8.00$.

$z=(51-45)/8.00\approx 0.7500$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 51)=\Phi((51-45)/8.00)=0.7734$. Pra modeli vendos përpjesëtimin 0.7734 të vlerave të ndryshores në ose nën 51 minuta. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(39-45)/8.00\approx -0.7500$ dhe $P(X>39)=1-\Phi((39-45)/8.00)=0.7734$. Ky është përpjesëtimi i modeluar mbi 39 minuta, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V03: Modeli normal: Rezultati i mirëqenies

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{81}=9.00$.

$z=(64-58)/9.00\approx 0.6667$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 64)=\Phi((64-58)/9.00)=0.7475$. Pra modeli vendos përpjesëtimin 0.7475 të vlerave të ndryshores në ose nën 64 pikë. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(52-58)/9.00\approx -0.6667$ dhe $P(X>52)=1-\Phi((52-58)/9.00)=0.7475$. Ky është përpjesëtimi i modeluar mbi 52 pikë, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V04: Modeli normal: Kohëzgjatja e vizitës në muze

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{225}=15.00$.

$z=(105-90)/15.00\approx 1.0000$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 105)=\Phi((105-90)/15.00)=0.8413$. Pra modeli vendos përpjesëtimin 0.8413 të vlerave të ndryshores në ose nën 105 minuta. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(78-90)/15.00\approx -0.8000$ dhe $P(X>78)=1-\Phi((78-90)/15.00)=0.7881$. Ky është përpjesëtimi i modeluar mbi 78 minuta, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V05: Modeli normal: Rezultati i kujtesës

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{144}=12.00$.

$z=(124-110)/12.00\approx 1.1667$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 124)=\Phi((124-110)/12.00)=0.8783$. Pra modeli vendos përpjesëtimin 0.8783 të vlerave të ndryshores në ose nën 124 pikë. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(103-110)/12.00\approx -0.5833$ dhe $P(X>103)=1-\Phi((103-110)/12.00)=0.7202$. Ky është përpjesëtimi i modeluar mbi 103 pikë, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V06: Modeli normal: Indeksi i nivelit të zërit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{49}=7.00$.

$z=(42-38)/7.00\approx 0.5714$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 42)=\Phi((42-38)/7.00)=0.7161$. Pra modeli vendos përpjesëtimin 0.7161 të vlerave të ndryshores në ose nën 42 pikë indeksi. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(33-38)/7.00\approx -0.7143$ dhe $P(X>33)=1-\Phi((33-38)/7.00)=0.7625$. Ky është përpjesëtimi i modeluar mbi 33 pikë indeksi, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V07: Modeli normal: Rezultati i sigurisë në kurs

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{121}=11.00$.

$z=(75-66)/11.00\approx 0.8182$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 75)=\Phi((75-66)/11.00)=0.7934$. Pra modeli vendos përpjesëtimin 0.7934 të vlerave të ndryshores në ose nën 75 pikë. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(59-66)/11.00\approx -0.6364$ dhe $P(X>59)=1-\Phi((59-66)/11.00)=0.7377$. Ky është përpjesëtimi i modeluar mbi 59 pikë, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V08: Modeli normal: Koha e reagimit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{3600}=60.00$.

$z=(575-520)/60.00\approx 0.9167$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 575)=\Phi((575-520)/60.00)=0.8203$. Pra modeli vendos përpjesëtimin 0.8203 të vlerave të ndryshores në ose nën 575 milisekonda. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(485-520)/60.00\approx -0.5833$ dhe $P(X>485)=1-\Phi((485-520)/60.00)=0.7202$. Ky është përpjesëtimi i modeluar mbi 485 milisekonda, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V09: Modeli normal: Rezultati i besimit në komunitet

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{64}=8.00$.

$z=(54-48)/8.00\approx 0.7500$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 54)=\Phi((54-48)/8.00)=0.7734$. Pra modeli vendos përpjesëtimin 0.7734 të vlerave të ndryshores në ose nën 54 pikë. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(43-48)/8.00\approx -0.6250$ dhe $P(X>43)=1-\Phi((43-48)/8.00)=0.7340$. Ky është përpjesëtimi i modeluar mbi 43 pikë, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

### T02-A10-V10: Modeli normal: Rezultati i saktësisë së katalogimit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{36}=6.00$.

$z=(88-84)/6.00\approx 0.6667$. Duke ruajtur herësin e parrumbullakosur merret $P(X\leq 88)=\Phi((88-84)/6.00)=0.7475$. Pra modeli vendos përpjesëtimin 0.7475 të vlerave të ndryshores në ose nën 88 pikë. Ngjyrose anën e majtë të këtij kufiri.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z=(79-84)/6.00\approx -0.8333$ dhe $P(X>79)=1-\Phi((79-84)/6.00)=0.7977$. Ky është përpjesëtimi i modeluar mbi 79 pikë, i paraqitur nga skaji i djathtë. Të dy interpretimet varen nga modeli normal i dhënë.

## A11: Kuantilet e anasjella të shpërndarjes normale standarde

### T02-A11-V01: Gjetja e kuantileve z për 70% dhe 92%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.70$ jep $z_{70\%}=0.5244$. Meqë 0.70 është më e madhe se 0.50, ky kufi është pozitiv.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.92$ jep $z_{92\%}=1.4051$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V02: Gjetja e kuantileve z për 15% dhe 88%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.15$ jep $z_{15\%}=-1.0364$. Meqë 0.15 është më e vogël se 0.50, ky kufi është negativ.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.88$ jep $z_{88\%}=1.1750$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V03: Gjetja e kuantileve z për 80% dhe 96%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.80$ jep $z_{80\%}=0.8416$. Meqë 0.80 është më e madhe se 0.50, ky kufi është pozitiv.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.96$ jep $z_{96\%}=1.7507$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V04: Gjetja e kuantileve z për 28% dhe 90%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.28$ jep $z_{28\%}=-0.5828$. Meqë 0.28 është më e vogël se 0.50, ky kufi është negativ.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.90$ jep $z_{90\%}=1.2816$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V05: Gjetja e kuantileve z për 50% dhe 94%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.50$ jep $z_{50\%}=0.0000$. Meqë 0.50 është e barabartë me 0.50, ky kufi është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.94$ jep $z_{94\%}=1.5548$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V06: Gjetja e kuantileve z për 75% dhe 97%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.75$ jep $z_{75\%}=0.6745$. Meqë 0.75 është më e madhe se 0.50, ky kufi është pozitiv.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.97$ jep $z_{97\%}=1.8808$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V07: Gjetja e kuantileve z për 32% dhe 68%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.32$ jep $z_{32\%}=-0.4677$. Meqë 0.32 është më e vogël se 0.50, ky kufi është negativ.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.68$ jep $z_{68\%}=0.4677$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V08: Gjetja e kuantileve z për 82% dhe 95%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.82$ jep $z_{82\%}=0.9154$. Meqë 0.82 është më e madhe se 0.50, ky kufi është pozitiv.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.95$ jep $z_{95\%}=1.6449$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V09: Gjetja e kuantileve z për 11% dhe 62%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.11$ jep $z_{11\%}=-1.2265$. Meqë 0.11 është më e vogël se 0.50, ky kufi është negativ.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.62$ jep $z_{62\%}=0.3055$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

### T02-A11-V10: Gjetja e kuantileve z për 78% dhe 93%

**Përgatit llogaritjen, pjesa (a)**

Një kuantil fillon me probabilitetin kumulativ $q$ dhe zgjidh $\Phi(z)=q$ për një pozitë.

$\Phi(z)=0.78$ jep $z_{78\%}=0.7722$. Meqë 0.78 është më e madhe se 0.50, ky kufi është pozitiv.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$\Phi(z)=0.93$ jep $z_{93\%}=1.4758$; kufiri i dytë pritet të jetë pozitiv. Hyrjet janë sipërfaqe, ndërsa daljet janë pozita në boshtin z. Kjo e përmbys drejtimin e një llogaritjeje të zakonshme të CDF-së.

## A12: Shpërndarja e kampionimit e mesatares

### T02-A12-V01: Saktësia e mesatares së kampionit për rezultatin e leximit

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=64$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{196}=14.00$, prandaj $\operatorname{SE}=14.00/\sqrt{49}=2.0000$ pikë. Në kampione të përsëritura, mesataret përqendrohen te 64 pikë me devijim standard 2.0000 pikë.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 100, $\operatorname{SE}=\sqrt{100}/\sqrt{49}=1.4286$ pikë. Varianca më e vogël e popullatës e zvogëlon SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=121$, $\operatorname{SE}=\sqrt{196}/\sqrt{121}=1.2727$ pikë. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V02: Saktësia e mesatares së kampionit për kohën e përpunimit

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=52$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{225}=15.00$, prandaj $\operatorname{SE}=15.00/\sqrt{36}=2.5000$ minuta. Në kampione të përsëritura, mesataret përqendrohen te 52 minuta me devijim standard 2.5000 minuta.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 144, $\operatorname{SE}=\sqrt{144}/\sqrt{36}=2.0000$ minuta. Varianca më e vogël e popullatës e zvogëlon SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=100$, $\operatorname{SE}=\sqrt{225}/\sqrt{100}=1.5000$ minuta. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V03: Saktësia e mesatares së kampionit për indeksin e mirëqenies

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=71$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{144}=12.00$, prandaj $\operatorname{SE}=12.00/\sqrt{64}=1.5000$ pikë indeksi. Në kampione të përsëritura, mesataret përqendrohen te 71 pikë indeksi me devijim standard 1.5000 pikë indeksi.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 256, $\operatorname{SE}=\sqrt{256}/\sqrt{64}=2.0000$ pikë indeksi. Varianca më e madhe e popullatës e rrit SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=81$, $\operatorname{SE}=\sqrt{144}/\sqrt{81}=1.3333$ pikë indeksi. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V04: Saktësia e mesatares së kampionit për rezultatin e kujtesës

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=105$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{324}=18.00$, prandaj $\operatorname{SE}=18.00/\sqrt{81}=2.0000$ pikë. Në kampione të përsëritura, mesataret përqendrohen te 105 pikë me devijim standard 2.0000 pikë.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 225, $\operatorname{SE}=\sqrt{225}/\sqrt{81}=1.6667$ pikë. Varianca më e vogël e popullatës e zvogëlon SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=144$, $\operatorname{SE}=\sqrt{324}/\sqrt{144}=1.5000$ pikë. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V05: Saktësia e mesatares së kampionit për vlerësimin e besimit

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=48$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{100}=10.00$, prandaj $\operatorname{SE}=10.00/\sqrt{25}=2.0000$ pikë vlerësimi. Në kampione të përsëritura, mesataret përqendrohen te 48 pikë vlerësimi me devijim standard 2.0000 pikë vlerësimi.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 169, $\operatorname{SE}=\sqrt{169}/\sqrt{25}=2.6000$ pikë vlerësimi. Varianca më e madhe e popullatës e rrit SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=64$, $\operatorname{SE}=\sqrt{100}/\sqrt{64}=1.2500$ pikë vlerësimi. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V06: Saktësia e mesatares së kampionit për kohën e reagimit

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=480$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{2500}=50.00$, prandaj $\operatorname{SE}=50.00/\sqrt{100}=5.0000$ milisekonda. Në kampione të përsëritura, mesataret përqendrohen te 480 milisekonda me devijim standard 5.0000 milisekonda.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 1600, $\operatorname{SE}=\sqrt{1600}/\sqrt{100}=4.0000$ milisekonda. Varianca më e vogël e popullatës e zvogëlon SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=400$, $\operatorname{SE}=\sqrt{2500}/\sqrt{400}=2.5000$ milisekonda. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V07: Saktësia e mesatares së kampionit për rezultatin e sigurisë

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=59$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{121}=11.00$, prandaj $\operatorname{SE}=11.00/\sqrt{49}=1.5714$ pikë. Në kampione të përsëritura, mesataret përqendrohen te 59 pikë me devijim standard 1.5714 pikë.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 196, $\operatorname{SE}=\sqrt{196}/\sqrt{49}=2.0000$ pikë. Varianca më e madhe e popullatës e rrit SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=100$, $\operatorname{SE}=\sqrt{121}/\sqrt{100}=1.1000$ pikë. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V08: Saktësia e mesatares së kampionit për kohëzgjatjen e vizitës

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=82$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{400}=20.00$, prandaj $\operatorname{SE}=20.00/\sqrt{64}=2.5000$ minuta. Në kampione të përsëritura, mesataret përqendrohen te 82 minuta me devijim standard 2.5000 minuta.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 256, $\operatorname{SE}=\sqrt{256}/\sqrt{64}=2.0000$ minuta. Varianca më e vogël e popullatës e zvogëlon SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=144$, $\operatorname{SE}=\sqrt{400}/\sqrt{144}=1.6667$ minuta. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V09: Saktësia e mesatares së kampionit për rezultatin e saktësisë

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=88$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{81}=9.00$, prandaj $\operatorname{SE}=9.00/\sqrt{36}=1.5000$ pikë. Në kampione të përsëritura, mesataret përqendrohen te 88 pikë me devijim standard 1.5000 pikë.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 144, $\operatorname{SE}=\sqrt{144}/\sqrt{36}=2.0000$ pikë. Varianca më e madhe e popullatës e rrit SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=49$, $\operatorname{SE}=\sqrt{81}/\sqrt{49}=1.2857$ pikë. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

### T02-A12-V10: Saktësia e mesatares së kampionit për indeksin e zërit

**Arsyeto para llogaritjes, pjesa (a)**

Për një mesatare të paanshme të kampionit, $E(\bar X)=\mu=42$. Pavarësia jep $\operatorname{SD}(\bar X)=\sigma/\sqrt n$.

$\sigma=\sqrt{169}=13.00$, prandaj $\operatorname{SE}=13.00/\sqrt{25}=2.6000$ pikë indeksi. Në kampione të përsëritura, mesataret përqendrohen te 42 pikë indeksi me devijim standard 2.6000 pikë indeksi.

**Zhvillo llogaritjen, pjesa (b)**

Me variancë 100, $\operatorname{SE}=\sqrt{100}/\sqrt{25}=2.0000$ pikë indeksi. Varianca më e vogël e popullatës e zvogëlon SE-në kundrejt pjesës

**Zhvillo llogaritjen, pjesa (a)**

.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me $n=64$, $\operatorname{SE}=\sqrt{169}/\sqrt{64}=1.6250$ pikë indeksi. Madhësia më e madhe e kampionit e zvogëlon SE-në përmes rrënjës katrore të $n$. SE më e vogël do të thotë se mesataret e kampioneve të përsëritura grumbullohen më afër mesatares së popullatës.

## A13: Intervalet nën një model normal

### T02-A13-V01: Probabilitetet e intervaleve për rezultatin e përqendrimit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{81}=9.00$.

Kufijtë janë $z_a=(50-50)/9.00\approx 0.0000$ dhe $z_b=(59-50)/9.00\approx 1.0000$. Duke përdorur vlerat z të parrumbullakosura, $P(50<X\leq 59)=\Phi((59-50)/9.00)-\Phi((50-50)/9.00)=0.3413$. Prandaj modeli vendos përpjesëtimin 0.3413 të vlerave të ndryshores nga 50 deri në 59 pikë.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(43-50)/9.00\approx -0.7778$ dhe $z_d=(61-50)/9.00\approx 1.2222$, duke dhënë $P(43<X\leq 61)=\Phi((61-50)/9.00)-\Phi((43-50)/9.00)=0.6708$. Ky është përpjesëtimi i modeluar nga 43 deri në 61 pikë. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V02: Probabilitetet e intervaleve për rezultatin e leximit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{100}=10.00$.

Kufijtë janë $z_a=(65-70)/10.00\approx -0.5000$ dhe $z_b=(82-70)/10.00\approx 1.2000$. Duke përdorur vlerat z të parrumbullakosura, $P(65<X\leq 82)=\Phi((82-70)/10.00)-\Phi((65-70)/10.00)=0.5764$. Prandaj modeli vendos përpjesëtimin 0.5764 të vlerave të ndryshores nga 65 deri në 82 pikë.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(58-70)/10.00\approx -1.2000$ dhe $z_d=(76-70)/10.00\approx 0.6000$, duke dhënë $P(58<X\leq 76)=\Phi((76-70)/10.00)-\Phi((58-70)/10.00)=0.6107$. Ky është përpjesëtimi i modeluar nga 58 deri në 76 pikë. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V03: Probabilitetet e intervaleve për kohëzgjatjen e vizitës

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{225}=15.00$.

Kufijtë janë $z_a=(80-80)/15.00\approx 0.0000$ dhe $z_b=(95-80)/15.00\approx 1.0000$. Duke përdorur vlerat z të parrumbullakosura, $P(80<X\leq 95)=\Phi((95-80)/15.00)-\Phi((80-80)/15.00)=0.3413$. Prandaj modeli vendos përpjesëtimin 0.3413 të vlerave të ndryshores nga 80 deri në 95 minuta.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(62-80)/15.00\approx -1.2000$ dhe $z_d=(101-80)/15.00\approx 1.4000$, duke dhënë $P(62<X\leq 101)=\Phi((101-80)/15.00)-\Phi((62-80)/15.00)=0.8042$. Ky është përpjesëtimi i modeluar nga 62 deri në 101 minuta. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V04: Probabilitetet e intervaleve për rezultatin e kujtesës

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{144}=12.00$.

Kufijtë janë $z_a=(96-105)/12.00\approx -0.7500$ dhe $z_b=(117-105)/12.00\approx 1.0000$. Duke përdorur vlerat z të parrumbullakosura, $P(96<X\leq 117)=\Phi((117-105)/12.00)-\Phi((96-105)/12.00)=0.6147$. Prandaj modeli vendos përpjesëtimin 0.6147 të vlerave të ndryshores nga 96 deri në 117 pikë.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(88-105)/12.00\approx -1.4167$ dhe $z_d=(122-105)/12.00\approx 1.4167$, duke dhënë $P(88<X\leq 122)=\Phi((122-105)/12.00)-\Phi((88-105)/12.00)=0.8434$. Ky është përpjesëtimi i modeluar nga 88 deri në 122 pikë. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V05: Probabilitetet e intervaleve për indeksin e besimit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{64}=8.00$.

Kufijtë janë $z_a=(40-44)/8.00\approx -0.5000$ dhe $z_b=(52-44)/8.00\approx 1.0000$. Duke përdorur vlerat z të parrumbullakosura, $P(40<X\leq 52)=\Phi((52-44)/8.00)-\Phi((40-44)/8.00)=0.5328$. Prandaj modeli vendos përpjesëtimin 0.5328 të vlerave të ndryshores nga 40 deri në 52 pikë indeksi.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(33-44)/8.00\approx -1.3750$ dhe $z_d=(49-44)/8.00\approx 0.6250$, duke dhënë $P(33<X\leq 49)=\Phi((49-44)/8.00)-\Phi((33-44)/8.00)=0.6494$. Ky është përpjesëtimi i modeluar nga 33 deri në 49 pikë indeksi. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V06: Probabilitetet e intervaleve për kohën e reagimit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{2500}=50.00$.

Kufijtë janë $z_a=(475-500)/50.00\approx -0.5000$ dhe $z_b=(560-500)/50.00\approx 1.2000$. Duke përdorur vlerat z të parrumbullakosura, $P(475<X\leq 560)=\Phi((560-500)/50.00)-\Phi((475-500)/50.00)=0.5764$. Prandaj modeli vendos përpjesëtimin 0.5764 të vlerave të ndryshores nga 475 deri në 560 milisekonda.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(410-500)/50.00\approx -1.8000$ dhe $z_d=(535-500)/50.00\approx 0.7000$, duke dhënë $P(410<X\leq 535)=\Phi((535-500)/50.00)-\Phi((410-500)/50.00)=0.7221$. Ky është përpjesëtimi i modeluar nga 410 deri në 535 milisekonda. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V07: Probabilitetet e intervaleve për rezultatin e mirëqenies

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{121}=11.00$.

Kufijtë janë $z_a=(62-62)/11.00\approx 0.0000$ dhe $z_b=(74-62)/11.00\approx 1.0909$. Duke përdorur vlerat z të parrumbullakosura, $P(62<X\leq 74)=\Phi((74-62)/11.00)-\Phi((62-62)/11.00)=0.3623$. Prandaj modeli vendos përpjesëtimin 0.3623 të vlerave të ndryshores nga 62 deri në 74 pikë.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(48-62)/11.00\approx -1.2727$ dhe $z_d=(69-62)/11.00\approx 0.6364$, duke dhënë $P(48<X\leq 69)=\Phi((69-62)/11.00)-\Phi((48-62)/11.00)=0.6362$. Ky është përpjesëtimi i modeluar nga 48 deri në 69 pikë. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V08: Probabilitetet e intervaleve për rezultatin e katalogimit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{49}=7.00$.

Kufijtë janë $z_a=(81-86)/7.00\approx -0.7143$ dhe $z_b=(93-86)/7.00\approx 1.0000$. Duke përdorur vlerat z të parrumbullakosura, $P(81<X\leq 93)=\Phi((93-86)/7.00)-\Phi((81-86)/7.00)=0.6038$. Prandaj modeli vendos përpjesëtimin 0.6038 të vlerave të ndryshores nga 81 deri në 93 pikë.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(74-86)/7.00\approx -1.7143$ dhe $z_d=(90-86)/7.00\approx 0.5714$, duke dhënë $P(74<X\leq 90)=\Phi((90-86)/7.00)-\Phi((74-86)/7.00)=0.6729$. Ky është përpjesëtimi i modeluar nga 74 deri në 90 pikë. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V09: Probabilitetet e intervaleve për nivelin e zërit

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{36}=6.00$.

Kufijtë janë $z_a=(36-36)/6.00\approx 0.0000$ dhe $z_b=(42-36)/6.00\approx 1.0000$. Duke përdorur vlerat z të parrumbullakosura, $P(36<X\leq 42)=\Phi((42-36)/6.00)-\Phi((36-36)/6.00)=0.3413$. Prandaj modeli vendos përpjesëtimin 0.3413 të vlerave të ndryshores nga 36 deri në 42 decibel.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(27-36)/6.00\approx -1.5000$ dhe $z_d=(39-36)/6.00\approx 0.5000$, duke dhënë $P(27<X\leq 39)=\Phi((39-36)/6.00)-\Phi((27-36)/6.00)=0.6247$. Ky është përpjesëtimi i modeluar nga 27 deri në 39 decibel. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.

### T02-A13-V10: Probabilitetet e intervaleve për vlerësimin e sigurisë

**Përgatit llogaritjen, pjesa (a)**

Devijimi standard është $\sigma=\sqrt{64}=8.00$.

Kufijtë janë $z_a=(51-55)/8.00\approx -0.5000$ dhe $z_b=(63-55)/8.00\approx 1.0000$. Duke përdorur vlerat z të parrumbullakosura, $P(51<X\leq 63)=\Phi((63-55)/8.00)-\Phi((51-55)/8.00)=0.5328$. Prandaj modeli vendos përpjesëtimin 0.5328 të vlerave të ndryshores nga 51 deri në 63 pikë vlerësimi.

**Interpreto dhe kontrollo rezultatin, pjesa (b)**

$z_c=(43-55)/8.00\approx -1.5000$ dhe $z_d=(59-55)/8.00\approx 0.5000$, duke dhënë $P(43<X\leq 59)=\Phi((59-55)/8.00)-\Phi((43-55)/8.00)=0.6247$. Ky është përpjesëtimi i modeluar nga 43 deri në 59 pikë vlerësimi. Përfshirja e kufirit nuk e ndryshon probabilitetin e një modeli të vazhdueshëm.
