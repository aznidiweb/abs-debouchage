# -*- coding: utf-8 -*-
"""
CONTENU DU SITE ABS DÉBOUCHAGE
Tous les textes sont ici. Après une modification : python3 build.py
"""

SITE_URL = "https://www.absdebouchage.be"   # domaine final (utilisé pour Google)
PHONE_DISPLAY = "0484 72 47 24"
PHONE_TEL = "+32484724724"
WHATSAPP = "32484724724"
EMAIL = "absdebouchage@gmail.com"
# Date de dernière modification de la politique de confidentialité (à changer seulement quand son texte change)
PRIVACY_UPDATED = "2026-11-24"

# Réseaux sociaux officiels (pied de page + données Google « sameAs »). Laisser vide ce qui n'existe pas encore.
SOCIAL = [
    ("instagram", "Instagram", "https://www.instagram.com/absdebouchage/"),
    ("facebook", "Facebook", "https://www.facebook.com/absdebouchage"),
    ("tiktok", "TikTok", "https://www.tiktok.com/@abs.debouchage"),
]
# ---- Fiche Google (Google Business Profile) ----
# Identifiant Maps de la fiche (vérifié le 23/11/2026 : « ABS Débouchage »). Liens publics, aucun script chargé sans clic.
GBP_CID = "7929071025865156455"
GBP_MAPS_URL = "https://www.google.com/maps?cid=" + GBP_CID
GBP_REVIEW_URL = "https://g.page/r/CWfniIcWuAluEBM/review"
# Note et nombre d'avis affichés sur le site : à mettre à jour quand les avis augmentent (relevé du 23/11/2026).
GBP_RATING = "5,0"
GBP_COUNT = 8
VAT = "BE 0719.885.401"
VAT_RAW = "BE0719885401"
BRAND = "ABS Débouchage"

