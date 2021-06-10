Web aplikacija naziva ERO (Evidencija Računalne Opreme) služi za evidenciju računalne opreme unutar firme. Računalnu opremu čine razne skupine uređaja (PC-evi, laptopi, monitori, printeri, telefoni, mrežni uređaji...). Aplikacija omogućava izvršavanje CRUD operacija nad modelima u bazi preko web sučelja. Za pristup web aplikaciji potrebno je imati odgovarajuće korisničko ime i lozinku (account kojeg kreira administrator). Za izradu aplikacije koristio se Django framework na backend strani, te bootstrap i CSS na frontend strani. Za bazu podataka koristi se MySQL. 


Zahtjevi za korištenje aplikacije:

    - na računalu je potrebno imati instaliran Python (najbolje verzija 3.8.5 ili novija)
    - potrebno je imati MySQL bazu (najbolje verzija 8.0.25 ili novija)
    - asgiref==3.3.1
    - Django==3.1.6
    - django-filter==2.4.0
    - mysqlclient==2.0.3
    - pytz==2021.1
    - sqlparse==0.4.1

Detaljni koraci za instalaciju aplikacije:

1. Instalirati Python (verzija 3.8.5 ili novija)


2. Instalirati MySQL bazu (verzija 8.0.23 ili novija)


3. Klonirati repozitorij sa githuba (https://github.com/pinky84/ero_projekt) lokalno na računalo


4. Instalirati softverske zahtjeve iz requirements.txt datoteke naredbom:
	pip install -r requirements.txt


5. Na MySQL serveru kreirati bazu "erodb"


6. Zatim u MySQL bazi kreirati korisnika "admin" i dati mu sve ovlasti sa sljedeće dvije naredbe:
	CREATE USER 'admin'@'%' IDENTIFIED BY 'Pinky_11';
	GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%';


7. Napraviti i primjeniti migraciju na bazu dvijema naredbama:
	python manage.py makemigrations
	python manage.py migrate


8. Kreirati superusera za pristup aplikaciji naredbom:
	python manage.py createsuperuser
		- nakon ove naredbe proizvoljno unijeti željeno korisničko ime i lozinku


9. Pokrenuti web server naredbom:
	python manage.py runserver


10. Nakon toga u web pregledniku ići na url http://127.0.0.1:8000/ ili http://localhost:8000/ za pristup aplikaciji
    Otvoriti će se login stranica za pristup aplikaciji. Ukucati username i password koji ste prije definirali
