---
title: "Fleta e ushtrimeve"
subtitle: "Regresioni i shumëfishtë"
document-id: "topic-07-multiple-regression-exercises-sq"
topic-id: "topic-07-multiple-regression"
topic-number: "07"
topic-slug: "multiple-regression"
document-type: "exercises"
locale: "sq"
paired-document-id: "topic-07-multiple-regression-solutions-sq"
---

Kjo fletë përmban 90 ushtrime të organizuara në 9 grupe objektivash mësimorë. Përpiqu ta zgjidhësh secilin ushtrim para se të shikosh zgjidhjen e plotë përkatëse. Trego formulën ose rregullin përkatës, vlerat e zëvendësuara, njësitë dhe interpretimin. Të gjitha situatat, vlerat, të dhënat dhe rezultatet e programeve janë krijuar për mësim; nuk janë gjetje empirike.

# Pjesa I: Teoria

## A06: Ndërtimi i treguesve dhe gjetja e kategorisë referuese

### T07-A06-V01: Formati i tutorialit

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Formati i tutorialit» ka $k=3$ kategori: Tekst, Video, Ndërveprues. Përdor «Tekst» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_2$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e arsyetimit» është $\hat Y=61.00 + 3.50D_1 + 6.00D_2$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V02: Vendi i studimit

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Vendi i studimit» ka $k=4$ kategori: Shtëpi, Bibliotekë, Dhomë studimi, Jashtë. Përdor «Shtëpi» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_3$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e përqendrimit» është $\hat Y=54.00 + 4.00D_1 + 2.50D_2 - 1.50D_3$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V03: Kanali i vlerësimit

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Kanali i vlerësimit» ka $k=3$ kategori: Me shkrim, Audio, Video. Përdor «Me shkrim» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_2$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e rishikimit» është $\hat Y=66.00 + 2.00D_1 + 4.50D_2$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V04: Mënyra e mbajtjes së shënimeve

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Mënyra e mbajtjes së shënimeve» ka $k=4$ kategori: Letër, Tablet, Laptop, E përzier. Përdor «Letër» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_3$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e kujtesës» është $\hat Y=58.00 - 1.50D_1 - 2.50D_2 + 3.00D_3$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V05: Orari i seminarit

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Orari i seminarit» ka $k=3$ kategori: Mëngjes, Pasdite, Mbrëmje. Përdor «Mëngjes» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_2$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e vetëbesimit» është $\hat Y=49.00 + 2.50D_1 - 3.00D_2$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V06: Udhëzuesi i arkivit

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Udhëzuesi i arkivit» ka $k=4$ kategori: Listë kontrolli, Hartë, Mentor, Mjet kërkimi. Përdor «Listë kontrolli» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_3$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e gjetjes» është $\hat Y=63.00 + 1.50D_1 + 5.00D_2 + 3.00D_3$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V07: Strategjia e rishikimit

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Strategjia e rishikimit» ka $k=3$ kategori: Vetërishikim, Rishikim nga bashkëmoshatarët, Rishikim nga mësimdhënësi. Përdor «Vetërishikim» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_2$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e cilësisë» është $\hat Y=60.00 + 4.00D_1 + 7.00D_2$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V08: Rruga në muze

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Rruga në muze» ka $k=5$ kategori: Kronologjike, Tematike, Zgjedhje e lirë, E udhëhequr, Hibride. Përdor «Kronologjike» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_4$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e njohurive» është $\hat Y=57.00 + 3.00D_1 - 1.00D_2 + 5.50D_3 + 4.00D_4$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V09: Plani i studimit

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Plani i studimit» ka $k=3$ kategori: Çdo ditë, Dy herë në javë, Çdo javë. Përdor «Çdo ditë» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_2$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e kujtesës» është $\hat Y=69.00 - 2.00D_1 - 5.00D_2$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

### T07-A06-V10: Ndërfaqja e detyrës

Në një model të ndërtuar, ndryshorja parashikuese kategorike «Ndërfaqja e detyrës» ka $k=4$ kategori: Listë, Tabelë, Kalendar, Vijë kohore. Përdor «Listë» si kategori referuese dhe mbaje prerjen. Përdor $D_1$ deri te $D_3$ për të identifikuar kategoritë joreferuese sipas rendit të dhënë. Modeli i përshtatur për ndryshoren e rezultatit «pikët e përfundimit» është $\hat Y=62.00 + 2.50D_1 + 4.00D_2 + 1.00D_3$.

(a) Shëno sa tregues nevojiten dhe shpjego pse. (b) Ndërtoje tabelën e plotë të kodimit me zero dhe një për secilën kategori. (c) Gjeje rreshtin referues, llogarite vlerën e përshtatur të secilës kategori dhe interpretoje koeficientin e $D_1$ si krahasim me referencën. (d) Shpjego pse shtimi i një treguesi të veçantë për të gjitha $k$ kategoritë, duke e mbajtur prerjen, krijon varësi lineare të saktë. Përshkruaj çfarë do të ndryshonte dhe çfarë do të mbetej e pandryshuar po të zgjidhej një referencë tjetër.

# Pjesa II: Praktika me kalkulator

## A01: Leximi i ekuacionit dhe rezultatit të regresionit të shumëfishtë

### T07-A01-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 80 raste. Ndryshorja e rezultatit $Y$ quhet «pikët e arsyetimit» dhe matet me njësinë «pikë»; $X_1$ është ndryshorja parashikuese «orët e praktikës së udhëhequr», ndërsa $X_2$ është ndryshorja parashikuese «pikët e përgatitjes paraprake». Prerja e përshtatur është 38.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | 2.400 | 0.580 | 0.419 | 0.550 |
| $X_2$ | 0.310 | 0.108 | 0.292 | 0.480 |

Modeli raporton $R^2=0.370$, R-katrorin e përshtatur $R^2=0.354$, gabimin standard të rezidualeve $=5.60$ pikë dhe shkallët e lirisë reziduale $df=77$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 72 raste. Ndryshorja e rezultatit $Y$ quhet «koha e gjetjes» dhe matet me njësinë «minuta»; $X_1$ është ndryshorja parashikuese «seancat e praktikës me listë kontrolli», ndërsa $X_2$ është ndryshorja parashikuese «muajt e përvojës në arkiv». Prerja e përshtatur është 70.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | -1.750 | 0.467 | -0.407 | -0.510 |
| $X_2$ | -0.220 | 0.093 | -0.257 | -0.420 |

Modeli raporton $R^2=0.316$, R-katrorin e përshtatur $R^2=0.296$, gabimin standard të rezidualeve $=4.80$ minuta dhe shkallët e lirisë reziduale $df=69$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 95 raste. Ndryshorja e rezultatit $Y$ quhet «pikët e të kuptuarit» dhe matet me njësinë «pikë»; $X_1$ është ndryshorja parashikuese «orët javore të leximit», ndërsa $X_2$ është ndryshorja parashikuese «pikët fillestare të fjalorit». Prerja e përshtatur është 42.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | 1.850 | 0.443 | 0.383 | 0.490 |
| $X_2$ | 0.280 | 0.084 | 0.306 | 0.440 |

