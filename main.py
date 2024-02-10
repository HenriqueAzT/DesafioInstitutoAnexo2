import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter
from scipy.stats import zscore

# Carregar dados do arquivo CSV
data = pd.read_csv('./dados.csv')  # Substitua pelo caminho do seu arquivo CSV

# Extrair colunas de posição (x e y)
positionsX = data['x'].values
positionsY = data['y'].values

# Calcular os scores Z das posições
zScores_X = zscore(positionsX)
zScores_Y = zscore(positionsY)

# Definir um limite para os scores Z. Pontos de dados com um scores Z maior do que este limite serão considerados valores atípicos, e portanto, não serão levados em conta.
limite = 3

# Remover os valores atípicos
positionsX = positionsX[np.abs(zScores_X) < limite]
positionsY = positionsY[np.abs(zScores_Y) < limite]

# Aumentar o tamanho da janela e a ordem polinomial
windowSize = 101  # Deve ser ímpar

# Função para calcular a média móvel
def movingAverage(data, windowSize):
    return np.convolve(data, np.ones(windowSize), 'valid') / windowSize

sigma = 10
smoothedPositionsX = gaussian_filter(positionsX, sigma)
smoothedPositionsY = gaussian_filter(positionsY, sigma)

# Aplicar o filtro Gaussiano várias vezes
for _ in range(50): 
    smoothedPositionsX = gaussian_filter(smoothedPositionsX, sigma)
    smoothedPositionsY = gaussian_filter(smoothedPositionsY, sigma)

# Carregar a imagem de fundo
backgroundImage = Image.open("./backgroundImage.jpg")

# Criar um objeto de desenho
draw = ImageDraw.Draw(backgroundImage)

# Desenhar os pontos suavizados na imagem de fundo
for x, y in zip(smoothedPositionsX, smoothedPositionsY):
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill='red')  # Desenha um círculo vermelho de raio 2 centrado no ponto (x, y)

# Exibir a imagem com os pontos suavizados
backgroundImage.show()

# Salvar a imagem
backgroundImage.save('output.png')