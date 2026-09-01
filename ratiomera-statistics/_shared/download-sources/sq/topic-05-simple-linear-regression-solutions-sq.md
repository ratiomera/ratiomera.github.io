---
title: "Zgjidhjet e plota"
subtitle: "Regresioni i thjeshtë linear"
document-id: "topic-05-simple-linear-regression-solutions-sq"
topic-id: "topic-05-simple-linear-regression"
topic-number: "05"
topic-slug: "simple-linear-regression"
document-type: "solutions"
locale: "sq"
paired-document-id: "topic-05-simple-linear-regression-exercises-sq"
---

Këto zgjidhje të plota përdorin të njëjtat kode dhe të njëjtën renditje si Fleta e ushtrimeve. Vlerat ndërmjetëse ruhen deri te hapi i treguar i rrumbullakimit, prandaj aty ku shënohet pranohen dallime të vogla që vijnë nga rrumbullakimi më i hershëm. Të gjitha situatat, vlerat, të dhënat dhe rezultatet e programeve janë krijuar për mësim; nuk janë gjetje empirike.

# Pjesa I: Teoria

## A08: Interpretimi i kujdesshëm i evidencës së dobët

### T05-A08-V01: Ushtrimi javor dhe arsyetimi

**Përcakto çështjen**

Meqë $p=0.276>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $0.16\pm2(0.14)=[-0.1200, 0.4400]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(1.11)^2/[(1.11)^2+28-2]=0.0452$, ose 4.5% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është 0.16 pikë për orë, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V02: Përvoja në arkiv dhe koha e kërkimit

**Përcakto çështjen**

Meqë $p=0.288>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $-0.12\pm2(0.11)=[-0.3400, 0.1000]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(-1.08)^2/[(-1.08)^2+34-2]=0.0352$, ose 3.5% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është -0.12 minuta për muaj, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V03: Vizitat në muze dhe njohuritë

**Përcakto çështjen**

Meqë $p=0.283>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $0.1\pm2(0.09)=[-0.0800, 0.2800]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(1.09)^2/[(1.09)^2+40-2]=0.0303$, ose 3.0% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është 0.1 pikë për vizitë, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V04: Koha e leximit dhe të kuptuarit

**Përcakto çështjen**

Meqë $p=0.329>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $0.08\pm2(0.08)=[-0.0800, 0.2400]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(0.99)^2/[(0.99)^2+46-2]=0.0218$, ose 2.2% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është 0.08 pikë për orë, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V05: Njohja e rrugës dhe gabimet e orientimit

**Përcakto çështjen**

Meqë $p=0.323>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $-0.07\pm2(0.07)=[-0.2100, 0.0700]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(-1.00)^2/[(-1.00)^2+52-2]=0.0196$, ose 2.0% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është -0.07 gabime për pikë, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Përcakto çështjen**

Meqë $p=0.326>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $0.06\pm2(0.06)=[-0.0600, 0.1800]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(0.99)^2/[(0.99)^2+60-2]=0.0166$, ose 1.7% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është 0.06 pikë për seancë, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V07: Njoftimet dhe përqendrimi

**Përcakto çështjen**

Meqë $p=0.326>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $-0.05\pm2(0.05)=[-0.1500, 0.0500]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(-0.99)^2/[(-0.99)^2+70-2]=0.0142$, ose 1.4% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është -0.05 pikë për njoftim, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V08: Ushtrimi i kërkimit dhe saktësia

**Përcakto çështjen**

Meqë $p=0.32>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $0.05\pm2(0.05)=[-0.0500, 0.1500]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(1.00)^2/[(1.00)^2+80-2]=0.0127$, ose 1.3% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është 0.05 pikë për ushtrim, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Përcakto çështjen**

Meqë $p=0.325>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $0.04\pm2(0.04)=[-0.0400, 0.1200]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(0.99)^2/[(0.99)^2+90-2]=0.0110$, ose 1.1% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është 0.04 minuta për kilometër, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

### T05-A08-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Përcakto çështjen**

Meqë $p=0.32>0.05$, nuk e refuzojmë $H_0:\beta_1=0$.

Intervali i përafërt është $-0.04\pm2(0.04)=[-0.1200, 0.0400]$ dhe përmban zeron.

**Arsyeto hap pas hapi nga evidenca**

Përshtatja është $R^2=(-1.00)^2/[(-1.00)^2+100-2]=0.0101$, ose 1.0% e ndryshueshmërisë së kampionit.

Pjerrësia e vlerësuar është -0.04 pikë për kontribut, por të dhënat mbeten të përputhshme me zeron dhe pjerrësi të afërta.

**Jep përfundimin dhe kufijtë e tij**

Përfundimi i duhur është evidencë lineare e dobët ose jo përfundimtare, jo provë e mungesës së lidhjes.

As shenja dhe as një vlerë e vogël p nuk do të vendosnin shkakësi pa dizajn të përshtatshëm.

## A09: Kontrolli i shpërndarjes së rezidualeve

### T05-A09-V01: Ushtrimi javor dhe arsyetimi

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.0, 2), (-2.0, 7), (-1.0, 15), (0.0, 22), (1.0, 15), (2.0, 7), (3.0, 2); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është përafërsisht normal.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve duket i besueshëm nga ky histogram i përgjithshëm.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V02: Përvoja në arkiv dhe koha e kërkimit

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.0, 18), (-2.0, 20), (-1.0, 14), (0.0, 8), (1.0, 4), (2.0, 2), (3.0, 1); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është i anuar djathtas.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve është i dyshimtë dhe duhet shqyrtuar me rezidualet fillestare dhe diagram normal të kuantileve.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V03: Vizitat në muze dhe njohuritë

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.0, 1), (-2.0, 6), (-1.0, 14), (0.0, 20), (1.0, 14), (2.0, 6), (3.0, 1); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është përafërsisht normal.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve duket i besueshëm nga ky histogram i përgjithshëm.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V04: Koha e leximit dhe të kuptuarit

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-4.0, 3), (-3.0, 8), (-2.0, 16), (-1.0, 22), (0.0, 15), (1.0, 5), (2.0, 1), (3.0, 0), (4.0, 1); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është një vlerë skajore e sipërme ose bisht i rëndë djathtas.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve është i dyshimtë dhe duhet shqyrtuar me rezidualet fillestare dhe diagram normal të kuantileve.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V05: Njohja e rrugës dhe gabimet e orientimit

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.0, 5), (-2.0, 9), (-1.0, 12), (0.0, 13), (1.0, 12), (2.0, 9), (3.0, 5); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është simetrik, por më i sheshtë se trajta normale.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve është i dyshimtë dhe duhet shqyrtuar me rezidualet fillestare dhe diagram normal të kuantileve.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.0, 1), (-2.0, 2), (-1.0, 4), (0.0, 8), (1.0, 14), (2.0, 20), (3.0, 18); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është i anuar majtas.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve është i dyshimtë dhe duhet shqyrtuar me rezidualet fillestare dhe diagram normal të kuantileve.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V07: Njoftimet dhe përqendrimi

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.0, 2), (-2.0, 8), (-1.0, 17), (0.0, 24), (1.0, 17), (2.0, 8), (3.0, 2); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është përafërsisht normal.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve duket i besueshëm nga ky histogram i përgjithshëm.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V08: Ushtrimi i kërkimit dhe saktësia

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.5, 3), (-2.5, 12), (-1.5, 18), (-0.5, 7), (0.5, 6), (1.5, 17), (2.5, 11), (3.5, 3); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është bimodal.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve është i dyshimtë dhe duhet shqyrtuar me rezidualet fillestare dhe diagram normal të kuantileve.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.0, 5), (-2.0, 7), (-1.0, 12), (0.0, 20), (1.0, 12), (2.0, 7), (3.0, 5); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është simetrik me bishta më të rëndë.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve është i dyshimtë dhe duhet shqyrtuar me rezidualet fillestare dhe diagram normal të kuantileve.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