# ---- Google Ads : mesure des appels et des clics WhatsApp ----
# Laisser vide tant que le compte n'existe pas : aucun script Google n'est chargé et aucun bandeau n'apparaît.
# Exemple une fois le compte créé : GADS_ID = "AW-123456789", GADS_CALL = "AbCdEf123", GADS_WA = "XyZ987"
GADS_ID = "AW-18584749791"      # identifiant du compte (Outils > Conversions > balise Google)
GADS_CALL = "9gY3CNTsmrwdEN-N851F"    # libellé de la conversion « Clic sur le numéro »
GADS_WA = "KNNmCNfsmrwdEN-N851F"      # libellé de la conversion « Clic WhatsApp »
GADS_FORM = ""   # libellé de la conversion « Demande envoyée (formulaire) » : à créer dans Google Ads puis coller ici
LEGAL_NAME = "C.R.N.M. & Cie SRL"
STREET = "Rue de la Carpe 2"
POSTCODE = "1080"
CITY = {"fr": "Bruxelles", "nl": "Brussel"}

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
  "id": "wc", "icon": "toilet", "price": None, "slug": {"fr": "debouchage-wc", "nl": "ontstopping-wc"},
  "fr": {
   "name": "Débouchage WC",
   "card": "Cuvette qui déborde ou se vide mal : on débouche sans abîmer la faïence.",
   "title": "Débouchage WC 7j/7 – Bruxelles & Belgique | ABS Débouchage",
   "desc": "WC bouché à Bruxelles ou ailleurs en Belgique ? Technicien disponible 7j/7. Débouchage propre au furet électrique, prix annoncé avant travaux, devis gratuit.",
   "h1": "Débouchage WC à Bruxelles et partout en Belgique, 7j/7",
   "intro": "Des toilettes bouchées, c'est l'urgence la plus fréquente… et la plus stressante. Nos techniciens interviennent à Bruxelles et dans toute la Belgique, avec un furet électrique professionnel qui débouche la cuvette et le tuyau d'évacuation sans rayer la porcelaine.",
   "signs": ["L'eau monte jusqu'au bord de la cuvette après la chasse", "La cuvette se vide très lentement ou fait des bruits de glouglou", "Une odeur d'égout remonte dans la salle de bain", "La ventouse ne donne plus aucun résultat"],
   "causes": ["Trop de papier toilette en une fois", "Lingettes, cotons-tiges ou serviettes hygiéniques jetés dans le WC", "Objet tombé dans la cuvette (jouet, brosse, déodorant)", "Dépôts de calcaire qui réduisent le passage du tuyau"],
   "method": [["Diagnostic", "On identifie où se trouve le bouchon : cuvette, coude ou colonne d'évacuation."], ["Débouchage", "Furet électrique rotatif ou pompe haute pression selon le cas, sans démonter le WC."], ["Test", "Plusieurs chasses d'eau pour vérifier un écoulement parfait."], ["Nettoyage", "La zone est nettoyée et désinfectée avant notre départ."]],
   "tip": "En attendant le technicien : ne tirez plus la chasse, fermez le robinet d'arrivée d'eau derrière le WC et évitez les produits chimiques, qui abîment les joints et sont dangereux pour nos techniciens.",
   "faq": [["Combien coûte un débouchage de WC à Bruxelles ?", "Le prix dépend du type d'intervention, de l'heure et du jour (soirée, week-end). Il vous est annoncé gratuitement par téléphone ou WhatsApp avant l'intervention, et c'est ce prix qui figure sur la facture."], ["Faut-il démonter les toilettes ?", "Dans la grande majorité des cas, non. Le furet électrique passe directement par la cuvette jusqu'au bouchon."], ["Quels sont vos horaires pour un WC bouché ?", "Tous les jours, de 6h à 21h, week-end compris."]]
  },
  "nl": {
   "name": "Ontstopping wc",
   "card": "Pot die overloopt of traag leegloopt: we ontstoppen zonder de porselein te beschadigen.",
   "title": "Ontstopping wc 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Wc verstopt in Brussel of elders in België? Technieker beschikbaar 7/7. Propere ontstopping met elektrische veer, prijs vooraf gekend, gratis offerte.",
   "h1": "Wc ontstoppen in Brussel en heel België, 7/7",
   "intro": "Een verstopt toilet is de meest voorkomende noodsituatie… en de meest stresserende. Onze techniekers komen in Brussel en in heel België, met een professionele elektrische veer die de pot en de afvoer ontstopt zonder het porselein te krassen.",
   "signs": ["Het water komt na het doorspoelen tot aan de rand van de pot", "De pot loopt heel traag leeg of maakt borrelende geluiden", "Er komt een rioolgeur in de badkamer", "De ontstopper (zuignap) helpt niet meer"],
   "causes": ["Te veel toiletpapier in één keer", "Doekjes, wattenstaafjes of maandverband in het toilet", "Voorwerp in de pot gevallen (speelgoed, borstel, deodorant)", "Kalkaanslag die de afvoer vernauwt"],
   "method": [["Diagnose", "We zoeken waar de verstopping zit: pot, bocht of afvoerkolom."], ["Ontstopping", "Elektrische veer of hogedrukpomp, afhankelijk van de situatie, zonder de wc te demonteren."], ["Test", "Meermaals doorspoelen om een perfecte afvoer te controleren."], ["Opkuis", "De werkzone wordt gereinigd en ontsmet voor we vertrekken."]],
   "tip": "In afwachting van de technieker: spoel niet meer door, sluit de waterkraan achter de wc en gebruik geen chemische producten. Die beschadigen de dichtingen en zijn gevaarlijk voor onze techniekers.",
   "faq": [["Hoeveel kost een wc-ontstopping in Brussel?", "De prijs hangt af van de situatie. Je krijgt hem gratis telefonisch of via WhatsApp vóór de interventie, en die prijs staat op de factuur."], ["Moet het toilet gedemonteerd worden?", "In de meeste gevallen niet. De elektrische veer gaat rechtstreeks via de pot tot aan de verstopping."], ["Wat zijn jullie uren voor een verstopte wc?", "Elke dag van 6 tot 21 uur, ook in het weekend."]]
  }
 },
 {
  "id": "sanibroyeur", "icon": "sanibroyeur", "price": None, "slug": {"fr": "debouchage-sanibroyeur", "nl": "ontstopping-sanibroyeur"},
  "fr": {
   "name": "Sanibroyeur & WC suspendu",
   "card": "Broyeur bloqué ou WC suspendu Geberit : intervention délicate, sans casse.",
   "title": "Débouchage sanibroyeur – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Sanibroyeur bloqué ou WC suspendu bouché à Bruxelles ou ailleurs en Belgique ? Intervention 7j/7, sans abîmer le moteur ni le bâti. Devis gratuit : 0484 72 47 24",
   "h1": "Débouchage de sanibroyeur et WC suspendu à Bruxelles et partout en Belgique",
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
   "title": "Ontstopping sanibroyeur 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Sanibroyeur geblokkeerd of hangtoilet verstopt in Brussel of elders in België? Interventie 7/7, zonder schade aan motor of reservoir. Gratis offerte.",
   "h1": "Sanibroyeur en hangtoilet ontstoppen in Brussel en heel België",
   "intro": "Een sanibroyeur of hangtoilet ontstop je niet zoals een gewoon toilet. De motor, messen en membranen zijn kwetsbaar en het reservoir zit in de muur. Onze techniekers kennen deze installaties en zetten ze weer in werking zonder schade.",
   "signs": ["De motor van de broyeur draait leeg of stopt niet meer", "De broyeur maakt een abnormaal geluid of start niet", "Vuil water komt omhoog in de aangesloten douche of lavabo", "Het hangtoilet loopt slecht weg, ook met een zuignap"],
   "causes": ["Doekjes of keukenpapier vast in de messen", "Kalk in het reservoir van de broyeur", "Vuile membraan of terugslagklep", "Verstopping in de dunne afvoerleiding"],
   "method": [["Veiligheid", "Stroom van de broyeur uitschakelen voor elke interventie."], ["Openen", "Toegang tot het reservoir en verwijderen van wat de messen blokkeert."], ["Ontkalken", "Reiniging van reservoir, klep en afvoerleiding."], ["Herstart", "Volledige test van de pompcyclus en de dichtheid."]],
   "tip": "In afwachting: trek de stekker van de sanibroyeur uit, gebruik de aangesloten toestellen (douche, lavabo) niet meer en giet nooit chemische ontstopper. Die vernielt de dichtingen en het membraan.",
   "faq": [["Kan een verstopte sanibroyeur hersteld worden zonder hem te vervangen?", "Ja, meestal volstaat een grondige reiniging en ontkalking om hem weer te laten werken."], ["Werken jullie aan Geberit-hangtoiletten?", "Ja, we ontstoppen hangtoiletten zonder de muur open te breken of het reservoir te demonteren."], ["Hoeveel kost de interventie?", "De prijs hangt af van het probleem. Je krijgt hem gratis vooraf, telefonisch of via WhatsApp."]]
  }
 },
 {
  "id": "evier", "icon": "sink", "price": None, "slug": {"fr": "debouchage-evier", "nl": "ontstopping-gootsteen"},
  "fr": {
   "name": "Débouchage évier",
   "card": "Graisse et restes de repas : dégraissage complet du siphon et du tuyau.",
   "title": "Débouchage évier 7j/7 – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Évier de cuisine bouché à Bruxelles ou ailleurs en Belgique ? Débouchage et dégraissage haute pression, 7j/7. Prix annoncé avant travaux, devis gratuit.",
   "h1": "Débouchage d'évier de cuisine à Bruxelles et partout en Belgique",
   "intro": "L'évier de cuisine reçoit chaque jour de la graisse chaude, qui fige dans les tuyaux et retient les restes alimentaires. Résultat : l'eau stagne et les odeurs s'installent. Nous débouchons et dégraissons le siphon et la canalisation pour retrouver un écoulement comme neuf.",
   "signs": ["L'eau stagne dans les bacs de l'évier", "Odeur de graisse rance ou d'égout", "Gargouillements quand le lave-vaisselle se vide", "L'eau remonte dans le second bac"],
   "causes": ["Graisse de cuisson versée dans l'évier", "Marc de café, riz, pâtes et restes alimentaires", "Siphon encrassé jamais nettoyé", "Lave-vaisselle raccordé sur une évacuation trop étroite"],
   "method": [["Démontage du siphon", "Nettoyage complet du siphon et de la bonde."], ["Furet électrique", "Passage du furet dans la canalisation pour casser le bouchon de graisse."], ["Dégraissage", "Rinçage haute pression pour nettoyer les parois du tuyau."], ["Contrôle", "Test à plein débit, évier et lave-vaisselle."]],
   "tip": "En attendant : n'utilisez plus le lave-vaisselle et ne versez pas d'eau bouillante si le tuyau est en PVC, elle peut le déformer.",
   "faq": [["Combien coûte un débouchage d'évier ?", "Le prix dépend du type d'intervention, de l'heure et du jour (soirée, week-end). Il vous est annoncé gratuitement par téléphone ou WhatsApp avant l'intervention, et c'est ce prix qui figure sur la facture."], ["Mon évier se rebouche souvent, que faire ?", "C'est souvent un dépôt de graisse en profondeur. Un hydrocurage ou une inspection caméra permet de traiter la cause."], ["Intervenez-vous dans les restaurants ?", "Oui, nous intervenons aussi pour les cuisines professionnelles, 7j/7."]]
  },
  "nl": {
   "name": "Ontstopping gootsteen",
   "card": "Vet en etensresten: volledige reiniging van sifon en afvoer.",
   "title": "Ontstopping gootsteen 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Gootsteen verstopt in Brussel of elders in België? Ontstopping en hogedrukreiniging, 7/7. Prijs vooraf gekend, gratis offerte. ☎ 0484 72 47 24",
   "h1": "Gootsteen ontstoppen in Brussel en heel België",
   "intro": "De keukengootsteen krijgt elke dag heet vet te verwerken. Dat stolt in de leidingen en houdt etensresten vast. Gevolg: het water blijft staan en het begint te stinken. Wij ontstoppen en ontvetten de sifon en de afvoer zodat alles weer vlot wegloopt.",
   "signs": ["Het water blijft in de gootsteen staan", "Geur van ranzig vet of riool", "Borrelende geluiden als de vaatwasser leegloopt", "Water komt omhoog in de tweede kuip"],
   "causes": ["Bakvet in de gootsteen gegoten", "Koffiedik, rijst, pasta en etensresten", "Vuile sifon die nooit gereinigd werd", "Vaatwasser aangesloten op een te smalle afvoer"],
   "method": [["Sifon demonteren", "Volledige reiniging van sifon en afvoerplug."], ["Elektrische veer", "De veer breekt de vetprop in de leiding."], ["Ontvetten", "Spoelen onder hoge druk om de wanden van de leiding te reinigen."], ["Controle", "Test op vol debiet, gootsteen en vaatwasser."]],
   "tip": "In afwachting: gebruik de vaatwasser niet meer en giet geen kokend water als de leiding uit pvc is, die kan vervormen.",
   "faq": [["Hoeveel kost een gootsteenontstopping?", "De prijs hangt af van de situatie. Je krijgt hem gratis telefonisch of via WhatsApp vóór de interventie, en die prijs staat op de factuur."], ["Mijn gootsteen raakt vaak verstopt, wat nu?", "Meestal zit er diep in de leiding vet. Hogedrukreiniging of een camera-inspectie pakt de oorzaak aan."], ["Komen jullie ook naar restaurants?", "Ja, ook voor professionele keukens, 7/7."]]
  }
 },
 {
  "id": "lavabo", "icon": "basin", "price": None, "slug": {"fr": "debouchage-lavabo", "nl": "ontstopping-lavabo"},
  "fr": {
   "name": "Débouchage lavabo",
   "card": "Cheveux, savon, dentifrice : siphon et vidage nettoyés proprement.",
   "title": "Débouchage lavabo 7j/7 – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Lavabo ou vasque bouché à Bruxelles ou ailleurs en Belgique ? Intervention rapide 7j/7, siphon et évacuation nettoyés sans abîmer vos meubles.",
   "h1": "Débouchage de lavabo et vasque à Bruxelles et partout en Belgique",
   "intro": "Cheveux, savon et dentifrice forment petit à petit un bouchon dans le siphon du lavabo. Nos techniciens démontent et nettoient le siphon, la bonde et la canalisation, avec soin pour vos meubles de salle de bain.",
   "signs": ["L'eau stagne après le brossage de dents", "Bonde clic-clac bloquée", "Odeurs dans la salle de bain", "Écoulement lent qui s'aggrave"],
   "causes": ["Cheveux accumulés dans la bonde", "Savon et dentifrice qui collent aux parois", "Calcaire dans le siphon", "Petit objet tombé (bouchon, bijou)"],
   "method": [["Bonde", "Démontage et nettoyage de la bonde et du mécanisme clic-clac."], ["Siphon", "Démontage du siphon, nettoyage, remontage étanche."], ["Canalisation", "Passage du furet si le bouchon est plus loin."], ["Test", "Vérification de l'écoulement et de l'étanchéité."]],
   "tip": "En attendant : retirez la bonde clic-clac si vous pouvez et enlevez les cheveux visibles. Évitez la soude caustique.",
   "faq": [["Combien coûte un débouchage de lavabo ?", "Le prix dépend du type d'intervention, de l'heure et du jour (soirée, week-end). Il vous est annoncé gratuitement par téléphone ou WhatsApp avant l'intervention, et c'est ce prix qui figure sur la facture."], ["Pouvez-vous récupérer un bijou tombé dans le lavabo ?", "Souvent oui : il reste généralement coincé dans le siphon. Arrêtez d'utiliser le lavabo et appelez-nous."], ["Vous démontez le meuble ?", "Rarement. Le siphon est accessible sous la vasque dans la plupart des cas."]]
  },
  "nl": {
   "name": "Ontstopping lavabo",
   "card": "Haren, zeep, tandpasta: sifon en afvoer netjes gereinigd.",
   "title": "Ontstopping lavabo 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Lavabo of wastafel verstopt in Brussel of elders in België? Snelle interventie 7/7, sifon en afvoer gereinigd zonder schade aan je meubels. Gratis offerte.",
   "h1": "Lavabo en wastafel ontstoppen in Brussel en heel België",
   "intro": "Haren, zeep en tandpasta vormen beetje bij beetje een prop in de sifon van de lavabo. Onze techniekers demonteren en reinigen sifon, afvoerplug en leiding, met respect voor je badkamermeubel.",
   "signs": ["Het water blijft staan na het tandenpoetsen", "Klik-klakplug geblokkeerd", "Geur in de badkamer", "Trage afvoer die erger wordt"],
   "causes": ["Haren in de afvoerplug", "Zeep en tandpasta op de wanden", "Kalk in de sifon", "Klein voorwerp gevallen (dop, juweel)"],
   "method": [["Afvoerplug", "Demonteren en reinigen van de plug en het klik-klakmechanisme."], ["Sifon", "Sifon demonteren, reinigen en waterdicht terugplaatsen."], ["Leiding", "Elektrische veer als de verstopping verder zit."], ["Test", "Controle van afvoer en dichtheid."]],
   "tip": "In afwachting: verwijder de klik-klakplug als dat lukt en haal zichtbare haren weg. Vermijd bijtende soda.",
   "faq": [["Hoeveel kost een lavabo-ontstopping?", "De prijs hangt af van de situatie. Je krijgt hem gratis telefonisch of via WhatsApp vóór de interventie, en die prijs staat op de factuur."], ["Kunnen jullie een juweel uit de lavabo halen?", "Vaak wel: het blijft meestal in de sifon steken. Gebruik de lavabo niet meer en bel ons."], ["Wordt het meubel gedemonteerd?", "Zelden. De sifon is meestal bereikbaar onder de wastafel."]]
  }
 },
 {
  "id": "douche", "icon": "shower", "price": None, "slug": {"fr": "debouchage-douche", "nl": "ontstopping-douche"},
  "fr": {
   "name": "Débouchage douche",
   "card": "Bac ou douche à l'italienne qui déborde : débouché sans casser le carrelage.",
   "title": "Débouchage douche 7j/7 – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Douche bouchée à Bruxelles ou ailleurs en Belgique ? Bac, douche à l'italienne ou caniveau : débouchage sans casser le carrelage, 7j/7.",
   "h1": "Débouchage de douche et douche à l'italienne à Bruxelles et partout en Belgique",
   "intro": "Une douche qui ne s'évacue plus inonde vite la salle de bain. Bondes extra-plates, caniveaux de douche à l'italienne, siphons de sol : nous connaissons tous les systèmes et débouchons sans casser le carrelage ni les joints.",
   "signs": ["L'eau monte au-dessus du receveur pendant la douche", "Écoulement très lent", "Odeur d'égout qui remonte par la bonde", "L'eau d'un autre appareil ressort dans la douche"],
   "causes": ["Cheveux et poils mêlés au savon", "Bonde extra-plate trop étroite", "Calcaire dans le siphon", "Pente insuffisante d'une douche à l'italienne"],
   "method": [["Accès", "Ouverture de la bonde ou du caniveau, sans toucher au carrelage."], ["Extraction", "Retrait des cheveux et dépôts dans le siphon."], ["Furet", "Débouchage de la canalisation jusqu'à la colonne."], ["Test", "Douche à plein débit pendant plusieurs minutes."]],
   "tip": "En attendant : n'utilisez plus la douche, ni le lave-linge s'il est raccordé sur la même évacuation.",
   "faq": [["Combien coûte un débouchage de douche ?", "Le prix dépend du type d'intervention, de l'heure et du jour (soirée, week-end). Il vous est annoncé gratuitement par téléphone ou WhatsApp avant l'intervention, et c'est ce prix qui figure sur la facture."], ["Ma douche à l'italienne n'a pas de trappe, vous pouvez la déboucher ?", "Oui, nous passons par le caniveau ou la grille, sans casser le carrelage."], ["Pourquoi ma douche se rebouche-t-elle ?", "Souvent à cause de la pente ou d'un dépôt plus loin dans la canalisation. Une inspection caméra permet de le vérifier."]]
  },
  "nl": {
   "name": "Ontstopping douche",
   "card": "Overlopende douchebak of inloopdouche: ontstopt zonder tegels te breken.",
   "title": "Ontstopping douche 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Douche verstopt in Brussel of elders in België? Douchebak, inloopdouche of douchegoot: ontstopping zonder tegels te breken, 7/7. Gratis offerte. ☎ 0484 72 47 24",
   "h1": "Douche en inloopdouche ontstoppen in Brussel en heel België",
   "intro": "Een douche die niet meer afloopt, zet de badkamer snel onder water. Extra platte afvoerputjes, douchegoten, vloerputjes: we kennen alle systemen en ontstoppen zonder tegels of voegen te beschadigen.",
   "signs": ["Het water komt boven de douchebak tijdens het douchen", "Zeer trage afvoer", "Rioolgeur uit het afvoerputje", "Water van een ander toestel komt omhoog in de douche"],
   "causes": ["Haren vermengd met zeep", "Te smal extra plat putje", "Kalk in de sifon", "Onvoldoende helling bij een inloopdouche"],
   "method": [["Toegang", "Openen van het putje of de douchegoot, zonder aan de tegels te komen."], ["Verwijderen", "Haren en afzettingen uit de sifon halen."], ["Veer", "Ontstoppen van de leiding tot aan de kolom."], ["Test", "Enkele minuten douchen op vol debiet."]],
   "tip": "In afwachting: gebruik de douche niet meer, en ook de wasmachine niet als die op dezelfde afvoer zit.",
   "faq": [["Hoeveel kost een douche-ontstopping?", "De prijs hangt af van de situatie. Je krijgt hem gratis telefonisch of via WhatsApp vóór de interventie, en die prijs staat op de factuur."], ["Mijn inloopdouche heeft geen luik, kunnen jullie ze ontstoppen?", "Ja, we werken via de douchegoot of het rooster, zonder tegels te breken."], ["Waarom raakt mijn douche steeds opnieuw verstopt?", "Vaak door de helling of een afzetting verder in de leiding. Een camera-inspectie kan dat nagaan."]]
  }
 },
 {
  "id": "baignoire", "icon": "bath", "price": None, "slug": {"fr": "debouchage-baignoire", "nl": "ontstopping-bad"},
  "fr": {
   "name": "Débouchage baignoire",
   "card": "Eau stagnante vidée, évacuation dégagée, sans démonter le tablier.",
   "title": "Débouchage baignoire 7j/7 – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Baignoire bouchée à Bruxelles ou ailleurs en Belgique ? Évacuation dégagée, sans démonter le tablier carrelé, 7j/7. Devis gratuit : 0484 72 47 24",
   "h1": "Débouchage de baignoire à Bruxelles et partout en Belgique",
   "intro": "Une baignoire pleine d'eau qui ne se vide pas, ce sont des dizaines de litres bloqués dans la salle de bain. Nous dégageons l'évacuation par la bonde et le trop-plein, sans démonter le tablier carrelé.",
   "signs": ["La baignoire met des heures à se vider", "L'eau du lave-linge remonte dans la baignoire", "Bruits de glouglou dans la bonde", "Mauvaises odeurs"],
   "causes": ["Cheveux et savon dans le siphon", "Bonde automatique encrassée", "Dépôts de calcaire", "Bouchon dans la canalisation commune avec le lavabo"],
   "method": [["Vidange", "Évacuation de l'eau stagnante si nécessaire."], ["Bonde et trop-plein", "Nettoyage du mécanisme et du siphon."], ["Hydro-propulsion", "Dégagement de la canalisation par jet d'eau sous pression."], ["Test", "Remplissage et vidange complète de la baignoire."]],
   "tip": "En attendant : n'utilisez plus le lave-linge si son évacuation rejoint celle de la baignoire.",
   "faq": [["Faut-il casser le tablier de la baignoire ?", "Non, nous intervenons par la bonde et le trop-plein dans la très grande majorité des cas."], ["Combien coûte l'intervention ?", "Le prix vous est annoncé gratuitement avant le déplacement."], ["Intervenez-vous le week-end ?", "Oui, tous les jours de 6h à 21h."]]
  },
  "nl": {
   "name": "Ontstopping bad",
   "card": "Stilstaand water weg en afvoer vrij, zonder het badpaneel te demonteren.",
   "title": "Ontstopping bad 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Bad verstopt in Brussel of elders in België? Afvoer vrij, zonder het betegelde badpaneel te demonteren, 7/7. Gratis offerte: 0484 72 47 24",
   "h1": "Bad ontstoppen in Brussel en heel België",
   "intro": "Een vol bad dat niet leegloopt, betekent tientallen liters water die vastzitten in de badkamer. Wij maken de afvoer vrij via de afvoerplug en de overloop, zonder het betegelde badpaneel te demonteren.",
   "signs": ["Het bad loopt urenlang niet leeg", "Water van de wasmachine komt omhoog in het bad", "Borrelende geluiden in de afvoer", "Slechte geuren"],
   "causes": ["Haren en zeep in de sifon", "Vuile automatische afvoerplug", "Kalkafzetting", "Verstopping in de gemeenschappelijke leiding met de lavabo"],
   "method": [["Leegmaken", "Stilstaand water wegpompen indien nodig."], ["Plug en overloop", "Reinigen van het mechanisme en de sifon."], ["Hogedruk", "Leiding vrijmaken met een waterstraal onder druk."], ["Test", "Bad volledig vullen en laten leeglopen."]],
   "tip": "In afwachting: gebruik de wasmachine niet meer als die op dezelfde afvoer als het bad zit.",
   "faq": [["Moet het badpaneel afgebroken worden?", "Nee, in bijna alle gevallen werken we via de afvoerplug en de overloop."], ["Hoeveel kost de interventie?", "Je krijgt de prijs gratis vóór we vertrekken."], ["Komen jullie in het weekend?", "Ja, elke dag van 6 tot 21 uur."]]
  }
 },
 {
  "id": "cuisine", "icon": "pipes", "price": None, "slug": {"fr": "debouchage-cuisine", "nl": "ontstopping-keukenafvoer"},
  "fr": {
   "name": "Canalisations & colonnes",
   "card": "Évier et lave-vaisselle qui refoulent : curage complet des conduites.",
   "title": "Débouchage canalisation – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Canalisation ou colonne bouchée à Bruxelles ou ailleurs en Belgique ? Curage haute pression des conduites de cuisine et colonnes d'immeuble, 7j/7. ☎ 0484 72 47 24",
   "h1": "Débouchage de canalisations et colonnes à Bruxelles et partout en Belgique",
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
   "title": "Ontstopping leidingen 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Leiding of afvoerkolom verstopt in Brussel of elders in België? Hogedrukreiniging van keukenleidingen en gebouwkolommen, 7/7. ☎ 0484 72 47 24",
   "h1": "Leidingen en afvoerkolommen ontstoppen in Brussel en heel België",
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
   "card": "Refoulement en cave, chambre de visite pleine : hydrocurage haute pression.",
   "title": "Débouchage égout 7j/7 – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Égout bouché ou refoulement en cave à Bruxelles ou ailleurs en Belgique ? Camion hydrocureur, intervention 7j/7, facture pour l'assurance. ☎ 0484 72 47 24",
   "h1": "Débouchage d'égout et de chambre de visite à Bruxelles et partout en Belgique",
   "intro": "Un égout principal bouché menace toute la maison : refoulement d'eaux usées dans la cave, odeurs, risques sanitaires. Nos camions hydrocureurs haute pression dégagent racines, calcaire et bouchons massifs, et nous fournissons un rapport pour votre assurance.",
   "signs": ["Eaux usées qui remontent dans la cave ou le sous-sol", "Chambre de visite (regard) pleine ou qui déborde", "Tous les appareils de la maison s'écoulent mal", "Refoulements lors de fortes pluies"],
   "causes": ["Racines d'arbres entrées dans les joints", "Affaissement ou casse de la conduite", "Accumulation de graisse et de lingettes", "Siphon disconnecteur bouché"],
   "method": [["Ouverture du regard", "Accès à la chambre de visite et au siphon disconnecteur."], ["Hydrocurage haute pression", "Jet haute pression qui coupe les racines et dissout les dépôts."], ["Aspiration", "Pompage des boues et des eaux stagnantes."], ["Inspection", "Contrôle caméra si nécessaire, avec rapport."]],
   "tip": "En attendant : n'utilisez plus d'eau dans la maison (WC, douche, machines) et éloignez enfants et animaux de la cave.",
   "faq": [["L'assurance rembourse-t-elle un débouchage d'égout ?", "Souvent, en cas de dégât des eaux. Nous fournissons une facture avec n° TVA et un rapport technique."], ["Qu'est-ce qu'une chambre de visite ?", "C'est le regard d'accès à l'égout, souvent dans la cave ou le jardin, qui permet de déboucher la conduite principale."], ["Combien coûte un débouchage d'égout ?", "Le prix dépend de l'accès et de la gravité. Il est annoncé gratuitement avant l'intervention."]]
  },
  "nl": {
   "name": "Ontstopping riool",
   "card": "Terugslag in de kelder, volle inspectieput: hogedrukreiniging.",
   "title": "Ontstopping riool 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Riool verstopt of terugslag in de kelder in Brussel of elders in België? Hogedrukwagen, interventie 7/7, factuur voor de verzekering. ☎ 0484 72 47 24",
   "h1": "Riool en inspectieput ontstoppen in Brussel en heel België",
   "intro": "Een verstopte hoofdriolering bedreigt het hele huis: afvalwater in de kelder, geuren, gezondheidsrisico's. Onze hogedrukwagens verwijderen wortels, kalk en zware verstoppingen, en we leveren een verslag voor je verzekering.",
   "signs": ["Afvalwater komt omhoog in de kelder", "Inspectieput vol of overlopend", "Alle toestellen in huis lopen slecht af", "Terugslag bij hevige regen"],
   "causes": ["Boomwortels in de voegen", "Verzakte of gebroken leiding", "Ophoping van vet en doekjes", "Verstopte reukafsnijder (sifonput)"],
   "method": [["Put openen", "Toegang tot de inspectieput en de reukafsnijder."], ["Hogedrukreiniging", "Straal onder hoge druk die wortels snijdt en afzettingen oplost."], ["Afzuigen", "Wegpompen van slib en stilstaand water."], ["Inspectie", "Cameracontrole indien nodig, met verslag."]],
   "tip": "In afwachting: gebruik geen water meer in huis (wc, douche, machines) en hou kinderen en dieren uit de kelder.",
   "faq": [["Betaalt de verzekering een rioolontstopping terug?", "Vaak wel bij waterschade. Je krijgt een factuur met btw-nummer en een technisch verslag."], ["Wat is een inspectieput?", "Dat is de toegang tot de riolering, vaak in de kelder of tuin, waarlangs de hoofdleiding ontstopt wordt."], ["Hoeveel kost een rioolontstopping?", "De prijs hangt af van de toegang en de ernst. Je krijgt hem gratis vooraf."]]
  }
 },
 {
  "id": "fosse", "icon": "manhole", "price": None, "slug": {"fr": "vidange-fosse-septique", "nl": "septische-put-ledigen"},
  "fr": {
   "name": "Vidange fosse septique",
   "card": "Fosse septique pleine, odeurs, débordement : vidange par camion.",
   "title": "Vidange fosse septique 7j/7 – Belgique | ABS Débouchage",
   "desc": "Fosse septique pleine ou qui déborde ? Vidange et curage par camion, 7j/7 en Wallonie, Flandre et Bruxelles. Prix annoncé avant. ☎ 0484 72 47 24",
   "h1": "Vidange et curage de fosse septique",
   "intro": "Une fosse septique pleine fait remonter les eaux usées, sent mauvais et peut abîmer le système d'épuration. Nous venons avec un camion de vidange : aspiration des boues, curage des canalisations d'arrivée et contrôle de l'écoulement. Le prix est annoncé au téléphone avant le départ.",
   "signs": ["Odeurs d'égout autour de la maison ou dans le jardin", "WC et éviers qui s'écoulent lentement partout", "Eau ou boues qui remontent par le regard de la fosse", "Pas de vidange depuis plusieurs années"],
   "causes": ["Fosse pleine : boues et graisses accumulées", "Canalisation d'arrivée bouchée", "Lingettes et graisses envoyées dans les WC", "Préfiltre ou dégraisseur colmaté"],
   "method": [["Ouverture", "Repérage et ouverture du regard de la fosse."], ["Vidange", "Aspiration des boues et des eaux par camion."], ["Curage", "Débouchage des canalisations d'arrivée et de sortie si besoin."], ["Contrôle", "Test d'écoulement et conseils d'entretien, facture remise sur place."]],
   "tip": "En attendant : limitez l'eau (pas de lave-linge ni de bain) et ne jetez rien d'autre que du papier toilette dans les WC.",
   "faq": [["Combien coûte une vidange de fosse septique ?", "Le prix dépend du volume de la fosse, de l'accès pour le camion et de la distance. Il vous est annoncé au téléphone avant le départ, et c'est ce prix qui figure sur la facture."], ["Tous les combien faut-il vider une fosse septique ?", "En général tous les 3 à 4 ans pour une famille, plus souvent si la fosse est petite ou très utilisée. Des odeurs ou un écoulement lent sont le signe qu'elle est pleine."], ["Le camion doit-il pouvoir accéder au jardin ?", "Le camion reste dans la rue ou l'allée, et le tuyau d'aspiration va jusqu'à la fosse. Dites-nous au téléphone à quelle distance elle se trouve."]]
  },
  "nl": {
   "name": "Septische put ledigen",
   "card": "Volle septische put, geurtjes, overlopen: ledigen met de wagen.",
   "title": "Septische put ledigen 7/7 – België | ABS Débouchage",
   "desc": "Septische put vol of loopt hij over? Ledigen en ruimen met de wagen, 7/7 in Vlaanderen, Wallonië en Brussel. Prijs vooraf. ☎ 0484 72 47 24",
   "h1": "Septische put ledigen en ruimen",
   "intro": "Een volle septische put laat afvalwater terugkomen, ruikt slecht en kan je zuiveringssysteem beschadigen. We komen met een ledigingswagen: slib afzuigen, aanvoerleidingen ruimen en de afvoer controleren. Je krijgt de prijs aan de telefoon voor we vertrekken.",
   "signs": ["Rioolgeur rond het huis of in de tuin", "Wc's en gootstenen lopen overal traag af", "Water of slib komt omhoog langs het putdeksel", "Al jaren niet meer geledigd"],
   "causes": ["Volle put: slib en vet opgehoopt", "Verstopte aanvoerleiding", "Doekjes en vet in de wc", "Verstopte voorfilter of vetvanger"],
   "method": [["Openen", "Put opzoeken en deksel openen."], ["Ledigen", "Slib en water wegzuigen met de wagen."], ["Ruimen", "Aanvoer- en afvoerleidingen ontstoppen indien nodig."], ["Controle", "Afvoertest en onderhoudstips, factuur ter plaatse."]],
   "tip": "In afwachting: gebruik zo weinig mogelijk water (geen wasmachine of bad) en spoel enkel wc-papier door.",
   "faq": [["Hoeveel kost het ledigen van een septische put?", "De prijs hangt af van het volume, de toegang voor de wagen en de afstand. Je krijgt hem aan de telefoon voor we vertrekken, en die prijs staat op de factuur."], ["Hoe vaak moet een septische put geledigd worden?", "Meestal om de 3 tot 4 jaar voor een gezin, vaker bij een kleine of intensief gebruikte put. Geurtjes of trage afvoer betekenen dat hij vol is."], ["Moet de wagen tot in de tuin kunnen?", "De wagen blijft op straat of de oprit, de zuigslang gaat tot aan de put. Zeg ons aan de telefoon hoe ver de put ligt."]]
  }
 },
 {
  "id": "siphon", "icon": "drain", "price": None, "slug": {"fr": "debouchage-siphon", "nl": "ontstopping-afvoerputje"},
  "fr": {
   "name": "Siphon de sol",
   "card": "Garage, buanderie, cour : curage et aspiration des boues.",
   "title": "Débouchage siphon de sol – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Siphon de sol bouché à Bruxelles ou ailleurs en Belgique (garage, cave, buanderie, cour) ? Curage et aspiration des boues 7j/7, devis gratuit. ☎ 0484 72 47 24",
   "h1": "Débouchage de siphon de sol à Bruxelles et partout en Belgique",
   "intro": "Les siphons de sol des garages, caves, buanderies et cours piègent sable, feuilles et résidus de lessive. Quand ils se bouchent, l'eau stagne ou remonte à chaque orage. Nous les curons, aspirons les boues et les désinfectons.",
   "signs": ["Flaque permanente autour du siphon", "Refoulement lors des fortes pluies", "Odeur d'égout dans le garage ou la cave", "L'eau du lave-linge déborde du siphon"],
   "causes": ["Sable, terre et feuilles", "Peluches et résidus de lessive", "Grille absente ou cassée", "Bouchon dans la conduite vers l'égout"],
   "method": [["Ouverture", "Retrait de la grille et du panier."], ["Aspiration", "Pompage des boues et sédiments."], ["Curage", "Débouchage de la conduite jusqu'à l'égout."], ["Désinfection", "Nettoyage et remise en place de la grille."]],
   "tip": "En attendant : n'utilisez plus le lave-linge s'il se vide dans ce siphon.",
   "faq": [["Combien coûte un débouchage de siphon de sol ?", "Le prix dépend du type d'intervention, de l'heure et du jour (soirée, week-end). Il vous est annoncé gratuitement par téléphone ou WhatsApp avant l'intervention, et c'est ce prix qui figure sur la facture."], ["Mon siphon déborde à chaque orage, pourquoi ?", "La conduite vers l'égout est souvent partiellement bouchée. Un curage, voire une inspection caméra, règle le problème."], ["Intervenez-vous pour les commerces ?", "Oui, garages, ateliers et commerces, 7j/7."]]
  },
  "nl": {
   "name": "Vloerputje",
   "card": "Garage, wasruimte, koer: reiniging en afzuigen van slib.",
   "title": "Ontstopping afvoerputje 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Vloerputje verstopt in Brussel of elders in België (garage, kelder, wasruimte, koer)? Reiniging en afzuigen van slib 7/7, gratis offerte. ☎ 0484 72 47 24",
   "h1": "Vloerputje en afvoerputje ontstoppen in Brussel en heel België",
   "intro": "Vloerputjes in garages, kelders, wasruimtes en koeren houden zand, bladeren en wasresten vast. Als ze verstopt raken, blijft het water staan of komt het bij elk onweer omhoog. Wij reinigen ze, zuigen het slib af en ontsmetten ze.",
   "signs": ["Permanente plas rond het putje", "Terugslag bij hevige regen", "Rioolgeur in garage of kelder", "Water van de wasmachine loopt over"],
   "causes": ["Zand, aarde en bladeren", "Pluisjes en wasresten", "Ontbrekend of kapot rooster", "Verstopping in de leiding naar de riool"],
   "method": [["Openen", "Rooster en korf verwijderen."], ["Afzuigen", "Slib en sediment wegpompen."], ["Reinigen", "Leiding ontstoppen tot aan de riool."], ["Ontsmetten", "Reinigen en rooster terugplaatsen."]],
   "tip": "In afwachting: gebruik de wasmachine niet meer als die in dit putje loost.",
   "faq": [["Hoeveel kost een vloerputje ontstoppen?", "De prijs hangt af van de situatie. Je krijgt hem gratis telefonisch of via WhatsApp vóór de interventie, en die prijs staat op de factuur."], ["Mijn putje loopt over bij elk onweer, waarom?", "De leiding naar de riool is vaak deels verstopt. Een reiniging of camera-inspectie lost het op."], ["Komen jullie ook voor handelszaken?", "Ja, garages, werkplaatsen en winkels, 7/7."]]
  }
 },
 {
  "id": "camera", "icon": "camera", "price": None, "slug": {"fr": "inspection-camera", "nl": "camera-inspectie"},
  "fr": {
   "name": "Inspection caméra",
   "card": "Bouchons à répétition ? On trouve la cause, avec rapport vidéo.",
   "title": "Inspection caméra – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Inspection caméra HD des canalisations à Bruxelles et dans toute la Belgique : racines, fissures et contre-pentes localisées, rapport vidéo pour l'assurance.",
   "h1": "Inspection caméra des canalisations à Bruxelles et partout en Belgique",
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
   "title": "Camera-inspectie riolering – Brussel & België | ABS Débouchage",
   "desc": "HD-camera-inspectie van je leidingen in Brussel en heel België: wortels, scheuren en tegenhellingen op de centimeter gelokaliseerd, videorapport voor de verzekering.",
   "h1": "Camera-inspectie van leidingen in Brussel en heel België",
   "intro": "Steeds terugkerende verstoppingen, onverklaarbare geuren, vocht in een muur? Onze draaibare HD-camera gaat in je leidingen, lokaliseert het probleem tot op de centimeter en neemt alles op video op. Je krijgt een verslag dat geldig is voor verzekering, syndicus of notaris.",
   "signs": ["Steeds verstopt op dezelfde plaats", "Onverklaarbaar vocht in muur of vloer", "Aanhoudende geuren ondanks ontstoppingen", "Aankoop of verkoop van een woning"],
   "causes": ["Wortels in de voegen", "Gescheurde, gebroken of verzakte leiding", "Tegenhelling die water vasthoudt", "Slecht uitgevoerde aansluiting"],
   "method": [["Inbrengen", "Draaibare HD-camera 360° via een put of sifon."], ["Lokaliseren", "Radiosonde om het exacte punt vanaf de oppervlakte te vinden."], ["Opnemen", "Volledige video van het traject van de leiding."], ["Verslag", "Schriftelijk verslag met vaststellingen en aanbevelingen."]],
   "tip": "Tip: laat de leidingen inspecteren voor je een oud huis koopt. Zo vermijd je dure verrassingen.",
   "faq": [["Waarvoor dient een camera-inspectie?", "Om de binnenkant van de leidingen te zien zonder breekwerk, de exacte oorzaak te vinden en onnodige werken te vermijden."], ["Aanvaarden verzekeraars het verslag?", "Ja, het video- en schriftelijk verslag dient als bewijs voor je verzekeringsdossier of syndicus."], ["Hoeveel kost een camera-inspectie?", "De prijs hangt af van de te inspecteren lengte. Je krijgt hem gratis vooraf."]]
  }
 },
 {
  "id": "plomberie", "icon": "wrench", "price": None, "slug": {"fr": "plomberie", "nl": "loodgieterij"},
  "fr": {
   "name": "Plomberie",
   "card": "Fuite, robinetterie, sanitaires, chauffe-eau : un plombier à Bruxelles, 7j/7, sur devis.",
   "title": "Plombier 7j/7 – Bruxelles & Belgique | ABS Débouchage",
   "desc": "Plombier à Bruxelles et en Belgique, disponible 7j/7 : fuite d'eau, robinetterie, sanitaires, chauffe-eau, canalisations. Devis gratuit avant les travaux.",
   "h1": "Plombier à Bruxelles et partout en Belgique, 7j/7",
   "intro": "Dépannage, réparation, remplacement et installation, 7j/7 à Bruxelles et dans toute la Belgique. Devis gratuit avant les travaux.",
   "signs": ["Une fuite d'eau visible ou une tache d'humidité qui s'étend", "Un robinet ou une chasse d'eau qui coule en continu", "Plus d'eau chaude, ou une pression d'eau qui chute", "Des bruits ou des coups dans les canalisations"],
   "causes": ["Joints, flexibles ou raccords usés par le temps", "Calcaire qui bloque la robinetterie et les appareils", "Installation ancienne ou mal posée", "Gel ou variation de pression qui fragilise un tuyau"],
   "method": [["Diagnostic", "On cherche l'origine du problème et on coupe l'eau si nécessaire pour limiter les dégâts."], ["Devis gratuit", "Le prix vous est annoncé avant les travaux : pas de surprise sur la facture."], ["Réparation", "Réparation, remplacement ou installation, avec du matériel professionnel."], ["Contrôle", "On teste l'installation avant de partir et on vous explique ce qui a été fait."]],
   "tip": "En attendant le technicien : fermez l'arrivée d'eau (robinet d'arrêt ou compteur), coupez le courant si l'eau approche d'une prise ou du tableau électrique, et épongez pour limiter les dégâts.",
   "faq": [["Faites-vous aussi de la plomberie ?", "Oui. En plus du débouchage, nous intervenons pour vos besoins de plomberie : dépannage, réparation, remplacement et installation."], ["Intervenez-vous en urgence et le week-end ?", "Oui, tous les jours de 6h à 21h, dans les mêmes zones que le débouchage : Bruxelles et toute la Belgique."], ["Comment est calculé le prix ?", "Toujours sur devis gratuit, annoncé avant l'intervention. Décrivez la situation par téléphone ou WhatsApp : on vous répond avec un prix, et c'est ce prix qui figure sur la facture."],
           ["Que faire en cas de fuite d'eau en attendant le plombier ?", "Fermez l'arrivée d'eau au robinet d'arrêt ou au compteur, coupez le courant si l'eau approche d'une prise ou du tableau électrique, puis épongez. Prenez quelques photos des dégâts : elles serviront pour votre assurance."],
           ["Je suis locataire : qui paie le plombier ?", "En règle générale, les petites réparations d'usage (joint, flexible, mécanisme de chasse) sont à charge du locataire, et les grosses réparations ou le remplacement d'une installation vétuste à charge du propriétaire. Vérifiez votre bail et prévenez votre propriétaire avant les travaux, sauf urgence."],
           ["Mon assurance couvre-t-elle une fuite d'eau ?", "Le plus souvent, l'assurance habitation couvre les dégâts causés par l'eau (sol, murs, plafond), pas la réparation de la pièce défectueuse. Certains contrats prennent aussi en charge la recherche de fuite. Vous recevez une facture avec numéro de TVA à joindre à votre déclaration."],
           ["Vaut-il mieux réparer ou remplacer ?", "On répare quand la réparation tient dans le temps : un joint, une cartouche ou un mécanisme suffisent souvent. Quand la pièce est trop usée ou que la réparation coûterait presque autant, on vous le dit et on vous propose le remplacement. Dans les deux cas, vous connaissez le prix avant qu'on commence."],
           ["Intervenez-vous dans toutes les communes de Bruxelles ?", "Oui : Anderlecht, Bruxelles-Ville, Ixelles, Molenbeek-Saint-Jean, Schaerbeek, Uccle et les autres communes de la Région, ainsi qu'en Wallonie et en Flandre."]],
   "details": [
    ["fuites", "Fuites d'eau", "Une fuite ne s'arrête jamais toute seule : même un simple goutte-à-goutte finit par abîmer un mur, un plafond ou un meuble. Nous cherchons d'où vient l'eau (joint, raccord, flexible, tuyau percé), nous coupons l'arrivée si nécessaire, puis nous réparons ou remplaçons la pièce en cause.",
     ["Fuite sous un évier, un lavabo ou une baignoire", "Raccord qui suinte ou tuyau percé", "Tache d'humidité sur un mur ou un plafond", "Compteur d'eau qui tourne, robinets fermés"]],
    ["robinetterie", "Robinetterie", "Un robinet qui goutte gaspille de l'eau jour et nuit, et un mitigeur qui force finit par casser. Selon l'état, nous changeons le joint ou la cartouche, ou nous remplaçons le robinet complet, avec votre accord et après devis.",
     ["Robinet qui goutte ou qui fuit à la base", "Mitigeur dur, bloqué ou qui ne mélange plus", "Robinet d'arrêt grippé ou qui ne ferme plus", "Flexible ou pommeau de douche à remplacer"]],
    ["sanitaires", "Sanitaires & WC", "Une chasse d'eau qui coule en continu ou un WC qui fuit au pied se réparent le plus souvent sans tout changer. Nous remplaçons le mécanisme, le flotteur ou le joint, et nous posons de nouveaux sanitaires quand la réparation ne suffit plus.",
     ["Chasse d'eau qui coule ou qui ne se remplit plus", "WC qui fuit au sol ou au raccord", "Lavabo, évier ou bidet à reposer ou à remplacer", "Siphon ou bonde qui fuit"]],
    ["chauffe-eau", "Chauffe-eau & pression", "Plus d'eau chaude, une eau seulement tiède ou une pression qui s'effondre : nous contrôlons le chauffe-eau, le groupe de sécurité et le réducteur de pression pour trouver la panne, puis nous vous disons s'il vaut mieux réparer ou remplacer.",
     ["Plus d'eau chaude, ou eau seulement tiède", "Groupe de sécurité qui goutte en permanence", "Pression trop faible à tous les robinets", "Coups ou sifflements dans les tuyaux"]],
    ["canalisations", "Canalisations", "Les tuyaux d'arrivée d'eau et d'évacuation vieillissent : corrosion, raccords fatigués, tronçons abîmés lors de travaux. Nous réparons la partie touchée ou nous la remplaçons, et nous vérifions l'étanchéité avant de refermer.",
     ["Tuyau corrodé, fissuré ou percé", "Raccord ou soudure qui fuit", "Remplacement d'un tronçon d'alimentation ou d'évacuation", "Évacuation mal raccordée ou en contre-pente"]],
    ["installation", "Installation & remplacement", "Nouvelle cuisine, salle de bain à rafraîchir ou appareil à raccorder : nous posons et raccordons vos équipements, puis nous testons l'installation avec vous avant de partir.",
     ["Pose d'un robinet, d'un lavabo, d'un évier ou d'un WC", "Raccordement d'un lave-linge ou d'un lave-vaisselle", "Remplacement d'un chauffe-eau", "Remise en état lors d'une rénovation"]]]
  },
  "nl": {
   "name": "Loodgieterij",
   "card": "Lek, kranen, sanitair, boiler: een loodgieter in Brussel, 7/7, op offerte.",
   "title": "Loodgieter 7/7 – Brussel & België | ABS Débouchage",
   "desc": "Loodgieter in Brussel en heel België, 7/7 beschikbaar: waterlek, kranen, sanitair, boiler, leidingen. Gratis offerte vóór de werken.",
   "h1": "Loodgieter in Brussel en heel België, 7/7",
   "intro": "Noodhulp, herstelling, vervanging en installatie, 7/7 in Brussel en heel België. Gratis offerte vóór de werken.",
   "signs": ["Een zichtbaar lek of een vochtplek die groter wordt", "Een kraan of spoelbak die blijft lopen", "Geen warm water meer, of een dalende waterdruk", "Geluiden of slagen in de leidingen"],
   "causes": ["Voegen, flexibels of koppelingen die versleten zijn", "Kalk die kranen en toestellen blokkeert", "Oude of slecht geplaatste installatie", "Vorst of drukschommelingen die een leiding verzwakken"],
   "method": [["Diagnose", "We zoeken de oorzaak en sluiten indien nodig het water af om schade te beperken."], ["Gratis offerte", "U kent de prijs vóór de werken: geen verrassingen op de factuur."], ["Herstelling", "Herstelling, vervanging of installatie, met professioneel materiaal."], ["Controle", "We testen de installatie voor we vertrekken en leggen uit wat er gedaan is."]],
   "tip": "In afwachting van de technieker: sluit de watertoevoer af (afsluitkraan of meter), schakel de stroom uit als er water bij een stopcontact of de elektrische kast komt, en dweil om de schade te beperken.",
   "faq": [["Doen jullie ook loodgieterswerk?", "Ja. Naast ontstopping doen we ook loodgieterswerk: noodhulp, herstelling, vervanging en installatie."], ["Komen jullie ook in het weekend?", "Ja, elke dag van 6 tot 21 uur, in dezelfde regio als de ontstopping: Brussel en heel België."], ["Hoe wordt de prijs berekend?", "Altijd op gratis offerte, vooraf meegedeeld. Beschrijf de situatie telefonisch of via WhatsApp: je krijgt een prijs, en die prijs staat op de factuur."],
           ["Wat doe ik bij een waterlek in afwachting van de loodgieter?", "Sluit de watertoevoer af aan de afsluitkraan of de meter, schakel de stroom uit als er water bij een stopcontact of de elektrische kast komt, en dweil het water op. Neem enkele foto's van de schade: die zijn nuttig voor je verzekering."],
           ["Ik ben huurder: wie betaalt de loodgieter?", "In de regel zijn kleine herstellingen door gebruik (dichting, flexibel, spoelmechanisme) voor de huurder, en grote herstellingen of de vervanging van een verouderde installatie voor de eigenaar. Kijk je huurcontract na en verwittig je eigenaar vóór de werken, behalve bij nood."],
           ["Dekt mijn verzekering een waterlek?", "Meestal dekt de woonverzekering de schade door het water (vloer, muren, plafond), niet de herstelling van het defecte onderdeel. Sommige contracten vergoeden ook de lekopsporing. Je krijgt een factuur met btw-nummer voor je aangifte."],
           ["Herstellen of vervangen: wat is het beste?", "We herstellen wanneer de herstelling duurzaam is: een dichting, een cartouche of een mechanisme volstaat vaak. Is het onderdeel te versleten of kost herstellen bijna evenveel, dan zeggen we dat en stellen we vervanging voor. In beide gevallen ken je de prijs voor we beginnen."],
           ["Komen jullie in alle Brusselse gemeenten?", "Ja: Anderlecht, Brussel-Stad, Elsene, Sint-Jans-Molenbeek, Schaarbeek, Ukkel en de andere gemeenten van het Gewest, en ook in Wallonië en Vlaanderen."]],
   "details": [
    ["lekken", "Waterlekken", "Een lek stopt nooit vanzelf: zelfs wat gedruppel beschadigt op termijn een muur, een plafond of een meubel. We zoeken waar het water vandaan komt (dichting, koppeling, flexibel, doorboorde leiding), sluiten indien nodig de toevoer af en herstellen of vervangen het defecte onderdeel.",
     ["Lek onder een gootsteen, lavabo of bad", "Koppeling die zweet of doorboorde leiding", "Vochtplek op een muur of plafond", "Watermeter die draait terwijl alle kranen dicht zijn"]],
    ["kranen", "Kranen", "Een druppelende kraan verspilt dag en nacht water, en een mengkraan die klemt, gaat uiteindelijk stuk. Naargelang de staat vervangen we de dichting of de cartouche, of de volledige kraan, met jouw akkoord en na offerte.",
     ["Kraan die druppelt of lekt aan de voet", "Mengkraan die klemt, vastzit of niet meer mengt", "Afsluitkraan die vastzit of niet meer sluit", "Doucheslang of douchekop vervangen"]],
    ["sanitair", "Sanitair & wc", "Een spoelbak die blijft lopen of een wc die lekt aan de voet is meestal te herstellen zonder alles te vervangen. We vervangen het mechanisme, de vlotter of de dichting, en plaatsen nieuw sanitair als herstellen niet meer volstaat.",
     ["Spoelbak die blijft lopen of niet meer vult", "Wc die lekt op de vloer of aan de aansluiting", "Lavabo, gootsteen of bidet herplaatsen of vervangen", "Sifon of afvoerplug die lekt"]],
    ["boiler", "Boiler & waterdruk", "Geen warm water meer, alleen lauw water of een druk die wegvalt: we controleren de boiler, de veiligheidsgroep en de drukregelaar om de oorzaak te vinden, en zeggen je daarna of herstellen of vervangen het beste is.",
     ["Geen warm water, of alleen lauw water", "Veiligheidsgroep die voortdurend druppelt", "Te lage druk aan alle kranen", "Slagen of gefluit in de leidingen"]],
    ["leidingen", "Leidingen", "Aanvoer- en afvoerleidingen verouderen: corrosie, vermoeide koppelingen, stukken die bij werken beschadigd raakten. We herstellen het getroffen deel of vervangen het, en controleren de dichtheid voor we alles weer sluiten.",
     ["Leiding die verroest, gebarsten of doorboord is", "Koppeling of las die lekt", "Vervanging van een stuk aanvoer- of afvoerleiding", "Afvoer die slecht is aangesloten of geen afschot heeft"]],
    ["installatie", "Installatie & vervanging", "Nieuwe keuken, badkamer opfrissen of een toestel aansluiten: we plaatsen en sluiten je toestellen aan, en testen de installatie samen met jou voor we vertrekken.",
     ["Plaatsing van een kraan, lavabo, gootsteen of wc", "Aansluiting van een wasmachine of vaatwasser", "Vervanging van een boiler", "Herstelling bij een renovatie"]]]
  }
 },
]

