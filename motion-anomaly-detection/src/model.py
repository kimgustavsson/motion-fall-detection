from sklearn.ensemble import IsolationForest


def build_model(random_state: int = 42) -> IsolationForest:
    return IsolationForest(n_estimators=100, contamination='auto', random_state=random_state)