### T05-A09-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Përcakto çështjen**

Përcaktimi i plotë i koordinatave të shtyllave është (-3.0, 1), (-2.0, 4), (-1.0, 10), (0.0, 30), (1.0, 10), (2.0, 4), (3.0, 1); koordinata e dytë është lartësia e shtyllës në koordinatën e parë.

Modeli që rezulton është simetrik, por me kulm më të mprehtë.

**Arsyeto hap pas hapi nga evidenca**

Normaliteti i përafërt i rezidualeve është i dyshimtë dhe duhet shqyrtuar me rezidualet fillestare dhe diagram normal të kuantileve.

Ky kontroll ka rëndësi kryesisht për shpërndarjet referuese t dhe F në kampione të vogla, si edhe për intervalet dhe vlerat e tyre p.

**Jep përfundimin dhe kufijtë e tij**

Vija e përshtatur mund të llogaritet edhe pa normalitet të përsosur.

Histogrami i shpërfill vlerat e përshtatura, ndaj nuk mund të tregojë nëse mesatarja e rezidualeve lakohet me parashikuesin ose nëse ndryshon shpërndarja e rezidualeve.

Këto pyetje kërkojnë diagramin e rezidualeve kundrejt vlerave të përshtatura.

## A10: Modelet e rezidualeve kundrejt vlerave të përshtatura

### T05-A10-V01: Ushtrimi javor dhe arsyetimi

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, -0.1), (2, 0.2), (3, -0.2), (4, 0.1), (5, 0.0).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [-2.2, 2.0], brezi 2: [-1.8, 2.2], brezi 3: [-2.4, 2.0], brezi 4: [-2.0, 2.2], brezi 5: [-2.0, 2.0].

Së bashku, paraqitja e grupuar tregon një brez horizontal të rastësishëm.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve qëndrojnë afër zeros dhe shpërndarjet mbeten të ngjashme, siç pritet.

Në këtë përmbledhje të grupuar nuk duket jolinearitet apo pabarazi e variancës.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V02: Përvoja në arkiv dhe koha e kërkimit

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, 2.4), (2, 0.6), (3, -1.0), (4, 0.5), (5, 2.3).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [0.9, 3.9], brezi 2: [-1.0, 2.2], brezi 3: [-2.7, 0.7], brezi 4: [-1.1, 2.1], brezi 5: [0.8, 3.8].

Së bashku, paraqitja e grupuar tregon lakim.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve ndryshojnë sistematikisht nga pozitive në negative dhe përsëri, duke treguar lakim.

Funksioni mesatar në vijë të drejtë nuk mjafton.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V03: Vizitat në muze dhe njohuritë

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, 0.0), (2, 0.1), (3, -0.1), (4, 0.2), (5, 0.0).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [-0.8, 0.8], brezi 2: [-1.1, 1.3], brezi 3: [-1.9, 1.7], brezi 4: [-2.4, 2.8], brezi 5: [-3.5, 3.5].

Së bashku, paraqitja e grupuar tregon shpërndarje në rritje.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve qëndrojnë afër zeros, por shpërndarja tregon shpërndarje në rritje.

Kushti i variancës konstante është i dyshimtë.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V04: Koha e leximit dhe të kuptuarit

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, -2.0), (2, -0.7), (3, 0.8), (4, 0.4), (5, -1.8).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [-3.4, -0.6], brezi 2: [-2.2, 0.8], brezi 3: [-0.8, 2.4], brezi 4: [-1.1, 1.9], brezi 5: [-3.2, -0.4].

Së bashku, paraqitja e grupuar tregon lakim.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve ndryshojnë sistematikisht nga pozitive në negative dhe përsëri, duke treguar lakim.

Funksioni mesatar në vijë të drejtë nuk mjafton.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V05: Njohja e rrugës dhe gabimet e orientimit

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, 0.1), (2, -0.1), (3, 0.0), (4, 0.1), (5, -0.1).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [-3.1, 3.3], brezi 2: [-2.7, 2.5], brezi 3: [-1.9, 1.9], brezi 4: [-1.2, 1.4], brezi 5: [-0.9, 0.7].

Së bashku, paraqitja e grupuar tregon shpërndarje në ulje.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve qëndrojnë afër zeros, por shpërndarja tregon shpërndarje në ulje.

Kushti i variancës konstante është i dyshimtë.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, 0.2), (2, -0.2), (3, 0.1), (4, -0.1), (5, 0.0).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [-1.6, 2.0], brezi 2: [-2.1, 1.7], brezi 3: [-1.6, 1.8], brezi 4: [-1.9, 1.7], brezi 5: [-1.9, 1.9].

Së bashku, paraqitja e grupuar tregon një brez horizontal të rastësishëm.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve qëndrojnë afër zeros dhe shpërndarjet mbeten të ngjashme, siç pritet.

Në këtë përmbledhje të grupuar nuk duket jolinearitet apo pabarazi e variancës.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V07: Njoftimet dhe përqendrimi

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, -1.5), (2, -0.4), (3, 0.6), (4, 0.3), (5, -1.4).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [-2.7, -0.3], brezi 2: [-1.7, 0.9], brezi 3: [-0.8, 2.0], brezi 4: [-1.0, 1.6], brezi 5: [-2.6, -0.2].

Së bashku, paraqitja e grupuar tregon lakim.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve ndryshojnë sistematikisht nga pozitive në negative dhe përsëri, duke treguar lakim.

Funksioni mesatar në vijë të drejtë nuk mjafton.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V08: Ushtrimi i kërkimit dhe saktësia

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, 0.0), (2, 0.1), (3, 0.0), (4, -0.1), (5, 0.1).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [-0.7, 0.7], brezi 2: [-1.0, 1.2], brezi 3: [-1.7, 1.7], brezi 4: [-2.5, 2.3], brezi 5: [-3.1, 3.3].

Së bashku, paraqitja e grupuar tregon shpërndarje në rritje.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve qëndrojnë afër zeros, por shpërndarja tregon shpërndarje në rritje.

Kushti i variancës konstante është i dyshimtë.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, 0.1), (2, 0.0), (3, -0.1), (4, 0.0), (5, 0.1).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [-1.9, 2.1], brezi 2: [-2.1, 2.1], brezi 3: [-2.0, 1.8], brezi 4: [-2.0, 2.0], brezi 5: [-2.0, 2.2].

Së bashku, paraqitja e grupuar tregon një brez horizontal të rastësishëm.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve qëndrojnë afër zeros dhe shpërndarjet mbeten të ngjashme, siç pritet.

Në këtë përmbledhje të grupuar nuk duket jolinearitet apo pabarazi e variancës.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

### T05-A10-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Përcakto çështjen**

Koordinatat e plota mesatare janë (1, 1.8), (2, 0.5), (3, -0.9), (4, 0.4), (5, 1.7).

Pikat fundore të pesë shtyllave vertikale janë brezi 1: [0.5, 3.1], brezi 2: [-0.9, 1.9], brezi 3: [-2.4, 0.6], brezi 4: [-1.0, 1.8], brezi 5: [0.4, 3.0].

Së bashku, paraqitja e grupuar tregon lakim.

**Arsyeto hap pas hapi nga evidenca**

Mesataret e rezidualeve ndryshojnë sistematikisht nga pozitive në negative dhe përsëri, duke treguar lakim.

Funksioni mesatar në vijë të drejtë nuk mjafton.

Shqyrto diagramin e rezidualeve për çdo rast kundrejt vlerave të përshtatura, jo vetëm pesë brezat.

**Jep përfundimin dhe kufijtë e tij**

