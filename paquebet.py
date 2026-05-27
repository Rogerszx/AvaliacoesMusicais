import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12, 8)

nome_arquivo = 'C:\\Users\\Roger\\Downloads\\peca.jpg' 

img_bgr = cv2.imread(nome_arquivo)

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("1. Imagem Original (RGB)")
plt.axis('off') 
plt.show()

altura, largura, canais = img_rgb.shape
    
print("Propriedades da Imagem:")
print(f"Altura: {altura} pixels")
print(f"Largura: {largura} pixels")
print(f"Número de canais (cores): {canais}")
print(f"Tipo dos dados: {img_rgb.dtype}")
print(f"Valor Mínimo do pixel: {img_rgb.min()}")
print(f"Valor Máximo do pixel: {img_rgb.max()}")

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

plt.imshow(img_gray, cmap='gray')
plt.title("2. Imagem em Escala de Cinza")
plt.axis('off')
plt.show()

img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

plt.imshow(img_blur, cmap='gray')
plt.title("3. Imagem Suavizada")
plt.axis('off')
plt.show()

x, thresh_simples = cv2.threshold(img_blur, 127, 255, cv2.THRESH_BINARY)

valor_otsu, thresh_otsu = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
print(f"Valor de corte calculado automaticamente pelo OTSU: {valor_otsu}")

figura, axes = plt.subplots(1, 5, figsize=(20, 5))

imagens = [img_rgb, img_gray, img_blur, thresh_simples, thresh_otsu]
titulos = ['1. Original (RGB)', '2. Cinza', '3. Suavizada', '4. Limiar Simples', f'5. OTSU (T={valor_otsu:.0f})']

for i in range(5):
        if i == 0:
            axes[i].imshow(imagens[i])
        else:
            axes[i].imshow(imagens[i], cmap='gray')
            
        axes[i].set_title(titulos[i])
        axes[i].axis('off')

plt.tight_layout()
plt.show()