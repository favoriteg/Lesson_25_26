# class Borsch:
#     value = 2
#     meat = 'beef'
#     ingredients = ['beet', 'potato', 'cabbage']
#
#     def boiled(self):
#         print('You boiled borsch')
#
# odessa = Borsch()

# class Human:
#     name = 'John'
#     surname = 'Doe'
#     phone = '+380931112233'
#     height = 170
#     weight = 80
#
#     def walk(self):
#         print('Human walk')
#
#     def eat(self):
#         print('Human eat')
#
#     def read(self):
#         print('Human read')
#
#     def run(self):
#         print('Human run')
#
#
# sten = Human()
# sten.name = 'Sten'
# print(sten.name)
#
# sten.height = 178
# print(sten.height)
# sten.weight = 85
# print(sten.weight)
#
# sten.run()
# sten.read()

# '''Задание 2
# Создайте класс «Город». Необходимо хранить в полях класса: название города,
# название региона, название
# страны, количество жителей в городе, почтовый индекс
# города, телефонный код города. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.'''

class City:
    name = 'default'
    country_name = 'Ukraine'
    population = 10000
    specialization = 'general'
    postal = 80980
    telephone_code = 48

    def __init__(self, name, country_name, population, specialization, postal, telephone_code):
        self.name = name
        self.population = population
        self.specialization = specialization
        self.postal = postal
        self.country_name = country_name
        self.telephone_code = telephone_code

    def show_population(self):
        return self.population

    def change_specialization(self, new_specialization):
        self.specialization = new_specialization

    def change_country_name(self, new_country):
        self.country_name = new_country

    def change_postal(self, new_postal):
        self.postal = new_postal

    def change_telephone_code(self, new_telephone):
        self.telephone_code = new_telephone





lviv = City('Lviv', 'Ukraine', 700000, 'general', 79007, 32)
print(lviv.name)
print(lviv.population)
print(lviv.show_population())
print(lviv.country_name)
print(lviv.specialization)
print(lviv.postal)
print(lviv.telephone_code)
lviv.change_country_name("Ukr")
print(lviv.country_name)
lviv.change_postal(12312312)
print(lviv.postal)
lviv.change_telephone_code(5453085843)
print(lviv.telephone_code)
