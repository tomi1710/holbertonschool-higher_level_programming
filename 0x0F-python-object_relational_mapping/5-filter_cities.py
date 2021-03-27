#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities
    of that state, using the database hbtn_0e_4_usa """

if __name__ == "__main__":

    from sys import argv
    import MySQLdb
    MY_H = "localhost"
    MY_U = argv[1]
    MY_P = argv[2]
    MY_D = argv[3]
    argument = argv[4]
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR\
                     ', ') FROM cities INNER JOIN states ON states.name\
                      = %s WHERE cities.state_id = states.id ORDER\
                       BY cities.id ASC;", (argument,))
    resultado = consulta.fetchall()
    for fila in resultado:
        proceso = str(fila).replace(",)", "")
        proceso = proceso.replace("(", "")
        proceso = proceso.replace("'", "")
        if (proceso != 'None'):
            print(proceso)
        else:
            print()
    nuevaconexion.close()
