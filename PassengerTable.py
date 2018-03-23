import pandas as pd
from faker import Factory
fake = Factory.create()
import re

pas_index=range(1,3362400+1)
Passengers = pd.DataFrame(columns=['FirstName','LastName', 'Gender', 'Address' ,'DOB', 'Phone', 'Email', 'PasspNo'], index=pas_index)

Passengers.index.name = 'id'

for i in pas_index:
    person = fake.profile()
    lastN = fake.last_name()
    fone = fake.phone_number()

    Passengers.loc[i] = pd.Series({'FirstName':person['name'], 'LastName':lastN, 'Gender':person['sex'], 'Address':person['address'].replace('\n', ' '),  'DOB':person['birthdate'], 'Phone':fone, 'Email':person['mail'], 'PasspNo':person['ssn']})

Passengers.to_csv("Passenger.csv")