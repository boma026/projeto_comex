from etl.etl_pipeline import executar_etl
import schedule
import time

# Roda agora para testar
executar_etl()

# Agendar o ETL para rodar todo dia às 10h
schedule.every().day.at("10:00").do(executar_etl)

print("Agendador iniciado. Aguardando execução...")

# Loop contínuo para verificar se está na hora de rodar
while True:
    schedule.run_pending()
    time.sleep(60)