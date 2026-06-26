import pandas as pd

# 1. On crée des données scientifiques
donnees = {
    'Matière': ['Maths', 'Physique', 'Informatique', 'Chimie'],
    'Note': [18, 17, 20, 15],
    'Coeff': [5, 4, 5, 3]
}

# 2. On transforme ça en "DataFrame" (le tableau magique de Pandas)
df = pd.DataFrame(donnees)

# 3. On fait un calcul scientifique : la moyenne pondérée
df['Total'] = df['Note'] * df['Coeff']
moyenne = df['Total'].sum() / df['Coeff'].sum()

print("--- TABLEAU DE BORD RUPHIA ---")
print(df)
print(f"\nMoyenne Générale : {moyenne:.2f}/20")

# 4. On l'enregistre en fichier Excel (CSV)
df.to_csv('notes_ruphia.csv', index=False)
print("\n✅ Fichier 'notes_ruphia.csv' créé avec succès !")
