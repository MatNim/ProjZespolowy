from datetime import datetime
from ProjZespolowy import db
from pony.orm import *
from datetime import date
from flask_login import UserMixin,LoginManager


class Projekt(db.Entity):
    projekt_id = PrimaryKey(int, auto=True)
    osobaosoba_id = Required(int)
    firmafirma_id = Optional(int)
  #  rok = Required(int)
    semestr = Required(str)
    tytul = Required(str)
    komentarz = Optional(str, nullable=True)
    opis = Required(LongStr)
    naklad_czasu = Required(str)
    max_studentow = Required(int)
    min_studentow = Required(int)
    max_grup = Required(int)
    ilosc_zapisanych_grup = Required(int)
    status = Required(int)
    opiekun_nazwisko = Optional(str, nullable=True)
    opiekun_imie = Optional(str, nullable=True)
    opiekun_email = Optional(str, nullable=True)
    data_zgloszenia = Optional(date)
   # Osoba=Required('Osoba')

class Osoba(db.Entity, UserMixin):
    id = PrimaryKey(int, auto=True)   #id a nie osoba_id poniewaz LoginManager inaczej nie widzi id
    imie = Required(str)
    nazwisko = Required(str)
    email = Optional(str, nullable=True)
    telefon = Optional(str, nullable=True)
    specialnosc = Optional(str, nullable=True)
    rok = Optional(int, nullable=True)
    login = Optional(str, nullable=True)
    haslo = Optional(str, nullable=True)
    numer_indeksu = Optional(int, nullable=True)
    rodzaj_konta = Required(int)
    stan_konta = Optional(int, nullable=True)
   # projekt = set(Projekt)
    osoba = Set('Pracownicy_firmy')
    osobagrupa = Set('Czlonkowie')

class Firma(db.Entity):
    firma_id = PrimaryKey(int, auto=True)
    nazwa = Required(str)
    opis  = Optional(str, nullable=True)
    email  = Optional(str, nullable=True)
    czy_aktywna  = Required(bool)
    miejscowosc = Optional(str, nullable=True)
    ulica = Optional(str, nullable=True)
    numer_budynku = Optional(str, nullable=True)
    numer_mieszkania = Optional(str, nullable=True)
    firma = Set('Pracownicy_firmy')

class Grupa(db.Entity):
    grupa_id = PrimaryKey(int, auto=True)
    projektProjekt_id = Optional(int)
    nazwa = Optional(str, nullable=True)
    opis  = Optional(str, nullable=True)
    email  = Optional(str, nullable=True)
    liczba_czlonkow = Required(int)
    stan_zapisu = Required(int)
    data_zgloszenia = Optional(datetime)
    grupa = Set('Czlonkowie')


class Pracownicy_firmy(db.Entity):
    firmafirma_id = Required(Firma)
    osobaosoba_id = Required(Osoba)
    czy_glowny = Required(bool)
    PrimaryKey(firmafirma_id, osobaosoba_id)

class Czlonkowie(db.Entity):
    grupagrupa_id = Required(Grupa)
    osobaosoba_id = Required(Osoba)
    czy_lider = Required(bool)
    PrimaryKey(grupagrupa_id, osobaosoba_id)
