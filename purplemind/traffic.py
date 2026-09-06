import random
from datetime import datetime

import pyshark
from scapy.all import IP, TCP

from config import PORTE_NORMALI, PORTE_ATTACCO


# Genera eventi di traffico simulato
def genera_traffico(eventi_normali, eventi_attacco):
    eventi = []

    # Traffico normale
    for numero_evento in range(eventi_normali):
        pacchetto = IP(
            src="192.168.1.10",
            dst="192.168.1.20"
        ) / TCP(
            dport=random.choice(PORTE_NORMALI)
        )

        eventi.append({
            "timestamp": datetime.now(),
            "src_ip": pacchetto.src,
            "dst_port": pacchetto.dport,
            "bytes_sent": random.randint(200, 4000),
            "duration": round(random.uniform(0.5, 5.0), 2),
            "failed_logins": random.randint(0, 6),
            "request_rate": random.randint(1, 40),
            "label": "benign"
        })

    # Traffico di attacco
    for numero_evento in range(eventi_attacco):
        pacchetto = IP(
            src="10.0.0.50",
            dst="192.168.1.20"
        ) / TCP(
            dport=random.choice(PORTE_ATTACCO)
        )

        eventi.append({
            "timestamp": datetime.now(),
            "src_ip": pacchetto.src,
            "dst_port": pacchetto.dport,
            "bytes_sent": random.randint(1000, 12000),
            "duration": round(random.uniform(0.1, 2.0), 2),
            "failed_logins": random.randint(2, 25),
            "request_rate": random.randint(10, 120),
            "label": "malicious"
        })

    random.shuffle(eventi)

    return eventi


# Cattura pacchetti reali tramite PyShark
def cattura_traffico(interfaccia, numero_pacchetti=100):
    cattura = pyshark.LiveCapture(
        interface=interfaccia
    )

    eventi = []

    for pacchetto in cattura.sniff_continuously(
        packet_count=numero_pacchetti
    ):
        if hasattr(pacchetto, "ip"):
            eventi.append({
                "timestamp": datetime.now(),
                "src_ip": pacchetto.ip.src,
                "dst_port": estrai_porta(pacchetto),
                "bytes_sent": int(
                    getattr(pacchetto, "length", 0)
                ),
                "duration": 0,
                "failed_logins": 0,
                "request_rate": 1,
                "label": "unknown"
            })

    cattura.close()

    return eventi


# Recupera la porta di destinazione
def estrai_porta(pacchetto):
    if hasattr(pacchetto, "tcp"):
        return int(pacchetto.tcp.dstport)

    if hasattr(pacchetto, "udp"):
        return int(pacchetto.udp.dstport)

    return 0