Për lakimin, shqyrto nëse një parashikues i transformuar ose term jolinear i arsyetuar qartë përputhet me pyetjen kërkimore.

Për ndryshim të shpërndarjes, kontrollo matjen, nëngrupet, shkallën e rezultatit dhe modelimin e variancës.

Një model i pastër i mbështet kushtet diagnostike, por nuk i provon dhe nuk vendos shkakësi.

# Pjesa II: Praktika me kalkulator

## A01: Koeficientët e katrorëve më të vegjël nga shumat e papërpunuara

### T05-A01-V01: Ushtrimi javor dhe arsyetimi

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (2, 58), (3, 60), (4, 65), (5, 67), (6, 71), (7, 73), (8, 78), (9, 80), me interval horizontal [2, 9].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë rritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=44/8=5.5000$ orë dhe $\bar y=552/8=69.0000$ pikë.

Shumat e korrigjuara janë $S_{xx}=284-44^2/8=42.0000$ dhe $S_{xy}=3172-44(552)/8=136.0000$.

**Zhvillo llogaritjen**

Prandaj $b_1=136.0000/42.0000=3.2381$ pikë për orë dhe $b_0=69.0000-(3.2381)(5.5000)=51.1905$ pikë.

Pjerrësia është dallimi i përshtatur prej 3.2381 pikë kur parashikuesi «orët e ushtrimit javor» rritet me një orë.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është jashtë intervalit të vrojtuar [2, 9], prandaj prerja nevojitet matematikisht, por nuk duhet trajtuar si nivel fillestar i vrojtuar.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=51.1905+(3.2381)X$.

Meqë 2 $\leq$ 6 $\leq$ 9, kërkesa është interpolim.

Në $X=6$, $\widehat Y=51.1905+(3.2381)(6)=70.6190$ pikë.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V02: Përvoja në arkiv dhe koha e kërkimit

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (2, 68), (4, 64), (6, 61), (8, 57), (10, 55), (12, 50), (14, 48), (16, 45), me interval horizontal [2, 16].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë zbritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=72/8=9.0000$ muaj dhe $\bar y=448/8=56.0000$ minuta.

Shumat e korrigjuara janë $S_{xx}=816-72^2/8=168.0000$ dhe $S_{xy}=3756-72(448)/8=-276.0000$.

**Zhvillo llogaritjen**

Prandaj $b_1=-276.0000/168.0000=-1.6429$ minuta për muaj dhe $b_0=56.0000-(-1.6429)(9.0000)=70.7857$ minuta.

Pjerrësia është dallimi i përshtatur prej -1.6429 minuta kur parashikuesi «muajt e përvojës në arkiv» rritet me një muaj.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është jashtë intervalit të vrojtuar [2, 16], prandaj prerja nevojitet matematikisht, por nuk duhet trajtuar si nivel fillestar i vrojtuar.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=70.7857+(-1.6429)X$.

Meqë 2 $\leq$ 9 $\leq$ 16, kërkesa është interpolim.

Në $X=9$, $\widehat Y=70.7857+(-1.6429)(9)=56.0000$ minuta.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V03: Vizitat në muze dhe njohuritë

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (0, 45), (1, 48), (2, 52), (3, 56), (4, 61), (5, 65), (6, 68), (7, 74), me interval horizontal [0, 7].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë rritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=28/8=3.5000$ vizita dhe $\bar y=469/8=58.6250$ pikë.

Shumat e korrigjuara janë $S_{xx}=140-28^2/8=42.0000$ dhe $S_{xy}=1815-28(469)/8=173.5000$.

**Zhvillo llogaritjen**

Prandaj $b_1=173.5000/42.0000=4.1310$ pikë për vizitë dhe $b_0=58.6250-(4.1310)(3.5000)=44.1667$ pikë.

Pjerrësia është dallimi i përshtatur prej 4.1310 pikë kur parashikuesi «vizitat në muze gjatë këtij viti» rritet me një vizitë.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është brenda intervalit të vrojtuar [0, 7], prandaj prerja përshkruan një nivel fillestar të përshtatur që mbështetet nga këto të dhëna.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=44.1667+(4.1310)X$.

Meqë 0 $\leq$ 4 $\leq$ 7, kërkesa është interpolim.

Në $X=4$, $\widehat Y=44.1667+(4.1310)(4)=60.6905$ pikë.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V04: Koha e leximit dhe të kuptuarit

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (1, 52), (2, 56), (3, 60), (4, 63), (5, 69), (6, 72), (7, 76), (8, 81), me interval horizontal [1, 8].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë rritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=36/8=4.5000$ orë dhe $\bar y=529/8=66.1250$ pikë.

Shumat e korrigjuara janë $S_{xx}=204-36^2/8=42.0000$ dhe $S_{xy}=2553-36(529)/8=172.5000$.

**Zhvillo llogaritjen**

Prandaj $b_1=172.5000/42.0000=4.1071$ pikë për orë dhe $b_0=66.1250-(4.1071)(4.5000)=47.6429$ pikë.

Pjerrësia është dallimi i përshtatur prej 4.1071 pikë kur parashikuesi «koha javore e leximit» rritet me një orë.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është jashtë intervalit të vrojtuar [1, 8], prandaj prerja nevojitet matematikisht, por nuk duhet trajtuar si nivel fillestar i vrojtuar.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=47.6429+(4.1071)X$.

Meqë 1 $\leq$ 5 $\leq$ 8, kërkesa është interpolim.

Në $X=5$, $\widehat Y=47.6429+(4.1071)(5)=68.1786$ pikë.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V05: Njohja e rrugës dhe gabimet e orientimit

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (2, 14), (3, 12), (4, 11), (5, 9), (6, 8), (7, 6), (8, 5), (9, 4), me interval horizontal [2, 9].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë zbritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=44/8=5.5000$ pikë dhe $\bar y=69/8=8.6250$ gabime.

Shumat e korrigjuara janë $S_{xx}=284-44^2/8=42.0000$ dhe $S_{xy}=319-44(69)/8=-60.5000$.

**Zhvillo llogaritjen**

Prandaj $b_1=-60.5000/42.0000=-1.4405$ gabime për pikë dhe $b_0=8.6250-(-1.4405)(5.5000)=16.5476$ gabime.

Pjerrësia është dallimi i përshtatur prej -1.4405 gabime kur parashikuesi «pikët e njohjes së rrugës» rritet me një pikë.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është jashtë intervalit të vrojtuar [2, 9], prandaj prerja nevojitet matematikisht, por nuk duhet trajtuar si nivel fillestar i vrojtuar.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=16.5476+(-1.4405)X$.

Meqë 2 $\leq$ 6 $\leq$ 9, kërkesa është interpolim.

Në $X=6$, $\widehat Y=16.5476+(-1.4405)(6)=7.9048$ gabime.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (0, 38), (1, 43), (2, 47), (3, 53), (4, 56), (5, 62), (6, 65), (7, 70), me interval horizontal [0, 7].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë rritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=28/8=3.5000$ seanca dhe $\bar y=434/8=54.2500$ pikë.

Shumat e korrigjuara janë $S_{xx}=140-28^2/8=42.0000$ dhe $S_{xy}=1710-28(434)/8=191.0000$.

**Zhvillo llogaritjen**

Prandaj $b_1=191.0000/42.0000=4.5476$ pikë për seancë dhe $b_0=54.2500-(4.5476)(3.5000)=38.3333$ pikë.

Pjerrësia është dallimi i përshtatur prej 4.5476 pikë kur parashikuesi «seancat e ndjekura të seminarit» rritet me një seancë.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është brenda intervalit të vrojtuar [0, 7], prandaj prerja përshkruan një nivel fillestar të përshtatur që mbështetet nga këto të dhëna.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=38.3333+(4.5476)X$.

