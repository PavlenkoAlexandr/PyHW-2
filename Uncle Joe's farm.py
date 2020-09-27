class Animal:
    kind = ''
    name = ''
    weight = int()
    product = ''
    noise = ''

    def feed(self, food):
        self.weight += food

    def make_noise(self):
        print(f'{self.kind} {self.name} говорит: {self.noise}!')

    def harvest(self, number, quantity):
        print(f'Ресурс "{self.product.lower()}" в количестве {number} {quantity} собран.')

class Goose(Animal):
    kind = 'Гусь'
    product = 'Перо'
    noise = 'Га-га-га'

class AnimalDB():
    animals_list = list()

    def add_animal(self, animal):
        self.animals_list.append(animal)

class Cow(Animal):
    kind = 'Корова'
    product = 'Молоко'
    noise = 'Му-у-у'

class Chiken(Animal):
    kind = 'Кура'
    product = 'Яйцо'
    noise = 'Ко-ко-ко'

class Duck(Animal):
    kind = 'Утка'
    product = 'Перо'
    noise = 'Кря-кря-кря'

class Sheep(Animal):
    kind = 'Овца'
    product = 'Шерсть'
    noise = 'Бе-е-е'

class Goat(Animal):
    kind = 'Коза'
    product = 'Молоко'
    noise = 'Ме-е-е'


seryy = Goose()
seryy.name = 'Серый'
seryy.weight = 3
seryy.feed(0.1)
seryy.make_noise()
seryy.harvest(200, 'гр.')

print('')

belyy = Goose()
belyy.name = 'Белый'
belyy.weight = 2.5
belyy.feed(0.2)
belyy.make_noise()
belyy.harvest(150, 'гр.')

print('')

manka = Cow()
manka.name = 'Манька'
manka.weight = 400
manka.feed(10)
manka.make_noise()
manka.harvest(10, 'л.')

print('')

ko_ko = Chiken()
ko_ko.name = 'Ко-ко'
ko_ko.weight = 2
ko_ko.feed(0.1)
ko_ko.make_noise()
ko_ko.harvest(1, 'шт.')

print('')

kukareku = Chiken()
kukareku.name = 'Кукареку'
kukareku.weight = 2.5
kukareku.feed(0.1)
kukareku.noise = 'Ку-ка-ре-ку'
kukareku.make_noise()

print('')

kriakva = Duck()
kriakva.name = 'Кряква'
kriakva.weight = 3
kriakva.make_noise()
kriakva.feed(0.1)
kriakva.harvest(100, 'гр.')

print('')

barashek = Sheep()
barashek.name = 'Барашек'
barashek.weight = 120
barashek.feed(1)
barashek.make_noise()
barashek.harvest(6, 'кг.')

print('')

kudriavyy = Sheep()
kudriavyy.name = 'Кудрявый'
kudriavyy.weight = 100
kudriavyy.feed(2)
kudriavyy.make_noise()
kudriavyy.harvest(5, 'кг.')

print('')

roga = Goat()
roga.name = 'Рога'
roga.weight = 100
roga.make_noise()
roga.feed(1)
roga.harvest(5, 'л.')

print('')

kopyta = Goat()
kopyta.name = 'Копыта'
kopyta.weight = 80
kopyta.make_noise()
kopyta.feed(1)
kopyta.harvest(4, 'л.')

print('')

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

def weight_count():
    weight_sum = sum([animal.weight for animal in AnimalDB.animals_list])
    return weight_sum

print(f'Общий вес животных {weight_count():.2f} кг.\n')

def weight_compare():
    weight_max = max([animal.weight for animal in AnimalDB.animals_list])
    animal = [animal.name for animal in AnimalDB.animals_list if animal.weight == weight_max]
    return animal

print(f'Самое тяжелое животное: {weight_compare()[0]}')