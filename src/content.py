# -*- coding: utf-8 -*-
"""
CONTENU DU SITE ABS DÉBOUCHAGE
Tous les textes sont ici. Après une modification : python3 build.py
"""

SITE_URL = "https://www.abs-debouchage.be"   # domaine final (utilisé pour Google)
PHONE_DISPLAY = "0484 72 47 24"
PHONE_TEL = "+32484724724"
WHATSAPP = "32484724724"
EMAIL = "contact@abs-debouchage.be"
VAT = "BE 0719.885.401"
VAT_RAW = "BE0719885401"
BRAND = "ABS Débouchage"

COMMUNES = [
    # (FR, NL, code postal)
    ("Anderlecht", "Anderlecht", "1070"),
    ("Auderghem", "Oudergem", "1160"),
    ("Berchem-Sainte-Agathe", "Sint-Agatha-Berchem", "1082"),
    ("Bruxelles-Ville", "Brussel-Stad", "1000"),
    ("Etterbeek", "Etterbeek", "1040"),
    ("Evere", "Evere", "1140"),
    ("Forest", "Vorst", "1190"),
    ("Ganshoren", "Ganshoren", "1083"),
    ("Ixelles", "Elsene", "1050"),
    ("Jette", "Jette", "1090"),
    ("Koekelberg", "Koekelberg", "1081"),
    ("Molenbeek-Saint-Jean", "Sint-Jans-Molenbeek", "1080"),
    ("Saint-Gilles", "Sint-Gillis", "1060"),
    ("Saint-Josse-ten-Noode", "Sint-Joost-ten-Node", "1210"),
    ("Schaerbeek", "Schaarbeek", "1030"),
    ("Uccle", "Ukkel", "1180"),
    ("Watermael-Boitsfort", "Watermaal-Bosvoorde", "1170"),
    ("Woluwe-Saint-Lambert", "Sint-Lambrechts-Woluwe", "1200"),
    ("Woluwe-Saint-Pierre", "Sint-Pieters-Woluwe", "1150"),
]
PERIPHERIE = [("Zaventem", "Zaventem"), ("Vilvorde", "Vilvoorde"), ("Dilbeek", "Dilbeek"),
              ("Drogenbos", "Drogenbos"), ("Kraainem", "Kraainem"), ("Wezembeek-Oppem", "Wezembeek-Oppem"),
              ("Machelen", "Machelen"), ("Grimbergen", "Grimbergen")]

