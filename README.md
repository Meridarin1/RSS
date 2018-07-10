RSS scraper page written in Django

Całość zadania zajęło mi 3:30 h. Celery było podchwtyliwe, ale bardzo przydatny framework. Raczej większość nie sprawiło problemów. Oczywiście nie zdążyłem dodać wszyskich walut tylko 4 przykładowe. Chyba nie jest to, aż tak rozbudowany projekt by się tutaj rozpisywać. Wszystko raczej napisane prosto z użycime Generic Views.

Architektura: 
wykorzystałem baze NoSQL Redis, do wywoływania Scrapera cyklicznie Celery reszta natomiast to czyste Django. 

By uruchomic serwer robimy to naturalnie przez python manage.py runserver 
Natomiast by nasz Scraper cyklicznie sprawdzał podaną stronę i w razie pojawienia sie nowych danych tworzył nowy wpis w bazie należy:
Uruchomic serwer Redis commenda: redis-server
Włączyć Celery komendami: celery -A picha worker -l info
 celery -A picha beat -l info
