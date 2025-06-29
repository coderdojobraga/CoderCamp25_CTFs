# Autenticação (Client Side)

Os ninjas devem encontrar as credenciais de acesso para se autenticarem e encontrarem a flag.
A autenticação é feita pelo cliente (no frontend).

**Link do website**: https://www.marcoslobo.xyz/login

**Link dos CTF's (Web)**: https://bernardolobo06.github.io/webCoderCamp25/

**Solução**: As credenciais estão escritas no script de javascript que está no código fonte.

**Flag**: CD25{webserver-login}

**Localização**: index.html linha 61
```
if (utilizador == 'ninja' && password === 'coderdojo25')
```