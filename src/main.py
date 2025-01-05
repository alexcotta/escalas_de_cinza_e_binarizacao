from PIL import Image
 
def exibe_imagem(imagem):
    imagem.show()

def converter_para_tons_de_cinza(imagem, imagem_name):
    imagem.convert("L").save("images/escala_cinza_"+imagem_name)

def binarizar(imagem, imagem_name):
    limiar = 200

    imagem = imagem.convert("L")
    largura, altura = imagem.size

    for x in range(largura):
        for y in range(altura):

            if imagem.getpixel((x,y)) < limiar:
                imagem.putpixel((x,y),0)

            else:
                imagem.putpixel((x,y),255)

    imagem.save("images/binarizada_"+imagem_name)


if __name__ == "__main__":
    path_imagens = "../src/images/"
    imagem = "gato2.jpg"

    try:
        imagem = Image.open(path_imagens+imagem)
        imagem_name = str(imagem.filename.split("/")[-1])#Nome da imagem último valor da lista
        
        converter_para_tons_de_cinza(imagem, imagem_name)
        binarizar(imagem, imagem_name)
        
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print("Não foi possível carregar a imagem "+imagem)
    
