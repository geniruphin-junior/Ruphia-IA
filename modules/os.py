import os
import subprocess
import shutil
import psutil
import threading
from datetime import datetime
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.completion import WordCompleter
from pygments.lexers.shell import BashLexer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Import de vos modules personnalisés (assurez-vous que les fichiers sont dans le même dossier)
try:
    from voice import parler
except ImportError:

    def parler(t):
        print(f"(Voix non chargée) : {t}")


console = Console()

# --- ALIAS & AUTO-COMPLÉTION ---
#  "cd.." pour qu'il soit reconnu même collé
ALIAS = {
    "ruphia": "python app.py",
    "ruphy": "npm start",
    "ls": "ls --color=auto",
    "ll": "ls -la",
    "cd..": "cd ..",
}

commands_list = list(ALIAS.keys()) + [
    "exit",
    "clear",
    "cd",
    "git",
    "python",
    "npm",
    "node",
]
ruphin_completer = WordCompleter(commands_list, ignore_case=True)

# --- CONFIGURATION STYLE BLEU DE NUIT ---
midnight_style = Style.from_dict(
    {
        "username": "#00d4ff bold",
        "at": "#444444",
        "node": "#0055ff bold",
        "path": "#5bc0de italic",
        "prompt": "#00ffff bold",
        "completion-menu.completion": "bg:#000814 #00d4ff",
        "completion-menu.completion.current": "bg:#001d3d #ffffff",
    }
)


def get_stats_bar():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    time_now = datetime.now().strftime("%H:%M:%S")
    return f"[bold #0055ff] RUPHIN-OS[/] [white]|[/] [bold #00d4ff]   {time_now}[/] [white]|[/] [bold #00ff00]CPU:[/] {cpu}% [bold #5bc0de]RAM:[/] {ram}%"


def show_header():
    os.system("cls" if os.name == "nt" else "clear")
    banner = Text(
        r"""
    █▀█ █░█ █▀█ █░█ █ █▄░█   █▀█ █▀
    █▀▄ █▄█ █▀▀ █▀█ █ █░▀█   █▄█ ▄█ """,
        style="bold #0055ff",
    )
    console.print(
        Panel(
            banner,
            subtitle="[#00d4ff]MIDNIGHT ENGINEERING EDITION[/#00d4ff]",
            border_style="#003366",
        )
    )
    console.print(get_stats_bar(), justify="center")
    print("\033[38;5;18m" + "━" * shutil.get_terminal_size().columns + "\033[0m")


def main():
    show_header()
    session = PromptSession(completer=ruphin_completer)

    while True:
        try:
            cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
            user = os.getlogin()

            # PROMPT
            message = [
                ("class:username", user),
                ("class:at", " @ "),
                ("class:node", "engineer"),
                ("class:at", " in "),
                ("class:path", f"{cwd}\n"),
                ("class:prompt", "   ➜ "),
            ]

            cmd_input = session.prompt(
                message, style=midnight_style, lexer=PygmentsLexer(BashLexer)
            ).strip()

            if not cmd_input:
                continue

            # --- GESTION DES ALIAS ---
            parts = cmd_input.split()
            if parts[0] in ALIAS:
                cmd_input = ALIAS[parts[0]] + (
                    " " + " ".join(parts[1:]) if len(parts) > 1 else ""
                )

            # --- COMMANDES SYSTÈME ---
            if cmd_input.lower() in ["exit", "quit"]:
                break

            if cmd_input.lower() == "clear":
                show_header()
                continue

            # --- CORRECTION DU CD (gère cd.., cd.. / et cd chemin) ---
            if cmd_input.startswith("cd") and (
                len(cmd_input) == 2 or cmd_input[2] in [" ", ".", "/"]
            ):
                # On extrait le chemin : tout ce qui est après "cd"
                path = cmd_input[2:].strip()
                try:
                    os.chdir(os.path.expanduser(path or "~"))
                except Exception as e:
                    console.print(f"[bold red]✘ {e}[/bold red]")
                continue

            # --- EXECUTION DES COMMANDES ---
            # Si vous voulez que l'IA commente l'exécution, vous pouvez ajouter parler() ici
            result = subprocess.run(cmd_input, shell=True)

            # Exemple : Si la commande échoue, l'IA le dit (en thread pour ne pas bloquer)
            if result.returncode != 0:
                threading.Thread(
                    target=parler, args=("La commande a échoué",), daemon=True
                ).start()

        except KeyboardInterrupt:
            continue
        except EOFError:
            break

    console.print(
        "\n[bold #0055ff]➜ DISCONNECTING FROM MIDNIGHT SERVER...[/bold #0055ff]"
    )


if __name__ == "__main__":
    main()
