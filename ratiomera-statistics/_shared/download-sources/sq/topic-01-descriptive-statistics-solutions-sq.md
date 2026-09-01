---
title: "Zgjidhjet e plota"
subtitle: "Statistika përshkruese"
document-id: "topic-01-descriptive-statistics-solutions-sq"
topic-id: "topic-01-descriptive-statistics"
topic-number: "01"
topic-slug: "descriptive-statistics"
document-type: "solutions"
locale: "sq"
paired-document-id: "topic-01-descriptive-statistics-exercises-sq"
---

Këto zgjidhje të plota përdorin të njëjtat kode dhe të njëjtën renditje si Fleta e ushtrimeve. Vlerat ndërmjetëse ruhen deri te hapi i treguar i rrumbullakimit, prandaj aty ku shënohet pranohen dallime të vogla që vijnë nga rrumbullakimi më i hershëm. Të gjitha situatat, vlerat, të dhënat dhe rezultatet e programeve janë krijuar për mësim; nuk janë gjetje empirike.

# Pjesa I: Teoria

## A01: Të vendosësh nëse mesatarja ka kuptim

### T01-A01-V01: Ndryshoret e një biblioteke komunitare

**Përcakto çështjen**

Kodi i degës është etiketë nominale, prandaj mesatarja e tij nuk ka kuptim për bibliotekën.

**Arsyeto hap pas hapi nga evidenca**

Minutat e leximit janë të shkallës së raportit dhe mund të mesatarizohen; mediana mund ta përshkruajë më mirë një shpërndarje asimetrike.

Vlerësimi i renditur i shërbimit është rendor, prandaj përpjesëtimet e kategorive, moda dhe mediana janë parësore; mesatarja supozon largësi të barabarta ndërmjet kategorive.

**Jep përfundimin dhe kufijtë e tij**

Temperatura në Fahrenheit është e shkallës intervalore, prandaj mesatarja dhe dallimet ndërmjet temperaturave kanë kuptim, ndonëse raportet jo.

Numri i artikujve të huazuar është absolut, prandaj numri mesatar ka kuptim, por forma vazhdon të jetë e rëndësishme për përfaqësueshmërinë.

### T01-A01-V02: Regjistrat e një festivali teatror

**Përcakto çështjen**

Kategoria e biletës është nominale, prandaj mesatarja është e pavlefshme.

Kohëzgjatja ka zero me kuptim dhe njësi të barabarta, kështu që mesatarja e saj është e vlefshme.

**Arsyeto hap pas hapi nga evidenca**

Rangu i rreshtit të ulëseve është rendor; rangjet mesatare ndonjëherë krahasohen sipas konventave të shprehura qartë, por mediana dhe shpërndarja e respektojnë informacionin e garantuar.

Viti kalendarik është intervalor, kështu që një vit mesatar mund ta përmbledhë kohën brenda një grupi koherent, por jo raportet e moshës.

**Jep përfundimin dhe kufijtë e tij**

Numri i rikthimeve të aktorëve në skenë për përshëndetjet përfundimtare është absolut dhe mund të mesatarizohet.

Përdor medianën krahas çdo mesatareje kur shpërndarjet sasiore janë asimetrike.

### T01-A01-V03: Vrojtimet në kopshte urbane

**Përcakto çështjen**

Etiketa e parcelës është identifikues dhe mbetet nominale pavarësisht shifrave, prandaj mesatarizimi i saj nuk ka kuptim.

**Arsyeto hap pas hapi nga evidenca**

Përqindja e lagështisë së tokës është sasiore me intervale të barabarta; brenda një përkufizimi të përbashkët, mesatarja ka kuptim, ndonëse një matje 0% kërkon interpretim fizik përpara pretendimeve me raporte.

Klasa e shëndetit të bimëve është rendore, prandaj mediana ose përpjesëtimet e kategorive janë më të sigurta se mesatarja.

**Jep përfundimin dhe kufijtë e tij**

Temperatura në Celsius është intervalore dhe mbështet mesataren, por jo raportet e temperaturave.

Numri i bimëve me lule është absolut dhe mbështet një numër mesatar.

### T01-A01-V04: Të dhënat e një seminari gjuhësor

**Përcakto çështjen**

Numri i distinktivit i etiketon personat dhe nuk ka mesatare sasiore.

Orët e ushtrimit kanë njësi të barabarta dhe zero me kuptim, prandaj mesatarizimi është i mbrojtshëm.

**Arsyeto hap pas hapi nga evidenca**

Niveli i zotërimit të gjuhës është rendor; mesatarja e kodeve arbitrare të niveleve supozon largësi të barabarta të pambështetura.

Një pikëzim i standardizuar i rrjedhshmërisë trajtohet zakonisht si intervalor, duke lejuar mesataren, por jo pretendime të drejtpërdrejta me raporte.

**Jep përfundimin dhe kufijtë e tij**

Numri i moduleve të përfunduara është absolut dhe mund të mesatarizohet.

Në çdo rast sasior, shqyrto formën dhe të dhënat që mungojnë përpara se ta quash mesataren tipike.

### T01-A01-V05: Regjistrat e transportit publik

**Përcakto çështjen**

Identifikuesi i linjës është nominal.

Koha e udhëtimit është e shkallës së raportit, prandaj mesatarja është e vlefshme, por vonesat e gjata mund ta tërheqin lart.

**Arsyeto hap pas hapi nga evidenca**

Kategoria e kënaqësisë është rendore dhe përmblidhet më mirë me përpjesëtime, modë ose medianë.

Ora e ditës rinis pas 24 orësh; një mesatare e zakonshme mund t'i vendosë oraret e vona të natës në mesditë, prandaj nevojiten metoda rrethore ose një pikë nisjeje e zgjedhur me kujdes për kohën e kaluar.

**Jep përfundimin dhe kufijtë e tij**

Numri i ndërrimeve është absolut dhe mbështet mesataren.

Vetëm pamja numerike nuk e lejon kurrë mesatarizimin.

### T01-A01-V06: Fushat e një koleksioni muzeal

**Përcakto çështjen**

Numri i hyrjes në koleksion është identifikues nominal dhe nuk duhet të mesatarizohet.

Masa e objektit është e shkallës së raportit dhe mbështet mesataren.

**Arsyeto hap pas hapi nga evidenca**

Rangu i përparësisë së konservimit është rendor, prandaj rendi i tij ka kuptim, por largësitë e barabarta ndërmjet rangjeve nuk garantohen.

Viti i krijimit është intervalor në një kalendar të përbashkët; një vit mesatar mund ta përmbledhë një koleksion koherent, ndërsa pohimi «dy herë më i vjetër» nuk rrjedh prej tij.

**Jep përfundimin dhe kufijtë e tij**

Numri i restaurimeve është absolut dhe mund të mesatarizohet.

Forma e shpërndarjes përcakton nëse mesataret e vlefshme janë edhe përfaqësuese.

### T01-A01-V07: Regjistri i vrojtimeve bregdetare

**Përcakto çështjen**

Emri i stacionit është nominal dhe nuk ka mesatare.

**Arsyeto hap pas hapi nga evidenca**

Lartësia e valës është e shkallës së raportit, prandaj mesatarja ka kuptim brenda një periudhe të përcaktuar vrojtimi.

Niveli i paralajmërimit është rendor dhe favorizon frekuencat e kategorive dhe medianën.

**Jep përfundimin dhe kufijtë e tij**

Koordinata lokale lindje-perëndim është intervalore: mesatarja mund ta gjejë një pikë baraspeshe brenda sistemit të fiksuar të koordinatave dhe dallimet ndërmjet koordinatave kanë kuptim, por raportet varen nga origjina arbitrare.

Numri i zogjve të detit është absolut dhe mbështet një numër mesatar.

### T01-A01-V08: Rrjedha e punës në një arkiv digjital

**Përcakto çështjen**

Formati i skedarit është nominal, prandaj vlejnë vetëm përmbledhjet e kategorive, si moda.

Kohëzgjatja e përpunimit është e shkallës së raportit dhe mund të mesatarizohet, ndërsa mediana është e dobishme nën asimetri djathtas.

**Arsyeto hap pas hapi nga evidenca**

Rangu i urgjencës është rendor dhe nuk garanton largësi të barabarta.

Ora e ditës është rrethore: 23:55 dhe 00:05 janë afër, megjithëse mesatarja e tyre e zakonshme numerike është mesdita.

**Jep përfundimin dhe kufijtë e tij**

Përdor përmbledhje rrethore ose kohën e kaluar nga një pikë reference me kuptim.

Numri i faqeve është absolut dhe mbështet mesatarizimin.

### T01-A01-V09: Regjistrat e një kori komunitar

**Përcakto çështjen**

Seksioni zanor është nominal dhe moda e tij, jo mesatarja, e identifikon kategorinë më të shpeshtë.

Përqindja e pjesëmarrjes ka njësi të barabarta dhe mund të mesatarizohet kur emëruesit dhe periudhat e vrojtimit janë të krahasueshme.

**Arsyeto hap pas hapi nga evidenca**

Rangu në audicion është rendor dhe favorizon medianën ose shpërndarjen e rangjeve.

Frekuenca në hertz është e shkallës së raportit dhe ka mesatare aritmetike me kuptim, ndonëse lartësia e perceptuar e tingullit mund ta arsyetojë një shkallë logaritmike për një pyetje tjetër.

**Jep përfundimin dhe kufijtë e tij**

Numri i sesioneve të humbura është absolut dhe mund të mesatarizohet.

Kodet dhe rangjet nuk bëhen sasi vetëm sepse përdorin numra.

### T01-A01-V10: Inventari i një kooperative ushqimore

**Përcakto çështjen**

ID-ja e furnitorit është nominale, prandaj mesatarja e saj nuk ka kuptim.

Masa e dërgesës është e shkallës së raportit dhe mbështet mesatarizimin.

**Arsyeto hap pas hapi nga evidenca**

Klasa e freskisë është rendore, çka i bën medianën, modën dhe përpjesëtimet të mbrojtshme pa supozuar largësi të barabarta.

Temperatura e ruajtjes në Celsius është intervalore, prandaj temperatura mesatare ka kuptim, por pohimi «dy herë më e ngrohtë» jo.

**Jep përfundimin dhe kufijtë e tij**

Numri i artikujve të dëmtuar është absolut dhe mbështet mesataren.

Intervalet e barabarta numerike e mbështesin mesatarizimin; vetëm një etiketë ose një rend nuk e mbështet.

## A02: Nivelet e matjes, duke përfshirë identifikuesit numerikë

### T01-A02-V01: Ndryshoret në një anketë arti në lagje

**Përcakto çështjen**

ID-ja e muralit është nominale: 4107 emërton një regjistrim dhe një kod tjetër një-për-një do ta ruante kuptimin e saj.

Forma e parapëlqyer e artit është gjithashtu nominale.

**Arsyeto hap pas hapi nga evidenca**

Renditja e jurisë është rendore, sepse rendi ka kuptim, por largësitë ndërmjet vendeve nuk janë të fiksuara.

Temperatura në Celsius është intervalore: dallimet i mbijetojnë një rishkallëzimi linear pozitiv, por zeroja është konvencionale.

**Jep përfundimin dhe kufijtë e tij**

Vëllimi i bojës është i shkallës së raportit, sepse njësitë e barabarta dhe zeroja me kuptim mbështesin raportet.

Numri i skicave të dorëzuara është absolut, sepse njësia e tij natyrore është një skicë.

Mesatarizimi i ID-së do ta përmblidhte skemën e kodimit dhe jo muralet.

### T01-A02-V02: Regjistrat e një biblioteke publike

**Përcakto çështjen**

Kodi i huamarrësit dhe zhanri i librit janë nominalë.

Gjendja e dëmtimit është rendore, sepse kategoritë e saj kanë rend, por jo largësi të barabarta të garantuara.

**Arsyeto hap pas hapi nga evidenca**

Viti i botimit është intervalor në kalendarin e vet: dallimet kanë kuptim, ndërsa raportet e viteve varen nga origjina e zgjedhur.

Gjatësia e raftit është e shkallës së raportit, sepse gjatësia zero dhe raportet kanë kuptim.

**Jep përfundimin dhe kufijtë e tij**

Numri i rinovimeve është absolut.

Transformimet e vlefshme janë riemërtimi një-për-një për të dhënat nominale, rikodimi rreptësisht rritës për të dhënat rendore, transformimi afin pozitiv për vitet, shumëzimi i njësisë për gjatësinë dhe mosrishkallëzimi arbitrar i numërimeve të sakta.

### T01-A02-V03: Të dhënat nga një studim i rrugëve për ecje

**Përcakto çështjen**

Numri i rrugës është nominal dhe jo sasi.

Lloji i sipërfaqes është nominal.

**Arsyeto hap pas hapi nga evidenca**

Kategoria e vështirësisë është rendore.

Koordinata lokale lindje-perëndim në hartë është intervalore: dallimet ndërmjet koordinatave kanë kuptim, por zeroja është një origjinë lokale arbitrare, prandaj raportet nuk kanë kuptim.

**Jep përfundimin dhe kufijtë e tij**

Largësia e rrugës është e shkallës së raportit dhe mbështet zero me kuptim dhe raporte.

Numri i këmbësorëve është absolut.

Pra, barazia zbatohet për etiketat, rendi për vështirësinë, dallimet për koordinatat, raportet për largësinë dhe veprimet e numërimit në njësi të plota për këmbësorët.

### T01-A02-V04: Matjet e një teatri komunitar

**Përcakto çështjen**

Etiketa e kostumit dhe zhanri i produksionit janë nominalë.

Renditja për çmimin e publikut është rendore.

**Arsyeto hap pas hapi nga evidenca**

Temperatura në Fahrenheit është intervalore, sepse dallimet e barabarta të temperaturës kanë kuptim, por 0°F nuk është mungesë e energjisë termike.

Kohëzgjatja e shfaqjes është e shkallës së raportit: zero minuta do të thotë se nuk ka kaluar kohë shfaqjeje dhe raportet mund të interpretohen.

**Jep përfundimin dhe kufijtë e tij**

Numri i ndryshimeve të skenës është absolut.

Zëvendësimi i numrave të etiketave me etiketa të tjera unike nuk ndryshon asnjë informacion; trajtimi i largësive të tyre numerike si matje do të krijonte informacion të sajuar.

### T01-A02-V05: Ndryshoret në një skedar monitorimi bregdetar

**Përcakto çështjen**

Numri serik i sensorit dhe materiali i vijës bregdetare janë nominalë.

Klasa e rrezikut të erozionit është rendore.

**Arsyeto hap pas hapi nga evidenca**

Viti i vrojtimit është intervalor në një kalendar të deklaruar.

Thellësia e ujit është e shkallës së raportit kur matet nga sipërfaqja zero e përcaktuar, ndërsa numri i vendeve të folezimit është absolut.

**Jep përfundimin dhe kufijtë e tij**

Numri serik mbetet nominal, sepse zbritja, renditja ose mesatarizimi pasqyrojnë rregullat e caktimit dhe jo vetitë e sensorit.

