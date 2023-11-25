import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Чтение данных из CSV-файла
df = pd.read_csv(r'C:\\Users\\Аделина\\Desktop\\АИВТ ЛАБЫ\\маг.диссер\\готово\\СЕРАПЛОНОСТЬ\\ConsoleApplication1\\ConsoleApplication1\\sera2.csv', sep=',', encoding='cp1251')
print(df.columns)

# Создание графика
fig, ax = plt.subplots()
ax.axis('off')
# Создание графика для каждой группы из 100 строк
for i in range(0, len(df), 101):
    data = df.iloc[i:i+101]
    ax = fig.add_subplot(len(df)//101 + 1, 1, i//101+1)
    ax.plot(data['координата'], data['сера'])
    ax.set_title('Время ' + str(data['время'][i]) + 'с ') # Добавление подписи к каждому подграфику
    ax.set_xticks(np.arange(0, 110000, step=10000))
    ax.set_yticks(np.arange(0, 0.1, step=0.02))
fig.suptitle('Моделирование движения партий (сера)')

#график плотности
# Чтение данных из CSV-файла
df = pd.read_csv(r'C:\\Users\\Аделина\\Desktop\\АИВТ ЛАБЫ\\маг.диссер\\готово\\СЕРАПЛОНОСТЬ\\ConsoleApplication1\\ConsoleApplication1\\massiv2.csv', sep=',', encoding='cp1251')
print(df.columns)

# Создание графика
fig2, ax = plt.subplots()
ax.axis('off')
# Создание графика для каждой группы из 100 строк
for i in range(0, len(df), 101):
    data = df.iloc[i:i+101]
    ax = fig2.add_subplot(len(df)//101 + 1, 1, i//101+1)
    ax.plot(data['координата'], data['плотность'])
    ax.set_title('Время ' + str(data['время'][i]) + 'с ') # Добавление подписи к каждому подграфику
    ax.set_xticks(np.arange(0, 110000, step=10000))
    ax.set_yticks(np.arange(840, 880, step=10))
fig2.suptitle('Моделирование движения партий (плотность)')
# Отображение графиков
plt.show()