# --------------------------------------------------------------------------
# TEXTES COMMUNS (interface)
# --------------------------------------------------------------------------
UI = {
 "fr": {
  "lang_name": "Français", "other": "nl", "other_label": "NL",
  "brand_sub": "Débouchage & plomberie · Belgique",
  "top": "Techniciens disponibles 7j/7 · 6h–21h",
  "nav_services": "Services", "nav_prices": "Tarifs", "nav_zones": "Zones", "nav_about": "À propos", "nav_contact": "Contact", "nav_all": "Tous nos services",
  "call": "Appeler", "call_now": "Appeler maintenant", "wa_quote": "Devis gratuit WhatsApp", "menu": "Menu",
  "chk": ["Devis gratuit", "Prix annoncé avant", "Garantie sur l'intervention", "Facture pour l'assurance", "5,0 sur Google · 8 avis"],
  "from": "dès", "on_quote": "Devis gratuit", "learn": "En savoir plus",
  "home": "Accueil",
  # Devis
  "q_kick": "Devis express", "q_title": "Votre devis sur WhatsApp en 1 minute",
  "q_lead": "Répondez à 4 questions : votre demande arrive sur notre WhatsApp, déjà complète. On vous répond tout de suite avec un prix.",
  "q_steps": ["Choisissez votre problème et votre commune.", "WhatsApp s'ouvre avec le message déjà écrit : appuyez sur « Envoyer ».", "Ajoutez une photo si possible, on vous répond avec le prix."],
  "f_prob": "Quel est le problème ?", "f_urg": "C'est urgent ?", "u": {"now": "Oui, maintenant", "today": "Aujourd'hui", "plan": "À planifier"},
  "f_where": "Commune ou code postal", "ph_where": "ex. 1050 Ixelles", "f_name": "Votre prénom", "ph_name": "ex. Marc",
  "f_desc": "Détails (facultatif)", "ph_desc": "ex. L'eau remonte dans la douche depuis ce matin, 2e étage.",
  "other_pb": "Autre", "err": "Choisissez un problème et indiquez votre commune.",
  "send": "Envoyer ma demande sur WhatsApp", "note": "Gratuit et sans engagement",
  "wa": {"hello": "Bonjour ABS Débouchage, je souhaite un devis.", "prob": "Problème", "urg": "Urgence", "where": "Commune", "name": "Nom", "det": "Détails",
         "urgv": {"now": "URGENT – maintenant", "today": "Aujourd'hui", "plan": "À planifier"}},
  # Accueil
  "home_title": "Débouchage 7j/7 Bruxelles, Wallonie, Flandre | ABS Débouchage",
  "home_desc": "Débouchage WC, évier, douche, égout et plomberie à Bruxelles, en Wallonie et en Flandre. Urgence 7j/7, prix annoncé avant. ☎ 0484 72 47 24",
  "hero_pill": "Urgence débouchage à Bruxelles",
  "hero_h1": "Débouchage à Bruxelles, <em>rapidement sur place</em>, 7j/7.",
  "hero_lead": "WC, évier, douche, égout à Bruxelles : un technicien équipé part dès votre appel, tous les jours de 6h à 21h. Prix annoncé avant de commencer, intervention propre et sans casse.",
  "eta_title": "Exemple d'intervention", "eta_status": "Technicien en route", "eta_time": "Arrivée estimée", "eta_min": "min",
  "eta_steps": ["Appel reçu", "Prix confirmé", "En route", "Débouché"],
  "trust": [["clock", "6h–21h", "Tous les jours, week-end compris"], ["euro", "0 €", "Devis et déplacement annoncé"], ["shield", "Assurances", "Facture et rapport acceptés"], ["gauge", "Hydrocureur", "Haute pression professionnelle"]],
  "s_kick": "Nos interventions", "s_title": "Tous les bouchons, toutes les canalisations",
  "s_lead": "Du simple lavabo à l'égout principal, nous avons le bon matériel pour déboucher sans casser.",
  "w_kick": "Pourquoi ABS", "w_title": "Rapide, honnête, efficace",
  "why": [["clock", "Départ dès votre appel", "Au téléphone, on vous donne l'heure d'arrivée estimée avant de partir."], ["euro", "Prix annoncé avant", "Le prix est fixé au téléphone. Aucun travail ne commence sans votre accord."], ["gauge", "Matériel pro", "Furet électrique, hydrocureur haute pression et caméra : on débouche sans abîmer vos tuyaux."], ["file", "Dossier assurance", "Facture officielle avec n° TVA et rapport technique pour votre remboursement."]],
  "h_kick": "Simple et rapide", "h_title": "Comment ça se passe ?",
  "how": [["Vous nous contactez", "Par téléphone ou WhatsApp, 7j/7. Décrivez le problème, on vous donne un prix."], ["Le technicien arrive", "Rapidement, avec tout le matériel nécessaire."], ["C'est débouché", "Test d'écoulement, nettoyage de la zone, facture remise sur place."]],
  "p_kick": "Tarifs transparents", "p_title": "Des prix clairs, sans surprise",
  "p_lead": "Le prix exact est confirmé avant l'intervention. Ce qui est annoncé est ce que vous payez.",
  "badge": "Le plus demandé", "from_long": "à partir de", "price_lbl": "prix",
  "plans": [["Débouchage sanitaire", None, ["WC, évier, lavabo, douche, siphon", "Furet électrique professionnel", "Test d'écoulement après travaux"]], ["Égout, fosse & haute pression", None, ["Égout, colonne, chambre de visite", "Vidange de fosse septique par camion", "Camion hydrocureur haute pression"]], ["Inspection caméra", None, ["Caméra HD rotative 360°", "Localisation au centimètre", "Rapport vidéo pour assurance ou syndic"]]],
  "ask_price": "Demander le prix", "p_note": "Devis gratuit et sans engagement : le prix exact vous est annoncé avant toute intervention.",
  "z_kick": "Zone d'intervention", "z_title": "Partout en Belgique",
  "z_lead": "Nous intervenons partout en Belgique, 7j/7 : à Bruxelles, en Wallonie et en Flandre.",
  "z_peri": "Périphérie",
  "f_kick": "FAQ", "f_title": "Questions fréquentes",
  "faq": [["En combien de temps arrivez-vous ?", "Le plus vite possible, tous les jours de 6h à 21h. Au téléphone, on vous donne une estimation de l'heure d'arrivée selon votre commune."], ["Combien coûte un débouchage à Bruxelles ?", "Le prix dépend du type d'intervention, de l'heure et du jour (soirée, week-end). Il vous est annoncé gratuitement par téléphone ou WhatsApp avant l'intervention, et c'est ce prix qui figure sur la facture."], ["Quels sont vos horaires ?", "Tous les jours, de 6h à 21h, week-end compris."], ["Mon assurance peut-elle rembourser ?", "Souvent oui, surtout en cas de dégât des eaux. Nous fournissons une facture officielle avec n° TVA et un rapport technique."], ["Que faire en attendant le technicien ?", "Arrêtez d'utiliser l'eau (chasse, lave-linge, lave-vaisselle), coupez l'arrivée d'eau si ça déborde et évitez les produits chimiques corrosifs."], ["Utilisez-vous des produits chimiques ?", "Non. Nous travaillons mécaniquement (furet, haute pression), sans produits corrosifs pour vos tuyaux ni pour l'environnement."]],
  "fin_title": "Un bouchon ? N'attendez pas que ça déborde.",
  "fin_lead": "Un seul appel : on écoute votre problème, on vous donne le prix et un technicien part chez vous, tous les jours de 6h à 21h.",
  # Pages service
  "sv_signs": "Les signes qui ne trompent pas", "sv_causes": "Les causes les plus fréquentes",
  "sv_method": "Notre méthode d'intervention", "sv_price": "Tarif", "sv_price_free": "Prix annoncé gratuitement avant l'intervention",
  "sv_tip": "En attendant le technicien", "sv_faq": "Questions fréquentes", "sv_other": "Nos autres services",
  "sv_zone": "Intervention à Bruxelles et dans toute la Belgique",
  # Footer
  "foot_about": "Débouchage d'urgence, hydrocurage et inspection caméra pour particuliers, syndics et entreprises, à Bruxelles et dans toute la Belgique.",
  "foot_hours": "Ouvert 7j/7 · 6h–21h", "foot_info": "Informations", "foot_services": "Services",
  "vat": "TVA", "insured": "Facture et rapport pour votre assurance", "rights": "Tous droits réservés", "privacy": "Confidentialité",
  # Pages
  "about_slug": "a-propos", "contact_slug": "contact", "privacy_slug": "politique-de-confidentialite",
  "notfound": "Page introuvable", "notfound_lead": "Cette page n'existe pas ou a été déplacée. Besoin d'un débouchage ? On est là 7j/7, de 6h à 21h.",
 },
 "nl": {
  "lang_name": "Nederlands", "other": "fr", "other_label": "FR",
  "brand_sub": "Ontstopping & loodgieterij · België",
  "top": "Techniekers beschikbaar 7/7 · 6–21 uur",
  "nav_services": "Diensten", "nav_prices": "Prijzen", "nav_zones": "Regio", "nav_about": "Over ons", "nav_contact": "Contact", "nav_all": "Al onze diensten",
  "call": "Bellen", "call_now": "Nu bellen", "wa_quote": "Gratis offerte via WhatsApp", "menu": "Menu",
  "chk": ["Gratis offerte", "Prijs vooraf", "Factuur voor je verzekering"],
  "from": "vanaf", "on_quote": "Gratis offerte", "learn": "Meer info",
  "home": "Home",
  "q_kick": "Snelle offerte", "q_title": "Je offerte via WhatsApp in 1 minuut",
  "q_lead": "Beantwoord 4 vragen: je aanvraag komt volledig ingevuld op onze WhatsApp. We antwoorden meteen met een prijs.",
  "q_steps": ["Kies je probleem en je gemeente.", "WhatsApp opent met het bericht al ingevuld: druk op « Verzenden ».", "Voeg indien mogelijk een foto toe, we antwoorden met de prijs."],
  "f_prob": "Wat is het probleem?", "f_urg": "Is het dringend?", "u": {"now": "Ja, nu", "today": "Vandaag", "plan": "In te plannen"},
  "f_where": "Gemeente of postcode", "ph_where": "bv. 1050 Elsene", "f_name": "Je voornaam", "ph_name": "bv. Marc",
  "f_desc": "Details (optioneel)", "ph_desc": "bv. Het water komt sinds vanochtend omhoog in de douche, 2e verdieping.",
  "other_pb": "Andere", "err": "Kies een probleem en vul je gemeente in.",
  "send": "Mijn aanvraag via WhatsApp versturen", "note": "Gratis en vrijblijvend",
  "wa": {"hello": "Hallo ABS Débouchage, ik wil graag een offerte.", "prob": "Probleem", "urg": "Dringend", "where": "Gemeente", "name": "Naam", "det": "Details",
         "urgv": {"now": "DRINGEND – nu", "today": "Vandaag", "plan": "In te plannen"}},
  "home_title": "Ontstopping 7/7 Brussel, Vlaanderen, Wallonië | ABS Débouchage",
  "home_desc": "Ontstopping wc, gootsteen, douche, riool en loodgieterij in Brussel, Vlaanderen en Wallonië. Spoed 7/7, prijs vooraf gekend. ☎ 0484 72 47 24",
  "hero_pill": "Spoedontstopping in Brussel",
  "hero_h1": "Ontstopping in Brussel, <em>snel</em> ter plaatse, 7 dagen op 7.",
  "hero_lead": "Wc, gootsteen, douche, riool in Brussel: een uitgeruste technieker vertrekt meteen na je oproep, elke dag van 6 tot 21 uur. Prijs vooraf gekend, propere interventie zonder breekwerk.",
  "eta_title": "Voorbeeld van een interventie", "eta_status": "Technieker onderweg", "eta_time": "Verwachte aankomst", "eta_min": "min",
  "eta_steps": ["Oproep ontvangen", "Prijs bevestigd", "Onderweg", "Ontstopt"],
  "trust": [["clock", "6–21 uur", "Elke dag, ook in het weekend"], ["euro", "0 €", "Offerte vooraf gekend"], ["shield", "Verzekering", "Factuur en verslag aanvaard"], ["gauge", "Hogedruk", "Professionele hogedrukwagen"]],
  "s_kick": "Onze interventies", "s_title": "Alle verstoppingen, alle leidingen",
  "s_lead": "Van een eenvoudige lavabo tot de hoofdriolering: wij hebben het juiste materiaal om te ontstoppen zonder breekwerk.",
  "w_kick": "Waarom ABS", "w_title": "Snel, eerlijk, efficiënt",
  "why": [["clock", "Vertrek na je oproep", "Aan de telefoon krijg je het geschatte aankomstuur voor we vertrekken."], ["euro", "Prijs vooraf", "De prijs wordt telefonisch vastgelegd. Er gebeurt niets zonder je akkoord."], ["gauge", "Professioneel materiaal", "Elektrische veer, hogedrukwagen en camera: ontstoppen zonder je leidingen te beschadigen."], ["file", "Verzekeringsdossier", "Officiële factuur met btw-nummer en technisch verslag voor je terugbetaling."]],
  "h_kick": "Eenvoudig en snel", "h_title": "Hoe gaat het in zijn werk?",
  "how": [["Je neemt contact op", "Telefonisch of via WhatsApp, 7/7. Beschrijf het probleem, wij geven je een prijs."], ["De technieker komt", "Snel, met al het nodige materiaal."], ["Het is ontstopt", "Doorlooptest, opkuis van de werkzone en factuur ter plaatse."]],
  "p_kick": "Transparante prijzen", "p_title": "Duidelijke prijzen, geen verrassingen",
  "p_lead": "De exacte prijs wordt vóór de interventie bevestigd. Wat we zeggen, is wat je betaalt.",
  "badge": "Meest gevraagd", "from_long": "vanaf", "price_lbl": "prijs",
  "plans": [["Sanitaire ontstopping", None, ["Wc, gootsteen, lavabo, douche, putje", "Professionele elektrische veer", "Doorlooptest na de werken"]], ["Riool & hogedruk", None, ["Riool, kolom, inspectieput", "Hogedrukwagen", "Wortels, vet en kalk verwijderd"]], ["Camera-inspectie", None, ["Draaibare HD-camera 360°", "Lokalisatie tot op de centimeter", "Videorapport voor verzekering of syndicus"]]],
  "ask_price": "Prijs vragen", "p_note": "Gratis en vrijblijvende offerte: de exacte prijs krijg je vóór elke interventie.",
  "z_kick": "Werkgebied", "z_title": "Overal in België",
  "z_lead": "We komen overal in België, 7/7: in Brussel, Vlaanderen en Wallonië.",
  "z_peri": "Rand",
  "f_kick": "FAQ", "f_title": "Veelgestelde vragen",
  "faq": [["Hoe snel zijn jullie ter plaatse?", "Zo snel mogelijk, elke dag van 6 tot 21 uur. Aan de telefoon geven we je een inschatting van het aankomstuur volgens je gemeente."], ["Hoeveel kost een ontstopping in Brussel?", "De prijs hangt af van de situatie. Je krijgt hem gratis telefonisch of via WhatsApp vóór de interventie, en die prijs staat op de factuur."], ["Wat zijn jullie uren?", "Elke dag van 6 tot 21 uur, ook in het weekend."], ["Betaalt mijn verzekering terug?", "Vaak wel, zeker bij waterschade. Je krijgt een officiële factuur met btw-nummer en een technisch verslag."], ["Wat doe ik in afwachting van de technieker?", "Gebruik geen water meer (spoelen, wasmachine, vaatwasser), sluit de watertoevoer af als het overloopt en vermijd bijtende producten."], ["Gebruiken jullie chemische producten?", "Nee. We werken mechanisch (veer, hogedruk), zonder bijtende producten voor je leidingen of het milieu."]],
  "fin_title": "Verstopping? Wacht niet tot het overloopt.",
  "fin_lead": "Eén telefoontje: we luisteren naar je probleem, geven je de prijs en een technieker vertrekt naar je toe, elke dag van 6 tot 21 uur.",
  "sv_signs": "Duidelijke signalen", "sv_causes": "De meest voorkomende oorzaken",
  "sv_method": "Onze werkwijze", "sv_price": "Prijs", "sv_price_free": "Prijs gratis vooraf meegedeeld",
  "sv_tip": "In afwachting van de technieker", "sv_faq": "Veelgestelde vragen", "sv_other": "Onze andere diensten",
  "sv_zone": "Interventie in Brussel en in heel België",
  "foot_about": "Spoedontstopping, hogedrukreiniging en camera-inspectie voor particulieren, syndici en bedrijven, in Brussel en in heel België.",
  "foot_hours": "Elke dag open · 6–21 uur", "foot_info": "Informatie", "foot_services": "Diensten",
  "vat": "Btw", "insured": "Factuur en verslag voor je verzekering", "rights": "Alle rechten voorbehouden", "privacy": "Privacy",
  "about_slug": "over-ons", "contact_slug": "contact", "privacy_slug": "privacybeleid",
  "notfound": "Pagina niet gevonden", "notfound_lead": "Deze pagina bestaat niet of werd verplaatst. Nood aan een ontstopping? We zijn er elke dag van 6 tot 21 uur.",
 }
}