Modeli raporton $R^2=0.322$, R-katrorin e përshtatur $R^2=0.308$, gabimin standard të rezidualeve $=5.10$ pikë dhe shkallët e lirisë reziduale $df=92$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 68 raste. Ndryshorja e rezultatit $Y$ quhet «koha e navigimit» dhe matet me njësinë «minuta»; $X_1$ është ndryshorja parashikuese «përpjekjet për ta ushtruar rrugën», ndërsa $X_2$ është ndryshorja parashikuese «pikët e njohjes së rrugës». Prerja e përshtatur është 65.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | -2.100 | 0.519 | -0.446 | -0.530 |
| $X_2$ | -0.160 | 0.080 | -0.220 | -0.390 |

Modeli raporton $R^2=0.322$, R-katrorin e përshtatur $R^2=0.302$, gabimin standard të rezidualeve $=6.00$ minuta dhe shkallët e lirisë reziduale $df=65$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 110 raste. Ndryshorja e rezultatit $Y$ quhet «pikët e saktësisë në katalog» dhe matet me njësinë «pikë»; $X_1$ është ndryshorja parashikuese «grupet e ushtrimeve të kërkimit», ndërsa $X_2$ është ndryshorja parashikuese «pikët e njohurive paraprake të katalogut». Prerja e përshtatur është 48.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | 1.550 | 0.413 | 0.339 | 0.460 |
| $X_2$ | 0.340 | 0.107 | 0.288 | 0.430 |

Modeli raporton $R^2=0.280$, R-katrorin e përshtatur $R^2=0.266$, gabimin standard të rezidualeve $=4.60$ pikë dhe shkallët e lirisë reziduale $df=107$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 76 raste. Ndryshorja e rezultatit $Y$ quhet «pikët e vetëbesimit» dhe matet me njësinë «pikë»; $X_1$ është ndryshorja parashikuese «seancat e seminarit», ndërsa $X_2$ është ndryshorja parashikuese «pikët fillestare të vetëbesimit». Prerja e përshtatur është 30.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | 2.200 | 0.546 | 0.395 | 0.500 |
| $X_2$ | 0.450 | 0.125 | 0.352 | 0.470 |

Modeli raporton $R^2=0.363$, R-katrorin e përshtatur $R^2=0.345$, gabimin standard të rezidualeve $=5.00$ pikë dhe shkallët e lirisë reziduale $df=73$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 120 raste. Ndryshorja e rezultatit $Y$ quhet «pikët e saktësisë së detyrës» dhe matet me njësinë «pikë»; $X_1$ është ndryshorja parashikuese «blloqet pa njoftime», ndërsa $X_2$ është ndryshorja parashikuese «kohëzgjatja e gjumit në orë». Prerja e përshtatur është 55.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | 1.300 | 0.330 | 0.329 | 0.410 |
| $X_2$ | 1.150 | 0.335 | 0.288 | 0.380 |

Modeli raporton $R^2=0.244$, R-katrorin e përshtatur $R^2=0.231$, gabimin standard të rezidualeve $=4.30$ pikë dhe shkallët e lirisë reziduale $df=117$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 84 raste. Ndryshorja e rezultatit $Y$ quhet «pikët e njohurive historike» dhe matet me njësinë «pikë»; $X_1$ është ndryshorja parashikuese «vizitat në muze», ndërsa $X_2$ është ndryshorja parashikuese «pikët e njohurive paraprake të historisë». Prerja e përshtatur është 40.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | 2.650 | 0.619 | 0.411 | 0.520 |
| $X_2$ | 0.370 | 0.118 | 0.302 | 0.450 |

Modeli raporton $R^2=0.350$, R-katrorin e përshtatur $R^2=0.334$, gabimin standard të rezidualeve $=5.50$ pikë dhe shkallët e lirisë reziduale $df=81$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 92 raste. Ndryshorja e rezultatit $Y$ quhet «pikët e cilësisë së rishikimit» dhe matet me njësinë «pikë»; $X_1$ është ndryshorja parashikuese «raundet e vlerësimit nga bashkëmoshatarët», ndërsa $X_2$ është ndryshorja parashikuese «pikët fillestare të shkrimit». Prerja e përshtatur është 44.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | 2.100 | 0.507 | 0.391 | 0.480 |
| $X_2$ | 0.300 | 0.104 | 0.271 | 0.400 |

Modeli raporton $R^2=0.296$, R-katrorin e përshtatur $R^2=0.280$, gabimin standard të rezidualeve $=4.90$ pikë dhe shkallët e lirisë reziduale $df=89$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

### T07-A01-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një studim i ndërtuar përdor 88 raste. Ndryshorja e rezultatit $Y$ quhet «koha e përfundimit» dhe matet me njësinë «minuta»; $X_1$ është ndryshorja parashikuese «seancat e planifikimit», ndërsa $X_2$ është ndryshorja parashikuese «pikët e ndërlikimit të detyrës». Prerja e përshtatur është 82.000. Rezultati i përzgjedhur është:

| Termi | Vlerësimi | SE | I standardizuar | r bivariat |
| --- | --- | --- | --- | --- |
| $X_1$ | -1.900 | 0.384 | -0.430 | -0.450 |
| $X_2$ | 0.850 | 0.185 | 0.398 | 0.420 |

Modeli raporton $R^2=0.361$, R-katrorin e përshtatur $R^2=0.346$, gabimin standard të rezidualeve $=5.70$ minuta dhe shkallët e lirisë reziduale $df=85$.

(a) Shkruaje ekuacionin e përshtatur dhe shpjego si ndryshon një vlerësim i pastandardizuar nga një koeficient i standardizuar. (b) Interpretoji me kusht të dyja pjerrësitë e pastandardizuara. Përdor njësinë e rezultatit dhe shprehjen "duke e mbajtur të pandryshuar ndryshoren tjetër parashikuese". (c) Llogarite secilën statistikë $t$ si vlerësimi i pjesëtuar me gabimin e vet standard, gjeji vlerat e dyanshme $p$ dhe merr vendimin në $\alpha=.05$. (d) Interpreto $R^2$, $R^2$ të përshtatur dhe gabimin standard të rezidualeve. Pastaj shpjego pse secili koeficient i standardizuar i regresionit të shumëfishtë mund të ndryshojë nga korrelacioni i vet bivariat.

## A02: Krahasimi i një vargu të paracaktuar modelesh të ndërfutura

