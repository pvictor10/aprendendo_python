Dias_Da_Semana = ("abacaxi","laranja","maçã","manga","goiaba")
print(Dias_Da_Semana[2])

#criacao
pessoa = {
    "nome: pedro",
    "idade: 18",
    "endereço: Rua dona aparecida"
}
#recuperar valor
#print(pessoa["nome"])
#print(pessoa.get("nome"))

#alterar
pessoa["endereço"] = "Rua a"
#deletar
del pessoa["endereço"]
#print(pessoa)
#altualizar
pessoa.update({"nomeMae:": "Rosa", "nomePai": "Thiago", "Endereco": "Rua c"})
#print(pessoa)

pessoa.update({"endereco": "rua Z"})
