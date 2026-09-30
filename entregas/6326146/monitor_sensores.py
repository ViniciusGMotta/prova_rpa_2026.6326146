# entregas/6326146/monitor_sensores.py


def main():
    """Ponto de entrada da Questão 2."""
    leituras = [36.5, 41.2, 38.0, 105.0, 37.4, -999.0, 39.1, 40.0]

    soma_validas = 0.0
    qtd_validas = 0
    interrompido = False

    for leitura in leituras:
        if leitura == -999.0:
            print(
                f"[FALHA] Sensor corrompido ({leitura}). "
                "Interrompendo monitoramento..."
            )
            interrompido = True
            break
        elif leitura > 80.0:
            print(
                f"[DESCARTE] Leitura de {leitura}°C "
                "fora da faixa: ignorada."
            )
            continue
        else:
            print(f"[OK] Leitura de {leitura}°C registrada.")
            soma_validas += leitura
            qtd_validas += 1

    # O resumo só aparece se o loop NÃO foi interrompido
    if not interrompido:
        print("\n--- Resumo das Leituras ---")
        if qtd_validas > 0:
            media = soma_validas / qtd_validas
            print(f"Quantidade de leituras válidas: {qtd_validas}")
            print(f"Média das leituras: {media:.2f}°C")
        else:
            print("Nenhuma leitura válida foi registrada.")


if __name__ == "__main__":
    main()
    