### T07-A02-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=70$ raste, të njëjtën ndryshore rezultati «pikët e arsyetimit» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=1840.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | orët e praktikës së udhëhequr | 1 | 0.220 |
| M2 | orët e praktikës së udhëhequr; pikët e përgatitjes paraprake | 2 | 0.370 |
| M3 | orët e praktikës së udhëhequr; pikët e përgatitjes paraprake; numri i seancave të reflektimit | 3 | 0.390 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «numri i seancave të reflektimit». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 66 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=80$ raste, të njëjtën ndryshore rezultati «koha e gjetjes» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=1320.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | seancat e praktikës me listë kontrolli | 1 | 0.280 |
| M2 | seancat e praktikës me listë kontrolli; muajt e përvojës në arkiv | 2 | 0.350 |
| M3 | seancat e praktikës me listë kontrolli; muajt e përvojës në arkiv; pikët e njohjes së katalogut | 3 | 0.351 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «pikët e njohjes së katalogut». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 76 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=60$ raste, të njëjtën ndryshore rezultati «pikët e të kuptuarit» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=1560.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | orët javore të leximit | 1 | 0.180 |
| M2 | orët javore të leximit; pikët fillestare të fjalorit | 2 | 0.310 |
| M3 | orët javore të leximit; pikët fillestare të fjalorit; numri i seancave të shënimeve | 3 | 0.360 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «numri i seancave të shënimeve». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 56 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=90$ raste, të njëjtën ndryshore rezultati «koha e navigimit» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=2100.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | përpjekjet për ta ushtruar rrugën | 1 | 0.250 |
| M2 | përpjekjet për ta ushtruar rrugën; pikët e njohjes së rrugës | 2 | 0.330 |
| M3 | përpjekjet për ta ushtruar rrugën; pikët e njohjes së rrugës; pikët e kujtimit të pikave orientuese | 3 | 0.334 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «pikët e kujtimit të pikave orientuese». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 86 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=100$ raste, të njëjtën ndryshore rezultati «pikët e saktësisë në katalog» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=1750.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | grupet e ushtrimeve të kërkimit | 1 | 0.300 |
| M2 | grupet e ushtrimeve të kërkimit; pikët e njohurive paraprake të katalogut | 2 | 0.410 |
| M3 | grupet e ushtrimeve të kërkimit; pikët e njohurive paraprake të katalogut; pikët e planifikimit të kërkimit | 3 | 0.440 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «pikët e planifikimit të kërkimit». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 96 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=55$ raste, të njëjtën ndryshore rezultati «pikët e vetëbesimit» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=980.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | seancat e seminarit | 1 | 0.160 |
| M2 | seancat e seminarit; pikët fillestare të vetëbesimit | 2 | 0.290 |
| M3 | seancat e seminarit; pikët fillestare të vetëbesimit; numri i ditarëve të reflektimit | 3 | 0.292 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «numri i ditarëve të reflektimit». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 51 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=120$ raste, të njëjtën ndryshore rezultati «pikët e saktësisë së detyrës» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=2280.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | blloqet pa njoftime | 1 | 0.210 |
| M2 | blloqet pa njoftime; kohëzgjatja e gjumit në orë | 2 | 0.340 |
| M3 | blloqet pa njoftime; kohëzgjatja e gjumit në orë; numri i pushimeve për planifikim | 3 | 0.370 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «numri i pushimeve për planifikim». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 116 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=75$ raste, të njëjtën ndryshore rezultati «pikët e njohurive historike» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=1440.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | vizitat në muze | 1 | 0.240 |
| M2 | vizitat në muze; pikët e njohurive paraprake të historisë | 2 | 0.320 |
| M3 | vizitat në muze; pikët e njohurive paraprake të historisë; numri i shënimeve për ekspozitat | 3 | 0.321 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «numri i shënimeve për ekspozitat». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 71 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=65$ raste, të njëjtën ndryshore rezultati «pikët e cilësisë së rishikimit» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=1620.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | raundet e vlerësimit nga bashkëmoshatarët | 1 | 0.190 |
| M2 | raundet e vlerësimit nga bashkëmoshatarët; pikët fillestare të shkrimit | 2 | 0.360 |
| M3 | raundet e vlerësimit nga bashkëmoshatarët; pikët fillestare të shkrimit; pikët e planit të rishikimit | 3 | 0.420 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «pikët e planit të rishikimit». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 61 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

### T07-A02-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Tri modele të ndërtuara, të përshtatura me metodën e zakonshme të katrorëve më të vegjël, përdorin të njëjtat $n=110$ raste, të njëjtën ndryshore rezultati «koha e përfundimit» dhe një prerje. Secili model vijues i përmban të gjithë termat e modelit të mëparshëm. Shuma totale e përbashkët e katrorëve është $SST=1960.0$, ndërsa $p$ shënon numrin e koeficienteve parashikues.

| Modeli | Grupi i ndryshoreve parashikuese | p | R-katrori |
| --- | --- | --- | --- |
| M1 | seancat e planifikimit | 1 | 0.270 |
| M2 | seancat e planifikimit; pikët e ndërlikimit të detyrës | 2 | 0.390 |
| M3 | seancat e planifikimit; pikët e ndërlikimit të detyrës; numri i kontrolleve të përparimit | 3 | 0.395 |

(a) Llogarite shumën e katrorëve të rezidualeve $SSE=SST(1-R^2)$ për secilin model dhe ndryshimin në $R^2$ në secilin hap pas M1. (b) Llogarite vlerën e përshtatur $R^2=1-(1-R^2)(n-1)/(n-p-1)$ për të tria modelet. (c) Përshkruaj çfarë tregojnë $R^2$ i zakonshëm dhe ai i përshtatur për shtimin e ndryshores parashikuese «numri i kontrolleve të përparimit». (d) Trajtoje M2 si modelin e kufizuar dhe M3 si modelin e pakufizuar. Shkruaji të dy ekuacionet e modeleve, formuloje hipotezën zero për koeficientin e shtuar dhe llogarite testin e rritjes $F=[(R_U^2-R_R^2)/1]/[(1-R_U^2)/(n-3-1)]$ me 1 dhe 106 shkallë lirie. Gjeje vlerën p dhe interpretoje vendimin. (e) Shpjego pse ky është një varg i vlefshëm modelesh të ndërfutura dhe pse as tabela e përshtatjes, as testi i rritjes nuk vërteton shkakësi ose performancë me të dhëna të reja.

## A03: Dallimi i testit global F nga testet t të koeficienteve