ABOUT = {
 "fr": {
  "title": "À propos & tarifs | ABS Débouchage, Belgique",
  "desc": "ABS Débouchage, entreprise belge de débouchage d'urgence à Bruxelles : nos engagements, notre matériel et nos tarifs transparents. TVA BE 0719.885.401.",
  "h1": "À propos d'ABS Débouchage",
  "lead": "Une entreprise belge spécialisée dans le débouchage d'urgence, l'hydrocurage et l'inspection caméra, pour les particuliers, les syndics, les commerces et les restaurants, à Bruxelles et dans toute la Belgique.",
  "blocks": [["Nos engagements", ["Intervention rapide, tous les jours de 6h à 21h.", "Prix annoncé avant le départ du technicien : c'est ce prix qui figure sur la facture.", "Aucun travail ne commence sans votre accord.", "Intervention propre : la zone est nettoyée avant notre départ."]],
             ["Notre matériel", ["Furets électriques rotatifs professionnels.", "Camions hydrocureurs haute pression.", "Camion de vidange pour fosses septiques.", "Caméra d'inspection HD rotative 360° avec sonde de localisation.", "Aucun produit chimique corrosif."]],
             ["Assurance & facturation", ["Facture officielle avec n° TVA BE 0719.885.401.", "Rapport technique et vidéo pour votre dossier d'assurance.", "Documents acceptés par les syndics et notaires."]]]
 },
 "nl": {
  "title": "Over ons & prijzen | ABS Débouchage, België",
  "desc": "ABS, Belgisch bedrijf voor spoedontstopping in Brussel: onze engagementen, ons materiaal en onze transparante prijzen. Btw BE 0719.885.401.",
  "h1": "Over ABS",
  "lead": "Een Belgisch bedrijf gespecialiseerd in spoedontstopping, hogedrukreiniging en camera-inspectie, voor particulieren, syndici, winkels en restaurants, in Brussel en heel België.",
  "blocks": [["Onze engagementen", ["Snelle interventie, elke dag van 6 tot 21 uur.", "Prijs gekend vóór de technieker vertrekt: die prijs staat op de factuur.", "Er gebeurt niets zonder je akkoord.", "Propere interventie: de werkzone wordt gereinigd voor we vertrekken."]],
             ["Ons materiaal", ["Professionele elektrische veren.", "Hogedrukwagens.", "Draaibare HD-inspectiecamera 360° met lokalisatiesonde.", "Geen bijtende chemische producten."]],
             ["Verzekering & facturatie", ["Officiële factuur met btw-nummer BE 0719.885.401.", "Technisch en videoverslag voor je verzekeringsdossier.", "Documenten aanvaard door syndici en notarissen."]]]
 }
}

