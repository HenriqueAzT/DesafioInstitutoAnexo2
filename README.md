# Suavização de Posições Estimadas da Tag

Este projeto tem como objetivo suavizar as posições estimadas de uma tag em um sistema de localização em tempo real (RTLS - Real Time Location System). As posições estimadas são sujeitas a interferências ambientais, e a suavização é realizada para melhorar a precisão dos dados.

## Funcionalidades

-   Leitura de dados a partir de um arquivo CSV contendo as posições estimadas da tag.
-   Remoção de outliers utilizando a técnica de Z-score.
-   Aplicação de média móvel e filtro Gaussiano para suavização das posições.
-   Visualização das posições suavizadas sobre uma imagem de fundo.