# --------------------------------------------------------------------------
# SERVICES — même adresse (slug) que l'ancien site pour garder le référencement
# --------------------------------------------------------------------------
SERVICES = [
 {
  "id": "wc", "icon": "toilet", "price": 85, "slug": {"fr": "debouchage-wc", "nl": "ontstopping-wc"},
  "fr": {
   "name": "Débouchage WC",
   "card": "Cuvette qui déborde ou se vide mal : on débouche sans abîmer la faïence.",
   "title": "Débouchage WC Bruxelles 24h/24 – dès 85 € | ABS Débouchage",
   "desc": "WC bouché à Bruxelles ? Technicien sur place en 30 min, 24h/24. Débouchage propre au furet électrique, prix annoncé avant travaux, dès 85 €. ☎ 0484 72 47 24",
   "h1": "Débouchage WC à Bruxelles, en urgence 24h/24",
   "intro": "Des toilettes bouchées, c'est l'urgence la plus fréquente… et la plus stressante. Nos techniciens interviennent dans toutes les communes de Bruxelles, en moyenne en 30 minutes, avec un furet électrique professionnel qui débouche la cuvette et le tuyau d'évacuation sans rayer la porcelaine.",
   "signs": ["L'eau monte jusqu'au bord de la cuvette après la chasse", "La cuvette se vide très lentement ou fait des bruits de glouglou", "Une odeur d'égout remonte dans la salle de bain", "La ventouse ne donne plus aucun résultat"],
   "causes": ["Trop de papier toilette en une fois", "Lingettes, cotons-tiges ou serviettes hygiéniques jetés dans le WC", "Objet tombé dans la cuvette (jouet, brosse, déodorant)", "Dépôts de calcaire qui réduisent le passage du tuyau"],
   "method": [["Diagnostic", "On identifie où se trouve le bouchon : cuvette, coude ou colonne d'évacuation."], ["Débouchage", "Furet électrique rotatif ou pompe haute pression selon le cas, sans démonter le WC."], ["Test", "Plusieurs chasses d'eau pour vérifier un écoulement parfait."], ["Nettoyage", "La zone est nettoyée et désinfectée avant notre départ."]],
   "tip": "En attendant le technicien : ne tirez plus la chasse, fermez le robinet d'arrivée d'eau derrière le WC et évitez les produits chimiques, qui abîment les joints et sont dangereux pour nos techniciens.",
   "faq": [["Combien coûte un débouchage de WC à Bruxelles ?", "Un débouchage de WC standard démarre à 85 €. Le prix exact est annoncé par téléphone ou WhatsApp avant le départ du technicien, et c'est ce prix qui figure sur la facture."], ["Faut-il démonter les toilettes ?", "Dans la grande majorité des cas, non. Le furet électrique passe directement par la cuvette jusqu'au bouchon."], ["Vous intervenez la nuit pour des WC bouchés ?", "Oui, 24h/24 et 7j/7, week-ends et jours fériés compris, car un WC bouché ne peut pas attendre le lendemain."]]
  },
  "nl": {
   "name": "Ontstopping wc",
   "card": "Pot die overloopt of traag leegloopt: we ontstoppen zonder de porselein te beschadigen.",
   "title": "Ontstopping wc Brussel 24/7 – vanaf 85 € | ABS Débouchage",
   "desc": "Wc verstopt in Brussel? Technieker binnen 30 min ter plaatse, 24/7. Propere ontstopping met elektrische veer, prijs vooraf gekend, vanaf 85 €. ☎ 0484 72 47 24",
   "h1": "Wc ontstoppen in Brussel, dringend en 24/7",
   "intro": "Een verstopt toilet is de meest voorkomende noodsituatie… en de meest stresserende. Onze techniekers komen in alle Brusselse gemeenten, gemiddeld binnen 30 minuten, met een professionele elektrische veer die de pot en de afvoer ontstopt zonder het porselein te krassen.",
   "signs": ["Het water komt na het doorspoelen tot aan de rand van de pot", "De pot loopt heel traag leeg of maakt borrelende geluiden", "Er komt een rioolgeur in de badkamer", "De ontstopper (zuignap) helpt niet meer"],
   "causes": ["Te veel toiletpapier in één keer", "Doekjes, wattenstaafjes of maandverband in het toilet", "Voorwerp in de pot gevallen (speelgoed, borstel, deodorant)", "Kalkaanslag die de afvoer vernauwt"],
   "method": [["Diagnose", "We zoeken waar de verstopping zit: pot, bocht of afvoerkolom."], ["Ontstopping", "Elektrische veer of hogedrukpomp, afhankelijk van de situatie, zonder de wc te demonteren."], ["Test", "Meermaals doorspoelen om een perfecte afvoer te controleren."], ["Opkuis", "De werkzone wordt gereinigd en ontsmet voor we vertrekken."]],
   "tip": "In afwachting van de technieker: spoel niet meer door, sluit de waterkraan achter de wc en gebruik geen chemische producten. Die beschadigen de dichtingen en zijn gevaarlijk voor onze techniekers.",
   "faq": [["Hoeveel kost een wc-ontstopping in Brussel?", "Een standaard wc-ontstopping start vanaf 85 €. De exacte prijs krijg je telefonisch of via WhatsApp vóór de technieker vertrekt, en die prijs staat op de factuur."], ["Moet het toilet gedemonteerd worden?", "In de meeste gevallen niet. De elektrische veer gaat rechtstreeks via de pot tot aan de verstopping."], ["Komen jullie ook 's nachts voor een verstopte wc?", "Ja, 24/7, ook in het weekend en op feestdagen. Een verstopte wc kan niet wachten tot morgen."]]
  }
 },
 {
  "id": "sanibroyeur", "icon": "sanibroyeur", "price": None, "slug": {"fr": "debouchage-toilette", "nl": "ontstopping-sanibroyeur"},
  "fr": {
   "name": "Sanibroyeur & WC suspendu",
   "card": "Broyeur bloqué ou WC suspendu Geberit : intervention délicate, sans casse.",
   "title": "Débouchage sanibroyeur Bruxelles 24h/24 | ABS Débouchage",
   "desc": "Sanibroyeur bloqué ou WC suspendu bouché à Bruxelles ? Intervention 24h/24 en 30 min, sans abîmer le moteur ni le bâti. Devis gratuit : 0484 72 47 24",
   "h1": "Débouchage de sanibroyeur et WC suspendu à Bruxelles",
   "intro": "Un sanibroyeur ou un WC suspendu ne se débouche pas comme des toilettes classiques. Le moteur, les lames et les membranes sont fragiles, et le bâti est caché dans le mur. Nos techniciens connaissent ces installations et les remettent en marche sans dégât.",
   "signs": ["Le moteur du broyeur tourne dans le vide ou ne s'arrête plus", "Le broyeur fait un bruit anormal ou ne démarre pas", "De l'eau sale remonte dans la douche ou le lavabo raccordés", "Le WC suspendu se vide mal malgré la ventouse"],
   "causes": ["Lingettes ou papier absorbant coincés dans les lames", "Calcaire accumulé dans la cuve du broyeur", "Membrane ou clapet anti-retour encrassé", "Bouchon dans la petite conduite d'évacuation"],
   "method": [["Mise en sécurité", "Coupure de l'alimentation électrique du broyeur avant toute intervention."], ["Ouverture", "Accès à la cuve et retrait de ce qui bloque les lames."], ["Détartrage", "Nettoyage de la cuve, du clapet et de la conduite d'évacuation."], ["Remise en route", "Test complet du cycle de pompage et de l'étanchéité."]],
   "tip": "En attendant : débranchez le sanibroyeur, n'utilisez plus les appareils qui y sont raccordés (douche, lavabo) et ne versez jamais de déboucheur chimique, il détruit les joints et la membrane.",
   "faq": [["Un sanibroyeur bouché peut-il être réparé sans le remplacer ?", "Oui, dans la plupart des cas un nettoyage complet et un détartrage suffisent à le remettre en marche."], ["Intervenez-vous sur les WC suspendus Geberit ?", "Oui, nous débouchons les WC suspendus sans casser le mur ni démonter le bâti."], ["Combien coûte l'intervention ?", "Le prix dépend de la panne. Il vous est annoncé gratuitement avant l'intervention, par téléphone ou WhatsApp."]]
  },
  "nl": {
   "name": "Sanibroyeur & hangtoilet",
   "card": "Geblokkeerde sanibroyeur of Geberit-hangtoilet: delicate interventie, zonder schade.",
   "title": "Ontstopping sanibroyeur & hangtoilet Brussel 24/7 | ABS Débouchage",
   "desc": "Sanibroyeur geblokkeerd of hangtoilet verstopt in Brussel? Interventie 24/7 binnen 30 min, zonder schade aan motor of inbouwreservoir. Gratis offerte: 0484 72 47 24",
   "h1": "Sanibroyeur en hangtoilet ontstoppen in Brussel",
   "intro": "Een sanibroyeur of hangtoilet ontstop je niet zoals een gewoon toilet. De motor, messen en membranen zijn kwetsbaar en het reservoir zit in de muur. Onze techniekers kennen deze installaties en zetten ze weer in werking zonder schade.",
   "signs": ["De motor van de broyeur draait leeg of stopt niet meer", "De broyeur maakt een abnormaal geluid of start niet", "Vuil water komt omhoog in de aangesloten douche of lavabo", "Het hangtoilet loopt slecht weg, ook met een zuignap"],
   "causes": ["Doekjes of keukenpapier vast in de messen", "Kalk in het reservoir van de broyeur", "Vuile membraan of terugslagklep", "Verstopping in de dunne afvoerleiding"],
   "method": [["Veiligheid", "Stroom van de broyeur uitschakelen voor elke interventie."], ["Openen", "Toegang tot het reservoir en verwijderen van wat de messen blokkeert."], ["Ontkalken", "Reiniging van reservoir, klep en afvoerleiding."], ["Herstart", "Volledige test van de pompcyclus en de dichtheid."]],
   "tip": "In afwachting: trek de stekker van de sanibroyeur uit, gebruik de aangesloten toestellen (douche, lavabo) niet meer en giet nooit chemische ontstopper. Die vernielt de dichtingen en het membraan.",
   "faq": [["Kan een verstopte sanibroyeur hersteld worden zonder hem te vervangen?", "Ja, meestal volstaat een grondige reiniging en ontkalking om hem weer te laten werken."], ["Werken jullie aan Geberit-hangtoiletten?", "Ja, we ontstoppen hangtoiletten zonder de muur open te breken of het reservoir te demonteren."], ["Hoeveel kost de interventie?", "De prijs hangt af van het probleem. Je krijgt hem gratis vooraf, telefonisch of via WhatsApp."]]
  }
 },
 {
  "id": "evier", "icon": "sink", "price": 80, "slug": {"fr": "debouchage-evier", "nl": "ontstopping-gootsteen"},
  "fr": {
   "name": "Débouchage évier",
   "card": "Graisse et restes de repas : dégraissage complet du siphon et du tuyau.",
   "title": "Débouchage évier Bruxelles 24h/24 – dès 80 € | ABS Débouchage",
   "desc": "Évier de cuisine bouché à Bruxelles ? Débouchage et dégraissage haute pression en 30 min, 24h/24. Prix annoncé avant travaux, dès 80 €. ☎ 0484 72 47 24",
   "h1": "Débouchage d'évier de cuisine à Bruxelles",
   "intro": "L'évier de cuisine reçoit chaque jour de la graisse chaude, qui fige dans les tuyaux et retient les restes alimentaires. Résultat : l'eau stagne et les odeurs s'installent. Nous débouchons et dégraissons le siphon et la canalisation pour retrouver un écoulement comme neuf.",
   "signs": ["L'eau stagne dans les bacs de l'évier", "Odeur de graisse rance ou d'égout", "Gargouillements quand le lave-vaisselle se vide", "L'eau remonte dans le second bac"],
   "causes": ["Graisse de cuisson versée dans l'évier", "Marc de café, riz, pâtes et restes alimentaires", "Siphon encrassé jamais nettoyé", "Lave-vaisselle raccordé sur une évacuation trop étroite"],
   "method": [["Démontage du siphon", "Nettoyage complet du siphon et de la bonde."], ["Furet électrique", "Passage du furet dans la canalisation pour casser le bouchon de graisse."], ["Dégraissage", "Rinçage haute pression pour nettoyer les parois du tuyau."], ["Contrôle", "Test à plein débit, évier et lave-vaisselle."]],
   "tip": "En attendant : n'utilisez plus le lave-vaisselle et ne versez pas d'eau bouillante si le tuyau est en PVC, elle peut le déformer.",
   "faq": [["Combien coûte un débouchage d'évier ?", "À partir de 80 €. Le prix exact vous est confirmé avant l'intervention."], ["Mon évier se rebouche souvent, que faire ?", "C'est souvent un dépôt de graisse en profondeur. Un hydrocurage ou une inspection caméra permet de traiter la cause."], ["Intervenez-vous dans les restaurants ?", "Oui, nous intervenons aussi pour les cuisines professionnelles, 24h/24."]]
  },
  "nl": {
   "name": "Ontstopping gootsteen",
   "card": "Vet en etensresten: volledige reiniging van sifon en afvoer.",
   "title": "Ontstopping gootsteen Brussel 24/7 – vanaf 80 € | ABS Débouchage",
   "desc": "Gootsteen verstopt in Brussel? Ontstopping en hogedrukreiniging binnen 30 min, 24/7. Prijs vooraf gekend, vanaf 80 €. ☎ 0484 72 47 24",
   "h1": "Gootsteen ontstoppen in Brussel",
   "intro": "De keukengootsteen krijgt elke dag heet vet te verwerken. Dat stolt in de leidingen en houdt etensresten vast. Gevolg: het water blijft staan en het begint te stinken. Wij ontstoppen en ontvetten de sifon en de afvoer zodat alles weer vlot wegloopt.",
   "signs": ["Het water blijft in de gootsteen staan", "Geur van ranzig vet of riool", "Borrelende geluiden als de vaatwasser leegloopt", "Water komt omhoog in de tweede kuip"],
   "causes": ["Bakvet in de gootsteen gegoten", "Koffiedik, rijst, pasta en etensresten", "Vuile sifon die nooit gereinigd werd", "Vaatwasser aangesloten op een te smalle afvoer"],
   "method": [["Sifon demonteren", "Volledige reiniging van sifon en afvoerplug."], ["Elektrische veer", "De veer breekt de vetprop in de leiding."], ["Ontvetten", "Spoelen onder hoge druk om de wanden van de leiding te reinigen."], ["Controle", "Test op vol debiet, gootsteen en vaatwasser."]],
   "tip": "In afwachting: gebruik de vaatwasser niet meer en giet geen kokend water als de leiding uit pvc is, die kan vervormen.",
   "faq": [["Hoeveel kost een gootsteenontstopping?", "Vanaf 80 €. De exacte prijs wordt vooraf bevestigd."], ["Mijn gootsteen raakt vaak verstopt, wat nu?", "Meestal zit er diep in de leiding vet. Hogedrukreiniging of een camera-inspectie pakt de oorzaak aan."], ["Komen jullie ook naar restaurants?", "Ja, ook voor professionele keukens, 24/7."]]
  }
 },
 {
  "id": "lavabo", "icon": "basin", "price": 80, "slug": {"fr": "debouchage-lavabo", "nl": "ontstopping-lavabo"},
  "fr": {
   "name": "Débouchage lavabo",
   "card": "Cheveux, savon, dentifrice : siphon et vidage nettoyés proprement.",
   "title": "Débouchage lavabo Bruxelles 24h/24 – dès 80 € | ABS Débouchage",
   "desc": "Lavabo ou vasque bouché à Bruxelles ? Intervention rapide 24h/24, siphon et évacuation nettoyés sans abîmer vos meubles. Dès 80 €. ☎ 0484 72 47 24",
   "h1": "Débouchage de lavabo et vasque à Bruxelles",
   "intro": "Cheveux, savon et dentifrice forment petit à petit un bouchon dans le siphon du lavabo. Nos techniciens démontent et nettoient le siphon, la bonde et la canalisation, avec soin pour vos meubles de salle de bain.",
   "signs": ["L'eau stagne après le brossage de dents", "Bonde clic-clac bloquée", "Odeurs dans la salle de bain", "Écoulement lent qui s'aggrave"],
   "causes": ["Cheveux accumulés dans la bonde", "Savon et dentifrice qui collent aux parois", "Calcaire dans le siphon", "Petit objet tombé (bouchon, bijou)"],
   "method": [["Bonde", "Démontage et nettoyage de la bonde et du mécanisme clic-clac."], ["Siphon", "Démontage du siphon, nettoyage, remontage étanche."], ["Canalisation", "Passage du furet si le bouchon est plus loin."], ["Test", "Vérification de l'écoulement et de l'étanchéité."]],
   "tip": "En attendant : retirez la bonde clic-clac si vous pouvez et enlevez les cheveux visibles. Évitez la soude caustique.",
   "faq": [["Combien coûte un débouchage de lavabo ?", "À partir de 80 €, prix confirmé avant l'intervention."], ["Pouvez-vous récupérer un bijou tombé dans le lavabo ?", "Souvent oui : il reste généralement coincé dans le siphon. Arrêtez d'utiliser le lavabo et appelez-nous."], ["Vous démontez le meuble ?", "Rarement. Le siphon est accessible sous la vasque dans la plupart des cas."]]
  },
  "nl": {
   "name": "Ontstopping lavabo",
   "card": "Haren, zeep, tandpasta: sifon en afvoer netjes gereinigd.",
   "title": "Ontstopping lavabo Brussel 24/7 – vanaf 80 € | ABS Débouchage",
   "desc": "Lavabo of wastafel verstopt in Brussel? Snelle interventie 24/7, sifon en afvoer gereinigd zonder schade aan je meubels. Vanaf 80 €. ☎ 0484 72 47 24",
   "h1": "Lavabo en wastafel ontstoppen in Brussel",
   "intro": "Haren, zeep en tandpasta vormen beetje bij beetje een prop in de sifon van de lavabo. Onze techniekers demonteren en reinigen sifon, afvoerplug en leiding, met respect voor je badkamermeubel.",
   "signs": ["Het water blijft staan na het tandenpoetsen", "Klik-klakplug geblokkeerd", "Geur in de badkamer", "Trage afvoer die erger wordt"],
   "causes": ["Haren in de afvoerplug", "Zeep en tandpasta op de wanden", "Kalk in de sifon", "Klein voorwerp gevallen (dop, juweel)"],
   "method": [["Afvoerplug", "Demonteren en reinigen van de plug en het klik-klakmechanisme."], ["Sifon", "Sifon demonteren, reinigen en waterdicht terugplaatsen."], ["Leiding", "Elektrische veer als de verstopping verder zit."], ["Test", "Controle van afvoer en dichtheid."]],
   "tip": "In afwachting: verwijder de klik-klakplug als dat lukt en haal zichtbare haren weg. Vermijd bijtende soda.",
   "faq": [["Hoeveel kost een lavabo-ontstopping?", "Vanaf 80 €, prijs bevestigd vóór de interventie."], ["Kunnen jullie een juweel uit de lavabo halen?", "Vaak wel: het blijft meestal in de sifon steken. Gebruik de lavabo niet meer en bel ons."], ["Wordt het meubel gedemonteerd?", "Zelden. De sifon is meestal bereikbaar onder de wastafel."]]
  }
 },
 {
  "id": "douche", "icon": "shower", "price": 85, "slug": {"fr": "debouchage-douche", "nl": "ontstopping-douche"},
  "fr": {
   "name": "Débouchage douche",
   "card": "Bac ou douche à l'italienne qui déborde : débouché sans casser le carrelage.",
   "title": "Débouchage douche Bruxelles 24h/24 – dès 85 € | ABS Débouchage",
   "desc": "Douche bouchée à Bruxelles ? Bac, douche à l'italienne ou caniveau : débouchage en 30 min sans casser le carrelage, 24h/24. Dès 85 €. ☎ 0484 72 47 24",
   "h1": "Débouchage de douche et douche à l'italienne à Bruxelles",
   "intro": "Une douche qui ne s'évacue plus inonde vite la salle de bain. Bondes extra-plates, caniveaux de douche à l'italienne, siphons de sol : nous connaissons tous les systèmes et débouchons sans casser le carrelage ni les joints.",
   "signs": ["L'eau monte au-dessus du receveur pendant la douche", "Écoulement très lent", "Odeur d'égout qui remonte par la bonde", "L'eau d'un autre appareil ressort dans la douche"],
   "causes": ["Cheveux et poils mêlés au savon", "Bonde extra-plate trop étroite", "Calcaire dans le siphon", "Pente insuffisante d'une douche à l'italienne"],
   "method": [["Accès", "Ouverture de la bonde ou du caniveau, sans toucher au carrelage."], ["Extraction", "Retrait des cheveux et dépôts dans le siphon."], ["Furet", "Débouchage de la canalisation jusqu'à la colonne."], ["Test", "Douche à plein débit pendant plusieurs minutes."]],
   "tip": "En attendant : n'utilisez plus la douche, ni le lave-linge s'il est raccordé sur la même évacuation.",
   "faq": [["Combien coûte un débouchage de douche ?", "À partir de 85 €, prix confirmé avant l'intervention."], ["Ma douche à l'italienne n'a pas de trappe, vous pouvez la déboucher ?", "Oui, nous passons par le caniveau ou la grille, sans casser le carrelage."], ["Pourquoi ma douche se rebouche-t-elle ?", "Souvent à cause de la pente ou d'un dépôt plus loin dans la canalisation. Une inspection caméra permet de le vérifier."]]
  },
  "nl": {
   "name": "Ontstopping douche",
   "card": "Overlopende douchebak of inloopdouche: ontstopt zonder tegels te breken.",
   "title": "Ontstopping douche Brussel 24/7 – vanaf 85 € | ABS Débouchage",
   "desc": "Douche verstopt in Brussel? Douchebak, inloopdouche of douchegoot: ontstopping binnen 30 min zonder tegels te breken, 24/7. Vanaf 85 €. ☎ 0484 72 47 24",
   "h1": "Douche en inloopdouche ontstoppen in Brussel",
   "intro": "Een douche die niet meer afloopt, zet de badkamer snel onder water. Extra platte afvoerputjes, douchegoten, vloerputjes: we kennen alle systemen en ontstoppen zonder tegels of voegen te beschadigen.",
   "signs": ["Het water komt boven de douchebak tijdens het douchen", "Zeer trage afvoer", "Rioolgeur uit het afvoerputje", "Water van een ander toestel komt omhoog in de douche"],
   "causes": ["Haren vermengd met zeep", "Te smal extra plat putje", "Kalk in de sifon", "Onvoldoende helling bij een inloopdouche"],
   "method": [["Toegang", "Openen van het putje of de douchegoot, zonder aan de tegels te komen."], ["Verwijderen", "Haren en afzettingen uit de sifon halen."], ["Veer", "Ontstoppen van de leiding tot aan de kolom."], ["Test", "Enkele minuten douchen op vol debiet."]],
   "tip": "In afwachting: gebruik de douche niet meer, en ook de wasmachine niet als die op dezelfde afvoer zit.",
   "faq": [["Hoeveel kost een douche-ontstopping?", "Vanaf 85 €, prijs bevestigd vóór de interventie."], ["Mijn inloopdouche heeft geen luik, kunnen jullie ze ontstoppen?", "Ja, we werken via de douchegoot of het rooster, zonder tegels te breken."], ["Waarom raakt mijn douche steeds opnieuw verstopt?", "Vaak door de helling of een afzetting verder in de leiding. Een camera-inspectie kan dat nagaan."]]
  }
 },
 {
  "id": "baignoire", "icon": "bath", "price": None, "slug": {"fr": "debouchage-baignoire", "nl": "ontstopping-bad"},
  "fr": {
   "name": "Débouchage baignoire",
   "card": "Eau stagnante vidée, évacuation dégagée, sans démonter le tablier.",
   "title": "Débouchage baignoire Bruxelles 24h/24 | ABS Débouchage",
   "desc": "Baignoire bouchée à Bruxelles ? Évacuation dégagée en 30 min, sans démonter le tablier carrelé, 24h/24. Devis gratuit : 0484 72 47 24",
   "h1": "Débouchage de baignoire à Bruxelles",
   "intro": "Une baignoire pleine d'eau qui ne se vide pas, ce sont des dizaines de litres bloqués dans la salle de bain. Nous dégageons l'évacuation par la bonde et le trop-plein, sans démonter le tablier carrelé.",
   "signs": ["La baignoire met des heures à se vider", "L'eau du lave-linge remonte dans la baignoire", "Bruits de glouglou dans la bonde", "Mauvaises odeurs"],
   "causes": ["Cheveux et savon dans le siphon", "Bonde automatique encrassée", "Dépôts de calcaire", "Bouchon dans la canalisation commune avec le lavabo"],
   "method": [["Vidange", "Évacuation de l'eau stagnante si nécessaire."], ["Bonde et trop-plein", "Nettoyage du mécanisme et du siphon."], ["Hydro-propulsion", "Dégagement de la canalisation par jet d'eau sous pression."], ["Test", "Remplissage et vidange complète de la baignoire."]],
   "tip": "En attendant : n'utilisez plus le lave-linge si son évacuation rejoint celle de la baignoire.",
   "faq": [["Faut-il casser le tablier de la baignoire ?", "Non, nous intervenons par la bonde et le trop-plein dans la très grande majorité des cas."], ["Combien coûte l'intervention ?", "Le prix vous est annoncé gratuitement avant le déplacement."], ["Intervenez-vous le week-end ?", "Oui, 24h/24 et 7j/7."]]
  },
  "nl": {
   "name": "Ontstopping bad",
   "card": "Stilstaand water weg en afvoer vrij, zonder het badpaneel te demonteren.",
   "title": "Ontstopping bad Brussel 24/7 | ABS Débouchage",
   "desc": "Bad verstopt in Brussel? Afvoer vrij binnen 30 min, zonder het betegelde badpaneel te demonteren, 24/7. Gratis offerte: 0484 72 47 24",
   "h1": "Bad ontstoppen in Brussel",
   "intro": "Een vol bad dat niet leegloopt, betekent tientallen liters water die vastzitten in de badkamer. Wij maken de afvoer vrij via de afvoerplug en de overloop, zonder het betegelde badpaneel te demonteren.",
   "signs": ["Het bad loopt urenlang niet leeg", "Water van de wasmachine komt omhoog in het bad", "Borrelende geluiden in de afvoer", "Slechte geuren"],
   "causes": ["Haren en zeep in de sifon", "Vuile automatische afvoerplug", "Kalkafzetting", "Verstopping in de gemeenschappelijke leiding met de lavabo"],
   "method": [["Leegmaken", "Stilstaand water wegpompen indien nodig."], ["Plug en overloop", "Reinigen van het mechanisme en de sifon."], ["Hogedruk", "Leiding vrijmaken met een waterstraal onder druk."], ["Test", "Bad volledig vullen en laten leeglopen."]],
   "tip": "In afwachting: gebruik de wasmachine niet meer als die op dezelfde afvoer als het bad zit.",
   "faq": [["Moet het badpaneel afgebroken worden?", "Nee, in bijna alle gevallen werken we via de afvoerplug en de overloop."], ["Hoeveel kost de interventie?", "Je krijgt de prijs gratis vóór we vertrekken."], ["Komen jullie in het weekend?", "Ja, 24/7."]]
  }
 },
 {
  "id": "cuisine", "icon": "pipes", "price": None, "slug": {"fr": "debouchage-cuisine", "nl": "ontstopping-keukenafvoer"},
  "fr": {
   "name": "Canalisations & colonnes",
   "card": "Évier et lave-vaisselle qui refoulent : curage complet des conduites.",
   "title": "Débouchage canalisation Bruxelles 24h/24 | ABS Débouchage",
   "desc": "Canalisation ou colonne bouchée à Bruxelles ? Curage haute pression des conduites de cuisine et colonnes d'immeuble, 24h/24 en 30 min. ☎ 0484 72 47 24",
   "h1": "Débouchage de canalisations et colonnes à Bruxelles",
   "intro": "Quand plusieurs appareils refoulent en même temps, le bouchon n'est plus dans un siphon mais dans la canalisation principale ou la colonne de l'immeuble. Nous curons les conduites sur toute leur longueur avec du matériel haute pression, pour les particuliers comme pour les syndics.",
   "signs": ["L'évier et le lave-vaisselle refoulent en même temps", "L'eau remonte chez le voisin du dessous", "Odeur tenace de graisse dans tout le logement", "Plusieurs appareils s'écoulent mal"],
   "causes": ["Accumulation de graisse sur des années", "Colonne d'immeuble encrassée", "Pente insuffisante ou coude mal placé", "Tartre dans les anciennes canalisations en fonte"],
   "method": [["Localisation", "On repère la section bouchée, si besoin avec la caméra."], ["Curage", "Hydrocurage haute pression sur toute la longueur de la conduite."], ["Rinçage", "Évacuation des résidus de graisse et de tartre."], ["Contrôle", "Test de tous les appareils raccordés."]],
   "tip": "En attendant : prévenez vos voisins si vous êtes en immeuble, et limitez l'usage de l'eau dans tout le logement.",
   "faq": [["Travaillez-vous pour les syndics d'immeubles ?", "Oui, nous intervenons sur les colonnes communes et fournissons un rapport pour le syndic."], ["Combien coûte un curage de canalisation ?", "Le prix dépend de la longueur et de l'accès. Il est annoncé gratuitement avant l'intervention."], ["L'hydrocurage abîme-t-il les vieux tuyaux ?", "Non, la pression est adaptée au matériau : PVC, fonte ou grès."]]
  },
  "nl": {
   "name": "Leidingen & kolommen",
   "card": "Gootsteen en vaatwasser die terugslaan: volledige reiniging van de leidingen.",
   "title": "Ontstopping leidingen Brussel 24/7 | ABS Débouchage",
   "desc": "Leiding of afvoerkolom verstopt in Brussel? Hogedrukreiniging van keukenleidingen en gebouwkolommen, 24/7 binnen 30 min. ☎ 0484 72 47 24",
   "h1": "Leidingen en afvoerkolommen ontstoppen in Brussel",
   "intro": "Als meerdere toestellen tegelijk terugslaan, zit de verstopping niet meer in een sifon maar in de hoofdleiding of de kolom van het gebouw. We reinigen de leidingen over hun volledige lengte met hogedrukmateriaal, voor particulieren en syndici.",
   "signs": ["Gootsteen en vaatwasser slaan tegelijk terug", "Water komt omhoog bij de onderburen", "Hardnekkige vetgeur in de hele woning", "Meerdere toestellen lopen slecht af"],
   "causes": ["Jarenlange vetophoping", "Vervuilde gebouwkolom", "Onvoldoende helling of slecht geplaatste bocht", "Kalk in oude gietijzeren leidingen"],
   "method": [["Lokaliseren", "We zoeken het verstopte stuk, desnoods met de camera."], ["Reinigen", "Hogedrukreiniging over de volledige leiding."], ["Spoelen", "Afvoer van vet- en kalkresten."], ["Controle", "Test van alle aangesloten toestellen."]],
   "tip": "In afwachting: verwittig je buren als je in een appartement woont en beperk het waterverbruik in de hele woning.",
   "faq": [["Werken jullie voor syndici?", "Ja, we werken aan gemeenschappelijke kolommen en leveren een verslag voor de syndicus."], ["Hoeveel kost een leidingreiniging?", "De prijs hangt af van de lengte en de toegang. Je krijgt hem gratis vooraf."], ["Beschadigt hogedruk oude leidingen?", "Nee, de druk wordt aangepast aan het materiaal: pvc, gietijzer of gres."]]
  }
 },
 {
  "id": "egout", "icon": "manhole", "price": None, "slug": {"fr": "debouchage-egout", "nl": "ontstopping-riool"},
  "fr": {
   "name": "Débouchage égout",
   "card": "Refoulement en cave, chambre de visite pleine : hydrocurage 400 bars.",
   "title": "Débouchage égout Bruxelles 24h/24 – 400 bars | ABS Débouchage",
   "desc": "Égout bouché ou refoulement en cave à Bruxelles ? Camion hydrocureur 400 bars, intervention 24h/24 en 30 min, rapport pour l'assurance. ☎ 0484 72 47 24",
   "h1": "Débouchage d'égout et de chambre de visite à Bruxelles",
   "intro": "Un égout principal bouché menace toute la maison : refoulement d'eaux usées dans la cave, odeurs, risques sanitaires. Nos camions hydrocureurs 400 bars dégagent racines, calcaire et bouchons massifs, et nous fournissons un rapport pour votre assurance.",
   "signs": ["Eaux usées qui remontent dans la cave ou le sous-sol", "Chambre de visite (regard) pleine ou qui déborde", "Tous les appareils de la maison s'écoulent mal", "Refoulements lors de fortes pluies"],
   "causes": ["Racines d'arbres entrées dans les joints", "Affaissement ou casse de la conduite", "Accumulation de graisse et de lingettes", "Siphon disconnecteur bouché"],
   "method": [["Ouverture du regard", "Accès à la chambre de visite et au siphon disconnecteur."], ["Hydrocurage 400 bars", "Jet haute pression qui coupe les racines et dissout les dépôts."], ["Aspiration", "Pompage des boues et des eaux stagnantes."], ["Inspection", "Contrôle caméra si nécessaire, avec rapport."]],
   "tip": "En attendant : n'utilisez plus d'eau dans la maison (WC, douche, machines) et éloignez enfants et animaux de la cave.",
   "faq": [["L'assurance rembourse-t-elle un débouchage d'égout ?", "Souvent, en cas de dégât des eaux. Nous fournissons une facture avec n° TVA et un rapport technique."], ["Qu'est-ce qu'une chambre de visite ?", "C'est le regard d'accès à l'égout, souvent dans la cave ou le jardin, qui permet de déboucher la conduite principale."], ["Combien coûte un débouchage d'égout ?", "Le prix dépend de l'accès et de la gravité. Il est annoncé gratuitement avant l'intervention."]]
  },
  "nl": {
   "name": "Ontstopping riool",
   "card": "Terugslag in de kelder, volle inspectieput: hogedrukreiniging 400 bar.",
   "title": "Ontstopping riool Brussel 24/7 – hogedruk 400 bar | ABS Débouchage",
   "desc": "Riool verstopt of terugslag in de kelder in Brussel? Hogedrukwagen 400 bar, interventie 24/7 binnen 30 min, verslag voor de verzekering. ☎ 0484 72 47 24",
   "h1": "Riool en inspectieput ontstoppen in Brussel",
   "intro": "Een verstopte hoofdriolering bedreigt het hele huis: afvalwater in de kelder, geuren, gezondheidsrisico's. Onze hogedrukwagens van 400 bar verwijderen wortels, kalk en zware verstoppingen, en we leveren een verslag voor je verzekering.",
   "signs": ["Afvalwater komt omhoog in de kelder", "Inspectieput vol of overlopend", "Alle toestellen in huis lopen slecht af", "Terugslag bij hevige regen"],
   "causes": ["Boomwortels in de voegen", "Verzakte of gebroken leiding", "Ophoping van vet en doekjes", "Verstopte reukafsnijder (sifonput)"],
   "method": [["Put openen", "Toegang tot de inspectieput en de reukafsnijder."], ["Hogedruk 400 bar", "Straal onder hoge druk die wortels snijdt en afzettingen oplost."], ["Afzuigen", "Wegpompen van slib en stilstaand water."], ["Inspectie", "Cameracontrole indien nodig, met verslag."]],
   "tip": "In afwachting: gebruik geen water meer in huis (wc, douche, machines) en hou kinderen en dieren uit de kelder.",
   "faq": [["Betaalt de verzekering een rioolontstopping terug?", "Vaak wel bij waterschade. Je krijgt een factuur met btw-nummer en een technisch verslag."], ["Wat is een inspectieput?", "Dat is de toegang tot de riolering, vaak in de kelder of tuin, waarlangs de hoofdleiding ontstopt wordt."], ["Hoeveel kost een rioolontstopping?", "De prijs hangt af van de toegang en de ernst. Je krijgt hem gratis vooraf."]]
  }
 },
 {
  "id": "siphon", "icon": "drain", "price": 80, "slug": {"fr": "debouchage-siphon", "nl": "ontstopping-afvoerputje"},
  "fr": {
   "name": "Siphon de sol",
   "card": "Garage, buanderie, cour : curage et aspiration des boues.",
   "title": "Débouchage siphon de sol Bruxelles 24h/24 – dès 80 € | ABS Débouchage",
   "desc": "Siphon de sol bouché à Bruxelles (garage, cave, buanderie, cour) ? Curage et aspiration des boues 24h/24, dès 80 €. ☎ 0484 72 47 24",
   "h1": "Débouchage de siphon de sol à Bruxelles",
   "intro": "Les siphons de sol des garages, caves, buanderies et cours piègent sable, feuilles et résidus de lessive. Quand ils se bouchent, l'eau stagne ou remonte à chaque orage. Nous les curons, aspirons les boues et les désinfectons.",
   "signs": ["Flaque permanente autour du siphon", "Refoulement lors des fortes pluies", "Odeur d'égout dans le garage ou la cave", "L'eau du lave-linge déborde du siphon"],
   "causes": ["Sable, terre et feuilles", "Peluches et résidus de lessive", "Grille absente ou cassée", "Bouchon dans la conduite vers l'égout"],
   "method": [["Ouverture", "Retrait de la grille et du panier."], ["Aspiration", "Pompage des boues et sédiments."], ["Curage", "Débouchage de la conduite jusqu'à l'égout."], ["Désinfection", "Nettoyage et remise en place de la grille."]],
   "tip": "En attendant : n'utilisez plus le lave-linge s'il se vide dans ce siphon.",
   "faq": [["Combien coûte un débouchage de siphon de sol ?", "À partir de 80 €, prix confirmé avant l'intervention."], ["Mon siphon déborde à chaque orage, pourquoi ?", "La conduite vers l'égout est souvent partiellement bouchée. Un curage, voire une inspection caméra, règle le problème."], ["Intervenez-vous pour les commerces ?", "Oui, garages, ateliers et commerces, 24h/24."]]
  },
  "nl": {
   "name": "Vloerputje",
   "card": "Garage, wasruimte, koer: reiniging en afzuigen van slib.",
   "title": "Ontstopping afvoerputje Brussel 24/7 – vanaf 80 € | ABS Débouchage",
   "desc": "Vloerputje verstopt in Brussel (garage, kelder, wasruimte, koer)? Reiniging en afzuigen van slib 24/7, vanaf 80 €. ☎ 0484 72 47 24",
   "h1": "Vloerputje en afvoerputje ontstoppen in Brussel",
   "intro": "Vloerputjes in garages, kelders, wasruimtes en koeren houden zand, bladeren en wasresten vast. Als ze verstopt raken, blijft het water staan of komt het bij elk onweer omhoog. Wij reinigen ze, zuigen het slib af en ontsmetten ze.",
   "signs": ["Permanente plas rond het putje", "Terugslag bij hevige regen", "Rioolgeur in garage of kelder", "Water van de wasmachine loopt over"],
   "causes": ["Zand, aarde en bladeren", "Pluisjes en wasresten", "Ontbrekend of kapot rooster", "Verstopping in de leiding naar de riool"],
   "method": [["Openen", "Rooster en korf verwijderen."], ["Afzuigen", "Slib en sediment wegpompen."], ["Reinigen", "Leiding ontstoppen tot aan de riool."], ["Ontsmetten", "Reinigen en rooster terugplaatsen."]],
   "tip": "In afwachting: gebruik de wasmachine niet meer als die in dit putje loost.",
   "faq": [["Hoeveel kost een vloerputje ontstoppen?", "Vanaf 80 €, prijs bevestigd vóór de interventie."], ["Mijn putje loopt over bij elk onweer, waarom?", "De leiding naar de riool is vaak deels verstopt. Een reiniging of camera-inspectie lost het op."], ["Komen jullie ook voor handelszaken?", "Ja, garages, werkplaatsen en winkels, 24/7."]]
  }
 },
 {
  "id": "camera", "icon": "camera", "price": None, "slug": {"fr": "inspection-camera", "nl": "camera-inspectie"},
  "fr": {
   "name": "Inspection caméra",
   "card": "Bouchons à répétition ? On trouve la cause, avec rapport vidéo.",
   "title": "Inspection caméra canalisation Bruxelles | ABS Débouchage",
   "desc": "Inspection caméra HD des canalisations à Bruxelles : racines, fissures et contre-pentes localisées au centimètre, rapport vidéo pour assurance ou syndic.",
   "h1": "Inspection caméra des canalisations à Bruxelles",
   "intro": "Bouchons à répétition, odeurs inexpliquées, humidité dans un mur ? Notre caméra rotative haute définition descend dans vos tuyaux, localise le problème au centimètre près et enregistre tout en vidéo. Vous recevez un rapport valable pour l'assurance, le syndic ou le notaire.",
   "signs": ["Bouchons à répétition au même endroit", "Humidité inexpliquée sur un mur ou un sol", "Odeurs persistantes malgré les débouchages", "Achat ou vente d'un bien immobilier"],
   "causes": ["Racines dans les joints de canalisation", "Tuyau fissuré, cassé ou affaissé", "Contre-pente qui retient l'eau", "Raccordement mal réalisé"],
   "method": [["Introduction", "Caméra HD rotative 360° introduite par un regard ou un siphon."], ["Localisation", "Sonde radio pour repérer le point exact depuis la surface."], ["Enregistrement", "Vidéo complète du parcours de la canalisation."], ["Rapport", "Rapport écrit avec constats et recommandations."]],
   "tip": "Conseil : faites inspecter les canalisations avant d'acheter une maison ancienne, cela évite de mauvaises surprises coûteuses.",
   "faq": [["À quoi sert une inspection caméra ?", "À voir l'intérieur des tuyaux sans casser, pour trouver la cause exacte d'un problème et éviter des travaux inutiles."], ["Le rapport est-il accepté par les assurances ?", "Oui, le rapport vidéo et écrit sert de preuve pour votre dossier d'assurance ou votre syndic."], ["Combien coûte une inspection caméra ?", "Le prix dépend de la longueur à inspecter. Il est annoncé gratuitement avant le rendez-vous."]]
  },
  "nl": {
   "name": "Camera-inspectie",
   "card": "Steeds opnieuw verstopt? We vinden de oorzaak, met videorapport.",
   "title": "Camera-inspectie riolering Brussel – videorapport | ABS Débouchage",
   "desc": "HD-camera-inspectie van je leidingen in Brussel: wortels, scheuren en tegenhellingen op de centimeter gelokaliseerd, videorapport voor verzekering of syndicus.",
   "h1": "Camera-inspectie van leidingen in Brussel",
   "intro": "Steeds terugkerende verstoppingen, onverklaarbare geuren, vocht in een muur? Onze draaibare HD-camera gaat in je leidingen, lokaliseert het probleem tot op de centimeter en neemt alles op video op. Je krijgt een verslag dat geldig is voor verzekering, syndicus of notaris.",
   "signs": ["Steeds verstopt op dezelfde plaats", "Onverklaarbaar vocht in muur of vloer", "Aanhoudende geuren ondanks ontstoppingen", "Aankoop of verkoop van een woning"],
   "causes": ["Wortels in de voegen", "Gescheurde, gebroken of verzakte leiding", "Tegenhelling die water vasthoudt", "Slecht uitgevoerde aansluiting"],
   "method": [["Inbrengen", "Draaibare HD-camera 360° via een put of sifon."], ["Lokaliseren", "Radiosonde om het exacte punt vanaf de oppervlakte te vinden."], ["Opnemen", "Volledige video van het traject van de leiding."], ["Verslag", "Schriftelijk verslag met vaststellingen en aanbevelingen."]],
   "tip": "Tip: laat de leidingen inspecteren voor je een oud huis koopt. Zo vermijd je dure verrassingen.",
   "faq": [["Waarvoor dient een camera-inspectie?", "Om de binnenkant van de leidingen te zien zonder breekwerk, de exacte oorzaak te vinden en onnodige werken te vermijden."], ["Aanvaarden verzekeraars het verslag?", "Ja, het video- en schriftelijk verslag dient als bewijs voor je verzekeringsdossier of syndicus."], ["Hoeveel kost een camera-inspectie?", "De prijs hangt af van de te inspecteren lengte. Je krijgt hem gratis vooraf."]]
  }
 },
]

