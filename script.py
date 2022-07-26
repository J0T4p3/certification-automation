from PIL import Image, ImageDraw, ImageFont
import pandas as pd

csv = pd.read_csv('curso_tranças.csv')


def generate_certifications():
    # get an image
    with Image.open("Certificado.jpg").convert("RGBA") as base:
        # Fonte da Assinatura
        signature_fnt = ImageFont.truetype("Fonts/Signature.ttf", 40)

        # Fonte padrão
        default_fnt = ImageFont.truetype("Fonts/default.ttf", 20)

        # Altura e Largura do arquivo
        l, a = base.size

        # Percorre a lista de pessoas para gerar os certificados
        for index, pessoa in csv.iterrows():
            # Fundo vazio para os textos
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

            # Cria um quadro em branco para criar o texto
            d = ImageDraw.Draw(txt)

            nome = pessoa['Nome']
            curso = pessoa['Curso']
            data = pessoa['Data']

            #  width = font.getsize(nome)[0]

            # Escreve no fundo vazio o texto criado
            d.text((610, 565), 'Projeto de Deus',
                   font=signature_fnt, fill=(0, 0, 0))

            # Nome
            d.text((l/2, 310), f'{nome}',
                   font=default_fnt, fill=(0, 0, 0))

            # Curso
            d.text((l/2, 385), f'{curso}',
                   font=default_fnt, fill=(0, 0, 0))

            dia, mes, ano = data.split('/')

            # Data
            d.text((440, 468), f"{dia}         {mes}       {ano}",
                   font=default_fnt, fill=(0, 0, 0))

            # Cola as duas imagens, uma em cima da outra
            out = Image.alpha_composite(base, txt)

            # Muda os caracteres especiais e espaços para salvar o nome do arquivo
            nome = nome.replace(" ", "_")
            curso = curso.replace(" ", "_")
            data = data.replace("/", "_")

       #      out.show()

            out.save(
                f"/home/reversejp/Documents/PDD/certificados/{nome}_{curso}_{data}.png", )


if __name__ == "__main__":
    generate_certifications()