Transformimet duhet të ruajnë vetëm identitetin e kategorisë për numrin serik dhe materialin, rendin për rrezikun, dallimet për vitin, raportet për thellësinë dhe njësitë e sakta për numërimin.

### T01-A02-V06: Një grup të dhënash nga shkencat humane digjitale

**Përcakto çështjen**

Kodi i regjistrit të dorëshkrimit dhe kategoria e sistemit të shkrimit janë nominalë.

Rangu i ruajtjes është rendor.

**Arsyeto hap pas hapi nga evidenca**

Viti historik është intervalor në një kalendar të përbashkët, me dallime me kuptim, por me origjinë kalendarike arbitrare.

Madhësia e skedarit është e shkallës së raportit nën ndryshime të njësive, si nga megabajt në bajt.

**Jep përfundimin dhe kufijtë e tij**

Numri i faqeve të anotuara është absolut.

Transformimet përkatëse të lejueshme janë riemërtimi, rikodimi rreptësisht rritës, shndërrimi kalendarik afin pozitiv, shkallëzimi pozitiv i njësisë dhe transformimi identik për numërimet, sipas radhës.

### T01-A02-V07: Të dhënat e dërgesave të një kooperative ushqimore

**Përcakto çështjen**

Numri i furnitorit dhe kategoria e produktit janë nominalë.

Klasa e freskisë është rendore.

**Arsyeto hap pas hapi nga evidenca**

Temperatura e ruajtjes në Celsius është intervalore.

Masa e dërgesës është e shkallës së raportit, ndërsa numri i arkave është absolut.

**Jep përfundimin dhe kufijtë e tij**

Renditja e numrave të furnitorëve nuk ka kuptim përmbajtësor; renditja e freskisë ka.

Dallimet e temperaturës, si 4°C, kanë kuptim, por raportet e temperaturave jo.

Si dallimet, ashtu edhe raportet mund të kenë kuptim për masën, ndërsa arkat kanë një njësi natyrore të fiksuar numërimi.

### T01-A02-V08: Informacioni nga një seminar muzikor

**Përcakto çështjen**

Kodi i pjesëmarrësit dhe familja e instrumentit janë nominalë.

Renditja në audicion është rendore, sepse vendi i parë i paraprin të dytit pa një largësi të fiksuar.

**Arsyeto hap pas hapi nga evidenca**

Shmangia e akordimit në cent është intervalore rreth një pike reference konvencionale: dallimet kanë kuptim, por shmangia zero nuk është mungesë e lartësisë së tingullit.

Kohëzgjatja e ushtrimit është e shkallës së raportit.

**Jep përfundimin dhe kufijtë e tij**

Numri i pjesëve të interpretuara është absolut.

Mesataret e kodeve ose etiketave të familjeve nuk kanë interpretim, ndërsa veprimet aritmetike me kohëzgjatjet dhe numërimet mund t'u përgjigjen pyetjeve përmbajtësore.

### T01-A02-V09: Regjistrat e shërbimeve komunale

**Përcakto çështjen**

ID-ja e kërkesës dhe departamenti i shërbimit janë nominalë.

Niveli i përparësisë është rendor.

**Arsyeto hap pas hapi nga evidenca**

Viti kalendarik është intervalor.

Koha e përgjigjes është e shkallës së raportit, duke supozuar se zero orë përfaqëson mungesën e vonesës, ndërsa thirrjet përcjellëse formojnë një numërim absolut.

**Jep përfundimin dhe kufijtë e tij**

Shifrat në një ID mbartin vetëm informacion për barazinë.

Dallimet ndërmjet viteve i mbijetojnë zhvendosjeve të kalendarit, raportet e kohës së përgjigjes i mbijetojnë shndërrimit të njësive dhe njësia e një numërimi mbetet një thirrje.

### T01-A02-V10: Vrojtimet ekologjike në terren

**Përcakto çështjen**

Etiketa e parcelës dhe klasa e habitatit janë nominale.

**Arsyeto hap pas hapi nga evidenca**

Rangu i gjendjes së kurorës është rendor.

Lartësia mbidetare është intervalore, sepse niveli i detit është pikë reference e zgjedhur dhe janë të mundshme vlera negative.

**Jep përfundimin dhe kufijtë e tij**

Diametri i trungut është i shkallës së raportit, ndërsa numri i pemëve është absolut.

Kuptimi ruhet nga riemërtimi një-për-një për ndryshoret nominale, rikodimi rreptësisht rritës për rangun, transformimet afine pozitive të referencës për lartësinë mbidetare, shkallëzimi pozitiv i njësisë për diametrin dhe njësia natyrore e numërimit për pemët.

## A03: Zgjedhja mes mesatares, medianës dhe modës

### T01-A03-V01: Përmbledhjet e një tregu fermerësh

**Përcakto çështjen**

Kategoria e shitësit mbështet modën dhe përpjesëtimet, jo mesataren ose medianën.

**Arsyeto hap pas hapi nga evidenca**

Koha e pritjes është në shkallë raporti: raporto një mesatare dhe SD kur forma e saj është mjaft e ekuilibruar, por medianën dhe IQR-në kur pritjet e gjata krijojnë anim djathtas.

Vlerësimi i freskisë është rendor, prandaj moda, mediana dhe përpjesëtimet e kategorive e respektojnë informacionin e tij.

**Jep përfundimin dhe kufijtë e tij**

Numri i tezgës është identifikues dhe nuk ka qendër me kuptim përtej modës, nëse përsëritet.

Kostoja e shportës është në shkallë raporti; mesatarja pasqyron shpenzimin e përgjithshëm për shportë, ndërsa mediana e përfaqëson më mirë një shportë tipike kur ka anim.

### T01-A03-V02: Të dhënat e një radioje komunitare

**Përcakto çështjen**

Zhanri i programit është nominal, prandaj përdor modën dhe përpjesëtimet.

**Arsyeto hap pas hapi nga evidenca**

Kohëzgjatja e episodit është në shkallë raporti; mesatarja dhe mediana janë të dyja të vlefshme, ndërsa animi përcakton cila është më përfaqësuese.

Renditja e episodit të parapëlqyer është rendore dhe mbështet medianën dhe modën, jo mesataren pa një marrëveshje për largësi të barabarta.

**Jep përfundimin dhe kufijtë e tij**

Shenja identifikuese e stacionit është nominale, prandaj mund t'i përcaktohet moda, por nuk duhet mesatarizuar.

Shuma e dhurimit është në shkallë raporti, por shpesh anohet djathtas, çka i bën medianën dhe IQR-në përmbledhjet kryesore, ndërsa mesatarja mbetet e dobishme për të ardhurat e përgjithshme për dhurues.

### T01-A03-V03: Kërkesat në një arkiv publik

**Përcakto çështjen**

Lloji i kërkesës është nominal dhe mbështet modën.

**Arsyeto hap pas hapi nga evidenca**

Ditët e përpunimit janë në shkallë raporti, prandaj mesatarja dhe mediana janë të vlefshme; rastet e gjata shpesh e bëjnë medianën më përfaqësuese.

Kategoria e urgjencës është rendore dhe mbështet medianën, modën dhe përpjesëtimet.

**Jep përfundimin dhe kufijtë e tij**

Kodi i kutisë së arkivit është nominal dhe nuk duhet të përmblidhet me masa numerike të qendrës.

Numri i faqeve të dorëzuara është numërim absolut; mesatarja i përgjigjet pyetjes për ngarkesën mesatare të punës, ndërsa mediana mund ta përshkruajë më mirë një kërkesë tipike nëse pak dërgesa janë shumë të mëdha.

### T01-A03-V04: Regjistrat e biçikletave me qira

**Përcakto çështjen**

Modeli i biçikletës është nominal dhe mbështet modën.

Kohëzgjatja e udhëtimit është në shkallë raporti; raporto medianën kur animi djathtas është i zakonshëm dhe mesataren kur ka rëndësi koha e përgjithshme për udhëtim.

**Arsyeto hap pas hapi nga evidenca**

Rangu i përparësisë së mirëmbajtjes është rendor, prandaj parapëlqe medianën, modën dhe shpërndarjen e kategorive.

Identifikuesi i stacionit të parkimit është nominal.

**Jep përfundimin dhe kufijtë e tij**

Mosha e përdoruesit është në shkallë raporti në përdorimin e zakonshëm demografik, prandaj mesatarja dhe mediana janë të vlefshme; shpërndarja e vëzhguar e moshës përcakton sa përfaqësuese janë.

Asnjë statistikë e qendrës nuk e përshkruan e vetme përzierjen ose shpërhapjen e grupit.

### T01-A03-V05: Të dhënat e një seminari për të rritur

**Përcakto çështjen**

Formati i seminarit është nominal, prandaj përdor modën dhe përpjesëtimet.

Orët e pjesëmarrjes janë në shkallë raporti dhe mbështesin si mesataren, ashtu edhe medianën.

**Arsyeto hap pas hapi nga evidenca**

Kategoria e vetëbesimit është rendore dhe parapëlqen medianën, modën dhe frekuencat e kategorive.

Numri i regjistrimit është identifikues nominal.

**Jep përfundimin dhe kufijtë e tij**

Një pikëzim vlerësimi 0–100 trajtohet zakonisht si intervalor, prandaj mesatarja është e mbrojtshme nëse diferencat e barabarta ndërmjet pikëzimeve kanë kuptim të krahasueshëm; mediana mbetet e vlefshme kur ka anim ose efekte tavani.

Interpretimi me intervale të barabarta duhet të shprehet.

### T01-A03-V06: Inventari i pemëve në lagje

**Përcakto çështjen**

Lloji i pemës është nominal, prandaj moda jep llojin më të shpeshtë.

**Arsyeto hap pas hapi nga evidenca**

Perimetri i trungut është në shkallë raporti dhe mbështet mesataren dhe medianën; pemët e vjetra me përmasa të pazakonta mund ta bëjnë medianën më përfaqësuese.

Klasa e shëndetit është rendore dhe mbështet medianën, modën dhe përpjesëtimet.

**Jep përfundimin dhe kufijtë e tij**

Etiketa e inventarit është nominale.

Numri i zgavrave është absolut; mesatarja dhe mediana janë të dyja të vlefshme, por shumë zero dhe pak numërime të mëdha shpesh favorizojnë medianën së bashku me një shpërndarje frekuencash.

### T01-A03-V07: Regjistrat e një festivali kulturor

**Përcakto çështjen**

Lloji i aktivitetit është nominal dhe mbështet modën dhe përpjesëtimet.

Kohëzgjatja e aktivitetit është në shkallë raporti, prandaj lejon mesataren dhe medianën.

**Arsyeto hap pas hapi nga evidenca**

Kategoria e kënaqësisë është rendore, ndaj raporto medianën, modën dhe shpërndarjen.

Kodi i vendit është nominal.

**Jep përfundimin dhe kufijtë e tij**

Numri i pjesëmarrësve është absolut, prandaj mesatarja është e vlefshme për planifikimin e totalit, por mediana mund ta përfaqësojë më mirë një aktivitet tipik kur aktivitetet kryesore krijojnë anim të fortë djathtas.

Vlefshmëria rrjedh nga vetitë e shkallës; dobia varet edhe nga forma dhe qëllimi.

### T01-A03-V08: Të dhënat e një shërbimi lokal autobusësh

**Përcakto çështjen**

Kategoria e linjës është nominale dhe mbështet modën.

Vonesa është një diferencë sasiore nga orari dhe mund të mesatarizohet, por animi i fortë djathtas i bën medianën dhe IQR-në më përfaqësuese për shërbimin e zakonshëm.

**Arsyeto hap pas hapi nga evidenca**

Niveli i mbushjes është rendor, prandaj përdor medianën, modën dhe përpjesëtimet.

Identifikuesi i automjetit është nominal.

**Jep përfundimin dhe kufijtë e tij**

Largësia është në shkallë raporti dhe mbështet mesataren dhe medianën.

Raporto edhe vonesën mesatare kur pyetja lidhet me ndikimin në kohën e përgjithshme të udhëtarëve, duke e shënuar ndjeshmërinë e saj ndaj vonesave të rënda.

### T01-A03-V09: Të dhënat e katalogut të historisë gojore

**Përcakto çështjen**

Gjuha e intervistës është nominale; moda dhe përpjesëtimet e përshkruajnë atë.

Kohëzgjatja e regjistrimit është në shkallë raporti dhe mbështet mesataren ose medianën, varësisht nga forma.

**Arsyeto hap pas hapi nga evidenca**

Rangu i cilësisë së zërit është rendor, prandaj parapëlqe medianën, modën dhe shpërndarjen e kategorive.

Numri i katalogut është nominal.

**Jep përfundimin dhe kufijtë e tij**

Numri i temave të indeksuara është absolut, prandaj mesatarja dhe mediana janë të vlefshme, ndërsa animi përcakton se cilës masë duhet t'i jepet më shumë peshë.

Për gjuhën dhe numrin e katalogut, një qendër numerike tjetër përveç kategorisë më të shpeshtë nuk ka kuptim përmbajtësor.

### T01-A03-V10: Regjistrat e një kuzhine komunitare

**Përcakto çështjen**

Kategoria e vaktit është nominale dhe mbështet modën.

Koha e përgatitjes është në shkallë raporti, prandaj mesatarja dhe mediana janë të vlefshme; mediana u reziston përgatitjeve jashtëzakonisht të gjata.

**Arsyeto hap pas hapi nga evidenca**

Niveli i pikantësisë është rendor dhe mbështet medianën, modën dhe përpjesëtimet.

Identifikuesi i recetës është nominal.

**Jep përfundimin dhe kufijtë e tij**

Numri i racioneve të prodhuara është absolut dhe mund të përmblidhet me mesatare dhe medianë.

Një mesatare mund të jetë e vlefshme për shkallën, por jo përfaqësuese kur shpërndarja është e anuar ose multimodale, prandaj shqyrtoje shpërndarjen e plotë.

## A12: Krahasimi i paraqitjeve grafike alternative të të njëjtave të dhëna

### T01-A12-V01: Vizitat në bibliotekë në dy shkallë vertikale

**Përcakto çështjen**

Ndryshimi absolut është $132-120=12$ qindëshe vizitash, ose 1,200 vizita.

**Arsyeto hap pas hapi nga evidenca**

Në raport me tremujorin e parë, ai është $12/120\times100=10\%$.

Grafiku B bën që një rritje prej 10% të zërë pjesën më të madhe të lartësisë së zonës së vizatimit, sepse boshti i tij përfshin vetëm 16 qindëshe vizitash; Grafiku A e vendos atë në shtrirjen e plotë që nis nga zeroja.

**Jep përfundimin dhe kufijtë e tij**

Për një raport të përgjithshëm, paraqitja që nis nga zeroja ofron një krahasim më të sigurt të madhësisë.

Një paraqitje e përqendruar te prirja mund ta përdorë shkallën e ngushtë nëse pikat fundore, njësitë dhe vija bazë jozero tregohen qartë.

### T01-A12-V02: Përqindjet e shërbimit në kohë

