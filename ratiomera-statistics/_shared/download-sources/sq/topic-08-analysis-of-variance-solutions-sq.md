---
title: "Zgjidhjet e plota"
subtitle: "Analiza e variancës"
document-id: "topic-08-analysis-of-variance-solutions-sq"
topic-id: "topic-08-analysis-of-variance"
topic-number: "08"
topic-slug: "analysis-of-variance"
document-type: "solutions"
locale: "sq"
paired-document-id: "topic-08-analysis-of-variance-exercises-sq"
---

Këto zgjidhje të plota përdorin të njëjtat kode dhe të njëjtën renditje si Fleta e ushtrimeve. Vlerat ndërmjetëse ruhen deri te hapi i treguar i rrumbullakimit, prandaj aty ku shënohet pranohen dallime të vogla që vijnë nga rrumbullakimi më i hershëm. Të gjitha situatat, vlerat, të dhënat dhe rezultatet e programeve janë krijuar për mësim; nuk janë gjetje empirike.

# Pjesa I: Teoria

## A01: Pyetja së cilës i përgjigjet ANOVA njëfaktoriale

### T08-A01-V01: Formatet e leximit dhe të kuptuarit

**Përcakto çështjen**

Rezultati sasior është «rezultati i të kuptuarit»; njësia matëse është pikë.

Faktori është «formati i leximit» me nivelet tekst i shtypur, tablet dhe audio.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë rastet u caktuan rastësisht, një studim i zbatuar mirë mund të mbështetë interpretim shkakor për këto kushte, në varësi të dizajnit dhe supozimeve.

### T08-A01-V02: Rrugët në muze dhe kohëzgjatja e vizitës

**Përcakto çështjen**

Rezultati sasior është «kohëzgjatja e vizitës»; njësia matëse është minuta.

Faktori është «lloji i rrugës» me nivelet rrugë e lirë, rrugë e numërtuar dhe rrugë me udhërrëfyes.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë rastet u caktuan rastësisht, një studim i zbatuar mirë mund të mbështetë interpretim shkakor për këto kushte, në varësi të dizajnit dhe supozimeve.

### T08-A01-V03: Vendet e studimit dhe përqendrimi

**Përcakto çështjen**

Rezultati sasior është «rezultati i përqendrimit»; njësia matëse është pikë.

Faktori është «vendi i zakonshëm i studimit» me nivelet shtëpi, bibliotekë dhe hapësirë e përbashkët pune.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë grupet u vrojtuan dhe nuk u caktuan rastësisht, dallimi përshkruan lidhje dhe nuk identifikon vetvetiu efekt shkakor.

### T08-A01-V04: Oraret e kujtesave dhe vonesa e përgjigjes

**Përcakto çështjen**

Rezultati sasior është «vonesa e përgjigjes»; njësia matëse është orë.

Faktori është «orari i kujtesave» me nivelet pa kujtesë, një kujtesë dhe tri kujtesa.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë rastet u caktuan rastësisht, një studim i zbatuar mirë mund të mbështetë interpretim shkakor për këto kushte, në varësi të dizajnit dhe supozimeve.

### T08-A01-V05: Ndërfaqet e arkivit dhe saktësia e gjetjes

**Përcakto çështjen**

Rezultati sasior është «saktësia e gjetjes»; njësia matëse është pikë.

Faktori është «versioni i ndërfaqes» me nivelet standard, i përmbledhur dhe i udhëzuar.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë rastet u caktuan rastësisht, një studim i zbatuar mirë mund të mbështetë interpretim shkakor për këto kushte, në varësi të dizajnit dhe supozimeve.

### T08-A01-V06: Mënyrat e udhëtimit dhe koha e vajtje-ardhjes

**Përcakto çështjen**

Rezultati sasior është «koha e vajtje-ardhjes»; njësia matëse është minuta.

Faktori është «mënyra e zakonshme e udhëtimit» me nivelet ecje, transport publik dhe makinë.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë grupet u vrojtuan dhe nuk u caktuan rastësisht, dallimi përshkruan lidhje dhe nuk identifikon vetvetiu efekt shkakor.

### T08-A01-V07: Rutinat e ushtrimit dhe rikujtimi i vonuar

**Përcakto çështjen**

Rezultati sasior është «rezultati i rikujtimit të vonuar»; njësia matëse është pikë.

Faktori është «rutina e ushtrimit» me nivelet rilexim, vetëtestim dhe ushtrim i përzier.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë rastet u caktuan rastësisht, një studim i zbatuar mirë mund të mbështetë interpretim shkakor për këto kushte, në varësi të dizajnit dhe supozimeve.

### T08-A01-V08: Drejtimet e seminarit dhe vetëbesimi

**Përcakto çështjen**

Rezultati sasior është «rezultati i vetëbesimit»; njësia matëse është pikë.

Faktori është «drejtimi i zgjedhur i seminarit» me nivelet metoda, shkrim dhe prezantim.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë grupet u vrojtuan dhe nuk u caktuan rastësisht, dallimi përshkruan lidhje dhe nuk identifikon vetvetiu efekt shkakor.

### T08-A01-V09: Stilet e titrave dhe të kuptuarit e tutorialit

**Përcakto çështjen**

Rezultati sasior është «rezultati i të kuptuarit»; njësia matëse është pikë.

Faktori është «stili i titrave» me nivelet pa titra, fjalë për fjalë dhe të redaktuar.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë rastet u caktuan rastësisht, një studim i zbatuar mirë mund të mbështetë interpretim shkakor për këto kushte, në varësi të dizajnit dhe supozimeve.

### T08-A01-V10: Llojet e lagjeve dhe përdorimi i parkut

**Përcakto çështjen**

Rezultati sasior është «numri javor i vizitave në park»; njësia matëse është vizita.

Faktori është «lloji i lagjes» me nivelet qendrore, periferike dhe rurale.

Shënoji mesataret e popullatave me $\mu_1$, $\mu_2$ dhe $\mu_3$.

**Arsyeto hap pas hapi nga evidenca**

Hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$.

Alternativa thotë se të paktën dy mesatare ndryshojnë.

Nuk thotë se ndryshon çdo çift.

**Jep përfundimin dhe kufijtë e tij**

Fillimi me tri teste të veçanta do të krijonte disa mundësi për gabim të llojit I, ndërsa testi i përgjithshëm $F$ e bën fillimisht pyetjen e vetme globale.

Rezultati domethënës do të jepte evidencë kundër barazisë së të tria mesatareve të popullatave, por nuk do të tregonte cilat çifte ndryshojnë.

Meqë grupet u vrojtuan dhe nuk u caktuan rastësisht, dallimi përshkruan lidhje dhe nuk identifikon vetvetiu efekt shkakor.

## A06: Përcaktimi i familjes së krahasimeve para shqyrtimit të rezultateve

### T08-A06-V01: Rutinat e studimit

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V02: Paraqitjet e tekstit

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V03: Udhëzimet e arkivit

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V04: Rrugët në muze

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V05: Oraret e kujtesave

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | asnjë |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | asnjë |
| Personi 5 | 5 | 0.010 | asnjë |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V06: Modelet e shënimeve

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V07: Intervalet e ushtrimit

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V08: Mjediset zanore

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V09: Ndihmat e navigimit

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

### T08-A06-V10: Oraret e komenteve kthyese

**Përcakto çështjen, pjesa (a)**

dhe

**Arsyeto hap pas hapi nga evidenca, pjesa (b)**

Një familje përmban çdo krahasim që procesi i vendimmarrjes e bën të disponueshëm, përfshirë krahasimet që u shqyrtuan dhe u fshehën më vonë. Kjo jep madhësitë dhe pragjet e mëposhtme:

