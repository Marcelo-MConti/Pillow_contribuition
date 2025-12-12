import neon
import sepia
import dither
import primary
from PIL import Image

def main():
   path = "paisagem.png"
   img = Image.open(path)

   img2 = Image.open("mario.png")

   result = neon.neon_glow(img2,alpha = 0.3)
   result.save("neon_glow.png")
   print("Imagem com efeito Neon gerada!")

   sepia.sepia(img).save("sepia.png")
   print("Imagem com efeito Sépia gerada!")

   dither.convert_dithering(img2).save("dither.png")
   print("Imagem com efeito Dither gerada!")

   primary.convert_primay(img).save("primary.png")
   print("Imagem com efeito Primary gerada!")


if __name__ == "__main__":
    main()
