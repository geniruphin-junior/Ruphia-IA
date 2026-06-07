#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════
#  MOTEUR RUPHIA 9.0 – Moteur Mathématique Universel
# Auteur : Ruphin Bahati
# Modules : Sympy + Numpy
# Fonctions : Algèbre, Trigo, Statistiques, Physique, Calcul symbolique
# ════════════════════════════════════════════════════════════════

import sympy as sp
import numpy as np
import re
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

# ════════════════════════════════════════════════════════════════
# CONSTANTES PHYSIQUES
# ════════════════════════════════════════════════════════════════
CONSTANTES = {
    "pi": sp.pi,
    "e": sp.E,
    "i": sp.I,
    "c": 299792458,
    "g": 9.81,
    "G": 6.67e-11,
    "h": 6.626e-34,
    "hbar": 1.054e-34,
    "kb": 1.38e-23,
    "na": 6.022e23,
    "me": 9.11e-31,
    "qe": 1.6e-19,
}


# ════════════════════════════════════════════════════════════════
# CLASSE SYMPYENGINE – Procédure pas à pas
# ════════════════════════════════════════════════════════════════
class SympyEngine:
    def __init__(self, expr, var):
        self.expr = expr
        self.var = var
        self.steps = []

    def simplify(self):
        self.steps.append(f"Expression initiale : {self.expr}")
        res = sp.simplify(sp.trigsimp(self.expr))
        self.steps.append(f"Simplification → {res}")
        return res

    def expand(self):
        self.steps.append(f"Développement de {self.expr}")
        res = sp.expand(self.expr)
        self.steps.append(f"Développé → {res}")
        return res

    def factor(self):
        self.steps.append(f"Factorisation de {self.expr}")
        res = sp.factor(self.expr)
        self.steps.append(f"Factorisé → {res}")
        return res

    def derive(self):
        self.steps.append(f"Fonction : {self.expr}")
        res = sp.diff(self.expr, self.var)
        self.steps.append(f"Dérivée par rapport à {self.var} → {res}")
        return res

    def integrate(self):
        self.steps.append(f"Fonction : {self.expr}")
        res = sp.integrate(self.expr, self.var)
        self.steps.append(f"Intégrale par rapport à {self.var} → {res}")
        return res

    def solve(self):
        self.steps.append(f"Équation : {self.expr} = 0")
        res = sp.solve(self.expr, self.var)
        self.steps.append(f"Solutions pour {self.var} → {res}")
        if isinstance(res, list):
            if len(res) == 2:
                self.steps.append(f"x₁ = {res[0]}, x₂ = {res[1]}")
            elif len(res) == 1:
                self.steps.append(f"x = {res[0]}")
        return res

    def limit(self, point=0):
        self.steps.append(f"Expression : {self.expr}")
        res = sp.limit(self.expr, self.var, point)
        self.steps.append(f"Limite quand {self.var} → {point} → {res}")
        return res

    def series(self, point=0, n=5):
        self.steps.append(f"Série de Taylor de {self.expr} autour de {point}")
        res = sp.series(self.expr, self.var, point, n)
        self.steps.append(f"Développement limité → {res}")
        return res

    def matrix_ops(self):
        M = sp.Matrix([[1, 2], [3, 4]])
        self.steps.append(f"Matrice : {M}")
        det = M.det()
        inv = M.inv()
        eig = M.eigenvals()
        self.steps.append(f"Déterminant → {det}")
        self.steps.append(f"Inverse → {inv}")
        self.steps.append(f"Valeurs propres → {eig}")
        return {"det": det, "inv": inv, "eig": eig}


# ════════════════════════════════════════════════════════════════
# CLASSE NUMPYENGINE – Statistiques avancées
# ════════════════════════════════════════════════════════════════
class NumpyEngine:
    def __init__(self, data):
        self.data = np.array(data)

    def stats(self):
        return (
            f"📊 STATISTIQUES RUPHIA :\n"
            f"  - Moyenne   : {np.mean(self.data):.4f}\n"
            f"  - Médiane   : {np.median(self.data)}\n"
            f"  - Variance  : {np.var(self.data):.4f}\n"
            f"  - Écart-type: {np.std(self.data):.4f}\n"
            f"  - Somme     : {np.sum(self.data)}\n"
            f"  - Min / Max : {np.min(self.data)} / {np.max(self.data)}\n"
            f"  - Q1 / Q3   : {np.percentile(self.data,25)} / {np.percentile(self.data,75)}\n"
            f"  - Corrélation auto : {np.corrcoef(self.data)}"
        )


# ════════════════════════════════════════════════════════════════
# FONCTION PRINCIPALE – Fusion Sympy + Numpy
# ════════════════════════════════════════════════════════════════
def ruphia_ultra_engine(text):
    try:
        q = text.lower().strip()
        t = standard_transformations + (
            implicit_multiplication_application,
            convert_xor,
        )

        # Mode statistiques
        if "[" in q and "]" in q:
            list_str = re.search(r"\[.*\]", q).group()
            data = eval(list_str)
            return NumpyEngine(data).stats()

        # Conversion degrés → radians
        if "deg" in q:
            q = re.sub(r"(\d+)\s*deg", r"(\1*pi/180)", q)

        # Correction auto
        q = re.sub(r"(sin|cos|tan|log|sqrt)(\d+)", r"\1(\2)", q)

        # Parsing
        expr = parse_expr(q.replace("=", "-"), transformations=t, local_dict=CONSTANTES)
        syms = list(expr.free_symbols)
        var = syms[0] if syms else sp.Symbol("x")
        engine = SympyEngine(expr, var)

        # Détection automatique d’équation
        if "=" in q or "résous" in q or "solve" in q or "solution" in q:
            res = engine.solve()
        elif "dérive" in q or "diff" in q:
            res = engine.derive()
        elif "intègre" in q or "intégrale" in q:
            res = engine.integrate()
        elif "limite" in q:
            res = engine.limit()
        elif "série" in q:
            res = engine.series()
        elif "matrice" in q:
            res = engine.matrix_ops()
        elif "factorise" in q:
            res = engine.factor()
        elif "développe" in q:
            res = engine.expand()
        else:
            res = engine.simplify()

        # Résultat numérique
        try:
            val_dec = float(sp.N(res))
            engine.steps.append(f"Valeur numérique ≈ {val_dec:.6f}")
        except Exception:
            pass

        return "🧮 Procédure Ruphia :\n" + "\n".join(engine.steps)

    except Exception as e:
        return f"❌ Erreur Ruphia : {str(e)}"


# ════════════════════════════════════════════════════════════════
# MODE INTERACTIF
# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("═══ RUPHIA 9.0 : MOTEUR MATHÉMATIQUE ═══")
    print("Modules : Sympy + Numpy | Stats, Trigo, Physique, Algèbre, ODE, Matrices")
    while True:
        user_input = input("\n[KNG] Commande : ")
        if user_input.lower() in ["exit", "quitter", "q"]:
            print("🔚 Fin du moteur Ruphia.")
            break
        print(ruphia_ultra_engine(user_input))
