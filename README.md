# Titanic
Projeto de  ciência de dados com Machine lmachine learning (Classificação)

Descrição do Projeto: Previsão de Sobrevivência no Titanic

O objetivo deste projeto foi aplicar as etapas completas de um processo de Ciência de Dados utilizando o dataset clássico do Titanic, disponível na plataforma Kaggle. As principais etapas realizadas estão descritas abaixo:

Exploração e Tratamento de Dados:

Importação do dataset para o ambiente de trabalho.

Realização de tratamentos necessários, incluindo a limpeza de valores ausentes e conversão de variáveis categóricas para numéricas.

Criação de visualizações gráficas para análise exploratória, destacando padrões e correlações nos dados.

Balanceamento da Base de Dados:

Identificou-se que a base de dados estava desbalanceada, com uma quantidade maior de passageiros que não sobreviveram em relação aos que sobreviveram.

Para corrigir esse desbalanceamento, foi utilizado o método SMOTE (Synthetic Minority Oversampling Technique), que permite a criação de novas amostras sintéticas para a classe minoritária, garantindo um treinamento mais equilibrado dos modelos.

Separação de Dados de Treino e Teste:

Divisão do dataset em bases de treino e teste para garantir a validação eficaz dos modelos.

Treinamento e Avaliação de Algoritmos de Classificação:

Implementação de diversos algoritmos de classificação, como Regressão Logística, Random Forest e Support Vector Machine.

Análise comparativa do desempenho dos modelos com base em métricas como acurácia e matriz de confusão.

Seleção da Regressão Linear como o modelo mais adequado para o problema.

Deploy do Modelo:

Salvamento do modelo treinado e implementação em um ambiente de produção.

Desenvolvimento de uma interface funcional utilizando a biblioteca Streamlit, permitindo interação direta com usuários finais.

Implementação de Interface Interativa:

Criação de telas intuitivas que permitem a entrada de dados pelo usuário e exibem a previsão de sobrevivência com base nas características fornecidas.

Tecnologias Utilizadas:

Python: Linguagem principal para análise, modelagem e deploy.

Bibliotecas: Pandas, NumPy, Matplotlib, Scikit-learn, SMOTE e Streamlit.

Plataforma Kaggle: Fonte do dataset utilizado.

Impacto e Aprendizado: O projeto demonstrou um ciclo completo de um pipeline de ciência de dados, desde o tratamento inicial dos dados até a entrega de uma aplicação funcional e interativa. Além disso, destaca-se pela aplicação do SMOTE para balancear a base de dados, garantindo maior imparcialidade no treinamento dos modelos, e pelo uso de técnicas de aprendizado supervisionado para prever a sobrevivência no Titanic com precisão.




