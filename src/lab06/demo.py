from models import Book, Ebook, AudioBook
from container import TypedCollection, Displayable, Scorable

def demo1():
    print("=== сценарий1: типизированная коллекция ===")
    coll = TypedCollection[Book]()
    coll.add(Book("Война и мир", "Толстой", 1869, 1300))
    coll.add(Book("1984", "Оруэлл", 1949, 328))
    coll.add(Ebook("Преступление и наказание", "Достоевский", 1866, 672, 3.2))

    print("список:")
    for b in coll.get_all():
        print(b.display())

    print("\nfind по названию '1984':")
    found = coll.find(lambda b: b.name == "1984")
    print(found.display() if found else "None")

    print("\nfind несуществующей:")
    found2 = coll.find(lambda b: b.name == "zzz")
    print("None" if found2 is None else found2.display())

    print("\nfilter книги после 1900:")
    after = coll.filter(lambda b: b.year > 1900)
    for b in after:
        print(b.display())

    print("\nmap -> имена:")
    names = coll.map(lambda b: b.name)
    print(names)

    print("\nmap -> годы+10:")
    years = coll.map(lambda b: b.year + 10)
    print(years)

def demo2():
    print("\n=== сценарий2: Displayable (протокол) ===")
    col = TypedCollection[Displayable]()
    col.add(Book("Детство", "Толстой", 1852, 150))
    col.add(Ebook("Улисс", "Джойс", 1922, 1056, 5.0))
    col.add(AudioBook("Тихий Дон", "Шолохов", 1928, 1500, 28.0, "Литвинов"))

    for item in col:
        print(item.display())

def demo3():
    print("\n=== сценарий3: Scorable ===")
    col = TypedCollection[Scorable]()
    col.add(Book("Анна Каренина", "Толстой", 1877, 864))
    col.add(Ebook("Преступление и наказание", "Достоевский", 1866, 672, 3.2, drm_protected=True))
    col.add(AudioBook("Евгений Онегин", "Пушкин", 1833, 320, 8.0, "Иванов"))

    for item in col:
        print(f"{item.display()} -> score: {item.score()}")

    scores = col.map(lambda x: x.score())
    print("\nоценки:", scores)

    high = col.filter(lambda x: x.score() > 5)
    print("высокий рейтинг >5:")
    for h in high:
        print(h.display())

if __name__ == "__main__":
    demo1()
    demo2()
    demo3()