**Përcakto çështjen**

Rritja është $86\%-82\%=4$ pikë përqindjeje.

**Arsyeto hap pas hapi nga evidenca**

Në raport me 82%, ajo është $4/82\times100=4.88\%$.

Shtyllat me vijë bazë në 80% e zmadhojnë raportin e gjatësive të tyre, sepse gjatësia e shtyllës zakonisht kodon madhësinë duke nisur nga zeroja.

**Jep përfundimin dhe kufijtë e tij**

Përdor shtylla që nisin nga zeroja për krahasim të drejtpërdrejtë të madhësisë, ose përdor një diagram me pika apo me vijë për ndryshime të vogla, duke e bërë të qartë shtrirjen e ngushtuar.

Si «4 pikë përqindjeje», ashtu edhe «rritje relative prej 4.88%» duhet të etiketohen saktë.

### T01-A12-V03: Piktogramet e përdorimit të parqeve

**Përcakto çështjen**

Në raport me 240, raportet e vizitave janë $252/240=1.05$ dhe $258/240=1.075$, që përfaqësojnë rritje prej 5% dhe 7.5%.

**Arsyeto hap pas hapi nga evidenca**

Nëse të dyja përmasat e ikonës përdorin këto raporte, sipërfaqet bëhen $1.05^2=1.1025$ dhe $1.075^2=1.1556$, duke sugjeruar rritje prej 10.25% dhe 15.56%.

**Jep përfundimin dhe kufijtë e tij**

Sipërfaqja i zmadhon dallimet mes vlerave.

Shtyllat me gjerësi të barabartë që nisin nga zeroja e kodojnë secilën vlerë në një përmasë dhe japin krahasimin e mbrojtshëm.

### T01-A12-V04: Përqindjet e anketës me shtylla të sheshta dhe 3D

**Përcakto çështjen**

Dallimi është $52\%-48\%=4$ pikë përqindjeje.

**Arsyeto hap pas hapi nga evidenca**

Një vijë bazë në 45% i bën gjatësitë e dukshme të shtyllave 3 dhe 7 njësi, me raport $7/3$, edhe pse përqindjet janë të afërta.

Perspektiva shton një sinjal gjerësie që nuk lidhet me të dhënat.

**Jep përfundimin dhe kufijtë e tij**

Rivizato shtylla të sheshta me gjerësi të barabartë duke nisur nga zeroja, ose përdor dy pika të etiketuara në një bosht përqindjeje ku shtrirja e ngushtuar bëhet e qartë.

Mbishkrimi shpjegues duhet të raportojë dallimin prej 4 pikësh dhe bazën e kampionit.

### T01-A12-V05: Regjistrimet për një aktivitet në paraqitje kronologjike dhe të rirenditur

**Përcakto çështjen**

Ndryshimi neto është $320-310=10$ regjistrime, që është $10/310\times100=3.23\%$.

**Arsyeto hap pas hapi nga evidenca**

Rendi kronologjik tregon rënien në 300 dhe rimëkëmbjen pas saj; renditja e vlerave e heq këtë vijueshmëri dhe përgjigjet vetëm se cila javë renditet më poshtë ose më lart.

**Jep përfundimin dhe kufijtë e tij**

Përdor diagramin me vijë për ndryshimin në kohë dhe diagramin me shtylla të renditura vetëm për një krahasim rangjesh të etiketuar shprehimisht.

Asnjëri rend nuk i ndryshon vlerat, por e ndryshon pyetjen së cilës mund t'i përgjigjet shikuesi.

### T01-A12-V06: Normat e riciklimit me dy vija bazë

**Përcakto çështjen**

Ndryshimi është $66\%-61\%=5$ pikë përqindjeje, ose $5/61\times100=8.20\%$ në raport me normën e parë.

**Arsyeto hap pas hapi nga evidenca**

Shkalla 60%–67% e bën ndryshimin të lehtë për t'u shqyrtuar, por të madh në pamje; shkalla 0%–100% komunikon madhësinë e përqindjes.

**Jep përfundimin dhe kufijtë e tij**

Një diagram i ngushtë me pika ose me vijë është i pranueshëm për hollësitë e prirjes kur kufijtë e boshtit dhe vlerat dallohen qartë.

Shtyllat që nisin nga zeroja parapëlqehen nëse gjatësia e shtyllës përfaqëson vetë përqindjen.

### T01-A12-V07: Vlerat e donacioneve të paraqitura me rrathë

**Përcakto çështjen**

Raporti i vërtetë i vlerave është $50/40=1.25$, prandaj fondi i dytë mori 25% më shumë.

**Arsyeto hap pas hapi nga evidenca**

Nëse diametri i rrethit shumëzohet me 1.25, sipërfaqja shumëzohet me $1.25^2=1.5625$, duke dhënë përshtypjen pamore të një sipërfaqeje 56.25% më të madhe.

**Jep përfundimin dhe kufijtë e tij**

Shtyllat me gjerësi të barabartë dhe gjatësi në përpjesëtim me vlerën përdorin një përmasë dhe e ruajnë raportin 1.25.

Rrathët me sipërfaqe përpjesëtimore do të kërkonin që diametri të shkallëzohej me $\sqrt{1.25}$, por shtyllat mbeten më të lehta për t'u krahasuar.

### T01-A12-V08: Përdorimi i ujit në një bosht të përmbysur

**Përcakto çështjen**

Përdorimi bie me $90-84=6$ njësi, që është ulje prej $6/90\times100=6.67\%$.

**Arsyeto hap pas hapi nga evidenca**

Në boshtin e zakonshëm, vija zbret kur përdorimi bie.

**Jep përfundimin dhe kufijtë e tij**

Përmbysja e boshtit bën që përdorimi më i ulët të shfaqet më lart dhe mund të ngatërrohet me rritje.

Përdor një bosht ku vlerat rriten nga poshtë lart, etiketo njësitë dhe vlerat dhe trego se tri vrojtimet paraqesin një rënie prej 6 njësish pa ia atribuar atë ndonjë shkaku.

### T01-A12-V09: Normat e përgjigjes dhe gjerësitë e pabarabarta të shtyllave

**Përcakto çështjen**

Dallimi është $73\%-71\%=2$ pikë përqindjeje.

**Arsyeto hap pas hapi nga evidenca**

Raporti i vërtetë i lartësive është $73/71=1.028$.

Nëse shtylla e dytë është dy herë më e gjerë, raporti i sipërfaqeve bëhet $2(73)/71=2.056$, duke sugjeruar më shumë se dyfishin e sasisë pamore.

**Jep përfundimin dhe kufijtë e tij**

Gjerësitë e barabarta të shtyllave sigurojnë që normën e përgjigjes ta kodojë gjatësia dhe jo sipërfaqja e pakontrolluar.

Etiketat duhet të japin edhe emëruesit, në mënyrë që të mos ngatërrohen përqindje të barabarta nga madhësi të ndryshme kampioni.

### T01-A12-V10: Përqindjet e përdorimit të kohës në diagram rrethor 3D dhe shtylla horizontale

**Përcakto çështjen**

Shuma e përqindjeve është $35+30+20+15=100\%$.

**Arsyeto hap pas hapi nga evidenca**

Pjerrësia e zmadhon sipërfaqen në plan të parë dhe i ngjesh sektorët në sfond, prandaj sektori 20% përpara mund të duket më i madh se sektorët 30% ose 35%.

**Jep përfundimin dhe kufijtë e tij**

Një diagram me shtylla horizontale që nisin nga zeroja përdor gjatësi të rreshtuara mbi të njëjtën vijë bazë, mundëson vlerësime të sakta të renditjes dhe dallimeve dhe mund ta shfaqë secilën përqindje.

Pamja 3D shton shtrembërim nga perspektiva pa shtuar të dhëna.

## A13: Diagnostikimi dhe ndreqja e një grafiku mashtrues

### T01-A13-V01: Diagram i pjesëmarrjes me bosht të shkurtuar

**Përcakto çështjen**

Dallimi është $508-492=16$ dhe dallimi relativ është $16/492\times100=3.25\%$.

**Arsyeto hap pas hapi nga evidenca**

Nisja në 488 i bën lartësitë e dukshme 4 dhe 20, duke sugjeruar në pamje një rezultat pesëfish.

Mungesa e etiketave të periudhave pengon gjithashtu një krahasim të vlefshëm.

**Jep përfundimin dhe kufijtë e tij**

Përdor shtylla me gjerësi të barabartë që nisin nga zeroja, me datat, popullatën dhe numërimet, ose një diagram me pika të etiketuara ku shtrirja e ngushtë bëhet e qartë.

Mbishkrimi shpjegues duhet të tregojë si dallimin prej 16 personash, ashtu edhe atë prej 3.25%.

### T01-A13-V02: Klasa të histogramit me gjerësi të pabarabarta, të paraqitura si numërime

**Përcakto çështjen**

Ka $n=100$ vrojtime.

**Arsyeto hap pas hapi nga evidenca**

Dendësia e frekuencës relative është $h_j=n_j/(n w_j)$, që jep $20/(100\cdot2)=0.100$, $35/(100\cdot5)=0.070$ dhe $45/(100\cdot10)=0.045$.

**Jep përfundimin dhe kufijtë e tij**

Po të përdorej frekuenca si lartësi, sipërfaqet do të ishin 40, 175 dhe 450, në vend që të përfaqësonin frekuencat.

Paraqit dendësitë e llogaritura si lartësi, në mënyrë që sipërfaqet të bëhen 0.20, 0.35 dhe 0.45, pikërisht frekuencat relative, dhe etiketo boshtin vertikal «Dendësia e frekuencës relative».

### T01-A13-V03: Panel informues komunitar me dy boshte

**Përcakto çështjen**

Boshte të veçanta lejojnë pothuajse çfarëdo përputhjeje pamore, sepse secila shtrirje mund të rregullohet në mënyrë të pavarur.

**Arsyeto hap pas hapi nga evidenca**

Prandaj pozicionet e përputhshme të vijave nuk e matin lidhjen dhe madje mund të çiftojnë prirje kohore pa lidhje.

Një ndreqje është përdorimi i dy paneleve të vendosura vertikalisht me një bosht të përbashkët kohor dhe boshte y të etiketuara plotësisht.

**Jep përfundimin dhe kufijtë e tij**

Nëse pyetja ka të bëjë me lidhjen, paraqit një diagram shpërndarjeje të vrojtimeve të çiftuara dhe raporto një masë të përshtatshme numerike të lidhjes së bashku me supozimet e saj.

Asnjëra alternativë nuk e shndërron një seri të shkurtër kohore në evidencë shkakësore.

### T01-A13-V04: Data të parregullta me hapësira të barabarta

**Përcakto çështjen**

Intervalet kohore janë afërsisht 1, 5 dhe 5 muaj, jo tri intervale të barabarta.

**Arsyeto hap pas hapi nga evidenca**

Në segmente pamore me gjerësi të barabartë, rritja nga shkurti deri në korrik është $31-22=9$, ndërsa ajo nga janari deri në shkurt është vetëm $22-20=2$.

Ndryshimet faktike në muaj janë afërsisht $(22-20)/1=2$, $(31-22)/5=1.8$ dhe $(32-31)/5=0.2$.

**Jep përfundimin dhe kufijtë e tij**

Prandaj, hapësirat e barabarta bëjnë që rritja pesëmujore të duket shumë më e shpejtë, ndonëse norma e saj mujore është pak më e ulët; ato e mbivlerësojnë edhe normën mujore përfundimtare.

Përdor një bosht me data të vërteta, paraqit të gjitha datat e disponueshme dhe etiketo njësinë e matjes.

### T01-A13-V05: Diagram rrethor i anuar për regjistrimet në program

**Përcakto çështjen**

Totali është $38+33+17+12=100\%$, me rend zbritës 38%, 33%, 17%, 12%.

**Arsyeto hap pas hapi nga evidenca**

Perspektiva i ndryshon sipërfaqet e projektuara sipas pozicionit, prandaj madhësia pamore nuk përputhet më me përqindjen.

**Jep përfundimin dhe kufijtë e tij**

Zëvendësoje grafikun me shtylla horizontale të etiketuara që nisin nga zeroja dhe renditen në rend zbritës.

Nëse diagrami rrethor ruhet, bëje të sheshtë, shmang sektorët e shkëputur dhe shfaq vlerat, megjithëse krahasimet e këndeve dhe sipërfaqeve mbeten më pak të sakta se gjatësitë e rreshtuara.

### T01-A13-V06: Totale kumulative të paraqitura si aktivitet mujor

**Përcakto çështjen**

Numrin e kërkesave për secilin muaj e gjen nga diferencat e njëpasnjëshme: 40 në muajin 1, $85-40=45$, $135-85=50$ dhe $190-135=55$.

**Arsyeto hap pas hapi nga evidenca**

Kur numërimet janë jonegative, seria kumulative nuk mund të ulet.

**Jep përfundimin dhe kufijtë e tij**

Prandaj, vija e saj në rritje nuk tregon vetvetiu përshpejtim të aktivitetit mujor.

Ose paraqit numërimet mujore me një titull të saktë, ose mbaj totalet kumulative me titullin «Kërkesa kumulative» dhe shpjego si ndërtohet shuma kumulative.

### T01-A13-V07: Ikona të shkallëzuara për pjesëmarrjen në punëtori

**Përcakto çështjen**

Raporti i pjesëmarrjes është $30/25=1.20$, që është rritje prej 20%.

**Arsyeto hap pas hapi nga evidenca**

Shkallëzimi si i lartësisë, ashtu edhe i gjerësisë me 1.20 e shumëzon sipërfaqen e ikonës me $1.20^2=1.44$, duke dhënë përshtypjen pamore të 44% më shumë.

**Jep përfundimin dhe kufijtë e tij**

Përdor shtylla me gjerësi të barabartë dhe gjatësi 25 dhe 30 që nisin nga zeroja, ose përsërit ikona të njëjta njësie me një çelës të shpjeguar.

Kodimi njëpërmasor e ruan raportin e synuar 1.20.

### T01-A13-V08: Dritare kohore e përzgjedhur për nivelet e lumit

**Përcakto çështjen**

Rritja e paraqitur është $2.7-2.1=0.6$ metra, ose $0.6/2.1\times100=28.57\%$ në raport me ditën e parë të paraqitur.

**Arsyeto hap pas hapi nga evidenca**

Kjo llogaritje përshkruan katër ditë të përzgjedhura, jo muajin.

**Jep përfundimin dhe kufijtë e tij**

Raporti kërkon të gjitha 30 vlerat, informacion për të dhënat që mungojnë, kohët e matjes, rregullin e përzgjedhjes dhe kontekstin përkatës stinor ose meteorologjik.

Paraqit regjistrin e plotë kronologjik në një bosht të qëndrueshëm dhe përshkruaje rritjen katërditore si nënperiudhë.

### T01-A13-V09: Panele krahasuese me shkallë të papajtueshme

**Përcakto çështjen**

Një lëvizje vertikale e fiksuar përkon me ndryshime numerike shumë të ndryshme ndërmjet paneleve.

