# Avaliação de Viabilidade de Processo para RPA (PDD)

## 1. Processo Escolhido
**Cenário A:** Renomeação e arquivamento diário de comprovantes em PDF.

## 2. Descrição Resumida
Captura diária de arquivos PDF de comprovantes, leitura das informações padronizadas no nome do arquivo (data e número do documento), renomeação seguindo regra pré-estabelecida e movimentação para a pasta de destino.

## 3. Volume e Frequência
- **Frequência:** Diária.
- **Volume:** Alto e recorrente (dezenas a centenas de comprovantes por dia).

## 4. As entradas são estruturadas?
**Sim.** A informação necessária (data e número do documento) segue um padrão fixo e predeterminado no nome do arquivo original, sem depender de interpretação de texto livre ou de imagens.

## 5. As regras são claras e determinísticas?
**Sim.** A regra de renomeação é baseada unicamente em lógica condicional fixa, sem necessidade de interpretação, julgamento ou análise subjetiva. Para a mesma entrada, o resultado é sempre o mesmo.

## 6. Veredito
**Elegível para RPA.**
- **Regras claras:** a nomenclatura segue uma regra fixa e determinística.
- **Dados estruturados:** data e número do documento vêm em padrão previsível no nome do arquivo.
- **Repetibilidade:** o processo roda todos os dias, em alto volume e sempre da mesma forma.

Trata-se de um caso clássico de automação por robô, reduzindo tempo operacional e eliminando erros manuais de digitação e arquivamento.