### T07-A03-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «pikët e arsyetimit» përdor $n=50$ dhe raporton $R^2=0.220$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,46}=2.80684$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| orët e praktikës së udhëhequr | 1.800 | 0.600 |
| pikët e përgatitjes paraprake | 0.220 | 0.180 |
| seancat e reflektimit | 0.120 | 0.160 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 46 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «koha e gjetjes» përdor $n=60$ dhe raporton $R^2=0.300$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,56}=2.76943$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| seancat e praktikës me listë kontrolli | -1.400 | 0.450 |
| muajt e përvojës në arkiv | -0.200 | 0.160 |
| njohja e katalogut | 0.300 | 0.120 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 56 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «pikët e të kuptuarit» përdor $n=70$ dhe raporton $R^2=0.100$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,66}=2.74371$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| orët javore të leximit | 1.100 | 0.580 |
| pikët fillestare të fjalorit | 0.180 | 0.130 |
| seancat e shënimeve | -0.150 | 0.140 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 66 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «koha e navigimit» përdor $n=80$ dhe raporton $R^2=0.250$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,76}=2.72494$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| përpjekjet për ta ushtruar rrugën | -1.800 | 0.550 |
| pikët e njohjes së rrugës | -0.120 | 0.100 |
| kujtimi i pikave orientuese | 0.280 | 0.110 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 76 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «pikët e saktësisë në katalog» përdor $n=90$ dhe raporton $R^2=0.080$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,86}=2.71065$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| grupet e ushtrimeve të kërkimit | 1.000 | 0.570 |
| pikët e njohurive paraprake të katalogut | 0.150 | 0.120 |
| planifikimi i kërkimit | 0.180 | 0.140 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 86 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «pikët e vetëbesimit» përdor $n=100$ dhe raporton $R^2=0.350$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,96}=2.69939$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| seancat e seminarit | 2.100 | 0.500 |
| pikët fillestare të vetëbesimit | 0.380 | 0.140 |
| ditarët e reflektimit | -0.100 | 0.130 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 96 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «pikët e saktësisë së detyrës» përdor $n=110$ dhe raporton $R^2=0.200$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,106}=2.69030$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| blloqet pa njoftime | 1.300 | 0.400 |
| kohëzgjatja e gjumit në orë | 0.120 | 0.110 |
| pushimet për planifikim | 0.250 | 0.150 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 106 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «pikët e njohurive historike» përdor $n=120$ dhe raporton $R^2=0.280$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,116}=2.68281$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| vizitat në muze | 2.000 | 0.480 |
| pikët e njohurive paraprake të historisë | 0.310 | 0.130 |
| shënimet për ekspozitat | 0.080 | 0.120 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 116 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «pikët e cilësisë së rishikimit» përdor $n=75$ dhe raporton $R^2=0.160$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,71}=2.73365$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| raundet e vlerësimit nga bashkëmoshatarët | 1.200 | 0.520 |
| pikët fillestare të shkrimit | 0.190 | 0.150 |
| planifikimi i rishikimit | -0.090 | 0.130 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 71 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

### T07-A03-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model i ndërtuar me tri ndryshore parashikuese për ndryshoren e rezultatit «koha e përfundimit» përdor $n=65$ dhe raporton $R^2=0.240$. Le të shënojnë $\beta_1$, $\beta_2$ dhe $\beta_3$ tri pjerrësitë e popullatës. Për $\alpha=.05$, vlera kritike e dhënë është $F_{3,61}=2.75548$. Tabela e koeficienteve është:

| Ndryshorja parashikuese | Vlerësimi | SE |
| --- | --- | --- |
| seancat e planifikimit | -1.600 | 0.500 |
| pikët e ndërlikimit të detyrës | 0.420 | 0.170 |
| kontrollet e përparimit | 0.160 | 0.140 |

(a) Shënoje hipotezën zero globale, llogarite $F=(R^2/3)/[(1-R^2)/(n-3-1)]$ dhe merr vendimin global. (b) Për secilën ndryshore parashikuese, llogarite $t=b/SE$, vlerën e saj të dyanshme $p$ me 61 shkallë lirie reziduale dhe vendimin në $\alpha=.05$. (c) Shënoje hipotezën zero për koeficientin individual dhe shpjego pse rezultati global nuk tregon se cila pjerrësi ndryshon nga zeroja. (d) Pajtoji vendimet globale dhe individuale të këtij modeli pa e trajtuar asnjërin lloj testi si provë për rëndësi, parashikim ose shkakësi.

## A04: Korrelacioni gjysmëpartial dhe rritja e R-katrorit

### T07-A04-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «pikët e arsyetimit» tashmë përmban ndryshoret parashikuese «orët e praktikës së udhëhequr» dhe «pikët e përgatitjes paraprake». Ai ka $R^2=0.300$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| seancat e reflektimit | 0.240 |
| takimet me partnerin e studimit | 0.100 |
| kontrollet e planifikimit | -0.180 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «koha e gjetjes» tashmë përmban ndryshoret parashikuese «seancat e praktikës me listë kontrolli» dhe «muajt e përvojës në arkiv». Ai ka $R^2=0.260$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| njohja e katalogut | -0.120 |
| përdorimi i hartës së tavolinës | -0.270 |
| këshillimet nga mentori | 0.080 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «pikët e të kuptuarit» tashmë përmban ndryshoret parashikuese «orët javore të leximit» dhe «pikët fillestare të fjalorit». Ai ka $R^2=0.340$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| seancat e shënimeve | 0.150 |
| postimet në diskutim | 0.310 |
| blloqet e leximit në qetësi | 0.200 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «koha e navigimit» tashmë përmban ndryshoret parashikuese «përpjekjet për ta ushtruar rrugën» dhe «pikët e njohjes së rrugës». Ai ka $R^2=0.290$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| kujtimi i pikave orientuese | -0.280 |
| kontrollet e hartës | -0.140 |
| shikimet paraprake të rrugës | 0.190 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «pikët e saktësisë në katalog» tashmë përmban ndryshoret parashikuese «grupet e ushtrimeve të kërkimit» dhe «pikët e njohurive paraprake të katalogut». Ai ka $R^2=0.370$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| planifikimi i kërkimit | 0.110 |
| ushtrimet me fjalë kyçe | 0.220 |
| udhëzimet e katalogut të përdorura | 0.290 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «pikët e vetëbesimit» tashmë përmban ndryshoret parashikuese «seancat e seminarit» dhe «pikët fillestare të vetëbesimit». Ai ka $R^2=0.320$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| ditarët e reflektimit | 0.260 |
| takimet me bashkëmoshatarët | 0.170 |
| demonstrimet praktike | -0.090 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «pikët e saktësisë së detyrës» tashmë përmban ndryshoret parashikuese «blloqet pa njoftime» dhe «kohëzgjatja e gjumit në orë». Ai ka $R^2=0.250$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| pushimet për planifikim | 0.130 |
| intervalet pa ekran | 0.210 |
| shikimet paraprake të detyrës | 0.070 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «pikët e njohurive historike» tashmë përmban ndryshoret parashikuese «vizitat në muze» dhe «pikët e njohurive paraprake të historisë». Ai ka $R^2=0.310$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| shënimet për ekspozitat | 0.180 |
| ndalesat e vizitës së udhëhequr | 0.120 |
| leximet vijuese | 0.250 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «pikët e cilësisë së rishikimit» tashmë përmban ndryshoret parashikuese «raundet e vlerësimit nga bashkëmoshatarët» dhe «pikët fillestare të shkrimit». Ai ka $R^2=0.360$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| planifikimi i rishikimit | 0.090 |
| komentet e përdorura nga bashkëmoshatarët | 0.280 |
| kalimet e redaktimit | 0.160 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

### T07-A04-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aktual i ndërtuar për ndryshoren e rezultatit «koha e përfundimit» tashmë përmban ndryshoret parashikuese «seancat e planifikimit» dhe «pikët e ndërlikimit të detyrës». Ai ka $R^2=0.280$. Secila ndryshore kandidate më poshtë është regresuar veçmas mbi këto ndryshore parashikuese aktuale. Reziduali nga ai regresion është pjesa e ndryshores kandidate që nuk parashikohet në mënyrë lineare nga grupi aktual. Tabela raporton korrelacionin mes asaj ndryshoreje kandidate të kthyer në rezidual dhe rezultatit fillestar, jo të kthyer në rezidual. Simboli $r_{sp}$ shënon këtë korrelacion gjysmëpartial:

| Ndryshorja kandidate | r gjysmëpartial |
| --- | --- |
| kontrollet e përparimit | -0.230 |
| përkujtuesit e kalendarit | -0.110 |
| shikimet paraprake të detyrës | 0.200 |