**Arsyeto hap pas hapi nga evidenca**

Shtrirja me katër njësi e Panelit B e zmadhon luhatjen e vogël në raport me shtrirjen me 50 njësi të Panelit A, prandaj pjerrësitë dhe ndryshueshmëria në pamje nuk janë të krahasueshme.

**Jep përfundimin dhe kufijtë e tij**

Përdor kufij identikë të boshtit y dhe largësi identike ndërmjet shenjave kur synohet krahasimi i drejtpërdrejtë.

Nëse kufijtë e veçantë janë të nevojshëm për hollësi lokale, etiketoji qartë dhe shto një pamje shoqëruese të standardizuar ose me shkallë të përbashkët.

### T01-A13-V10: Përqindje pa emëruesin e saj

**Përcakto çështjen**

Përqindja mes rasteve të regjistruara është $12/20=60\%$, por vetëm për $20/50=40\%$ të të ftuarve është regjistruar pjesëmarrja.

**Arsyeto hap pas hapi nga evidenca**

Përqindja e pjesëmarrësve të konfirmuar mes të gjithë të ftuarve është $12/50=24\%$.

**Jep përfundimin dhe kufijtë e tij**

Rezultatet e 30 personave të tjerë mungojnë dhe nuk duhet të rikodohen si mospjesëmarrje.

Paraqit rezultatet e regjistruara me numërime, bëj të dukshëm numrin e ftesave dhe të dhënat që mungojnë pranë grafikut, mos nënkupto një normë të plotë në nivelin e të ftuarve dhe shqyrto nëse përgjigjja lidhet me pjesëmarrjen.

# Pjesa II: Praktika me kalkulator

## A04: Matja sasiore e ndikimit të një vlere të skajshme në mesatare

### T01-A04-V01: Numri i sesioneve të leximit

**Përgatit llogaritjen**

Fillimisht, $\bar{x}=60/6=10$ dhe mediana është $(10+10)/2=10$.

**Zhvillo llogaritjen**

Pasi 12 bëhet 42, $\bar{x}=(60-12+42)/6=90/6=15$, ndërsa mediana mbetet $(10+10)/2=10$.

**Interpreto dhe kontrollo rezultatin**

Mesatarja rritet me 5; mediana ndryshon me 0.

Madhësia e skajshme hyn drejtpërdrejt në mesatare, ndërsa pozicionet qendrore nuk lëvizin.

### T01-A04-V02: Kohët e shikimit të ekspozitës

**Përgatit llogaritjen**

Shuma fillestare është 96, prandaj $\bar{x}=96/6=16$; mediana është $(16+16)/2=16$.

**Zhvillo llogaritjen**

Me 48 në vend të 18, shuma është $96-18+48=126$, çka jep $\bar{x}=21$.

**Interpreto dhe kontrollo rezultatin**

Vlerat e renditura në mes mbeten 16 dhe 16, prandaj mediana është 16.

Mesatarja rritet me 5 minuta, ndërsa mediana nuk ndryshon, gjë që tregon rezistencën më të madhe të medianës.

### T01-A04-V03: Largësitë e pjesëve të shtegut

**Përgatit llogaritjen**

Fillimisht, $\bar{x}=30/6=5$ km dhe $\tilde{x}=(5+5)/2=5$ km.

**Zhvillo llogaritjen**

Pas gabimit, shuma është $30-7+31=54$, prandaj $\bar{x}=9$ km.

**Interpreto dhe kontrollo rezultatin**

Mediana mbetet 5 km.

Mesatarja rritet me 4 km sepse çdo madhësi kontribuon; rendi i vrojtimeve qendrore nuk ndryshon.

### T01-A04-V04: Numri i faqeve të digjitalizuara

**Përgatit llogaritjen**

Shuma fillestare është 126, çka jep $\bar{x}=126/6=21$ faqe, dhe $\tilde{x}=(21+21)/2=21$.

**Zhvillo llogaritjen**

Zëvendësimi i 24 me 84 jep shumën $186$ dhe mesataren $186/6=31$, ndërsa mediana mbetet 21.

**Interpreto dhe kontrollo rezultatin**

Vlera e skajshme i shton 60 totalit dhe, rrjedhimisht, 10 mesatares, por nuk ndryshon cilat vlera zënë pozicionet qendrore.

### T01-A04-V05: Kohëzgjatjet në radhë

**Përgatit llogaritjen**

Fillimisht, $\bar{x}=42/6=7$ minuta dhe $\tilde{x}=7$.

**Zhvillo llogaritjen**

Shuma e ndryshuar është $42-9+39=72$, prandaj mesatarja e re është $72/6=12$ minuta.

**Interpreto dhe kontrollo rezultatin**

Vlerat e mesit janë ende 7 dhe 7, kështu që mediana mbetet 7.

Mesatarja rritet me 5 minuta; ndryshimi zero i medianës pasqyron mbështetjen e saj në rend dhe jo në largësinë nga qendra.

### T01-A04-V06: Numri i pjesëmarrësve në seminar

**Përgatit llogaritjen**

Mesatarja fillestare është $144/6=24$, dhe mediana është $(24+24)/2=24$.

**Zhvillo llogaritjen**

Pasi 26 bëhet 62, $\bar{x}=(144-26+62)/6=180/6=30$.

**Interpreto dhe kontrollo rezultatin**

Mediana mbetet 24.

Prandaj, një vlerë e pabesueshme e rrit mesataren me 6 pjesëmarrës, por e lë medianën të pandryshuar, çka sinjalizon nevojën për të verifikuar regjistrin burimor.

### T01-A04-V07: Pikëzimet e cilësisë në arkiv

**Përgatit llogaritjen**

Fillimisht, $\bar{x}=204/6=34$ dhe $\tilde{x}=34$.

**Zhvillo llogaritjen**

Gabimi i importimit jep shumën $204-37+85=252$, prandaj $\bar{x}=42$; mediana mbetet 34.

Mesatarja rritet me 8 pikë.

**Interpreto dhe kontrollo rezultatin**

Një analist duhet të kontrollojë kodimin, njësitë, prejardhjen dhe shtrirjen e mundshme përpara se ta korrigjojë ose përjashtojë 85.

Vetëm skajshmëria nuk dëshmon se një vrojtim i vërtetë është i pavlefshëm.

### T01-A04-V08: Detyrat komunitare të përfunduara

**Përgatit llogaritjen**

Fillimisht, $\bar{x}=24/6=4$ detyra dhe $\tilde{x}=4$.

**Zhvillo llogaritjen**

Zëvendësimi i 6 me 30 jep shumën 48, prandaj $\bar{x}=48/6=8$, ndërsa $\tilde{x}=4$.

**Interpreto dhe kontrollo rezultatin**

Mesatarja e dyfishuar pasqyron totalin e detyrave të pjesëtuar me të gjashtë rastet.

Mediana e pandryshuar përshkruan çiftin qendror të renditur dhe e përfaqëson më mirë grumbullin e pesë numërimeve të vogla.

### T01-A04-V09: Kohëzgjatjet e regjistruara të intervistave

**Përgatit llogaritjen**

Mesatarja fillestare është $300/6=50$ minuta, dhe mediana është 50.

**Zhvillo llogaritjen**

Shuma e rishikuar është $300-54+114=360$, çka jep $\bar{x}=60$ minuta; çifti i mesit mbetet 50 dhe 50.

**Interpreto dhe kontrollo rezultatin**

Kështu, një vlerë e rrit mesataren me 10 minuta, por e ndryshon medianën me 0.

Shumica e intervistave mbeten të përqendruara pranë 50 minutave.

### T01-A04-V10: Numri i fidanëve të mbijetuar

**Përgatit llogaritjen**

Fillimisht, $\bar{x}=78/6=13$ fidanë dhe $\tilde{x}=13$.

**Zhvillo llogaritjen**

Me 57 në vend të 15, shuma bëhet $78-15+57=120$, prandaj $\bar{x}=20$, ndërsa mediana mbetet 13.

**Interpreto dhe kontrollo rezultatin**

Mesatarja rritet me 7 sepse madhësia e ndryshuar hyn në numërues.

Kontrolli i regjistrit burimor përcakton nëse 57 është gabim, mospërputhje e njësive apo një parcelë vërtet e pazakontë.

## A05: Llogaritja dhe krahasimi i medianave të grupeve

### T01-A05-V01: Dy dhoma galerie

**Përgatit llogaritjen**

Dhoma Veri renditet si $7,8,10,11,14$, prandaj mediana e saj është vlera e tretë, 10 minuta.

**Zhvillo llogaritjen**

Dhoma Jug renditet si $8,9,12,13,15$, çka jep medianën 12 minuta.

**Interpreto dhe kontrollo rezultatin**

Vizita qendrore e kampionit në Dhomën Jug është 2 minuta më e gjatë.

Ky krahasim përshkrues nuk tregon se dhoma shkaktoi shikim më të gjatë, sepse vizitorët dhe ekspozitat mund të ndryshojnë.

### T01-A05-V02: Dy ekipe katalogimi

**Përgatit llogaritjen**

Ekipi Cedër renditet si $15,16,17,18,20,21$, prandaj $\tilde{x}=(17+18)/2=17.5$ regjistra.

**Zhvillo llogaritjen**

Ekipi Panje renditet si $13,14,17,18,19,22$, çka jep po ashtu $(17+18)/2=17.5$.

**Interpreto dhe kontrollo rezultatin**

Medianat përputhen, ndonëse vlerat dhe shpërhapjet e tjera ndryshojnë.

Medianat e barabarta nuk i bëjnë të barabarta shpërndarjet e plota.

### T01-A05-V03: Dy rrugë për ecje

**Përgatit llogaritjen**

Rruga Liqen renditet si $27,29,31,32,35$, me medianë 31 minuta.

**Zhvillo llogaritjen**

Rruga Kodër renditet si $30,34,36,38,41$, me medianë 36 minuta.

**Interpreto dhe kontrollo rezultatin**

Mediana e vëzhguar e Rrugës Kodër është 5 minuta më e lartë.

Kjo përmbledh kohën qendrore të udhëtimit në këta kampionë, jo një efekt të përshtatur të rrugës.

### T01-A05-V04: Dy seminare publike

**Përgatit llogaritjen**

Seminari Argjilë renditet si $3,4,5,6,7,8$, prandaj mediana e tij është $(5+6)/2=5.5$ pyetje.

**Zhvillo llogaritjen**

Seminari Shtyp renditet si $2,3,4,5,7,9$, çka jep $(4+5)/2=4.5$.

**Interpreto dhe kontrollo rezultatin**

Mediana e Seminarit Argjilë është një pyetje më e lartë.

Vetëm medianat nuk zbulojnë amplitudat, grumbullimin ose nëse pak sesione ishin të pazakonta.

### T01-A05-V05: Dy koleksione të historisë gojore

**Përgatit llogaritjen**

Koleksioni Port renditet si $41,48,50,55,62$, prandaj mediana është 50 minuta.

**Zhvillo llogaritjen**

Koleksioni Pemishte renditet si $39,44,46,52,57$, prandaj mediana është 46 minuta.

**Interpreto dhe kontrollo rezultatin**

Regjistrimi qendror i Koleksionit Port është 4 minuta më i gjatë në këta kampionë.

Shpërhapja dhe përzgjedhja kërkojnë ende vlerësim të veçantë.

### T01-A05-V06: Dy kopshte komunitare

**Përgatit llogaritjen**

Kopshti Lindje renditet si $19,22,24,26,28,31$, çka jep $(24+26)/2=25$.

**Zhvillo llogaritjen**

Kopshti Perëndim renditet si $17,21,23,25,27,29$, çka jep $(23+25)/2=24$.

**Interpreto dhe kontrollo rezultatin**

Mediana e kampionit të Kopshtit Lindje e tejkalon atë të Kopshtit Perëndim me një prodhim të korrur.

Ndryshueshmëria e kampionimit dhe dallimet ndërmjet parcelave nuk lejojnë të nxirret një përfundim për popullatën vetëm nga ky dallim përshkrues.

### T01-A05-V07: Dy rrethe leximi

**Përgatit llogaritjen**

Rrethi Qelibar renditet si $12,14,16,18,20$, me medianë 16 faqe.

**Zhvillo llogaritjen**

Rrethi Indigo renditet si $13,15,17,19,21$, me medianë 17 faqe.

**Interpreto dhe kontrollo rezultatin**

Qendra e vëzhguar e Rrethit Indigo është një faqe më e lartë.

Një masë e shpërhapjes dhe të dhënat e plota të renditura ndihmojnë për të përcaktuar nëse ky dallim i vogël ka rëndësi përmbajtësore.

### T01-A05-V08: Dy sportele riparimi

**Përgatit llogaritjen**

Sporteli Një renditet si $18,20,22,24,26,30$, prandaj $\tilde{x}=(22+24)/2=23$ minuta.

**Zhvillo llogaritjen**

Sporteli Dy renditet si $17,21,23,25,27,29$, prandaj $\tilde{x}=(23+25)/2=24$.

**Interpreto dhe kontrollo rezultatin**

Rasti qendror në Sportelin Dy zgjati një minutë më shumë në këtë grup të dhënash; nga ky dallim nuk rrjedh asnjë shpjegim shkakësor.

### T01-A05-V09: Dy shkëmbime gjuhësore

**Përgatit llogaritjen**

Shkëmbimi Thupër renditet si $38,42,44,47,51$, çka jep medianën 44 radhë.

**Zhvillo llogaritjen**

Shkëmbimi Pishë renditet si $36,41,45,49,53$, çka jep medianën 45.

**Interpreto dhe kontrollo rezultatin**

Shkëmbimi Pishë është një radhë më lart në qendër.

Një IQR, amplitudë ose shpërndarje e plotë do të shtonte informacion për qëndrueshmërinë që medianat nuk e japin.

### T01-A05-V10: Dy ekipe të ruajtjes së natyrës

**Përgatit llogaritjen**

Ekipi Kreshtë renditet si $9,11,12,13,14,16$, prandaj mediana e tij është $(12+13)/2=12.5$ parcela.

**Zhvillo llogaritjen**

Ekipi Luginë renditet si $8,10,11,14,15,17$, çka jep po ashtu $(11+14)/2=12.5$.

**Interpreto dhe kontrollo rezultatin**

Ekipet kanë mediana të barabarta të kampionit pavarësisht vlerave të ndryshme të renditura, prandaj modelet e tyre të plota të performancës nuk duhen quajtur identike.

## A06: Detyra vijuese me mesataren dhe medianën

### T01-A06-V01: Faqet javore të përkthimit

**Përgatit llogaritjen, pjesa (a)**

Vlerat e renditura janë $4,5,6,7,8$, prandaj $\tilde{x}=6$ dhe $\bar{x}=30/5=6$.

**Zhvillo llogaritjen, pjesa (b)**

Me vlerën që mungon $m$, $(4+6+7+8+m)/5=6$, prandaj $25+m=30$ dhe $m=5$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Zëvendësimi i 5 me 25 jep shumën 50, mesataren 10 dhe medianën e renditur 7. Vlera e skajshme e rrit mesataren me 4, por e lëviz medianën vetëm me 1, sepse e ndryshon vetëm pak renditjen pranë qendrës.

