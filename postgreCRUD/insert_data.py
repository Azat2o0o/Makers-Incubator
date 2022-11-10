import peewee
from models import Category, Product

def add_category(name):
    try:
        row = Category(name = name.lower().strip())
        row.save()
        print(f'Сохранили категорию {name.strip()}!')
    except (peewee.IntegrityError, peewee.InternalError):
        print('Такая категория уже существует!')

def add_product(title, category_name, price):
    try:
        category = Category.select().where(Category.name == category_name.lower().strip()).get()
        category_exist = True
    except peewee.DoesNotExist:
        category_exist = False

    if category_exist:
        row = Product(
            title = title.lower().strip(),
            price = price,
            category = category
        )
        row.save()
        print(f'Сохранили товар {title.strip()}')
    else:
        print(f'Категории {category_name} не существует!')

# add_category('Платья')
# add_category('Джинсы')
# add_category('Футболки')
# add_category('Обувь')

# add_product('Lacoste кроссовки', 'Обувь', 15290)
# add_product('Lining кроссовки', 'Обувь', 6470)
# add_product('Lining футболка', 'Футболки', 4200)
# add_product('lining футболка', 'футболки', 2100)