# Створити словник оцінок передбачуваних студентів (Ключ – ПІ студента, значення –
# список оцінок студентів). Знайти найуспішнішого і самого слабенького за середнім балом.


d = {
    'Muniz Adrienne': [3, 4, 5, 4],
    'Coleman Tanya': [3, 5, 4, 4],
    'April Amy': [1, 2],
}


def marks(a):
    return sum(a) / len(a)
# for i in d.values():
#     a = sum(i) / len(i)
sorted_students = sorted(d.keys(), key=lambda student: marks(d[student]))
# Сортування КЛЮЧІВ від найменшого до найбільшого середнього аріфметичного в залежності від ЗНАЧЕНЬ цих ключів.

# У "сортед_стьюдентс" сортуються ключі словника (key=) за значеннями, переданими у функцію lambda student:
# marks(d[student])). Тобто ЗНАЧЕННЯ КЛЮЧЕЙ передаються у def marks(a) функцію, знаходиться середнє арифметичне,
# а далі по значенням сортуються від найменшого до найбільшого КЛЮЧІ (тобто імена).
print(sorted_students[-1], 'has the best arithmetic mean.')
print(sorted_students[0], 'has the worst arithmetic mean.')

# я очень старалась на украинском писать ))