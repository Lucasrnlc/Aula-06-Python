clientes = [
    {"nome":"Ana","cel": "11111","empresa": "FIAT"},
    {"nome":"Pedro","cel": "22222","empresa": "INTEL"},
    {"nome":"Maria","cel": "33333","empresa": "SEBRAE"},
    {"nome":"Felipe","cel": "44444","empresa": "MICROSOFT"}
]

empresa_digitada = input ("Digite o nome da empresa: ")
for cliente in clientes:
    if cliente ["empresa"] == empresa_digitada:
        print(cliente)

# Cadastrar um novo cliente

print("Cadastrando um novo Cliente")
nome = input("Digite o nome do novo Cliente: ")
celular = input("Digite o nome número do Cliente: ")
empresa = input("Digite a empresa do Cliente: ")

novo_cliente = {
    "nome": nome,
    "celular": celular,
    "empresa": empresa
}
clientes.append(novo_cliente)
print(clientes)

#Remover cliente


print("Remova um Cliente pelo nome")
nome_excluir = input("Digite o nome do Cliente que desejas remover: ")
for cliente in clientes:
    if cliente["nome"] == nome_excluir:
        clientes.remove(cliente)
        break

print(clientes)


