# Python: Izdevumu izsekotājs [Expense Tracker]
## Programmas apraksts

Šī programma ir vienkārsš rīks, kas ar pārskatāmu lietotāja grafisko intefeisu (GUI), ļauj ērti un vienkārši sekot līdzi izdevumiem.
Pamatfunkcijas - izdevumu grupēšana, iespēja pievienot dažādas kategorijas, šķirot pēc datuma, mēneša vai gada, iestatīt izdevuma limitus, kā arī veikt datu eksportēšanu uz CSV vai vienkāršu teksta failu
Programma ir domāta kā fiziskām personām privātajai lietošanai, tā arī saimnieciskas darbības veicējiem.

## Datu struktūra

Viena izdevuma ieraksta piemērs:
```
Izdevumu ieraksts 
    id: int
    datums: YYYY-MM-DD
    summa: decimal
    dokumenta Nr/ identifikātors: str
    kategorija: str
    apraksts: str
    maksājuma veids: str

```
 Šada struktūra izvēlēta balstoties uz pārsvarā būtiskākajiem faktoriem, kas būtu nepieciešami gan filtrējot šos datus, gan tālāk apstrādājot

 ## Moduļu plāns

### app.py

Galvenais modulis, kas apvieno programmas datu ievadi / izvadi, palaižot programmu startē GUI, kur lietotājs vienkārši caur grafisko saskarni var veikt darbības ar programmu. Apvieno visus zemāk minētos moduļus.


Iekļauj šādas pamatfunkcijas:
> main()
```
Startē pašu aplikāciju
- Izveido pamatlogu OS vidē
- Inicializē UI komponentus
- Iegūst saglabātos sarakstus
- Inicializē GUI ciklu, kas ļauj lietotājam vadīt programmu ar grafisko saskarni un saņemt atgriezenisko saiti
 ```       
> create_expense_form()

Izveido formu, caur kuru ievada izdevumu datus  
```
Datu lauki: 
- Datums
- Summa
- Dokumenta Nr. / identifikātors
- Kategorija
- Apraksts
- Maksājuma veids
 ```   
> submit_expense()

Funkcija, kas tiek palaista, kad lietotājs pievieno jaunu izdevumu ierakstu.\
```
Pamatuzdevumi:
- Ievākt datus no lietotāja aizpildītas formas
- Datu validācija
- Izsaukt logic.py funkciju datu saglabāšanai
- Atjaunot izdevumu sarakstu GUI
- Ja iestatīts izdevumu limits - pārbaudīt vai tas nav sasniegts
 ```   
> refresh_expense_table()

Funkcija, kas atjauno aktīvo izdevumu sarakstu

> delete_selected_expense()

Funkcija, kas ļauj izdzēst izdevumu no saraksta

> switch_expense_list()

Funkcija, kas ļauj nomainīt aktīvo izdevumu sarakstu uz citu.\
```
Pamatuzdevumi:
- Noteikt aktīvo sarakstu
- Izsaukt logic.py funkciju, kas nomaina sarakstus
- Atsvaidzināt UI datus
```    
> set_spending_limit()

Funkcija, kas ļauj lietotājam noteikt izdevumu limitus\
```
Datu lauki:
- periods (diena/nedēļa/mēnesis/gads)
- limita summa\
Apstrāda ievadi caur logic.py
```
> export_data()

Funkcija, kas ļauj lietotājam eksportēt izdevuma sarakstu.\
Izsauc izvēlēta eksportēšanas veida funkciju no export.py

> show_statistics()

Funkcija, kas atspoguļo izdevumus pa kategorijam\
Izsauc attiecīgo logic.py funkciju

> search_expenses()

Funkcija, kas ļauj meklēt izdevuma sarakstā
```
Datu ievade:
- Atslēgasvārds
- Kategorija
- Periods\
Izsauc attiecīgo logic.py funkciju
```
    

### storage.py

Modulis, kas atbild par datu apstrādi, ielasīšanu, ierakstīšanu JSON failā vai failos.\

> load_data()

Ielāde visus saglabātos datus
```
Iekļauj:
    - Izdevumu sarakstus
    - Izdevumu limitus
    - Iestatījumus
```

> save_data(data)

Ieraksta datus atmiņā - JSON

> generate_new_id(expenses)

Izveido unikālu ID numuru jaunam ierakstam

> save_limits(limits)  

Ieraksta atmiņa izdevumu limitus

> load_limits()

