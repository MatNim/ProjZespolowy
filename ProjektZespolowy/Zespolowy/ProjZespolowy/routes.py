from flask import render_template, url_for, flash, redirect
from ProjZespolowy import app
from ProjZespolowy.forms import *
from pony.orm import *
from ProjZespolowy.models import *
from flask_bcrypt import Bcrypt
from flask_login import current_user, logout_user, login_user, login_required
import datetime


bcrypt=Bcrypt()
db.bind(provider='mysql', host='localhost', user='root', passwd='', db='ProjektZespolowy')
set_sql_debug(True)     #wyswietla w konsoli jakie zapytania sql wykonal
db.generate_mapping(create_tables=True) #tworzy tablice jesli nie istnialy na podstawie class Nazwa(db.Entity)

def remove_last_line_from_string(s,email):
    if s.endswith(email):
        return s.replace(email, '')
    else:
        return s.replace(email+"\n", '')




   # return s[:s.rfind(email)]

@db_session
def add_osobarejestracja(imie,nazwisko,email,login,haslo):
    Osoba(imie=imie,nazwisko=nazwisko,email=email,login=login,haslo=haslo,rodzaj_konta=3,stan_konta=3)

@db_session
def add_osobarejestracjastudent(imie,nazwisko,email,numer_indeksu,login,haslo):
    Osoba(imie=imie,nazwisko=nazwisko,email=email,numer_indeksu=numer_indeksu,login=login,haslo=haslo,rodzaj_konta=1)

@db_session
def add_osobarejestracjapwr(imie,nazwisko,email,login,haslo):
    Osoba(imie=imie,nazwisko=nazwisko,email=email,login=login,haslo=haslo,rodzaj_konta=2)

@db_session
def add_nowyprojekt(osobaosoba_id,firmafirma_id,tytul,opis,komentarz,naklad_czasu,max_studentow,min_studentow,max_grup,semestr):
    Projekt(osobaosoba_id=osobaosoba_id,firmafirma_id=firmafirma_id,tytul=tytul,opis=opis,komentarz=komentarz,naklad_czasu=naklad_czasu,max_studentow=max_studentow,min_studentow=min_studentow,max_grup=max_grup,semestr=semestr,status=1,data_zgloszenia=datetime.datetime.now(),ilosc_zapisanych_grup=0)

@db_session
def add_osobadofirmy(osobaid,firmaid):
    Pracownicy_firmy(osobaosoba_id=osobaid,firmafirma_id=firmaid,czy_glowny=0)

@db_session
def add_nowafira(nazwa,czyaktywna):
    Firma(nazwa=nazwa,czy_aktywna=czyaktywna)

@db_session
def add_nowagrupa(email):
    Grupa(email=email,liczba_czlonkow=1,opis=email,projektProjekt_id=11,stan_zapisu=1)

@db_session
def add_glownyfirma(osobaid,firmaid):
    Pracownicy_firmy(osobaosoba_id=osobaid,firmafirma_id=firmaid,czy_glowny=1)

@db_session
def add_glownygrupa(osobaid,grupaid):
    Czlonkowie(osobaosoba_id=osobaid,grupagrupa_id=grupaid,czy_lider=1)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/modifyGroup", methods=['GET', 'POST'])
def modifyGroup():
    form=ModifyGroupForm()
    czlonkowie=db.Czlonkowie.get(osobaosoba_id=current_user.id)
    grupa = czlonkowie.grupagrupa_id

    projekt = Projekt[grupa.projektProjekt_id]
    if form.validate_on_submit(): #dodawanie
        if form.submit.data:
            if grupa.opis.find(form.email.data)!=-1:
                flash(f'Osoba o podanym emailu jest juz w grupie', 'danger')
                return render_template('modifyGroup.html', title='Modyfikacja grupy',grupa=grupa,czlonkowie=czlonkowie,projekt=projekt,form=form)

            else:
                grupa.liczba_czlonkow=grupa.liczba_czlonkow+1
                grupa.opis=grupa.opis+"\n"+form.email.data+"\n"
                flash(f'Dodano czlonka do grupy', 'success')
                return render_template('modifyGroup.html', title='Modyfikacja grupy',grupa=grupa,czlonkowie=czlonkowie,projekt=projekt,form=form)

        elif form.delete.data:#usuwanie
            if grupa.liczba_czlonkow < 2 or grupa.email==form.email.data :
                flash(f'Nie mozna usunac lidera grupy. W celu usuniecia calej grupy wciscnij usun grupe', 'danger')
                return render_template('modifyGroup.html', title='Modyfikacja grupy',grupa=grupa,czlonkowie=czlonkowie,projekt=projekt,form=form)
            else:
                string = grupa.opis
                if grupa.opis!=remove_last_line_from_string(string,form.email.data):
                    grupa.opis=remove_last_line_from_string(string,form.email.data)
                    grupa.liczba_czlonkow=grupa.liczba_czlonkow-1
                    flash(f'Usunieto czlonka z grupy', 'success')
                    return render_template('modifyGroup.html', title='Modyfikacja grupy',grupa=grupa,czlonkowie=czlonkowie,projekt=projekt,form=form)
                else:
                    flash(f'Brak takiego emaila w grupie', 'danger')
                    return render_template('modifyGroup.html', title='Modyfikacja grupy',grupa=grupa,czlonkowie=czlonkowie,projekt=projekt,form=form)
    return render_template('modifyGroup.html', title='Modyfikacja grupy',grupa=grupa,czlonkowie=czlonkowie,projekt=projekt,form=form)

