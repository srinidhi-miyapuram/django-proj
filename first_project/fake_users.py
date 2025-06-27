import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

from first_app.models import UserDetails
from faker import Faker

fakegen = Faker()

def usersgeneration(count = 10):
    for _ in range(count):
        user = UserDetails.objects.get_or_create(
            firstName = fakegen.first_name(),
            lastName = fakegen.last_name(),
            email = fakegen.email()
        )[0]

if __name__ == "__main__":
    print("Popuating data into the database")
    usersgeneration(20)
    print("Populating completed")