### T01-A06-V02: Kohëzgjatjet e thirrjeve komunitare

**Përgatit llogaritjen, pjesa (a)**

Të dhënat e renditura $12,12,14,15,17$ japin medianën 14 dhe mesataren $70/5=14$ minuta.

**Zhvillo llogaritjen, pjesa (b)**

$(12+14+15+17+m)/5=14$ jep $58+m=70$, prandaj $m=12$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me 42, shuma është 100, mesatarja 20 dhe mediana e renditur 15. Katër thirrje janë ndërmjet 12 dhe 17, prandaj 20 tërhiqet përtej këtij grumbulli dhe nuk është kohëzgjatja e tij tipike.

### T01-A06-V03: Shënimet në terren

**Përgatit llogaritjen, pjesa (a)**

Vlerat e renditura $20,22,23,24,26$ kanë medianën 23; mesatarja është $115/5=23$.

**Zhvillo llogaritjen, pjesa (b)**

$(20+22+24+26+m)/5=23$ jep $92+m=115$, prandaj $m=23$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Zëvendësimi i saj me 58 jep shumën 150, mesataren 30 dhe medianën e renditur 24. Mesatarja rritet me 7 shënime, ndërsa mediana rritet me 1, çka tregon ndjeshmëri të ndryshme.

### T01-A06-V04: Pyetjet në mbledhjet e lagjes

**Përgatit llogaritjen, pjesa (a)**

Renditja jep $7,8,9,10,11$, medianën 9 dhe $\bar{x}=45/5=9$.

**Zhvillo llogaritjen, pjesa (b)**

$(7+9+10+11+m)/5=9$ jep $37+m=45$, prandaj $m=8$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me 28, shuma është 65 dhe mesatarja 13; vlerat e renditura $7,9,10,11,28$ kanë medianën 10. Një numërim i skajshëm e ndryshon mesataren me 4 dhe medianën me 1.

### T01-A06-V05: Përpunimi i kutive të arkivit

**Përgatit llogaritjen, pjesa (a)**

Vlerat e renditura $30,32,33,34,36$ japin medianën 33; $\bar{x}=165/5=33$ minuta.

**Zhvillo llogaritjen, pjesa (b)**

$(30+32+34+36+m)/5=33$ jep $132+m=165$, prandaj $m=33$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me 78, shuma është $210$, mesatarja 42 dhe mediana 34. Mediana është më afër katër kohëve të zakonshme, ndërsa mesatarja e përfshin rastin jashtëzakonisht të gjatë.

### T01-A06-V06: Numri i pushimeve gjatë provës

**Përgatit llogaritjen, pjesa (a)**

Renditja jep $2,3,4,5,6$; mediana dhe mesatarja janë të dyja 4 sepse shuma është 20.

**Zhvillo llogaritjen, pjesa (b)**

$(2+4+5+6+m)/5=4$ jep $17+m=20$, prandaj $m=3$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me 18, shuma është 35, mesatarja 7 dhe mediana e renditur 5. Numërimi i skajshëm i shton 15 totalit dhe 3 mesatares, por e lëviz pozicionin qendror vetëm me një njësi.

### T01-A06-V07: Vizitorët në tezgat e tregut

**Përgatit llogaritjen, pjesa (a)**

Vlerat e renditura $40,44,45,46,50$ japin medianën 45; mesatarja është $225/5=45$ qindra.

**Zhvillo llogaritjen, pjesa (b)**

$(40+44+46+50+m)/5=45$ jep $180+m=225$, prandaj $m=45$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Zëvendësimi i saj me 85 jep shumën 265, mesataren 53 dhe medianën 46. Katër periudha mbeten në 50 qindra ose më poshtë, prandaj mediana e përfaqëson më mirë qendrën e tyre.

### T01-A06-V08: Numri i fjalëve në etiketat e ekspozitës

**Përgatit llogaritjen, pjesa (a)**

Vlerat e renditura janë $9,10,11,12,13$; mediana dhe mesatarja janë 11 dhjetëshe sepse $55/5=11$.

**Zhvillo llogaritjen, pjesa (b)**

$(9+11+12+13+m)/5=11$ jep $45+m=55$, prandaj $m=10$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me 35, shuma është 80, mesatarja 16 dhe mediana 12. Mesatarja reagon ndaj rritjes së plotë prej 25 njësish; mediana varet nga vrojtimi i ri qendror.

### T01-A06-V09: Kohëzgjatjet e vrojtimeve të habitatit

**Përgatit llogaritjen, pjesa (a)**

Renditja jep $16,18,19,20,22$, pra medianën 19 dhe mesataren $95/5=19$ minuta.

**Zhvillo llogaritjen, pjesa (b)**

$(16+18+20+22+m)/5=19$ jep $76+m=95$, prandaj $m=19$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me 54, shuma është 130, mesatarja 26 dhe mediana 20. Kohëzgjatja e skajshme e rrit mesataren me 7 minuta, por medianën vetëm me 1 minutë.

### T01-A06-V10: Totali i dërgesave të kooperativës

**Përgatit llogaritjen, pjesa (a)**

Vlerat e renditura $24,26,27,28,30$ japin medianën 27 dhe mesataren $135/5=27$.

**Zhvillo llogaritjen, pjesa (b)**

$(24+26+28+30+m)/5=27$ jep $108+m=135$, prandaj $m=27$.

**Interpreto dhe kontrollo rezultatin, pjesa (c)**

Me 72, shuma është 180, mesatarja 36 dhe mediana 28. Meqë katër ditë shtrihen nga 24 deri në 30, mediana e vendos më mirë qendrën e tyre; mesatarja përcjell edhe totalin më të madh të shkaktuar nga dita e skajshme.

## A07: Medianat e të dhënave të bashkuara dhe zëvendësimi i vlerave

### T01-A07-V01: Bashkimi i dy grupeve të leximit

**Përgatit llogaritjen**

Renditja e të dhënave të bashkuara është $2,3,5,6,8,9,11,12,14,15$, prandaj $\tilde{x}=(8+9)/2=8.5$.

**Zhvillo llogaritjen**

Zëvendësimi i 5 me 10 jep vlerat qendrore 9 dhe 10, e kështu medianën 9.5.

**Interpreto dhe kontrollo rezultatin**

Duke u nisur nga të dhënat fillestare, zëvendësimi i 15 me 60 i lë vlerat qendrore 8 dhe 9 dhe medianën 8.5.

Zëvendësimi i parë i kalon pozicionet qendrore; rritja e një vlere që gjendet tashmë mbi to nuk i kalon.

### T01-A07-V02: Bashkimi i dy periudhave të tregut

**Përgatit llogaritjen**

Renditja fillestare është $10,12,14,16,18,20,22,24,26,28$, çka jep $(18+20)/2=19$.

**Zhvillo llogaritjen**

Kur 14 ndryshohet në 21, renditja rreth qendrës është $...,18,20,21,22,...$, prandaj mediana është $(20+21)/2=20.5$.

**Interpreto dhe kontrollo rezultatin**

Zëvendësimi i vlerës fillestare 28 me 80 i lë pozicionet e pesta dhe të gjashta në 18 dhe 20, prandaj mediana mbetet 19.

Rezultatin e kontrollon pozicioni në renditje, jo largësia e skajshme.

### T01-A07-V03: Bashkimi i dy rafteve të arkivit

**Përgatit llogaritjen**

Renditja e të dhënave të bashkuara $1,2,4,5,7,8,10,11,13,14$ jep medianën $(7+8)/2=7.5$.

**Zhvillo llogaritjen**

Kur 4 bëhet 9, çifti qendror është 8 dhe 9, çka jep 8.5.

**Interpreto dhe kontrollo rezultatin**

Duke u kthyer te të dhënat fillestare dhe duke ndryshuar 14 në 40, çifti qendror mbetet 7 dhe 8, prandaj mediana mbetet 7.5.

Vetëm zëvendësimi i parë ndryshon vlerat që zënë qendrën.

### T01-A07-V04: Bashkimi i dy sesioneve të ecjes

**Përgatit llogaritjen**

Fillimisht, vlerat qendrore të renditura janë 40 dhe 42, prandaj $\tilde{x}=41$ qindra hapa.

**Zhvillo llogaritjen**

Zëvendësimi i 35 me 44 jep vlerat qendrore 42 dhe 44, e kështu medianën 43.

**Interpreto dhe kontrollo rezultatin**

Në zëvendësimin e veçantë të 52 me 100, çifti qendror mbetet 40 dhe 42 dhe mediana mbetet 41.

Zëvendësimi i dytë e rrit madhësinë pa i ndryshuar pozicionet qendrore.

### T01-A07-V05: Bashkimi i dy tavolinave të seminarit

**Përgatit llogaritjen**

Renditja e të dhënave të bashkuara jep vlerat qendrore 12 dhe 13, prandaj $\tilde{x}=12.5$.

**Zhvillo llogaritjen**

Pasi 9 bëhet 14, vlerat qendrore janë 13 dhe 14, çka jep medianën 13.5.

**Interpreto dhe kontrollo rezultatin**

Duke u nisur sërish nga vlerat fillestare, ndryshimi i 19 në 49 i lë 12 dhe 13 në pozicionet e pesta dhe të gjashta, prandaj mediana mbetet 12.5.

Një zëvendësim ndikon në medianë vetëm kur ndryshon renditjen në mes.

### T01-A07-V06: Bashkimi i dy zonave të vrojtimit

**Përgatit llogaritjen**

Çifti qendror fillestar është 27 dhe 28, çka jep $27.5$ familje.

**Zhvillo llogaritjen**

Kur 24 zëvendësohet me 29, çifti qendror i renditur bëhet 28 dhe 29, prandaj mediana është 28.5.

**Interpreto dhe kontrollo rezultatin**

Në ndryshimin e veçantë nga 34 në 74, 27 dhe 28 mbeten qendrore dhe mediana mbetet 27.5.

Madhësia e vlerës së largët në skajin e sipërm nuk ka rëndësi përderisa rangu i saj mbetet mbi qendër.

### T01-A07-V07: Bashkimi i dy grupeve të provave

**Përgatit llogaritjen**

Vlerat qendrore fillestare të renditura janë 12 dhe 14, prandaj mediana është 13 masa.

**Zhvillo llogaritjen**

Zëvendësimi i 8 me 15 e ndryshon çiftin qendror në 14 dhe 15, çka jep 14.5.

**Interpreto dhe kontrollo rezultatin**

Ndërkaq, zëvendësimi i maksimumit fillestar 22 me 70 i lë 12 dhe 14 në qendër, prandaj mediana mbetet 13.

Rezultatet ndjekin pozicionet e pesta dhe të gjashta të dhjetë vlerave.

### T01-A07-V08: Bashkimi i dy rrjedhave të vizitorëve

**Përgatit llogaritjen**

Qendra fillestare është $(120+125)/2=122.5$ vizitorë.

**Zhvillo llogaritjen**

Zëvendësimi i 110 me 128 e ndryshon çiftin qendror të renditur në 125 dhe 128, prandaj $\tilde{x}=126.5$.

**Interpreto dhe kontrollo rezultatin**

Në një ndryshim të veçantë, zëvendësimi i 145 me 300 i mban 120 dhe 125 në qendër, duke e lënë medianën 122.5.

Prandaj, një maksimum shumë më i madh nuk ndikon domosdoshmërisht në medianë.

### T01-A07-V09: Bashkimi i dy ekipeve të ruajtjes së natyrës

**Përgatit llogaritjen**

Fillimisht, vlerat e pesta dhe të gjashta janë 21 dhe 23, prandaj $\tilde{x}=22$.

**Zhvillo llogaritjen**

Zëvendësimi i 17 me 24 i vendos 23 dhe 24 në qendër, çka jep 23.5.

**Interpreto dhe kontrollo rezultatin**

Kthimi te grupi fillestar dhe zëvendësimi i 31 me 71 i lë 21 dhe 23 në qendër dhe medianën në 22.

Ndryshimi i pozicionit në renditje në ndryshimin e parë ka rëndësi; zgjatja e skajit të sipërm në të dytin nuk ka.

### T01-A07-V10: Bashkimi i dy dritareve të dërgesave

**Përgatit llogaritjen**

Vlerat qendrore fillestare janë 60 dhe 62, prandaj mediana është 61 arka.

**Zhvillo llogaritjen**

Zëvendësimi i 55 me 64 prodhon vlerat qendrore 62 dhe 64, çka jep medianën 63.

**Interpreto dhe kontrollo rezultatin**

Zëvendësimi i veçantë i vlerës fillestare 72 me 150 i mban 60 dhe 62 në mes, prandaj mediana mbetet 61.

Këto janë pozicionet e pesta dhe të gjashta, sepse $n=10$.

## A08: Mesatarja, moda, varianca e kampionit, SD-ja e kampionit dhe amplituda

### T01-A08-V01: Kontributet në një rreth tregimesh

**Përgatit llogaritjen**

Shuma është 48, prandaj $\bar{x}=48/8=6$; moda është 6.

**Zhvillo llogaritjen**

Devijimet janë $(-4,-2,-2,0,0,0,2,6)$ dhe katrorët e tyre janë $(16,4,4,0,0,0,4,36)$, me shumën 64.

Prandaj $s^2=64/7=9.14$ dhe $s=\sqrt{64/7}=3.02$.

**Interpreto dhe kontrollo rezultatin**

Amplituda është $12-2=10$.

Kontributet përqendrohen në 6, me një shpërhapje tipike të kampionit prej afërsisht 3.02 kontributesh rreth kësaj mesatareje.

### T01-A08-V02: Gjatësitë e etiketave të ekspozitës

**Përgatit llogaritjen**

Vlerat kanë shumën 72, çka jep $\bar{x}=72/8=9$ rreshta, dhe 9 është moda.

**Zhvillo llogaritjen**

Devijimet $(-4,-2,-2,0,0,0,2,6)$ kanë shumën e katrorëve $64$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $s^2=64/7=9.14$, $s=3.02$ rreshta dhe amplituda $15-5=10$ rreshta.

Etiketa me 15 rreshta kontribuon $6^2=36$ në shumën e katrorëve të devijimeve.

### T01-A08-V03: Pyetjet në sesionet komunitare

**Përgatit llogaritjen**

Shuma është 56, prandaj $\bar{x}=7$.

**Zhvillo llogaritjen**

Vlerat 3, 7 dhe 11 paraqiten secila dy herë, prandaj të tria janë vlera modale.

Katrorët e devijimeve $(16,16,4,0,0,4,16,16)$ kanë shumën 72.

**Interpreto dhe kontrollo rezultatin**

Kështu, $s^2=72/7=10.29$, $s=\sqrt{72/7}=3.21$ dhe amplituda $11-3=8$.

Disa moda nënkuptojnë se asnjë vlerë nuk e ka e vetme frekuencën më të lartë.

### T01-A08-V04: Kohët e katalogimit

