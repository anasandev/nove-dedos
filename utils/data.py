from datetime import datetime

def formatar_data(data):

    try:
        return datetime.strptime(
            data,
            "%d/%m/%Y"
        ).strftime("%Y-%m-%d")

    except ValueError:
        return None