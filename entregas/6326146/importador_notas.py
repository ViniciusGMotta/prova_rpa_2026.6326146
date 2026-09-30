# entregas/6326146/importador_notas.py

import logging

import pandas as pd

# 1. Configurando o logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("importacao.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def importar_notas(caminho: str) -> float:
    """Lê um CSV de notas com pandas e retorna o total faturado."""
    try:
        df = pd.read_csv(caminho)

        # Log INFO para cada nota lida
        for _, row in df.iterrows():
            logging.info(
                "Nota: %s | Cliente: %s | Valor: R$ %.2f",
                row["nota"],
                row["cliente"],
                row["valor"],
            )

        # Soma com pandas
        total = float(df["valor"].sum())
        logging.info("Total faturado consolidado: R$ %.2f", total)
        return total

    except FileNotFoundError:
        logging.error("Arquivo não encontrado: %s", caminho)
        return 0.0
    except pd.errors.EmptyDataError:
        logging.error("O arquivo CSV está vazio: %s", caminho)
        return 0.0
    except Exception as e:
        logging.error("Erro inesperado durante a importação: %s", e)
        return 0.0
    finally:
        logging.info("Tentativa de importação finalizada.")


if __name__ == "__main__":
    print("--- Teste 1: Arquivo Válido ---")
    importar_notas("notas.csv")

    print("\n--- Teste 2: Arquivo Inexistente ---")
    importar_notas("caminho_inexistente.csv")
    