print("Что вершит судьбу кода в пайчарм?")
print("Незримое существо или курсор?")
print("Подобно длани господня парящей над миром.")
print("Истинно то, что человек не властен даже над своей функцией.\n")

print("\033[1mДобро пожаловать в жестокий мир Берсерка.\033[0m")
print("Вы - отважный воин Гатс, отправляющийся на поиски мести и приключений.")

print("Вы стоите перед двумя дорогами: пойти налево (1) или направо (2)?")
vibor1 = input("Выберите направление (1/2): ")

if vibor1 == "1":
    print("Вы направились налево и вышли к реке. На берегу видите маленький домик.")
    print("Идти к дому (1) или вернуться и идти направо (2)?")
    vibor2 = input("Выберите действие (1/2): ")

    if vibor2 == "1":
        print("Подойдя к дому, вас встречает негр, который предлагает помощь. Отказаться (1) или согласиться (2)?")
        vibor3 = input("Выберите действие (1/2): ")

        if vibor3 == "1":
            print("Вы отказались от помощи и отправились дальше. Ваш тяжелый путь продолжается!")
        elif vibor3 == "2":
            print("Черный негр оказался магом и даровал вам новое оружие. Ваши силы возросли, и вы готовы к тяжелому пути!")
        else:
            print("Плохой выбор. Игра окончена.")
    elif vibor2 == "2":
        print("Вы решили вернуться и идти направо. Новый тяжелый путь ждет вас!")
    else:
        print("Плохой выбор. Игра окончена.")
elif vibor1 == "2":
    print("Вы свернули направо и увидели город. Вам нужно пройти через город или обойти его?")
    print("Пройти через город (1) или обойти (2)?")
    vibor4 = input("Выберите действие (1/2): ")

    if vibor4 == "1":
        print("Вы вошли в город, где вас ждут новые испытания и сражения!")
    elif vibor4 == "2":
        print("Вы обошли город, но на вас напали грабители. Смогли ли вы убить их не жалея?")
    else:
        print("Плохой выбор. Игра окончена.")
else:
    print("Плохой выбор. Игра окончена.")

print("prod.by Кернер, Корочкин, Скупков")