@app.route("/AddProject", methods=['GET', 'POST'])
def AddProject():
    if current_user.stan_konta==1:
        form = ProjectForm()
        if form.validate_on_submit():   #jesli wszystko zostalo wpisane odpowiednio
            firma_pracownik=db.Pracownicy_firmy.get(osobaosoba_id=current_user.id)
            firma = firma_pracownik.firmafirma_id
            add_nowyprojekt(current_user.id,firma.firma_id,form.title.data,form.description.data,form.comment.data,form.time_nedded.data,int(form.max_students.data),int(form.min_students.data),int(form.max_groups.data),form.semester.data)
            flash(f'Dodano nowy projekt {form.title.data}!', 'success')
        return render_template('addProject.html', form=form,legend='Dodanie nowego projektu',buttontext='Dodaj projekt')
    else:
        flash('Twoje konto nie jest jeszcze zaakceptowane', 'danger')
        return redirect(url_for('account'))

@app.route("/updateProject<int:projekt_id>", methods=['GET', 'POST'])
def updateProject(projekt_id):

    semestr = Required(str)
    tytul = Required(str)
    komentarz = Optional(str, nullable=True)
    opis = Required(LongStr)
    naklad_czasu = Required(str)
    max_studentow = Required(int)
    min_studentow = Required(int)
    max_grup = Required(int)
    status = Required(int)
    opiekun_nazwisko = Optional(str, nullable=True)
    opiekun_imie = Optional(str, nullable=True)
    opiekun_email = Optional(str, nullable=True)
    data_zgloszenia = Optional(date)
   # Osoba=Required('Osoba')
    if current_user.stan_konta==1:
        projekt=Projekt[projekt_id]
        form = ProjectForm()
        if form.validate_on_submit():   #jesli wszystko zostalo wpisane odpowiednio
            projekt.tytul = form.title.data
            projekt.opis = form.description.data
            projekt.komentarz = form.comment.data
            projekt.naklad_czasu = form.time_nedded.data
            projekt.max_studentow = form.max_students.data
            projekt.min_studentow = form.min_students.data
            projekt.max_grup = form.max_groups.data
            projekt.semestr = form.semester.data
            flash('Zmodyfikowano projekt', 'success')
            return redirect(url_for('account'))

        form.title.data = projekt.tytul
        form.description.data = projekt.opis
        form.comment.data = projekt.komentarz
        form.time_nedded.data = projekt.naklad_czasu
        form.max_students.data = projekt.max_studentow
        form.min_students.data = projekt.min_studentow
        form.max_groups.data = projekt.max_grup
        form.semester.data = projekt.semestr
        return render_template('addProject.html', form=form,legend='Modyfikacja projektu' ,buttontext='Modyfikuj projekt')
    else:
        flash('Twoje konto nie jest jeszcze zaakceptowane', 'danger')
        return redirect(url_for('account'))

@app.route("/verifyAccounts", methods=['GET', 'POST'])
def verifyAccounts():
    result = select(osoba for osoba in Osoba if osoba.stan_konta == 3)[:]
    # print(result)
    form = VerifyForm()
    return render_template('verifyAccounts.html',form=form,result=result)


@app.route("/showProjects", methods=['GET', 'POST'])
def showProjects():
  #  if current_user.rodzaj_konta==1 or current_user.rodzaj_konta==2 or current_user.rodzaj_konta==3 :
    s = str(current_user)
    if s.startswith("<flask_login.mixins.AnonymousUserMixin"):
        print(current_user)
        print(s)
        flash(f'Niezalogowany', 'danger')
        result = select(projekt for projekt in Projekt )[:]
        firma = select(firma for firma in Firma )[:]
        return render_template('choseProject.html',result=result,firma=firma,accountType=0)
    else:
        flash(f'Zalogowany', 'success')
        result = select(projekt for projekt in Projekt )[:]
        firma = select(firma for firma in Firma )[:]
        return render_template('choseProject.html',result=result,firma=firma,accountType=current_user.rodzaj_konta)


