@echo off
:check_internet
ping -n 1 www.google.com > nul
if errorlevel 1 (
    echo Pas de connexion Internet. Vous devez vous connecter. Nouvelle tentative dans 5 secondes...
    timeout /t 5 > nul
    goto check_internet
) else (
    echo Connexion Internet. Execution du script...
    python "H:\Desktop\WhatsApp\Disquette\Disquette.py"
)
pause