Meqë 0 $\leq$ 4 $\leq$ 7, kërkesa është interpolim.

Në $X=4$, $\widehat Y=38.3333+(4.5476)(4)=56.5238$ pikë.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V07: Njoftimet dhe përqendrimi

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (10, 88), (20, 84), (30, 79), (40, 73), (50, 69), (60, 64), (70, 58), (80, 54), me interval horizontal [10, 80].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë zbritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=360/8=45.0000$ njoftime dhe $\bar y=569/8=71.1250$ pikë.

Shumat e korrigjuara janë $S_{xx}=20400-360^2/8=4200.0000$ dhe $S_{xy}=23520-360(569)/8=-2085.0000$.

**Zhvillo llogaritjen**

Prandaj $b_1=-2085.0000/4200.0000=-0.4964$ pikë për njoftim dhe $b_0=71.1250-(-0.4964)(45.0000)=93.4643$ pikë.

Pjerrësia është dallimi i përshtatur prej -0.4964 pikë kur parashikuesi «numri ditor i njoftimeve» rritet me një njoftim.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është jashtë intervalit të vrojtuar [10, 80], prandaj prerja nevojitet matematikisht, por nuk duhet trajtuar si nivel fillestar i vrojtuar.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=93.4643+(-0.4964)X$.

Meqë 10 $\leq$ 45 $\leq$ 80, kërkesa është interpolim.

Në $X=45$, $\widehat Y=93.4643+(-0.4964)(45)=71.1250$ pikë.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V08: Ushtrimi i kërkimit dhe saktësia

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (1, 55), (2, 59), (3, 63), (4, 68), (5, 72), (6, 77), (7, 81), (8, 86), me interval horizontal [1, 8].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë rritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=36/8=4.5000$ ushtrime dhe $\bar y=561/8=70.1250$ pikë.

Shumat e korrigjuara janë $S_{xx}=204-36^2/8=42.0000$ dhe $S_{xy}=2711-36(561)/8=186.5000$.

**Zhvillo llogaritjen**

Prandaj $b_1=186.5000/42.0000=4.4405$ pikë për ushtrim dhe $b_0=70.1250-(4.4405)(4.5000)=50.1429$ pikë.

Pjerrësia është dallimi i përshtatur prej 4.4405 pikë kur parashikuesi «ushtrimet e përfunduara të kërkimit» rritet me një ushtrim.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është jashtë intervalit të vrojtuar [1, 8], prandaj prerja nevojitet matematikisht, por nuk duhet trajtuar si nivel fillestar i vrojtuar.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=50.1429+(4.4405)X$.

Meqë 1 $\leq$ 5 $\leq$ 8, kërkesa është interpolim.

Në $X=5$, $\widehat Y=50.1429+(4.4405)(5)=72.3452$ pikë.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (2, 65), (4, 70), (6, 75), (8, 82), (10, 88), (12, 94), (14, 101), (16, 107), me interval horizontal [2, 16].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë rritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=72/8=9.0000$ kilometra dhe $\bar y=682/8=85.2500$ minuta.

Shumat e korrigjuara janë $S_{xx}=816-72^2/8=168.0000$ dhe $S_{xy}=6650-72(682)/8=512.0000$.

**Zhvillo llogaritjen**

Prandaj $b_1=512.0000/168.0000=3.0476$ minuta për kilometër dhe $b_0=85.2500-(3.0476)(9.0000)=57.8214$ minuta.

Pjerrësia është dallimi i përshtatur prej 3.0476 minuta kur parashikuesi «distanca e udhëtimit» rritet me një kilometër.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është jashtë intervalit të vrojtuar [2, 16], prandaj prerja nevojitet matematikisht, por nuk duhet trajtuar si nivel fillestar i vrojtuar.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=57.8214+(3.0476)X$.

Meqë 2 $\leq$ 9 $\leq$ 16, kërkesa është interpolim.

Në $X=9$, $\widehat Y=57.8214+(3.0476)(9)=85.2500$ minuta.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

### T05-A01-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Përgatit llogaritjen**

Diagrami i plotë i shpërndarjes përdor koordinatat (0, 50), (1, 54), (2, 58), (3, 61), (4, 66), (5, 69), (6, 73), (7, 78), me interval horizontal [0, 7].

Duke i lexuar pikat nga e majta në të djathtë, shfaqet një model afërsisht i drejtë rritës dhe asnjë koordinatë nuk ndahet qartë nga të gjitha pikat fqinje.

Mesataret janë $\bar x=28/8=3.5000$ kontribute dhe $\bar y=509/8=63.6250$ pikë.

Shumat e korrigjuara janë $S_{xx}=140-28^2/8=42.0000$ dhe $S_{xy}=1946-28(509)/8=164.5000$.

**Zhvillo llogaritjen**

Prandaj $b_1=164.5000/42.0000=3.9167$ pikë për kontribut dhe $b_0=63.6250-(3.9167)(3.5000)=49.9167$ pikë.

Pjerrësia është dallimi i përshtatur prej 3.9167 pikë kur parashikuesi «kontributet në diskutim» rritet me një kontribut.

Prerja është rezultati i përshtatur në $X=0$.

Zeroja është brenda intervalit të vrojtuar [0, 7], prandaj prerja përshkruan një nivel fillestar të përshtatur që mbështetet nga këto të dhëna.

**Interpreto dhe kontrollo rezultatin**

Ekuacioni i përshtatur është $\widehat Y=49.9167+(3.9167)X$.

Meqë 0 $\leq$ 4 $\leq$ 7, kërkesa është interpolim.

Në $X=4$, $\widehat Y=49.9167+(3.9167)(4)=65.5833$ pikë.

Kjo është mesatare e kushtëzuar e vlerësuar, jo rezultat i garantuar për një rast.

## A02: Nga mesataret, devijimet standarde dhe kovarianca te vija

### T05-A02-V01: Ushtrimi javor dhe arsyetimi

**Arsyeto para llogaritjes**

Korrelacioni është $r=11.0/(2.2\times8.0)=0.6250$.

Pjerrësia është $b_1=11.0/2.2^2=2.2727$ pikë për një njësi të $X$, dhe $b_0=68-(2.2727)(5.5)=55.5000$ pikë.

**Zhvillo llogaritjen**

Në $X=7.0$, $\widehat Y=55.5000+(2.2727)(7.0)=71.4091$ pikë.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V02: Përvoja në arkiv dhe koha e kërkimit

**Arsyeto para llogaritjes**

Korrelacioni është $r=-36.0/(6.0\times9.0)=-0.6667$.

Pjerrësia është $b_1=-36.0/6.0^2=-1.0000$ minuta për një njësi të $X$, dhe $b_0=42-(-1.0000)(18)=60.0000$ minuta.

**Zhvillo llogaritjen**

Në $X=24$, $\widehat Y=60.0000+(-1.0000)(24)=36.0000$ minuta.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V03: Vizitat në muze dhe njohuritë

**Arsyeto para llogaritjes**

Korrelacioni është $r=13.5/(1.8\times10.0)=0.7500$.

Pjerrësia është $b_1=13.5/1.8^2=4.1667$ pikë për një njësi të $X$, dhe $b_0=62-(4.1667)(4.5)=43.2500$ pikë.

**Zhvillo llogaritjen**

Në $X=6$, $\widehat Y=43.2500+(4.1667)(6)=68.2500$ pikë.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V04: Koha e leximit dhe të kuptuarit

**Arsyeto para llogaritjes**

Korrelacioni është $r=15.75/(2.5\times9.0)=0.7000$.

Pjerrësia është $b_1=15.75/2.5^2=2.5200$ pikë për një njësi të $X$, dhe $b_0=74-(2.5200)(7)=56.3600$ pikë.

**Zhvillo llogaritjen**