(a) Shpjego pse ky është korrelacion gjysmëpartial dhe jo korrelacion i pjesshëm. (b) Për secilën shtesë me një ndryshore kandidate, llogarite $\Delta R^2=r_{sp}^2$ dhe $R^2$ që rezulton. (c) Nëse një hap përpara përdor rritjen më të madhe, gjeje ndryshoren kandidate të zgjedhur dhe përcaktoje rritjen e saj. (d) Shpjego çfarë arsyeton dhe çfarë nuk arsyeton ky hap, duke përfshirë pse ai as nuk vërteton se ndryshorja e zgjedhur është e vërtetë ose shkakësore, as nuk garanton se do të mbetet më e mira pasi të hyjë një term tjetër.

## A05: Krahasimi i modeleve kandidate të paracaktuara me AIC

### T07-A05-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «pikët e arsyetimit». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | orët e praktikës së udhëhequr | 3 | -155.0 |
| M2 | orët e praktikës së udhëhequr + pikët e përgatitjes paraprake | 4 | -146.0 |
| M3 | orët e praktikës së udhëhequr + pikët e përgatitjes paraprake + numri i seancave të reflektimit | 5 | -142.5 |
| M4 | orët e praktikës së udhëhequr + pikët e përgatitjes paraprake + numri i seancave të reflektimit + një term prodhimi i paracaktuar | 6 | -141.9 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «pikët e përgatitjes paraprake» | 300.00 |
| Hapi 1 | shto «numri i seancave të reflektimit» | 303.20 |
| Hapi 1 | shto termin e prodhimit | 306.40 |
| Hapi 2 | ndalo pas M2 | 300.00 |
| Hapi 2 | shto «numri i seancave të reflektimit» | 295.00 |
| Hapi 2 | shto termin e prodhimit | 297.80 |
| Hapi 3 | ndalo pas M3 | 295.00 |
| Hapi 3 | shto termin e prodhimit | 295.80 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «koha e gjetjes». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | seancat e praktikës me listë kontrolli | 3 | -142.0 |
| M2 | seancat e praktikës me listë kontrolli + muajt e përvojës në arkiv | 4 | -134.0 |
| M3 | seancat e praktikës me listë kontrolli + muajt e përvojës në arkiv + pikët e njohjes së katalogut | 5 | -133.4 |
| M4 | seancat e praktikës me listë kontrolli + muajt e përvojës në arkiv + pikët e njohjes së katalogut + një term prodhimi i paracaktuar | 6 | -131.8 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «muajt e përvojës në arkiv» | 276.00 |
| Hapi 1 | shto «pikët e njohjes së katalogut» | 279.20 |
| Hapi 1 | shto termin e prodhimit | 282.40 |
| Hapi 2 | ndalo pas M2 | 276.00 |
| Hapi 2 | shto «pikët e njohjes së katalogut» | 276.80 |
| Hapi 2 | shto termin e prodhimit | 279.60 |
| Hapi 3 | ndalo pas M3 | 276.80 |
| Hapi 3 | shto termin e prodhimit | 275.60 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «pikët e të kuptuarit». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | orët javore të leximit | 3 | -180.0 |
| M2 | orët javore të leximit + pikët fillestare të fjalorit | 4 | -170.0 |
| M3 | orët javore të leximit + pikët fillestare të fjalorit + numri i seancave të shënimeve | 5 | -166.0 |
| M4 | orët javore të leximit + pikët fillestare të fjalorit + numri i seancave të shënimeve + një term prodhimi i paracaktuar | 6 | -165.5 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «pikët fillestare të fjalorit» | 348.00 |
| Hapi 1 | shto «numri i seancave të shënimeve» | 351.20 |
| Hapi 1 | shto termin e prodhimit | 354.40 |
| Hapi 2 | ndalo pas M2 | 348.00 |
| Hapi 2 | shto «numri i seancave të shënimeve» | 342.00 |
| Hapi 2 | shto termin e prodhimit | 344.80 |
| Hapi 3 | ndalo pas M3 | 342.00 |
| Hapi 3 | shto termin e prodhimit | 343.00 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «koha e navigimit». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | përpjekjet për ta ushtruar rrugën | 3 | -130.0 |
| M2 | përpjekjet për ta ushtruar rrugën + pikët e njohjes së rrugës | 4 | -126.0 |
| M3 | përpjekjet për ta ushtruar rrugën + pikët e njohjes së rrugës + pikët e kujtimit të pikave orientuese | 5 | -125.5 |
| M4 | përpjekjet për ta ushtruar rrugën + pikët e njohjes së rrugës + pikët e kujtimit të pikave orientuese + një term prodhimi i paracaktuar | 6 | -125.2 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «pikët e njohjes së rrugës» | 260.00 |
| Hapi 1 | shto «pikët e kujtimit të pikave orientuese» | 263.20 |
| Hapi 1 | shto termin e prodhimit | 266.40 |
| Hapi 2 | ndalo pas M2 | 260.00 |
| Hapi 2 | shto «pikët e kujtimit të pikave orientuese» | 261.00 |
| Hapi 2 | shto termin e prodhimit | 263.80 |
| Hapi 3 | ndalo pas M3 | 261.00 |
| Hapi 3 | shto termin e prodhimit | 262.40 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «pikët e saktësisë në katalog». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | grupet e ushtrimeve të kërkimit | 3 | -200.0 |
| M2 | grupet e ushtrimeve të kërkimit + pikët e njohurive paraprake të katalogut | 4 | -188.0 |
| M3 | grupet e ushtrimeve të kërkimit + pikët e njohurive paraprake të katalogut + pikët e planifikimit të kërkimit | 5 | -183.0 |
| M4 | grupet e ushtrimeve të kërkimit + pikët e njohurive paraprake të katalogut + pikët e planifikimit të kërkimit + një term prodhimi i paracaktuar | 6 | -180.0 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «pikët e njohurive paraprake të katalogut» | 384.00 |
| Hapi 1 | shto «pikët e planifikimit të kërkimit» | 387.20 |
| Hapi 1 | shto termin e prodhimit | 390.40 |
| Hapi 2 | ndalo pas M2 | 384.00 |
| Hapi 2 | shto «pikët e planifikimit të kërkimit» | 376.00 |
| Hapi 2 | shto termin e prodhimit | 378.80 |
| Hapi 3 | ndalo pas M3 | 376.00 |
| Hapi 3 | shto termin e prodhimit | 372.00 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «pikët e vetëbesimit». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | seancat e seminarit | 3 | -165.0 |
| M2 | seancat e seminarit + pikët fillestare të vetëbesimit | 4 | -157.0 |
| M3 | seancat e seminarit + pikët fillestare të vetëbesimit + numri i ditarëve të reflektimit | 5 | -156.4 |
| M4 | seancat e seminarit + pikët fillestare të vetëbesimit + numri i ditarëve të reflektimit + një term prodhimi i paracaktuar | 6 | -155.8 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «pikët fillestare të vetëbesimit» | 322.00 |
| Hapi 1 | shto «numri i ditarëve të reflektimit» | 325.20 |
| Hapi 1 | shto termin e prodhimit | 328.40 |
| Hapi 2 | ndalo pas M2 | 322.00 |
| Hapi 2 | shto «numri i ditarëve të reflektimit» | 322.80 |
| Hapi 2 | shto termin e prodhimit | 325.60 |
| Hapi 3 | ndalo pas M3 | 322.80 |
| Hapi 3 | shto termin e prodhimit | 323.60 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «pikët e saktësisë së detyrës». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | blloqet pa njoftime | 3 | -175.0 |
| M2 | blloqet pa njoftime + kohëzgjatja e gjumit në orë | 4 | -166.0 |
| M3 | blloqet pa njoftime + kohëzgjatja e gjumit në orë + numri i pushimeve për planifikim | 5 | -162.0 |
| M4 | blloqet pa njoftime + kohëzgjatja e gjumit në orë + numri i pushimeve për planifikim + një term prodhimi i paracaktuar | 6 | -161.2 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «kohëzgjatja e gjumit në orë» | 340.00 |
| Hapi 1 | shto «numri i pushimeve për planifikim» | 343.20 |
| Hapi 1 | shto termin e prodhimit | 346.40 |
| Hapi 2 | ndalo pas M2 | 340.00 |
| Hapi 2 | shto «numri i pushimeve për planifikim» | 334.00 |
| Hapi 2 | shto termin e prodhimit | 336.80 |
| Hapi 3 | ndalo pas M3 | 334.00 |
| Hapi 3 | shto termin e prodhimit | 334.40 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «pikët e njohurive historike». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | vizitat në muze | 3 | -145.0 |
| M2 | vizitat në muze + pikët e njohurive paraprake të historisë | 4 | -140.0 |
| M3 | vizitat në muze + pikët e njohurive paraprake të historisë + numri i shënimeve për ekspozitat | 5 | -138.0 |
| M4 | vizitat në muze + pikët e njohurive paraprake të historisë + numri i shënimeve për ekspozitat + një term prodhimi i paracaktuar | 6 | -136.4 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «pikët e njohurive paraprake të historisë» | 288.00 |
| Hapi 1 | shto «numri i shënimeve për ekspozitat» | 291.20 |
| Hapi 1 | shto termin e prodhimit | 294.40 |
| Hapi 2 | ndalo pas M2 | 288.00 |
| Hapi 2 | shto «numri i shënimeve për ekspozitat» | 286.00 |
| Hapi 2 | shto termin e prodhimit | 288.80 |
| Hapi 3 | ndalo pas M3 | 286.00 |
| Hapi 3 | shto termin e prodhimit | 284.80 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «pikët e cilësisë së rishikimit». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | raundet e vlerësimit nga bashkëmoshatarët | 3 | -190.0 |
| M2 | raundet e vlerësimit nga bashkëmoshatarët + pikët fillestare të shkrimit | 4 | -181.0 |
| M3 | raundet e vlerësimit nga bashkëmoshatarët + pikët fillestare të shkrimit + pikët e planit të rishikimit | 5 | -180.3 |
| M4 | raundet e vlerësimit nga bashkëmoshatarët + pikët fillestare të shkrimit + pikët e planit të rishikimit + një term prodhimi i paracaktuar | 6 | -179.9 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «pikët fillestare të shkrimit» | 370.00 |
| Hapi 1 | shto «pikët e planit të rishikimit» | 373.20 |
| Hapi 1 | shto termin e prodhimit | 376.40 |
| Hapi 2 | ndalo pas M2 | 370.00 |
| Hapi 2 | shto «pikët e planit të rishikimit» | 370.60 |
| Hapi 2 | shto termin e prodhimit | 373.40 |
| Hapi 3 | ndalo pas M3 | 370.60 |
| Hapi 3 | shto termin e prodhimit | 371.80 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