**Përgatit llogaritjen**

Shuma është 108, prandaj $\bar{x}=13.5$ minuta; moda është 15.

**Zhvillo llogaritjen**

Katrorët e devijimeve kanë shumën e parrumbullakosur $12.25+2.25+2.25+0.25+2.25+2.25+2.25+6.25=30$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $s^2=30/7=4.2857\ldots\approx4.29$, $s=\sqrt{30/7}=2.0701\ldots\approx2.07$ minuta dhe amplituda $16-10=6$ minuta.

Rrumbullakimi bëhet vetëm në variancën dhe SD-në përfundimtare të paraqitur.

### T01-A08-V05: Kërkesat ditore për riparim

**Përgatit llogaritjen**

Shuma është 32, çka jep $\bar{x}=4$, dhe moda është 4.

**Zhvillo llogaritjen**

Katrorët e devijimeve $(9,4,4,1,0,0,0,64)$ kanë shumën 82.

**Interpreto dhe kontrollo rezultatin**

Prandaj $s^2=82/7=11.71$, $s=3.42$ dhe amplituda $12-1=11$.

Kontributi i vlerës 12 është 64 prej 82 njësive të katrorëve të devijimeve, dhe kjo vlerë e tërheq mesataren mbi gjashtë prej tetë vrojtimeve.

### T01-A08-V06: Kohëzgjatjet e segmenteve audio

**Përgatit llogaritjen**

Shuma është 188, prandaj $\bar{x}=23.5$ sekonda; 24 është moda.

**Zhvillo llogaritjen**

Katrorët e devijimeve kanë shumën $12.25+2.25+0.25+0.25+0.25+0.25+0.25+20.25=36$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $s^2=36/7=5.14$, $s=\sqrt{36/7}=2.27$ sekonda dhe amplituda $28-20=8$ sekonda.

Përmbledhjet tregojnë një grumbull pranë 24 me shpërhapje të moderuar.

### T01-A08-V07: Vrojtimet në parcelat e kopshtit

**Përgatit llogaritjen**

Totali është 60, çka jep $\bar{x}=7.5$; moda është 7.

**Zhvillo llogaritjen**

Katrorët e devijimeve janë $12.25,2.25,0.25,0.25,0.25,0.25,2.25,20.25$, me total 38.

**Interpreto dhe kontrollo rezultatin**

Prandaj $s^2=38/7=5.4286\ldots\approx5.43$, $s=\sqrt{38/7}=2.3299\ldots\approx2.33$ dhe amplituda $12-4=8$.

Vlerat mbeten të parrumbullakosura deri te varianca dhe SD-ja përfundimtare e paraqitur.

### T01-A08-V08: Kohët e regjistrimit në seminar

**Përgatit llogaritjen**

Shuma është 280, prandaj $\bar{x}=35$ minuta; 38 është moda.

**Zhvillo llogaritjen**

Katrorët e devijimeve $(25,9,1,1,1,9,9,9)$ kanë shumën 64.

**Interpreto dhe kontrollo rezultatin**

Kështu, $s^2=64/7=9.14$, $s=3.02$ minuta dhe amplituda $38-30=8$ minuta.

Mesatarja është nën modë sepse kohët më të ulëta të regjistrimit shtrihen më larg nga 35 sesa kohët më të larta.

### T01-A08-V09: Numri i temave të indeksuara

**Përgatit llogaritjen**

Shuma është 96, çka jep $\bar{x}=12$.

**Zhvillo llogaritjen**

Si 10, ashtu edhe 12 paraqiten dy herë, prandaj të dyja janë vlera modale.

Katrorët e devijimeve $(9,4,4,1,0,0,1,49)$ kanë shumën 68.

**Interpreto dhe kontrollo rezultatin**

Kështu, $s^2=68/7=9.71$, $s=3.12$ dhe amplituda $19-9=10$.

Mesatarja 12 nuk zbulon se kontributi i vlerës 19 është 49 prej 68 njësive të katrorëve të devijimeve.

### T01-A08-V10: Intervalet e dërgesave komunitare

**Përgatit llogaritjen**

Totali është 336, prandaj $\bar{x}=42$ minuta, që është edhe moda.

**Zhvillo llogaritjen**

Katrorët e devijimeve $(16,4,4,0,0,0,4,36)$ kanë totalin 64.

**Interpreto dhe kontrollo rezultatin**

Rrjedhimisht, $s^2=64/(8-1)=9.14$, $s=3.02$ minuta dhe amplituda $48-38=10$ minuta.

Emëruesi 7 tregon variancën e korrigjuar të kampionit dhe jo variancën e popullatës.

## A09: Mesataret e barabarta nuk nënkuptojnë shpërndarje të ngjashme

### T01-A09-V01: Dy programe leximi në lagje

**Arsyeto para llogaritjes**

Të dyja shumat janë 30, prandaj të dyja mesataret janë $30/5=6$.

**Zhvillo llogaritjen**

Amplituda e Programit Përrua është $8-4=4$; shuma e devijimeve të ngritura në katror është 10, prandaj $s=\sqrt{10/4}=1.58$.

Amplituda e Programit Fushë është 12; shuma e devijimeve të ngritura në katror është 90, prandaj $s=\sqrt{90/4}=4.74$.

**Interpreto dhe kontrollo rezultatin**

Programi Fushë ka shpërhapje tri herë më të madhe në njësi të SD-së.

Mesatarja e përbashkët e përcakton qendrën, por e fsheh këtë dallim të madh në qëndrueshmëri.

### T01-A09-V02: Dy rrjedha pune në arkiv

**Arsyeto para llogaritjes**

Secila rrjedhë pune ka shumë 100, që jep mesataren 20.

**Zhvillo llogaritjen**

Rrjedha Pishë ka amplitudë 4 dhe $s=\sqrt{10/4}=1.58$.

Rrjedha Gur ka amplitudë 20 dhe $s=\sqrt{250/4}=7.91$.

**Interpreto dhe kontrollo rezultatin**

Kohët e përfundimit janë të grupuara shumë më ngushtë për Rrjedhën Pishë.

Raportimi se «të dyja kanë mesatare 20 minuta» do ta fshihte ndryshueshmërinë operative që mund të ketë rëndësi për planifikimin.

### T01-A09-V03: Dy grupe të të folurit publik

**Arsyeto para llogaritjes**

Të dyja grupet kanë shumë 50, prandaj $\bar{x}=10$.

**Zhvillo llogaritjen**

Amplituda e Grupit Koral është $13-7=6$, me SD të korrigjuar të kampionit $s=\sqrt{20/(5-1)}=2.24$.

**Interpreto dhe kontrollo rezultatin**

Amplituda e Grupit Rrasë është $18-2=16$, me SD të korrigjuar të kampionit $s=\sqrt{200/(5-1)}=7.07$.

E njëjta qendër bashkëjeton me vlera shumë të ndryshme në skajin e poshtëm dhe të sipërm, prandaj mesatarja nuk mund ta përshkruajë qëndrueshmërinë.

### T01-A09-V04: Dy orare aktivitetesh komunitare

**Arsyeto para llogaritjes**

Secili grup ka shumë 150 dhe mesatare 30 minuta.

**Zhvillo llogaritjen**

Orari Lis ka amplitudë 4 dhe $s=\sqrt{10/4}=1.58$.

**Interpreto dhe kontrollo rezultatin**

Orari Kallam ka amplitudë 40 dhe $s=\sqrt{1000/4}=15.81$.

Orari Lis është më homogjen, sepse aktivitetet e tij mbeten pranë 30, ndërsa Orari Kallam shtrihet nga 10 deri në 50.

### T01-A09-V05: Dy modele të korrash në kopsht

**Arsyeto para llogaritjes**

Të dyja modelet kanë total 30, prandaj të dyja mesataret janë 6.

**Zhvillo llogaritjen**

Modeli Diell ka amplitudë $10-2=8$, me $s=\sqrt{40/4}=3.16$.

Modeli Hije ka amplitudë 12, me $s=\sqrt{144/4}=6.00$.

**Interpreto dhe kontrollo rezultatin**

Modeli Hije ka gjithashtu vlera të skajshme të përsëritura në 0 dhe 12, në vend të largësive të njëtrajtshme.

Mesatarja fsheh si shpërhapjen më të madhe, ashtu edhe formën e ndryshme.

### T01-A09-V06: Dy rrugë vizitash në muze

**Arsyeto para llogaritjes**

Të dyja rrugët kanë shumë 250, që jep mesataren 50 minuta.

**Zhvillo llogaritjen**

Rruga Qelq ka amplitudë 4 dhe $s=\sqrt{10/4}=1.58$.

Rruga Dru ka amplitudë 60 dhe $s=\sqrt{2250/4}=23.72$.

**Interpreto dhe kontrollo rezultatin**

Kohët e Rrugës Qelq grupohen ngushtë dhe janë të parashikueshme rreth 50; kohët e Rrugës Dru mund të jenë 30 minuta nën ose mbi këtë vlerë.

Prandaj, kohëzgjatja mesatare e barabartë nuk nënkupton përvojë të ngjashme për vizitorët.

### T01-A09-V07: Dy seminare të historisë lokale

**Arsyeto para llogaritjes**

Të dyja totalet janë 75, prandaj mesatarja është 15 pjesëmarrës.

**Zhvillo llogaritjen**

Seminari Bojë ka amplitudë 8 dhe $s=\sqrt{40/4}=3.16$.

**Interpreto dhe kontrollo rezultatin**

Seminari Letër ka amplitudë 24 dhe $s=\sqrt{360/4}=9.49$.

Organizatori nuk do ta dallonte se pjesëmarrja në Seminarin Letër luhatet tri herë më shumë në njësi të SD-së, gjë që ndikon në personelin e nevojshëm edhe pse pjesëmarrja mesatare përputhet.

### T01-A09-V08: Dy dritare vrojtimi bregdetar

**Arsyeto para llogaritjes**

Secila dritare ka total 370, që jep mesataren 74 vrojtime.

**Zhvillo llogaritjen**

Amplituda e Dritares Agim është $78-70=8$, me SD të korrigjuar të kampionit $s=\sqrt{40/(5-1)}=3.16$.

Amplituda e Dritares Muzg është $98-50=48$, me SD të korrigjuar të kampionit $s=\sqrt{1440/(5-1)}=18.97$.

**Interpreto dhe kontrollo rezultatin**

Dritarja Agim është shumë më e qëndrueshme.

Qendra e përbashkët nuk tregon asgjë për këtë dallim gjashtëfish të amplitudës.

### T01-A09-V09: Dy vargje provash

**Arsyeto para llogaritjes**

Të dyja vargjet kanë shumë 25 dhe ndryshim mesatar 5.

**Zhvillo llogaritjen**

Vargu Kambanë ka amplitudë 8 dhe $s=\sqrt{40/4}=3.16$.

Vargu Daulle ka amplitudë 24 dhe $s=\sqrt{360/4}=9.49$.

**Interpreto dhe kontrollo rezultatin**

Vlerat negative janë ndryshime të vlefshme nën nivelin bazë.

Vargu Daulle ka ndryshueshmëri tri herë më të madhe në njësi të SD-së, pavarësisht ndryshimit mesatar identik.

### T01-A09-V10: Dy rrugë dërgesash

**Arsyeto para llogaritjes**

Të dyja grupet kanë total 125, prandaj secila mesatare është 25 minuta.

**Zhvillo llogaritjen**

Rruga Limon ka amplitudë 4 dhe $s=\sqrt{10/4}=1.58$.

**Interpreto dhe kontrollo rezultatin**

Rruga Kumbull ka amplitudë 40 dhe $s=\sqrt{1000/4}=15.81$.

Kohët e Rrugës Limon janë në aspektin përshkrues më të parashikueshme, sepse grupohen pranë mesatares; nuk është përcaktuar asnjë arsye shkakësore për këtë dallim.

## A10: Transformimet lineare të mesatares, variancës dhe SD-së

### T01-A10-V01: Rishkallëzimi i një indeksi angazhimi

**Përgatit llogaritjen**

Këtu $a=5$, $b=2$ dhe $s_x=\sqrt{9}=3$.

**Zhvillo llogaritjen**

Prandaj $\bar{y}=5+2(12)=29$, $s_y^2=2^2(9)=36$ dhe $s_y=|2|(3)=6$.

**Interpreto dhe kontrollo rezultatin**

Shtimi i 5 e zhvendos çdo vlerë dhe mesataren me 5; shumëzimi me 2 i dyfishon të gjitha devijimet dhe e katërfishon mesataren e katrorëve të tyre.

### T01-A10-V02: Shndërrimi i një pikëzimi kohe

**Përgatit llogaritjen**

Me $a=-3$, $b=0.5$ dhe $s_x=4$, $\bar{y}=-3+0.5(20)=7$.

**Zhvillo llogaritjen**

Varianca është $s_y^2=0.5^2(16)=4$ dhe $s_y=0.5(4)=2$.

**Interpreto dhe kontrollo rezultatin**

Shumëzimi me 0.5 e përgjysmon secilën largësi nga mesatarja; konstantja mbledhëse e zhvendos shkallën pa ndikuar në shpërhapje.

### T01-A10-V03: Përmbysja e një shkalle cilësie

**Përgatit llogaritjen**

Këtu $a=40$, $b=-3$ dhe $s_x=5$.

**Zhvillo llogaritjen**

Prandaj $\bar{y}=40-3(8)=16$, $s_y^2=(-3)^2(25)=225$ dhe $s_y=|-3|(5)=15$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia negative e përmbys renditjen.

Shpërhapja mbetet jonegative, sepse largësitë përdorin madhësinë absolute dhe largësitë në katror përdorin $(-3)^2$.

### T01-A10-V04: Zgjerimi i një pikëzimi pjesëmarrjeje

**Përgatit llogaritjen**

SD-ja fillestare është $s_x=\sqrt{4}=2$.

**Zhvillo llogaritjen**

Zëvendësimi jep $\bar{y}=10+4(15)=70$, $s_y^2=4^2(4)=64$ dhe $s_y=4(2)=8$.

**Interpreto dhe kontrollo rezultatin**

Shtimi i 10 ndikon vetëm në mesatare.

Shumëzimi me 4 e shumëzon SD-në me 4 dhe variancën me 16.

### T01-A10-V05: Rikalibrimi i një indeksi terreni

**Përgatit llogaritjen**

SD-ja fillestare është $s_x=\sqrt{36}=6$.

**Zhvillo llogaritjen**

Me $a=-5$ dhe $b=1.5$, $\bar{y}=-5+1.5(30)=40$, $s_y^2=1.5^2(36)=2.25(36)=81$ dhe $s_y=1.5(6)=9$.

**Interpreto dhe kontrollo rezultatin**

Zhvendosja e ul çdo pikëzim të transformuar me 5 pas shkallëzimit, por nuk e ndryshon shpërhapjen.

### T01-A10-V06: Pasqyrimi i një shkalle përgjigjesh

**Përgatit llogaritjen**