@app.route("/showPendingGroups", methods=['GET', 'POST'])
def showPendingGroups():
    projekty=[]
    grupy = select(grupa for grupa in Grupa if grupa.projektProjekt_id != 11 and grupa.stan_zapisu==2)[:]
    for grupa in grupy:
        if grupa.stan_zapisu==2:
            if Projekt[grupa.projektProjekt_id] not in projekty:
                projekty.append(Projekt[grupa.projektProjekt_id])
            print('sklad:', grupa.opis)#debug
            print('email:', grupa.email)#debug
    for projekt in projekty:
        print('tytul',projekt.tytul)#debug
    return render_template('showPendingGroups.html',grupa=grupy,projekt=projekty)

@app.route("/choseProjectToModify", methods=['GET', 'POST'])
def choseProjectToModify():
    firma_pracownik=db.Pracownicy_firmy.get(osobaosoba_id=current_user.id)
    firma = firma_pracownik.firmafirma_id
    result = select(projekt for projekt in Projekt if projekt.firmafirma_id==firma.firma_id )[:]
    # print(result)
    form = VerifyForm()
    return render_template('choseProjectToModify.html',form=form,result=result)

@app.route("/verify/<int:osoba_id>", methods=['GET', 'POST'])
def verify(osoba_id):
    form = VerifyForm()
    weryfikowany = Osoba[osoba_id]
    weryfikowany.stan_konta=1
    flash(f'Zaakceptowano konto pracownika', 'success')
    result = select(osoba for osoba in Osoba if osoba.stan_konta == 3)[:]
    return render_template('verifyAccounts.html',form=form,result=result)

@app.route("/sendreserveproject/<int:projekt_id>", methods=['GET', 'POST'])
def sendreserveproject(projekt_id):
    czlonkowie=db.Czlonkowie.get(osobaosoba_id=current_user.id)
    grupa = czlonkowie.grupagrupa_id
    projekt = Projekt[projekt_id]
    if  grupa.projektProjekt_id!=11: # projekt poczatkowy
        flash(f'Twoja grupa jest juz zapisana do projektu', 'danger')
        result = select(projekt for projekt in Projekt )[:]
        return redirect(url_for('showProjects'))
    elif projekt.status==4:#zarezerwowany
        flash(f'Ten projekt jest juz zajety', 'danger')
        result = select(projekt for projekt in Projekt )[:]
        return redirect(url_for('showProjects'))
    elif projekt.min_studentow > grupa.liczba_czlonkow:
        flash(f'Twoja grupa ma mniejsza ilosc czlonkow niz wymagana liczba czlonkow do projektu. Skontaktuj sie z prowadzacym projektu w celu zwiekszenia szansy zatwiedzenia tematu.', 'warning')
        projekt.status=3        #zarezerwowany
        grupa.stan_zapisu=2
        grupa.data_zgloszenia=datetime.datetime.now()
        grupa.projektProjekt_id=projekt_id
        return redirect(url_for('showProjects'))
    elif projekt.max_studentow < grupa.liczba_czlonkow:
        flash(f'Twoja grupa przekracza dozwolona ilosc czlonkow dla tego projektu', 'danger')
        return redirect(url_for('showProjects'))
    else:
        flash(f'Zarezerwowano projekt', 'success')
        projekt.status=3
        grupa.stan_zapisu=2
        grupa.projektProjekt_id=projekt_id
        grupa.data_zgloszenia=datetime.datetime.now()
        return redirect(url_for('showProjects'))

@app.route("/delete/<int:osoba_id>", methods=['GET', 'POST'])
def delete(osoba_id):
    form = VerifyForm()
    Osoba[osoba_id].delete()
    result = select(osoba for osoba in Osoba if osoba.stan_konta == 3)[:]
    flash(f'Usunieto konto nieprawidlowego pracownika', 'success')
    return render_template('verifyAccounts.html',form=form,result=result)

@app.route("/deleteProject/<int:projekt_id>", methods=['GET', 'POST'])
def deleteProject(projekt_id):
    projectToDelete=Projekt[projekt_id]
    if projectToDelete.ilosc_zapisanych_grup>0 :
        flash(f'Nie mozna usunac projektu z zapisanymi grupami', 'danger')
        return redirect(url_for('choseProjectToModify'))
    else:
        Projekt[projekt_id].delete()
        flash(f'Usunieto Projekt', 'success')
        return redirect(url_for('choseProjectToModify'))