Në $X=9$, $\widehat Y=56.3600+(2.5200)(9)=79.0400$ pikë.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V05: Njohja e rrugës dhe gabimet e orientimit

**Arsyeto para llogaritjes**

Korrelacioni është $r=-25.2/(12.0\times3.0)=-0.7000$.

Pjerrësia është $b_1=-25.2/12.0^2=-0.1750$ gabime për një njësi të $X$, dhe $b_0=8-(-0.1750)(55)=17.6250$ gabime.

**Zhvillo llogaritjen**

Në $X=65$, $\widehat Y=17.6250+(-0.1750)(65)=6.2500$ gabime.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto para llogaritjes**

Korrelacioni është $r=7.35/(1.5\times7.0)=0.7000$.

Pjerrësia është $b_1=7.35/1.5^2=3.2667$ pikë për një njësi të $X$, dhe $b_0=51-(3.2667)(3.5)=39.5667$ pikë.

**Zhvillo llogaritjen**

Në $X=5$, $\widehat Y=39.5667+(3.2667)(5)=55.9000$ pikë.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V07: Njoftimet dhe përqendrimi

**Arsyeto para llogaritjes**

Korrelacioni është $r=-82.5/(15.0\times11.0)=-0.5000$.

Pjerrësia është $b_1=-82.5/15.0^2=-0.3667$ pikë për një njësi të $X$, dhe $b_0=70-(-0.3667)(48)=87.6000$ pikë.

**Zhvillo llogaritjen**

Në $X=35$, $\widehat Y=87.6000+(-0.3667)(35)=74.7667$ pikë.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V08: Ushtrimi i kërkimit dhe saktësia

**Arsyeto para llogaritjes**

Korrelacioni është $r=11.2/(2.0\times8.0)=0.7000$.

Pjerrësia është $b_1=11.2/2.0^2=2.8000$ pikë për një njësi të $X$, dhe $b_0=76-(2.8000)(6)=59.2000$ pikë.

**Zhvillo llogaritjen**

Në $X=9$, $\widehat Y=59.2000+(2.8000)(9)=84.4000$ pikë.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Arsyeto para llogaritjes**

Korrelacioni është $r=54.0/(5.0\times18.0)=0.6000$.

Pjerrësia është $b_1=54.0/5.0^2=2.1600$ minuta për një njësi të $X$, dhe $b_0=95-(2.1600)(14)=64.7600$ minuta.

**Zhvillo llogaritjen**

Në $X=18$, $\widehat Y=64.7600+(2.1600)(18)=103.6400$ minuta.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

### T05-A02-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Arsyeto para llogaritjes**

Korrelacioni është $r=18.0/(3.0\times10.0)=0.6000$.

Pjerrësia është $b_1=18.0/3.0^2=2.0000$ pikë për një njësi të $X$, dhe $b_0=67-(2.0000)(8)=51.0000$ pikë.

**Zhvillo llogaritjen**

Në $X=11$, $\widehat Y=51.0000+(2.0000)(11)=73.0000$ pikë.

Korrelacioni nuk ka njësi dhe është simetrik mes $X$ dhe $Y$.

**Interpreto dhe kontrollo rezultatin**

Pjerrësia e regresionit e cakton $Y$ si rezultat, i ruan njësitë e matjes dhe përshkruan ndryshimin e përshtatur të rezultatit për njësi të parashikuesit.

Të dy fillojnë nga e njëjta bashkëndryshueshmëri me shenjë.

## A03: Pjerrësitë e pastandardizuara dhe të standardizuara

### T05-A03-V01: Ushtrimi javor dhe arsyetimi

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar 3.2 do të thotë se një dallim prej një njësie në parashikuesin «orët e ushtrimit javor» shoqërohet me dallim të përshtatur prej 3.2 pikë në rezultatin «pikët e arsyetimit».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=42+(3.2)(2)=48.4000$ pikë.

Pjerrësia e standardizuar është $\beta^*=(3.2)(1.5)/8.0=0.6000$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 1.5 orë, shoqërohet me dallim të përshtatur prej 0.6000 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V02: Përvoja në arkiv dhe koha e kërkimit

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar -1.2 do të thotë se një dallim prej një njësie në parashikuesin «muajt e përvojës në arkiv» shoqërohet me dallim të përshtatur prej -1.2 minuta në rezultatin «koha e kërkimit».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=75+(-1.2)(20)=51.0000$ minuta.

Pjerrësia e standardizuar është $\beta^*=(-1.2)(6.0)/9.0=-0.8000$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 6.0 muaj, shoqërohet me dallim të përshtatur prej -0.8000 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V03: Vizitat në muze dhe njohuritë

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar 4.5 do të thotë se një dallim prej një njësie në parashikuesin «vizitat në muze gjatë këtij viti» shoqërohet me dallim të përshtatur prej 4.5 pikë në rezultatin «pikët e njohurive historike».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=48+(4.5)(3)=61.5000$ pikë.

Pjerrësia e standardizuar është $\beta^*=(4.5)(1.8)/10.0=0.8100$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 1.8 vizita, shoqërohet me dallim të përshtatur prej 0.8100 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V04: Koha e leximit dhe të kuptuarit

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar 2.8 do të thotë se një dallim prej një njësie në parashikuesin «koha javore e leximit» shoqërohet me dallim të përshtatur prej 2.8 pikë në rezultatin «pikët e të kuptuarit».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=55+(2.8)(8)=77.4000$ pikë.

Pjerrësia e standardizuar është $\beta^*=(2.8)(2.5)/9.0=0.7778$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 2.5 orë, shoqërohet me dallim të përshtatur prej 0.7778 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V05: Njohja e rrugës dhe gabimet e orientimit

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar -0.12 do të thotë se një dallim prej një njësie në parashikuesin «pikët e njohjes së rrugës» shoqërohet me dallim të përshtatur prej -0.12 gabime në rezultatin «numri i gabimeve të orientimit».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=18+(-0.12)(60)=10.8000$ gabime.

Pjerrësia e standardizuar është $\beta^*=(-0.12)(12.0)/3.0=-0.4800$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 12.0 pikë, shoqërohet me dallim të përshtatur prej -0.4800 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar 3.5 do të thotë se një dallim prej një njësie në parashikuesin «seancat e ndjekura të seminarit» shoqërohet me dallim të përshtatur prej 3.5 pikë në rezultatin «pikët e vetëbesimit».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=35+(3.5)(4)=49.0000$ pikë.

Pjerrësia e standardizuar është $\beta^*=(3.5)(1.5)/7.0=0.7500$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 1.5 seanca, shoqërohet me dallim të përshtatur prej 0.7500 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V07: Njoftimet dhe përqendrimi

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar -0.3 do të thotë se një dallim prej një njësie në parashikuesin «numri ditor i njoftimeve» shoqërohet me dallim të përshtatur prej -0.3 pikë në rezultatin «pikët e përqendrimit».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=82+(-0.3)(50)=67.0000$ pikë.

Pjerrësia e standardizuar është $\beta^*=(-0.3)(15.0)/11.0=-0.4091$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 15.0 njoftime, shoqërohet me dallim të përshtatur prej -0.4091 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V08: Ushtrimi i kërkimit dhe saktësia

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar 4.0 do të thotë se një dallim prej një njësie në parashikuesin «ushtrimet e përfunduara të kërkimit» shoqërohet me dallim të përshtatur prej 4.0 pikë në rezultatin «pikët e saktësisë së kërkimit».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=60+(4.0)(7)=88.0000$ pikë.

Pjerrësia e standardizuar është $\beta^*=(4.0)(2.0)/8.0=1.0000$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 2.0 ushtrime, shoqërohet me dallim të përshtatur prej 1.0000 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar 2.4 do të thotë se një dallim prej një njësie në parashikuesin «distanca e udhëtimit» shoqërohet me dallim të përshtatur prej 2.4 minuta në rezultatin «kohëzgjatja e vizitës».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=50+(2.4)(16)=88.4000$ minuta.

