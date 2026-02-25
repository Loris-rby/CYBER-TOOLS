import argparse
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)



# BANNIÈRE 

M, W, R, Y, B, D = Fore.MAGENTA, Fore.WHITE, Fore.RED, Fore.YELLOW, Style.BRIGHT, Style.DIM

try:
    # AFFICHAGE BANNIÈRE ET CHARGEMENT 
    print(f"{M}{B}" + r"""
       _  _    _  _   _  _____  ____   _____     _______  ____   ____  _        _____ 
      | || |  | || \ | ||_   _|/ __ \ |  __ \   |__   __|/ __ \ / __ \| |      / ____|
      | || |  | ||  \| |  | | | |  | || |__) |     | |  | |  | | |  | | |     | (___  
  _   | || |  | || . ' |  | | | |  | ||  _  /      | |  | |  | | |  | | |      \___ \ 
 | |__| || |__| || |\  |_ _| |_| |__| || | \ \     | |  | |__| | |__| | |____  ____) |
  \____/  \____/ |_| \_| |_____|\____/ |_|  \_\    |_|   \____/ \____/|______||_____/ 
    """)
    
    for mod in ["Core", "Network", "Recon"]:
        print(f"{M}[*]{W} Chargement du module {mod}...", end="\r")
        time.sleep(0.2)
        print(f"{M}[+]{W} Module {mod} chargé !         ")
        
    print(f"\n{D}─────────────────────────────────────────────────────────────────────────────────────────\n")

    # CONFIGURATION DES ARGUMENTS
    p = argparse.ArgumentParser(
        description=f"\n{M}{B}Junior Tools{W} - Outils de reconnaisance simple\n",
        usage=f"\n  {M}python3 %(prog)s -t <cible> [options]\n",
        formatter_class=argparse.RawTextHelpFormatter, add_help=False 
    )

    # Ajout des args 
    
    # General 
    hg = p.add_argument_group(f'\n{B}{W}OPTIONS GÉNÉRALES')
    hg.add_argument("-h", "--help", action="help", help="  Affiche ce menu d'aide et quitte le programme\n\n")
    
    # Target 
    tg = p.add_argument_group(f'\n{B}{W}PARAMÈTRES CIBLE')
    tg.add_argument("-t", "--target", required=True, metavar="IP/DOMAINE", help="  Définir la cible à scanner (ex: 192.168.1.1 ou site.com)\n\n")
    
    # Params
    mg = p.add_argument_group(f'\n{B}{W}PARAMÈTRES OPTIONS')
    mg.add_argument("-p", "--ports", action="store_true", help="  Activer le scan de ports (TCP SYN)\n\n")
    mg.add_argument("-s", "--sub", action="store_true", help="  Activer l'énumération de sous-domaines \n\n")
    

    # Charger les args
    args = p.parse_args()

    # RÉSUMÉ DE LA MISSION 
    mods = [name for name, active in [("PORT_SCANNER", args.ports), ("SUB_ENUMERATOR", args.sub)] if active]
    
    print(f"\n{B}{M}[ MISSION CONFIRMÉE ]\n")
    print(f"{M} ¤ Cible    : {W}{B}{args.target}\n")
    print(f"{M} ¤ Modules  : {W}{B}{', '.join(mods) if mods else R + 'Aucun'}\n")
    print(f"{D}─────────────────────────────────────────────────────────────────────────────────────────\n")
    
    if not mods:
        sys.exit(f"{Y}[!] Aucun module sélectionné. Ajoutez -p ou -s pour lancer un scan.\n")
        
    print(f"{B}{M}[*]{W} Début des opérations de reconnaissance sur {args.target}...\n")

except KeyboardInterrupt:
    sys.exit(f"\n\n\n{R}{B}[!] Interruption par l'utilisateur. Sortie sécurisée.\n")

#test