| Personi | Madhësia e familjes | Pragu Bonferroni | Rezultatet nën prag |
|---|---|---|---|
| Personi 1 | 2 | 0.025 | A kundrejt B, A kundrejt C |
| Personi 2 | 5 | 0.010 | A kundrejt B |
| Personi 3 | 1 | 0.050 | A kundrejt D |
| Personi 4 | 5 | 0.010 | A kundrejt B |
| Personi 5 | 5 | 0.010 | A kundrejt B |

**Arsyeto hap pas hapi nga evidenca, pjesa (c)**

Çdo rezultat në kolonën e fundit merret duke krahasuar vetëm vlerat p në familjen e deklaruar ndershmërisht nga ai person me $0.05/m$. Personi 1 ka dy krahasime të përcaktuara paraprakisht, Personi 2 ka pesë dhe Personi 3 ka një. Edhe Personat 4 dhe 5 kanë pesë, sepse zvogëlimi i tyre ndodhi pasi rezultatet u bënë të dukshme.

**Arsyeto hap pas hapi nga evidenca, pjesa (d)**

Heqja e rezultatit më të madh ose theksimi i rezultatit më të vogël pas shqyrtimit është përzgjedhje e varur nga të dhënat. Kjo nuk i zhduk mundësitë e tjera për një gabim të llojit I dhe nuk e bën pyetjen e theksuar të planifikuar në mënyrë prapavepruese.

**Jep përfundimin dhe kufijtë e tij, pjesa (e)**

Para se t'i shihte rezultatet, secili person duhej të shënonte krahasimin shkencor, drejtimin ose peshat e kontrastit kur ishin të rëndësishme, familjen e plotë të krahasimeve kryesore dhe dytësore, si dhe rregullin e zgjedhur për krahasimet e shumëfishta.

# Pjesa II: Praktika me kalkulator

## A02: Mesataret e grupeve, ndarja e shumave të katrorëve dhe testi F njëfaktorial

### T08-A02-V01: Rutinat e studimit dhe rezultati i të nxënit

**Përgatit llogaritjen**

Mesataret e grupeve janë 12, 16, 20, ndërsa mesatarja e përgjithshme është 16.0000 pikë.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=128.0000$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=188.0000$ dhe 188.0000 = 128.0000 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=128.0000/2=64.0000$, $MS_e=60.0000/9=6.6667$ dhe $F=64.0000/6.6667=9.6000$.

Meqë 9.6000 është më e madhe se 4.26, e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V02: Paraqitjet e tekstit dhe shpejtësia e leximit

**Përgatit llogaritjen**

Mesataret e grupeve janë 20, 22, 24, ndërsa mesatarja e përgjithshme është 22.0000 fjalë në minutë mbi nivelin fillestar.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=32.0000$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=92.0000$ dhe 92.0000 = 32.0000 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=32.0000/2=16.0000$, $MS_e=60.0000/9=6.6667$ dhe $F=16.0000/6.6667=2.4000$.

Meqë 2.4000 nuk është më e madhe se 4.26, nuk e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V03: Udhëzimet e arkivit dhe regjistrimet e sakta

**Përgatit llogaritjen**

Mesataret e grupeve janë 15, 15, 15, ndërsa mesatarja e përgjithshme është 15.0000 regjistrime.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=0.0000$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=60.0000$ dhe 60.0000 = 0.0000 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=0.0000/2=0.0000$, $MS_e=60.0000/9=6.6667$ dhe $F=0.0000/6.6667=0.0000$.

Meqë 0.0000 nuk është më e madhe se 4.26, nuk e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V04: Hartat e muzeut dhe siguria për rrugën

**Përgatit llogaritjen**

Mesataret e grupeve janë 45, 50, 47, ndërsa mesatarja e përgjithshme është 47.3333 pikë.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=50.6667$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=110.6667$ dhe 110.6667 = 50.6667 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=50.6667/2=25.3333$, $MS_e=60.0000/9=6.6667$ dhe $F=25.3333/6.6667=3.8000$.

Meqë 3.8000 nuk është më e madhe se 4.26, nuk e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V05: Koha e kujtesës dhe përfundimi

**Përgatit llogaritjen**

Mesataret e grupeve janë 30, 35, 39, ndërsa mesatarja e përgjithshme është 34.6667 pikë.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=162.6667$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=222.6667$ dhe 222.6667 = 162.6667 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=162.6667/2=81.3333$, $MS_e=60.0000/9=6.6667$ dhe $F=81.3333/6.6667=12.2000$.

Meqë 12.2000 është më e madhe se 4.26, e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V06: Formatet e shënimeve dhe dallimi i argumentit

**Përgatit llogaritjen**

Mesataret e grupeve janë 52, 56, 61, ndërsa mesatarja e përgjithshme është 56.3333 pikë.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=162.6667$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=222.6667$ dhe 222.6667 = 162.6667 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=162.6667/2=81.3333$, $MS_e=60.0000/9=6.6667$ dhe $F=81.3333/6.6667=12.2000$.

Meqë 12.2000 është më e madhe se 4.26, e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V07: Shpërndarja e ushtrimit në kohë dhe rikujtimi

**Përgatit llogaritjen**

Mesataret e grupeve janë 40, 43, 48, ndërsa mesatarja e përgjithshme është 43.6667 pikë.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=130.6667$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=190.6667$ dhe 190.6667 = 130.6667 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=130.6667/2=65.3333$, $MS_e=60.0000/9=6.6667$ dhe $F=65.3333/6.6667=9.8000$.

Meqë 9.8000 është më e madhe se 4.26, e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V08: Mjediset zanore dhe përqendrimi

**Përgatit llogaritjen**

Mesataret e grupeve janë 70, 68, 63, ndërsa mesatarja e përgjithshme është 67.0000 pikë.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=104.0000$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=164.0000$ dhe 164.0000 = 104.0000 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=104.0000/2=52.0000$, $MS_e=60.0000/9=6.6667$ dhe $F=52.0000/6.6667=7.8000$.

Meqë 7.8000 është më e madhe se 4.26, e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V09: Udhëzimet e rrugës dhe gabimet

**Përgatit llogaritjen**

Mesataret e grupeve janë 18, 14, 10, ndërsa mesatarja e përgjithshme është 14.0000 gabime.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=128.0000$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=188.0000$ dhe 188.0000 = 128.0000 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=128.0000/2=64.0000$, $MS_e=60.0000/9=6.6667$ dhe $F=64.0000/6.6667=9.6000$.

Meqë 9.6000 është më e madhe se 4.26, e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

### T08-A02-V10: Koha e komenteve kthyese dhe cilësia e rishikimit

**Përgatit llogaritjen**

Mesataret e grupeve janë 64, 67, 65, ndërsa mesatarja e përgjithshme është 65.3333 pikë.

Llogaritja mes grupeve jep $SS_A=\sum_i n_i(\bar y_i-\bar y)^2=18.6667$.

**Zhvillo llogaritjen**

Mbledhja e devijimeve në katror brenda tri grupeve jep $SS_e=60.0000$.

Rreth mesatares së përgjithshme, $SS_{total}=78.6667$ dhe 78.6667 = 18.6667 + 60.0000, prandaj ndarja përputhet.

Shkallët e lirisë janë $df_A=3-1=2$, $df_e=12-3=9$ dhe $df_{total}=11$.

**Interpreto dhe kontrollo rezultatin**

Kështu $MS_A=18.6667/2=9.3333$, $MS_e=60.0000/9=6.6667$ dhe $F=9.3333/6.6667=1.4000$.