Pjerrësia e standardizuar është $\beta^*=(2.4)(5.0)/18.0=0.6667$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 5.0 kilometra, shoqërohet me dallim të përshtatur prej 0.6667 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

### T05-A03-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Përgatit llogaritjen**

Pjerrësia e pastandardizuar 3.0 do të thotë se një dallim prej një njësie në parashikuesin «kontributet në diskutim» shoqërohet me dallim të përshtatur prej 3.0 pikë në rezultatin «pikët e arsyetimit».

**Zhvillo llogaritjen**

Parashikimi është $\widehat Y=40+(3.0)(10)=70.0000$ pikë.

Pjerrësia e standardizuar është $\beta^*=(3.0)(3.0)/10.0=0.9000$.

**Interpreto dhe kontrollo rezultatin**

Kështu, një dallim prej një devijimi standard në parashikues, i barabartë me 3.0 kontribute, shoqërohet me dallim të përshtatur prej 0.9000 devijimesh standarde të rezultatit.

Numri i pastandardizuar i përgjigjet pyetjes në njësitë fillestare; numri i standardizuar i përgjigjet pyetjes në devijime standarde.

## A04: Krahasimi i dy rezultateve të regresionit të thjeshtë

### T05-A04-V01: Ushtrimi javor dhe arsyetimi

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë 2.6 në Rezultatin A dhe 3.1 në Rezultatin B; 38 dhe 45 janë prerje.

Kur parashikuesi «orët e ushtrimit javor» rritet me një orë, rezultati i përshtatur «pikët e arsyetimit» rritet me 2.60 pikë.

**Zhvillo llogaritjen**

Kur parashikuesi «seancat e udhëzuara të studimit» rritet me një seancë, rezultati i përshtatur rritet me 3.10 pikë.

Pjerrësitë e standardizuara janë 0.49 dhe 0.58.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «seancat e udhëzuara të studimit» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një orë te parashikuesi «orët e ushtrimit javor» nuk ka të njëjtën shkallë si një seancë te parashikuesi «seancat e udhëzuara të studimit».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V02: Përvoja në arkiv dhe koha e kërkimit

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë -1.5 në Rezultatin A dhe -2.2 në Rezultatin B; 80 dhe 70 janë prerje.

Kur parashikuesi «muajt e përvojës në arkiv» rritet me një muaj, rezultati i përshtatur «koha e kërkimit» ulet me 1.50 minuta.

**Zhvillo llogaritjen**

Kur parashikuesi «seancat e praktikës së rikujtimit» rritet me një seancë, rezultati i përshtatur ulet me 2.20 minuta.

Pjerrësitë e standardizuara janë -0.46 dhe -0.35.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «muajt e përvojës në arkiv» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një muaj te parashikuesi «muajt e përvojës në arkiv» nuk ka të njëjtën shkallë si një seancë te parashikuesi «seancat e praktikës së rikujtimit».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V03: Vizitat në muze dhe njohuritë

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë 4.2 në Rezultatin A dhe 3.6 në Rezultatin B; 45 dhe 50 janë prerje.

Kur parashikuesi «vizitat në muze gjatë këtij viti» rritet me një vizitë, rezultati i përshtatur «pikët e njohurive historike» rritet me 4.20 pikë.

**Zhvillo llogaritjen**

Kur parashikuesi «seancat e leximit të historisë» rritet me një seancë, rezultati i përshtatur rritet me 3.60 pikë.

Pjerrësitë e standardizuara janë 0.58 dhe 0.44.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «vizitat në muze gjatë këtij viti» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një vizitë te parashikuesi «vizitat në muze gjatë këtij viti» nuk ka të njëjtën shkallë si një seancë te parashikuesi «seancat e leximit të historisë».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V04: Koha e leximit dhe të kuptuarit

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë 3.0 në Rezultatin A dhe 0.9 në Rezultatin B; 52 dhe 48 janë prerje.

Kur parashikuesi «koha javore e leximit» rritet me një orë, rezultati i përshtatur «pikët e të kuptuarit» rritet me 3.00 pikë.

**Zhvillo llogaritjen**

Kur parashikuesi «faqet e shënuara në javë» rritet me një faqe, rezultati i përshtatur rritet me 0.90 pikë.

Pjerrësitë e standardizuara janë 0.4 dhe 0.55.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «faqet e shënuara në javë» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një orë te parashikuesi «koha javore e leximit» nuk ka të njëjtën shkallë si një faqe te parashikuesi «faqet e shënuara në javë».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V05: Njohja e rrugës dhe gabimet e orientimit

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë -0.1 në Rezultatin A dhe -0.55 në Rezultatin B; 15 dhe 13 janë prerje.

Kur parashikuesi «pikët e njohjes së rrugës» rritet me një pikë, rezultati i përshtatur «numri i gabimeve të orientimit» ulet me 0.10 gabime.

**Zhvillo llogaritjen**

Kur parashikuesi «përpjekjet e mëparshme në rrugë» rritet me një përpjekje, rezultati i përshtatur ulet me 0.55 gabime.

Pjerrësitë e standardizuara janë -0.35 dhe -0.62.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «përpjekjet e mëparshme në rrugë» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një pikë te parashikuesi «pikët e njohjes së rrugës» nuk ka të njëjtën shkallë si një përpjekje te parashikuesi «përpjekjet e mëparshme në rrugë».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë 3.8 në Rezultatin A dhe 2.7 në Rezultatin B; 33 dhe 40 janë prerje.

Kur parashikuesi «seancat e ndjekura të seminarit» rritet me një seancë, rezultati i përshtatur «pikët e vetëbesimit» rritet me 3.80 pikë.

**Zhvillo llogaritjen**

Kur parashikuesi «seancat me komente nga bashkëmoshatarët» rritet me një seancë, rezultati i përshtatur rritet me 2.70 pikë.

Pjerrësitë e standardizuara janë 0.55 dhe 0.47.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «seancat e ndjekura të seminarit» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një seancë te parashikuesi «seancat e ndjekura të seminarit» nuk ka të njëjtën shkallë si një seancë te parashikuesi «seancat me komente nga bashkëmoshatarët».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V07: Njoftimet dhe përqendrimi

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë -0.28 në Rezultatin A dhe 2.4 në Rezultatin B; 85 dhe 78 janë prerje.

Kur parashikuesi «numri ditor i njoftimeve» rritet me një njoftim, rezultati i përshtatur «pikët e përqendrimit» ulet me 0.28 pikë.

**Zhvillo llogaritjen**

Kur parashikuesi «blloqet e planifikuara të përqendrimit» rritet me një bllok, rezultati i përshtatur rritet me 2.40 pikë.

Pjerrësitë e standardizuara janë -0.42 dhe 0.51.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «blloqet e planifikuara të përqendrimit» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një njoftim te parashikuesi «numri ditor i njoftimeve» nuk ka të njëjtën shkallë si një bllok te parashikuesi «blloqet e planifikuara të përqendrimit».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V08: Ushtrimi i kërkimit dhe saktësia

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë 4.4 në Rezultatin A dhe 1.5 në Rezultatin B; 58 dhe 62 janë prerje.

Kur parashikuesi «ushtrimet e përfunduara të kërkimit» rritet me një ushtrim, rezultati i përshtatur «pikët e saktësisë së kërkimit» rritet me 4.40 pikë.

**Zhvillo llogaritjen**

Kur parashikuesi «muajt e përvojës në arkiv» rritet me një muaj, rezultati i përshtatur rritet me 1.50 pikë.

