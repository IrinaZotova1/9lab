def nom1():
    import os
    from PIL import Image, ImageFilter
    x = r"D:\СПБГУПТД\АиП\9 лаб\91"
    y = r"D:\СПБГУПТД\АиП\9 лаб\2"
    #возвращает список, содержащий имена файлов и директорий в каталоге, заданном путем path
    a = os.listdir(x)
    lions = []
    for li in a:
        #правильно соединяет переданный путь path к одному или более компонентов пути *paths
        p1 = os.path.join(y, li)
        lions.append(li)
        for i in lions:
            photo = Image.open(i)
            pho = photo.convert('L')
            pho.save(p1)
nom1()
def nom2():
    import os
    from PIL import Image, ImageFilter
    x = r"D:\СПБГУПТД\АиП\9 лаб"
    y = r"D:\СПБГУПТД\АиП\9 лаб\2"
    a = os.listdir(x)
    print(a)
    lions = []

    for li in a:
        #условие, для исключения обработки файлов в папках
        if os.path.isfile(os.path.join(x, li)):
            #выбирает файлы, которые оканчиваютя на ".jpg" или ".png"
            if li.endswith(".jpg") or li.endswith(".png"):
                p1 = os.path.join(y, li)
                lions.append(li)
            if not li.endswith(".jpg"):
                print(f"Есть файлы других расширений: {li}")
        for i in lions:
            photo = Image.open(i)
            pho = photo.convert('L')
            pho.save(p1)


def nom3():
    import csv
    itog_stoim = 0
    print("Нужно купить:")
    with open("Книга1.csv", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tovar = row['Продукт']
            kolichestvo = int(row['Количество'])
            price = int(row['Цена'])
            cost = kolichestvo * price
            itog_stoim = itog_stoim + cost
            print(f"{tovar} - {kolichestvo} шт. за {price} руб.")
    print("Итоговая сумма:", itog_stoim, "руб.")