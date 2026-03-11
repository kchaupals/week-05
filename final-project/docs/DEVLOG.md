# Izstrādes žurnāls

## 1. solis: Plānošana
Plānošanas procesā biju pārliecināts, par to, ka šo programmu vēlos veidot ar GUI, plašām funkcijām utt.
Atgriežoties pie plāna norādīta un salīdzinot ar nepieciešamo laiku, lai iegūtu pilnība funkcionējošu programmu ar GUI, saskaros ar to, ka tas nav izdarāms līdz darba iesniegšanas brīdim.
Balsoties uz šo, skaidrs, ka pilnīga pieturēšanas pie izstrādes plāna nav iespējama. Izveidoju projekta skeletu - pamata faili, direkotijas utt. Faili satur aizpildošu tekstu, bez loģikas.

## 2. solis: Pamata darbības
Sākumā bija doma pārkopēt datus no 4.nedēļas darba, bet tad domājot par "scalability" un iespēju pievienot GUI nākotnē, izdomāju veidot šo visu no 0 - itkā laika ziņā tas neatmaksājas, bet kodu iespējams veidot
daudz atbilstošāk šis programmas vajadzībam un iespējams uzlabot vai labot nepilnības, kas atspoguļojās 4.nedēļas darbā. 
Pamata nostādne bija iegūt moduli, kas darbojas un izpilda nepieciešamās prasības - iegūstot vēlamo rezultātu, pilnveidoju kodu un funkcijas. Šajā gadījuma, ņemot vērā, ka 4.nedēļas darbā izmantoju Python iekļautu moduli argparse, tad šajā projekta to neizmantošu. Tādēļ esmu spiests veidot saucamo loop, kas attiecīgi ielasa lietotāja ievadi un balstoties uz šo ievadi izpilda funkciju, pārslēdz izvēlni vai aizver programmu.
Pievienoju ievades datu validāciju, id numura piešķiršanu fonā, kad lietotājs pievieno izdevumu. Izveidoju datu ielasi un izvadi uz JSON. 

## 3.solis: Filtrēšana, kopsavilkums un dzēšana
Izveidoju funkciju, kas veic filtrāciju pēc mēneša, kas ir sasaistīts ar funkciju, kas izvada mēnešus(ar gadu), kuros ir definēti izdevumi. Galā sakārtoju izvēlnes iespējas app.py, lai lietotājs varētu inicializēt šo filtrēšanu
Papildus šim, veicu arī nelielas korekcijas sum_total(), kas tagad ielasa izdevumus, attiecīgi padarot šo funkciju izmantojamu vairākos etapos. Balstoties uz filtrēšanu, izveidoju arī kopsavilkuma atspoguļojumu kategorijām.
Šajā etapa grūtākais bija izprast, ka izveidot funkciju datu izvadi, kas lielākoties ir tabulu veida strukturizāciju bez print() komandas. Atrisinot šo, tālāk jau viss kļuva nedaudz vieglāk, protams, ja neskaita to, ka brižiem liekas, pievienojot ko jaunu, jau darbojošas funkcijas mēdz sastapties ar problēmam - nav pilnīga izpilde vai attainojas kļūdu paziņojums. Šeit cik noprotu, lielāka problēma ir ar šo datu izvadi, ja viena funkcija jau izveido vārdnīcu vai sarakstu, tad datu attēlojums var būt nekorekts vai arī tiek izvadīta globāla Python kļūda par neatbilstību datu tipos utt.


## 4.solis: CSV eksports un dokumentācija
Par CSV eksportu, izmantoju jau sarakstītu kodu no 4.nedēļas, tik cik pielāgoju mainīgos un vizuālas nianses. Veicu pārbaudi un kļūdu apstrādi, iespējoju opciju UTF-8-SIG encodingam.
Ņemot vēra, ka 4.nedēļas darbā jau bija sagatavots ar opciju eksportēt CSV vai TXT, tad jau no sākuma saglabāju esošo funkcionālu un pielāgoju šai aplikācijai.
Papildus eksportam, pievienoju vai atjaunoju funkciju DOCSTRING, notīru neizmantotos moduļus no app.py, logic.py, storage.py un export.py datnem
Izveidoju README failu - balsoties uz programmas pamatfunkciju, uzstādīšanas niansēm un lietojuma komandām. Liekot uzsvaru uz vienkāršu lietojāmību.
Apkopoju izstrādes laika paveikto un novēroto - izstrādes žurnāla.

