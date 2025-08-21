import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

#Simulando dados de clientes
data = pd.DataFrame({
    'idade': [25, 40, 35, 50, None],
    'renda_mensal': [3000, 7000, 5000, 10000, 4000],
    'score_credito': [600, 750, 680, 800, 620],
    'atrasos_anteriores': [2, 0, 1, 0, 3],
    'inadimplente': [1, 0, 0, 0, 1]  # 1 = inadimplente, 0 = adimplente
})

#Separando features e target
X = data.drop('inadimplente', axis=1)
y = data['inadimplente']

#Dividindo em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Criando a pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),         # Preenche valores ausentes
    ('scaler', StandardScaler()),                        # Normaliza os dados
    ('model', RandomForestClassifier(random_state=42))   # Modelo de classificação
])

#Treinando o modelo
pipeline.fit(X_train, y_train)

#Fazendo previsões
y_pred = pipeline.predict(X_test)

#Avaliando o modelo
print(classification_report(y_test, y_pred))