PRIVACY = {
 "fr": ("Politique de confidentialité", [
  "ABS Débouchage est une marque de C.R.N.M. & Cie SRL, Rue de la Carpe 2, 1080 Bruxelles, TVA BE 0719.885.401. Responsable du traitement, elle respecte votre vie privée conformément au Règlement général sur la protection des données (RGPD).",
  "Données collectées : lorsque vous remplissez le formulaire de demande d'intervention, nous recevons le type de problème, le niveau d'urgence, votre description, le code postal, la ville et, si vous l'indiquez, l'adresse, vos nom, téléphone et, si vous l'indiquez, e-mail, ainsi que les photos que vous ajoutez (4 au maximum, réduites avant l'envoi). Ces informations servent uniquement à traiter votre demande, à vous recontacter, à établir le devis et à réaliser l'intervention. Elles ne sont ni vendues ni utilisées à des fins publicitaires. Base légale : votre consentement, donné en cochant la case du formulaire, et les mesures précontractuelles prises à votre demande.",
  "Destinataires : votre demande est enregistrée sur l'infrastructure de notre hébergeur (Cloudflare) et peut nous être transmise par e-mail et par notification WhatsApp. Ces prestataires agissent uniquement pour notre compte. Pendant que vous remplissez le formulaire, vos réponses sont gardées temporairement dans votre navigateur (pas les photos) et effacées après l'envoi ou à la fermeture de l'onglet. Si vous choisissez l'envoi par WhatsApp, un message est préparé dans WhatsApp et c'est vous qui choisissez de l'envoyer. Les informations transmises par téléphone ou WhatsApp servent aux mêmes fins.",
  "Conservation : vos données sont conservées le temps nécessaire au suivi de l'intervention et aux obligations comptables légales.",
  "Statistiques : notre hébergeur Cloudflare compte les visites du site de façon anonyme (Cloudflare Web Analytics), sans cookie et sans suivi d'un site à l'autre.",
  ("Cookies : ce site n'utilise pas de cookies de suivi ou publicitaires. Votre choix de langue peut être mémorisé localement dans votre navigateur." if not GADS_ID else "Cookies : uniquement si vous cliquez sur « Accepter », le site charge la balise Google Ads, qui enregistre un cookie pour savoir si un appel ou un message WhatsApp vient d'une de nos annonces. Aucune publicité personnalisée n'est activée. Si vous refusez, rien n'est chargé chez Google. Pour changer d'avis, videz les données du site dans votre navigateur."),
  "Vos droits : vous pouvez demander l'accès, la rectification ou la suppression de vos données en nous appelant au 0484 72 47 24, par e-mail à absdebouchage@gmail.com ou en écrivant à notre adresse (Rue de la Carpe 2, 1080 Bruxelles). Vous pouvez aussi introduire une plainte auprès de l'Autorité de protection des données (autoriteprotectiondonnees.be)."]),
 "nl": ("Privacybeleid", [
  "ABS Débouchage is een merk van C.R.N.M. & Cie SRL, Rue de la Carpe 2, 1080 Brussel, btw BE 0719.885.401. Als verwerkingsverantwoordelijke respecteert zij je privacy overeenkomstig de Algemene Verordening Gegevensbescherming (AVG/GDPR).",
  "Verzamelde gegevens: wanneer je het formulier voor een interventieaanvraag invult, ontvangen we het soort probleem, de dringendheid, je beschrijving, de postcode, de gemeente en, als je het opgeeft, het adres, je naam, telefoonnummer en, als je het opgeeft, e-mailadres, en de foto's die je toevoegt (maximaal 4, verkleind voor verzending). Deze gegevens dienen enkel om je aanvraag te behandelen, je te contacteren, de offerte op te stellen en de interventie uit te voeren. Ze worden niet verkocht en niet voor reclame gebruikt. Rechtsgrond: je toestemming, gegeven door het vakje in het formulier aan te vinken, en de precontractuele maatregelen op jouw verzoek.",
  "Ontvangers: je aanvraag wordt opgeslagen op de infrastructuur van onze hostingprovider (Cloudflare) en kan ons per e-mail en via een WhatsApp-melding bereiken. Deze dienstverleners handelen uitsluitend in onze opdracht. Terwijl je het formulier invult, worden je antwoorden tijdelijk in je browser bewaard (niet de foto's) en gewist na verzending of bij het sluiten van het tabblad. Kies je voor verzending via WhatsApp, dan wordt een bericht in WhatsApp voorbereid en kies jij of je het verstuurt. Gegevens die je per telefoon of WhatsApp doorgeeft, dienen hetzelfde doel.",
  "Bewaring: je gegevens worden bewaard zolang nodig voor de opvolging van de interventie en de wettelijke boekhoudkundige verplichtingen.",
  "Statistieken: onze hostingprovider Cloudflare telt de bezoeken aan de site anoniem (Cloudflare Web Analytics), zonder cookies en zonder je te volgen van site tot site.",
  ("Cookies: deze site gebruikt geen tracking- of advertentiecookies. Je taalkeuze kan lokaal in je browser worden onthouden." if not GADS_ID else "Cookies: alleen als je op « Akkoord » klikt, laadt de site de Google Ads-tag, die een cookie plaatst om te weten of een oproep of WhatsApp-bericht via een van onze advertenties komt. Er wordt geen gepersonaliseerde reclame geactiveerd. Weiger je, dan wordt niets bij Google geladen. Van gedacht veranderen? Wis de sitegegevens in je browser."),
  "Je rechten: je kunt inzage, verbetering of verwijdering van je gegevens vragen door ons te bellen op 0484 72 47 24, te mailen naar absdebouchage@gmail.com of te schrijven naar ons adres (Rue de la Carpe 2, 1080 Brussel). Je kunt ook klacht indienen bij de Gegevensbeschermingsautoriteit (gegevensbeschermingsautoriteit.be)."]),
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
 "fosse": [("urgent", "La fosse déborde ou les eaux usées remontent", "De put loopt over of het afvalwater komt terug"),
           ("today", "Odeurs autour de la maison, tout s'écoule lentement", "Geurtjes rond het huis, alles loopt traag af"),
           ("plan", "Vidange d'entretien (pas faite depuis des années)", "Onderhoudslediging (al jaren niet gedaan)")],
 "siphon": [("urgent", "L'eau déborde du siphon", "Het water loopt over uit het putje"),
            ("today", "Une flaque reste autour du siphon", "Er blijft een plas rond het putje staan"),
            ("plan", "Une odeur d'égout remonte", "Er komt een rioolgeur omhoog")],
 "camera": [("today", "Bouchons à répétition au même endroit", "Steeds opnieuw verstopt op dezelfde plaats"),
            ("today", "Humidité inexpliquée dans un mur ou un sol", "Onverklaarbaar vocht in een muur of vloer"),
            ("plan", "Contrôle avant un achat ou une vente", "Controle voor een aankoop of verkoop")],
 "plomberie": [("urgent", "Une fuite d'eau active ou un dégât des eaux", "Een actieve waterlek of waterschade"),
               ("today", "Plus d'eau chaude ou plus de pression", "Geen warm water of geen druk meer"),
               ("plan", "Un robinet, une chasse ou un sanitaire à réparer ou remplacer", "Een kraan, spoelbak of sanitair te herstellen of te vervangen")],
 "autre": [("urgent", "Ça déborde ou ça refoule", "Het loopt over of slaat terug"),
           ("today", "Ça s'écoule mal", "Het loopt slecht weg"),
           ("plan", "Je veux un conseil ou un rendez-vous", "Ik wil advies of een afspraak")],
}