Meqë 1.4000 nuk është më e madhe se 4.26, nuk e refuzojmë hipotezën zero të mesatareve të barabarta në nivelin 5%.

Vendimi lidhet me modelin global të mesatareve, jo me çdo çift veçmas.

## A03: Rindërtimi i tabelës ANOVA dhe leximi i dizajnit

### T08-A03-V01: Udhëzime leximi të caktuara rastësisht

**Arsyeto para llogaritjes**

Për $k=3$ grupe, $H_0:\mu_1=\cdots=\mu_3$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 96+144=240.

**Zhvillo llogaritjen**

Me $N=24$, shkallët e lirisë janë $df_A=3-1=2$, $df_e=24-3=21$ dhe $df_{total}=24-1=23$.

Pastaj $MS_A=96/2=48.0000$, $MS_e=144/21=6.8571$ dhe $F=7.0000$.

**Interpreto dhe kontrollo rezultatin**

Meqë 7.0000 është më e madhe se 3.44, e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e barabarta të grupeve e bëjnë dizajnin të balancuar.

Caktimi i rastësishëm mund të mbështetë interpretim shkakor për kushtet e caktuara nëse zbatimi dhe supozimet e modelit janë të besueshme.

### T08-A03-V02: Mënyra të vrojtuara udhëtimi

**Arsyeto para llogaritjes**

Për $k=3$ grupe, $H_0:\mu_1=\cdots=\mu_3$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 45+210=255.

**Zhvillo llogaritjen**

Me $N=26$, shkallët e lirisë janë $df_A=3-1=2$, $df_e=26-3=23$ dhe $df_{total}=26-1=25$.

Pastaj $MS_A=45/2=22.5000$, $MS_e=210/23=9.1304$ dhe $F=2.4643$.

**Interpreto dhe kontrollo rezultatin**

Meqë 2.4643 nuk është më e madhe se 3.42, nuk e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e pabarabarta të grupeve e bëjnë dizajnin të pabalancuar.

Pa caktim të rastësishëm, rezultati përshkruan lidhje mes grupeve dhe nuk mund t'i përjashtojë vetë dallimet që ekzistonin më parë.

### T08-A03-V03: Ndërfaqe arkivi të caktuara rastësisht

**Arsyeto para llogaritjes**

Për $k=4$ grupe, $H_0:\mu_1=\cdots=\mu_4$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 180+220=400.

**Zhvillo llogaritjen**

Me $N=24$, shkallët e lirisë janë $df_A=4-1=3$, $df_e=24-4=20$ dhe $df_{total}=24-1=23$.

Pastaj $MS_A=180/3=60.0000$, $MS_e=220/20=11.0000$ dhe $F=5.4545$.

**Interpreto dhe kontrollo rezultatin**

Meqë 5.4545 është më e madhe se 3.10, e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e barabarta të grupeve e bëjnë dizajnin të balancuar.

Caktimi i rastësishëm mund të mbështetë interpretim shkakor për kushtet e caktuara nëse zbatimi dhe supozimet e modelit janë të besueshme.

### T08-A03-V04: Drejtime seminari të zgjedhura vetë

**Arsyeto para llogaritjes**

Për $k=3$ grupe, $H_0:\mu_1=\cdots=\mu_3$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 30+330=360.

**Zhvillo llogaritjen**

Me $N=36$, shkallët e lirisë janë $df_A=3-1=2$, $df_e=36-3=33$ dhe $df_{total}=36-1=35$.

Pastaj $MS_A=30/2=15.0000$, $MS_e=330/33=10.0000$ dhe $F=1.5000$.

**Interpreto dhe kontrollo rezultatin**

Meqë 1.5000 nuk është më e madhe se 3.28, nuk e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e barabarta të grupeve e bëjnë dizajnin të balancuar.

Pa caktim të rastësishëm, rezultati përshkruan lidhje mes grupeve dhe nuk mund t'i përjashtojë vetë dallimet që ekzistonin më parë.

### T08-A03-V05: Oraret e kujtesave të caktuara rastësisht

**Arsyeto para llogaritjes**

Për $k=3$ grupe, $H_0:\mu_1=\cdots=\mu_3$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 120+180=300.

**Zhvillo llogaritjen**

Me $N=27$, shkallët e lirisë janë $df_A=3-1=2$, $df_e=27-3=24$ dhe $df_{total}=27-1=26$.

Pastaj $MS_A=120/2=60.0000$, $MS_e=180/24=7.5000$ dhe $F=8.0000$.

**Interpreto dhe kontrollo rezultatin**

Meqë 8.0000 është më e madhe se 3.35, e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e barabarta të grupeve e bëjnë dizajnin të balancuar.

Caktimi i rastësishëm mund të mbështetë interpretim shkakor për kushtet e caktuara nëse zbatimi dhe supozimet e modelit janë të besueshme.

### T08-A03-V06: Lloje lagjesh të vrojtuara

**Arsyeto para llogaritjes**

Për $k=3$ grupe, $H_0:\mu_1=\cdots=\mu_3$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 75+270=345.

**Zhvillo llogaritjen**

Me $N=30$, shkallët e lirisë janë $df_A=3-1=2$, $df_e=30-3=27$ dhe $df_{total}=30-1=29$.

Pastaj $MS_A=75/2=37.5000$, $MS_e=270/27=10.0000$ dhe $F=3.7500$.

**Interpreto dhe kontrollo rezultatin**

Meqë 3.7500 është më e madhe se 3.35, e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e pabarabarta të grupeve e bëjnë dizajnin të pabalancuar.

Pa caktim të rastësishëm, rezultati përshkruan lidhje mes grupeve dhe nuk mund t'i përjashtojë vetë dallimet që ekzistonin më parë.

### T08-A03-V07: Stile titrash të caktuara rastësisht

**Arsyeto para llogaritjes**

Për $k=4$ grupe, $H_0:\mu_1=\cdots=\mu_4$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 210+252=462.

**Zhvillo llogaritjen**

Me $N=28$, shkallët e lirisë janë $df_A=4-1=3$, $df_e=28-4=24$ dhe $df_{total}=28-1=27$.

Pastaj $MS_A=210/3=70.0000$, $MS_e=252/24=10.5000$ dhe $F=6.6667$.

**Interpreto dhe kontrollo rezultatin**

Meqë 6.6667 është më e madhe se 3.01, e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e barabarta të grupeve e bëjnë dizajnin të balancuar.

Caktimi i rastësishëm mund të mbështetë interpretim shkakor për kushtet e caktuara nëse zbatimi dhe supozimet e modelit janë të besueshme.

### T08-A03-V08: Vende studimi të zgjedhura

**Arsyeto para llogaritjes**

Për $k=3$ grupe, $H_0:\mu_1=\cdots=\mu_3$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 54+243=297.

**Zhvillo llogaritjen**

Me $N=30$, shkallët e lirisë janë $df_A=3-1=2$, $df_e=30-3=27$ dhe $df_{total}=30-1=29$.

Pastaj $MS_A=54/2=27.0000$, $MS_e=243/27=9.0000$ dhe $F=3.0000$.

**Interpreto dhe kontrollo rezultatin**

Meqë 3.0000 nuk është më e madhe se 3.35, nuk e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e pabarabarta të grupeve e bëjnë dizajnin të pabalancuar.

Pa caktim të rastësishëm, rezultati përshkruan lidhje mes grupeve dhe nuk mund t'i përjashtojë vetë dallimet që ekzistonin më parë.

### T08-A03-V09: Harta rrugësh të caktuara rastësisht

**Arsyeto para llogaritjes**

Për $k=3$ grupe, $H_0:\mu_1=\cdots=\mu_3$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 160+240=400.

