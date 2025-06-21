import subprocess

def adivinha_password():
    with open('passwords.txt', 'r') as f:
        for linha in f:
            password = linha.strip()
            resultado = subprocess.run(["./login", password], capture_output=True, text=True)
            if resultado.stdout[0] != "F":
                print(f"{resultado.stdout.strip()}")
            else: 
                print("Password: " + password)
                break
        
adivinha_password()