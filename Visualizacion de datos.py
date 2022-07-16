from collections import Counter
from matplotlib import pyplot as plt


years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020,2030,2040,2050]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3,1075.9, 2862.5,1075.9, 2862.5 ]
plt.plot(years, gdp, color='g', marker='o', linestyle='dashed') #configurando el grafico
plt.title("Nominal GDP", color='magenta') #adicionando el titulo del grafico
plt.ylabel("Miles de millones", color='red')
plt.xlabel("valores que asume el GDP nominal")
plt.grid(True, linestyle='dashed', color='blue')
plt.show()


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
xs=[i+0.1 for i, _ in enumerate(movies) ]
plt.bar(xs, num_oscars, color='orange')
plt.grid(True, linestyle='dashed', color='grey')
plt.ylabel('# de primiasiones')
plt.xlabel("filmes que a populacao gosta")
plt.title('meus filmes favoritos')
plt.xticks([i + 0.1 for i, movies in enumerate(movies)], movies)
plt.show()

#haciendo un histograma
grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]
decile=lambda grade: grade // 10*10
histograma=Counter(decile(grade) for grade in grades)
plt.bar([x for x in histograma.keys()], histograma.values(), 8, color='grey')
plt.grid(True, linestyle='dashed', color='black', linewidth=0.4)
plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("decil", style='italic')
plt.ylabel("# de alunos")
plt.title("distribuicao das notas do teste 1")
plt.show()
#graficos de linha
variance=[1,2,4,8,16,32,64,128,256]
bias_squared=[256,128,64,32,16,8,4,2,1]
invento=[2,40,135,69,55,97,49,106,341]
total_error=[x+y for x, y in zip(variance,bias_squared)]
xs=[i for i, _ in enumerate(variance)]
plt.plot(xs, variance, color='r', linestyle=':', label='variance', linewidth=.4)
plt.plot(xs, bias_squared, color='b', linestyle='--', label='bias_squared')
plt.plot(xs, total_error, color='g', linestyle='dashed', label='total_error')
plt.plot(xs, invento, color='grey', linewidth=2, linestyle=':', label='invento')
plt.xlabel("numeros de interes comun", style='italic', weight=1000)
plt.ylabel("complejidad de la mierda")
plt.legend(loc='best')
plt.xlabel("complexidade do modelo")
plt.title("compromisso entre polarizacao e varianza")
plt.show()
#graficos de dispersion
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
plt.xlabel("Frecuencias del fenomeno", color='red', style='italic', weight=1000)
plt.ylabel("categoria observada", color='g', style='normal', weight=800)

for label, friends_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                               xy=(friends_count, minute_count),
                               xytext=(5,-5),
                               textcoords='offset points')
plt.title("frecuencias vs categorias observadas")
plt.grid(True, linestyle='--')
plt.show()

plt.pie([0.5, 0.05, .45])
plt.show()
