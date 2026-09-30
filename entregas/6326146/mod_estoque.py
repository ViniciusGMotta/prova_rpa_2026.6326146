# entregas/6326146/mod_estoque.py


def cadastrar_item(nome: str, quantidade: int, preco_unitario: float) -> dict:
    """Retorna um dicionário representando o item."""
    return {
        "nome": nome,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
    }


def calcular_valor_estoque(itens: list) -> float:
    """Calcula a soma de quantidade * preco_unitario de todos os itens."""
    total = 0.0
    for item in itens:
        total += item["quantidade"] * item["preco_unitario"]
    return total


def listar_itens_em_falta(itens: list, minimo: int) -> list:
    """Retorna nova lista com itens de quantidade menor que minimo."""
    em_falta = []
    for item in itens:
        if item["quantidade"] < minimo:
            em_falta.append(item)
    return em_falta