### T07-A05-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Katër modele kandidate të ndërtuara dhe të paracaktuara përdorin pikërisht të njëjtat raste dhe të njëjtën ndryshore rezultati «koha e përfundimit». Këtu $\log(L)$ është log-likelihood-u i maksimizuar që raporton modeli i përshtatur. Sipas marrëveshjes së shënuar, $K$ numëron të gjithë parametrat e vlerësuar që përdoren në llogaritjen e AIC-së.

| Modeli | Termat | K | Log-likelihood-u |
| --- | --- | --- | --- |
| M1 | seancat e planifikimit | 3 | -158.0 |
| M2 | seancat e planifikimit + pikët e ndërlikimit të detyrës | 4 | -149.0 |
| M3 | seancat e planifikimit + pikët e ndërlikimit të detyrës + numri i kontrolleve të përparimit | 5 | -145.0 |
| M4 | seancat e planifikimit + pikët e ndërlikimit të detyrës + numri i kontrolleve të përparimit + një term prodhimi i paracaktuar | 6 | -144.4 |

(a) Llogarite $AIC=-2\log(L)+2K$ për secilin model dhe llogarite secilën $\Delta AIC=AIC-AIC_{min}$. (b) Duke nisur nga M1, kryeje përzgjedhjen përpara me tabelën e kandidatëve për secilin hap. Në çdo hap zgjidhe AIC-në më të ulët të disponueshme vetëm nëse është më e ulët se AIC-ja e modelit aktual. Përndryshe, ndalo.

| Hapi përpara | Veprimi i mundshëm | AIC |
| --- | --- | --- |
| Hapi 1 | shto «pikët e ndërlikimit të detyrës» | 306.00 |
| Hapi 1 | shto «numri i kontrolleve të përparimit» | 309.20 |
| Hapi 1 | shto termin e prodhimit | 312.40 |
| Hapi 2 | ndalo pas M2 | 306.00 |
| Hapi 2 | shto «numri i kontrolleve të përparimit» | 300.00 |
| Hapi 2 | shto termin e prodhimit | 302.80 |
| Hapi 3 | ndalo pas M3 | 300.00 |
| Hapi 3 | shto termin e prodhimit | 300.80 |

(c) Vizatoje rrugën e AIC-së për modelet që u përzgjodhën vërtet, duke nisur me M1 në hapin 0. (d) Shkruaje formulën e modelit përfundimtar dhe interpreto çfarë u shtojnë termat e përzgjedhur lidhjeve të përshtatura. (e) Shpjego pse rruga varet nga zgjedhjet e mëparshme dhe pse modeli përfundimtar nuk vërtetohet në këtë mënyrë si i vërtetë, shkakësor ose parashikues jashtë kampionit.

## A07: Interpretimi i një modeli grupor aditiv

