import pandas as pd


def main():

    collumns = ['CLASSE', 'IDADE', 'SEXO', 'ESTERÓIDE', 'ANTIVIRAIS', 'FADIGA', 'MAL-ESTAR', 'ANOREXIA', 'GRANDE FÍGADO', 'FÍGADO', 'BATIDO', 'ARANHAS' , 'ASCITAS', 'VARICES', 'BILIRRUBINA', 'ALK PHOSPHATE', 'SGOT', 'ALBUMINA', 'PROTIME', 'HISTOLOGIA']  # Todas as colunas
    collumns2 = ['CLASSE', 'IDADE', 'SEXO', 'ESTERÓIDE', 'ANTIVIRAIS', 'FADIGA', 'MAL-ESTAR', 'ANOREXIA', 'GRANDE FÍGADO', 'FÍGADO', 'BATIDO', 'ARANHAS' , 'ASCITAS', 'VARICES', 'BILIRRUBINA', 'ALBUMINA']  # Colunas que serão utilizadas
    continuousData = ['BILIRRUBINA', 'ALBUMINA']  #dados numéricos contínuos

    input_file = '../Datasets/hepatitis.data' 
    df = pd.read_csv(input_file, delim_whitespace=True,names=collumns, usecols=collumns2, na_values='?')


    for campo in collumns2: 
        if campo in continuousData: 
            method = 'mean'
        else:  # Se dado não pertença ao conjuntos de dados contínuos será utilizado a moda
            method = 'mode'

        if method == 'mean':
            #  média
            mean = round(df[campo].mean(), 1)
            df[campo].fillna(mean, inplace=True)
        else:
            #  moda
            mode = df[campo].mode()[0]
            df[campo].fillna(mode, inplace=True)

    df.to_csv('../Datasets/hepatitis-clean.data', index=False)

    print(df.info())


if __name__ == "__main__":
    main()
