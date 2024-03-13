from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Adatok betöltése és előkészítése
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Modell létrehozása és tanítása
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Modell kiértékelése
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Pontosság:", accuracy)
