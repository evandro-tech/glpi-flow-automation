# GLPI Flow Automation

## Objetivo

Automatizar a construção de fluxos do GLPI Taskflow.

## Roadmap

### Fase 1

Leitura e interpretação automática dos PDFs.

Entrada:

PDF

Saída:

- estrutura.json
- relatorio.txt

### Fase 2

Construção automática dos fluxos dentro do GLPI.

### Fase 3

Integração completa com chamados.

Entrada:

Número do chamado

Saída:

Fluxo criado automaticamente.

---

## Estrutura

```
pdf/
output/
logs/
src/
```

---

## Funcionamento

1. Coloque um único PDF dentro da pasta `pdf`.
2. Execute o projeto.
3. O sistema localizará o PDF.
4. O texto será extraído.
5. O fluxo será interpretado.
6. Será gerado um JSON estruturado.

---

## Ambiente

Python 3.11+

---

## Criar ambiente virtual

```
python -m venv .venv
```

Windows:

```
.venv\Scripts\activate
```

Linux:

```
source .venv/bin/activate
```

---

## Instalar dependências

```
pip install -r requirements.txt
```

---

## Executar

```
python src/main.py
```

---

## Regra principal do MVP

A pasta `pdf` deve conter exatamente 1 PDF.

Se houver:

- 0 PDFs → erro
- 2 ou mais PDFs → erro

---

## Tecnologias previstas

### PDF

- PyMuPDF
- pdfplumber

### OCR

- pytesseract
- Pillow

### Estrutura de Fluxos

- networkx

### Dados

- pandas

### Logs e Terminal

- rich

---

## Meta do MVP

Validar se conseguimos converter:

PDF → Estrutura de Fluxo

Antes de iniciar qualquer integração com GLPI.
