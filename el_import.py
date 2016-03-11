#!/usr/bin/env python3

import psycopg2

try:
    conn = psycopg2.connect("dbname='estudiolivre' \
                             user='estudiolivre' \
                             host='192.168.122.2' \
                             password='estudiolivre'")
except:
    print("I am unable to connect to the database")
else:
    print("Conectado")

cur = conn.cursor()

sql = 'SELECT title, \
              to_char(to_timestamp(publishDate), \'DD/MM/YYYY\') as Data, \
              array_agg(fileName) as Arquivos, \
              p.actualClass \
           FROM estudiolivre.publication p LEFT JOIN estudiolivre.filereference f \
           ON p.id = f.publicationId \
           GROUP BY p.id \
           ORDER BY publishDate DESC \
           LIMIT 100 '

cur.execute(sql)

colnames = [desc[0] for desc in cur.description]

rows = cur.fetchall()

print("Colunas: ", colnames, "\n")

for idx, row in enumerate(rows):
    data = zip(colnames, row)

    for value in data:
        print(value)

    print("\n")
