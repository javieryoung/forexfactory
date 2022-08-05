# vamos a tomar los datos de actual, forecast y previous y escribirlos en proporcion a actual
# es decir, actual siempre va a valer 1 y los demás valdrán proporcional a 1

import csv

print(",".join(['Time', 'Currency', 'Impact', 'Event', 'Actual', 'Forecast','Previous', 'Gmt time','Open','High','Low','Close','Volume', 'Low Impact', 'Medium Impact', 'High Impact']))


def remove_units(str):
    return str.replace('%', '').replace('K', '').replace('M', '').replace('B', '').replace('T', '').replace('<', '').replace('>', '').replace('k', '')


with open('./data.csv', "r") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if (row[4] != 'Actual'):
            if (row[4] == ''):
                row[4] = '0'
            actual = float(remove_units(row[4]))
            if (actual != 0):
                if (row[5] != ''): # muchas veces no hay forecast
                    forecast = float(remove_units(row[5]))
                if (row[6] != ''): # algunos no tienen previous
                    previous = float(remove_units(row[6]))



                if (row[6] != ''):
                    row[6] = str(previous / actual)
                if (row[5] != ''):
                    row[5] = str(forecast / actual)
                row[4] = "1"
                print(",".join(row))
            else:
                "TODO: no se que hacer con estas, por ahora las sacrifico"
                # print(",".join(row))
                