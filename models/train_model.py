import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score
import joblib
#Загрузка датасета
df = pd.read_csv('data/UCI_Credit_Card.csv')

#print(df.head())
#print(df.isna().sum())
#df.info()

y = df['default.payment.next.month']
X = df.drop(columns=['default.payment.next.month','ID'])

#Препроцессинг
cat_features = X.select_dtypes("int64").columns
num_features =  X.select_dtypes("float64").columns

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, num_features),
        ('cat', 'passthrough', cat_features)
    ])
#Деление на обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42)

#Модель
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', GradientBoostingClassifier())])

clf.fit(X_train, y_train)
print(f'accuracy {accuracy_score(y_test, clf.predict(X_test))}')

joblib.dump(clf, 'models/model_v1.pkl')
print('Обучение завершено, модель сохранена')