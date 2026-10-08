from pathlib import Path
import fitz # PyMuPDF

class LeitorPDF:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extrair_texto(self):
        texto_completo = []

        with fitz.open(self.pdf_path) as pdf:
            total_paginas = len(pdf)

            for numero_pagina in range(total_paginas):
                pagina = pdf[numero_pagina]

                texto = pagina.get_text()

                texto_completo.append(
                    f"\n{'='*50}\n"
                    f"PÁGINA {numero_pagina + 1}\n"
                    f"{'='*50}\n\n"
                )

                texto_completo.append(texto)
        
        return "".join(texto_completo)    