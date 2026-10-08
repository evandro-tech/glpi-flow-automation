from pathlib import Path

PDF_DIR = Path("pdf")


def validar_pdf():
    pdfs = list(PDF_DIR.glob("*.pdf"))

    if len(pdfs) == 0:
        raise Exception("Nenhum PDF encontrado na pasta pdf")

    if len(pdfs) > 1:
        raise Exception(
            f"Foram encontrados {len(pdfs)} PDFs. Mantenha apenas um."
        )

    return pdfs[0]


def main():
    pdf = validar_pdf()

    print("=" * 50)
    print("GLPI FLOW AUTOMATION")
    print("=" * 50)
    print(f"PDF encontrado: {pdf.name}")


if __name__ == "__main__":
    main()