**Zhvillo llogaritjen**

Me $N=30$, shkallët e lirisë janë $df_A=3-1=2$, $df_e=30-3=27$ dhe $df_{total}=30-1=29$.

Pastaj $MS_A=160/2=80.0000$, $MS_e=240/27=8.8889$ dhe $F=9.0000$.

**Interpreto dhe kontrollo rezultatin**

Meqë 9.0000 është më e madhe se 3.35, e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e barabarta të grupeve e bëjnë dizajnin të balancuar.

Caktimi i rastësishëm mund të mbështetë interpretim shkakor për kushtet e caktuara nëse zbatimi dhe supozimet e modelit janë të besueshme.

### T08-A03-V10: Sektorë punësimi të vrojtuar

**Arsyeto para llogaritjes**

Për $k=3$ grupe, $H_0:\mu_1=\cdots=\mu_3$; alternativa thotë se të paktën dy mesatare ndryshojnë.

Shuma totale e katrorëve është 40+260=300.

**Zhvillo llogaritjen**

Me $N=30$, shkallët e lirisë janë $df_A=3-1=2$, $df_e=30-3=27$ dhe $df_{total}=30-1=29$.

Pastaj $MS_A=40/2=20.0000$, $MS_e=260/27=9.6296$ dhe $F=2.0769$.

**Interpreto dhe kontrollo rezultatin**

Meqë 2.0769 nuk është më e madhe se 3.35, nuk e refuzojmë hipotezën zero në nivelin 5%.

Madhësitë e pabarabarta të grupeve e bëjnë dizajnin të pabalancuar.

Pa caktim të rastësishëm, rezultati përshkruan lidhje mes grupeve dhe nuk mund t'i përjashtojë vetë dallimet që ekzistonin më parë.

## A04: Kontrastet e thjeshta dyshe dhe kontrastet komplekse të bashkuara

### T08-A04-V01: Katër rutina studimi

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=4.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(25/8)[(-1)^2+1^2]}=2.5000$, duke dhënë $t_s=4.0000/2.5000=1.6000$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=16.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(25/8)[(-1)^2+(-1)^2+1^2+1^2]}=3.5355$, prandaj $t_c=4.5255$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V02: Katër paraqitje teksti

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=5.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(16/8)[(-1)^2+1^2]}=2.0000$, duke dhënë $t_s=5.0000/2.0000=2.5000$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=13.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(16/8)[(-1)^2+(-1)^2+1^2+1^2]}=2.8284$, prandaj $t_c=4.5962$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V03: Katër udhëzime arkivi

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=3.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(9/8)[(-1)^2+1^2]}=1.5000$, duke dhënë $t_s=3.0000/1.5000=2.0000$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=8.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(9/8)[(-1)^2+(-1)^2+1^2+1^2]}=2.1213$, prandaj $t_c=3.7712$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V04: Katër rrugë muzeu

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=-3.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(36/8)[(-1)^2+1^2]}=3.0000$, duke dhënë $t_s=-3.0000/3.0000=-1.0000$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=15.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(36/8)[(-1)^2+(-1)^2+1^2+1^2]}=4.2426$, prandaj $t_c=3.5355$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V05: Katër orare kujtesash

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=5.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(20/8)[(-1)^2+1^2]}=2.2361$, duke dhënë $t_s=5.0000/2.2361=2.2361$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=14.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(20/8)[(-1)^2+(-1)^2+1^2+1^2]}=3.1623$, prandaj $t_c=4.4272$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V06: Katër modele shënimesh

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=3.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(24/8)[(-1)^2+1^2]}=2.4495$, duke dhënë $t_s=3.0000/2.4495=1.2247$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=17.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(24/8)[(-1)^2+(-1)^2+1^2+1^2]}=3.4641$, prandaj $t_c=4.9075$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V07: Katër intervale ushtrimi

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=5.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(30/8)[(-1)^2+1^2]}=2.7386$, duke dhënë $t_s=5.0000/2.7386=1.8257$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=17.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(30/8)[(-1)^2+(-1)^2+1^2+1^2]}=3.8730$, prandaj $t_c=4.3894$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V08: Katër mjedise zanore

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=-4.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(18/8)[(-1)^2+1^2]}=2.1213$, duke dhënë $t_s=-4.0000/2.1213=-1.8856$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=-11.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(18/8)[(-1)^2+(-1)^2+1^2+1^2]}=3.0000$, prandaj $t_c=-3.6667$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V09: Katër ndihma navigimi

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=5.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(22/8)[(-1)^2+1^2]}=2.3452$, duke dhënë $t_s=5.0000/2.3452=2.1320$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=17.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(22/8)[(-1)^2+(-1)^2+1^2+1^2]}=3.3166$, prandaj $t_c=5.1257$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

### T08-A04-V10: Katër orare komentesh kthyese

**Përgatit llogaritjen**

Shuma e secilit vektor të peshave është zero, prandaj të dy janë kontraste të vlefshme.

Kontrasti i thjeshtë krahason Grupin 2 me Grupin 1: $D_s=4.0000$.

**Zhvillo llogaritjen**

Gabimi standard është $SE_s=\sqrt{(28/8)[(-1)^2+1^2]}=2.6458$, duke dhënë $t_s=4.0000/2.6458=1.5119$.

Kontrasti kompleks krahason shumën e Grupeve 3 dhe 4 me shumën e Grupeve 1 dhe 2: $D_c=8.0000$.

**Interpreto dhe kontrollo rezultatin**

Gabimi standard është $SE_c=\sqrt{(28/8)[(-1)^2+(-1)^2+1^2+1^2]}=3.7417$, prandaj $t_c=2.1381$.

Pjesëtimi i çdo peshe komplekse me 2 do ta shprehte dallimin mes dy mesatareve të bashkuara dhe do ta linte statistikën $t$ të pandryshuar, sepse vlerësimi dhe gabimi standard shkallëzohen së bashku.

Vlerësimet e papërpunuara të kontrasteve përdorin shkallë të ndryshme kur ndryshojnë peshat, prandaj krahaso pyetjen e deklaruar dhe statistikën e standardizuar, jo vetëm madhësinë.

## A05: Të gjitha krahasimet dyshe dhe mbrojtja Bonferroni

### T08-A05-V01: Të gjitha çiftet mes 3 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=3(3-1)/2=3$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/3=0.0167$.

Nëse të gjitha 3 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{3}=0.1426$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V02: Të gjitha çiftet mes 4 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=4(4-1)/2=6$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/6=0.0083$.

Nëse të gjitha 6 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{6}=0.2649$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V03: Të gjitha çiftet mes 5 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=5(5-1)/2=10$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/10=0.0050$.

Nëse të gjitha 10 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{10}=0.4013$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V04: Të gjitha çiftet mes 6 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=6(6-1)/2=15$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/15=0.0033$.

Nëse të gjitha 15 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{15}=0.5367$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V05: Të gjitha çiftet mes 7 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=7(7-1)/2=21$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/21=0.0024$.

Nëse të gjitha 21 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{21}=0.6594$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V06: Të gjitha çiftet mes 8 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=8(8-1)/2=28$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/28=0.0018$.

Nëse të gjitha 28 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{28}=0.7622$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V07: Të gjitha çiftet mes 4 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=4(4-1)/2=6$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/6=0.0083$.

Nëse të gjitha 6 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{6}=0.2649$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V08: Të gjitha çiftet mes 5 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=5(5-1)/2=10$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/10=0.0050$.

Nëse të gjitha 10 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{10}=0.4013$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V09: Të gjitha çiftet mes 6 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=6(6-1)/2=15$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/15=0.0033$.

