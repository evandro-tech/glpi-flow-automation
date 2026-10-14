import json
from pathlib import Path
from leitor_pdf import LeitorPDF

PDF_DIR = Path("pdf")
OUTPUT_DIR = Path("output")


def localizar_pdf():
    pdfs = list(PDF_DIR.glob("*.pdf"))

    if len(pdfs) == 0:
        raise Exception("Nenhum PDF encontrado na pasta pdf")

    if len(pdfs) > 1:
        raise Exception(
            f"Foram encontrados {len(pdfs)} PDFs. Mantenha apenas um."
        )

    return pdfs[0]

def salvar_elementos(elementos):
    OUTPUT_DIR.mkdir(exist_ok=True)

    arquivo_saida = OUTPUT_DIR / "elementos.json"

    with open(arquivo_saida, "w", encoding="utf-8") as arquivo:
        json.dump(elementos, arquivo, ensure_ascii=False, indent=2)

    return arquivo_saida

def main():
    pdf = localizar_pdf()

    print(f"PDF encontrado: {pdf.name}")

    leitor = LeitorPDF(pdf)

    elementos = leitor.extrair_elementos()

    arquivo = salvar_elementos(elementos)

    print(f"Elementos do PDF salvos em: {arquivo}")

if __name__ == "__main__":
    main()