DIAG_UI = {
 "fr": {
  "label": "Diagnostic express", "title": "Décrivez votre problème, on vous dit quoi faire",
  "lead": "Moins d'une minute. Vous obtenez le niveau d'urgence, le prix de départ et les bons gestes en attendant. Votre demande nous arrive ensuite déjà complète sur WhatsApp.",
  "pros": ["Gratuit et sans engagement", "Réponse rapide, 7j/7 de 6h à 21h", "Prix annoncé avant toute intervention"],
  "alt": "Vous préférez appeler directement ?",
  "box": "Diagnostic express", "step": "Étape {n} sur 3",
  "q1": "Quel est le problème ?", "h1": "Choisissez ce qui correspond le mieux.",
  "q2": "Que se passe-t-il exactement ?", "h2": "Votre réponse nous aide à évaluer l'urgence.",
  "q3": "Votre diagnostic", "back": "Retour", "other": "Autre problème",
  "sev": {"urgent": ("Urgent : intervention immédiate recommandée", "Appelez-nous tout de suite. N'attendez pas que la situation s'aggrave."),
          "today": ("À traiter aujourd'hui", "Ce n'est pas encore une inondation, mais ça peut vite s'aggraver. Mieux vaut intervenir dans la journée."),
          "plan": ("Pas d'urgence immédiate", "On peut fixer ensemble un rendez-vous qui vous arrange, sans frais supplémentaires.")},
  "price": "Prix", "price_q": "Devis gratuit, annoncé avant l'intervention", "wait": "En attendant le technicien",
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
  "lead": "Minder dan een minuut. Je krijgt het dringendheidsniveau, de startprijs en wat je intussen kunt doen. Je aanvraag komt daarna volledig ingevuld bij ons op WhatsApp.",
  "pros": ["Gratis en vrijblijvend", "Snel antwoord, 7/7 van 6 tot 21 uur", "Prijs gekend vóór elke interventie"],
  "alt": "Liever meteen bellen?",
  "box": "Snelle diagnose", "step": "Stap {n} van 3",
  "q1": "Wat is het probleem?", "h1": "Kies wat het best overeenkomt.",
  "q2": "Wat gebeurt er precies?", "h2": "Je antwoord helpt ons de dringendheid in te schatten.",
  "q3": "Jouw diagnose", "back": "Terug", "other": "Ander probleem",
  "sev": {"urgent": ("Dringend: onmiddellijke interventie aangeraden", "Bel ons meteen. Wacht niet tot het erger wordt."),
          "today": ("Vandaag aanpakken", "Het is nog geen overstroming, maar het kan snel erger worden. Best vandaag nog laten bekijken."),
          "plan": ("Geen onmiddellijke nood", "We spreken samen een moment af dat jou past, zonder extra kosten.")},
  "price": "Prijs", "price_q": "Gratis offerte, vooraf meegedeeld", "wait": "In afwachting van de technieker",
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


# ---------------------------------------------------------------------------
# Demande d'intervention (formulaire en 6 étapes qui remplace le diagnostic express)
# ---------------------------------------------------------------------------
# Problèmes proposés à l'étape 1 : (id, icône, libellé FR, libellé NL, service du site dont on reprend les situations)
REQ_PROBLEMS = [
 ("wc", "toilet", "WC bouché", "Wc verstopt", "wc"),
 ("evier", "sink", "Évier bouché", "Gootsteen verstopt", "evier"),
 ("douche", "shower", "Douche ou baignoire bouchée", "Douche of bad verstopt", "douche"),
 ("canalisation", "pipes", "Canalisation bouchée", "Leiding verstopt", "cuisine"),
 ("egout", "manhole", "Égout bouché", "Riool verstopt", "egout"),
 ("odeurs", "smell", "Mauvaises odeurs", "Slechte geurtjes", None),
 ("camera", "camera", "Inspection caméra", "Camera-inspectie", "camera"),
 ("plomberie", "wrench", "Plomberie, fuite", "Loodgieterij, lek", "plomberie"),
 ("autre", "help", "Autre problème", "Ander probleem", "autre"),
]
# Service d'une page → carte présélectionnée à l'étape 1
REQ_PRE = {"wc": "wc", "sanibroyeur": "wc", "evier": "evier", "lavabo": "evier", "douche": "douche", "baignoire": "douche",
           "cuisine": "canalisation", "siphon": "canalisation", "egout": "egout", "fosse": "egout", "camera": "camera", "plomberie": "plomberie"}
REQ_ODEURS_SITS = [("today", "Odeur d'égout dans la maison", "Rioolgeur in huis"),
                   ("plan", "Odeur qui revient de temps en temps", "Geur die af en toe terugkomt"),
                   ("today", "Odeur avec gargouillements ou écoulement lent", "Geur met geborrel of trage afvoer")]

REQ_UI = {
 "fr": {
  "box": "Diagnostic express", "badge": "Gratuit · 2 min",
  "aside_t": "Votre demande d'intervention, en 2 minutes.",
  "aside": [("gauge", "Le niveau d'urgence", "évalué avec vous"), ("euro", "Le prix", "annoncé avant tout déplacement"), ("shield", "Les bons gestes", "à faire en attendant")],
  "steps": ["Le problème", "L'urgence", "L'adresse", "Photos", "Vos coordonnées", "Récapitulatif"],
  "step": "Étape {n} sur {t}",
  "q1": "Quel est le problème ?", "h1": "Choisissez ce qui correspond le mieux.",
  "q2": "C'est urgent ?", "h2": "Votre réponse nous aide à organiser l'intervention.",
  "sits": "Ce qui se passe (facultatif)",
  "urg": {"urgent": ("Intervention urgente aujourd'hui", "Ça déborde, ça ne s'écoule plus, ou ça ne peut pas attendre."),
          "soon": ("Dans les prochains jours", "Ça s'écoule mal, mais vous pouvez encore patienter."),
          "quote": ("Demande de devis, sans urgence", "Vous voulez un prix ou un rendez-vous planifié.")},
  "urg_call": "En cas d'urgence, le plus rapide reste de nous appeler :",
  "wait": "En attendant le technicien",
  "wait_generic": "Arrêtez d'utiliser l'eau, coupez l'arrivée d'eau si ça déborde et évitez les produits chimiques.",
  "desc": "Décrivez le problème", "desc_ph": "Ex. : le WC du rez-de-chaussée déborde depuis ce matin, la ventouse n'a rien donné.", "desc_hint": "Facultatif, mais ça nous aide à venir avec le bon matériel.",
  "q3": "Où faut-il intervenir ?", "h3": "Nous intervenons partout en Belgique : Bruxelles, Wallonie et Flandre.",
  "cp": "Code postal", "cp_ph": "1050", "city": "Ville ou commune", "city_ph": "Ixelles", "addr": "Adresse de l'intervention", "addr_ph": "Rue et numéro", "addr_hint": "Facultatif : on peut vous la demander plus tard.",
  "q4": "Ajoutez des photos", "h4": "Facultatif. Jusqu'à 4 photos : le bouchon, l'endroit, l'accès. Ça nous aide à préparer l'intervention.",
  "add": "Ajouter des photos", "add_more": "Ajouter une photo", "rm": "Retirer la photo", "photo_n": "Photo {n}",
  "q5": "Comment vous joindre ?", "h5": "Uniquement pour traiter votre demande.",
  "name": "Nom et prénom", "name_ph": "Marie Dupont", "tel": "Téléphone", "tel_ph": "0470 12 34 56", "mail": "E-mail", "mail_ph": "marie@exemple.be",
  "opt": "facultatif",
  "consent": "J'accepte qu'ABS Débouchage utilise ces informations pour traiter ma demande, comme expliqué dans la",
  "privacy": "politique de confidentialité",
  "q6": "Vérifiez votre demande", "h6": "Touchez « Modifier » pour corriger une information.",
  "r_prob": "Problème", "r_urg": "Urgence", "r_loc": "Adresse", "r_desc": "Description", "r_photos": "Photos", "r_contact": "Coordonnées",
  "none": "Aucune", "nodesc": "Pas de description", "edit": "Modifier", "back_recap": "Revenir au récapitulatif",
  "next": "Continuer", "back": "Retour", "send": "Envoyer ma demande", "sending": "Envoi en cours…",
  "send_wa": "Envoyer via WhatsApp", "wa_note": "WhatsApp s'ouvre avec votre demande déjà rédigée : il vous reste à appuyer sur Envoyer, et à y joindre vos photos.",
  "ok_t": "Demande envoyée", "ok_p": "Votre demande nous est bien parvenue. ABS Débouchage vous recontacte au {tel}.",
  "ok_id": "Numéro de demande", "ok_at": "Reçue le", "ok_urgent": "C'est urgent ? N'attendez pas notre appel :",
  "ko_t": "Votre demande n'a pas pu être envoyée", "ko_p": "Rien n'a été transmis. Pour ne pas perdre de temps, envoyez-la par WhatsApp (elle est déjà rédigée) ou appelez-nous.",
  "ko_retry": "Réessayer", "new": "Nouvelle demande",
  "call": "Appeler", "call_now": "Appeler maintenant",
  "err": {"prob": "Choisissez le type de problème.", "urg": "Indiquez le niveau d'urgence.", "cp": "Entrez un code postal belge à 4 chiffres.",
          "city": "Indiquez la ville ou la commune.", "name": "Indiquez votre nom.", "tel": "Entrez un numéro de téléphone valide, par exemple 0470 12 34 56.",
          "mail": "Cette adresse e-mail ne semble pas valide.", "consent": "Votre accord est nécessaire pour traiter la demande.",
          "photo_type": "Ce fichier n'est pas une photo prise en charge (JPEG, PNG, WebP ou HEIC depuis un iPhone).", "photo_big": "Cette photo est trop lourde (20 Mo maximum).",
          "photo_max": "4 photos maximum.", "photo_read": "Cette photo n'a pas pu être lue. Essayez avec une autre."},
  "region": {"bxl": "Bruxelles", "wal": "Wallonie", "vl": "Flandre"},
  "wa": {"hello": "Bonjour ABS Débouchage, voici ma demande :", "prob": "Problème", "urg": "Urgence", "where": "Adresse", "desc": "Description", "name": "Nom", "tel": "Téléphone", "mail": "E-mail", "photos": "Je vous envoie mes photos juste après."},
  "noscript": "Pour une demande d'intervention, appelez-nous directement :",
 },
 "nl": {
  "box": "Snelle diagnose", "badge": "Gratis · 2 min",
  "aside_t": "Je interventieaanvraag, in 2 minuten.",
  "aside": [("gauge", "Het dringendheidsniveau", "samen ingeschat"), ("euro", "De prijs", "gekend voor we vertrekken"), ("shield", "De juiste reflexen", "in afwachting")],
  "steps": ["Het probleem", "De dringendheid", "Het adres", "Foto's", "Je gegevens", "Overzicht"],
  "step": "Stap {n} van {t}",
  "q1": "Wat is het probleem?", "h1": "Kies wat het best overeenkomt.",
  "q2": "Is het dringend?", "h2": "Je antwoord helpt ons de interventie te plannen.",
  "sits": "Wat er gebeurt (optioneel)",
  "urg": {"urgent": ("Dringende interventie vandaag", "Het loopt over, het loopt niet meer weg, of het kan niet wachten."),
          "soon": ("In de komende dagen", "Het loopt slecht weg, maar je kunt nog even wachten."),
          "quote": ("Offerteaanvraag, niet dringend", "Je wilt een prijs of een geplande afspraak.")},
  "urg_call": "Bij spoed bel je ons best meteen:",
  "wait": "In afwachting van de technieker",
  "wait_generic": "Gebruik geen water meer, sluit de watertoevoer af als het overloopt en vermijd chemische producten.",
  "desc": "Beschrijf het probleem", "desc_ph": "Bv.: het toilet op het gelijkvloers loopt al sinds vanochtend over, de ontstopper hielp niet.", "desc_hint": "Optioneel, maar zo komen we met het juiste materiaal.",
  "q3": "Waar moeten we komen?", "h3": "We komen overal in België: Brussel, Vlaanderen en Wallonië.",
  "cp": "Postcode", "cp_ph": "1050", "city": "Stad of gemeente", "city_ph": "Elsene", "addr": "Adres van de interventie", "addr_ph": "Straat en nummer", "addr_hint": "Optioneel: we kunnen het later nog vragen.",
  "q4": "Voeg foto's toe", "h4": "Optioneel. Tot 4 foto's: de verstopping, de plaats, de toegang. Zo bereiden we de interventie voor.",
  "add": "Foto's toevoegen", "add_more": "Foto toevoegen", "rm": "Foto verwijderen", "photo_n": "Foto {n}",
  "q5": "Hoe bereiken we je?", "h5": "Enkel om je aanvraag te behandelen.",
  "name": "Naam en voornaam", "name_ph": "Marie Peeters", "tel": "Telefoon", "tel_ph": "0470 12 34 56", "mail": "E-mail", "mail_ph": "marie@voorbeeld.be",
  "opt": "optioneel",
  "consent": "Ik ga akkoord dat ABS Débouchage deze gegevens gebruikt om mijn aanvraag te behandelen, zoals uitgelegd in het",
  "privacy": "privacybeleid",
  "q6": "Controleer je aanvraag", "h6": "Tik op « Wijzigen » om iets aan te passen.",
  "r_prob": "Probleem", "r_urg": "Dringendheid", "r_loc": "Adres", "r_desc": "Beschrijving", "r_photos": "Foto's", "r_contact": "Gegevens",
  "none": "Geen", "nodesc": "Geen beschrijving", "edit": "Wijzigen", "back_recap": "Terug naar het overzicht",
  "next": "Verder", "back": "Terug", "send": "Mijn aanvraag versturen", "sending": "Bezig met versturen…",
  "send_wa": "Versturen via WhatsApp", "wa_note": "WhatsApp opent met je aanvraag al ingevuld: je hoeft alleen nog op Verzenden te drukken en je foto's toe te voegen.",
  "ok_t": "Aanvraag verstuurd", "ok_p": "We hebben je aanvraag goed ontvangen. ABS Débouchage neemt contact met je op via {tel}.",
  "ok_id": "Aanvraagnummer", "ok_at": "Ontvangen op", "ok_urgent": "Dringend? Wacht niet op onze oproep:",
  "ko_t": "Je aanvraag kon niet verstuurd worden", "ko_p": "Er is niets doorgestuurd. Verlies geen tijd: stuur ze via WhatsApp (ze is al ingevuld) of bel ons.",
  "ko_retry": "Opnieuw proberen", "new": "Nieuwe aanvraag",
  "call": "Bellen", "call_now": "Nu bellen",
  "err": {"prob": "Kies het soort probleem.", "urg": "Geef aan hoe dringend het is.", "cp": "Vul een Belgische postcode van 4 cijfers in.",
          "city": "Vul de stad of gemeente in.", "name": "Vul je naam in.", "tel": "Vul een geldig telefoonnummer in, bijvoorbeeld 0470 12 34 56.",
          "mail": "Dit e-mailadres lijkt niet geldig.", "consent": "Je akkoord is nodig om de aanvraag te behandelen.",
          "photo_type": "Dit bestand is geen ondersteunde foto (JPEG, PNG, WebP of HEIC van een iPhone).", "photo_big": "Deze foto is te groot (max. 20 MB).",
          "photo_max": "Maximaal 4 foto's.", "photo_read": "Deze foto kon niet gelezen worden. Probeer een andere."},
  "region": {"bxl": "Brussel", "wal": "Wallonië", "vl": "Vlaanderen"},
  "wa": {"hello": "Hallo ABS Débouchage, hier is mijn aanvraag:", "prob": "Probleem", "urg": "Dringendheid", "where": "Adres", "desc": "Beschrijving", "name": "Naam", "tel": "Telefoon", "mail": "E-mail", "photos": "Ik stuur mijn foto's meteen hierna."},
  "noscript": "Voor een interventieaanvraag, bel ons rechtstreeks:",
 },
}