Nëse të gjitha 15 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{15}=0.5367$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

### T08-A05-V10: Të gjitha çiftet mes 7 niveleve

**Përgatit llogaritjen**

Numri i çifteve të ndryshme të parenditura është $m=k(k-1)/2=7(7-1)/2=21$.

**Zhvillo llogaritjen**

Bonferroni përdor $\alpha_{test}=0.05/21=0.0024$.

Nëse të gjitha 21 testet do të ishin të pavarura dhe secili do të përdorte 0.05, probabiliteti i të paktën një gabimi të llojit I nën hipotezën zero të plotë do të ishte $1-(1-0.05)^{21}=0.6594$.

**Interpreto dhe kontrollo rezultatin**

Krahasimet dyshe të vërteta shpesh përdorin grupe të përbashkëta dhe prandaj janë të varura, kështu që shprehja e fundit është ilustrim dhe jo norma e tyre e përgjithshme e saktë e gabimit për familjen e testeve.

Bonferroni mbështetet në kufirin e sipërm të probabilitetit të bashkimit të gabimeve, ndaj e kontrollon familjen edhe pa pavarësi, megjithëse mund të jetë konservativ.

## A07: Një kontrast prirjeje i përcaktuar paraprakisht

### T08-A07-V01: Seancat e ushtrimit dhe rikujtimi

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=57.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(25/10)(9+1+1+9)}=7.0711$. Prandaj $t=57.0000/7.0711=8.0610$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|8.0610|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja pozitive do të thotë se modeli i peshuar priret të rritet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V02: Intensiteti i kujtesave dhe përgjigjja

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=36.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(16/10)(9+1+1+9)}=5.6569$. Prandaj $t=36.0000/5.6569=6.3640$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|6.3640|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja pozitive do të thotë se modeli i peshuar priret të rritet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V03: Udhëzimi në lexim dhe të kuptuarit

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=40.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(20/10)(9+1+1+9)}=6.3246$. Prandaj $t=40.0000/6.3246=6.3246$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|6.3246|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja pozitive do të thotë se modeli i peshuar priret të rritet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V04: Shembujt në arkiv dhe saktësia

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=31.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(9/10)(9+1+1+9)}=4.2426$. Prandaj $t=31.0000/4.2426=7.3068$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|7.3068|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja pozitive do të thotë se modeli i peshuar priret të rritet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V05: Ushtrimi i rrugës dhe vetëbesimi

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=51.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(24/10)(9+1+1+9)}=6.9282$. Prandaj $t=51.0000/6.9282=7.3612$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|7.3612|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja pozitive do të thotë se modeli i peshuar priret të rritet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V06: Struktura e shënimeve dhe arsyetimi

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=42.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(18/10)(9+1+1+9)}=6.0000$. Prandaj $t=42.0000/6.0000=7.0000$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|7.0000|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja pozitive do të thotë se modeli i peshuar priret të rritet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V07: Shpeshtësia e komenteve kthyese dhe rishikimi

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=31.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(22/10)(9+1+1+9)}=6.6332$. Prandaj $t=31.0000/6.6332=4.6734$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|4.6734|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja pozitive do të thotë se modeli i peshuar priret të rritet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V08: Zhurma e ambientit dhe përqendrimi

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=-39.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(16/10)(9+1+1+9)}=5.6569$. Prandaj $t=-39.0000/5.6569=-6.8943$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|-6.8943|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja negative do të thotë se modeli i peshuar priret të ulet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V09: Mbështetja e navigimit dhe gabimet

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=-37.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(12/10)(9+1+1+9)}=4.8990$. Prandaj $t=-37.0000/4.8990=-7.5526$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|-7.5526|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja negative do të thotë se modeli i peshuar priret të ulet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

### T08-A07-V10: Vonesa e komenteve kthyese dhe mbajtja mend

**Arsyeto para llogaritjes, pjesa (a)**

Peshat $c_1$ rriten me një njësi në çdo nivel, prandaj skica e tyre formon një renditje të drejtë në rritje. Edhe peshat $c_2$ rriten me hapa të barabartë dhe janë të qendërzuara rreth zeros. Peshat $c_3$ krahasojnë dy pikat fundore me dy nivelet e mesme, prandaj paraqesin lakim dhe jo prirje lineare.

**Zhvillo llogaritjen, pjesa (b)**

Shumat janë $0+1+2+3=6$, $-3-1+1+3=0$ dhe $0.5-0.5-0.5+0.5=0$. Kështu, $c_2$ dhe $c_3$ janë kontraste, por vetëm $c_2$ është kontrasti i dhënë i prirjes lineare.

**Zhvillo llogaritjen, pjesa (c)**

Pesha mesatare e $c_1$ është $1.5$. Zbritja e saj jep $(-1.5,-0.5,0.5,1.5)$, që është saktësisht gjysma e $c_2$. Shumëzimi i të gjitha peshave të kontrastit me të njëjtën konstante pozitive e ndryshon së bashku shkallën numerike të vlerësimit dhe gabimit standard, por nuk e ndryshon drejtimin që testohet ose statistikën $t$.

**Zhvillo llogaritjen, pjesa (d)**

Me $c_2$, vlerësimi i peshuar është $D=\sum c_i\bar y_i=-40.0000$. Meqë grupet janë të balancuara, $SE(D)=\sqrt{(MS_e/n)\sum c_i^2}=\sqrt{(20/10)(9+1+1+9)}=6.3246$. Prandaj $t=-40.0000/6.3246=-6.3246$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Meqë $|-6.3246|$ është më e madhe se 2.028, prirja lineare e plotëson kriterin e dyanshëm 5%. Shenja negative do të thotë se modeli i peshuar priret të ulet përgjatë niveleve të renditura. Kjo nuk provon se ndryshimet mes niveleve fqinje janë të barabarta dhe as nuk e përjashton lakimin.

## A08: Mesataret e qelizave, mesataret margjinale dhe ndërveprimi në ANOVA dyfaktoriale