Pjerrësitë e standardizuara janë 0.63 dhe 0.39.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «ushtrimet e përfunduara të kërkimit» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një ushtrim te parashikuesi «ushtrimet e përfunduara të kërkimit» nuk ka të njëjtën shkallë si një muaj te parashikuesi «muajt e përvojës në arkiv».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë 2.1 në Rezultatin A dhe 4.5 në Rezultatin B; 47 dhe 55 janë prerje.

Kur parashikuesi «distanca e udhëtimit» rritet me një kilometër, rezultati i përshtatur «kohëzgjatja e vizitës» rritet me 2.10 minuta.

**Zhvillo llogaritjen**

Kur parashikuesi «ndalesat e planifikuara» rritet me një ndalesë, rezultati i përshtatur rritet me 4.50 minuta.

Pjerrësitë e standardizuara janë 0.38 dhe 0.66.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «ndalesat e planifikuara» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një kilometër te parashikuesi «distanca e udhëtimit» nuk ka të njëjtën shkallë si një ndalesë te parashikuesi «ndalesat e planifikuara».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

### T05-A04-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Arsyeto para llogaritjes**

Vlerësimet e parashikuesve janë 2.7 në Rezultatin A dhe 3.4 në Rezultatin B; 43 dhe 49 janë prerje.

Kur parashikuesi «kontributet në diskutim» rritet me një kontribut, rezultati i përshtatur «pikët e arsyetimit» rritet me 2.70 pikë.

**Zhvillo llogaritjen**

Kur parashikuesi «koha e përgatitjes» rritet me një orë, rezultati i përshtatur rritet me 3.40 pikë.

Pjerrësitë e standardizuara janë 0.45 dhe 0.52.

Ato shprehin ndryshime të përshtatura në devijime standarde të rezultatit për një devijim standard të parashikuesit, ndaj mund të krahasohen madhësitë absolute: parashikuesi «koha e përgatitjes» ka lidhjen absolute të standardizuar më të madhe në këto dy modele të veçanta.

**Interpreto dhe kontrollo rezultatin**

Në regresionin e thjeshtë me prerje, secila pjerrësi e standardizuar është edhe korrelacioni i Pearson-it mes atij parashikuesi dhe rezultatit.

Pjerrësitë e papërpunuara nuk mund të renditen sipas forcës, sepse një kontribut te parashikuesi «kontributet në diskutim» nuk ka të njëjtën shkallë si një orë te parashikuesi «koha e përgatitjes».

Këto janë dy lidhje bivariate; asnjëra nuk e mban parashikuesin tjetër konstant dhe nuk vendos efekt shkakor.

## A05: Koeficientët dhe ndryshueshmëria e shpjeguar

### T05-A05-V01: Ushtrimi javor dhe arsyetimi

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=120/180=0.6667$.

Ndryshueshmëria e shpjeguar është $SSR=720-640.0000=80.0000$, që është gjithashtu $b_1S_{xy}=0.6667(120)=80.0000$.

**Zhvillo llogaritjen**

Prandaj $R^2=80.0000/720=0.1111$.

Vlera e përshtatur është $\widehat Y=40+(0.6667)(8)=45.3333$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 11.1% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 88.9% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V02: Përvoja në arkiv dhe koha e kërkimit

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=-84/210=-0.4000$.

Ndryshueshmëria e shpjeguar është $SSR=630-596.4000=33.6000$, që është gjithashtu $b_1S_{xy}=-0.4000(-84)=33.6000$.

**Zhvillo llogaritjen**

Prandaj $R^2=33.6000/630=0.0533$.

Vlera e përshtatur është $\widehat Y=42+(-0.4000)(20)=34.0000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 5.3% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 94.7% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V03: Vizitat në muze dhe njohuritë

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=144/240=0.6000$.

Ndryshueshmëria e shpjeguar është $SSR=840-753.6000=86.4000$, që është gjithashtu $b_1S_{xy}=0.6000(144)=86.4000$.

**Zhvillo llogaritjen**

Prandaj $R^2=86.4000/840=0.1029$.

Vlera e përshtatur është $\widehat Y=36+(0.6000)(6)=39.6000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 10.3% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 89.7% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V04: Koha e leximit dhe të kuptuarit

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=135/225=0.6000$.

Ndryshueshmëria e shpjeguar është $SSR=900-819.0000=81.0000$, që është gjithashtu $b_1S_{xy}=0.6000(135)=81.0000$.

**Zhvillo llogaritjen**

Prandaj $R^2=81.0000/900=0.0900$.

Vlera e përshtatur është $\widehat Y=50+(0.6000)(9)=55.4000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 9.0% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 91.0% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V05: Njohja e rrugës dhe gabimet e orientimit

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=-66/132=-0.5000$.

Ndryshueshmëria e shpjeguar është $SSR=528-495.0000=33.0000$, që është gjithashtu $b_1S_{xy}=-0.5000(-66)=33.0000$.

**Zhvillo llogaritjen**

Prandaj $R^2=33.0000/528=0.0625$.

Vlera e përshtatur është $\widehat Y=44+(-0.5000)(60)=14.0000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 6.2% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 93.8% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=114/190=0.6000$.

Ndryshueshmëria e shpjeguar është $SSR=760-691.6000=68.4000$, që është gjithashtu $b_1S_{xy}=0.6000(114)=68.4000$.

**Zhvillo llogaritjen**

Prandaj $R^2=68.4000/760=0.0900$.

Vlera e përshtatur është $\widehat Y=38+(0.6000)(5)=41.0000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 9.0% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 91.0% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V07: Njoftimet dhe përqendrimi

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=-96/240=-0.4000$.

Ndryshueshmëria e shpjeguar është $SSR=960-921.6000=38.4000$, që është gjithashtu $b_1S_{xy}=-0.4000(-96)=38.4000$.

**Zhvillo llogaritjen**

Prandaj $R^2=38.4000/960=0.0400$.

Vlera e përshtatur është $\widehat Y=48+(-0.4000)(45)=30.0000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 4.0% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 96.0% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V08: Ushtrimi i kërkimit dhe saktësia

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=138/230=0.6000$.

Ndryshueshmëria e shpjeguar është $SSR=920-837.2000=82.8000$, që është gjithashtu $b_1S_{xy}=0.6000(138)=82.8000$.

**Zhvillo llogaritjen**

Prandaj $R^2=82.8000/920=0.0900$.

Vlera e përshtatur është $\widehat Y=46+(0.6000)(8)=50.8000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 9.0% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 91.0% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=104/208=0.5000$.

Ndryshueshmëria e shpjeguar është $SSR=832-780.0000=52.0000$, që është gjithashtu $b_1S_{xy}=0.5000(104)=52.0000$.

**Zhvillo llogaritjen**

Prandaj $R^2=52.0000/832=0.0625$.

Vlera e përshtatur është $\widehat Y=52+(0.5000)(18)=61.0000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 6.2% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 93.8% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

### T05-A05-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Përgatit llogaritjen**

Pjerrësia është $b_1=S_{xy}/S_{xx}=100/200=0.5000$.

Ndryshueshmëria e shpjeguar është $SSR=800-750.0000=50.0000$, që është gjithashtu $b_1S_{xy}=0.5000(100)=50.0000$.

**Zhvillo llogaritjen**

Prandaj $R^2=50.0000/800=0.0625$.

Vlera e përshtatur është $\widehat Y=40+(0.5000)(10)=45.0000$.

**Interpreto dhe kontrollo rezultatin**

Modeli shpjegon 6.2% të ndryshueshmërisë totale në katror të kampionit rreth $\bar y$; 93.8% e mbetur paraqitet nga ndryshueshmëria e rezidualeve në katror.

Kjo është ndarje e ndryshueshmërisë për kampionin e përshtatur, jo normë suksesi dhe jo evidencë shkakore.

