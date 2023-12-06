#skonczone
import random
import time


class Element:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __repr__(self):
        return f"{self.__priority} : {self.__data}"


class Heap:
    def __init__(self, tab=None):
        self.tab = tab
        self.heap_size = len(tab)
        if self.tab is not None:
            self.make_heap()

    def is_empty(self):
        if self.heap_size == 0:
            return True
        else:
            return False

    def peek(self):
        if self.heap_size == 0:
            return None
        return self.tab[0]

    def dequeue(self):
        if self.heap_size == 0:
            return None
        old_root = self.tab[0]
        self.tab[0], self.tab[self.heap_size - 1] = self.tab[self.heap_size - 1], self.tab[0]
        self.heap_size -= 1
        self.kopcowanie()
        return old_root

    def kopcowanie(self, idx=0):
        left_idx = self.left(idx)
        right_idx = self.right(idx)
        if right_idx >= self.heap_size:
            right_idx = left_idx
        while self.tab[left_idx] > self.tab[idx] or self.tab[right_idx] > self.tab[idx]:
            if self.heap_size == 2 and self.tab[left_idx] > self.tab[idx]:
                self.tab[0], self.tab[1] = self.tab[1], self.tab[0]
            elif self.heap_size == 2:
                break
            elif self.heap_size == 1:
                break
            elif self.tab[left_idx] > self.tab[idx] and self.tab[right_idx] > self.tab[idx]:
                if self.tab[left_idx] > self.tab[right_idx]:
                    self.tab[left_idx], self.tab[idx] = self.tab[idx], self.tab[left_idx]
                    idx = self.left(idx)
                    left_idx = self.left(idx)
                    right_idx = self.right(idx)
                else:
                    self.tab[right_idx], self.tab[idx] = self.tab[idx], self.tab[right_idx]
                    idx = self.right(idx)
                    left_idx = self.left(idx)
                    right_idx = self.right(idx)
            elif self.tab[left_idx] > self.tab[idx]:
                self.tab[left_idx], self.tab[idx] = self.tab[idx], self.tab[left_idx]
                idx = self.left(idx)
                left_idx = self.left(idx)
                right_idx = self.right(idx)
            else:
                self.tab[right_idx], self.tab[idx] = self.tab[idx], self.tab[right_idx]
                idx = self.right(idx)
                left_idx = self.left(idx)
                right_idx = self.right(idx)
            if left_idx >= self.heap_size or right_idx >= self.heap_size or idx >= self.heap_size:
                break

    def make_heap(self):
        idx = self.parent(self.heap_size - 1)
        for i in range(idx, -1, -1):
            self.kopcowanie(i)

    def enqueue(self, element):
        if self.tab is None:
            self.tab = []
        if self.heap_size == len(self.tab):
            self.tab.append(element)
            self.heap_size += 1
        else:
            self.tab[self.heap_size] = element
            self.heap_size += 1
        idx = self.heap_size - 1
        parent_idx = self.parent(idx)
        while self.tab[parent_idx] < self.tab[idx]:
            self.tab[parent_idx], self.tab[idx] = self.tab[idx], self.tab[parent_idx]
            idx = parent_idx
            parent_idx = self.parent(idx)

    def sort(self):
        while self.is_empty() is False:
            self.dequeue()
        return self.tab

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx >= 0:
            return parent_idx
        else:
            return 0

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.heap_size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        elem = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > elem:
           lista[j + 1] = lista[j]
           j = j - 1
        lista[j + 1] = elem
    return lista


def Shell_sort(lista):
    n = len(lista)
    h = 1
    counter = 0
    while h <= n / 3:
        h = ((3**counter) - 1) // 2
        counter += 1
    counter -= 2
    h = ((3**counter) - 1) // 2

    while h > 0:
        for i in range(h, n):
            elem = lista[i]
            j = i
            while j >= h and lista[j - h] > elem:
                lista[j] = lista[j - h]
                j -= h
            lista[j] = elem
        h = h // 3
    return lista


def main():
    priority = [5, 5, 7, 2, 5, 1, 7, 5, 1, 2]
    data = 'ABCDEFGHIJ'
    lista1 = []
    for i in range(len(priority)):
        lista1.append(Element(data[i], priority[i]))
    lista2 = lista1[:]

    lista3 = []
    for i in range(10000):
        lista3.append(random.randint(0, 99))
    lista4 = lista3[:]
    lista5 = lista3[:]


    print('Shell sort - stablilny\n', Shell_sort(lista1))
    print('Insertion sort - stablilny\n', insertion_sort(lista2))

    t_start = time.perf_counter()
    Shell_sort(lista3)
    t_stop = time.perf_counter()
    print("Czas obliczeń dla Shella:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    insertion_sort(lista4)
    t_stop = time.perf_counter()
    print("Czas obliczeń dla wstawiania:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    heap = Heap(lista5)
    heap.sort()
    t_stop = time.perf_counter()
    print("Czas obliczeń dla kopcowania:", "{:.7f}".format(t_stop - t_start))


main()

