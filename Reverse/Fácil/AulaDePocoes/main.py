import codec

ingredientes = {
    "veneno_de_basilisco": 5,
    "raiz_magica": 3,
    "olho_de_sapo": 8,
    "ovo_de_dragao": 1
}

if (ingredientes.get("sapos_saltitantes") == 3 and ingredientes.get("cerebros_de_ra") == 1 and ingredientes.get("ovos_de_farosutil") == 2 and ingredientes.get("garra_de_dragao_em_po") == 5):
    print("Fizeste um Elixir Baruffio para o cérebro.\nEsta poção aumenta a capacidade cognitiva de quem a consome.\nCom ela descobriste a flag:")
    codec.desencriptar("56$'mX[lWefW}g_S}baUSa}_SY[USo")
else:
    print("Falta algum ingrediente...")