### T08-A08-V01: Titrat dhe ushtrimi

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (65.0000, 73.0000); mesataret margjinale të Faktorit B janë (66.0000, 72.0000); mesatarja e përgjithshme është 69.0000.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B është i njëjtë në të dy nivelet e Faktorit A, prandaj këto mesatare qelizash nuk tregojnë ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=384.0000$, $SS_B=216.0000$ dhe $SS_{AB}=0.0000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=16(20)=320.0000$. Prandaj $F_A=24.0000$, $F_B=13.5000$ dhe $F_{AB}=0.0000$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,62.0000)$ dhe $(B_1,68.0000)$. Vizatoje $A_1$ përmes $(B_0,70.0000)$ dhe $(B_1,76.0000)$. Dy ndryshimet janë të barabarta, prandaj vijat janë paralele dhe grafiku nuk paraqet ndërveprim. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V02: Harta dhe ushtrimi i rrugës

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (57.0000, 64.0000); mesataret margjinale të Faktorit B janë (56.0000, 65.0000); mesatarja e përgjithshme është 60.5000.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=294.0000$, $SS_B=486.0000$ dhe $SS_{AB}=54.0000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=20(20)=400.0000$. Prandaj $F_A=14.7000$, $F_B=24.3000$ dhe $F_{AB}=2.7000$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,54.0000)$ dhe $(B_1,60.0000)$. Vizatoje $A_1$ përmes $(B_0,58.0000)$ dhe $(B_1,70.0000)$. Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V03: Dhoma e qetë dhe lista e kontrollit

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (68.0000, 72.0000); mesataret margjinale të Faktorit B janë (67.0000, 73.0000); mesatarja e përgjithshme është 70.0000.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B është i njëjtë në të dy nivelet e Faktorit A, prandaj këto mesatare qelizash nuk tregojnë ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=96.0000$, $SS_B=216.0000$ dhe $SS_{AB}=0.0000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=18(20)=360.0000$. Prandaj $F_A=5.3333$, $F_B=12.0000$ dhe $F_{AB}=0.0000$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,65.0000)$ dhe $(B_1,71.0000)$. Vizatoje $A_1$ përmes $(B_0,69.0000)$ dhe $(B_1,75.0000)$. Dy ndryshimet janë të barabarta, prandaj vijat janë paralele dhe grafiku nuk paraqet ndërveprim. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V04: Udhëzimi dhe komentet kthyese

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (54.5000, 58.5000); mesataret margjinale të Faktorit B janë (53.0000, 60.0000); mesatarja e përgjithshme është 56.5000.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=96.0000$, $SS_B=294.0000$ dhe $SS_{AB}=24.0000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=15(20)=300.0000$. Prandaj $F_A=6.4000$, $F_B=19.6000$ dhe $F_{AB}=1.6000$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,50.0000)$ dhe $(B_1,59.0000)$. Vizatoje $A_1$ përmes $(B_0,56.0000)$ dhe $(B_1,61.0000)$. Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V05: Ikonat dhe shembujt

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (73.0000, 79.5000); mesataret margjinale të Faktorit B janë (74.0000, 78.5000); mesatarja e përgjithshme është 76.2500.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=253.5000$, $SS_B=121.5000$ dhe $SS_{AB}=37.5000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=24(20)=480.0000$. Prandaj $F_A=10.5625$, $F_B=5.0625$ dhe $F_{AB}=1.5625$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,72.0000)$ dhe $(B_1,74.0000)$. Vizatoje $A_1$ përmes $(B_0,76.0000)$ dhe $(B_1,83.0000)$. Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V06: Planifikimi dhe vetëtestimi

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (63.5000, 72.0000); mesataret margjinale të Faktorit B janë (63.0000, 72.5000); mesatarja e përgjithshme është 67.7500.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=433.5000$, $SS_B=541.5000$ dhe $SS_{AB}=37.5000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=21(20)=420.0000$. Prandaj $F_A=20.6429$, $F_B=25.7857$ dhe $F_{AB}=1.7857$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,60.0000)$ dhe $(B_1,67.0000)$. Vizatoje $A_1$ përmes $(B_0,66.0000)$ dhe $(B_1,78.0000)$. Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V07: Ndriçimi dhe zhurma e sfondit

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (70.5000, 67.5000); mesataret margjinale të Faktorit B janë (72.0000, 66.0000); mesatarja e përgjithshme është 69.0000.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=54.0000$, $SS_B=216.0000$ dhe $SS_{AB}=6.0000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=17(20)=340.0000$. Prandaj $F_A=3.1765$, $F_B=12.7059$ dhe $F_{AB}=0.3529$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,74.0000)$ dhe $(B_1,67.0000)$. Vizatoje $A_1$ përmes $(B_0,70.0000)$ dhe $(B_1,65.0000)$. Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V08: Orientimi dhe shenjat

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (51.5000, 63.5000); mesataret margjinale të Faktorit B janë (53.5000, 61.5000); mesatarja e përgjithshme është 57.5000.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=864.0000$, $SS_B=384.0000$ dhe $SS_{AB}=6.0000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=19(20)=380.0000$. Prandaj $F_A=45.4737$, $F_B=20.2105$ dhe $F_{AB}=0.3158$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,48.0000)$ dhe $(B_1,55.0000)$. Vizatoje $A_1$ përmes $(B_0,59.0000)$ dhe $(B_1,68.0000)$. Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V09: Shpërndarja në kohë dhe shenjat e rikujtimit

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (68.0000, 74.5000); mesataret margjinale të Faktorit B janë (66.5000, 76.0000); mesatarja e përgjithshme është 71.2500.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=253.5000$, $SS_B=541.5000$ dhe $SS_{AB}=13.5000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=23(20)=460.0000$. Prandaj $F_A=11.0217$, $F_B=23.5435$ dhe $F_{AB}=0.5870$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,64.0000)$ dhe $(B_1,72.0000)$. Vizatoje $A_1$ përmes $(B_0,69.0000)$ dhe $(B_1,80.0000)$. Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

### T08-A08-V10: Modeli dhe shqyrtimi nga bashkëmoshatarët

**Arsyeto para llogaritjes, pjesa (a)**

Mesataret margjinale të Faktorit A janë (61.5000, 68.5000); mesataret margjinale të Faktorit B janë (60.0000, 70.0000); mesatarja e përgjithshme është 65.0000.

**Zhvillo llogaritjen, pjesa (b)**

Efekti kryesor A krahason dy mesataret margjinale të tij, ndërsa efekti kryesor B krahason dy mesataret margjinale të tij. Ndryshimi përgjatë Faktorit B dallon mes dy niveleve të Faktorit A, prandaj modeli i qelizave përmban ndërveprim.

**Zhvillo llogaritjen, pjesa (c)**

Tri hipotezat zero janë: pa efekt kryesor A në popullatë, pa efekt kryesor B në popullatë dhe pa ndërveprim $A\times B$ në popullatë.

**Zhvillo llogaritjen, pjesa (d)**

Llogaritjet e dizajnit të balancuar japin $SS_A=294.0000$, $SS_B=600.0000$ dhe $SS_{AB}=6.0000$. Me $df_A=df_B=df_{AB}=1$ dhe $df_e=4(6-1)=20$, $SS_e=MS_e\,df_e=20(20)=400.0000$. Prandaj $F_A=14.7000$, $F_B=30.0000$ dhe $F_{AB}=0.3000$.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Vizatoje nivelin $A_0$ të faktorit A përmes koordinatave $(B_0,57.0000)$ dhe $(B_1,66.0000)$. Vizatoje $A_1$ përmes $(B_0,63.0000)$ dhe $(B_1,74.0000)$. Dy ndryshimet dallojnë, prandaj vijat nuk janë paralele dhe grafiku e paraqet ndërveprimin. Efektet kryesore përmbledhin mesataret margjinale, ndërsa ndërveprimi pyet nëse modeli i një faktori ndryshon përgjatë faktorit tjetër.

## A09: Faktorët fiksë e të rastësishëm, komponentët e variancës dhe ICC-ja

### T08-A09-V01: Biblioteka të kampionuara nga një popullatë rajonale

**Arsyeto para llogaritjes**

Nivelet e faktorit «biblioteka» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «tri dizajne të zgjedhura qëllimisht të ndërfaqes» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(18-6)/5=2.4000$ dhe $\widehat{\sigma}_e^2=MS_e=6.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=2.4000/[2.4000+6.0000]=0.2857$.

Modeli ia atribuon rreth 28.6% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «biblioteka».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V02: Shkolla të kampionuara nga një distrikt

**Arsyeto para llogaritjes**

Nivelet e faktorit «shkolla» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «dy programe mësimore të emërtuara» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(20-5)/6=2.5000$ dhe $\widehat{\sigma}_e^2=MS_e=5.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=2.5000/[2.5000+5.0000]=0.3333$.

Modeli ia atribuon rreth 33.3% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «shkolla».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V03: Intervistues të kampionuar nga një grup i trajnuar

**Arsyeto para llogaritjes**

Nivelet e faktorit «intervistuesi» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «tri versione fikse të pyetësorit» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(15-7)/4=2.0000$ dhe $\widehat{\sigma}_e^2=MS_e=7.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=2.0000/[2.0000+7.0000]=0.2222$.

Modeli ia atribuon rreth 22.2% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «intervistuesi».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V04: Lagje të kampionuara nga një qytet