# --------------------------------------------------------------------------
# TEXTES COMMUNS (interface)
# --------------------------------------------------------------------------
UI = {
 "fr": {
  "lang_name": "Français", "other": "nl", "other_label": "NL",
  "brand_sub": "Débouchage d'urgence · Bruxelles",
  "top": "Techniciens disponibles maintenant · 24h/24 – 7j/7",
  "nav_services": "Services", "nav_prices": "Tarifs", "nav_zones": "Zones", "nav_about": "À propos", "nav_contact": "Contact", "nav_all": "Tous nos services",
  "call": "Appeler", "call_now": "Appeler maintenant", "wa_quote": "Devis gratuit WhatsApp", "menu": "Menu",
  "chk": ["Devis gratuit", "Agréé assurances", "Facture avec n° TVA"],
  "from": "dès", "on_quote": "Sur devis", "learn": "En savoir plus",
  "home": "Accueil",
  # Devis
  "q_kick": "Devis express", "q_title": "Votre devis sur WhatsApp en 1 minute",
  "q_lead": "Répondez à 4 questions : votre demande arrive sur notre WhatsApp, déjà complète. On vous répond tout de suite avec un prix.",
  "q_steps": ["Choisissez votre problème et votre commune.", "WhatsApp s'ouvre avec le message déjà écrit : appuyez sur « Envoyer ».", "Ajoutez une photo si possible, on vous répond avec le prix."],
  "f_prob": "Quel est le problème ?", "f_urg": "C'est urgent ?", "u": {"now": "Oui, maintenant", "today": "Aujourd'hui", "plan": "À planifier"},
  "f_where": "Commune ou code postal", "ph_where": "ex. 1050 Ixelles", "f_name": "Votre prénom", "ph_name": "ex. Marc",
  "f_desc": "Détails (facultatif)", "ph_desc": "ex. L'eau remonte dans la douche depuis ce matin, 2e étage.",
  "other_pb": "Autre", "err": "Choisissez un problème et indiquez votre commune.",
  "send": "Envoyer ma demande sur WhatsApp", "note": "Gratuit et sans engagement · Réponse immédiate",
  "wa": {"hello": "Bonjour ABS Débouchage, je souhaite un devis.", "prob": "Problème", "urg": "Urgence", "where": "Commune", "name": "Nom", "det": "Détails",
         "urgv": {"now": "URGENT – maintenant", "today": "Aujourd'hui", "plan": "À planifier"}},
  # Accueil
  "home_title": "Débouchage Bruxelles 24h/24 – technicien en 30 min | ABS Débouchage",
  "home_desc": "Débouchage WC, évier, douche, égout et inspection caméra à Bruxelles. Urgence 24h/24, technicien sur place en 30 min, prix annoncé avant. ☎ 0484 72 47 24",
  "hero_pill": "Urgence débouchage à Bruxelles",
  "hero_h1": "Débouchage à Bruxelles, <em>sur place en 30&nbsp;min</em>, jour et nuit.",
  "hero_lead": "WC, évier, douche, égout à Bruxelles : un technicien équipé part dès votre appel, jour et nuit. Prix annoncé avant de commencer, intervention propre et sans casse.",
  "eta_title": "Exemple d'intervention", "eta_status": "Technicien en route", "eta_time": "Arrivée estimée", "eta_min": "min",
  "eta_steps": ["Appel reçu", "Prix confirmé", "En route", "Débouché"],
  "trust": [["clock", "30 min", "Délai moyen d'arrivée"], ["euro", "0 €", "Devis et déplacement annoncé"], ["shield", "Assurances", "Facture et rapport acceptés"], ["gauge", "400 bars", "Hydrocureur professionnel"]],
  "s_kick": "Nos interventions", "s_title": "Tous les bouchons, toutes les canalisations",
  "s_lead": "Du simple lavabo à l'égout principal, nous avons le bon matériel pour déboucher sans casser.",
  "w_kick": "Pourquoi ABS", "w_title": "Rapide, honnête, efficace",
  "why": [["clock", "Arrivée express", "Nos techniciens circulent dans Bruxelles : le plus proche part dès votre appel."], ["euro", "Prix annoncé avant", "Le prix est fixé au téléphone. Aucun travail ne commence sans votre accord."], ["gauge", "Matériel pro", "Furet électrique, hydrocureur 400 bars et caméra HD : on débouche sans abîmer vos tuyaux."], ["file", "Dossier assurance", "Facture officielle avec n° TVA et rapport technique pour votre remboursement."]],
  "h_kick": "Simple et rapide", "h_title": "Comment ça se passe ?",
  "how": [["Vous nous contactez", "Par téléphone ou WhatsApp, 24h/24. Décrivez le problème, on vous donne un prix."], ["Le technicien arrive", "En 30 minutes en moyenne, avec tout le matériel nécessaire."], ["C'est débouché", "Test d'écoulement, nettoyage de la zone, facture remise sur place."]],
  "p_kick": "Tarifs transparents", "p_title": "Des prix clairs, sans surprise",
  "p_lead": "Le prix exact est confirmé avant l'intervention. Ce qui est annoncé est ce que vous payez.",
  "badge": "Le plus demandé", "from_long": "à partir de", "price_lbl": "prix",
  "plans": [["Débouchage sanitaire", 80, ["WC, évier, lavabo, douche, siphon", "Furet électrique professionnel", "Test d'écoulement après travaux"]], ["Égout & haute pression", None, ["Égout, colonne, chambre de visite", "Camion hydrocureur 400 bars", "Racines, graisse et calcaire éliminés"]], ["Inspection caméra", None, ["Caméra HD rotative 360°", "Localisation au centimètre", "Rapport vidéo pour assurance ou syndic"]]],
  "ask_price": "Demander le prix", "p_note": "Prix indicatifs TVA comprise, à confirmer selon l'intervention.",
  "z_kick": "Zone d'intervention", "z_title": "Partout à Bruxelles et en périphérie",
  "z_lead": "Nous intervenons dans les 19 communes de la Région de Bruxelles-Capitale et dans la périphérie proche.",
  "z_peri": "Périphérie",
  "f_kick": "FAQ", "f_title": "Questions fréquentes",
  "faq": [["En combien de temps arrivez-vous ?", "En moyenne en 30 minutes après votre appel, partout à Bruxelles, de jour comme de nuit."], ["Combien coûte un débouchage à Bruxelles ?", "Un débouchage simple (WC, évier, douche) démarre entre 80 et 85 €. Le prix exact vous est annoncé avant l'intervention, sans surprise."], ["Intervenez-vous la nuit, le week-end et les jours fériés ?", "Oui, 24h/24 et 7j/7, toute l'année."], ["Mon assurance peut-elle rembourser ?", "Souvent oui, surtout en cas de dégât des eaux. Nous fournissons une facture officielle avec n° TVA et un rapport technique."], ["Que faire en attendant le technicien ?", "Arrêtez d'utiliser l'eau (chasse, lave-linge, lave-vaisselle), coupez l'arrivée d'eau si ça déborde et évitez les produits chimiques corrosifs."], ["Utilisez-vous des produits chimiques ?", "Non. Nous travaillons mécaniquement (furet, haute pression), sans produits corrosifs pour vos tuyaux ni pour l'environnement."]],
  "fin_title": "Un bouchon ? N'attendez pas que ça déborde.",
  "fin_lead": "Appelez maintenant : un technicien peut être chez vous dans 30 minutes.",
  # Pages service
  "sv_signs": "Les signes qui ne trompent pas", "sv_causes": "Les causes les plus fréquentes",
  "sv_method": "Notre méthode d'intervention", "sv_price": "Tarif", "sv_price_free": "Prix annoncé gratuitement avant l'intervention",
  "sv_tip": "En attendant le technicien", "sv_faq": "Questions fréquentes", "sv_other": "Nos autres services",
  "sv_zone": "Intervention dans toutes les communes de Bruxelles",
  # Footer
  "foot_about": "Débouchage d'urgence, hydrocurage et inspection caméra pour particuliers, syndics et entreprises à Bruxelles.",
  "foot_hours": "Ouvert 24h/24 – 7j/7", "foot_info": "Informations", "foot_services": "Services",
  "vat": "TVA", "insured": "Agréé assurances", "rights": "Tous droits réservés", "privacy": "Confidentialité",
  # Pages
  "about_slug": "a-propos", "contact_slug": "contact", "privacy_slug": "politique-de-confidentialite",
  "notfound": "Page introuvable", "notfound_lead": "Cette page n'existe pas ou a été déplacée. Besoin d'un débouchage ? On est là 24h/24.",
 },
 "nl": {
  "lang_name": "Nederlands", "other": "fr", "other_label": "FR",
  "brand_sub": "Spoedontstopping · Brussel",
  "top": "Techniekers nu beschikbaar · 24/7",
  "nav_services": "Diensten", "nav_prices": "Prijzen", "nav_zones": "Regio", "nav_about": "Over ons", "nav_contact": "Contact", "nav_all": "Al onze diensten",
  "call": "Bellen", "call_now": "Nu bellen", "wa_quote": "Gratis offerte via WhatsApp", "menu": "Menu",
  "chk": ["Gratis offerte", "Erkend door verzekeraars", "Factuur met btw-nummer"],
  "from": "vanaf", "on_quote": "Op offerte", "learn": "Meer info",
  "home": "Home",
  "q_kick": "Snelle offerte", "q_title": "Je offerte via WhatsApp in 1 minuut",
  "q_lead": "Beantwoord 4 vragen: je aanvraag komt volledig ingevuld op onze WhatsApp. We antwoorden meteen met een prijs.",
  "q_steps": ["Kies je probleem en je gemeente.", "WhatsApp opent met het bericht al ingevuld: druk op « Verzenden ».", "Voeg indien mogelijk een foto toe, we antwoorden met de prijs."],
  "f_prob": "Wat is het probleem?", "f_urg": "Is het dringend?", "u": {"now": "Ja, nu", "today": "Vandaag", "plan": "In te plannen"},
  "f_where": "Gemeente of postcode", "ph_where": "bv. 1050 Elsene", "f_name": "Je voornaam", "ph_name": "bv. Marc",
  "f_desc": "Details (optioneel)", "ph_desc": "bv. Het water komt sinds vanochtend omhoog in de douche, 2e verdieping.",
  "other_pb": "Andere", "err": "Kies een probleem en vul je gemeente in.",
  "send": "Mijn aanvraag via WhatsApp versturen", "note": "Gratis en vrijblijvend · Meteen antwoord",
  "wa": {"hello": "Hallo ABS Débouchage, ik wil graag een offerte.", "prob": "Probleem", "urg": "Dringend", "where": "Gemeente", "name": "Naam", "det": "Details",
         "urgv": {"now": "DRINGEND – nu", "today": "Vandaag", "plan": "In te plannen"}},
  "home_title": "Ontstopping Brussel 24/7 – technieker binnen 30 min | ABS Débouchage",
  "home_desc": "Ontstopping wc, gootsteen, douche, riool en camera-inspectie in Brussel. Spoed 24/7, technieker binnen 30 min ter plaatse, prijs vooraf gekend. ☎ 0484 72 47 24",
  "hero_pill": "Spoedontstopping in Brussel",
  "hero_h1": "Ontstopping in Brussel, <em>binnen 30&nbsp;min</em> ter plaatse, dag en nacht.",
  "hero_lead": "Wc, gootsteen, douche, riool in Brussel: een uitgeruste technieker vertrekt meteen na je oproep, dag en nacht. Prijs vooraf gekend, propere interventie zonder breekwerk.",
  "eta_title": "Voorbeeld van een interventie", "eta_status": "Technieker onderweg", "eta_time": "Verwachte aankomst", "eta_min": "min",
  "eta_steps": ["Oproep ontvangen", "Prijs bevestigd", "Onderweg", "Ontstopt"],
  "trust": [["clock", "30 min", "Gemiddelde aankomsttijd"], ["euro", "0 €", "Offerte vooraf gekend"], ["shield", "Verzekering", "Factuur en verslag aanvaard"], ["gauge", "400 bar", "Professionele hogedrukwagen"]],
  "s_kick": "Onze interventies", "s_title": "Alle verstoppingen, alle leidingen",
  "s_lead": "Van een eenvoudige lavabo tot de hoofdriolering: wij hebben het juiste materiaal om te ontstoppen zonder breekwerk.",
  "w_kick": "Waarom ABS", "w_title": "Snel, eerlijk, efficiënt",
  "why": [["clock", "Snel ter plaatse", "Onze techniekers rijden rond in Brussel: de dichtstbijzijnde vertrekt meteen na je oproep."], ["euro", "Prijs vooraf", "De prijs wordt telefonisch vastgelegd. Er gebeurt niets zonder je akkoord."], ["gauge", "Professioneel materiaal", "Elektrische veer, hogedrukwagen 400 bar en HD-camera: ontstoppen zonder je leidingen te beschadigen."], ["file", "Verzekeringsdossier", "Officiële factuur met btw-nummer en technisch verslag voor je terugbetaling."]],
  "h_kick": "Eenvoudig en snel", "h_title": "Hoe gaat het in zijn werk?",
  "how": [["Je neemt contact op", "Telefonisch of via WhatsApp, 24/7. Beschrijf het probleem, wij geven je een prijs."], ["De technieker komt", "Gemiddeld binnen 30 minuten, met al het nodige materiaal."], ["Het is ontstopt", "Doorlooptest, opkuis van de werkzone en factuur ter plaatse."]],
  "p_kick": "Transparante prijzen", "p_title": "Duidelijke prijzen, geen verrassingen",
  "p_lead": "De exacte prijs wordt vóór de interventie bevestigd. Wat we zeggen, is wat je betaalt.",
  "badge": "Meest gevraagd", "from_long": "vanaf", "price_lbl": "prijs",
  "plans": [["Sanitaire ontstopping", 80, ["Wc, gootsteen, lavabo, douche, putje", "Professionele elektrische veer", "Doorlooptest na de werken"]], ["Riool & hogedruk", None, ["Riool, kolom, inspectieput", "Hogedrukwagen 400 bar", "Wortels, vet en kalk verwijderd"]], ["Camera-inspectie", None, ["Draaibare HD-camera 360°", "Lokalisatie tot op de centimeter", "Videorapport voor verzekering of syndicus"]]],
  "ask_price": "Prijs vragen", "p_note": "Indicatieve prijzen incl. btw, te bevestigen afhankelijk van de interventie.",
  "z_kick": "Werkgebied", "z_title": "Overal in Brussel en de rand",
  "z_lead": "We komen in de 19 gemeenten van het Brussels Hoofdstedelijk Gewest en de nabije rand.",
  "z_peri": "Rand",
  "f_kick": "FAQ", "f_title": "Veelgestelde vragen",
  "faq": [["Hoe snel zijn jullie ter plaatse?", "Gemiddeld binnen 30 minuten na je oproep, overal in Brussel, dag en nacht."], ["Hoeveel kost een ontstopping in Brussel?", "Een eenvoudige ontstopping (wc, gootsteen, douche) start tussen 80 en 85 €. De exacte prijs krijg je vooraf, zonder verrassingen."], ["Komen jullie 's nachts, in het weekend en op feestdagen?", "Ja, 24/7, het hele jaar door."], ["Betaalt mijn verzekering terug?", "Vaak wel, zeker bij waterschade. Je krijgt een officiële factuur met btw-nummer en een technisch verslag."], ["Wat doe ik in afwachting van de technieker?", "Gebruik geen water meer (spoelen, wasmachine, vaatwasser), sluit de watertoevoer af als het overloopt en vermijd bijtende producten."], ["Gebruiken jullie chemische producten?", "Nee. We werken mechanisch (veer, hogedruk), zonder bijtende producten voor je leidingen of het milieu."]],
  "fin_title": "Verstopping? Wacht niet tot het overloopt.",
  "fin_lead": "Bel nu: een technieker kan binnen 30 minuten bij je zijn.",
  "sv_signs": "Duidelijke signalen", "sv_causes": "De meest voorkomende oorzaken",
  "sv_method": "Onze werkwijze", "sv_price": "Prijs", "sv_price_free": "Prijs gratis vooraf meegedeeld",
  "sv_tip": "In afwachting van de technieker", "sv_faq": "Veelgestelde vragen", "sv_other": "Onze andere diensten",
  "sv_zone": "Interventie in alle Brusselse gemeenten",
  "foot_about": "Spoedontstopping, hogedrukreiniging en camera-inspectie voor particulieren, syndici en bedrijven in Brussel.",
  "foot_hours": "24/7 open", "foot_info": "Informatie", "foot_services": "Diensten",
  "vat": "Btw", "insured": "Erkend door verzekeraars", "rights": "Alle rechten voorbehouden", "privacy": "Privacy",
  "about_slug": "over-ons", "contact_slug": "contact", "privacy_slug": "privacybeleid",
  "notfound": "Pagina niet gevonden", "notfound_lead": "Deze pagina bestaat niet of werd verplaatst. Nood aan een ontstopping? We zijn er 24/7.",
 }
}

