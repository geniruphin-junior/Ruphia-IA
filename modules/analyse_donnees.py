def analyser_donnees(donnees):
    return {
        "somme": sum(donnees),
        "moyenne": sum(donnees) / len(donnees) if donnees else 0,
        "max": max(donnees) if donnees else None,
        "min": min(donnees) if donnees else None,
    }
