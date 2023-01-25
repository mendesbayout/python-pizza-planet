from flask_seeder import Seeder
from my_project.models import Item
from my_project.seeders import ItemSeeder

seeder = Seeder()
seeder.seed(ItemSeeder, {'number_of_items': 100})
