---
title: "Zgjidhjet e plota"
subtitle: "Regresioni i shumëfishtë"
document-id: "topic-07-multiple-regression-solutions-sq"
topic-id: "topic-07-multiple-regression"
topic-number: "07"
topic-slug: "multiple-regression"
document-type: "solutions"
locale: "sq"
paired-document-id: "topic-07-multiple-regression-exercises-sq"
---

Këto zgjidhje të plota përdorin të njëjtat kode dhe të njëjtën renditje si Fleta e ushtrimeve. Vlerat ndërmjetëse ruhen deri te hapi i treguar i rrumbullakimit, prandaj aty ku shënohet pranohen dallime të vogla që vijnë nga rrumbullakimi më i hershëm. Të gjitha situatat, vlerat, të dhënat dhe rezultatet e programeve janë krijuar për mësim; nuk janë gjetje empirike.

# Pjesa I: Teoria

## A06: Ndërtimi i treguesve dhe gjetja e kategorisë referuese

### T07-A06-V01: Formati i tutorialit

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=2$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Video) | $D_2$ (Ndërveprues) |
| --- | --- | --- |
| Tekst | 0 | 0 |
| Video | 1 | 0 |
| Ndërveprues | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Tekst» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e arsyetimit» |
| --- | --- |
| Tekst | 61.00 |
| Video | 64.50 |
| Ndërveprues | 67.00 |

Koeficienti i $D_1$ është 3.50. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e arsyetimit» për kategorinë «Video» është 3.50 pikë më e lartë se për kategorinë referuese «Tekst». Prerja 61.00 është vlera e përshtatur për «Tekst».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V02: Vendi i studimit

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=3$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Bibliotekë) | $D_2$ (Dhomë studimi) | $D_3$ (Jashtë) |
| --- | --- | --- | --- |
| Shtëpi | 0 | 0 | 0 |
| Bibliotekë | 1 | 0 | 0 |
| Dhomë studimi | 0 | 1 | 0 |
| Jashtë | 0 | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Shtëpi» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e përqendrimit» |
| --- | --- |
| Shtëpi | 54.00 |
| Bibliotekë | 58.00 |
| Dhomë studimi | 56.50 |
| Jashtë | 52.50 |

Koeficienti i $D_1$ është 4.00. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e përqendrimit» për kategorinë «Bibliotekë» është 4.00 pikë më e lartë se për kategorinë referuese «Shtëpi». Prerja 54.00 është vlera e përshtatur për «Shtëpi».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V03: Kanali i vlerësimit

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=2$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Audio) | $D_2$ (Video) |
| --- | --- | --- |
| Me shkrim | 0 | 0 |
| Audio | 1 | 0 |
| Video | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Me shkrim» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e rishikimit» |
| --- | --- |
| Me shkrim | 66.00 |
| Audio | 68.00 |
| Video | 70.50 |

Koeficienti i $D_1$ është 2.00. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e rishikimit» për kategorinë «Audio» është 2.00 pikë më e lartë se për kategorinë referuese «Me shkrim». Prerja 66.00 është vlera e përshtatur për «Me shkrim».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V04: Mënyra e mbajtjes së shënimeve

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=3$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Tablet) | $D_2$ (Laptop) | $D_3$ (E përzier) |
| --- | --- | --- | --- |
| Letër | 0 | 0 | 0 |
| Tablet | 1 | 0 | 0 |
| Laptop | 0 | 1 | 0 |
| E përzier | 0 | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Letër» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e kujtesës» |
| --- | --- |
| Letër | 58.00 |
| Tablet | 56.50 |
| Laptop | 55.50 |
| E përzier | 61.00 |

Koeficienti i $D_1$ është -1.50. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e kujtesës» për kategorinë «Tablet» është 1.50 pikë më e ulët se për kategorinë referuese «Letër». Prerja 58.00 është vlera e përshtatur për «Letër».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V05: Orari i seminarit

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=2$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Pasdite) | $D_2$ (Mbrëmje) |
| --- | --- | --- |
| Mëngjes | 0 | 0 |
| Pasdite | 1 | 0 |
| Mbrëmje | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Mëngjes» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e vetëbesimit» |
| --- | --- |
| Mëngjes | 49.00 |
| Pasdite | 51.50 |
| Mbrëmje | 46.00 |

Koeficienti i $D_1$ është 2.50. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e vetëbesimit» për kategorinë «Pasdite» është 2.50 pikë më e lartë se për kategorinë referuese «Mëngjes». Prerja 49.00 është vlera e përshtatur për «Mëngjes».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V06: Udhëzuesi i arkivit

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=3$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Hartë) | $D_2$ (Mentor) | $D_3$ (Mjet kërkimi) |
| --- | --- | --- | --- |
| Listë kontrolli | 0 | 0 | 0 |
| Hartë | 1 | 0 | 0 |
| Mentor | 0 | 1 | 0 |
| Mjet kërkimi | 0 | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Listë kontrolli» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e gjetjes» |
| --- | --- |
| Listë kontrolli | 63.00 |
| Hartë | 64.50 |
| Mentor | 68.00 |
| Mjet kërkimi | 66.00 |

Koeficienti i $D_1$ është 1.50. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e gjetjes» për kategorinë «Hartë» është 1.50 pikë më e lartë se për kategorinë referuese «Listë kontrolli». Prerja 63.00 është vlera e përshtatur për «Listë kontrolli».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V07: Strategjia e rishikimit

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=2$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Rishikim nga bashkëmoshatarët) | $D_2$ (Rishikim nga mësimdhënësi) |
| --- | --- | --- |
| Vetërishikim | 0 | 0 |
| Rishikim nga bashkëmoshatarët | 1 | 0 |
| Rishikim nga mësimdhënësi | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Vetërishikim» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e cilësisë» |
| --- | --- |
| Vetërishikim | 60.00 |
| Rishikim nga bashkëmoshatarët | 64.00 |
| Rishikim nga mësimdhënësi | 67.00 |

Koeficienti i $D_1$ është 4.00. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e cilësisë» për kategorinë «Rishikim nga bashkëmoshatarët» është 4.00 pikë më e lartë se për kategorinë referuese «Vetërishikim». Prerja 60.00 është vlera e përshtatur për «Vetërishikim».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V08: Rruga në muze

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=4$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Tematike) | $D_2$ (Zgjedhje e lirë) | $D_3$ (E udhëhequr) | $D_4$ (Hibride) |
| --- | --- | --- | --- | --- |
| Kronologjike | 0 | 0 | 0 | 0 |
| Tematike | 1 | 0 | 0 | 0 |
| Zgjedhje e lirë | 0 | 1 | 0 | 0 |
| E udhëhequr | 0 | 0 | 1 | 0 |
| Hibride | 0 | 0 | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Kronologjike» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e njohurive» |
| --- | --- |
| Kronologjike | 57.00 |
| Tematike | 60.00 |
| Zgjedhje e lirë | 56.00 |
| E udhëhequr | 62.50 |
| Hibride | 61.00 |

Koeficienti i $D_1$ është 3.00. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e njohurive» për kategorinë «Tematike» është 3.00 pikë më e lartë se për kategorinë referuese «Kronologjike». Prerja 57.00 është vlera e përshtatur për «Kronologjike».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V09: Plani i studimit

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=2$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Dy herë në javë) | $D_2$ (Çdo javë) |
| --- | --- | --- |
| Çdo ditë | 0 | 0 |
| Dy herë në javë | 1 | 0 |
| Çdo javë | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Çdo ditë» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e kujtesës» |
| --- | --- |
| Çdo ditë | 69.00 |
| Dy herë në javë | 67.00 |
| Çdo javë | 64.00 |

Koeficienti i $D_1$ është -2.00. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e kujtesës» për kategorinë «Dy herë në javë» është 2.00 pikë më e ulët se për kategorinë referuese «Çdo ditë». Prerja 69.00 është vlera e përshtatur për «Çdo ditë».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

### T07-A06-V10: Ndërfaqja e detyrës

**Përcakto çështjen, pjesa (a)**

Me një prerje nevojiten $k-1=3$ tregues. Kategoria e lënë jashtë përfaqësohet nga prerja dhe bëhet baza e krahasimit.

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Kodimi i plotë është:

| Kategoria | $D_1$ (Tabelë) | $D_2$ (Kalendar) | $D_3$ (Vijë kohore) |
| --- | --- | --- | --- |
| Listë | 0 | 0 | 0 |
| Tabelë | 1 | 0 | 0 |
| Kalendar | 0 | 1 | 0 |
| Vijë kohore | 0 | 0 | 1 |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Kategoria «Listë» është referenca sepse çdo tregues është zero në atë rresht. Vlerat e përshtatura të kategorive janë:

| Kategoria | Vlera e përshtatur e ndryshores «pikët e përfundimit» |
| --- | --- |
| Listë | 62.00 |
| Tabelë | 64.50 |
| Kalendar | 66.00 |
| Vijë kohore | 63.00 |

Koeficienti i $D_1$ është 2.50. Prandaj, vlera e përshtatur e ndryshores së rezultatit «pikët e përfundimit» për kategorinë «Tabelë» është 2.50 pikë më e lartë se për kategorinë referuese «Listë». Prerja 62.00 është vlera e përshtatur për «Listë».

**Jep përfundimin dhe kufijtë e tij, pjesa (d)**

Për secilin rast, $k$ treguesit e kategorive do të jepnin shumën saktësisht një, e cila tashmë është kolona e prerjes. Përfshirja e të gjithë treguesve bashkë me prerjen e bën njërën kolonë kombinim të saktë të kolonave të tjera, prandaj koeficientët nuk mund të përcaktohen në mënyrë unike. Zgjedhja e një reference tjetër e ndryshon prerjen dhe kontrastet e kategorive që paraqiten, por nuk e ndryshon vlerën e përshtatur të asnjë kategorie.

# Pjesa II: Praktika me kalkulator

## A01: Leximi i ekuacionit dhe rezultatit të regresionit të shumëfishtë

