import string

import flowers
import tree
import bush
from extenderr import *
import random
#----------------------------------------------
class Container:
    def __init__(self):
        self.store = []
    def file_in(self, strArray):
        arrayLen = len(strArray)
        i = 0  # Индекс, задающий текущую строку в массиве
        figNum = 0
        while i < arrayLen:
            str = strArray[i]
            key = int(str)  # преобразование в целое
            if key == 1:  # признак дерева
                i += 1
                if i >= len(strArray) - 1:
                    return 0
                plant = Tree(strArray[i], strArray[i + 1])
                i += 2
            elif key == 2:  # признак куста
                i += 1
                if i >= len(strArray) - 1:
                    return 0
                plant = Bush(strArray[i], strArray[i + 1])
                i += 2
            elif key == 3:
                i += 1
                if i >= len(strArray) - 1:
                    return 0
                plant = Flowers(strArray[i], strArray[i + 1])
                i += 2
            else:
                # что-то пошло не так. Должен быть известный признак
                # Возврат количества прочитанных растений
                return figNum
            # Количество пробелами растений увеличивается на 1
            if i == 0:
                return figNum
            figNum += 1
            self.store.append(plant)
        return figNum

    def random_in(self, plantsNumbers):
        if plantsNumbers < 1:
            return False
        for i in range(plantsNumbers):
            letters = string.ascii_lowercase
            rand_string = ''.join(random.choice(letters) for i in range(random.randint(1, 15)))
            key = random.randint(1, 3)
            if key == 1:
                plant = Tree(rand_string, random.randint(1, 100))
            elif key == 2:
                plant = Bush(rand_string, random.randint(1, 12))
            else:
                plant = Flowers(rand_string, random.randint(1, 3))
            self.store.append(plant)

    def Print(self):
        print("Container is store", len(self.store), "plants:\n")
        for plant in self.store:
            plant.Print()
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} plants:\n".format(len(self.store)))
        for plant in self.store:
            plant.Write(ostream)
            ostream.write("\n")
        pass

    def sort(self):
        length = len(self.store)
        swapped = True
        start_index = 0
        end_index = length - 1

        while (swapped == True):

            swapped = False

            # проход слева направо
            for i in range(start_index, end_index):
                if (self.store[i].quotient() > self.store[i + 1].quotient()):
                    # обмен элементов
                    self.store[i], self.store[i + 1] = self.store[i + 1], self.store[i]
                    swapped = True

            # если не было обменов прерываем цикл
            if (not (swapped)):
                break

            swapped = False

            end_index = end_index - 1

            # проход справа налево
            for i in range(end_index - 1, start_index - 1, -1):
                if (self.store[i].quotient() > self.store[i + 1].quotient()):
                    # обмен элементов
                    self.store[i], self.store[i + 1] = self.store[i + 1], self.store[i]
                    swapped = True

            start_index = start_index + 1
