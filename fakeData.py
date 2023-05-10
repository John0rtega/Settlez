from faker import Faker
import random

# Need address, price, num_bedrooms, num_br, 
for i in range(50):
    fake=Faker()
    print(fake.street_address())
    print('State: NJ')
    print(random.randint(200000,800000))
    print('Number of bedrooms:', random.randint(1,6))
    print('Number of bathrooms:', random.randint(1,6))
    print('\n')