ABOUT = {
 "fr": {
  "title": "À propos & tarifs – ABS Débouchage Bruxelles",
  "desc": "ABS Débouchage, entreprise belge de débouchage d'urgence à Bruxelles : nos engagements, notre matériel et nos tarifs transparents. TVA BE 0719.885.401.",
  "h1": "À propos d'ABS Débouchage",
  "lead": "Une entreprise belge spécialisée dans le débouchage d'urgence, l'hydrocurage et l'inspection caméra, pour les particuliers, les syndics, les commerces et les restaurants de Bruxelles.",
  "blocks": [["Nos engagements", ["Arrivée en moyenne en 30 minutes, 24h/24 et 7j/7.", "Prix annoncé avant le départ du technicien : c'est ce prix qui figure sur la facture.", "Aucun travail ne commence sans votre accord.", "Intervention propre : la zone est nettoyée avant notre départ."]],
             ["Notre matériel", ["Furets électriques rotatifs professionnels.", "Camions hydrocureurs haute pression jusqu'à 400 bars.", "Caméra d'inspection HD rotative 360° avec sonde de localisation.", "Aucun produit chimique corrosif."]],
             ["Assurance & facturation", ["Facture officielle avec n° TVA BE 0719.885.401.", "Rapport technique et vidéo pour votre dossier d'assurance.", "Documents acceptés par les syndics et notaires."]]]
 },
 "nl": {
  "title": "Over ons & prijzen – ABS Débouchage Brussel",
  "desc": "ABS, Belgisch bedrijf voor spoedontstopping in Brussel: onze engagementen, ons materiaal en onze transparante prijzen. Btw BE 0719.885.401.",
  "h1": "Over ABS",
  "lead": "Een Belgisch bedrijf gespecialiseerd in spoedontstopping, hogedrukreiniging en camera-inspectie, voor particulieren, syndici, winkels en restaurants in Brussel.",
  "blocks": [["Onze engagementen", ["Gemiddeld binnen 30 minuten ter plaatse, 24/7.", "Prijs gekend vóór de technieker vertrekt: die prijs staat op de factuur.", "Er gebeurt niets zonder je akkoord.", "Propere interventie: de werkzone wordt gereinigd voor we vertrekken."]],
             ["Ons materiaal", ["Professionele elektrische veren.", "Hogedrukwagens tot 400 bar.", "Draaibare HD-inspectiecamera 360° met lokalisatiesonde.", "Geen bijtende chemische producten."]],
             ["Verzekering & facturatie", ["Officiële factuur met btw-nummer BE 0719.885.401.", "Technisch en videoverslag voor je verzekeringsdossier.", "Documenten aanvaard door syndici en notarissen."]]]
 }
}