Meqë $s_x=\sqrt{49}=7$, $\bar{y}=2-2(6)=-10$, $s_y^2=(-2)^2(49)=196$ dhe $s_y=|-2|(7)=14$.

**Zhvillo llogaritjen**

Faktori $-2$ e përmbys renditjen dhe i dyfishon largësitë; shtimi i 2 pastaj e zhvendos çdo vlerë të transformuar në mënyrë të barabartë.

**Interpreto dhe kontrollo rezultatin**

As varianca, as SD-ja nuk janë negative.

### T01-A10-V07: Ngjeshja e një indeksi arkivi

**Përgatit llogaritjen**

SD-ja fillestare është 8.

**Zhvillo llogaritjen**

Prandaj $\bar{y}=100+0.25(50)=112.5$, $s_y^2=0.25^2(64)=4$ dhe $s_y=0.25(8)=2$.

**Interpreto dhe kontrollo rezultatin**

Një shumëzues prej një të katërtës e zvogëlon secilin devijim në një të katërtën dhe variancën në një të gjashtëmbëdhjetën.

Zhvendosja me 100 njësi ndryshon vetëm vendndodhjen.

### T01-A10-V08: Zhvendosja e një pikëzimi të ruajtjes së natyrës

**Përgatit llogaritjen**

Me $s_x=10$, $a=-20$ dhe $b=1.2$, $\bar{y}=-20+1.2(18)=1.6$.

**Zhvillo llogaritjen**

Gjithashtu, $s_y^2=1.2^2(100)=144$ dhe $s_y=1.2(10)=12$.

**Interpreto dhe kontrollo rezultatin**

Termi $-20$ e zhvendos qendrën, por i lë devijimet të pandryshuara; 1.2 e rrit SD-në me 20% dhe variancën me 44%.

### T01-A10-V09: Zmadhimi i një shkalle të shkurtër vlerësimi

**Përgatit llogaritjen**

SD-ja fillestare është $s_x=\sqrt{1.44}=1.2$.

**Zhvillo llogaritjen**

Prandaj $\bar{y}=7+5(9)=52$, $s_y^2=5^2(1.44)=36$ dhe $s_y=5(1.2)=6$ njësi të shkallës së re.

**Interpreto dhe kontrollo rezultatin**

Vlera mbledhëse 7 nuk hyn në asnjërën formulë të shpërhapjes.

### T01-A10-V10: Përmbysja dhe zvogëlimi i një indeksi kohëzgjatjeje

**Përgatit llogaritjen**

SD-ja fillestare është $s_x=\sqrt{121}=11$.

**Zhvillo llogaritjen**

Zëvendësimi jep $\bar{y}=3-0.8(42)=-30.6$, $s_y^2=(-0.8)^2(121)=0.64(121)=77.44$ dhe $s_y=0.8(11)=8.8$.

**Interpreto dhe kontrollo rezultatin**

Ngritja në katror e heq shenjën, sepse varianca mat largësitë në katror; shenja negative vetëm e përmbys renditjen.

## A11: Standardizimi z

### T01-A11-V01: Standardizimi i numrit të leximeve

**Përgatit llogaritjen**

Mesatarja është $\bar{x}=70/5=14$.

**Zhvillo llogaritjen**

Devijimet në katror janë $16,4,0,4,16$, prandaj $s_x=\sqrt{40/4}=\sqrt{10}=3.162$.

Zëvendësimi jep $z=(-4/\sqrt{10},-2/\sqrt{10},0,2/\sqrt{10},4/\sqrt{10})$, ose $(-1.265,-0.632,0.000,0.632,1.265)$.

**Interpreto dhe kontrollo rezultatin**

Shuma e tyre e saktë është 0 dhe shuma e katrorëve është 4, duke verifikuar mesataren 0 dhe SD-në e kampionit 1.

Rrumbullakimi i vlerave të paraqitura mund të krijojë një shmangie të vogël nga këto rezultate të sakta.

### T01-A11-V02: Standardizimi i totalit të katalogut

**Përgatit llogaritjen**

Totali është 135, prandaj $\bar{x}=27$.

**Zhvillo llogaritjen**

Devijimet $(-3,-1,1,1,2)$ kanë shumë katrorësh 16, që jep $s_x=\sqrt{16/4}=2$.

Kështu $z=(-1.500,-0.500,0.500,0.500,1.000)$.

**Interpreto dhe kontrollo rezultatin**

Shuma e pikëzimeve z është 0 dhe shuma e katrorëve të tyre është 4, prandaj $\bar{z}=0$ dhe $s_z=1$.

Totali më i vogël gjendet 1.5 SD të kampionit nën mesatare; më i madhi gjendet 1 SD mbi të.

### T01-A11-V03: Standardizimi i kohëzgjatjeve të seminarit

**Përgatit llogaritjen**

Mesatarja është $\bar{x}=60/5=12$.

**Zhvillo llogaritjen**

Devijimet në katror janë $25,0,1,1,9$, me total 36, prandaj $s_x=\sqrt{36/4}=3$.

**Interpreto dhe kontrollo rezultatin**

Vlerat e standardizuara janë $(-5/3,0,1/3,1/3,1)$, ose $(-1.667,0.000,0.333,0.333,1.000)$.

Pikëzimet z të sakta kanë shumë 0 dhe shumë katrorësh $25/9+1/9+1/9+1=4$, gjë që verifikon mesataren 0 dhe SD-në e kampionit 1.

### T01-A11-V04: Standardizimi i indekseve të rrjedhës së vizitorëve

**Përgatit llogaritjen**

Totali është 225, që jep $\bar{x}=45$.

**Zhvillo llogaritjen**

Devijimet $(-5,-2,-1,3,5)$ kanë shumë katrorësh 64, prandaj $s_x=\sqrt{64/4}=4$.

Kështu $z=(-1.250,-0.500,-0.250,0.750,1.250)$.

**Interpreto dhe kontrollo rezultatin**

Shuma e tyre e saktë është 0 dhe shuma e katrorëve është 4, që jep $\bar{z}=0$ dhe $s_z=1$.

Një vlerë me $z=0$ do të ishte e barabartë me mesataren fillestare 45; ky grup të dhënash nuk ka asnjë vlerë të vrojtuar pikërisht në atë mesatare.

### T01-A11-V05: Standardizimi i matjeve të madhësisë së arkivit

**Përgatit llogaritjen**

Mesatarja është $\bar{x}=570/5=114$.

**Zhvillo llogaritjen**

Devijimet $(-8,-1,1,3,5)$ kanë shumë katrorësh 100, prandaj $s_x=\sqrt{100/4}=5$.

Pikëzimet z janë $(-1.600,-0.200,0.200,0.600,1.000)$.

**Interpreto dhe kontrollo rezultatin**

Shuma e tyre është 0 dhe shuma e katrorëve të tyre është 4, duke verifikuar mesataren 0 dhe SD-në e kampionit 1.

Për shembull, 117 ka $z=(117-114)/5=0.600$, ose 0.6 SD mbi mesatare.

### T01-A11-V06: Standardizimi i totalit të vrojtimeve në terren

**Përgatit llogaritjen**

Totali është 115, prandaj $\bar{x}=23$.

**Zhvillo llogaritjen**

Devijimet $(-9,-2,1,3,7)$ kanë shumë katrorësh 144 dhe $s_x=\sqrt{144/4}=6$.

Prandaj $z=(-1.500,-0.333,0.167,0.500,1.167)$.

**Interpreto dhe kontrollo rezultatin**

Duke përdorur thyesat e sakta, pikëzimet z kanë shumë 0 dhe shumë katrorësh 4, që jep mesataren 0 dhe SD-në e kampionit 1.

Shenjat negative tregojnë totalet nën 23; shenjat pozitive tregojnë totalet mbi 23.

### T01-A11-V07: Standardizimi i gjatësive të provave

**Përgatit llogaritjen**

Mesatarja është $\bar{x}=300/5=60$.

**Zhvillo llogaritjen**

Devijimet $(-9,-5,1,5,8)$ kanë shumë katrorësh 196, prandaj $s_x=\sqrt{196/4}=7$.

Pikëzimet z janë $(-1.286,-0.714,0.143,0.714,1.143)$.

**Interpreto dhe kontrollo rezultatin**

Shuma e tyre e saktë është 0 dhe shuma e katrorëve është $196/49=4$, duke verifikuar mesataren dhe SD-në e standardizuar.

Një gjatësi 68 është $(68-60)/7=1.143$ SD të kampionit mbi mesatare.

### T01-A11-V08: Standardizimi i numrit të aktiviteteve komunitare

**Përgatit llogaritjen**

Shuma është 155, që jep $\bar{x}=31$.

**Zhvillo llogaritjen**

Devijimet në katror $(100,36,4,16,100)$ kanë total 256, prandaj $s_x=\sqrt{256/4}=8$.

Kështu $z=(-1.250,-0.750,0.250,0.500,1.250)$.

**Interpreto dhe kontrollo rezultatin**

Shuma e tyre e saktë është 0 dhe shuma e katrorëve është 4, prandaj $\bar{z}=0$ dhe $s_z=1$.

Pjesëtimi i një diference me një SD e anulon njësinë fillestare të matjes, duke lënë një pozicion relativ pa njësi.

### T01-A11-V09: Standardizimi i kohëve të digjitalizimit

**Përgatit llogaritjen**

Mesatarja është $\bar{x}=450/5=90$ minuta.

**Zhvillo llogaritjen**

Devijimet $(-7,-3,1,4,5)$ kanë shumë katrorësh 100, që jep $s_x=\sqrt{100/4}=5$ minuta.

Pikëzimet z janë $(-1.400,-0.600,0.200,0.800,1.000)$.

**Interpreto dhe kontrollo rezultatin**

Shuma e tyre e saktë është 0 dhe shuma e katrorëve të tyre është 4, duke verifikuar mesataren 0 dhe SD-në e kampionit 1.

Vrojtimi prej 83 minutash gjendet 1.4 SD të kampionit nën mesatare.

### T01-A11-V10: Standardizimi i totalit të vëllimit të anketës

**Përgatit llogaritjen**

Totali është 720, prandaj $\bar{x}=144$.

**Zhvillo llogaritjen**

Devijimet $(-7,-3,-1,2,9)$ kanë shumë katrorësh 144 dhe $s_x=\sqrt{144/4}=6$.

Prandaj $z=(-1.167,-0.500,-0.167,0.333,1.500)$.

**Interpreto dhe kontrollo rezultatin**

Pikëzimet z të sakta në formë thyese kanë shumë 0 dhe shumë katrorësh 4, që jep $\bar{z}=0$ dhe $s_z=1$.

Totalet 146 dhe 153 gjenden mbi mesatare dhe, prandaj, kanë pikëzime z pozitive.

## A14: Ndërtimi dhe interpretimi i një histogrami dhe i një diagrami kuti-me-mustaqe

### T01-A14-V01: Kohëzgjatjet e sesioneve të rrethit të leximit

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[0,5)$ | 3 | 0.30 | 5 | 0.06 |
| $[5,10)$ | 5 | 0.50 | 5 | 0.10 |
| $[10,15)$ | 1 | 0.10 | 5 | 0.02 |
| $[15,20]$ | 1 | 0.10 | 5 | 0.02 |

Mediana është $(6+7)/2=6.5$ dhe moda është 4.

**Zhvillo llogaritjen**

Mediana e gjysmës së poshtme jep $Q_1=4$; mediana e gjysmës së sipërme jep $Q_3=9$.

Prandaj $\mathrm{IQR}=9-4=5$, me kufij $4-1.5(5)=-3.5$ dhe $9+1.5(5)=16.5$.

**Interpreto dhe kontrollo rezultatin**

Mustaqet e Tukey-t përfundojnë në 3 dhe 10; 18 sinjalizohet.

Histogrami tregon se shumica e sesioneve janë nën 10 dhe se ka një bisht të rrallë djathtas; diagrami kuti-me-mustaqe thekson 50% të vlerave në mes dhe e veçon 18.

### T01-A14-V02: Kohët e gjetjes së materialeve në arkiv

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[10,15)$ | 5 | 0.50 | 5 | 0.10 |
| $[15,20)$ | 4 | 0.40 | 5 | 0.08 |
| $[20,25)$ | 0 | 0.00 | 5 | 0.00 |
| $[25,30]$ | 1 | 0.10 | 5 | 0.02 |

Moda është 13.

**Zhvillo llogaritjen**

Përmbledhja me pesë numra është minimumi 11, $Q_1=13$, mediana $(14+15)/2=14.5$, $Q_3=17$ dhe maksimumi 27.

Prandaj $\mathrm{IQR}=17-13=4$.

**Interpreto dhe kontrollo rezultatin**

Kufijtë janë $13-1.5(4)=7$ dhe $17+1.5(4)=23$.

Mustaqet e Tukey-t përfundojnë në 11 dhe 18; 27 sinjalizohet.

Klasa e zbrazët 20–25 e bën të qartë veçimin e vlerës së lartë në histogram; diagrami kuti-me-mustaqe e përmbledh në mënyrë të ngjeshur këtë veçim.

### T01-A14-V03: Kohët e plotësimit të anketës komunitare

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[20,25)$ | 6 | 0.60 | 5 | 0.12 |
| $[25,30)$ | 3 | 0.30 | 5 | 0.06 |
| $[30,35)$ | 0 | 0.00 | 5 | 0.00 |
| $[35,40]$ | 1 | 0.10 | 5 | 0.02 |

Mediana është $(23+24)/2=23.5$; moda është 23.

**Zhvillo llogaritjen**

Kuartilet janë $Q_1=22$ dhe $Q_3=26$, prandaj $\mathrm{IQR}=4$.

Kufijtë janë 16 dhe 32.

**Interpreto dhe kontrollo rezultatin**

Mustaqet e Tukey-t përfundojnë në 20 dhe 27; 36 sinjalizohet mbi kufirin e sipërm.

Të dy grafikët tregojnë një grupim të përqendruar poshtë dhe asimetri djathtas; asnjëri nuk vërteton një formë të shpërndarjes së popullatës.

### T01-A14-V04: Kohëzgjatjet e ndalesave në galeri

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[5,10)$ | 6 | 0.60 | 5 | 0.12 |
| $[10,15)$ | 3 | 0.30 | 5 | 0.06 |
| $[15,20)$ | 0 | 0.00 | 5 | 0.00 |
| $[20,25]$ | 1 | 0.10 | 5 | 0.02 |

**Zhvillo llogaritjen**

Mediana është $(8+9)/2=8.5$ dhe 7 është moda.

Me $Q_1=7$ dhe $Q_3=11$, $\mathrm{IQR}=4$, kufiri i poshtëm është $1$ dhe kufiri i sipërm është $17$.

**Interpreto dhe kontrollo rezultatin**

Mustaqet e Tukey-t përfundojnë në 5 dhe 12; ndalesa prej 21 minutash identifikohet si vlerë e mundshme e veçuar.

Histogrami nxjerr në pah klasën e zbrazët para vlerës 21; diagrami kuti-me-mustaqe përmbledh shpërhapjen e shprehur nga kuartilet dhe e shënon drejtpërdrejt vlerën e veçuar.

