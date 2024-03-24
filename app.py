import pandas as pd

# Lendo o arquivo
arquivo_excel = "Dia1.xlsx"
df = pd.read_excel(arquivo_excel)

# Visualizar dados
print("Dados originais:")
print(df)

# Exemplo de edição de dados (Linha e coluna):
df.at[0, 'Vendedor'] = 'Gelado'

# Inserindo dados:
new_row = pd.DataFrame({'Dia': [1],'Vendedor': ['Junior'],'Produto': ['Carro'],'Unidades': [8],'Preço': [20.00]}, columns=df.columns)
df = pd.concat([df, new_row], ignore_index=True)

# Visualizar os dados atualizados
print("\nDados após editar e inserir:")
print(df)

# Salvar as alterações de volta para o Excel
arquivo_excel_saida = "Dia1_atualizado.xlsx"
df.to_excel(arquivo_excel_saida, index=False)