@app.route("/acceptGroupToProject/<int:projekt_id>,<int:grupa_id>", methods=['GET', 'POST']) #call showPendingGroups from here?
def acceptGroupToProject(projekt_id,grupa_id):
    acceptedProject=Projekt[projekt_id]
    acceptedProject.ilosc_zapisanych_grup=acceptedProject.ilosc_zapisanych_grup+1
    acceptedGroup=Grupa[grupa_id]
    acceptedGroup.stan_zapisu=3
    if acceptedProject.ilosc_zapisanych_grup==acceptedProject.max_grup:
        acceptedProject.status=4

    flash(f'Zaakceptowano grupe do projektu', 'success')
    return redirect(url_for('showPendingGroups'))

@app.route("/cancelGroupToProject/<int:projekt_id>,<int:grupa_id>", methods=['GET', 'POST'])
def cancelGroupToProject(projekt_id,grupa_id):
    canceledProject=Projekt[projekt_id]
    canceledProject.status=2
    canceledGroup=Grupa[grupa_id]
    canceledGroup.projektProjekt_id=11
    canceledGroup.stan_zapisu=1
    flash(f'Anulowano zapis grupy do projektu', 'success')
    return redirect(url_for('showPendingGroups'))
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/account")
def account():
    firma_pracownik=db.Pracownicy_firmy.get(osobaosoba_id=current_user.id)
    firma = firma_pracownik.firmafirma_id
    return render_template('account.html', title='Account',firma=firma,firma_pracownik=firma_pracownik)



@app.route("/accountpwr")
def accountpwr():
    return render_template('accountpwr.html', title='Account')

@app.route("/accountstudent")
def accountstudent():
    return render_template('accountstudent.html', title='Account')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    form.company.choices= [(company.firma_id,company.nazwa) for company in db.Firma.select()]
    if form.validate_on_submit():   #jesli wszystko zostalo wpisane odpowiednio
        print(form.company.data)    #debugowy test wartosci
        flash(f'Utworzono konto dla {form.username.data}!', 'success')
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        add_osobarejestracja(form.name.data,form.last_name.data,form.email.data,form.username.data,hashed_password)
        if form.newcompany.data:
            add_nowafira(form.newcompany.data,0)
            add_glownyfirma(db.Osoba.get(login=form.username.data),db.Firma.get(nazwa=form.newcompany.data))
        else:
            add_osobadofirmy(db.Osoba.get(login=form.username.data),form.company.data)
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/registerpwr", methods=['GET', 'POST'])
def registerpwr():
    form = RegistrationFormPWR()
    if form.validate_on_submit():   #jesli wszystko zostalo wpisane odpowiednio
        flash(f'Utworzono konto dla {form.username.data}!', 'success')
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        add_osobarejestracjapwr(form.name.data,form.last_name.data,form.email.data,form.username.data,hashed_password)
        return redirect(url_for('login'))
    return render_template('registerpwr.html', title='Register', form=form)

@app.route("/registerstudent", methods=['GET', 'POST'])
def registerstudent():
    form = RegistrationFormStudent()
    if form.validate_on_submit():   #jesli wszystko zostalo wpisane odpowiednio
        flash(f'Utworzono konto dla {form.username.data}!', 'success')
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        add_osobarejestracjastudent(form.name.data,form.last_name.data,form.email.data,form.indeks.data,form.username.data,hashed_password)
        add_nowagrupa(form.email.data)
        add_glownygrupa(db.Osoba.get(login=form.username.data),db.Grupa.get(email=form.email.data))
        return redirect(url_for('login'))
    return render_template('registerstudent.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        possible_user = db.Osoba.get(login=form.login.data)
        if not possible_user:
            flash('Nieudana próba logowania, sprawdź login i hasło', 'danger')
            return redirect(url_for('login'))
        if bcrypt.check_password_hash(possible_user.haslo, form.password.data):
            login_user(possible_user)
            if current_user.rodzaj_konta==3: #firma
                return redirect(url_for('account'))
            elif current_user.rodzaj_konta==2: #pwr
                return redirect(url_for('accountpwr'))
            elif current_user.rodzaj_konta==1: #student
                return redirect(url_for('accountstudent'))
            else:
                flash('Nieznany typ konta', 'danger')
        else:
            flash('Nieudana próba logowania, sprawdź login i hasło', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/projectInfo/<int:projekt_id>")
def projectInfo(projekt_id):
    s = str(current_user)
    projekt=Projekt[projekt_id]
    firma= Firma[projekt.firmafirma_id]
    if s.startswith("<flask_login.mixins.AnonymousUserMixin"):
        return render_template('projectInfo.html', title='Project',firma=firma,projekt=projekt,accountType=0)
    return render_template('projectInfo.html', title='Project',firma=firma,projekt=projekt,accountType=current_user.rodzaj_konta)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