### T07-A01-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=38.000+(2.400)X_1+(0.310)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «pikët e përgatitjes paraprake», një rritje me një njësi e ndryshores parashikuese «orët e praktikës së udhëhequr» lidhet me një ndryshim të përshtatur prej 2.400 pikësh në ndryshoren e rezultatit «pikët e arsyetimit». Duke e mbajtur të pandryshuar ndryshoren parashikuese «orët e praktikës së udhëhequr», një rritje me një njësi e ndryshores parashikuese «pikët e përgatitjes paraprake» lidhet me një ndryshim të përshtatur prej 0.310 pikësh. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=2.400/0.580=4.136$ me 77 shkallë lirie, që jep $p < 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=0.310/0.108=2.879$, që jep $p = 0.0052$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.370$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 37.0% të ndryshueshmërisë në kampion të ndryshores së rezultatit «pikët e arsyetimit». R-katrori i përshtatur $R^2=0.354$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 5.60 pikë nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara 0.419 dhe 0.292 ndryshojnë nga korrelacionet bivariate 0.550 dhe 0.480, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=70.000+(-1.750)X_1+(-0.220)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «muajt e përvojës në arkiv», një rritje me një njësi e ndryshores parashikuese «seancat e praktikës me listë kontrolli» lidhet me një ndryshim të përshtatur prej -1.750 minutash në ndryshoren e rezultatit «koha e gjetjes». Duke e mbajtur të pandryshuar ndryshoren parashikuese «seancat e praktikës me listë kontrolli», një rritje me një njësi e ndryshores parashikuese «muajt e përvojës në arkiv» lidhet me një ndryshim të përshtatur prej -0.220 minutash. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=-1.750/0.467=-3.747$ me 69 shkallë lirie, që jep $p = 0.0004$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=-0.220/0.093=-2.366$, që jep $p = 0.0208$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.316$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 31.6% të ndryshueshmërisë në kampion të ndryshores së rezultatit «koha e gjetjes». R-katrori i përshtatur $R^2=0.296$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 4.80 minuta nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara -0.407 dhe -0.257 ndryshojnë nga korrelacionet bivariate -0.510 dhe -0.420, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=42.000+(1.850)X_1+(0.280)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «pikët fillestare të fjalorit», një rritje me një njësi e ndryshores parashikuese «orët javore të leximit» lidhet me një ndryshim të përshtatur prej 1.850 pikësh në ndryshoren e rezultatit «pikët e të kuptuarit». Duke e mbajtur të pandryshuar ndryshoren parashikuese «orët javore të leximit», një rritje me një njësi e ndryshores parashikuese «pikët fillestare të fjalorit» lidhet me një ndryshim të përshtatur prej 0.280 pikësh. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=1.850/0.443=4.179$ me 92 shkallë lirie, që jep $p < 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=0.280/0.084=3.340$, që jep $p = 0.0012$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.322$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 32.2% të ndryshueshmërisë në kampion të ndryshores së rezultatit «pikët e të kuptuarit». R-katrori i përshtatur $R^2=0.308$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 5.10 pikë nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara 0.383 dhe 0.306 ndryshojnë nga korrelacionet bivariate 0.490 dhe 0.440, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=65.000+(-2.100)X_1+(-0.160)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «pikët e njohjes së rrugës», një rritje me një njësi e ndryshores parashikuese «përpjekjet për ta ushtruar rrugën» lidhet me një ndryshim të përshtatur prej -2.100 minutash në ndryshoren e rezultatit «koha e navigimit». Duke e mbajtur të pandryshuar ndryshoren parashikuese «përpjekjet për ta ushtruar rrugën», një rritje me një njësi e ndryshores parashikuese «pikët e njohjes së rrugës» lidhet me një ndryshim të përshtatur prej -0.160 minutash. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=-2.100/0.519=-4.043$ me 65 shkallë lirie, që jep $p = 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=-0.160/0.080=-1.997$, që jep $p = 0.0500$; prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.322$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 32.2% të ndryshueshmërisë në kampion të ndryshores së rezultatit «koha e navigimit». R-katrori i përshtatur $R^2=0.302$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 6.00 minuta nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara -0.446 dhe -0.220 ndryshojnë nga korrelacionet bivariate -0.530 dhe -0.390, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=48.000+(1.550)X_1+(0.340)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «pikët e njohurive paraprake të katalogut», një rritje me një njësi e ndryshores parashikuese «grupet e ushtrimeve të kërkimit» lidhet me një ndryshim të përshtatur prej 1.550 pikësh në ndryshoren e rezultatit «pikët e saktësisë në katalog». Duke e mbajtur të pandryshuar ndryshoren parashikuese «grupet e ushtrimeve të kërkimit», një rritje me një njësi e ndryshores parashikuese «pikët e njohurive paraprake të katalogut» lidhet me një ndryshim të përshtatur prej 0.340 pikësh. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=1.550/0.413=3.752$ me 107 shkallë lirie, që jep $p = 0.0003$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=0.340/0.107=3.180$, që jep $p = 0.0019$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.280$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 28.0% të ndryshueshmërisë në kampion të ndryshores së rezultatit «pikët e saktësisë në katalog». R-katrori i përshtatur $R^2=0.266$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 4.60 pikë nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara 0.339 dhe 0.288 ndryshojnë nga korrelacionet bivariate 0.460 dhe 0.430, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=30.000+(2.200)X_1+(0.450)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «pikët fillestare të vetëbesimit», një rritje me një njësi e ndryshores parashikuese «seancat e seminarit» lidhet me një ndryshim të përshtatur prej 2.200 pikësh në ndryshoren e rezultatit «pikët e vetëbesimit». Duke e mbajtur të pandryshuar ndryshoren parashikuese «seancat e seminarit», një rritje me një njësi e ndryshores parashikuese «pikët fillestare të vetëbesimit» lidhet me një ndryshim të përshtatur prej 0.450 pikësh. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=2.200/0.546=4.027$ me 73 shkallë lirie, që jep $p = 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=0.450/0.125=3.590$, që jep $p = 0.0006$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.363$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 36.3% të ndryshueshmërisë në kampion të ndryshores së rezultatit «pikët e vetëbesimit». R-katrori i përshtatur $R^2=0.345$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 5.00 pikë nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara 0.395 dhe 0.352 ndryshojnë nga korrelacionet bivariate 0.500 dhe 0.470, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=55.000+(1.300)X_1+(1.150)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «kohëzgjatja e gjumit në orë», një rritje me një njësi e ndryshores parashikuese «blloqet pa njoftime» lidhet me një ndryshim të përshtatur prej 1.300 pikësh në ndryshoren e rezultatit «pikët e saktësisë së detyrës». Duke e mbajtur të pandryshuar ndryshoren parashikuese «blloqet pa njoftime», një rritje me një njësi e ndryshores parashikuese «kohëzgjatja e gjumit në orë» lidhet me një ndryshim të përshtatur prej 1.150 pikësh. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=1.300/0.330=3.935$ me 117 shkallë lirie, që jep $p = 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=1.150/0.335=3.438$, që jep $p = 0.0008$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.244$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 24.4% të ndryshueshmërisë në kampion të ndryshores së rezultatit «pikët e saktësisë së detyrës». R-katrori i përshtatur $R^2=0.231$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 4.30 pikë nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara 0.329 dhe 0.288 ndryshojnë nga korrelacionet bivariate 0.410 dhe 0.380, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=40.000+(2.650)X_1+(0.370)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «pikët e njohurive paraprake të historisë», një rritje me një njësi e ndryshores parashikuese «vizitat në muze» lidhet me një ndryshim të përshtatur prej 2.650 pikësh në ndryshoren e rezultatit «pikët e njohurive historike». Duke e mbajtur të pandryshuar ndryshoren parashikuese «vizitat në muze», një rritje me një njësi e ndryshores parashikuese «pikët e njohurive paraprake të historisë» lidhet me një ndryshim të përshtatur prej 0.370 pikësh. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=2.650/0.619=4.283$ me 81 shkallë lirie, që jep $p < 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=0.370/0.118=3.144$, që jep $p = 0.0023$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.350$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 35.0% të ndryshueshmërisë në kampion të ndryshores së rezultatit «pikët e njohurive historike». R-katrori i përshtatur $R^2=0.334$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 5.50 pikë nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara 0.411 dhe 0.302 ndryshojnë nga korrelacionet bivariate 0.520 dhe 0.450, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=44.000+(2.100)X_1+(0.300)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «pikët fillestare të shkrimit», një rritje me një njësi e ndryshores parashikuese «raundet e vlerësimit nga bashkëmoshatarët» lidhet me një ndryshim të përshtatur prej 2.100 pikësh në ndryshoren e rezultatit «pikët e cilësisë së rishikimit». Duke e mbajtur të pandryshuar ndryshoren parashikuese «raundet e vlerësimit nga bashkëmoshatarët», një rritje me një njësi e ndryshores parashikuese «pikët fillestare të shkrimit» lidhet me një ndryshim të përshtatur prej 0.300 pikësh. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=2.100/0.507=4.145$ me 89 shkallë lirie, që jep $p < 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=0.300/0.104=2.877$, që jep $p = 0.0050$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.296$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 29.6% të ndryshueshmërisë në kampion të ndryshores së rezultatit «pikët e cilësisë së rishikimit». R-katrori i përshtatur $R^2=0.280$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 4.90 pikë nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara 0.391 dhe 0.271 ndryshojnë nga korrelacionet bivariate 0.480 dhe 0.400, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

### T07-A01-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto para llogaritjes, pjesa (a)**

Ekuacioni i përshtatur është $\hat Y=82.000+(-1.900)X_1+(0.850)X_2$. Një pjerrësi e pastandardizuar përdor njësitë fillestare të matjes. Një koeficient i standardizuar përshkruan ndryshimin e përshtatur në devijime standarde të rezultatit kur ndryshorja parashikuese rritet me një devijim standard, duke u kushtëzuar nga ndryshorja tjetër parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Duke e mbajtur të pandryshuar ndryshoren parashikuese «pikët e ndërlikimit të detyrës», një rritje me një njësi e ndryshores parashikuese «seancat e planifikimit» lidhet me një ndryshim të përshtatur prej -1.900 minutash në ndryshoren e rezultatit «koha e përfundimit». Duke e mbajtur të pandryshuar ndryshoren parashikuese «seancat e planifikimit», një rritje me një njësi e ndryshores parashikuese «pikët e ndërlikimit të detyrës» lidhet me një ndryshim të përshtatur prej 0.850 minutash. Këto janë lidhje të kushtëzuara, jo automatikisht efekte shkakësore.

**Zhvillo llogaritjen, pjesa (c)**

Për $X_1$, $t=-1.900/0.384=-4.954$ me 85 shkallë lirie, që jep $p < 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë në $\alpha=.05$. Për $X_2$, $t=0.850/0.185=4.590$, që jep $p < 0.0001$; prandaj hipoteza zero për koeficientin hidhet poshtë. Secili test ka të bëjë me atë koeficient të vetëm të popullatës, duke u kushtëzuar nga pikërisht termi tjetër në këtë model.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

$R^2=0.361$ do të thotë se modeli i përshtatur me dy ndryshore parashikuese paraqet 36.1% të ndryshueshmërisë në kampion të ndryshores së rezultatit «koha e përfundimit». R-katrori i përshtatur $R^2=0.346$ vendos një dënim brenda kampionit për vlerësimin e dy pjerrësive. Nuk është test me të dhëna të reja. Gabimi standard i rezidualeve tregon se, sipas modelit, rezultatet e vëzhguara zakonisht largohen me rreth 5.70 minuta nga vlerat e tyre të përshtatura. Pjerrësitë e standardizuara -0.430 dhe 0.398 ndryshojnë nga korrelacionet bivariate -0.450 dhe 0.420, sepse secila pjerrësi e ndan marrëdhënien e kushtëzuar të një ndryshoreje parashikuese nga ndryshueshmëria që ajo ndan me ndryshoren tjetër parashikuese.

