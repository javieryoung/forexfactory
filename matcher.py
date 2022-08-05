# este archivo se encargará de matchear el calendario en UTC con la informacion de la vela (tambien en UTC)
import csv

def symbol_to_file(symbol):
    if symbol=='EUR':
        return 'EURUSD.csv'
    if symbol=='USD':
        return 'EURUSD.csv'
    if symbol=='AUD':
        return 'AUDUSD.csv'
    if symbol=='GBP':
        return 'GBPUSD.csv'
    if symbol=='NZD':
        return 'NZDUSD.csv'
    if symbol=='CAD':
        return 'USDCAD.csv'
    if symbol=='CHF':
        return 'USDCHF.csv'
    if symbol=='JPY':
        return 'USDJPY.csv'


print('Time', 'Currency', 'Impact', 'Event', 'Actual', 'Forecast','Previous', 'Gmt time','Open','High','Low','Close','Volume')
with open('./calendar_pruebas.csv', "r") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:

        if row[1] is not None:
            file = './datos-crudos/dukascopy-1m/' + symbol_to_file(row[1])

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