**Arsyeto para llogaritjes**

Nivelet e faktorit «lagjja» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «dy mesazhe të zgjedhura informuese» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(24-8)/8=2.0000$ dhe $\widehat{\sigma}_e^2=MS_e=8.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=2.0000/[2.0000+8.0000]=0.2000$.

Modeli ia atribuon rreth 20.0% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «lagjja».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V05: Udhërrëfyes muzeu të kampionuar nga lista e stafit

**Arsyeto para llogaritjes**

Nivelet e faktorit «udhërrëfyesi i muzeut» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «katër tekste fikse të vizitës» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(21-6)/5=3.0000$ dhe $\widehat{\sigma}_e^2=MS_e=6.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=3.0000/[3.0000+6.0000]=0.3333$.

Modeli ia atribuon rreth 33.3% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «udhërrëfyesi i muzeut».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V06: Kuti arkivi të kampionuara nga një koleksion

**Arsyeto para llogaritjes**

Nivelet e faktorit «kutia e arkivit» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «tri cilësime të zgjedhura skanimi» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(19-5)/7=2.0000$ dhe $\widehat{\sigma}_e^2=MS_e=5.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=2.0000/[2.0000+5.0000]=0.2857$.

Modeli ia atribuon rreth 28.6% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «kutia e arkivit».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V07: Grupe tutoriali të kampionuara nga një program

**Arsyeto para llogaritjes**

Nivelet e faktorit «grupi i tutorialit» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «dy orare fikse ushtrimi» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(17-7)/6=1.6667$ dhe $\widehat{\sigma}_e^2=MS_e=7.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=1.6667/[1.6667+7.0000]=0.1923$.

Modeli ia atribuon rreth 19.2% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «grupi i tutorialit».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V08: Rrugë të kampionuara nga një rrjet transporti

**Arsyeto para llogaritjes**

Nivelet e faktorit «rruga» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «tri dizajne të zgjedhura shenjash» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(27-9)/9=2.0000$ dhe $\widehat{\sigma}_e^2=MS_e=9.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=2.0000/[2.0000+9.0000]=0.1818$.

Modeli ia atribuon rreth 18.2% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «rruga».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V09: Seminare të kampionuara nga një seri vjetore

**Arsyeto para llogaritjes**

Nivelet e faktorit «seminari» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «dy formate të emërtuara lehtësimi» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(16-4)/5=2.4000$ dhe $\widehat{\sigma}_e^2=MS_e=4.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=2.4000/[2.4000+4.0000]=0.3750$.

Modeli ia atribuon rreth 37.5% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «seminari».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

### T08-A09-V10: Ditë të kampionuara nga një semestër

**Arsyeto para llogaritjes**

Nivelet e faktorit «dita» u kampionuan për të përfaqësuar një popullatë më të gjerë nivelesh të mundshme, prandaj përsëritja e studimit mund të zgjidhte nivele të reja.

Në të kundërt, faktori fiks «tri mesazhe fikse kujtese» emërton pikërisht kushtet e zgjedhura me interes.

**Zhvillo llogaritjen**

Synimi i faktorit të rastësishëm është ndryshueshmëria në popullatën e niveleve të tij, jo një listë dallimesh dyshe vetëm mes emërtimeve të kampionuara.

Në këtë model të balancuar njëfaktorial, $\widehat{\sigma}_A^2=(MS_A-MS_e)/n=(22-6)/8=2.0000$ dhe $\widehat{\sigma}_e^2=MS_e=6.0000$.

**Interpreto dhe kontrollo rezultatin**

Prandaj $ICC=2.0000/[2.0000+6.0000]=0.2500$.

Modeli ia atribuon rreth 25.0% të variancës së vet dallimeve mes niveleve të kampionuara të faktorit «dita».

Ky ekuacion varet nga një strukturë e balancuar njëfaktoriale me faktor të rastësishëm; dizajnet e kryqëzuara, të folezuara, të përsëritura ose të pabalancuara mund të kërkojnë komponentë dhe emërues të ndryshëm.

## A10: Matjet e përsëritura, sfericiteti dhe korrigjimi Greenhouse-Geisser