### T07-A07-V01: Mbështetja nga tutoriali dhe arsyetimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Pa udhëheqje» dhe $G=1$ për grupin «Me tutor»: $\hat Y=42.00+(3.00)X+(5.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e arsyetimit», ndërsa $X$ shënon ndryshoren parashikuese «orët e praktikës».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=2.0$ dhe $X=6.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V02: Përvoja në arkiv dhe gjetja

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Staf i ri» dhe $G=1$ për grupin «Staf me përvojë»: $\hat Y=36.00+(-1.80)X+(-4.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e gjetjes», ndërsa $X$ shënon ndryshoren parashikuese «seancat e praktikës».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=1.0$ dhe $X=5.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V03: Formati i leximit dhe të kuptuarit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Material i shtypur» dhe $G=1$ për grupin «Digjital»: $\hat Y=51.00+(2.20)X+(-2.50)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e të kuptuarit», ndërsa $X$ shënon ndryshoren parashikuese «orët e leximit».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=2.0$ dhe $X=7.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V04: Ndihma për rrugën dhe navigimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Hartë në letër» dhe $G=1$ për grupin «Hartë në aplikacion»: $\hat Y=44.00+(-2.00)X+(-3.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e navigimit», ndërsa $X$ shënon ndryshoren parashikuese «përpjekjet e ushtrimit».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=1.0$ dhe $X=4.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V05: Udhëzuesi i kërkimit dhe saktësia

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Pa udhëzues» dhe $G=1$ për grupin «Listë kontrolli»: $\hat Y=55.00+(2.50)X+(4.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e saktësisë», ndërsa $X$ shënon ndryshoren parashikuese «grupet e ushtrimeve».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=0.0$ dhe $X=4.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V06: Mënyra e seminarit dhe vetëbesimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Online» dhe $G=1$ për grupin «Në klasë»: $\hat Y=38.00+(3.20)X+(3.50)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e vetëbesimit», ndërsa $X$ shënon ndryshoren parashikuese «seancat e ndjekura».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=1.0$ dhe $X=5.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V07: Mjedisi i përqendrimit dhe saktësia

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Dhomë e përbashkët» dhe $G=1$ për grupin «Dhomë e qetë»: $\hat Y=60.00+(1.70)X+(4.50)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e saktësisë së detyrës», ndërsa $X$ shënon ndryshoren parashikuese «blloqet e përqendrimit».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=2.0$ dhe $X=8.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V08: Udhëzuesi i muzeut dhe njohuritë

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Pa udhëheqje» dhe $G=1$ për grupin «E udhëhequr»: $\hat Y=47.00+(4.00)X+(6.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e njohurive», ndërsa $X$ shënon ndryshoren parashikuese «vizitat».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=0.0$ dhe $X=3.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V09: Mënyra e vlerësimit dhe rishikimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Me shkrim» dhe $G=1$ për grupin «Bisedë»: $\hat Y=52.00+(3.50)X+(2.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e rishikimit», ndërsa $X$ shënon ndryshoren parashikuese «raundet e vlerësimit».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=1.0$ dhe $X=4.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

### T07-A07-V10: Formati i planifikimit dhe përfundimi

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar përdor $G=0$ për grupin «Letër» dhe $G=1$ për grupin «Digjital»: $\hat Y=70.00+(-2.40)X+(-3.50)G$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e përfundimit», ndërsa $X$ shënon ndryshoren parashikuese «seancat e planifikimit».

(a) Shkruaje ekuacionin e përshtatur për secilin grup dhe interpretoje prerjen në $X=0$, duke vënë në dukje kur zeroja mund të jetë vetëm referencë matematikore. (b) Interpretoji pjerrësinë e përbashkët të $X$ dhe koeficientin e grupit si krahasime të kushtëzuara. (c) Llogariti koordinatat e përshtatura për të dyja grupet në $X=1.0$ dhe $X=6.0$ dhe organizoji në tabelë. (d) Shpjego si tregojnë këto koordinata vija paralele dhe një largësi të pandryshueshme mes grupeve. Gjithashtu shëno pse largësia e përshtatur nuk vërteton vetvetiu efekt shkakësor të grupit.

## A08: Ndërrimi i referencës pa ndryshuar marrëdhëniet e përshtatura

### T07-A08-V01: Ndërrimi i referencës së formatit të praktikës

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Në mënyrë të pavarur» dhe $G=1$ për grupin «Me partner»: $\hat Y=40.00+(2.80)X+(4.50)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e arsyetimit», ndërsa $X$ shënon ndryshoren parashikuese «orët e praktikës». Rikodoje me $H=0$ për «Me partner» dhe $H=1$ për «Në mënyrë të pavarur».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=1.0$ dhe $X=5.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V02: Ndërrimi i referencës së rolit në arkiv

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Asistent» dhe $G=1$ për grupin «Koordinator»: $\hat Y=35.00+(-1.60)X+(-5.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e gjetjes», ndërsa $X$ shënon ndryshoren parashikuese «seancat e praktikës». Rikodoje me $H=0$ për «Koordinator» dhe $H=1$ për «Asistent».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=0.0$ dhe $X=4.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V03: Ndërrimi i referencës së mjetit të leximit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Material i shtypur» dhe $G=1$ për grupin «Audio»: $\hat Y=50.00+(2.00)X+(-3.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e të kuptuarit», ndërsa $X$ shënon ndryshoren parashikuese «orët e leximit». Rikodoje me $H=0$ për «Audio» dhe $H=1$ për «Material i shtypur».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=2.0$ dhe $X=6.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V04: Ndërrimi i referencës së ekranit të navigimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Statik» dhe $G=1$ për grupin «Ndërveprues»: $\hat Y=46.00+(-2.20)X+(-4.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e navigimit», ndërsa $X$ shënon ndryshoren parashikuese «përpjekjet e ushtrimit». Rikodoje me $H=0$ për «Ndërveprues» dhe $H=1$ për «Statik».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=1.0$ dhe $X=5.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V05: Ndërrimi i referencës së ndihmës së katalogut

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Indeks» dhe $G=1$ për grupin «Shirit kërkimi»: $\hat Y=53.00+(2.60)X+(3.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e saktësisë», ndërsa $X$ shënon ndryshoren parashikuese «grupet e ushtrimeve». Rikodoje me $H=0$ për «Shirit kërkimi» dhe $H=1$ për «Indeks».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=0.0$ dhe $X=3.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V06: Ndërrimi i referencës së mjedisit të seminarit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Online» dhe $G=1$ për grupin «Klasë»: $\hat Y=37.00+(3.00)X+(5.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e vetëbesimit», ndërsa $X$ shënon ndryshoren parashikuese «seancat». Rikodoje me $H=0$ për «Klasë» dhe $H=1$ për «Online».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=1.0$ dhe $X=4.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V07: Ndërrimi i referencës së dhomës së përqendrimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Dhomë e hapur» dhe $G=1$ për grupin «Dhomë private»: $\hat Y=59.00+(1.80)X+(4.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e saktësisë së detyrës», ndërsa $X$ shënon ndryshoren parashikuese «blloqet e përqendrimit». Rikodoje me $H=0$ për «Dhomë private» dhe $H=1$ për «Dhomë e hapur».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=2.0$ dhe $X=7.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V08: Ndërrimi i referencës së rrugës në muze

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Rrugë e lirë» dhe $G=1$ për grupin «Rrugë e përzgjedhur»: $\hat Y=45.00+(4.20)X+(6.50)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e njohurive», ndërsa $X$ shënon ndryshoren parashikuese «vizitat». Rikodoje me $H=0$ për «Rrugë e përzgjedhur» dhe $H=1$ për «Rrugë e lirë».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=0.0$ dhe $X=3.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V09: Ndërrimi i referencës së takimit për rishikim

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Asinkron» dhe $G=1$ për grupin «Drejtpërdrejt»: $\hat Y=51.00+(3.40)X+(2.50)G$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e rishikimit», ndërsa $X$ shënon ndryshoren parashikuese «raundet e vlerësimit». Rikodoje me $H=0$ për «Drejtpërdrejt» dhe $H=1$ për «Asinkron».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=1.0$ dhe $X=5.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

### T07-A08-V10: Ndërrimi i referencës së mjetit të planifikimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model aditiv i ndërtuar kodon $G=0$ për grupin «Fletore» dhe $G=1$ për grupin «Kalendar»: $\hat Y=72.00+(-2.50)X+(-4.00)G$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e përfundimit», ndërsa $X$ shënon ndryshoren parashikuese «seancat e planifikimit». Rikodoje me $H=0$ për «Kalendar» dhe $H=1$ për «Fletore».

(a) Nxirre prerjen e re, pjerrësinë e re të $X$ dhe koeficientin e $H$. (b) Shkruaji të dy ekuacionet e grupeve me kodimin e ri dhe interpretoje koeficientin e ri të grupit. (c) Në $X=1.0$ dhe $X=6.0$, llogariti vlerat e përshtatura nga të dy parametrizimet për të dyja grupet dhe vendosi krah për krah. (d) Përdori llogaritjet për të shpjeguar pse ndërrimi i referencës e ndryshon sistemin koordinativ të koeficienteve, por nuk mund t'i ndryshojë vlerat e përshtatura, rezidualet ose vijat e përshtatura të grupeve.

## A09: Interpretimi i ndërveprimit mes grupit dhe ndryshores parashikuese sasiore

### T07-A09-V01: Orët e praktikës sipas mbështetjes nga tutoriali

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Pa udhëheqje», $G=1$ për grupin «Me tutor» dhe prodhimin $XG$: $\hat Y=40.00+(2.00)X+(4.00)G+(1.20)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e arsyetimit», ndërsa $X$ shënon ndryshoren parashikuese «orët e praktikës».

(a) Ndërtoji rreshtat për të dyja grupet në $X=1.0$ dhe $X=5.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V02: Seancat e praktikës sipas rolit në arkiv

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Staf i ri», $G=1$ për grupin «Staf me përvojë» dhe prodhimin $XG$: $\hat Y=38.00+(-1.20)X+(-3.00)G+(-0.80)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e gjetjes», ndërsa $X$ shënon ndryshoren parashikuese «seancat e praktikës».

(a) Ndërtoji rreshtat për të dyja grupet në $X=0.0$ dhe $X=4.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V03: Orët e leximit sipas mjetit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Material i shtypur», $G=1$ për grupin «Audio» dhe prodhimin $XG$: $\hat Y=49.00+(2.60)X+(2.00)G+(-1.00)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e të kuptuarit», ndërsa $X$ shënon ndryshoren parashikuese «orët e leximit».

(a) Ndërtoji rreshtat për të dyja grupet në $X=2.0$ dhe $X=6.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V04: Ushtrimi sipas ekranit të navigimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Statik», $G=1$ për grupin «Ndërveprues» dhe prodhimin $XG$: $\hat Y=48.00+(-1.50)X+(-2.00)G+(-0.90)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e navigimit», ndërsa $X$ shënon ndryshoren parashikuese «përpjekjet e ushtrimit».

(a) Ndërtoji rreshtat për të dyja grupet në $X=1.0$ dhe $X=5.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V05: Grupet e ushtrimeve sipas ndihmës së katalogut

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Indeks», $G=1$ për grupin «Shirit kërkimi» dhe prodhimin $XG$: $\hat Y=52.00+(2.00)X+(3.00)G+(0.70)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e saktësisë», ndërsa $X$ shënon ndryshoren parashikuese «grupet e ushtrimeve».

(a) Ndërtoji rreshtat për të dyja grupet në $X=0.0$ dhe $X=4.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V06: Seancat sipas mjedisit të seminarit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Online», $G=1$ për grupin «Klasë» dhe prodhimin $XG$: $\hat Y=36.00+(2.40)X+(5.00)G+(0.80)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e vetëbesimit», ndërsa $X$ shënon ndryshoren parashikuese «seancat».

(a) Ndërtoji rreshtat për të dyja grupet në $X=1.0$ dhe $X=5.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V07: Blloqet e përqendrimit sipas llojit të dhomës

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Dhomë e hapur», $G=1$ për grupin «Dhomë private» dhe prodhimin $XG$: $\hat Y=58.00+(2.10)X+(4.00)G+(-0.60)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e saktësisë së detyrës», ndërsa $X$ shënon ndryshoren parashikuese «blloqet e përqendrimit».

(a) Ndërtoji rreshtat për të dyja grupet në $X=2.0$ dhe $X=7.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V08: Vizitat sipas rrugës në muze

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Rrugë e lirë», $G=1$ për grupin «Rrugë e përzgjedhur» dhe prodhimin $XG$: $\hat Y=44.00+(3.50)X+(3.00)G+(1.50)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e njohurive», ndërsa $X$ shënon ndryshoren parashikuese «vizitat».

(a) Ndërtoji rreshtat për të dyja grupet në $X=0.0$ dhe $X=3.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V09: Raundet e vlerësimit sipas mënyrës së takimit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Asinkron», $G=1$ për grupin «Drejtpërdrejt» dhe prodhimin $XG$: $\hat Y=50.00+(2.80)X+(4.00)G+(-0.50)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «pikët e rishikimit», ndërsa $X$ shënon ndryshoren parashikuese «raundet e vlerësimit».

(a) Ndërtoji rreshtat për të dyja grupet në $X=1.0$ dhe $X=5.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.

### T07-A09-V10: Planifikimi sipas llojit të mjetit

**Arsyeto fillimisht.** Para llogaritjes, thuaj lidhjen, rregullin ose modelin e pritur që e bën llogaritjen të përshtatshme.

Një model ndërveprimi i ndërtuar përdor $G=0$ për grupin «Fletore», $G=1$ për grupin «Kalendar» dhe prodhimin $XG$: $\hat Y=74.00+(-1.80)X+(-2.00)G+(-0.90)XG$. Këtu $Y$ shënon ndryshoren e rezultatit «koha e përfundimit», ndërsa $X$ shënon ndryshoren parashikuese «seancat e planifikimit».

(a) Ndërtoji rreshtat për të dyja grupet në $X=1.0$ dhe $X=6.0$, duke paraqitur $G$ dhe $XG$. (b) Nxirre prerjen dhe pjerrësinë e kushtëzuar të secilit grup. (c) Llogariti katër koordinatat e përshtatura dhe organizoji të gjitha madhësitë në një tabelë. (d) Vizatoji dy vijat e përshtatura nga këto koordinata në një grafik të vetëm të emërtuar dhe shënoje largësinë e përshtatur mes grupeve në të dyja vlerat e paraqitura të $X$. (e) Interpretoji $b_1$, $b_2$ dhe $b_3$ në kushtet e tyre të duhura referuese, shpjego si e ndryshon $b_3$ largësinë mes grupeve përgjatë $X$ dhe shëno pse një ndërveprim nuk është vetvetiu provë shkakësore.
