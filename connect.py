import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                        user="root",
                                        database="bddtgo")
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print ("Congrats twat, you connected your database successfully <3 !!! : ", record) 

cursor = connection.cursor()
print("Coucou1")
query =("SELECT terminal, numero_tc"
      "FROM etat_du_parc_tgo")
print("coucou2")
cursor.execute(query)
print("coucou3")
for (TERMINAL, NUMERO_TC, ISO, STATUT_VP, POIDS_BRUT, EXPLOITANT, ALLOTISSEMENT) in cursor:
       print("Numéro TC : {} a pour inforamtions :").format(NUMERO_TC)
       print("Terminal : {}").format(TERMINAL)
       print("ISO : {}").format(ISO)
       print("Statut V/P : {}").format(STATUT_VP)
       print("Poids brut").format(POIDS_BRUT)
       print("Exploitant").format(EXPLOITANT)
       print("Allotissement").format(ALLOTISSEMENT)
print("coucou4")
cursor.close()
print("coucou5")
connection.close()
