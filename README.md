# Desafio-Desenvolvedor-target
1. **Resposta**: 77    [**implmentação no arquivo**](https://github.com/MateusRampim/Desafio-Desenvolvedor-target/blob/main/implementacoes.py)

2. **Explicações**:

   a) Soma de 2 em 2, logo 9.

   b) Dobra o valor, logo 128.

   c) Sequência de \(x^2\), com \(x = 7\), então \(49\).

   d) \(x^2\) mas com \(x\) andando de 2 em 2. Próximo \(x = 10\), então \(x^2 = 100\).

   e) Fibonacci, resposta = \(x-1 + x-2 = 13\).

   f) O próximo número é 200, pois todos os números começam com a letra D e o próximo depois de 19 é duzentos.

3.
  ![**Imagem do banco**](https://i.imgur.com/43ZPyr9.png)
  
  [**SQL no arquivo**](https://github.com/MateusRampim/Desafio-Desenvolvedor-target/blob/main/Sql%20busca.sql).

4. [**implmentação no arquivo**](https://github.com/MateusRampim/Desafio-Desenvolvedor-target/blob/main/implementacoes.py)




5. **Para calcular a velocidade média do carro**:

   Devemos considerar o percurso total a 90 km/h e 15 minutos parados.

   O tempo total é calculado como:

   ```plaintext
   Tempo total = (Distância / Velocidade) + Tempo de parada
                = (125 km / 90 km/h) + (15 minutos / 60 minutos/hora)
                = 1,3889 horas + 0,25 horas
                = 1,6389 horas
   ```
   
   Então, a velocidade média é calculada como:
   ```plaintext
   Velocidade média = Distância / Tempo total
                 = 125 km / 1,6389 horas
                 ≈ 76,27 km/h
   ```
   O carro se afasta de Ribeirão Preto a essa velocidade, e o caminhão vem em direção a Ribeirão Preto a 80 km/h.

   Cálculo das distâncias:

   Distância percorrida pelo carro:
   ```plaintext
   Distância = Velocidade média * Tempo
          = 76,27 km/h * T
   ````
   Distância percorrida pelo caminhão:
   ```plaintext
   Distância = Distância total - (Velocidade caminhão * Tempo)
          = 125 km - 80 km/h * T
   ````
   Igualando as duas distâncias:
   ```plaintext
   76,27 * T = 125 - 80 * T
   156,27 * T = 125
   T ≈ 0,80 horas
   ````
   O carro está a:
   ```plaintext
   Distância do caminhão = Distância total - (Velocidade caminhão * Tempo)
                       = 125 km - 80 km/h * 0,80 horas
                       ≈ 61 km
   ````
   O caminhão está a:
   ```plaintext
   Distância do caminhão = Distância total - (Velocidade caminhão * Tempo)
                       = 125 km - 80 km/h * 0,80 horas
                       ≈ 61 km
   ````
   **Na margem de erro, os dois veículos estão à mesma distância de Ribeirão Preto.**

   
