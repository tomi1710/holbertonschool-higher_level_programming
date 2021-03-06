#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

from sys import argv
import MySQLdb
if __name__ == "__main__":

    MY_H = "localhost"
    MY_U = argv[1]
    MY_P = argv[2]
    MY_D = argv[3]
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT * FROM states ORDER BY id ASC")
    resultado = consulta.fetchall()
    for fila in resultado:
        if fila[1][0] == 'N':
            print(fila)
    nuevaconexion.close()
