#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """

if __name__ == "__main__":

    from sys import argv
    import MySQLdb
    MY_H = "localhost"
    MY_U = argv[1]
    MY_P = argv[2]
    MY_D = argv[3]
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    texto1 = "SELECT c.id, c.name, s.name FROM"
    texto2 = " cities c INNER JOIN states s ON c.state_id = s.id"
    consulta.execute(texto1 + texto2)
    resultado = consulta.fetchall()
    for fila in resultado:
        print(fila)
    nuevaconexion.close()
