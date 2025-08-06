# criando um hashmap com dict
hashmap = {
    "nome": "milena",
    "idade": 24,
    "cidade": "manaus"
}

# acessando valores
print(hashmap["nome"])     # milena
print(hashmap.get("idade")) # 23

# adicionando novo par chave-valor
hashmap["profissao"] = "Recepcionista"

# verificando se chave existe
if "cidade" in hashmap:
    print("cidade:", hashmap["cidade"])

# removendo uma chave
del hashmap["idade"]

# iterando sobre o hashmap
for chave, valor in hashmap.items():
    print(chave, "->", valor)