PRIVACY = {
 "fr": ("Politique de confidentialité", [
  "ABS Débouchage (TVA BE 0719.885.401) respecte votre vie privée conformément au Règlement général sur la protection des données (RGPD).",
  "Données collectées : ce site ne collecte aucune donnée via des formulaires stockés sur nos serveurs. Lorsque vous utilisez le bouton de devis, un message est préparé dans WhatsApp et c'est vous qui choisissez de l'envoyer. Les informations que vous nous transmettez par téléphone ou WhatsApp (prénom, commune, description du problème, photos) servent uniquement à établir un devis et à réaliser l'intervention.",
  "Conservation : vos données sont conservées le temps nécessaire au suivi de l'intervention et aux obligations comptables légales.",
  "Cookies : ce site n'utilise pas de cookies de suivi ou publicitaires. Votre choix de langue peut être mémorisé localement dans votre navigateur.",
  "Vos droits : vous pouvez demander l'accès, la rectification ou la suppression de vos données en écrivant à contact@abs-debouchage.be. Vous pouvez aussi introduire une plainte auprès de l'Autorité de protection des données (autoriteprotectiondonnees.be)."]),
 "nl": ("Privacybeleid", [
  "ABS (btw BE 0719.885.401) respecteert je privacy overeenkomstig de Algemene Verordening Gegevensbescherming (AVG/GDPR).",
  "Verzamelde gegevens: deze site verzamelt geen gegevens via formulieren die op onze servers worden opgeslagen. Wanneer je de offerteknop gebruikt, wordt een bericht in WhatsApp voorbereid en kies jij of je het verstuurt. De informatie die je ons telefonisch of via WhatsApp bezorgt (voornaam, gemeente, beschrijving, foto's) dient enkel om een offerte op te maken en de interventie uit te voeren.",
  "Bewaring: je gegevens worden bewaard zolang nodig voor de opvolging van de interventie en de wettelijke boekhoudkundige verplichtingen.",
  "Cookies: deze site gebruikt geen tracking- of advertentiecookies. Je taalkeuze kan lokaal in je browser worden onthouden.",
  "Je rechten: je kunt inzage, verbetering of verwijdering van je gegevens vragen via contact@abs-debouchage.be. Je kunt ook klacht indienen bij de Gegevensbeschermingsautoriteit (gegevensbeschermingsautoriteit.be)."]),
}