Ielasa izdevumu limitus

> save_lists(lists)

Saglabā visus izdevumu sarakstus

> load_lists()

Ielasa saglabātos izdevumu sarakstus

<br>
<br>

### logic.py

Modulis, kas atbild par biznesa loģiku - apstrāda datus, filtrē tos utt.\

> add_expense(expense_data)

Pievieno jaunu izdevumu aktivajā sarakstā
```
Soļi:
    - ģenerē ID
    - pievieno izdevumu pie aktivā saraksta
    - saglabā atjaunotos datus
    - pārbauda izdevumu limitus
```

> delete_expense(expense_id)

Izdzēš izdevumu pēc tā ID numura

> get_all_expenses()

Ielasa izdevumus no aktivā izdevumu saraksta

> calculate_total()

Aprēķina kopsummu aktivājam sarakstam

> filter_by_category(category)

Atgriež izdevumus pēc izvēlētas kategorijas

> set_limit(period, amount)

Definē izdevumu limitu aktivajām sarakstam (dienas / nedēļas / mēneša / gada)

> get_limit(period)

Atgriez iestatīto izdevumu ierobežojuma limitu

> calculate_period_total(period)

Aprēķina izdevumus par konkrētu laika posmu

> check_limit(period)

Salidzīna esošos izdevumus ar definēto limitu
```
Atgriež:
    bool: True ja pārsniedz, false ja nē
```

> create_list(list_name)

Izveido jaunu izdevumu sarakstu

> switch_list(list_name)

Nomaina aktīvo izdevumu sarakstu

> get_current_list()

Atgriež aktīva izdevumu saraksta nosaukumu

> get_expenses_from_current_list()

Atgriež izdevumus, kas atspoguļoti aktīvajā izdevumu sarakstā

> calculate_category_totals()

Aprēķina kopējos izdevumus pa kategorijam (Izmanto statistikai)

> search_expenses(keyword)

Meklē izdevumus balstoties uz aprakstu vai kategoriju

> filter_by_date(start_date, end_date)

Atgriež izdevumus, kas iekļaujas laika intervālā

> generate_summary_report() 

Ģenerē kopsummas statistiku (Kopējie izdevumi, kategoriju kopēja summa, perioda kopsumma)



### export.py

Modulis, kura pamatfunkcija ir sarakstu izvade, eksports uz CSV vai vienkāršu teksta failu

> export_to_csv(expenses, file_path)

Eksportē sarakstu CSV formatā

> export_to_json(expenses, file_path)

Eksportē sarakstu JSON formatā

> export_to_text(expenses, file_path)

Eksportē sarakstu TXT formatā

> export_summary(expenses,file_type, file_path)

Eksporte kopsummas statistiku ar formata izvēles iespēju


### Programmas direktorijas un failu izkārtojums
Zemāk attēlots, kādus failus un direktorijas satur pamatprogramma - Expense Tracker


```
└─── expense_tracker/
    ├── app.py
    ├── logic.py
    ├── storage.py
    ├── export.py
    ├── expenses.json
    └── lists
    │   └── company.json
    └── exports 
        └── monthly_expenses_january.csv
```

## Lietotāja scenāriji
Zemāk aprakstīti pāris lietotāja scenāriji

### Piemērs -jauna izdevuma pievienošana

> Lietotāja darbības

Lietotājs vēlas pievienot jaunu izdevumu.

Soļi:
```
    1. Lietotājs atvēr aplikāciju.
    2. Lietotājs izvēlas izdevumu sarakstu.
    3. Lietotājs uzspiež uz pogas - "Pievienot izdevumu"
    4. Lietotājs aizpilda datus veidlapa:
        Datums: 2026-03-03
        Summa: 1500.00
        Dokumenta Nr./ID: EKA020211
        Kategorija: Transports
        Apraksts: Auto apkope
        Maksājuma veids: Bankas karte
    5. Lietotājs uzspiež uz pogas - "Pievienot"
```

> Programmas darbības

```
    1. Programma ielasa lietotāja datus
    2. Ievades dati tiek validēti
    3. Izdevumi tiek padoti funkcijai logic.add_expense()
    4. Jauns izdevumu ID ir ģenerēts
    5. Izdevums ir pievienots aktivājam izdevumu sarakstam
    6. Dati ir saglabāti JSON failā
    7. Izdevumu tabula GUI tiek atsvaidzināta
    8. Jaunais izdevumu ieraksts tiek attēlots programma
```

