preco = float(input("Digite o preço do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

desconto = preco * (percentual_desconto / 100)
preco_final = preco - desconto

print(f"O preço final com desconto é: R$ {preco_final:.2f}")