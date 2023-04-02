import sqlite3


#connexion

print("connection...") # connection à la base de données (BDD)
conn = sqlite3.connect("baseDonnées.db") # BDD dans un fichier SQL spécifique
print("connecté !")


cur = conn.cursor() # récupération d'un curseur

print("effacement...")

cur.execute("DROP TABLE GENRES")
cur.execute("DROP TABLE AUTEUR")
cur.execute("DROP TABLE ANIME")
cur.execute("DROP TABLE PERSONNAGE")

print("effacé !")

conn.execute("PRAGMA foreign_keys = ON")    # Activation de clef étrangères

# preparation des données à ajouter

auteur = [

  ('Eiicherō','Oda','1975','Eiicherō Oda est un mangaka japonais principalement connu pour avoir écrit le manga le plus vendu du XXIème siècle au Japon et dans le reste du monde: One Piece !', 'OnePiece'



    ),



  ('Hajime','Isayama','1986','Hajime Isayama est nationalité japonaise et mangaka depuis le plus jeune âge. Il est devenu célèbre à partir de 2009 grâce à son manga à succès: Shingeki No Kyojin ou Attaques des Titans en Français.  - Le saviez-vous ? Hajime Isayama, seulement âgé de 23 ans, était considéré comme le meilleur mangaka "débutant" du Japon. - ', 'Attaque des Titans'



    ),



   ("Kōhei","Horikoshi","1986","Kōhei Horikishi est un mangaka Japonais né dans la préfecture d'Aichi. Il est connu pour avoir créé les séries shonen Crazy Zoo, Sensei no Bulge et plus récemment Boku no Hero Academia (My Hero Academia en anglais dont le surnom  est MHA). Il est aussi diplomé de l'Université d'art de Nagoya et a été l'assistant d'un grand mangaka des années 2000: Yasuki Tanaka", 'My Hero Academia'



    ),



]



anime = [



  ("OnePiece", "Eiichirō Oda", '1997', 'Toei Animation', "Il fut un temps où Gold Roger était le plus grand de tous les pirates, le Roi des Pirates était son surnom. A sa mort, son trésor d'une valeur inestimable connu sous le nom de 'One Piece' fut caché quelque part sur Grand Line. De nombreux pirates sont partis à la recherche de ce trésor mais tous sont morts avant même de l'atteindre. Monkey D. Luffy rêve de retrouver ce trésor légendaire et de devenir le nouveau Roi des Pirates. Après avoir mangé un fruit du démon, il possède un pouvoir lui permettant de réaliser son rêve. Il lui faut maintenant trouver un équipage pour partir à laventure !",""



    ),



  ('Attaque des Titans', 'Hajime Isayama', '2013', 'WIT STUDIO puis MAPPA (2020)', "Il y a 107 ans, les Titans ont presque exterminé la race humaine. Ces Titans mesurent principalement une dizaine de mètres et ils se nourrissent d'humains. Les rares ayant survécu à cette extermination ont construit une cité fortifiée aux murs d'enceinte de 50 mètres de haut pour pouvoir se protéger des Titans. Pendant 100 ans les humains ont connu la paix. Eren est un jeune garçon qui rêve de sortir de la ville pour explorer le monde extérieur. Il mène une vie paisible avec ses parents et sa sœur adoptive Mikasa dans le district de Shiganshina. Mais un jour de l'année 845, un Titan de plus de 60 mètres de haut apparaît. Il démolit une partie du mur du district de Shiganshina et provoque une invasion de Titans. Eren verra sa mère se faire dévorer sous ses yeux sans rien pouvoir faire. Il décidera après ces événements traumatisants de s'engager dans les forces militaires de la ville avec pour but d'exterminer tous les Titans qui existent.",""



    ),



   ('My Hero Academia', ' Kohei Horikoshi', '2014', 'Bones Studio', "Dans un futur proche suite à une mutation génétique, 80 % de la population mondiale possède des supers pouvoirs appelés Alters. Le plus célèbre des supers héro se nomme All Might. Izuku Midoriya en est fan, et rêve d'intégrer la filière super heroique du lycée Yuei pour suivre les traces de son idole et ainsi devenir le plus grand des super héros.",""

    ),

]



personnage = [

   ("Monkey D.","Luffy","05/05/2003","Monkey D. Luffy est un pirate, et est le principal protagoniste du manga et anime 'One Piece'. Son rêve le plus cher est de devenir le Roi des Pirates en trouvant le trésor légendaire caché quelque part dans ce vaste monde par Gol D. Roger. Selon lui, être le Seigneur des Pirates signifie être celui qui jouit d'une liberté sans pareille dans le monde.",'OnePiece'



    ),



   ("Jaeger",'Eren','30/03/835',"Eren Jäger est un personnage fictif et protagoniste du manga et anime 'L'Attaque des Titans' créé par Hajime Isayama. Eren est un adolescent qui a juré de se venger d'énormes créatures, appelées Titans, qui ont dévoré sa mère. Afin de les exterminer, Eren, accompagné de ses amis d'enfance Mikasa Ackerman et Armin Arlelt, s'engage dans l'Armée et rejoint les Bataillons d'Exploration (un groupe de soldats d'élite qui luttent contre les Titans hors des murs)",'Attaque des Titans'



    ),



   ("Midoriya","Izuku","16/07/2006","Izuku est né Sans-Alter, il attirera l'attention d'All Might pour son héroïsme et deviendra l'héritier de son Alter : le One For All. Poursuivant ses études au lycée Yuei afin de devenir un héros professionnel, Izuku aura la lourde tâche en tant que neuvième détenteur du One for All de devenir le nouveau symbole de la paix après All Might.",'My Hero Academia'

   ),

]



genres =[

   (1,"Action/Aventure/Pirates/Supers-pouvoirs/Amitié"),



   (2,"Actions/Drame/Horreur/Psychologique/Post-apocalyptique"),


   (3,"Actions/Comedie/Ecole/Super-hero/Super-pouvoirs"),

]


# créations des tables Auteur, Personnage et Anime

cur.executescript("""
CREATE TABLE IF NOT EXISTS GENRES(id_genres INTEGER PRIMARY KEY UNIQUE, description TEXT);
;""")
for i in genres:
    cur.execute("INSERT INTO GENRES(id_genres,description) VALUES(?,?)", i)
conn.commit()

cur.executescript("""
CREATE TABLE IF NOT EXISTS AUTEUR(id_auteur INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE , nom TXT, prenom TXT, date_naissance INT, biographie TEXT, anime TEXT);
;""")
cur.executemany("INSERT INTO AUTEUR(nom, prenom, date_naissance, biographie, anime) VALUES(?,?,?,?,?)", auteur)
conn.commit()

cur.executescript("""
CREATE TABLE IF NOT EXISTS ANIME( id_anime INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, titre TEXT, auteur INT, ann_publi INT, stud_anim TEXT, synopsis TEXT);
;""")
cur.executemany("INSERT INTO ANIME(titre, auteur, ann_publi, stud_anim, synopsis, auteur) VALUES(?,?,?,?,?,?)", anime)
conn.commit()

cur.executescript("""
CREATE TABLE IF NOT EXISTS PERSONNAGE(id_personnage INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TXT, prenom TXT, date_naissance INT, biographie TEXT, anime TXT);
""");
cur.executemany("INSERT INTO PERSONNAGE(nom, prenom, date_naissance, biographie, anime) VALUES(?,?,?,?,?)", personnage)
conn.commit()





print("déconnection...")

cur.close() # déconnection

print("déconnecté !")

