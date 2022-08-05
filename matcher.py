# este archivo se encargará de matchear el calendario en UTC con la informacion de la vela (tambien en UTC)
# se tiene que tener en la carpeta dukas-copy1m como sigue:

# dukascopy-1m
# |
# |-- AUDUSD
# |     |
# |     |-- 2019.csv
# |     |-- 2020.csv
# |     |-- ...
# |-- EURUSD
# |     |
# |     |-- 2019.csv
# |     |-- 2020.csv
# |     |-- ...
# ...

import csv

def symbol_to_folder(symbol):
    if symbol=='EUR':
        return 'EURUSD'
    if symbol=='USD':
        return 'EURUSD'
    if symbol=='AUD':
        return 'AUDUSD'
    if symbol=='GBP':
        return 'GBPUSD'
    if symbol=='NZD':
        return 'NZDUSD'
    if symbol=='CAD':
        return 'USDCAD'
    if symbol=='CHF':
        return 'USDCHF'
    if symbol=='JPY':
        return 'USDJPY'


print('Time', 'Currency', 'Impact', 'Event', 'Actual', 'Forecast','Previous', 'Gmt time','Open','High','Low','Close','Volume')
with open('./calendar_utc_formateado.csv', "r") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if len(row) > 1:
            year = row[0][6:10]

            file = './datos-crudos/dukascopy-1m/' + symbol_to_folder(row[1]) + '/' + year + '.csv'

            with open(file, "r") as csvfile2:
                datareader2 = csv.reader(csvfile2)
                for candle in datareader2:
                    if candle[0] == row[0] + '0': # encontre la candle con esa fecha

                        with open('./datos-crudos/noticias.csv', "r") as csvfile3:
                            datareader3 = csv.reader(csvfile3)
                            for noticias in datareader3:
                                if noticias[0] == row[3]: # encontré la noticia
                                    print(",".join(row + candle[1:] + noticias[1:]))
                                    break

