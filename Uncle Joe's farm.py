class AnimalDB():
    animals_list = list()

    def add_animal(self, animal):
        self.animals_list.append(animal)

class Animal:
    kind = ''
    name = ''
    weight = int()
    product = ''
    noise = ''

    def feed(self):
        print(f'{self.kind} {self.name} покормлен! "Ом-ном-ном"')

    def make_noise(self):
        print(f'{self.kind} {self.name} говорит: {self.noise}!')


class Egg_Givers(Animal):
    def harvest_eggs(self):
        print(f'Яйца собраны')

class Goose(Egg_Givers):
    kind = 'Гусь'
    noise = 'Га-га-га'

class Chiken(Egg_Givers):
    kind = 'Кура'
    noise = 'Ко-ко-ко'

class Duck(Egg_Givers):
    kind = 'Утка'
    noise = 'Кря-кря-кря'

class Milk_Givers(Animal):
    def harvest_milk(self):
        print(f'Молоко собрано')

class Cow(Milk_Givers):
    kind = 'Корова'
    noise = 'Му-у-у'

class Goat(Milk_Givers):
    kind = 'Коза'
    noise = 'Ме-е-е'

class Wool_Givers(Animal):
    def harvest_wool(self):
        print('Шерсть собрана')

class Sheep(Wool_Givers):
    kind = 'Овца'
    noise = 'Бе-е-е'

seryy = Goose()
seryy.name = 'Серый'
seryy.weight = 3
seryy.harvest_eggs()

belyy = Goose()
belyy.name = 'Белый'
belyy.weight = 2.5

manka = Cow()
manka.name = 'Манька'
manka.weight = 400

ko_ko = Chiken()
ko_ko.name = 'Ко-ко'
ko_ko.weight = 2

kukareku = Chiken()
kukareku.name = 'Кукареку'
kukareku.weight = 2.5

kriakva = Duck()
kriakva.name = 'Кряква'
kriakva.weight = 3

barashek = Sheep()
barashek.name = 'Барашек'
barashek.weight = 120

kudriavyy = Sheep()
kudriavyy.name = 'Кудрявый'
kudriavyy.weight = 100

roga = Goat()
roga.name = 'Рога'
roga.weight = 100

kopyta = Goat()
kopyta.name = 'Копыта'
kopyta.weight = 80

animaldb = AnimalDB()
animaldb.add_animal(seryy)
animaldb.add_animal(belyy)
animaldb.add_animal(manka)
animaldb.add_animal(ko_ko)
animaldb.add_animal(kukareku)
animaldb.add_animal(kriakva)
animaldb.add_animal(barashek)
animaldb.add_animal(kudriavyy)
animaldb.add_animal(roga)
animaldb.add_animal(kopyta)

def make_noise_together():
    for animal in AnimalDB.animals_list:
        animal.make_noise()

def weight_count():
    weight_sum = sum([animal.weight for animal in AnimalDB.animals_list])
    return weight_sum

def weight_compare():
    weight_max = max([animal.weight for animal in AnimalDB.animals_list])
    animal = [animal.name for animal in AnimalDB.animals_list if animal.weight == weight_max]
    return animal

def feed_everyone():
    for animal in AnimalDB.animals_list:
        animal.feed()

feed_everyone()
make_noise_together()
print(f'Общий вес животных {weight_count():.2f} кг.\n')
print(f'Самое тяжелое животное: {weight_compare()[0]}')
