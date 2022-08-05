# cuenta las noticias vecines
# es decir, cuenta cuantas noticias (y de que tipo) tiene cada noticia sucediendo a la vez

# ademas de separar por hora separo por simbolo, si hay dos noticias a la vez, una de EUR y otra de CAD las cuento por separado

# TODO: se pierde el ultimo chunk de noticias. Por ahora lo agrego a mano
# TODO: no deberiamos separar por USD porque todos los simbolos tienen a USD (ya sea base o contrapartida)

import csv

print(",".join(['Time', 'Currency', 'Impact', 'Event', 'Actual', 'Forecast','Previous', 'Open','High','Low','Close','Volume', 'Low Impact', 'Medium Impact', 'High Impact']))

date = ''
symbol = ''
simultaneous_news = []
with open('./joined.csv', "r") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[0] != date or row[1] != symbol:

            severities = [0, 0, 0]
            for sn in simultaneous_news:
                if sn[2] == 'Low Impact Expected':
                    severities[0] += 1
                if sn[2] == 'Medium Impact Expected':
                    severities[1] += 1
                if sn[2] == 'High Impact Expected':
                    severities[2] += 1
            severities[0] = str(severities[0])
            severities[1] = str(severities[1])
            severities[2] = str(severities[2])
            for sn in simultaneous_news:
                print(",".join(sn + severities))

            simultaneous_news = [row]
            date = row[0]
            symbol = row[1]
        else:
            simultaneous_news.append(row)
