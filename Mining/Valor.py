import pandas as pd
import statistics
import matplotlib.pyplot as plt

input_file = 'Datasets\hepatitis-clean.data'  
df = pd.read_csv(input_file)
columns = list(df.columns)

IDADELista = df['IDADE'].tolist()
IDADEListaOrdenado = sorted(df['IDADE'].tolist())

IDADEMedia = df['IDADE'].mean()
IDADEModa = df['IDADE'].mode()
IDADEMediana = statistics.median(IDADELista)
IDADEPontoMedio = (
    IDADEListaOrdenado[0] + IDADEListaOrdenado[len(IDADEListaOrdenado)-1])/2

print("Tendência Central de batimentos cardíacos cavalos com cólicas")
print("Média = " + str(IDADEMedia))
print("Moda = " + str(IDADEModa[0]))
print("Mediana = " + str(IDADEMediana))
print("Ponto Médio = " + str(IDADEPontoMedio))

IDADEAmplitude = IDADEListaOrdenado[len(
    IDADEListaOrdenado)-1] - IDADEListaOrdenado[0]
IDADEDesvioPadrao = statistics.pstdev(IDADELista)
IDADEVariancia = statistics.pvariance(IDADELista)
IDADECoeficienteVariacao = (IDADEDesvioPadrao/IDADEMedia)*100

print("\nMedidas de dispersão de batimentos cardíacos cavalos com cólicas")
print("Amplitude = " + str(IDADEAmplitude))
print("Desvio Padrão = " + str(IDADEDesvioPadrao))
print("Variância = " + str(IDADEVariancia))
print("Coeficiente de Variação = " +
      str(round(IDADECoeficienteVariacao, 2)) + "%\n")

IDADE = df['IDADE']
IDADE_descri = IDADE.describe()

q1 = IDADE_descri['25%']
mediana = IDADE_descri['50%']
q2 = IDADE_descri['75%']

s_q1 = "{0:.2f}".format(q1)
s_mediana = "{0:.2f}".format(mediana)
s_q2 = "{0:.2f}".format(q2)

font_1 = {'family': 'serif', 'color': 'darkred', 'size': '14'}

plt.figure(figsize=(6, 7))
plt.boxplot(IDADE)
plt.title('Boxplot Batimentos Cardíacos')
plt.text(1, q1, s_q1, fontdict=font_1)
plt.text(1, mediana, s_mediana, fontdict=font_1)
plt.text(1, q2, s_q2, fontdict=font_1)
plt.ylabel('Batimentos')
plt.show()