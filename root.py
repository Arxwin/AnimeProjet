from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
app = Flask(__name__)       # importation et création des modules pour le site web

print("Démarrer !")

def get_db_connection():
    """
    permet de ce connecter à la base de donnée souhaité

    -paramètre- none
    -sortie- la base de données

    "conn" correspond à la connection vers la BDD dans ce module python

    """
    conn = sqlite3.connect("baseDonnées.db")
    conn.row_factory = sqlite3.Row
    return conn


""" SECTION ROUTAGE """

@app.route('/')      #routage du la page index.html (pour le lancement du serveur)
def index():
    print("index.html reçu !")
    return render_template('index.html')

@app.route('/acceuil')      #routage du la page index.html (pour parcourir le site web)
def acceuil():
    print("index.html reçu !")
    return render_template('index.html')

@app.route('/explorer')     #routage du la page explorer.html
def explorer():
    print("explorer.html reçu !")
    return render_template("explorer.html")


@app.route('/credit')       #routage du la page credit.html
def credit():
    print("credit.html reçu !")
    return render_template("credit.html")

@app.route('/base')       #routage du la page base.html
def base():
    print("base.html reçu !")
    return render_template("base.html")

@app.route('/OnePiece')      #routage du la page Onepiece.html
def OnePiece():
    conn = get_db_connection()
    print("Onepiece.html reçu !")
    posts = conn.execute('SELECT * FROM ANIME WHERE titre="OnePiece" AND id_anime=1').fetchall()
    posts2 = conn.execute('SELECT * FROM PERSONNAGE WHERE anime="OnePiece"').fetchall()
    posts3 = conn.execute('SELECT * FROM GENRES WHERE id_genres=1').fetchall()
    conn.close()
    return render_template('Onepiece.html', posts=posts, posts2=posts2, posts3=posts3)

@app.route('/Attaque_Des_Titans')      #routage du la page AOT.html
def Attaque_Des_Titans():
    conn = get_db_connection()
    print("AOT.html reçu !")
    posts = conn.execute('SELECT * FROM ANIME WHERE titre="Attaque des Titans" AND id_anime=2').fetchall()
    posts2 = conn.execute('SELECT * FROM PERSONNAGE WHERE anime="Attaque des Titans"').fetchall()
    posts3 = conn.execute('SELECT * FROM GENRES WHERE id_genres=2').fetchall()
    conn.close()
    return render_template('AOT.html', posts=posts, posts2=posts2, posts3=posts3)

@app.route('/My_Hero_Academia')      #routage du la page MHA.html
def My_Hero_Academia():
    conn = get_db_connection()
    print("MHA.html reçu !")
    posts = conn.execute('SELECT * FROM ANIME WHERE titre="My Hero Academia" AND id_anime=3').fetchall()
    posts2 = conn.execute('SELECT * FROM PERSONNAGE WHERE anime="My Hero Academia"').fetchall()
    posts3 = conn.execute('SELECT * FROM GENRES WHERE id_genres=3').fetchall()
    conn.close()
    return render_template('MHA.html', posts=posts, posts2=posts2, posts3=posts3)

@app.route('/auteur')      #routage du la page auteur.html
def auteur():
    conn = get_db_connection()
    print("auteur.html reçu !")
    posts = conn.execute('SELECT * FROM AUTEUR WHERE id_auteur=1').fetchall()
    posts2 = conn.execute('SELECT * FROM AUTEUR WHERE id_auteur=2').fetchall()
    posts3 = conn.execute('SELECT * FROM AUTEUR WHERE id_auteur=3').fetchall()
    conn.close()
    return render_template('auteur.html', posts=posts, posts2=posts2, posts3=posts3)


""" SECTION CREATION """

# essais de nombreuses méthodes sur chaque formulaire pour faire marcher le création mais échec sur chacun...

@app.route('/creer',methods = ['POST', 'GET'])  #routage de creer.html pour l'ajout d'attributs dans la relation ANIME
def creer():
    if request.method == 'GET':
        return render_template("creer.html")
    elif request.method == 'POST':
      result = request.form
      return render_template("explorer.html",result = result)


@app.route('/formulaire1',methods = ['POST', 'GET'])
def formulaire1():
    if request.method == 'POST':
        description = request.form['description']

        conn = get_db_connection()
        conn.execute('INSERT INTO PERSONNAGE(description) VALUES(?)',
                     (description))
        conn.commit()
        conn.close()
        return request(url_for("explorer.html"))
    return render_template("formulaire1.html")

@app.route('/formulaire2',methods = ['POST', 'GET'])
def formulaire2():
    if request.method == 'POST':
        nom = request.form['title']
        prenom = request.form['content']
        date_naissance = request.form['date ce naissance']
        biographie = request.form['biographie']
        anime = request.form['anime']

        conn = get_db_connection()
        conn.execute('INSERT INTO PERSONNAGE(nom, prenom, date_naissance, biographie, anime) VALUES(?,?,?,?,?)',
                     (nom, prenom, date_naissance, biographie, anime))
        conn.commit()
        conn.close()

    return render_template("formulaire2.html")


@app.route('/formulaire3',methods = ['POST', 'GET'])
def formulaire3():
    return render_template("formulaire3.html")
    if request.method == 'POST':
            nom = request.form['nom']
            prenom = request.form['prenom']
            date_naissance = request.form['date_naissance']
            biographie = request.form['biographie']
            anime = request.form['anime']
            conn = get_db_connection()
            conn.execute('INSERT INTO AUTEUR(nom, prenom, date_naissance, biographie, anime) VALUES(?,?,?,?,?)',
                         (nom, prenom, date_naissance, biographie, anime))
            conn.commit()
            conn.close()
            return render_template('auteur.html')


""" SECTION MODIFICATION/SUPPRESSION """



