import json
import csv

ARQUIVO_JSON = "sensores.json"
ARQUIVO_CSV = "leituras.csv"

with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
    dados = json.load(f)

with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "sensor_id",
        "sensor_nome",
        "tipo",
        "modo",
        "timestamp",
        "valor",
        "status",
        "origem"
    ])

    for sensor in dados["sensores"]:

        for leitura in sensor.get("historico", []):

            writer.writerow([
                sensor["id"],
                sensor["nome"],
                sensor["tipo"],
                sensor["modo"],
                leitura["ts"],
                leitura["valor"],
                leitura["status"],
                leitura["origem"]
            ])

print(f"CSV gerado: {ARQUIVO_CSV}")