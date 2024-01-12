# Importer les bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Charger les données depuis un fichier Excel
file_path = 'Depression_DataTraining.xlsx'
df = pd.read_excel(file_path)

# Diviser les données en features (X) et target (y)
X = df[['Age', 'Indicateur_Sociale', 'Test_Depression']]
y = df['DegréDépression']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer le modèle SVM
model = SVC(kernel='linear', C=1.0, random_state=42)

# Entraîner le modèle sur l'ensemble d'entraînement
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
predictions = model.predict(X_test)

# Évaluer les performances du modèle
accuracy = accuracy_score(y_test, predictions)

# Évaluer les performances du modèle avec zero_division=1
report = classification_report(y_test, predictions, zero_division=1)

# Afficher les résultats
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", report)
# Maintenant, vous pouvez utiliser le modèle pour faire des prédictions sur de nouvelles données.
# Remplacez les valeurs suivantes par les nouvelles données que vous souhaitez prédire.
print("-------------------Prédiction---------------");
nouvelle_valeur_age=input("Entrez une valeur");
nouvelle_valeur_indicateur_sociale=input("Entrez une valeur");
nouvelle_valeur_test_estime_de_soi=input("Entrez une valeur");
new_data = pd.DataFrame({
    'Age': [nouvelle_valeur_age],
    'Indicateur_Sociale': [nouvelle_valeur_indicateur_sociale],
    'Test_Estime_De_Soi': [nouvelle_valeur_test_estime_de_soi]
})

# Faire des prédictions sur les nouvelles données
predictions_new_data = model.predict(new_data)

# Afficher les prédictions
print("Predictions for new data:")
print(predictions_new_data)