### T08-A10-V01: Leximi në tri kohë matjeje

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 32.0000, secili devijim standard është $\sqrt{32.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (18, 19, 20). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 18 deri në 20; raporti i më të madhes me më të voglën është 1.1111. Ky model është mjaft i ngjashëm dhe prandaj jep siguri përshkruese, megjithëse nuk e provon sfericitetin.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=84/2=42.0000$, $MS_{person}=176/11=16.0000$ dhe $MS_e=132/22=6.0000$. Prandaj $F_{condition}=7.0000$ me vlerë p 0.0044, ndërsa $F_{person}=16.0000/6.0000=2.6667$ me vlerë p 0.0241. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(16.0000-6.0000)/3=3.3333$, prandaj $ICC=3.3333/[3.3333+6.0000]=0.3571$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.82(2)=1.6400$ dhe $df_e^*=0.82(22)=18.0400$. Përdorimi i $F=7.0000$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0080.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V02: Përqendrimi në tri mjedise zanore

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 43.0000, secili devijim standard është $\sqrt{43.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (12, 22, 31). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 12 deri në 31; raporti i më të madhes me më të voglën është 2.5833. Ky model është dukshëm i pabarabartë dhe prandaj paralajmëron se referenca e pakorrigjuar mund të jetë e pasigurt.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=66/2=33.0000$, $MS_{person}=154/11=14.0000$ dhe $MS_e=110/22=5.0000$. Prandaj $F_{condition}=6.6000$ me vlerë p 0.0057, ndërsa $F_{person}=14.0000/5.0000=2.8000$ me vlerë p 0.0191. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(14.0000-5.0000)/3=3.0000$, prandaj $ICC=3.0000/[3.0000+5.0000]=0.3750$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.74(2)=1.4800$ dhe $df_e^*=0.74(22)=16.2800$. Përdorimi i $F=6.6000$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0125.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V03: Rikujtimi pas tri vonesave

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 29.0000, secili devijim standard është $\sqrt{29.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (16, 17, 15). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 15 deri në 17; raporti i më të madhes me më të voglën është 1.1333. Ky model është mjaft i ngjashëm dhe prandaj jep siguri përshkruese, megjithëse nuk e provon sfericitetin.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=72/2=36.0000$, $MS_{person}=198/11=18.0000$ dhe $MS_e=121/22=5.5000$. Prandaj $F_{condition}=6.5455$ me vlerë p 0.0059, ndërsa $F_{person}=18.0000/5.5000=3.2727$ me vlerë p 0.0086. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(18.0000-5.5000)/3=4.1667$, prandaj $ICC=4.1667/[4.1667+5.5000]=0.4310$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.91(2)=1.8200$ dhe $df_e^*=0.91(22)=20.0200$. Përdorimi i $F=6.5455$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0077.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V04: Navigimi në tri prova rruge

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 50.0000, secili devijim standard është $\sqrt{50.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (10, 25, 38). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 10 deri në 38; raporti i më të madhes me më të voglën është 3.8000. Ky model është dukshëm i pabarabartë dhe prandaj paralajmëron se referenca e pakorrigjuar mund të jetë e pasigurt.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=90/2=45.0000$, $MS_{person}=165/11=15.0000$ dhe $MS_e=143/22=6.5000$. Prandaj $F_{condition}=6.9231$ me vlerë p 0.0047, ndërsa $F_{person}=15.0000/6.5000=2.3077$ me vlerë p 0.0457. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(15.0000-6.5000)/3=2.8333$, prandaj $ICC=2.8333/[2.8333+6.5000]=0.3036$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.68(2)=1.3600$ dhe $df_e^*=0.68(22)=14.9600$. Përdorimi i $F=6.9231$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0130.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V05: Vetëbesimi në tri pika të kursit

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 33.0000, secili devijim standard është $\sqrt{33.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (20, 21, 19). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 19 deri në 21; raporti i më të madhes me më të voglën është 1.1053. Ky model është mjaft i ngjashëm dhe prandaj jep siguri përshkruese, megjithëse nuk e provon sfericitetin.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=78/2=39.0000$, $MS_{person}=187/11=17.0000$ dhe $MS_e=126/22=5.7273$. Prandaj $F_{condition}=6.8095$ me vlerë p 0.0050, ndërsa $F_{person}=17.0000/5.7273=2.9683$ me vlerë p 0.0144. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(17.0000-5.7273)/3=3.7576$, prandaj $ICC=3.7576/[3.7576+5.7273]=0.3962$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.88(2)=1.7600$ dhe $df_e^*=0.88(22)=19.3600$. Përdorimi i $F=6.8095$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0073.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V06: Saktësia me tri ndërfaqe

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 47.0000, secili devijim standard është $\sqrt{47.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (14, 28, 35). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 14 deri në 35; raporti i më të madhes me më të voglën është 2.5000. Ky model është dukshëm i pabarabartë dhe prandaj paralajmëron se referenca e pakorrigjuar mund të jetë e pasigurt.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=81/2=40.5000$, $MS_{person}=143/11=13.0000$ dhe $MS_e=119/22=5.4091$. Prandaj $F_{condition}=7.4874$ me vlerë p 0.0033, ndërsa $F_{person}=13.0000/5.4091=2.4034$ me vlerë p 0.0385. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(13.0000-5.4091)/3=2.5303$, prandaj $ICC=2.5303/[2.5303+5.4091]=0.3187$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.71(2)=1.4200$ dhe $df_e^*=0.71(22)=15.6200$. Përdorimi i $F=7.4874$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0092.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V07: Koha e përgjigjes me tri kujtesa

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 38.0000, secili devijim standard është $\sqrt{38.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (24, 23, 26). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 23 deri në 26; raporti i më të madhes me më të voglën është 1.1304. Ky model është mjaft i ngjashëm dhe prandaj jep siguri përshkruese, megjithëse nuk e provon sfericitetin.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=63/2=31.5000$, $MS_{person}=209/11=19.0000$ dhe $MS_e=138/22=6.2727$. Prandaj $F_{condition}=5.0217$ me vlerë p 0.0160, ndërsa $F_{person}=19.0000/6.2727=3.0290$ me vlerë p 0.0130. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(19.0000-6.2727)/3=4.2424$, prandaj $ICC=4.2424/[4.2424+6.2727]=0.4035$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.95(2)=1.9000$ dhe $df_e^*=0.95(22)=20.9000$. Përdorimi i $F=5.0217$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0178.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V08: Të kuptuarit me tri formate

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 46.0000, secili devijim standard është $\sqrt{46.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (11, 20, 34). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 11 deri në 34; raporti i më të madhes me më të voglën është 3.0909. Ky model është dukshëm i pabarabartë dhe prandaj paralajmëron se referenca e pakorrigjuar mund të jetë e pasigurt.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=96/2=48.0000$, $MS_{person}=176/11=16.0000$ dhe $MS_e=154/22=7.0000$. Prandaj $F_{condition}=6.8571$ me vlerë p 0.0048, ndërsa $F_{person}=16.0000/7.0000=2.2857$ me vlerë p 0.0476. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(16.0000-7.0000)/3=3.0000$, prandaj $ICC=3.0000/[3.0000+7.0000]=0.3000$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.65(2)=1.3000$ dhe $df_e^*=0.65(22)=14.3000$. Përdorimi i $F=6.8571$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0147.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V09: Cilësia e rishikimit në tri drafte

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 30.0000, secili devijim standard është $\sqrt{30.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (17, 18, 16). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 16 deri në 18; raporti i më të madhes me më të voglën është 1.1250. Ky model është mjaft i ngjashëm dhe prandaj jep siguri përshkruese, megjithëse nuk e provon sfericitetin.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=75/2=37.5000$, $MS_{person}=220/11=20.0000$ dhe $MS_e=132/22=6.0000$. Prandaj $F_{condition}=6.2500$ me vlerë p 0.0071, ndërsa $F_{person}=20.0000/6.0000=3.3333$ me vlerë p 0.0078. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(20.0000-6.0000)/3=4.6667$, prandaj $ICC=4.6667/[4.6667+6.0000]=0.4375$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.90(2)=1.8000$ dhe $df_e^*=0.90(22)=19.8000$. Përdorimi i $F=6.2500$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0094.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.

### T08-A10-V10: Aftësia e kërkimit në tri pika ushtrimi

**Arsyeto para llogaritjes, pjesa (a)**

Meqë të tria variancat margjinale janë 52.0000, secili devijim standard është $\sqrt{52.0000}$. Zëvendësimi jep afërsisht variancat e rezultateve të diferencave (13, 26, 40). Korrelacionet janë paraqitur me katër shifra dhjetore, prandaj ndryshimet e vogla gjatë rindërtimit vijnë vetëm nga rrumbullakimi. Sfericiteti pyet nëse variancat e popullatës të çdo diference dyshe mes kushteve janë të barabarta. Vlerat e rindërtuara shtrihen nga 13 deri në 40; raporti i më të madhes me më të voglën është 3.0769. Ky model është dukshëm i pabarabartë dhe prandaj paralajmëron se referenca e pakorrigjuar mund të jetë e pasigurt.

**Zhvillo llogaritjen, pjesa (b)**

Për kushtet, hipoteza zero është $H_0:\mu_1=\mu_2=\mu_3$; alternativa thotë se të paktën dy mesatare të kushteve ndryshojnë. Për personat, hipoteza zero e efektit të rastësishëm të personit është $H_0:\sigma_{person}^2=0$ kundrejt ndryshueshmërisë pozitive mes personave. Katrorët mesatarë janë $MS_{condition}=87/2=43.5000$, $MS_{person}=187/11=17.0000$ dhe $MS_e=143/22=6.5000$. Prandaj $F_{condition}=6.6923$ me vlerë p 0.0054, ndërsa $F_{person}=17.0000/6.5000=2.6154$ me vlerë p 0.0264. Testi i kushtit e hedh poshtë barazinë e mesatareve në nivelin 5%; testi i personit mbështet ndryshueshmëri mes personave në nivelin 5%.

**Zhvillo llogaritjen, pjesa (c)**

$\widehat{\sigma}_{person}^2=(17.0000-6.5000)/3=3.5000$, prandaj $ICC=3.5000/[3.5000+6.5000]=0.3500$. Sipas këtij modeli, ICC-ja përshkruan ngjashmërinë mes matjeve të të njëjtit person.

**Zhvillo llogaritjen, pjesa (d)**

Greenhouse-Geisser jep $df_{condition}^*=0.70(2)=1.4000$ dhe $df_e^*=0.70(22)=15.4000$. Përdorimi i $F=6.6923$ të vëzhguar me këto shkallë lirie referuese jep vlerën p të korrigjuar 0.0135.

**Interpreto dhe kontrollo rezultatin, pjesa (e)**

Korrigjimi i ndryshon shkallët referuese të lirisë dhe, për pasojë, vlerën p ose vlerën kritike. Nuk e ndryshon $F$ të vëzhguar, mesataret e përshtatura ose varësinë mes rreshtave të përsëritur. Matjet e të njëjtit person mbeten të lidhura.