### T01-A14-V05: Numërimet ditore të katalogimit

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[30,35)$ | 6 | 0.60 | 5 | 0.12 |
| $[35,40)$ | 3 | 0.30 | 5 | 0.06 |
| $[40,45)$ | 0 | 0.00 | 5 | 0.00 |
| $[45,50]$ | 1 | 0.10 | 5 | 0.02 |

Mediana është $(33+34)/2=33.5$ dhe moda është 33.

**Zhvillo llogaritjen**

Kuartilet janë 32 dhe 36, që japin $\mathrm{IQR}=4$ dhe kufijtë 26 dhe 42.

Mustaqet e Tukey-t përfundojnë në 30 dhe 37; 47 sinjalizohet.

**Interpreto dhe kontrollo rezultatin**

Histogrami tregon një boshllëk në anën e djathtë dhe një klasë të sipërme të veçuar.

Diagrami kuti-me-mustaqe tregon të njëjtën asimetri djathtas përmes pikës së largët të sinjalizuar, ndërsa i ngjesh hollësitë në nivel klasash.

### T01-A14-V06: Kërkesat për ndihmë në lagje

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[0,5)$ | 3 | 0.30 | 5 | 0.06 |
| $[5,10)$ | 6 | 0.60 | 5 | 0.12 |
| $[10,15)$ | 0 | 0.00 | 5 | 0.00 |
| $[15,20]$ | 1 | 0.10 | 5 | 0.02 |

**Zhvillo llogaritjen**

Mediana është $(5+6)/2=5.5$ dhe moda është 5.

Kuartilet e dy gjysmave të kampionit janë $Q_1=4$ dhe $Q_3=8$, prandaj $\mathrm{IQR}=4$ dhe kufijtë janë $-2$ dhe 14.

**Interpreto dhe kontrollo rezultatin**

Mustaqet e Tukey-t përfundojnë në 2 dhe 9; 16 identifikohet si vlerë e mundshme e veçuar.

Histogrami ruan numërimet brenda klasave; diagrami kuti-me-mustaqe përmbledh qendrën e bazuar në renditje, shpërhapjen e pjesës qendrore të të dhënave dhe pikën e sipërme të veçuar.

### T01-A14-V07: Kohëzgjatjet e klipeve zanore

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[40,45)$ | 6 | 0.60 | 5 | 0.12 |
| $[45,50)$ | 3 | 0.30 | 5 | 0.06 |
| $[50,55)$ | 0 | 0.00 | 5 | 0.00 |
| $[55,60]$ | 1 | 0.10 | 5 | 0.02 |

**Zhvillo llogaritjen**

Mediana është $(43+44)/2=43.5$ sekonda dhe moda është 43.

Kuartilet janë 42 dhe 46, prandaj $\mathrm{IQR}=4$, me kufij 36 dhe 52.

**Interpreto dhe kontrollo rezultatin**

Mustaqet e Tukey-t përfundojnë në 40 dhe 47; klipi prej 58 sekondash sinjalizohet.

Grafikët mbështetin përshkrimin e një vlere të sipërme të veçuar, jo fshirjen automatike të saj; burimi dhe vlefshmëria përmbajtësore e saj ende duhen shqyrtuar.

### T01-A14-V08: Totalet e aktiviteteve të punëtorisë

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[10,15)$ | 3 | 0.30 | 5 | 0.06 |
| $[15,20)$ | 6 | 0.60 | 5 | 0.12 |
| $[20,25)$ | 0 | 0.00 | 5 | 0.00 |
| $[25,30]$ | 1 | 0.10 | 5 | 0.02 |

Mediana është $(15+16)/2=15.5$ dhe 15 është moda.

**Zhvillo llogaritjen**

$Q_1=14$, $Q_3=18$ dhe $\mathrm{IQR}=4$, që japin kufijtë 8 dhe 24.

Mustaqet e Tukey-t përfundojnë në 12 dhe 19; 29 sinjalizohet.

**Interpreto dhe kontrollo rezultatin**

Në këtë kampion, shumica e totaleve shtrihen nga 12 deri në 19, me një rezultat të lartë të veçuar.

Nga dhjetë vrojtime nuk përligjet asnjë supozim për shpërndarjen e popullatës.

### T01-A14-V09: Numri i rreshtave në shënimet e terrenit

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[60,65)$ | 6 | 0.60 | 5 | 0.12 |
| $[65,70)$ | 3 | 0.30 | 5 | 0.06 |
| $[70,75)$ | 0 | 0.00 | 5 | 0.00 |
| $[75,80]$ | 1 | 0.10 | 5 | 0.02 |

**Zhvillo llogaritjen**

Mediana është $(63+64)/2=63.5$ dhe moda është 63.

Kuartilet 62 dhe 66 japin $\mathrm{IQR}=4$, kufirin e poshtëm 56 dhe kufirin e sipërm 72.

**Interpreto dhe kontrollo rezultatin**

Mustaqet e Tukey-t përfundojnë në 60 dhe 67; 77 identifikohet si vlerë e mundshme e veçuar.

Histogrami tregon klasën e zbrazët para vlerës 77, ndërsa diagrami kuti-me-mustaqe përmbledh qendrën, shpërhapjen e pjesës qendrore të të dhënave dhe vlerën e mundshme të veçuar.

### T01-A14-V10: Madhësitë e porosive të kooperativës

**Përgatit llogaritjen**

| Klasa | $n_j$ | $p_j$ | Gjerësia | $h_j$ |
|---|---:|---:|---:|---:|
| $[20,25)$ | 1 | 0.10 | 5 | 0.02 |
| $[25,30)$ | 6 | 0.60 | 5 | 0.12 |
| $[30,35)$ | 2 | 0.20 | 5 | 0.04 |
| $[35,40)$ | 0 | 0.00 | 5 | 0.00 |
| $[40,45]$ | 1 | 0.10 | 5 | 0.02 |

**Zhvillo llogaritjen**

Mediana është $(27+28)/2=27.5$ dhe 27 është moda.

$Q_1=26$, $Q_3=30$ dhe $\mathrm{IQR}=4$, prandaj kufijtë janë 20 dhe 36.

**Interpreto dhe kontrollo rezultatin**

Mustaqet e Tukey-t përfundojnë në 24 dhe 31; 41 sinjalizohet.

Histogrami tregon një interval të dendur 25–30 dhe një boshllëk sipër; diagrami kuti-me-mustaqe tregon se 41 gjendet përtej kufirit, duke ruajtur njëkohësisht përmbledhjen e gjysmës qendrore.

## A15: Krahasimi i gjerësive dhe pikave të nisjes së klasave të histogramit

### T01-A15-V01: Totalet e elementeve të punëtorisë me dy gjerësi klasash

**Përgatit llogaritjen**

Skema A ka frekuencat $(2,5,4,1)$.

Me gjerësi 4, dendësitë janë $(0.0417,0.1042,0.0833,0.0208)$.

**Zhvillo llogaritjen**

Skema B ka frekuencat $(2,3,2,2,2,1)$; gjerësia 2 jep dendësitë $(0.0833,0.1250,0.0833,0.0833,0.0833,0.0417)$.

Të dyja kanë total 12.

**Interpreto dhe kontrollo rezultatin**

Paraqitja me klasa të gjera thekson një përqendrim të përgjithshëm 4–8; paraqitja e hollësishme tregon se pjesa 4–6 përmban më shumë vrojtime.

Vetë të dhënat janë të pandryshuara.

### T01-A15-V02: Kohët e gjetjes së materialeve me pika nisjeje të zhvendosura

**Përgatit llogaritjen**

Frekuencat e Skemës A janë $(4,5,3)$, me dendësitë për klasat me gjerësi 5 $(0.0667,0.0833,0.0500)$.

**Zhvillo llogaritjen**

Skema B e zhvendosur ka frekuencat $(2,5,5)$, që japin dendësitë $(0.0333,0.0833,0.0833)$.

**Interpreto dhe kontrollo rezultatin**

Caktimi sipas kufijve i zhvendos vrojtimet ndërmjet shtyllave, duke e kthyer një kulm të dukshëm në mes në dy shtylla të sipërme të barabarta.

Asnjëri histogram nuk vërteton i vetëm një nënpopullatë të veçantë; raporto pikën e nisjes dhe shqyrto nëse modeli vazhdon në zgjedhje të mbrojtshme.

### T01-A15-V03: Numri i vizitorëve me klasa të gjera dhe të ngushta

**Përgatit llogaritjen**

Për Skemën A, frekuencat $(5,4,3)$ dhe gjerësia 5 japin dendësitë $(0.0833,0.0667,0.0500)$.

**Zhvillo llogaritjen**

Frekuencat e Skemës B janë $(3,2,2,3,1,1)$.

Pjesëtimi i secilës me $12(3)=36$ jep $(0.0833,0.0556,0.0556,0.0833,0.0278,0.0278)$.

**Interpreto dhe kontrollo rezultatin**

Klasat më të ngushta tregojnë përqendrime lokale në 29–32 dhe 38–41, të cilat i fsheh vargu në rënie me klasa të gjera.

Me vetëm 12 vlera, këto veçori duhen përshkruar me kujdes.

### T01-A15-V04: Kohët e leximit me klasa prej katër njësish dhe pikë nisjeje të zhvendosur

**Përgatit llogaritjen**

Numërimet e Skemës A janë $(3,5,4)$, prandaj dendësitë për klasat me gjerësi 4 janë $(0.0625,0.1042,0.0833)$.

**Zhvillo llogaritjen**

Numërimet e Skemës B janë $(1,4,5,2)$, me dendësitë $(0.0208,0.0833,0.1042,0.0417)$.

**Interpreto dhe kontrollo rezultatin**

Zhvendosja e pikës së nisjes me 2 njësi ndryshon cilat vrojtime ndodhen në të njëjtën klasë dhe e zhvendos shtyllën më të lartë nga 8–12 në 10–14.

Ajo nuk ndryshon asnjë kohë leximi dhe nuk mbështet një qendër tjetër numerike.

### T01-A15-V05: Intervalet e dërgesave në dy nivele hollësie

**Përgatit llogaritjen**

Frekuencat e Skemës A janë $(3,4,4,1)$.

**Zhvillo llogaritjen**

Me gjerësi 8, dendësitë janë $(0.0313,0.0417,0.0417,0.0104)$.

Skema B vendos dy vrojtime në secilën prej gjashtë klasave; prandaj gjerësia 4 jep dendësinë $2/[12(4)]=0.0417$ në secilën klasë.

**Interpreto dhe kontrollo rezultatin**

Paraqitja më e hollësishme zbulon çifte me largësi të njëtrajtshme, ndërsa klasat e gjera krijojnë numërime më të ulëta në skaje, sepse kufijtë e tyre shtrihen përtej shtrirjes së vrojtuar.

Të dyja e ruajnë sipërfaqen totale 1.

### T01-A15-V06: Indekset e katalogut me klasa prej gjashtë njësish dhe pikë nisjeje të zhvendosur

**Përgatit llogaritjen**

Frekuencat e Skemës A $(4,4,3,1)$ japin dendësitë $(0.0556,0.0556,0.0417,0.0139)$.

**Zhvillo llogaritjen**

Frekuencat e Skemës B $(2,4,4,2)$ japin $(0.0278,0.0556,0.0556,0.0278)$, sepse secila klasë ka gjerësi 6.

**Interpreto dhe kontrollo rezultatin**

Pika e parë e nisjes sugjeron zvogëlim drejt skajit të lartë; pika e zhvendosur e nisjes duket më e baraspeshuar.

Kjo ndjeshmëri tregon se duhen shqyrtuar vrojtimet dhe më shumë se një pikë nisjeje e arsyeshme nga ana përmbajtësore.

### T01-A15-V07: Numërimet e anketës me gjerësi prej pesë dhe tri njësish

**Përgatit llogaritjen**

Skema A ka frekuencat $(5,3,3,1)$; pjesëtimi me $12(5)=60$ jep dendësitë $(0.0833,0.0500,0.0500,0.0167)$.

**Zhvillo llogaritjen**

Skema B ka frekuencat $(3,2,2,2,2,1)$; pjesëtimi me 36 jep $(0.0833,0.0556,0.0556,0.0556,0.0556,0.0278)$.

**Interpreto dhe kontrollo rezultatin**

Klasa e parë e gjerë i bashkon vlerat e përsëritura 20 me vlerat deri në 24, duke e bërë përqendrimin në skajin e poshtëm të duket më i gjerë.

Pamja më e hollësishme e vendos atë më saktë.

### T01-A15-V08: Kohëzgjatjet e aktiviteteve me pikë të zhvendosur nisjeje

**Përgatit llogaritjen**

Frekuencat e Skemës A janë $(3,4,4,1)$, që japin dendësitë për klasat me gjerësi 6 $(0.0417,0.0556,0.0556,0.0139)$.

**Zhvillo llogaritjen**

Frekuencat e Skemës B janë $(1,4,4,3)$, që japin $(0.0139,0.0556,0.0556,0.0417)$.

**Interpreto dhe kontrollo rezultatin**

Bishti që duket i rrallë ndërron anë kur zhvendoset pika e nisjes, edhe pse dy shtyllat qendrore mbeten të barabarta.

Prandaj çdo pohim për asimetri nga një pikë e vetme nisjeje e klasave do të ishte i brishtë.

### T01-A15-V09: Totale skanimesh me largësi të barabarta

**Përgatit llogaritjen**

Secila nga tri klasat e Skemës A përmban 4 vrojtime, prandaj secila dendësi është $4/[12(12)]=0.0278$.

**Zhvillo llogaritjen**

Secila nga gjashtë klasat e Skemës B përmban 2 vrojtime, prandaj secila dendësi është $2/[12(6)]=0.0278$.

**Interpreto dhe kontrollo rezultatin**

Të dyja pamjet mbështetin një mbulim të njëtrajtshëm në të gjithë shtrirjen e paraqitur.

Këtu përfundimi është i qëndrueshëm, sepse largësitë përputhen në mënyrë të njëtrajtshme në të dy nivelet e hollësisë, megjithëse histogrami përsëri përmbledh në vend që t'i riprodhojë vlerat e sakta.

### T01-A15-V10: Grupime në kohëzgjatjet e itinerareve

**Përgatit llogaritjen**

Frekuencat e skemës A janë $(6,4,2)$; gjerësia 10 jep dendësitë $(0.0500,0.0333,0.0167)$, duke krijuar përshtypjen e një rënieje.

**Zhvillo llogaritjen**

Skema B ka frekuencat $(3,3,3,3)$; gjerësia 6 jep dendësinë $3/[12(6)]=0.0417$ në secilën klasë.

**Interpreto dhe kontrollo rezultatin**

Kufijtë e skemës B e vendosin secilin prej katër grupimeve me nga tri vlera në një klasë më vete dhe i fshehin boshllëqet ndërmjet tyre, ndërsa pamja me klasa të gjera i bashkon dy grupimet e para.

Një diagram me pika pranë cilitdo histogram do ta bënte të dukshëm grupimin e saktë.
