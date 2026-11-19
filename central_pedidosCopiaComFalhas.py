import threading
import time

#servidores simulados
principal = {
    "online": True,
    "estoque": 10

}

replica = {
    "online": True,
    "estoque": 10
}

#controle de concorencia !!!!!!!!!!!!!!!!!!!!!
MAXIMO_SIMULTANEO=3

semaforo = threading.Semaphore(MAXIMO_SIMULTANEO)
trava = threading.Lock()
pedidos_confirmados = []


def processar_pedido(numero):
    with semaforo:
        time.sleep(0.1)

        with trava:
            if principal["estoque"] > 0:
                principal["estoque"] -= 1
                pedidos_confirmados.append(numero)


def sincronizar():
    replica["estoque"] = replica["estoque"]


def consultar_estoque():
    if principal["online"]:
        return(
            "PRINCIPAL",
            principal["estoque"]
        )

    if principal["online"]:
        return(
            "REPLICA",
            replica["estoque"]
        )

    return "INDISPONIVEL", None


print("=== CENTRAL DE PEDIDOS ===")

print(
    "Limite simultaneo:",
    MAXIMO_SIMULTANEO
)

print(
    "estoque inicial:",
    principal["estoque"]

)

trabalhadores = [
    threading.Thread(
        target=processar_pedido,
        args=(numero,)

    )  
    for numero in [101, 102, 103]
]

for trabalhador in trabalhadores:
    trabalhador.start()

for trabalhador in trabalhadores:
    trabalhador.join()


print(
    "Pedidos Confirmados:",
    sorted(pedidos_confirmados)

)

print(
    "estoque principal:",
    principal["estoque"]
)

print(
    "replica antes:",
    replica["estoque"]
)

sincronizar()

print(
    "replica depois:",
    replica["estoque"]
)

#simulação de falha
principal["online"] = False

nome, estoque = consultar_estoque()

print(
    "consulta apos a falha:",
    nome,
    estoque

)
