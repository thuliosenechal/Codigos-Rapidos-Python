import random


dir_path = 'C:\\Users\\Etica\\Documents\\VisualStudioCode\\'

db_name = input('DB Name: ')
owner_name = input('Owner name: ')
table_name = input('Table Name: ')
qtd_campos = int(input('Quantidade de campos da tabela: '))
qtd_linhas = int(input('\nQuantidade de linhas a gerar: '))

campos_name = {}
campos_tipo = {}

db_name = f'use {db_name}'
file_name = f'INSERT_TABLE_{table_name}.sql'

# Recuperar nome do campo e o tipo
for i in range(1, qtd_campos+1):
    nome = input(f'Entre com o nome do {i}º campo: ')
    tipo = int(input(f'''Entre com o tipo do {i}º campo: 
    
     1 - Numérico
     2 - Varchar
     3 - Date
     
     >: '''))

    campos_name[i] = nome
    campos_tipo[i] = tipo


insert = f'insert into {owner_name}.{table_name} ('

# Cria a primeira parte do insert
for i in range(1, qtd_campos+1):
    if i == qtd_campos:
        insert += f'{campos_name[i]}) values ('
    else:
        insert += f'{campos_name[i]}, '


# Cria a parte dos values do insert
for i in range(1, qtd_campos+1):
    if i == qtd_campos:
        insert += f'{campos_name[i]}_value)'
    else:
        insert += f'{campos_name[i]}_value, '



with open(f'{dir_path}{file_name}', 'w') as arquivo:
    arquivo.write(db_name)
    arquivo.write('\n\n')
    
    for i in range(1, qtd_linhas+1):
        insert_tmp = insert
        for j in range(1, qtd_campos+1):
            if campos_tipo[j] == 1:
                old = f'{campos_name[j]}_value'
                new = str(i)
                insert_tmp = insert_tmp.replace(old, new)
            elif campos_tipo[j] == 2:
                old = f'{campos_name[j]}_value'
                new = f"'{campos_name[j]}_{str(i)}'"
                insert_tmp = insert_tmp.replace(old, new)
            elif campos_tipo[j] == 3:
                old = f'{campos_name[j]}_value'
                new = 'GETDATE()'
                insert_tmp = insert_tmp.replace(old, new)

        arquivo.write(insert_tmp)
        arquivo.write('\n')