## A02: Krahasimi i një vargu të paracaktuar modelesh të ndërfutura

### T07-A02-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=1840.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 1435.20 | nuk është hap vijues | 0.2085 |
| M2 | 1159.20 | 0.150 | 0.3512 |
| M3 | 1122.40 | 0.020 | 0.3623 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.370 në 0.390 kur shtohet ndryshorja parashikuese «numri i seancave të reflektimit». Rritja është 0.020, ose 2.0 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur rritet nga 0.3512 në 0.3623, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «numri i seancave të reflektimit»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.390-0.370)/1]/[(1-0.390)/(70-3-1)]=2.1639$ me 1 dhe 66 shkallë lirie. Vlera p është 0.1460, prandaj termi i shtuar nuk e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=1320.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 950.40 | nuk është hap vijues | 0.2708 |
| M2 | 858.00 | 0.070 | 0.3331 |
| M3 | 856.68 | 0.001 | 0.3254 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.350 në 0.351 kur shtohet ndryshorja parashikuese «pikët e njohjes së katalogut». Rritja është 0.001, ose 0.1 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur zvogëlohet nga 0.3331 në 0.3254, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «pikët e njohjes së katalogut»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.351-0.350)/1]/[(1-0.351)/(80-3-1)]=0.1171$ me 1 dhe 76 shkallë lirie. Vlera p është 0.7331, prandaj termi i shtuar nuk e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=1560.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 1279.20 | nuk është hap vijues | 0.1659 |
| M2 | 1076.40 | 0.130 | 0.2858 |
| M3 | 998.40 | 0.050 | 0.3257 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.310 në 0.360 kur shtohet ndryshorja parashikuese «numri i seancave të shënimeve». Rritja është 0.050, ose 5.0 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur rritet nga 0.2858 në 0.3257, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «numri i seancave të shënimeve»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.360-0.310)/1]/[(1-0.360)/(60-3-1)]=4.3750$ me 1 dhe 56 shkallë lirie. Vlera p është 0.0410, prandaj termi i shtuar e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=2100.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 1575.00 | nuk është hap vijues | 0.2415 |
| M2 | 1407.00 | 0.080 | 0.3146 |
| M3 | 1398.60 | 0.004 | 0.3108 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.330 në 0.334 kur shtohet ndryshorja parashikuese «pikët e kujtimit të pikave orientuese». Rritja është 0.004, ose 0.4 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur zvogëlohet nga 0.3146 në 0.3108, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «pikët e kujtimit të pikave orientuese»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.334-0.330)/1]/[(1-0.334)/(90-3-1)]=0.5165$ me 1 dhe 86 shkallë lirie. Vlera p është 0.4743, prandaj termi i shtuar nuk e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=1750.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 1225.00 | nuk është hap vijues | 0.2929 |
| M2 | 1032.50 | 0.110 | 0.3978 |
| M3 | 980.00 | 0.030 | 0.4225 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.410 në 0.440 kur shtohet ndryshorja parashikuese «pikët e planifikimit të kërkimit». Rritja është 0.030, ose 3.0 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur rritet nga 0.3978 në 0.4225, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «pikët e planifikimit të kërkimit»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.440-0.410)/1]/[(1-0.440)/(100-3-1)]=5.1429$ me 1 dhe 96 shkallë lirie. Vlera p është 0.0256, prandaj termi i shtuar e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=980.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 823.20 | nuk është hap vijues | 0.1442 |
| M2 | 695.80 | 0.130 | 0.2627 |
| M3 | 693.84 | 0.002 | 0.2504 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.290 në 0.292 kur shtohet ndryshorja parashikuese «numri i ditarëve të reflektimit». Rritja është 0.002, ose 0.2 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur zvogëlohet nga 0.2627 në 0.2504, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «numri i ditarëve të reflektimit»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.292-0.290)/1]/[(1-0.292)/(55-3-1)]=0.1441$ me 1 dhe 51 shkallë lirie. Vlera p është 0.7058, prandaj termi i shtuar nuk e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=2280.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 1801.20 | nuk është hap vijues | 0.2033 |
| M2 | 1504.80 | 0.130 | 0.3287 |
| M3 | 1436.40 | 0.030 | 0.3537 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.340 në 0.370 kur shtohet ndryshorja parashikuese «numri i pushimeve për planifikim». Rritja është 0.030, ose 3.0 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur rritet nga 0.3287 në 0.3537, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «numri i pushimeve për planifikim»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.370-0.340)/1]/[(1-0.370)/(120-3-1)]=5.5238$ me 1 dhe 116 shkallë lirie. Vlera p është 0.0204, prandaj termi i shtuar e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=1440.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 1094.40 | nuk është hap vijues | 0.2296 |
| M2 | 979.20 | 0.080 | 0.3011 |
| M3 | 977.76 | 0.001 | 0.2923 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.320 në 0.321 kur shtohet ndryshorja parashikuese «numri i shënimeve për ekspozitat». Rritja është 0.001, ose 0.1 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur zvogëlohet nga 0.3011 në 0.2923, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «numri i shënimeve për ekspozitat»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.321-0.320)/1]/[(1-0.321)/(75-3-1)]=0.1046$ me 1 dhe 71 shkallë lirie. Vlera p është 0.7474, prandaj termi i shtuar nuk e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=1620.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 1312.20 | nuk është hap vijues | 0.1771 |
| M2 | 1036.80 | 0.170 | 0.3394 |
| M3 | 939.60 | 0.060 | 0.3915 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.360 në 0.420 kur shtohet ndryshorja parashikuese «pikët e planit të rishikimit». Rritja është 0.060, ose 6.0 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur rritet nga 0.3394 në 0.3915, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «pikët e planit të rishikimit»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.420-0.360)/1]/[(1-0.420)/(65-3-1)]=6.3103$ me 1 dhe 61 shkallë lirie. Vlera p është 0.0147, prandaj termi i shtuar e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

### T07-A02-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto para llogaritjes, pjesa (a)**

Zbato $SSE=1960.0(1-R^2)$ dhe zbrit vlerat e njëpasnjëshme të $R^2$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësoje numrin e ndryshoreve parashikuese të secilit model në formulën e përshtatur:

| Modeli | SSE | Ndryshimi në R-katror | R-katrori i përshtatur |
| --- | --- | --- | --- |
| M1 | 1430.80 | nuk është hap vijues | 0.2632 |
| M2 | 1195.60 | 0.120 | 0.3786 |
| M3 | 1185.80 | 0.005 | 0.3779 |

**Zhvillo llogaritjen, pjesa (c)**

$R^2$ i zakonshëm rritet nga 0.390 në 0.395 kur shtohet ndryshorja parashikuese «numri i kontrolleve të përparimit». Rritja është 0.005, ose 0.5 pikë përqindjeje të ndryshueshmërisë në kampion. $R^2$ i zakonshëm nuk mund të zvogëlohet kur këtij modeli me të njëjtat raste dhe të njëjtën prerje i shtohet një ndryshore parashikuese. $R^2$ i përshtatur zvogëlohet nga 0.3786 në 0.3779, sepse e peshon përshtatjen shtesë kundrejt pjerrësisë shtesë të vlerësuar. Kjo masë e përshtatur është përshkruese dhe vlen vetëm brenda kampionit.

**Zhvillo llogaritjen, pjesa (d)**

Ekuacioni i kufizuar është $Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$. Ekuacioni i pakufizuar shton ndryshoren parashikuese «numri i kontrolleve të përparimit»: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\varepsilon$. Hipoteza zero është $H_0:\beta_3=0$, duke u kushtëzuar nga termat që gjenden tashmë në M2. Statistika e rritjes është $F=[(0.395-0.390)/1]/[(1-0.395)/(110-3-1)]=0.8760$ me 1 dhe 106 shkallë lirie. Vlera p është 0.3514, prandaj termi i shtuar nuk e plotëson kriterin 5%.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

M1 përfshihet në M2 dhe M2 përfshihet në M3: vendosja në zero e secilit koeficient të saposhtuar e rikrijon modelin e mëparshëm. Edhe ndryshorja e rezultatit, rastet dhe prerja mbeten të njëjta, prandaj ndryshimet e përshtatjes mund të krahasohen si hapa të ndërfutur. Ky varg nuk i cakton rastësisht ndryshoret parashikuese, nuk i përjashton ndryshoret e lëna jashtë, nuk vërteton mekanizëm dhe nuk mat parashikimin për raste të reja. Këto pyetje kërkojnë informacion për dizajnin dhe vlerësim të veçantë.

## A03: Dallimi i testit global F nga testet t të koeficienteve

