# entregas/6326146/main.py

from mod_estoque import (
    cadastrar_item,
    calcular_valor_estoque,
    listar_itens_em_falta,
)


def main():
    # Cadastrando pelo menos 3 itens
    item1 = cadastrar_item("Notebook Lenovo", 3, 3500.00)
    item2 = cadastrar_item("Mouse sem fio", 15, 60.00)
    item3 = cadastrar_item("Teclado Mecânico", 2, 250.00)

    estoque = [item1, item2, item3]

    # Calculando total
    valor_total = calcular_valor_estoque(estoque)
    print(f"Valor total do estoque imobilizado: R$ {valor_total:.2f}")

    # Verificando itens em falta (exemplo: estoque mínimo 5)
    minimo = 5
    itens_em_falta = listar_itens_em_falta(estoque, minimo)

    print(f"\n--- Itens em falta (Abaixo de {minimo} unidades) ---")
    for item in itens_em_falta:
        print(f"- {item['nome']}: {item['quantidade']} unidade(s)")


if __name__ == "__main__":
    main()
    