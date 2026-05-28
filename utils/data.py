from datetime import datetime

def formatar_data(data):
    # Tenta converter a data do formato "dd/mm/yyyy" para "yyyy-mm-dd", se a conversão falhar, retorna None
    try:
        return datetime.strptime(
            data,
            "%d/%m/%Y"
        ).strftime("%Y-%m-%d")

    except ValueError:
        return None