# Grandes villes de Wallonie et de Flandre : pages d'atterrissage pour les annonces Google Ads.
# (nom FR, nom NL, région, province FR, province NL, codes postaux, villes voisines FR, villes voisines NL)
# Région : "wal" = annonces en français, "vl" = annonces en néerlandais.
VILLES = [
    ("Liège", "Luik", "wal", "province de Liège", "provincie Luik", ["4000", "4020", "4030"], ["Seraing", "Herstal", "Ans", "Flémalle"], ["Seraing", "Herstal", "Ans", "Flémalle"]),
    ("Charleroi", "Charleroi", "wal", "Hainaut", "Henegouwen", ["6000", "6001", "6010", "6020"], ["Châtelet", "Fleurus", "Montigny-le-Tilleul", "Courcelles"], ["Châtelet", "Fleurus", "Montigny-le-Tilleul", "Courcelles"]),
    ("Namur", "Namen", "wal", "province de Namur", "provincie Namen", ["5000", "5100"], ["Gembloux", "Andenne", "Profondeville", "La Bruyère"], ["Gembloux", "Andenne", "Profondeville", "La Bruyère"]),
    ("Mons", "Bergen", "wal", "Hainaut", "Henegouwen", ["7000", "7011", "7012"], ["Quaregnon", "Saint-Ghislain", "Frameries", "Jurbise"], ["Quaregnon", "Saint-Ghislain", "Frameries", "Jurbeke"]),
    ("La Louvière", "La Louvière", "wal", "Hainaut", "Henegouwen", ["7100"], ["Binche", "Manage", "Morlanwelz", "Le Rœulx"], ["Binche", "Manage", "Morlanwelz", "Le Rœulx"]),
    ("Tournai", "Doornik", "wal", "Hainaut", "Henegouwen", ["7500"], ["Antoing", "Péruwelz", "Leuze-en-Hainaut", "Mouscron"], ["Antoing", "Péruwelz", "Leuze-en-Hainaut", "Moeskroen"]),
    ("Verviers", "Verviers", "wal", "province de Liège", "provincie Luik", ["4800"], ["Dison", "Pepinster", "Spa", "Theux"], ["Dison", "Pepinster", "Spa", "Theux"]),
    ("Wavre", "Waver", "wal", "Brabant wallon", "Waals-Brabant", ["1300"], ["Ottignies-Louvain-la-Neuve", "Rixensart", "Grez-Doiceau", "Chaumont-Gistoux"], ["Ottignies-Louvain-la-Neuve", "Rixensart", "Graven", "Chaumont-Gistoux"]),
    ("Nivelles", "Nijvel", "wal", "Brabant wallon", "Waals-Brabant", ["1400"], ["Braine-l'Alleud", "Waterloo", "Tubize", "Genappe"], ["Eigenbrakel", "Waterloo", "Tubeke", "Genepiën"]),
    ("Arlon", "Aarlen", "wal", "province de Luxembourg", "provincie Luxemburg", ["6700"], ["Messancy", "Aubange", "Attert", "Habay"], ["Messancy", "Aubange", "Attert", "Habay"]),
    ("Anvers", "Antwerpen", "vl", "province d'Anvers", "provincie Antwerpen", ["2000", "2018", "2060", "2100"], ["Mortsel", "Edegem", "Schoten", "Wijnegem"], ["Mortsel", "Edegem", "Schoten", "Wijnegem"]),
    ("Gand", "Gent", "vl", "Flandre-Orientale", "Oost-Vlaanderen", ["9000", "9030", "9040", "9050"], ["Merelbeke", "Destelbergen", "Lochristi", "De Pinte"], ["Merelbeke", "Destelbergen", "Lochristi", "De Pinte"]),
    ("Bruges", "Brugge", "vl", "Flandre-Occidentale", "West-Vlaanderen", ["8000", "8200", "8310"], ["Oostkamp", "Damme", "Jabbeke", "Zedelgem"], ["Oostkamp", "Damme", "Jabbeke", "Zedelgem"]),
    ("Louvain", "Leuven", "vl", "Brabant flamand", "Vlaams-Brabant", ["3000", "3001", "3010", "3012"], ["Herent", "Bertem", "Kortenberg", "Holsbeek"], ["Herent", "Bertem", "Kortenberg", "Holsbeek"]),
    ("Malines", "Mechelen", "vl", "province d'Anvers", "provincie Antwerpen", ["2800"], ["Bonheiden", "Sint-Katelijne-Waver", "Willebroek", "Duffel"], ["Bonheiden", "Sint-Katelijne-Waver", "Willebroek", "Duffel"]),
    ("Alost", "Aalst", "vl", "Flandre-Orientale", "Oost-Vlaanderen", ["9300"], ["Erpe-Mere", "Lede", "Denderleeuw", "Haaltert"], ["Erpe-Mere", "Lede", "Denderleeuw", "Haaltert"]),
    ("Courtrai", "Kortrijk", "vl", "Flandre-Occidentale", "West-Vlaanderen", ["8500"], ["Harelbeke", "Kuurne", "Wevelgem", "Menin"], ["Harelbeke", "Kuurne", "Wevelgem", "Menen"]),
    ("Hasselt", "Hasselt", "vl", "Limbourg", "Limburg", ["3500"], ["Diepenbeek", "Zonhoven", "Herk-de-Stad", "Lummen"], ["Diepenbeek", "Zonhoven", "Herk-de-Stad", "Lummen"]),
    ("Genk", "Genk", "vl", "Limbourg", "Limburg", ["3600"], ["As", "Zutendaal", "Houthalen-Helchteren", "Maasmechelen"], ["As", "Zutendaal", "Houthalen-Helchteren", "Maasmechelen"]),
    ("Ostende", "Oostende", "vl", "Flandre-Occidentale", "West-Vlaanderen", ["8400"], ["Bredene", "Middelkerke", "Oudenburg", "Gistel"], ["Bredene", "Middelkerke", "Oudenburg", "Gistel"]),
    ("Saint-Nicolas", "Sint-Niklaas", "vl", "Flandre-Orientale", "Oost-Vlaanderen", ["9100"], ["Temse", "Beveren", "Waasmunster", "Stekene"], ["Temse", "Beveren", "Waasmunster", "Stekene"]),
    ("Roulers", "Roeselare", "vl", "Flandre-Occidentale", "West-Vlaanderen", ["8800"], ["Izegem", "Ledegem", "Hooglede", "Moorslede"], ["Izegem", "Ledegem", "Hooglede", "Moorslede"]),
]
