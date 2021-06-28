import pandas
import json
import os
import sys
class Operacja: #y=0 to headery
  def __init__(self, operacje):
    self.arr = operacje.split(',')
    self.wiersz = int(self.arr[0]) # tu nie trzeba -1 bo naglowki maja id 0
    self.kolumna = int(self.arr[1])-1 #latwiejsze uzywanie kolumn
    self.nowe_dane = self.arr[2].replace('"', '') #usuniecie "" z nazwy w przypadku uzycia spacji

  def debug(self):
    print('Wiersz: {} Kolumna: {} Dane: {}'.format(self.wiersz, self.kolumna, self.nowe_dane))

nazwy_kolumn = []

### CSV ###
def odczyt_csv(nazwa):
  try:
    data_frame = pandas.read_csv(nazwa) #utworzenie data frame z pliku csv
    data_frame.index += 1 #ladniejsze wyswietlanie z indexowaniem od 1
    for col in data_frame.columns:
      nazwy_kolumn.append(col) #przepisanie nazw naglowkow do nowej tablicy
    return data_frame
  except FileNotFoundError:
    print('Nie znaleziono pliku, czy chodziło ci o:')
    directory = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir(directory):
      if filename.endswith('.csv'): 
          print(filename)
    sys.exit(1)

def zapisz_csv(data, nazwa):
  data.to_csv(nazwa, index=False)
### END CSV ###

### PICKLE ### 
def odczyt_pickle(nazwa):
  try:
    data_frame = pandas.read_pickle(nazwa) #utworzenie data frame z pliku pkl
    for col in data_frame.columns:
      nazwy_kolumn.append(col) #przepisanie nazw naglowkow do nowej tablicy
    return data_frame
  except FileNotFoundError:
    print('Nie znaleziono pliku, czy chodziło ci o:')
    directory = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir(directory):
      if filename.endswith(".csv"): 
          print(filename)
    sys.exit(1)

def zapisz_pickle(data, nazwa):
  data.to_pickle(nazwa)
### END PICKLE ###

### JSON ###
def odczyt_json(nazwa):
  try:
    data_frame = pandas.read_json(nazwa, orient="index") #utworzenie data frame z pliku json
    for col in data_frame.columns:
      nazwy_kolumn.append(col) #przepisanie nazw naglowkow do nowej tablicy
    return data_frame
  except FileNotFoundError:
    print('Nie znaleziono pliku, czy chodziło ci o:')
    directory = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir(directory):
      if filename.endswith(".json"): 
          print(filename)
    sys.exit(1)

def zapisz_json(data, nazwa):
  with open(nazwa, 'w', encoding='utf-8') as f:
    do_zapisu = json.loads(data.to_json(orient="index"))
    json.dump(do_zapisu, f, ensure_ascii=False, indent=4)
### END JSON ###    

def edytujXY(data_frame, operacje): #y=wiersz x=kolumna
  iter = 1
  for operacja in operacje:
    #operacja.debug()
    try:
      if operacja.wiersz == 0:
          print('Podano błędny numer wiersza w operacji {} dane w tych komórkach nie uległy zmianie'.format(iter))
      data_frame.at[operacja.wiersz, nazwy_kolumn[operacja.kolumna]] = operacja.nowe_dane
    except ValueError:
      print('Podano błędny typ danych w operacji: {} dane w tych komórkach nie uległy zmianie'.format(iter))
    iter+=1