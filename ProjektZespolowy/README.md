# ProjektZespolowy
Instalacja pythona  
W konsoli komendy  
$ sudo apt-get update  
$ sudo apt-get install python3.6  

Lista wymaganych pakietow znajduje sie w requirements.txt na jego podstawie mozna utworzyc wirtualne srodowisko.  
W konsoli nalezy wpisac:  
pip install virtualenv  
Nastepnie w miejscu w ktorym ma zostac utworzone wirtualne srodowisko nalezy w konsoli wpisac  
$ virtualenv -p /usr/bin/python3.6 zespolowy_env  
Tutorial w formie wideo:  
https://www.youtube.com/watch?v=N5vscPTWKOk

W celu uruchomienia bazy danych nalezy zainstalowac XAMPP  
Po zainstalowaniu XAMPP mozna go uruchomic komenda $ sudo /opt/lampp/manager-linux-x64.run  
Nastepnie po uruchomieniu XAMPP klikamy zakladke Manage Servers i wciskamy Start dla MySQL Database i Apache Web Server  
Status obu serwerow powinien zmienic sie na Running  
Po uruchomieniu serwerow mozna wpisac w przegladarce http://localhost:80 i kliknac zakladke phpMyAdmin w celu wyswietlenia utworzonych baz danych  
W celu dodania uzywanej przez nas bazy danych nalezy najpierw stworzyc nowa baze danych klikajac new po lewej stronie. W database name wpisujemy ProjektZespolowy a z wyboru obok wybieramy utf16_polish_ci  
Po stworzeniu bazy klikamy ProjektZespolowy w lewej zakladce a nastepnie import w gornych zakladkach, potem browse i wybieramy ProjektZespolowy.sql z folderu projektu po wyborze klikamy Go u dolu strony.  
Po dodaniu i konfiguracji bazy mozna ja zobaczyc wybierajac ProjektZespolowy z lewej listy  

Po postawieniu bazy nalezy otworzyc nowe okno terminala pozostawiac poprzednie otwarte.  
W celu uruchomienia aplikacji nalezy uruchomic wczesniej skonfigurowane wirtualne srodowisko komenda $source zespolowy_env/bin/activate bedac w folderze z wirtulnym srodowiskiem ("zespolowy_env" zalezy od nazwy folderu w ktorym znajduje sie wirtualne srodowisko)  
Nastepnie nalezy przejsc do folderu projektu Zespolowy z plikiem Run.py i uruchomic program komenda $python run.py  
Po uruchomieniu mozna otworzyc aplikacje w przegladarce wpisujac http://127.0.0.1:5000/  


wersja pythona -Python 3.6.7  
wersja Linux - Ubuntu 18.04.2 LTS 64-bit  


przykladowe konta firmy  
Glowny pracownik firmy nowa:  
Login: Jannow  
haslo: jannowhas  
Glowny pracownik firmy Nokia:  
Login: noknok  
haslo: noknokhas  
przykladowe konto administratora pwr  
Login: pwrpwr  
haslo: pwrpwrhas  
przykladowe konta student  
Przykladowe zapisane konta do projektu  
login: lidgru  
haslo: lidgruhas  
login: stustu  
haslo: stustuhas  
login: grugru  
haslo: grugruhas  
Przykladowe konto studenta bez projektu  
login: wolwol  
haslo: wolwolhas  
