# este archivo se encarga de tomar la información de las velas y medir la distancia maxima en la que se mueve como Distancia
# además vamos a medir la distancia en el otro sentido como el drawdown
# si cualquiera de los dos valores es negativo significa que se va hacia abajo

import csv

# print(",".join(['Time', 'Currency', 'Impact', 'Event', 'Actual', 'Forecast','Previous','Open','High','Low','Close','Volume', 'Low Impact', 'Medium Impact', 'High Impact']))
print(",".join(['Time', 'Currency', 'Impact', 'Event', 'Actual', 'Forecast','Previous', 'Low Impact', 'Medium Impact', 'High Impact', 'Distance', 'Drawdown']))

with open('./data.csv', "r") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if (row[7] != 'Open'):
            open = float(row[7])
            high = float(row[8])
            low = float(row[9])
            if (abs(open-high) > abs(open-low)):
                distance = abs(open-high)
                drawdown = -abs(open-low)
            else:
                distance = -abs(open-low)
                drawdown = abs(open-high)

            print(",".join(row[:7] + row[12:] + ["{:.9f}".format(distance), "{:.9f}".format(drawdown)]))