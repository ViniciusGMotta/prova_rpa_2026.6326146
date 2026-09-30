# entregas/6326146/config_conexao.py


def main():
    """Ponto de entrada da Questão 1."""
    # 1. Declaração das variáveis com os tipos corretos
    ENDPOINT_URL: str = "https://api.exemplo.com/v1"
    PORTA: int = 443
    TAXA_AMOSTRAGEM: float = 1.5
    USA_HTTPS: bool = True

    # 2. Dicionário reunindo os quatro parâmetros
    parametros = {
        "ENDPOINT_URL": ENDPOINT_URL,
        "PORTA": PORTA,
        "TAXA_AMOSTRAGEM": TAXA_AMOSTRAGEM,
        "USA_HTTPS": USA_HTTPS,
    }

    # 3. Relatório de validação com type()
    print("=== Relatório de Validação de Conexão ===")
    for chave, valor in parametros.items():
        print(
            f"Parâmetro: {chave:<15} | "
            f"Valor: {str(valor):<25} | "
            f"Tipo: {type(valor)}"
        )


if __name__ == "__main__":
    main()
    