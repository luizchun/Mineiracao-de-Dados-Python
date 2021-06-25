import pandas as pd
import matplotlib.pyplot as plt

input_file = 'Dataset/hepatitis-clean.data'  # Importação dos Dados
df = pd.read_csv(input_file, usecols=[
                 'MAL-ESTAR', 'IDADE', 'SEXO'])
temperaturas = df['MAL-ESTAR'].tolist()
IDADE = df['IDADE'].tolist()
SEXO = df['SEXO'].value_counts(sort=True)
print(SEXO)
labels = 'Viveu', 'Morreu', ''

plt.title('Pessoas')
plt.xlabel('idade')
plt.ylabel('Quantidade')
plt.hist(temperaturas, 15, rwidth=0.9, edgecolor='black')

plt.show()

plt.title('IDADE')
plt.xlabel('IDADE')
plt.ylabel('Quantidade')
plt.hist(IDADE, 15, rwidth=0.9, edgecolor='black')

plt.show()

plt.title("SEXO")
plt.pie(SEXO, labels=labels, autopct='%1.1f%%')
plt.show()