## A06: Testet dhe intervalet e besimit për pjerrësinë

### T05-A06-V01: Ushtrimi javor dhe arsyetimi

**Arsyeto para llogaritjes**

Statistika është $t=2.4/0.75=3.2000$ me $df=22$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{22}\geq|3.2000|)=0.0041$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(22)=2.0739$, prandaj intervali është $2.4\pm2.0739(0.75)=[0.8446, 3.9554]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është 2.4 pikë kur parashikuesi «orët e ushtrimit javor» rritet me një orë.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V02: Përvoja në arkiv dhe koha e kërkimit

**Arsyeto para llogaritjes**

Statistika është $t=-1.6/0.6=-2.6667$ me $df=28$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{28}\geq|-2.6667|)=0.0126$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(28)=2.0484$, prandaj intervali është $-1.6\pm2.0484(0.6)=[-2.8290, -0.3710]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është -1.6 minuta kur parashikuesi «muajt e përvojës në arkiv» rritet me një muaj.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V03: Vizitat në muze dhe njohuritë

**Arsyeto para llogaritjes**

Statistika është $t=3.1/1.05=2.9524$ me $df=34$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{34}\geq|2.9524|)=0.0057$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(34)=2.0322$, prandaj intervali është $3.1\pm2.0322(1.05)=[0.9661, 5.2339]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është 3.1 pikë kur parashikuesi «vizitat në muze gjatë këtij viti» rritet me një vizitë.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V04: Koha e leximit dhe të kuptuarit

**Arsyeto para llogaritjes**

Statistika është $t=2.0/0.68=2.9412$ me $df=40$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{40}\geq|2.9412|)=0.0054$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(40)=2.0211$, prandaj intervali është $2.0\pm2.0211(0.68)=[0.6257, 3.3743]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është 2.0 pikë kur parashikuesi «koha javore e leximit» rritet me një orë.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V05: Njohja e rrugës dhe gabimet e orientimit

**Arsyeto para llogaritjes**

Statistika është $t=-0.11/0.05=-2.2000$ me $df=48$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{48}\geq|-2.2000|)=0.0327$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(48)=2.0106$, prandaj intervali është $-0.11\pm2.0106(0.05)=[-0.2105, -0.0095]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është -0.11 gabime kur parashikuesi «pikët e njohjes së rrugës» rritet me një pikë.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Arsyeto para llogaritjes**

Statistika është $t=2.8/0.9=3.1111$ me $df=58$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{58}\geq|3.1111|)=0.0029$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(58)=2.0017$, prandaj intervali është $2.8\pm2.0017(0.9)=[0.9985, 4.6015]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është 2.8 pikë kur parashikuesi «seancat e ndjekura të seminarit» rritet me një seancë.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V07: Njoftimet dhe përqendrimi

**Arsyeto para llogaritjes**

Statistika është $t=-0.24/0.1=-2.4000$ me $df=68$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{68}\geq|-2.4000|)=0.0191$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(68)=1.9955$, prandaj intervali është $-0.24\pm1.9955(0.1)=[-0.4395, -0.0405]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është -0.24 pikë kur parashikuesi «numri ditor i njoftimeve» rritet me një njoftim.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V08: Ushtrimi i kërkimit dhe saktësia

**Arsyeto para llogaritjes**

Statistika është $t=3.6/1.1=3.2727$ me $df=78$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{78}\geq|3.2727|)=0.0016$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(78)=1.9908$, prandaj intervali është $3.6\pm1.9908(1.1)=[1.4101, 5.7899]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është 3.6 pikë kur parashikuesi «ushtrimet e përfunduara të kërkimit» rritet me një ushtrim.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Arsyeto para llogaritjes**

Statistika është $t=1.5/0.72=2.0833$ me $df=88$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{88}\geq|2.0833|)=0.0401$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(88)=1.9873$, prandaj intervali është $1.5\pm1.9873(0.72)=[0.0692, 2.9308]$.

Zeroja është jashtë intervalit, ndaj testi përkatës dyanësh e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është 1.5 minuta kur parashikuesi «distanca e udhëtimit» rritet me një kilometër.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

### T05-A06-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Arsyeto para llogaritjes**

Statistika është $t=1.2/0.62=1.9355$ me $df=98$.

Vlera e saktë p dyanëshe nga shpërndarja t është $p=2P(T_{98}\geq|1.9355|)=0.0558$.

**Zhvillo llogaritjen**

Vlera kritike 95% është $t_{0.975}(98)=1.9845$, prandaj intervali është $1.2\pm1.9845(0.62)=[-0.0304, 2.4304]$.

Zeroja është brenda intervalit, ndaj testi përkatës dyanësh nuk e refuzon $H_0$.

**Interpreto dhe kontrollo rezultatin**

Ndryshimi i përshtatur i vlerësuar është 1.2 pikë kur parashikuesi «kontributet në diskutim» rritet me një kontribut.

Intervali tregon gamën e pjerrësive të popullatës që përputhen me këtë procedurë dhe kampion nën supozimet e modelit linear.

Vlera p dhe intervali përdorin të njëjtën shpërndarje t referuese, ndaj vendimet e tyre pajtohen.

## A07: Testi i modelit të regresionit të thjeshtë përmes R-katrorit

### T05-A07-V01: Ushtrimi javor dhe arsyetimi

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.28/1]/[(1-0.28)/(20-2)]=7.0000$.

Meqë 7.0000 e tejkalon 4.414, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V02: Përvoja në arkiv dhe koha e kërkimit

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.22/1]/[(1-0.22)/(25-2)]=6.4872$.

Meqë 6.4872 e tejkalon 4.279, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V03: Vizitat në muze dhe njohuritë

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.18/1]/[(1-0.18)/(30-2)]=6.1463$.

Meqë 6.1463 e tejkalon 4.196, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V04: Koha e leximit dhe të kuptuarit

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.15/1]/[(1-0.15)/(35-2)]=5.8235$.

Meqë 5.8235 e tejkalon 4.139, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V05: Njohja e rrugës dhe gabimet e orientimit

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.12/1]/[(1-0.12)/(40-2)]=5.1818$.

Meqë 5.1818 e tejkalon 4.098, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V06: Pjesëmarrja në seminar dhe vetëbesimi

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.1/1]/[(1-0.1)/(50-2)]=5.3333$.

Meqë 5.3333 e tejkalon 4.043, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V07: Njoftimet dhe përqendrimi

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.08/1]/[(1-0.08)/(60-2)]=5.0435$.

Meqë 5.0435 e tejkalon 4.007, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V08: Ushtrimi i kërkimit dhe saktësia

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.07/1]/[(1-0.07)/(75-2)]=5.4946$.

Meqë 5.4946 e tejkalon 3.972, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V09: Distanca e udhëtimit dhe kohëzgjatja e vizitës

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.06/1]/[(1-0.06)/(90-2)]=5.6170$.

Meqë 5.6170 e tejkalon 3.949, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.

### T05-A07-V10: Pjesëmarrja në diskutim dhe arsyetimi

**Përgatit llogaritjen**

Hipoteza zero është $H_0:\beta_1=0$, në mënyrë të barasvlershme $H_0:R_{population}^2=0$ për këtë model linear me një parashikues.

**Zhvillo llogaritjen**

$F=[0.05/1]/[(1-0.05)/(120-2)]=6.2105$.

Meqë 6.2105 e tejkalon 3.921, e refuzojmë hipotezën zero në 5%.

**Interpreto dhe kontrollo rezultatin**

Kampioni jep evidencë për një pjerrësi lineare të popullatës të ndryshme nga zero.

Me një parashikues, $F=t^2$ për testin e pjerrësisë, ndaj testi global i modelit dhe testi dyanësh i koeficientit bëjnë të njëjtën pyetje dhe japin të njëjtin vendim.
