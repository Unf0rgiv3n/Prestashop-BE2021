git# INSTRUKCJA ODPALENIA

1. Klonujemy repo do siebie na lokalną maszynę

```git clone git@github.com:Unf0rgiv3n/Prestashop-BE2021.git```

to jest robione po ssh tutaj jest to w pełni opisane co trzeba zrobić https://docs.github.com/en/authentication/connecting-to-github-with-ssh

2. Pobieramy dockera na naszego linuxa

postępujemy tak jak tu opisane: https://docs.docker.com/engine/install/ubuntu/

a następnie tak jak tutaj w zakładce "manage docker as non root user": https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user

jest to ważne, bo to pozwoli nam uniknąć wpisywanania sudo przed każdą komendą dockerową

3. Odpalamy terminal w folderze ze sklonowanym repo i wpisujemy:

```cd scripts/```

następnie, żeby odpalić sklep:

```bash start_shop.sh```

w przeglądarce łączymy się z http://localhost:8080

żeby bezpiecznie wyłączyć sklep i zapisać dump bazy danych:

```bash stop_shop.sh```

żeby wyłączyć bez dumpa wpisujemy

```docker-compose down```


# WAŻNE INFO

W repo na gicie będzie się znajdować "startowy" dump bazy danych, ale dodaje w .gitignore flagę, która, będzie pomijać wasz lokalny dump. 

PRZED WRZUCENIEM ZMIAN USUWAMY STARY DUMP KOMENDĄ 

```git rm --cached mysql-db/databasedump.sql```

i potem dodajemy nasz nowy dump

```git add mysql-db/databasedump.sql -f```

musimy użyć forcea, bo domyślnie jest git ignore

## WORKFLOW

Będzie jeden główny branch - master, na ten branch nie wrzucamy swoich zmian, przy każdym zadaniu tworzymy nowy branch i nazywamy go odpowiednio tzn. "nazwisko/nrXX" np: "kwiatkowski/nr15".

Następnie na tym branchu pracujemy nad swoim featurem i tam wrzucamy swoje zmiany, jeżeli uznacie, że skończyliście NIE WRZUCACIE zmian na mastera tylko dajecie to przejrzeć przynajmniej 1 osobie, która daje wam approve'a - nie trzeba robić tego jakoś hardkorowo szczegółowo, ale to pozwoli wypatrzeć jakieś potencjalne błędy jeżeli takie są. Przed wrzuceniem na branch trzeba jeszcze zrebasować zmiany na swoim branchu do aktualnego mastera i ztestować czy nic się nie zepsuło. Przy rebasie mogą wystąpić merge conflicty jeżeli były robione zmiany na tych samych plikach przez innych, ale wtedy trzeba to rozwiązać zgodnie z guidem https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts dobrą praktyką w takim wypadku jest pytanie się co autor miał na myśli jeżeli nie wiecie o co chodzi, można sprawdzić kto modyfikował plik w historii repo ew. komendą git blame.

### tworzenie nowego brancha od mastera:

1. przełączamy się na mastera 

```git checkout master```

2. Pullujemy zmiany

```git pull origin master``` 

to zaciąga zmiany, które inni mogli wprowadzić

3. Tworzymy nowy branch na daną funkcjonlaność

```git checkout -b nazwisko/nrXX```

### wrzucanie zmian na swój branch

1. upewniamy się, że jesteśmy na swoim branchu

```git status```

pokaże nam na którym branchu jesteśmy oraz listę zmodyfikowanych plików

2. jeżeli chcemy dodać wszystkie pliki to używamy

```git add .```

jeżeli nie wszystkie to zamiast kropki wpisujemy ścieżke do poszczególnych plików np.

```git add test.txt```

3. ZANIM dodamy pliki można przejrzeć zmiany przez:

```git diff```

4. robimy commita

```git commit -m 'zrobiłem to i to'```


starajcie się dawać sensowne wiadomości w tych commitach, to ułatwia pracę. Co ważne, commit zapisuje zmiany lokalnie, to się nie wrzuca jeszcze na zdalne repo.

5. wrzucamy zmiany na repo

```git push origin <branch>```

np:

```git push origin kwiatkowski/nr15```


### Rebase po dostaniu approva

1. przełączamy się na mastera (po zcommitowaniu wszystkich zmian na waszym branchu)

```git checkout master```

2. pullujemy najnowsze zmiany

```git pull origin master```

3. wracamy na nasz branch

```git checkout <nasz_branch>```

4. rebasujemy, jeżeli nie będzie konfliktów to wszystko pójdzie zgrabnie, jak będa to można podbić do mnie przy pierwszym tego typu procesie, ale najpierw spróbujcie sami z guidem wyżej

```git rebase master```

5. testujemy zmiany po rebasie sprawdzamy czy nic się nie zepsuło po zaciągnięciu innych zmian

6. pushujemy na repo zrebasowny branch

```git push origin <nasz_branc> -f```

tutaj jak widać jest flaga -f i trzbea tak to zrobić, bo rebase "nadpisuje historię", ale wygląda to zgrabniej w repo i łatwiej się pracuje

### PULL request

po całej tej operacji z wyżej ja jeszcze przejrze zmianę i zaakceptuje je pull requestem do głównego brancha, proszę sami tego nie róbcie (przynajmniej na razie) :P