### Piemērs - Izdevumu ierobežojuma limita paziņojums

> Lietotāja darbības

Lietotājs ir iestatījis izdevumu ierobežojuma limitu 300€/mēnesī

Soļi:
```
    1. Lietotājs pievieno izdevumu par 370€
    2. Kopēja mēneša izdevumi - 370€
```

> Programmas darbības
```
    1. logic.check_limit("monthly") tiek izsaukts
    2. Programma aprēķina tekošos mēneša izdevumus
    3. Izdevumi pārsniedz limita summu.
    4. Programma attēlo paziņojumu:
        "Uzmanību: Ir pārsniegts iestatītais mēneša izdevumu limits"
    5. Izdevums tāpat tiek reģistrēts, bet lietotājs tiek informēts
```

### Piemērs - Sarakstu pārslēgšana

> Lietotāja darbības

Lietotājs vēlas pārslēgties no darba uz personīgo izdevumu sarakstu

Soļi:
```
    1. Lietotajs atvēr sarakstu izvēli uzspiežot GUI pogu - "Mainīt sarakstu"
    2. No saraksta izvēlas "Personīgs"
```

> Programmas darbības 

```
    1. switch_expense_list() tiek palaists
    2. logic.switch_list("Personīgs") tiek definēts kā aktivais saraksts
    3. Izdevumi, kas definēti "Personīgs" saraksta tiek iegūti
    4. GUI atspoguļo aktīva izdevuma saraksta datus
    5. Tikai izdevumu saraksta "Personīgs" dati tiek atspoguļoti GUI
```

## Robežgadījumi

### Piemērs - nepareiza vērtības ievade

> Lietotāja darbības

Lietotājs cenšas pievienot jaunu izdevumu, bet ievada nekoretu vērtību

Soļi:
```
    1. Lietotājs atver izdevumu pievienošans veidlapu
    2. Lietotajs ievada sekojošus datus:
        Datums: 2026-15-15
        Summa: 1500.00
        Dokumenta Nr./ID: EKA020211
        Kategorija: Transports
        Apraksts: Auto apkope
        Maksājuma veids: Bankas karte
    3. Lietotājs nospiež "Pievienot" pogu
```

> Programmas darbības
```
    1. submit_expense() ielasa veidlapas datus
    2. Ievades dati tiek validēti
    3. Validācija ir neveiksmīga, jo datums ir nekorekts
    4. Programma pārtrauc datu saglabāšanas procesu
    5. Tiek izvadīts kļūdas ziņojums:

        "Nepareizs datuma formāts. Izmantot formātu - GGGG-MM-DD"
    
    6. Izdevums nav saglabāts
    7. Lietotājs var izlabot kļūdu un mēģināt vēlreiz.
```

### Piemērs - izlasts vērtības lauks

> Lietotāja darbības

Lietotājs cenšas pievienot jaunu izdevumu, bet neaizpilda visus laukus

Soļi:
```
    1. Lietotājs atver izdevumu pievienošans veidlapu
    2. Lietotajs ievada sekojošus datus:
        Datums: 2026-03-03
        Summa: <tukšs lauks>
        Dokumenta Nr./ID: EKA020211
        Kategorija: Transports
        Apraksts: Auto apkope
        Maksājuma veids: Bankas karte
    3. Lietotājs nospiež "Pievienot" pogu
```

> Programmas darbības
```
    1. submit_expense() ielasa veidlapas datus
    2. Programma pārbauda vai nepieciešamie datu lauki ir aizpildīti
    3. Summas lauks ir tukšs
    4. Izdevumu pievienošana ir pārtraukta
    5. Tiek izvadīts kļūdas ziņojums:

        "Lūdzu aizpildiet obligātos datu laukus"
    
    7. Veidlapa paliek atvērta un lietotājs var aizpildīt trūkstošo lauku.
```

### Piemērs - tukšs izdevumu saraksts

> Lietotāja darbības

Lietotājs palaiž programmu un cenšas attēlot tukšu sarakstu

Soļi:
```
    1. Lietotājs atver programmu
    2. Lietotajs izveido jaunu sarakstu
```

> Programmas darbības
```
    1. load_list() tiek palaists
    2. Programma secina, ka nav datu, kurus atgriezt
    3. Tiek izvadīts ziņojums:
       
        "Izdevumu saraksts ir tukšs"
    
```

> Šis ir programmas izstrādes plāns