# --------------------------------------------------------------------------
# DIAGNOSTIC EXPRESS : situations proposées pour chaque problème
# niveau : "urgent" (intervention immédiate), "today" (dans la journée), "plan" (à planifier)
# --------------------------------------------------------------------------
DIAG = {
 "wc": [("urgent", "L'eau monte jusqu'au bord ou déborde", "Het water komt tot aan de rand of loopt over"),
        ("today", "L'eau s'écoule très lentement", "Het water loopt heel traag weg"),
        ("plan", "Ça s'écoule, mais il y a une odeur ou des bruits", "Het loopt weg, maar er is een geur of borrelend geluid")],
 "sanibroyeur": [("urgent", "Le broyeur ne démarre plus ou tourne sans s'arrêter", "De broyeur start niet of draait zonder te stoppen"),
                 ("urgent", "L'eau remonte dans la douche ou le lavabo raccordé", "Water komt omhoog in de aangesloten douche of lavabo"),
                 ("today", "Bruit anormal, mais il fonctionne encore", "Abnormaal geluid, maar hij werkt nog")],
 "evier": [("urgent", "L'eau stagne dans l'évier et ne descend plus", "Het water blijft in de gootsteen staan en zakt niet meer"),
           ("today", "L'eau descend lentement", "Het water zakt traag"),
           ("plan", "Odeurs ou gargouillements", "Geuren of borrelende geluiden")],
 "lavabo": [("today", "Le lavabo est plein et ne se vide plus", "De lavabo staat vol en loopt niet meer leeg"),
            ("plan", "Il se vide lentement", "Hij loopt traag leeg"),
            ("today", "Un objet est tombé dans la bonde", "Er is een voorwerp in de afvoer gevallen")],
 "douche": [("urgent", "L'eau déborde du bac de douche", "Het water loopt over de douchebak"),
            ("today", "L'eau s'évacue très lentement", "Het water loopt heel traag weg"),
            ("plan", "Une odeur remonte par la bonde", "Er komt een geur uit het afvoerputje")],
 "baignoire": [("today", "La baignoire est pleine et ne se vide pas", "Het bad staat vol en loopt niet leeg"),
               ("urgent", "L'eau d'un autre appareil remonte dedans", "Water van een ander toestel komt erin omhoog"),
               ("plan", "Elle se vide lentement", "Het loopt traag leeg")],
 "cuisine": [("urgent", "Plusieurs appareils refoulent en même temps", "Meerdere toestellen slaan tegelijk terug"),
             ("urgent", "L'eau remonte chez un voisin", "Het water komt omhoog bij een buur"),
             ("today", "Tout s'écoule lentement dans le logement", "Alles loopt traag weg in de woning")],
 "egout": [("urgent", "Les eaux usées remontent dans la cave", "Afvalwater komt omhoog in de kelder"),
           ("urgent", "Le regard (chambre de visite) déborde", "De inspectieput loopt over"),
           ("today", "Tout s'écoule mal, surtout quand il pleut", "Alles loopt slecht af, vooral bij regen")],
 "siphon": [("urgent", "L'eau déborde du siphon", "Het water loopt over uit het putje"),
            ("today", "Une flaque reste autour du siphon", "Er blijft een plas rond het putje staan"),
            ("plan", "Une odeur d'égout remonte", "Er komt een rioolgeur omhoog")],
 "camera": [("today", "Bouchons à répétition au même endroit", "Steeds opnieuw verstopt op dezelfde plaats"),
            ("today", "Humidité inexpliquée dans un mur ou un sol", "Onverklaarbaar vocht in een muur of vloer"),
            ("plan", "Contrôle avant un achat ou une vente", "Controle voor een aankoop of verkoop")],
 "autre": [("urgent", "Ça déborde ou ça refoule", "Het loopt over of slaat terug"),
           ("today", "Ça s'écoule mal", "Het loopt slecht weg"),
           ("plan", "Je veux un conseil ou un rendez-vous", "Ik wil advies of een afspraak")],
}

