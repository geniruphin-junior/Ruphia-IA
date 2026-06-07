import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
class MathSuperEngine:
    """Moteur de calcul scientifique haute performance pour Ruphia V4."""
   
    def __init__(self):
        self.x = sp.symbols('x')
        # Transformations pour permettre x^2 au lieu de x**2 et 2x au lieu de 2*x
        self.transformations = (standard_transformations + (implicit_multiplication_application,))
    def _parse(self, expr_str):
        """Convertit la chaine de l'utilisateur en expression SymPy sécurisée."""
        # Remplace ^ par ** pour la syntaxe Python
        expr_str = expr_str.replace('^', '**')
        # Gestion des équations avec '='
        if '=' in expr_str:
            left, right = expr_str.split('=')
            return parse_expr(f"{left.strip()} - ({right.strip()})", transformations=self.transformations)
        return parse_expr(expr_str, transformations=self.transformations)
    def execute(self, cmd, expr_str):
        """Routeur centralisé."""
        try:
            expr = self._parse(expr_str)
           
            # --- ALGEBRE ---
            if cmd == "solve":
                return f"Solution: {sp.solve(expr, self.x)}"
           
            elif cmd == "diff":
                return f"Dérivée: {sp.diff(expr, self.x)}"
           
            elif cmd == "int":
                return f"Intégrale: {sp.integrate(expr, self.x)} + C"
           
            elif cmd == "simplify":
                return f"Simplification: {sp.simplify(expr)}"
           
            # --- TRIGONOMETRIE ---
            elif cmd == "trig_simp":
                return f"Forme simplifiée: {sp.trigsimp(expr)}"
           
            elif cmd == "trig_expand":
                return f"Développement trig: {sp.expand_trig(expr)}"
           
            else:
                return "Commande inconnue."
               
        except Exception as e:
            return f"Erreur de calcul: {str(e)}"
# --- EXEMPLE D'UTILISATION ---
if __name__ == "__main__":
    brain = MathSuperEngine()
   
    # Test Algèbre
    print(brain.execute("solve", "x^2 - 4 = 0"))
   
    # Test Trigo (simplification de sin^2 + cos^2)
    print(brain.execute("trig_simp", "sin(x)^2 + cos(x)^2"))
   
    # Test Dérivée
    print(brain.execute("diff", "sin(x) * x"))
    print("2x-3x")