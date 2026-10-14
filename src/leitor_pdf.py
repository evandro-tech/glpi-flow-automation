import pymupdf # PyMuPDF

class LeitorPDF:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extrair_elementos(self):
        paginas = []

        with pymupdf.open(self.pdf_path) as pdf:
            for numero_pagina, pagina in enumerate(pdf, start=1):
                paginas.append(
                    {
                        "pagina": numero_pagina,
                        "largura": round(pagina.rect.width, 2),
                        "altura": round(pagina.rect.height, 2),
                        "elementos": self._extrair_elementos_pagina(pagina),
                    }
                )

        return {"paginas": paginas}

    def _extrair_elementos_pagina(self, pagina):
        linhas = []

        for bloco in pagina.get_text("dict")["blocks"]:
            for linha in bloco.get("lines", []):
                direcao = linha.get("dir", (1, 0))
                for span in linha["spans"]:
                    texto = " ".join(span["text"].split())
                    if not texto:
                        continue

                    x0, y0, x1, y1 = span["bbox"]
                    linhas.append(
                        {
                            "texto": texto,
                            "x0": x0,
                            "y0": y0,
                            "x1": x1,
                            "y1": y1,
                            "horizontal": abs(direcao[0]) >= abs(direcao[1]),
                        }
                    )

        elementos = []
        linhas.sort(key=lambda item: (item["y0"], item["x0"]))

        for linha in linhas:
            elemento_encontrado = None
            maior_sobreposicao = 0

            if linha["horizontal"]:
                for elemento in elementos:
                    if not elemento["horizontal"]:
                        continue

                    altura_linha = max(
                        linha["y1"] - linha["y0"],
                        elemento["ultima_altura"],
                    )
                    distancia_vertical = linha["y0"] - elemento["ultima_y1"]
                    if not -0.25 * altura_linha <= distancia_vertical <= 0.5 * altura_linha:
                        continue

                    largura_comum = min(linha["x1"], elemento["ultimo_x1"]) - max(
                        linha["x0"], elemento["ultimo_x0"]
                    )
                    largura_menor = min(
                        linha["x1"] - linha["x0"],
                        elemento["ultimo_x1"] - elemento["ultimo_x0"],
                    )
                    sobreposicao = largura_comum / largura_menor if largura_menor > 0 else 0

                    if sobreposicao >= 0.5 and sobreposicao > maior_sobreposicao:
                        elemento_encontrado = elemento
                        maior_sobreposicao = sobreposicao

            if elemento_encontrado is None:
                elementos.append(
                    {
                        **linha,
                        "ultima_y1": linha["y1"],
                        "ultima_altura": linha["y1"] - linha["y0"],
                        "ultimo_x0": linha["x0"],
                        "ultimo_x1": linha["x1"],
                    }
                )
                continue

            elemento_encontrado["texto"] += " " + linha["texto"]
            elemento_encontrado["x0"] = min(elemento_encontrado["x0"], linha["x0"])
            elemento_encontrado["y0"] = min(elemento_encontrado["y0"], linha["y0"])
            elemento_encontrado["x1"] = max(elemento_encontrado["x1"], linha["x1"])
            elemento_encontrado["y1"] = max(elemento_encontrado["y1"], linha["y1"])
            elemento_encontrado["ultima_y1"] = linha["y1"]
            elemento_encontrado["ultima_altura"] = linha["y1"] - linha["y0"]
            elemento_encontrado["ultimo_x0"] = linha["x0"]
            elemento_encontrado["ultimo_x1"] = linha["x1"]

        return [
            {
                "texto": elemento["texto"],
                "x0": round(elemento["x0"], 2),
                "y0": round(elemento["y0"], 2),
                "x1": round(elemento["x1"], 2),
                "y1": round(elemento["y1"], 2),
            }
            for elemento in sorted(elementos, key=lambda item: (item["y0"], item["x0"]))
        ]