### T07-A03-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.220/3)/[(1-0.220)/46]=4.325$. Meqë 4.325 është më e madhe se 2.80684, hipoteza zero globale hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: orët e praktikës së udhëhequr: $t=1.800/0.600=3.000$, $p = 0.0043$, prandaj hipoteza zero për koeficientin hidhet poshtë; pikët e përgatitjes paraprake: $t=0.220/0.180=1.222$, $p = 0.2278$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; seancat e reflektimit: $t=0.120/0.160=0.750$, $p = 0.4571$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Në 1 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.300/3)/[(1-0.300)/56]=8.000$. Meqë 8.000 është më e madhe se 2.76943, hipoteza zero globale hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: seancat e praktikës me listë kontrolli: $t=-1.400/0.450=-3.111$, $p = 0.0029$, prandaj hipoteza zero për koeficientin hidhet poshtë; muajt e përvojës në arkiv: $t=-0.200/0.160=-1.250$, $p = 0.2165$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; njohja e katalogut: $t=0.300/0.120=2.500$, $p = 0.0154$, prandaj hipoteza zero për koeficientin hidhet poshtë. Në 2 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.100/3)/[(1-0.100)/66]=2.444$. Meqë 2.444 është jo më e madhe se 2.74371, hipoteza zero globale nuk hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: orët javore të leximit: $t=1.100/0.580=1.897$, $p = 0.0623$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; pikët fillestare të fjalorit: $t=0.180/0.130=1.385$, $p = 0.1708$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; seancat e shënimeve: $t=-0.150/0.140=-1.071$, $p = 0.2879$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Në 0 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.250/3)/[(1-0.250)/76]=8.444$. Meqë 8.444 është më e madhe se 2.72494, hipoteza zero globale hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: përpjekjet për ta ushtruar rrugën: $t=-1.800/0.550=-3.273$, $p = 0.0016$, prandaj hipoteza zero për koeficientin hidhet poshtë; pikët e njohjes së rrugës: $t=-0.120/0.100=-1.200$, $p = 0.2339$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; kujtimi i pikave orientuese: $t=0.280/0.110=2.545$, $p = 0.0129$, prandaj hipoteza zero për koeficientin hidhet poshtë. Në 2 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.080/3)/[(1-0.080)/86]=2.493$. Meqë 2.493 është jo më e madhe se 2.71065, hipoteza zero globale nuk hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: grupet e ushtrimeve të kërkimit: $t=1.000/0.570=1.754$, $p = 0.0829$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; pikët e njohurive paraprake të katalogut: $t=0.150/0.120=1.250$, $p = 0.2147$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; planifikimi i kërkimit: $t=0.180/0.140=1.286$, $p = 0.2020$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Në 0 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.350/3)/[(1-0.350)/96]=17.231$. Meqë 17.231 është më e madhe se 2.69939, hipoteza zero globale hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: seancat e seminarit: $t=2.100/0.500=4.200$, $p < 0.0001$, prandaj hipoteza zero për koeficientin hidhet poshtë; pikët fillestare të vetëbesimit: $t=0.380/0.140=2.714$, $p = 0.0079$, prandaj hipoteza zero për koeficientin hidhet poshtë; ditarët e reflektimit: $t=-0.100/0.130=-0.769$, $p = 0.4436$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Në 2 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.200/3)/[(1-0.200)/106]=8.833$. Meqë 8.833 është më e madhe se 2.69030, hipoteza zero globale hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: blloqet pa njoftime: $t=1.300/0.400=3.250$, $p = 0.0015$, prandaj hipoteza zero për koeficientin hidhet poshtë; kohëzgjatja e gjumit në orë: $t=0.120/0.110=1.091$, $p = 0.2778$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; pushimet për planifikim: $t=0.250/0.150=1.667$, $p = 0.0985$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Në 1 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.280/3)/[(1-0.280)/116]=15.037$. Meqë 15.037 është më e madhe se 2.68281, hipoteza zero globale hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: vizitat në muze: $t=2.000/0.480=4.167$, $p < 0.0001$, prandaj hipoteza zero për koeficientin hidhet poshtë; pikët e njohurive paraprake të historisë: $t=0.310/0.130=2.385$, $p = 0.0187$, prandaj hipoteza zero për koeficientin hidhet poshtë; shënimet për ekspozitat: $t=0.080/0.120=0.667$, $p = 0.5063$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Në 2 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.160/3)/[(1-0.160)/71]=4.508$. Meqë 4.508 është më e madhe se 2.73365, hipoteza zero globale hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: raundet e vlerësimit nga bashkëmoshatarët: $t=1.200/0.520=2.308$, $p = 0.0239$, prandaj hipoteza zero për koeficientin hidhet poshtë; pikët fillestare të shkrimit: $t=0.190/0.150=1.267$, $p = 0.2094$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë; planifikimi i rishikimit: $t=-0.090/0.130=-0.692$, $p = 0.4910$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Në 1 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

### T07-A03-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto para llogaritjes, pjesa (a)**

Hipoteza zero globale është $H_0:\beta_1=\beta_2=\beta_3=0$. Statistika është $F=(0.240/3)/[(1-0.240)/61]=6.421$. Meqë 6.421 është më e madhe se 2.75548, hipoteza zero globale hidhet poshtë në $\alpha=.05$.

**Zhvillo llogaritjen, pjesa (b)**

Llogaritjet e koeficienteve janë: seancat e planifikimit: $t=-1.600/0.500=-3.200$, $p = 0.0022$, prandaj hipoteza zero për koeficientin hidhet poshtë; pikët e ndërlikimit të detyrës: $t=0.420/0.170=2.471$, $p = 0.0163$, prandaj hipoteza zero për koeficientin hidhet poshtë; kontrollet e përparimit: $t=0.160/0.140=1.143$, $p = 0.2576$, prandaj hipoteza zero për koeficientin nuk hidhet poshtë. Në 2 nga tri testet e paraqitura, hipoteza zero individuale hidhet poshtë në nivelin e shënuar.

**Zhvillo llogaritjen, pjesa (c)**

Për ndryshoren parashikuese $X_j$, hipoteza zero individuale është $H_0:\beta_j=0$, duke u kushtëzuar nga çdo term tjetër pikërisht në këtë model. Testi global bën një pyetje të përbashkët për të tria pjerrësitë. Hedhja poshtë e saj tregon se, sipas modelit, të paktën një pjerrësi e popullatës përveç prerjes ndryshon nga zeroja, por statistika globale nuk e emërton ndryshoren parashikuese. Moshedhja poshtë nuk është provë se çdo pjerrësi e popullatës është zero.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Dy llojet e vendimeve mund të ndryshojnë sepse testi global i vlerëson ndryshoret parashikuese së bashku, ndërsa secili test $t$ izolon një koeficient të kushtëzuar dhe pasigurinë e tij. Ndryshueshmëria e përbashkët e ndryshoreve parashikuese mund t'i zmadhojë gabimet standarde individuale edhe kur grupi parashikues ka vlerë shpjeguese së bashku. Anasjelltas, ndryshueshmëria e kampionit mund të japë një vlerë të vogël individuale p në një model, testi global i të cilit nuk hidhet poshtë. Vlera p nuk mat madhësinë e efektit, vlerën praktike, parashikimin e ardhshëm ose shkakësinë.

## A04: Korrelacioni gjysmëpartial dhe rritja e R-katrorit

### T07-A04-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| seancat e reflektimit | 0.240 | 0.0576 | 0.3576 |
| takimet me partnerin e studimit | 0.100 | 0.0100 | 0.3100 |
| kontrollet e planifikimit | -0.180 | 0.0324 | 0.3324 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0576, për seancat e reflektimit. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.300 në 0.3576.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| njohja e katalogut | -0.120 | 0.0144 | 0.2744 |
| përdorimi i hartës së tavolinës | -0.270 | 0.0729 | 0.3329 |
| këshillimet nga mentori | 0.080 | 0.0064 | 0.2664 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0729, për përdorimi i hartës së tavolinës. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.260 në 0.3329.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| seancat e shënimeve | 0.150 | 0.0225 | 0.3625 |
| postimet në diskutim | 0.310 | 0.0961 | 0.4361 |
| blloqet e leximit në qetësi | 0.200 | 0.0400 | 0.3800 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0961, për postimet në diskutim. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.340 në 0.4361.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| kujtimi i pikave orientuese | -0.280 | 0.0784 | 0.3684 |
| kontrollet e hartës | -0.140 | 0.0196 | 0.3096 |
| shikimet paraprake të rrugës | 0.190 | 0.0361 | 0.3261 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0784, për kujtimi i pikave orientuese. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.290 në 0.3684.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| planifikimi i kërkimit | 0.110 | 0.0121 | 0.3821 |
| ushtrimet me fjalë kyçe | 0.220 | 0.0484 | 0.4184 |
| udhëzimet e katalogut të përdorura | 0.290 | 0.0841 | 0.4541 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0841, për udhëzimet e katalogut të përdorura. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.370 në 0.4541.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| ditarët e reflektimit | 0.260 | 0.0676 | 0.3876 |
| takimet me bashkëmoshatarët | 0.170 | 0.0289 | 0.3489 |
| demonstrimet praktike | -0.090 | 0.0081 | 0.3281 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0676, për ditarët e reflektimit. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.320 në 0.3876.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| pushimet për planifikim | 0.130 | 0.0169 | 0.2669 |
| intervalet pa ekran | 0.210 | 0.0441 | 0.2941 |
| shikimet paraprake të detyrës | 0.070 | 0.0049 | 0.2549 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0441, për intervalet pa ekran. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.250 në 0.2941.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| shënimet për ekspozitat | 0.180 | 0.0324 | 0.3424 |
| ndalesat e vizitës së udhëhequr | 0.120 | 0.0144 | 0.3244 |
| leximet vijuese | 0.250 | 0.0625 | 0.3725 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0625, për leximet vijuese. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.310 në 0.3725.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| planifikimi i rishikimit | 0.090 | 0.0081 | 0.3681 |
| komentet e përdorura nga bashkëmoshatarët | 0.280 | 0.0784 | 0.4384 |
| kalimet e redaktimit | 0.160 | 0.0256 | 0.3856 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0784, për komentet e përdorura nga bashkëmoshatarët. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.360 në 0.4384.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

### T07-A04-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto para llogaritjes, pjesa (a)**

Secila ndryshore kandidate kthehet në rezidual kundrejt ndryshoreve parashikuese aktuale, por rezultati mbetet në formën e tij fillestare. Ky kthim në rezidual vetëm nga njëra anë përkufizon korrelacionin gjysmëpartial. Korrelacioni i pjesshëm do t'i kthente në reziduale si ndryshoren kandidate, ashtu edhe rezultatin kundrejt grupit aktual të ndryshoreve parashikuese.

**Zhvillo llogaritjen, pjesa (b)**

Katrori i secilit korrelacion gjysmëpartial jep rritjen nga një ndryshore parashikuese:

| Ndryshorja kandidate | r gjysmëpartial | Rritja në R-katror | R-katrori i ri |
| --- | --- | --- | --- |
| kontrollet e përparimit | -0.230 | 0.0529 | 0.3329 |
| përkujtuesit e kalendarit | -0.110 | 0.0121 | 0.2921 |
| shikimet paraprake të detyrës | 0.200 | 0.0400 | 0.3200 |

**Zhvillo llogaritjen, pjesa (c)**

Korrelacioni gjysmëpartial më i madh në katror është 0.0529, për kontrollet e përparimit. Një rregull përpara i bazuar vetëm në ndryshoret kandidate të paraqitura do ta shtonte së pari atë ndryshore parashikuese, duke e rritur $R^2$ e kampionit nga 0.280 në 0.3329.

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Hapi i rendit këto tri ndryshore kandidate sipas ndryshueshmërisë shtesë në kampion që shpjegon secila pas ndryshoreve parashikuese aktuale. Katrori e heq shenjën, prandaj shenja e $r_{sp}$ mbetet e rëndësishme për drejtimin e lidhjes edhe pse nuk ndikon në $\Delta R^2$. Renditja kushtëzohet nga modeli, ndryshoret kandidate dhe kampioni aktual. Pasi hyn një ndryshore tjetër parashikuese, ndryshueshmëria e përbashkët e ndryshon atë që mbetet në secilën ndryshore tjetër kandidate. Përzgjedhja nuk vërteton të vërtetën, efektin shkakësor, rëndësinë përmbajtësore ose performancën me të dhëna të reja.

## A05: Krahasimi i modeleve kandidate të paracaktuara me AIC

