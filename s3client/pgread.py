import sqlalchemy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(sqlalchemy.__version__)


def connect(user='postgres', password='P@ssw0rd', db='mart', host='localhost', port=5432):
    '''
    :param user:
    :param password:
    :param db:
    :param host:
    :param port:
    :return: connection and a metadata object
    '''
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect()

#print(con)
#print(meta)

#for table in meta.tables:
#    print(table)

occ = meta.tables['occupancy_fact']
print(occ.c)
#['occupancy_fact.id', 'occupancy_fact.owner_key', 'occupancy_fact.operator_key', 'occupancy_fact.group_key', 'occupancy_fact.site_key', 'occupancy_fact.date_key', 'occupancy_fact.time_key', 'occupancy_fact.operational_spaces', 'occupancy_fact.occupied_spaces', 'occupancy_fact.created']

#for row in con.execute(occ.select()):
#    print(row)

clause = occ.select().where(occ.c.date_key == 20170612)
for row in con.execute(clause):
    print(row)

# pandas
#df = pd.read_sql(clause, con)
#print(df)

''' creating table
from sqlalchemy import Table, Column, Integer, String, ForeignKey

slams = Table('slams', meta,
    Column('name', String, primary_key=True),
    Column('country', String)
)

results = Table('results', meta,
    Column('slam', String, ForeignKey('slams.name')),
    Column('year', Integer),
    Column('result', String)
)

# Create the above tables
meta.create_all(con)

# inserting
clause = slams.insert().values(name='Wimbledon', country='United Kingdom')
con.execute(clause)

# insert batch
victories = [
    {'slam': 'Wimbledon', 'year': 2003, 'result': 'W'},
    {'slam': 'Wimbledon', 'year': 2004, 'result': 'W'},
    {'slam': 'Wimbledon', 'year': 2005, 'result': 'W'}
]

con.execute(meta.tables['results'].insert(), victories)

## select

results = meta.tables['result']

for row in con.execute(results.select()):
...     print row
...

clause = results.select().where(results.c.year == 2005)

for row in con.execute(clause):
...     print row
...
(u'Wimbledon', 2005, u'W')
Bonus tip: If you happen to use Pandas for data manipulations, reading data is as simple as 
df = pd.read_sql(clause, con)

# JOIN http://docs.sqlalchemy.org/en/latest/core/selectable.html#sqlalchemy.sql.expression.Join

from sqlalchemy import select, alias
j = alias(
    select([j.left, j.right]).\
        select_from(j).\
        with_labels(True).\
        correlate(False),
    name=name
)


'''