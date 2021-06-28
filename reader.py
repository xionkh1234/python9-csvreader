import sys
from funkcje_pomocnicze import *


#jesli chcemy zmienic nazwe w polu na taka ze spacja to nalezy uzyc np. 1,1,"nowa nazwa" (pierwszy wiersz pierwsza kolumna)
if sys.argv[1]:
  operacje_arr = []
  nazwa_pliku = sys.argv[1]
  nazwa_nowego_pliku = sys.argv[2]
  #obsluga wejscia csv
  if nazwa_pliku.endswith('.csv'):
    df = odczyt_csv(nazwa_pliku)
    #wypisanie pliku przed modyfikacja
    print(df)
    for op in sys.argv[3:]:
      operacje_arr.append(Operacja(op))
    #edycja pliku
    edytujXY(df, operacje_arr)
    #zapis pliku
    if nazwa_nowego_pliku.endswith('.csv'):
      zapisz_csv(df, nazwa_nowego_pliku)
    elif nazwa_nowego_pliku.endswith('.pkl'):
      zapisz_pickle(df, nazwa_nowego_pliku)
    elif nazwa_nowego_pliku.endswith('.json'):
      zapisz_json(df, nazwa_nowego_pliku)
    else:
      print('Podano błędną nazwę pliku wyjściowego')
  #obsluga wejscia pkl
  elif nazwa_pliku.endswith('.pkl'):
    df = odczyt_pickle(nazwa_pliku)
    #wypisanie pliku przed modyfikacja
    print(df)
    for op in sys.argv[3:]:
      operacje_arr.append(Operacja(op))
    #edycja pliku
    edytujXY(df, operacje_arr)
    #zapis pliku
    if nazwa_nowego_pliku.endswith('.csv'):
      zapisz_csv(df, nazwa_nowego_pliku)
    elif nazwa_nowego_pliku.endswith('.pkl'):
      zapisz_pickle(df, nazwa_nowego_pliku)
    elif nazwa_nowego_pliku.endswith('.json'):
      zapisz_json(df, nazwa_nowego_pliku)
    else:
      print('Podano błędną nazwę pliku wyjściowego')
  #obsluga wejscia json
  elif nazwa_pliku.endswith('.json'):
    df = odczyt_json(nazwa_pliku)
    #wypisanie pliku przed modyfikacja
    print(df)
    for op in sys.argv[3:]:
      operacje_arr.append(Operacja(op))
    #edycja pliku
    edytujXY(df, operacje_arr)
    #zapis pliku
    if nazwa_nowego_pliku.endswith('.csv'):
      zapisz_csv(df, nazwa_nowego_pliku)
    elif nazwa_nowego_pliku.endswith('.pkl'):
      zapisz_pickle(df, nazwa_nowego_pliku)
    elif nazwa_nowego_pliku.endswith('.json'):
      zapisz_json(df, nazwa_nowego_pliku)
    else:
      print('Podano błędną nazwę pliku wyjściowego')
  else:
    print('Podano błędną nazwę pliku wejściowego')
