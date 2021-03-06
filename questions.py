# -*- coding: utf-8 -*-
questions = [
    {
        'text' : u'Vaše pohlavie? (z dôvodu výberu správneho kostýmu :)) ',
        'name' : 'gender',
        'options' : [
            {   'value' : 'm', 'label' : u'Muž', },
            {   'value' : 'f', 'label' : u'Žena',},
        ],
    },
    {
        'text' : u'Aký je Váš obľúbený drink?',
        'name' : 'q1',
        'options' : [
            { 'value' : 'a', 'label' : u'Miešaný koktail', },
            { 'value' : 'b', 'label' : u'Martini',         },
            { 'value' : 'c', 'label' : u'Kola Loka',       },
            { 'value' : 'd', 'label' : u'Rum',             },
            { 'value' : 'e', 'label' : u'Slivovica',       },
            { 'value' : 'f', 'label' : u'Šampanské',       },
            { 'value' : 'g', 'label' : u'Víno alebo pivo', },
            { 'value' : 'h', 'label' : u'Nepijem alkohol', },
            { 'value' : 'i', 'label' : u'Bloody Mary', },
        ],
    },
    {
        'text' : u'Zbraň, ktorú by ste najlepšie využili, ak by bolo treba?',
        'name' : 'q2',
        'options' : [
            { 'value' : 'a', 'label' : u'Svetelný meč alebo bumerang, svojho súpera nechcem zabiť, iba omráčiť', },
            { 'value' : 'b', 'label' : u'Vždy pripravený bič',         },
            { 'value' : 'c', 'label' : u'Vlastné päste',       },
            { 'value' : 'd', 'label' : u'Strelná zbraň ráže 9mm',             },
            { 'value' : 'e', 'label' : u'Mám výbornú mušku, stačila by mi puška s jedným nábojom',       },
            { 'value' : 'f', 'label' : u'Zvodný tanec',       },
            { 'value' : 'g', 'label' : u'Svojho súpera odzbrojím najlepšie slovami', },
            { 'value' : 'h', 'label' : u'Čarovný prútik',       },
            { 'value' : 'i', 'label' : u'Proste by som ho opil:)', },
        ],
    },
    {
        'text' : u'Keby ste sa narodili ako filmový hrdina, proti komu by ste najradšej bojovali?',
        'name' : 'q3',
        'options' : [
            { 'value' : 'a', 'label' : u'Proti robotom z budúcnosti', },
            { 'value' : 'b', 'label' : u'Proti teroristom a a zloduchom, ktorí chcú bombou zničiť celý svet',         },
            { 'value' : 'c', 'label' : u'Proti nadprirodzeným bytostiam',             },
            { 'value' : 'd', 'label' : u'Proti systému',       },
        ],
    }, 
    {
        'text' : u'Filmová postava, ktorej ste vždy najviac závideli?',
        'name' : 'q4',
        'options' : [
            { 'value' : 'a', 'label' : u'Bohuš z Dedičství', },
            { 'value' : 'b', 'label' : u'Superman',         },
            { 'value' : 'c', 'label' : u'Holly z Raňajok u Tiffanyho',       },
            { 'value' : 'd', 'label' : u'Lara Croft',             },
            { 'value' : 'e', 'label' : u'Homer Simpson',       },
            { 'value' : 'f', 'label' : u'Baby z Hriešneho tanca',       },
            { 'value' : 'g', 'label' : u'Alica v krajine zázrakov', },
        ],
    },
    {
        'text' : u'Ktorou myšlienkou sa v živote najviac riadite?',
        'name' : 'q5',
        'options' : [
            { 'value' : 'a', 'label' : u'Život je ako bonboniéra, nikdy nevieš, čo si vyberieš.', },
            { 'value' : 'b', 'label' : u'Hasta la vista, baby!',         },
            { 'value' : 'c', 'label' : u'Nikdy nebudem sedieť v kúte.',       },
            { 'value' : 'd', 'label' : u'Diamanty sú najlepší priatelia žien.',             },
            { 'value' : 'e', 'label' : u'Ešte som tu neskončil!',       },
            { 'value' : 'f', 'label' : u'S prehrou musíš počítať, keď chceš vyhrať.',       },
            { 'value' : 'g', 'label' : u'Nikdy alebo navždy!',       },
            { 'value' : 'h', 'label' : u'Smrť je pokludná a ľahká, život je ťažší.', },
        ],
    },
    {
        'text' : u'Najsympatickejšia dvojica, s ktorou by ste radi išli na dovolenku?',
        'name' : 'q6',
        'options' : [
            { 'value' : 'a', 'label' : u'Bonnie a Clyde', },
            { 'value' : 'b', 'label' : u'Sherlock a Watson',         },
            { 'value' : 'c', 'label' : u'Thelma a Louise',       },
            { 'value' : 'd', 'label' : u'Pán a pani Smithovi',             },
            { 'value' : 'e', 'label' : u'Mach a Šebestová',       },
            { 'value' : 'f', 'label' : u'Bella a Edward (Twillight)',       },
            { 'value' : 'g', 'label' : u'Carrie a pán "Božský"', },
        ],
    },
    {
        'text' : u'Keď dupnúť na pedál pri úniku pred svištiacimi guľkami, tak v aute?',
        'name' : 'q7',
        'options' : [
            { 'value' : 'a', 'label' : u'Ford Mustang', },
            { 'value' : 'b', 'label' : u'Aston Martin',         },
            { 'value' : 'c', 'label' : u'Chevrolet chevelle',       },
            { 'value' : 'd', 'label' : u'Batmobile',             },
            { 'value' : 'e', 'label' : u'Vojenský džíp',       },
            { 'value' : 'f', 'label' : u'Mini Cooper',       },
            { 'value' : 'g', 'label' : u'Mojim útočiskom by bol karaván',  },
            
            
        ],
    },
    {
        'text' : u'Česko-slovenský hrdina, ktorému vždy najviac držíte palce?',
        'name' : 'q8',
        'options' : [
            { 'value' : 'a', 'label' : u'Jánošík', },
            { 'value' : 'b', 'label' : u'Štepań Šafránek z Básnikov',         },
            { 'value' : 'c', 'label' : u'Dalibor Vrána z Vrchní prchní',       },
            { 'value' : 'd', 'label' : u'Voják Švejk',             },
            { 'value' : 'e', 'label' : u'Pani Škopková zo Slunce, seno,...',       },
            { 'value' : 'f', 'label' : u'Báthorička',       },
        ],
    },         
    {
        'text' : u'Predstavte si, že Váš život je film, aký žáner by to podľa Vás bol?',
        'name' : 'q9',
        'options' : [
            { 'value' : 'a', 'label' : u'Akčný film alebo napínavý thriller', },
            { 'value' : 'b', 'label' : u'Mysteriózny alebo tak trochu sci-fi',         },
            { 'value' : 'c', 'label' : u'Komédia alebo niečo veľmi vtipné',       },
            { 'value' : 'd', 'label' : u'Určite by to bol film plný dobrodružstiev',             },
            { 'value' : 'e', 'label' : u'Milujem hudbu, preto by to bol asi nejaký muzikál',       },
        ],
    },
     {
        'text' : u'Ktorá z nasledujúcich charakteristík je Vám najbližšia?',
        'name' : 'q10',
        'options' : [
            { 'value' : 'a', 'label' : u'Bežný človek, s bežnými problémami, úplne normálny', },
            { 'value' : 'b', 'label' : u'Tichý, introvertný intelektuál',         },
            { 'value' : 'c', 'label' : u'Extrovertný, priateľský a svojrázny',       },
            { 'value' : 'd', 'label' : u'Spoločenský, skôr umelecký typ',             },
            { 'value' : 'e', 'label' : u'Vtipný zorganizovaný, duchaplný a obľúbený',             },
            { 'value' : 'f', 'label' : u'Tak trochu podivín',       },
            { 'value' : 'g', 'label' : u'Dobrodružný, odvážny a nebojácny',       },
        ],
    },               
]