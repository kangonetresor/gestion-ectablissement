# cursor.rowcount : qui permet de compter la ligne 
#  cursor.lastrowid : lui permet d'avoir le dernier identifiant
import mysql.connector as MC

try:
    
    connex = MC.connect(host = 'localhost', database = 'projet_python', user = 'root', password = '')
    cursor = connex.cursor()

    req = "INSERT INTO utilisateur VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    infos = ("1245", "g", "g", "F", "gg@gmail.com", "Secretaire", "1245", "1245789663")
    cursor.execute(req, infos)
    connex.commit()

    req = 'SELECT * FROM utilisateur'
    cursor.execute(req)

    utilisateurlist = cursor.fetchall()

    for users in utilisateurlist:
        print("Prenom : {}".format(users[2]))


except MC.Error as err:
    print(err) 
finally:
    if (connex.is_connected()):
        cursor.close()
        connex.close()


# import datetime
# import mysql.connector as mc # Pour travailler sur une BD MySQL
# 
# connection_params = mc.connect(host = 'localhost',
                            # database = 'gesetudiant',
                            # user = 'root', 
                            # password = '')
# 
# request = """insert into etudiant
            # (matricule, NomPrenoms, classe, dateinscription)
            # values (%s, %s, %s, %s)"""
# params = (("CI0119376468","Adama Landry", "Licence 3", datetime.date.today()),
        #   ("CI0118330826", "Kouamé Yves", "Licence 1", datetime.date.today()),
        #   ("CI0117324072", "Maro Elavi", "Licence 1", datetime.date.today()),
        #   ("CI0115289594", "Touri Alasco", "Master 1", datetime.date.today()),
        #   ("CI0119365659", "Yakoue Boris", "Master 2", datetime.date.today()),
        #   ("CI0116453054", "Aka-De Naomi", "Licence 3", datetime.date.today()),
        #   ("CI0119363434", "Diakité Amarou", "Licence 3", datetime.date.today()),
        #   ("CI0118340270", "Amani Bakou Brice", "Doctorat", datetime.date.today()),
        #   ("CI0118764642", "Amiano Rock", "Licence 1", datetime.date.today()),
        #   ("CI0115697434", "Yapo Noel", "Licence 3", datetime.date.today()),
        #   ("CI0119546704", "Traore Oumar", "Licence 2", datetime.date.today()),
        #   ("CI0122422258", "Taboh Issouf", "Licence 3", datetime.date.today()),
        #   ("CI0121392926", "Kangone Bi Tresor", "Master 2", datetime.date.today()),
        #   ("CI0120381917", "Kate Shadrack", "Licence 3", datetime.date.today()),
        #   ("CI0120381232", "Chonou Oriane", "Master 2", datetime.date.today()),
        #   ("CI0119371757", "Georges St-Pierre", "Master 2", datetime.date.today()),
        #   ("CI0118184335", "Affi Cynthia", "Doctorat", datetime.date.today()),
        #   ("CI0119361708", "Soro Kayazin", "Licence 1", datetime.date.today()),
        #   ("CI0132396080", "Taylor DuBoi", "Licence 3", datetime.date.today())
        # )
# 
# with mysql.connector.connect(**connection_params) as db :
    # with db.cursor() as c :
        # c.executemany(request, params)
        # db.commit()
        # print("Nombre de lignes insérées :", c.rowcount)