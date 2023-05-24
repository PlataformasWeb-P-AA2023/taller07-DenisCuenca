from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club, Jugador

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


archivo = open('data/datos_clubs.txt', "r", encoding="utf-8")
archivojugadores = open('data/datos_jugadores.txt', "r", encoding="utf-8")

# obtener las líneas del archivo
lineas_clubs = archivo.readlines()
lineas_jugadores = archivojugadores.readlines()

for l in lineas_clubs:
        li = l.split(";")
  
        club = Club(nombre=li[0], deporte=li[1], \
        fundacion=int(li[2][0:4]))

        session.add(club)


for l in lineas_jugadores:
        li = l.split(";")
       
        club = session.query(Club).filter_by(nombre=li[0]).one()
        jugador = Jugador(nombre =li[3][:-2], dorsal=int(li[2]), posicion= li[1], club=club)

        print(f"nombre ={li[3][:-2]}, dorsal={int(li[2])}, posicion= {li[1]}, club={club}")
       

        session.add(jugador)


archivo.close()
archivojugadores.close()

session.commit()
