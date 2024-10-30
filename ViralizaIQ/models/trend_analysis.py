from sklearn.cluster import KMeans

class TrendAnalyzer:
    def __init__(self):
        self.model = KMeans(n_clusters=5)

    def fit(self, data):
        self.model.fit(data)

    def predict_trend(self, data):
        return self.model.predict(data)