### T07-A05-V01: Praktika e udhëhequr dhe arsyetimi

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-155.0)+2(3)=316.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 316.00 | 21.00 |
| M2 | 300.00 | 5.00 |
| M3 | 295.00 | 0.00 |
| M4 | 295.80 | 0.80 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 300.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 316.00 e M1. Në hapin 2 përzgjidhet M3, sepse AIC-ja e tij është më e ulët se vlera aktuale e M2. Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 316.00), (1, 300.00), (2, 295.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `pikët e arsyetimit ~ orët e praktikës së udhëhequr + pikët e përgatitjes paraprake + numri i seancave të reflektimit`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V02: Rrjedha e punës në arkiv dhe koha e gjetjes

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-142.0)+2(3)=290.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 290.00 | 14.40 |
| M2 | 276.00 | 0.40 |
| M3 | 276.80 | 1.20 |
| M4 | 275.60 | 0.00 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 276.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 290.00 e M1. Në hapin 2 ndalohet, sepse asnjë shtesë nuk ka AIC më të ulët se vlera aktuale e M2. Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 290.00), (1, 276.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `koha e gjetjes ~ seancat e praktikës me listë kontrolli + muajt e përvojës në arkiv`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V03: Rutinat e leximit dhe të kuptuarit

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-180.0)+2(3)=366.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 366.00 | 24.00 |
| M2 | 348.00 | 6.00 |
| M3 | 342.00 | 0.00 |
| M4 | 343.00 | 1.00 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 348.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 366.00 e M1. Në hapin 2 përzgjidhet M3, sepse AIC-ja e tij është më e ulët se vlera aktuale e M2. Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 366.00), (1, 348.00), (2, 342.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `pikët e të kuptuarit ~ orët javore të leximit + pikët fillestare të fjalorit + numri i seancave të shënimeve`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V04: Ushtrimi i rrugës dhe koha e navigimit

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-130.0)+2(3)=266.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 266.00 | 6.00 |
| M2 | 260.00 | 0.00 |
| M3 | 261.00 | 1.00 |
| M4 | 262.40 | 2.40 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 260.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 266.00 e M1. Në hapin 2 ndalohet, sepse asnjë shtesë nuk ka AIC më të ulët se vlera aktuale e M2. Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 266.00), (1, 260.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `koha e navigimit ~ përpjekjet për ta ushtruar rrugën + pikët e njohjes së rrugës`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V05: Praktika e kërkimit dhe saktësia në katalog

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-200.0)+2(3)=406.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 406.00 | 34.00 |
| M2 | 384.00 | 12.00 |
| M3 | 376.00 | 4.00 |
| M4 | 372.00 | 0.00 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 384.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 406.00 e M1. Në hapin 2 përzgjidhet M3, sepse AIC-ja e tij është më e ulët se vlera aktuale e M2. Më pas, në hapin 3 përzgjidhet M4, sepse AIC-ja e tij është më e ulët se ajo e M3.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 406.00), (1, 384.00), (2, 376.00), (3, 372.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `pikët e saktësisë në katalog ~ grupet e ushtrimeve të kërkimit + pikët e njohurive paraprake të katalogut + pikët e planifikimit të kërkimit + një term prodhimi i paracaktuar`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-165.0)+2(3)=336.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 336.00 | 14.00 |
| M2 | 322.00 | 0.00 |
| M3 | 322.80 | 0.80 |
| M4 | 323.60 | 1.60 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 322.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 336.00 e M1. Në hapin 2 ndalohet, sepse asnjë shtesë nuk ka AIC më të ulët se vlera aktuale e M2. Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 336.00), (1, 322.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `pikët e vetëbesimit ~ seancat e seminarit + pikët fillestare të vetëbesimit`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V07: Blloqet e përqendrimit dhe saktësia e detyrës

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-175.0)+2(3)=356.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 356.00 | 22.00 |
| M2 | 340.00 | 6.00 |
| M3 | 334.00 | 0.00 |
| M4 | 334.40 | 0.40 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 340.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 356.00 e M1. Në hapin 2 përzgjidhet M3, sepse AIC-ja e tij është më e ulët se vlera aktuale e M2. Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 356.00), (1, 340.00), (2, 334.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `pikët e saktësisë së detyrës ~ blloqet pa njoftime + kohëzgjatja e gjumit në orë + numri i pushimeve për planifikim`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V08: Vizitat në muze dhe njohuritë historike

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-145.0)+2(3)=296.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 296.00 | 11.20 |
| M2 | 288.00 | 3.20 |
| M3 | 286.00 | 1.20 |
| M4 | 284.80 | 0.00 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 288.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 296.00 e M1. Në hapin 2 përzgjidhet M3, sepse AIC-ja e tij është më e ulët se vlera aktuale e M2. Më pas, në hapin 3 përzgjidhet M4, sepse AIC-ja e tij është më e ulët se ajo e M3.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 296.00), (1, 288.00), (2, 286.00), (3, 284.80). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `pikët e njohurive historike ~ vizitat në muze + pikët e njohurive paraprake të historisë + numri i shënimeve për ekspozitat + një term prodhimi i paracaktuar`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V09: Vlerësimi nga bashkëmoshatarët dhe cilësia e rishikimit

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-190.0)+2(3)=386.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 386.00 | 16.00 |
| M2 | 370.00 | 0.00 |
| M3 | 370.60 | 0.60 |
| M4 | 371.80 | 1.80 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 370.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 386.00 e M1. Në hapin 2 ndalohet, sepse asnjë shtesë nuk ka AIC më të ulët se vlera aktuale e M2. Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 386.00), (1, 370.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `pikët e cilësisë së rishikimit ~ raundet e vlerësimit nga bashkëmoshatarët + pikët fillestare të shkrimit`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

### T07-A05-V10: Seancat e planifikimit dhe koha e përfundimit

**Arsyeto para llogaritjes, pjesa (a)**

Për shembull, M1 jep $-2(-158.0)+2(3)=322.00$. Zbatimi i të njëjtit rregull për të katër modelet jep:

| Modeli | AIC | Delta AIC |
| --- | --- | --- |
| M1 | 322.00 | 22.00 |
| M2 | 306.00 | 6.00 |
| M3 | 300.00 | 0.00 |
| M4 | 300.80 | 0.80 |

**Zhvillo llogaritjen, pjesa (b)**

Në hapin 1 përzgjidhet M2, sepse 306.00 është më e ulët se vlerat e tjera të paraqitura në hapin 1 dhe më e ulët se vlera 322.00 e M1. Në hapin 2 përzgjidhet M3, sepse AIC-ja e tij është më e ulët se vlera aktuale e M2. Në këtë rrugë përpara nuk përzgjidhet më vonë asnjë term prodhimi.

**Zhvillo llogaritjen, pjesa (c)**

Koordinatat e rrugës së përzgjedhur janë (0, 322.00), (1, 306.00), (2, 300.00). Vendose hapin në boshtin horizontal dhe AIC-në në boshtin vertikal. Lidhi vetëm modelet e njëpasnjëshme që u përzgjodhën dhe përfundo aty ku ndalon rregulli. Segmentet zbritëse tregojnë përmirësime të baraspeshës relative mes përshtatjes dhe ndërlikimit përgjatë pikërisht kësaj rruge.

**Zhvillo llogaritjen, pjesa (d)**

Formula përfundimtare e përzgjedhur është `koha e përfundimit ~ seancat e planifikimit + pikët e ndërlikimit të detyrës + numri i kontrolleve të përparimit`. Termat e saj përshkruajnë lidhje të kushtëzuara të përshtatura për këtë ndryshore rezultati dhe këto raste. Vetëm ata nuk përcaktojnë shkaqe.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Në një rrugë përpara, zgjedhja rillogaritet pas çdo termi të përzgjedhur. Prandaj, një shtesë që duket e dobishme në një hap mund të bëhet e tepërt në një hap të mëvonshëm. Rruga mund të ndalojë edhe para se të arrijë AIC-në më të ulët në tërësi mes kombinimeve që zgjedhjet e mëparshme nuk i bënë kurrë të arritshme. AIC-ja shpërblen përshtatjen, por shton një dënim për ndërlikimin. Nuk vërteton se modeli i përzgjedhur është e vërteta që ka prodhuar të dhënat ose se parashikimet e tij do të përgjithësohen. Performanca me të dhëna të reja kërkon vlerësim të veçantë. Vlerat AIC për ndryshore të ndryshme rezultati ose grupe të ndryshme rastesh nuk përbëjnë një familje të përbashkët modelesh kandidate për krahasim.

## A07: Interpretimi i një modeli grupor aditiv

### T07-A07-V01: Mbështetja nga tutoriali dhe arsyetimi

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Pa udhëheqje», vendos $G=0$: $\hat Y=42.00+(3.00)X$. Për grupin «Me tutor», vendos $G=1$: $\hat Y=47.00+(3.00)X$. Prerja 42.00 është vlera e përshtatur e ndryshores së rezultatit «pikët e arsyetimit» për grupin «Pa udhëheqje», kur ndryshorja parashikuese «orët e praktikës» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «orët e praktikës» lidhet me një ndryshim të përshtatur prej 3.00 njësish në ndryshoren e rezultatit «pikët e arsyetimit». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Me tutor» është 5.00 njësi më lart se për grupin «Pa udhëheqje». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «pikët e arsyetimit» |
| --- | --- | --- |
| Pa udhëheqje | 2.0 | 48.00 |
| Pa udhëheqje | 6.0 | 60.00 |
| Me tutor | 2.0 | 53.00 |
| Me tutor | 6.0 | 65.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi 3.00, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me 5.00 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V02: Përvoja në arkiv dhe gjetja

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Staf i ri», vendos $G=0$: $\hat Y=36.00+(-1.80)X$. Për grupin «Staf me përvojë», vendos $G=1$: $\hat Y=32.00+(-1.80)X$. Prerja 36.00 është vlera e përshtatur e ndryshores së rezultatit «koha e gjetjes» për grupin «Staf i ri», kur ndryshorja parashikuese «seancat e praktikës» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «seancat e praktikës» lidhet me një ndryshim të përshtatur prej -1.80 njësish në ndryshoren e rezultatit «koha e gjetjes». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Staf me përvojë» është 4.00 njësi më poshtë se për grupin «Staf i ri». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «koha e gjetjes» |
| --- | --- | --- |
| Staf i ri | 1.0 | 34.20 |
| Staf i ri | 5.0 | 27.00 |
| Staf me përvojë | 1.0 | 30.20 |
| Staf me përvojë | 5.0 | 23.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi -1.80, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me -4.00 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V03: Formati i leximit dhe të kuptuarit

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Material i shtypur», vendos $G=0$: $\hat Y=51.00+(2.20)X$. Për grupin «Digjital», vendos $G=1$: $\hat Y=48.50+(2.20)X$. Prerja 51.00 është vlera e përshtatur e ndryshores së rezultatit «pikët e të kuptuarit» për grupin «Material i shtypur», kur ndryshorja parashikuese «orët e leximit» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «orët e leximit» lidhet me një ndryshim të përshtatur prej 2.20 njësish në ndryshoren e rezultatit «pikët e të kuptuarit». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Digjital» është 2.50 njësi më poshtë se për grupin «Material i shtypur». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «pikët e të kuptuarit» |
| --- | --- | --- |
| Material i shtypur | 2.0 | 55.40 |
| Material i shtypur | 7.0 | 66.40 |
| Digjital | 2.0 | 52.90 |
| Digjital | 7.0 | 63.90 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi 2.20, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me -2.50 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V04: Ndihma për rrugën dhe navigimi

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Hartë në letër», vendos $G=0$: $\hat Y=44.00+(-2.00)X$. Për grupin «Hartë në aplikacion», vendos $G=1$: $\hat Y=41.00+(-2.00)X$. Prerja 44.00 është vlera e përshtatur e ndryshores së rezultatit «koha e navigimit» për grupin «Hartë në letër», kur ndryshorja parashikuese «përpjekjet e ushtrimit» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «përpjekjet e ushtrimit» lidhet me një ndryshim të përshtatur prej -2.00 njësish në ndryshoren e rezultatit «koha e navigimit». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Hartë në aplikacion» është 3.00 njësi më poshtë se për grupin «Hartë në letër». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «koha e navigimit» |
| --- | --- | --- |
| Hartë në letër | 1.0 | 42.00 |
| Hartë në letër | 4.0 | 36.00 |
| Hartë në aplikacion | 1.0 | 39.00 |
| Hartë në aplikacion | 4.0 | 33.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi -2.00, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me -3.00 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V05: Udhëzuesi i kërkimit dhe saktësia

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Pa udhëzues», vendos $G=0$: $\hat Y=55.00+(2.50)X$. Për grupin «Listë kontrolli», vendos $G=1$: $\hat Y=59.00+(2.50)X$. Prerja 55.00 është vlera e përshtatur e ndryshores së rezultatit «pikët e saktësisë» për grupin «Pa udhëzues», kur ndryshorja parashikuese «grupet e ushtrimeve» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «grupet e ushtrimeve» lidhet me një ndryshim të përshtatur prej 2.50 njësish në ndryshoren e rezultatit «pikët e saktësisë». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Listë kontrolli» është 4.00 njësi më lart se për grupin «Pa udhëzues». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «pikët e saktësisë» |
| --- | --- | --- |
| Pa udhëzues | 0.0 | 55.00 |
| Pa udhëzues | 4.0 | 65.00 |
| Listë kontrolli | 0.0 | 59.00 |
| Listë kontrolli | 4.0 | 69.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi 2.50, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me 4.00 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V06: Mënyra e seminarit dhe vetëbesimi

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Online», vendos $G=0$: $\hat Y=38.00+(3.20)X$. Për grupin «Në klasë», vendos $G=1$: $\hat Y=41.50+(3.20)X$. Prerja 38.00 është vlera e përshtatur e ndryshores së rezultatit «pikët e vetëbesimit» për grupin «Online», kur ndryshorja parashikuese «seancat e ndjekura» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «seancat e ndjekura» lidhet me një ndryshim të përshtatur prej 3.20 njësish në ndryshoren e rezultatit «pikët e vetëbesimit». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Në klasë» është 3.50 njësi më lart se për grupin «Online». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «pikët e vetëbesimit» |
| --- | --- | --- |
| Online | 1.0 | 41.20 |
| Online | 5.0 | 54.00 |
| Në klasë | 1.0 | 44.70 |
| Në klasë | 5.0 | 57.50 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi 3.20, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me 3.50 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V07: Mjedisi i përqendrimit dhe saktësia

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Dhomë e përbashkët», vendos $G=0$: $\hat Y=60.00+(1.70)X$. Për grupin «Dhomë e qetë», vendos $G=1$: $\hat Y=64.50+(1.70)X$. Prerja 60.00 është vlera e përshtatur e ndryshores së rezultatit «pikët e saktësisë së detyrës» për grupin «Dhomë e përbashkët», kur ndryshorja parashikuese «blloqet e përqendrimit» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «blloqet e përqendrimit» lidhet me një ndryshim të përshtatur prej 1.70 njësish në ndryshoren e rezultatit «pikët e saktësisë së detyrës». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Dhomë e qetë» është 4.50 njësi më lart se për grupin «Dhomë e përbashkët». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «pikët e saktësisë së detyrës» |
| --- | --- | --- |
| Dhomë e përbashkët | 2.0 | 63.40 |
| Dhomë e përbashkët | 8.0 | 73.60 |
| Dhomë e qetë | 2.0 | 67.90 |
| Dhomë e qetë | 8.0 | 78.10 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi 1.70, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me 4.50 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V08: Udhëzuesi i muzeut dhe njohuritë

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Pa udhëheqje», vendos $G=0$: $\hat Y=47.00+(4.00)X$. Për grupin «E udhëhequr», vendos $G=1$: $\hat Y=53.00+(4.00)X$. Prerja 47.00 është vlera e përshtatur e ndryshores së rezultatit «pikët e njohurive» për grupin «Pa udhëheqje», kur ndryshorja parashikuese «vizitat» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «vizitat» lidhet me një ndryshim të përshtatur prej 4.00 njësish në ndryshoren e rezultatit «pikët e njohurive». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «E udhëhequr» është 6.00 njësi më lart se për grupin «Pa udhëheqje». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «pikët e njohurive» |
| --- | --- | --- |
| Pa udhëheqje | 0.0 | 47.00 |
| Pa udhëheqje | 3.0 | 59.00 |
| E udhëhequr | 0.0 | 53.00 |
| E udhëhequr | 3.0 | 65.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi 4.00, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me 6.00 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V09: Mënyra e vlerësimit dhe rishikimi

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Me shkrim», vendos $G=0$: $\hat Y=52.00+(3.50)X$. Për grupin «Bisedë», vendos $G=1$: $\hat Y=54.00+(3.50)X$. Prerja 52.00 është vlera e përshtatur e ndryshores së rezultatit «pikët e rishikimit» për grupin «Me shkrim», kur ndryshorja parashikuese «raundet e vlerësimit» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «raundet e vlerësimit» lidhet me një ndryshim të përshtatur prej 3.50 njësish në ndryshoren e rezultatit «pikët e rishikimit». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Bisedë» është 2.00 njësi më lart se për grupin «Me shkrim». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «pikët e rishikimit» |
| --- | --- | --- |
| Me shkrim | 1.0 | 55.50 |
| Me shkrim | 4.0 | 66.00 |
| Bisedë | 1.0 | 57.50 |
| Bisedë | 4.0 | 68.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi 3.50, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me 2.00 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

### T07-A07-V10: Formati i planifikimit dhe përfundimi

**Arsyeto para llogaritjes, pjesa (a)**

Për grupin «Letër», vendos $G=0$: $\hat Y=70.00+(-2.40)X$. Për grupin «Digjital», vendos $G=1$: $\hat Y=66.50+(-2.40)X$. Prerja 70.00 është vlera e përshtatur e ndryshores së rezultatit «koha e përfundimit» për grupin «Letër», kur ndryshorja parashikuese «seancat e planifikimit» është zero. Mund të jetë e nevojshme matematikisht, por e padobishme nga ana përmbajtësore nëse zeroja gjendet jashtë intervalit kuptimplotë.

**Zhvillo llogaritjen, pjesa (b)**

Brenda cilitdo grup, një rritje me një njësi e ndryshores parashikuese «seancat e planifikimit» lidhet me një ndryshim të përshtatur prej -2.40 njësish në ndryshoren e rezultatit «koha e përfundimit». Kur ndryshorja parashikuese ka të njëjtën vlerë, vlera e përshtatur për grupin «Digjital» është 3.50 njësi më poshtë se për grupin «Letër». Shprehja "në të njëjtën vlerë" tregon krahasimin e kushtëzuar të modelit, jo një ndërhyrje.

**Zhvillo llogaritjen, pjesa (c)**

Zëvendësimi jep:

| Grupi | X | Vlera e përshtatur e ndryshores «koha e përfundimit» |
| --- | --- | --- |
| Letër | 1.0 | 67.60 |
| Letër | 6.0 | 55.60 |
| Digjital | 1.0 | 64.10 |
| Digjital | 6.0 | 52.10 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Të dy ekuacionet kanë pjerrësi -2.40, prandaj ndryshime të barabarta horizontale prodhojnë ndryshime të barabarta vertikale të përshtatura. Prerjet e tyre ndryshojnë me -3.50 dhe zbritja e dy vlerave të përshtatura në cilëndo $X$ të paraqitur jep po atë largësi të pandryshueshme. Modeli nuk përmban term prodhimi $XG$, prandaj imponon vija të përshtatura paralele. Largësia është lidhje e përshtatur. Pa dizajn dhe supozime të përshtatshme, nuk vërteton se ndryshimi i përkatësisë në grup do ta ndryshonte rezultatin.

## A08: Ndërrimi i referencës pa ndryshuar marrëdhëniet e përshtatura

### T07-A08-V01: Ndërrimi i referencës së formatit të praktikës

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=40.00+(4.50)=44.50$. Pjerrësia e përbashkët mbetet $b'_1=2.80$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(4.50)=-4.50$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Me partner», $H=0$, që jep $\hat Y=44.50+(2.80)X$. Për grupin «Në mënyrë të pavarur», $H=1$, që jep $\hat Y=44.50+(2.80)X+(-4.50)=40.00+(2.80)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Në mënyrë të pavarur» është 4.50 njësi më poshtë se për grupin «Me partner».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Në mënyrë të pavarur | 1.0 | 42.80 | 42.80 |
| Në mënyrë të pavarur | 5.0 | 54.00 | 54.00 |
| Me partner | 1.0 | 47.30 | 47.30 |
| Me partner | 5.0 | 58.50 | 58.50 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V02: Ndërrimi i referencës së rolit në arkiv

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=35.00+(-5.00)=30.00$. Pjerrësia e përbashkët mbetet $b'_1=-1.60$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(-5.00)=5.00$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Koordinator», $H=0$, që jep $\hat Y=30.00+(-1.60)X$. Për grupin «Asistent», $H=1$, që jep $\hat Y=30.00+(-1.60)X+(5.00)=35.00+(-1.60)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Asistent» është 5.00 njësi më lart se për grupin «Koordinator».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Asistent | 0.0 | 35.00 | 35.00 |
| Asistent | 4.0 | 28.60 | 28.60 |
| Koordinator | 0.0 | 30.00 | 30.00 |
| Koordinator | 4.0 | 23.60 | 23.60 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V03: Ndërrimi i referencës së mjetit të leximit

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=50.00+(-3.00)=47.00$. Pjerrësia e përbashkët mbetet $b'_1=2.00$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(-3.00)=3.00$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Audio», $H=0$, që jep $\hat Y=47.00+(2.00)X$. Për grupin «Material i shtypur», $H=1$, që jep $\hat Y=47.00+(2.00)X+(3.00)=50.00+(2.00)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Material i shtypur» është 3.00 njësi më lart se për grupin «Audio».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Material i shtypur | 2.0 | 54.00 | 54.00 |
| Material i shtypur | 6.0 | 62.00 | 62.00 |
| Audio | 2.0 | 51.00 | 51.00 |
| Audio | 6.0 | 59.00 | 59.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V04: Ndërrimi i referencës së ekranit të navigimit

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=46.00+(-4.00)=42.00$. Pjerrësia e përbashkët mbetet $b'_1=-2.20$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(-4.00)=4.00$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Ndërveprues», $H=0$, që jep $\hat Y=42.00+(-2.20)X$. Për grupin «Statik», $H=1$, që jep $\hat Y=42.00+(-2.20)X+(4.00)=46.00+(-2.20)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Statik» është 4.00 njësi më lart se për grupin «Ndërveprues».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Statik | 1.0 | 43.80 | 43.80 |
| Statik | 5.0 | 35.00 | 35.00 |
| Ndërveprues | 1.0 | 39.80 | 39.80 |
| Ndërveprues | 5.0 | 31.00 | 31.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V05: Ndërrimi i referencës së ndihmës së katalogut

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=53.00+(3.00)=56.00$. Pjerrësia e përbashkët mbetet $b'_1=2.60$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(3.00)=-3.00$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Shirit kërkimi», $H=0$, që jep $\hat Y=56.00+(2.60)X$. Për grupin «Indeks», $H=1$, që jep $\hat Y=56.00+(2.60)X+(-3.00)=53.00+(2.60)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Indeks» është 3.00 njësi më poshtë se për grupin «Shirit kërkimi».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Indeks | 0.0 | 53.00 | 53.00 |
| Indeks | 3.0 | 60.80 | 60.80 |
| Shirit kërkimi | 0.0 | 56.00 | 56.00 |
| Shirit kërkimi | 3.0 | 63.80 | 63.80 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V06: Ndërrimi i referencës së mjedisit të seminarit

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=37.00+(5.00)=42.00$. Pjerrësia e përbashkët mbetet $b'_1=3.00$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(5.00)=-5.00$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Klasë», $H=0$, që jep $\hat Y=42.00+(3.00)X$. Për grupin «Online», $H=1$, që jep $\hat Y=42.00+(3.00)X+(-5.00)=37.00+(3.00)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Online» është 5.00 njësi më poshtë se për grupin «Klasë».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Online | 1.0 | 40.00 | 40.00 |
| Online | 4.0 | 49.00 | 49.00 |
| Klasë | 1.0 | 45.00 | 45.00 |
| Klasë | 4.0 | 54.00 | 54.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V07: Ndërrimi i referencës së dhomës së përqendrimit

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=59.00+(4.00)=63.00$. Pjerrësia e përbashkët mbetet $b'_1=1.80$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(4.00)=-4.00$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Dhomë private», $H=0$, që jep $\hat Y=63.00+(1.80)X$. Për grupin «Dhomë e hapur», $H=1$, që jep $\hat Y=63.00+(1.80)X+(-4.00)=59.00+(1.80)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Dhomë e hapur» është 4.00 njësi më poshtë se për grupin «Dhomë private».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Dhomë e hapur | 2.0 | 62.60 | 62.60 |
| Dhomë e hapur | 7.0 | 71.60 | 71.60 |
| Dhomë private | 2.0 | 66.60 | 66.60 |
| Dhomë private | 7.0 | 75.60 | 75.60 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V08: Ndërrimi i referencës së rrugës në muze

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=45.00+(6.50)=51.50$. Pjerrësia e përbashkët mbetet $b'_1=4.20$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(6.50)=-6.50$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Rrugë e përzgjedhur», $H=0$, që jep $\hat Y=51.50+(4.20)X$. Për grupin «Rrugë e lirë», $H=1$, që jep $\hat Y=51.50+(4.20)X+(-6.50)=45.00+(4.20)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Rrugë e lirë» është 6.50 njësi më poshtë se për grupin «Rrugë e përzgjedhur».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Rrugë e lirë | 0.0 | 45.00 | 45.00 |
| Rrugë e lirë | 3.0 | 57.60 | 57.60 |
| Rrugë e përzgjedhur | 0.0 | 51.50 | 51.50 |
| Rrugë e përzgjedhur | 3.0 | 64.10 | 64.10 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V09: Ndërrimi i referencës së takimit për rishikim

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=51.00+(2.50)=53.50$. Pjerrësia e përbashkët mbetet $b'_1=3.40$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(2.50)=-2.50$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Drejtpërdrejt», $H=0$, që jep $\hat Y=53.50+(3.40)X$. Për grupin «Asinkron», $H=1$, që jep $\hat Y=53.50+(3.40)X+(-2.50)=51.00+(3.40)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Asinkron» është 2.50 njësi më poshtë se për grupin «Drejtpërdrejt».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Asinkron | 1.0 | 54.40 | 54.40 |
| Asinkron | 5.0 | 68.00 | 68.00 |
| Drejtpërdrejt | 1.0 | 56.90 | 56.90 |
| Drejtpërdrejt | 5.0 | 70.50 | 70.50 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

### T07-A08-V10: Ndërrimi i referencës së mjetit të planifikimit

**Arsyeto para llogaritjes, pjesa (a)**

Referenca e re është grupi i vjetër $G=1$, prandaj prerja e tij e vjetër bëhet prerja e re: $b'_0=72.00+(-4.00)=68.00$. Pjerrësia e përbashkët mbetet $b'_1=-2.50$. Kontrasti e ndërron drejtimin, prandaj $b'_2=-(-4.00)=4.00$.

**Zhvillo llogaritjen, pjesa (b)**

Për grupin «Kalendar», $H=0$, që jep $\hat Y=68.00+(-2.50)X$. Për grupin «Fletore», $H=1$, që jep $\hat Y=68.00+(-2.50)X+(4.00)=72.00+(-2.50)X$. Në të njëjtin $X$, vlera e përshtatur për grupin «Fletore» është 4.00 njësi më lart se për grupin «Kalendar».

**Zhvillo llogaritjen, pjesa (c)**

Të dy kodimet japin:

| Grupi | X | Përshtatja nga kodimi i vjetër | Përshtatja nga kodimi i ri |
| --- | --- | --- | --- |
| Fletore | 1.0 | 69.50 | 69.50 |
| Fletore | 6.0 | 57.00 | 57.00 |
| Kalendar | 1.0 | 65.50 | 65.50 |
| Kalendar | 6.0 | 53.00 | 53.00 |

**Interpreto dhe kontrollo rezultatin, pjesa (d)**

Çdo rresht ka vlera të përshtatura identike në të dy kodimet. Ndërrimi i referencës e ndryshon grupin që përfaqëson prerja dhe e përmbys kontrastin e paraqitur mes grupeve, por përshkruan të njëjtat dy vija. Meqë secili rast e mban të njëjtën vlerë të përshtatur, zbritja e saj nga rezultati i vëzhguar e lë të pandryshuar edhe secilin rezidual. Zgjedhja e referencës e ndryshon paraqitjen, jo përshtatjen e modelit ose marrëdhëniet e përshtatura.

## A09: Interpretimi i ndërveprimit mes grupit dhe ndryshores parashikuese sasiore

### T07-A09-V01: Orët e praktikës sipas mbështetjes nga tutoriali

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Pa udhëheqje»: $\hat Y=40.00+(2.00)X$, me pjerrësi 2.00. Për grupin «Me tutor»: $\hat Y=44.00+(3.20)X$, me pjerrësi $b_1+b_3=2.00+(1.20)=3.20$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «pikët e arsyetimit» |
| --- | --- | --- | --- | --- |
| Pa udhëheqje | 0 | 1.0 | 0.0 | 42.00 |
| Pa udhëheqje | 0 | 5.0 | 0.0 | 50.00 |
| Me tutor | 1 | 1.0 | 1.0 | 47.20 |
| Me tutor | 1 | 5.0 | 5.0 | 60.00 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «orët e praktikës» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «pikët e arsyetimit» në boshtin vertikal. Për grupin «Pa udhëheqje», lidhi dy koordinatat e tij nga tabela. Për grupin «Me tutor», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=1.0$ dhe $X=5.0$ dhe emërtoji gjatësitë e tyre me 5.20 dhe 10.00. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=2.00$ është pjerrësia e ndryshores parashikuese «orët e praktikës» në grupin referues. $b_2=4.00$ është diferenca e përshtatur «Me tutor» minus «Pa udhëheqje», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=1.20$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është 5.20 në $X=1.0$ dhe 10.00 në $X=5.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V02: Seancat e praktikës sipas rolit në arkiv

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Staf i ri»: $\hat Y=38.00+(-1.20)X$, me pjerrësi -1.20. Për grupin «Staf me përvojë»: $\hat Y=35.00+(-2.00)X$, me pjerrësi $b_1+b_3=-1.20+(-0.80)=-2.00$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «koha e gjetjes» |
| --- | --- | --- | --- | --- |
| Staf i ri | 0 | 0.0 | 0.0 | 38.00 |
| Staf i ri | 0 | 4.0 | 0.0 | 33.20 |
| Staf me përvojë | 1 | 0.0 | 0.0 | 35.00 |
| Staf me përvojë | 1 | 4.0 | 4.0 | 27.00 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «seancat e praktikës» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «koha e gjetjes» në boshtin vertikal. Për grupin «Staf i ri», lidhi dy koordinatat e tij nga tabela. Për grupin «Staf me përvojë», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=0.0$ dhe $X=4.0$ dhe emërtoji gjatësitë e tyre me -3.00 dhe -6.20. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=-1.20$ është pjerrësia e ndryshores parashikuese «seancat e praktikës» në grupin referues. $b_2=-3.00$ është diferenca e përshtatur «Staf me përvojë» minus «Staf i ri», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=-0.80$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është -3.00 në $X=0.0$ dhe -6.20 në $X=4.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V03: Orët e leximit sipas mjetit

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Material i shtypur»: $\hat Y=49.00+(2.60)X$, me pjerrësi 2.60. Për grupin «Audio»: $\hat Y=51.00+(1.60)X$, me pjerrësi $b_1+b_3=2.60+(-1.00)=1.60$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «pikët e të kuptuarit» |
| --- | --- | --- | --- | --- |
| Material i shtypur | 0 | 2.0 | 0.0 | 54.20 |
| Material i shtypur | 0 | 6.0 | 0.0 | 64.60 |
| Audio | 1 | 2.0 | 2.0 | 54.20 |
| Audio | 1 | 6.0 | 6.0 | 60.60 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «orët e leximit» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «pikët e të kuptuarit» në boshtin vertikal. Për grupin «Material i shtypur», lidhi dy koordinatat e tij nga tabela. Për grupin «Audio», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=2.0$ dhe $X=6.0$ dhe emërtoji gjatësitë e tyre me 0.00 dhe -4.00. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=2.60$ është pjerrësia e ndryshores parashikuese «orët e leximit» në grupin referues. $b_2=2.00$ është diferenca e përshtatur «Audio» minus «Material i shtypur», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=-1.00$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është 0.00 në $X=2.0$ dhe -4.00 në $X=6.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V04: Ushtrimi sipas ekranit të navigimit

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Statik»: $\hat Y=48.00+(-1.50)X$, me pjerrësi -1.50. Për grupin «Ndërveprues»: $\hat Y=46.00+(-2.40)X$, me pjerrësi $b_1+b_3=-1.50+(-0.90)=-2.40$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «koha e navigimit» |
| --- | --- | --- | --- | --- |
| Statik | 0 | 1.0 | 0.0 | 46.50 |
| Statik | 0 | 5.0 | 0.0 | 40.50 |
| Ndërveprues | 1 | 1.0 | 1.0 | 43.60 |
| Ndërveprues | 1 | 5.0 | 5.0 | 34.00 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «përpjekjet e ushtrimit» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «koha e navigimit» në boshtin vertikal. Për grupin «Statik», lidhi dy koordinatat e tij nga tabela. Për grupin «Ndërveprues», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=1.0$ dhe $X=5.0$ dhe emërtoji gjatësitë e tyre me -2.90 dhe -6.50. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=-1.50$ është pjerrësia e ndryshores parashikuese «përpjekjet e ushtrimit» në grupin referues. $b_2=-2.00$ është diferenca e përshtatur «Ndërveprues» minus «Statik», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=-0.90$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është -2.90 në $X=1.0$ dhe -6.50 në $X=5.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V05: Grupet e ushtrimeve sipas ndihmës së katalogut

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Indeks»: $\hat Y=52.00+(2.00)X$, me pjerrësi 2.00. Për grupin «Shirit kërkimi»: $\hat Y=55.00+(2.70)X$, me pjerrësi $b_1+b_3=2.00+(0.70)=2.70$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «pikët e saktësisë» |
| --- | --- | --- | --- | --- |
| Indeks | 0 | 0.0 | 0.0 | 52.00 |
| Indeks | 0 | 4.0 | 0.0 | 60.00 |
| Shirit kërkimi | 1 | 0.0 | 0.0 | 55.00 |
| Shirit kërkimi | 1 | 4.0 | 4.0 | 65.80 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «grupet e ushtrimeve» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «pikët e saktësisë» në boshtin vertikal. Për grupin «Indeks», lidhi dy koordinatat e tij nga tabela. Për grupin «Shirit kërkimi», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=0.0$ dhe $X=4.0$ dhe emërtoji gjatësitë e tyre me 3.00 dhe 5.80. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=2.00$ është pjerrësia e ndryshores parashikuese «grupet e ushtrimeve» në grupin referues. $b_2=3.00$ është diferenca e përshtatur «Shirit kërkimi» minus «Indeks», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=0.70$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është 3.00 në $X=0.0$ dhe 5.80 në $X=4.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V06: Seancat sipas mjedisit të seminarit

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Online»: $\hat Y=36.00+(2.40)X$, me pjerrësi 2.40. Për grupin «Klasë»: $\hat Y=41.00+(3.20)X$, me pjerrësi $b_1+b_3=2.40+(0.80)=3.20$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «pikët e vetëbesimit» |
| --- | --- | --- | --- | --- |
| Online | 0 | 1.0 | 0.0 | 38.40 |
| Online | 0 | 5.0 | 0.0 | 48.00 |
| Klasë | 1 | 1.0 | 1.0 | 44.20 |
| Klasë | 1 | 5.0 | 5.0 | 57.00 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «seancat» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «pikët e vetëbesimit» në boshtin vertikal. Për grupin «Online», lidhi dy koordinatat e tij nga tabela. Për grupin «Klasë», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=1.0$ dhe $X=5.0$ dhe emërtoji gjatësitë e tyre me 5.80 dhe 9.00. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=2.40$ është pjerrësia e ndryshores parashikuese «seancat» në grupin referues. $b_2=5.00$ është diferenca e përshtatur «Klasë» minus «Online», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=0.80$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është 5.80 në $X=1.0$ dhe 9.00 në $X=5.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V07: Blloqet e përqendrimit sipas llojit të dhomës

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Dhomë e hapur»: $\hat Y=58.00+(2.10)X$, me pjerrësi 2.10. Për grupin «Dhomë private»: $\hat Y=62.00+(1.50)X$, me pjerrësi $b_1+b_3=2.10+(-0.60)=1.50$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «pikët e saktësisë së detyrës» |
| --- | --- | --- | --- | --- |
| Dhomë e hapur | 0 | 2.0 | 0.0 | 62.20 |
| Dhomë e hapur | 0 | 7.0 | 0.0 | 72.70 |
| Dhomë private | 1 | 2.0 | 2.0 | 65.00 |
| Dhomë private | 1 | 7.0 | 7.0 | 72.50 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «blloqet e përqendrimit» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «pikët e saktësisë së detyrës» në boshtin vertikal. Për grupin «Dhomë e hapur», lidhi dy koordinatat e tij nga tabela. Për grupin «Dhomë private», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=2.0$ dhe $X=7.0$ dhe emërtoji gjatësitë e tyre me 2.80 dhe -0.20. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=2.10$ është pjerrësia e ndryshores parashikuese «blloqet e përqendrimit» në grupin referues. $b_2=4.00$ është diferenca e përshtatur «Dhomë private» minus «Dhomë e hapur», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=-0.60$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është 2.80 në $X=2.0$ dhe -0.20 në $X=7.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V08: Vizitat sipas rrugës në muze

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Rrugë e lirë»: $\hat Y=44.00+(3.50)X$, me pjerrësi 3.50. Për grupin «Rrugë e përzgjedhur»: $\hat Y=47.00+(5.00)X$, me pjerrësi $b_1+b_3=3.50+(1.50)=5.00$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «pikët e njohurive» |
| --- | --- | --- | --- | --- |
| Rrugë e lirë | 0 | 0.0 | 0.0 | 44.00 |
| Rrugë e lirë | 0 | 3.0 | 0.0 | 54.50 |
| Rrugë e përzgjedhur | 1 | 0.0 | 0.0 | 47.00 |
| Rrugë e përzgjedhur | 1 | 3.0 | 3.0 | 62.00 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «vizitat» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «pikët e njohurive» në boshtin vertikal. Për grupin «Rrugë e lirë», lidhi dy koordinatat e tij nga tabela. Për grupin «Rrugë e përzgjedhur», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=0.0$ dhe $X=3.0$ dhe emërtoji gjatësitë e tyre me 3.00 dhe 7.50. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=3.50$ është pjerrësia e ndryshores parashikuese «vizitat» në grupin referues. $b_2=3.00$ është diferenca e përshtatur «Rrugë e përzgjedhur» minus «Rrugë e lirë», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=1.50$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është 3.00 në $X=0.0$ dhe 7.50 në $X=3.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V09: Raundet e vlerësimit sipas mënyrës së takimit

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Asinkron»: $\hat Y=50.00+(2.80)X$, me pjerrësi 2.80. Për grupin «Drejtpërdrejt»: $\hat Y=54.00+(2.30)X$, me pjerrësi $b_1+b_3=2.80+(-0.50)=2.30$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «pikët e rishikimit» |
| --- | --- | --- | --- | --- |
| Asinkron | 0 | 1.0 | 0.0 | 52.80 |
| Asinkron | 0 | 5.0 | 0.0 | 64.00 |
| Drejtpërdrejt | 1 | 1.0 | 1.0 | 56.30 |
| Drejtpërdrejt | 1 | 5.0 | 5.0 | 65.50 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «raundet e vlerësimit» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «pikët e rishikimit» në boshtin vertikal. Për grupin «Asinkron», lidhi dy koordinatat e tij nga tabela. Për grupin «Drejtpërdrejt», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=1.0$ dhe $X=5.0$ dhe emërtoji gjatësitë e tyre me 3.50 dhe 1.50. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=2.80$ është pjerrësia e ndryshores parashikuese «raundet e vlerësimit» në grupin referues. $b_2=4.00$ është diferenca e përshtatur «Drejtpërdrejt» minus «Asinkron», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=-0.50$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është 3.50 në $X=1.0$ dhe 1.50 në $X=5.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.

### T07-A09-V10: Planifikimi sipas llojit të mjetit

**Arsyeto para llogaritjes, pjesa (a)**

Kur $G=0$, prodhimi $XG$ është zero për çdo $X$. Kur $G=1$, $XG=X$.

**Zhvillo llogaritjen, pjesa (b)**

Zëvendësimi jep për grupin «Fletore»: $\hat Y=74.00+(-1.80)X$, me pjerrësi -1.80. Për grupin «Kalendar»: $\hat Y=72.00+(-2.70)X$, me pjerrësi $b_1+b_3=-1.80+(-0.90)=-2.70$.

**Zhvillo llogaritjen, pjesa (c)**

Termat e prodhimit dhe koordinatat e përshtatura janë:

| Grupi | G | X | XG | Vlera e përshtatur e ndryshores «koha e përfundimit» |
| --- | --- | --- | --- | --- |
| Fletore | 0 | 1.0 | 0.0 | 72.20 |
| Fletore | 0 | 6.0 | 0.0 | 63.20 |
| Kalendar | 1 | 1.0 | 1.0 | 69.30 |
| Kalendar | 1 | 6.0 | 6.0 | 55.80 |

**Zhvillo llogaritjen, pjesa (d)**

Vendose ndryshoren parashikuese «seancat e planifikimit» në boshtin horizontal dhe vlerën e përshtatur të ndryshores së rezultatit «koha e përfundimit» në boshtin vertikal. Për grupin «Fletore», lidhi dy koordinatat e tij nga tabela. Për grupin «Kalendar», lidhi dy koordinatat e tij në një vijë të dytë të emërtuar. Vizato segmente vertikale mes vijave në $X=1.0$ dhe $X=6.0$ dhe emërtoji gjatësitë e tyre me -2.90 dhe -7.40. Pjerrësitë joparalele e bëjnë të dukshme largësinë që ndryshon.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

$b_1=-1.80$ është pjerrësia e ndryshores parashikuese «seancat e planifikimit» në grupin referues. $b_2=-2.00$ është diferenca e përshtatur «Kalendar» minus «Fletore», pikërisht në $X=0$. Mbetet e interpretueshme aty, megjithëse zeroja mund të mos jetë qendrore nga ana përmbajtësore. $b_3=-0.90$ është diferenca mes dy pjerrësive të grupeve. Prandaj, largësia e përshtatur mes grupeve është $b_2+b_3X$: ajo është -2.90 në $X=1.0$ dhe -7.40 në $X=6.0$. Ndërveprimi përshkruan si ndryshon një lidhje e kushtëzuar sipas grupit. Nuk vërteton se grupi ose $X$ e shkakton rezultatin.
