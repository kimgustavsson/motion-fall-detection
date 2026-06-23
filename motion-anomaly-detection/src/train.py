from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from src.data import load_data, preprocess_data
from src.model import build_model


def train(path: str):
    df = load_data(path)
    df = preprocess_data(df)

    X = df.drop(columns=['label'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = build_model()
    model.fit(X_train)

    y_pred = model.predict(X_test)
    y_pred = [1 if x == -1 else 0 for x in y_pred]

    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    train('data/raw/dataset.csv')