DIAG_UI = {
 "fr": {
  "label": "Diagnostic express", "title": "Décrivez votre problème, on vous dit quoi faire",
  "lead": "Trois questions, moins d'une minute. Vous obtenez le niveau d'urgence, le prix de départ et les bons gestes en attendant. Votre demande nous arrive ensuite déjà complète sur WhatsApp.",
  "pros": ["Gratuit et sans engagement", "Réponse immédiate, 24h/24", "Prix annoncé avant toute intervention"],
  "alt": "Vous préférez appeler directement ?",
  "box": "Diagnostic express", "step": "Étape {n} sur 3",
  "q1": "Quel est le problème ?", "h1": "Choisissez ce qui correspond le mieux.",
  "q2": "Que se passe-t-il exactement ?", "h2": "Votre réponse nous aide à évaluer l'urgence.",
  "q3": "Votre diagnostic", "back": "Retour", "other": "Autre problème",
  "sev": {"urgent": ("Urgent : intervention immédiate recommandée", "Un technicien peut être chez vous en 30 minutes environ. N'attendez pas que la situation s'aggrave."),
          "today": ("À traiter aujourd'hui", "Ce n'est pas encore une inondation, mais ça peut vite s'aggraver. Mieux vaut intervenir dans la journée."),
          "plan": ("Pas d'urgence immédiate", "On peut fixer ensemble un rendez-vous qui vous arrange, sans frais supplémentaires.")},
  "price": "Prix de départ", "price_q": "Annoncé gratuitement avant l'intervention", "wait": "En attendant le technicien",
  "wait_generic": "Arrêtez d'utiliser l'eau, coupez l'arrivée d'eau si ça déborde et évitez les produits chimiques.",
  "where": "Votre commune ou code postal", "where_ph": "ex. 1050 Ixelles", "name": "Votre prénom", "opt": "(facultatif)",
  "err": "Indiquez votre commune pour que l'on puisse estimer le délai.",
  "send": "Envoyer sur WhatsApp", "call": "Appeler maintenant",
  "note": "WhatsApp s'ouvre avec votre diagnostic déjà rédigé : il vous reste à appuyer sur Envoyer.",
  "sent": "WhatsApp s'est ouvert dans un nouvel onglet. Si rien ne s'est passé, appelez-nous au 0484 72 47 24.",
  "noscript": "Pour un diagnostic, appelez-nous directement :",
  "wa": {"hello": "Bonjour ABS Débouchage, voici mon diagnostic :", "prob": "Problème", "sit": "Situation", "lvl": "Niveau", "where": "Commune", "name": "Prénom"},
 },
 "nl": {
  "label": "Snelle diagnose", "title": "Beschrijf je probleem, wij zeggen wat je moet doen",
  "lead": "Drie vragen, minder dan een minuut. Je krijgt het dringendheidsniveau, de startprijs en wat je intussen kunt doen. Je aanvraag komt daarna volledig ingevuld bij ons op WhatsApp.",
  "pros": ["Gratis en vrijblijvend", "Meteen antwoord, 24/7", "Prijs gekend vóór elke interventie"],
  "alt": "Liever meteen bellen?",
  "box": "Snelle diagnose", "step": "Stap {n} van 3",
  "q1": "Wat is het probleem?", "h1": "Kies wat het best overeenkomt.",
  "q2": "Wat gebeurt er precies?", "h2": "Je antwoord helpt ons de dringendheid in te schatten.",
  "q3": "Jouw diagnose", "back": "Terug", "other": "Ander probleem",
  "sev": {"urgent": ("Dringend: onmiddellijke interventie aangeraden", "Een technieker kan binnen ongeveer 30 minuten bij je zijn. Wacht niet tot het erger wordt."),
          "today": ("Vandaag aanpakken", "Het is nog geen overstroming, maar het kan snel erger worden. Best vandaag nog laten bekijken."),
          "plan": ("Geen onmiddellijke nood", "We spreken samen een moment af dat jou past, zonder extra kosten.")},
  "price": "Startprijs", "price_q": "Gratis vooraf meegedeeld", "wait": "In afwachting van de technieker",
  "wait_generic": "Gebruik geen water meer, sluit de watertoevoer af als het overloopt en vermijd chemische producten.",
  "where": "Je gemeente of postcode", "where_ph": "bv. 1050 Elsene", "name": "Je voornaam", "opt": "(optioneel)",
  "err": "Vul je gemeente in zodat we de aankomsttijd kunnen inschatten.",
  "send": "Versturen via WhatsApp", "call": "Nu bellen",
  "note": "WhatsApp opent met je diagnose al ingevuld: je hoeft alleen nog op Verzenden te drukken.",
  "sent": "WhatsApp is geopend in een nieuw tabblad. Gebeurde er niets? Bel ons op 0484 72 47 24.",
  "noscript": "Voor een diagnose, bel ons rechtstreeks:",
  "wa": {"hello": "Hallo ABS Débouchage, hier is mijn diagnose:", "prob": "Probleem", "sit": "Situatie", "lvl": "Niveau", "where": "Gemeente", "name": "Voornaam"},
 }
}
