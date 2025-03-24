import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

PAYMENT_API_URL = "https://api.paymentprovider.com/charge"
API_KEY = "your_api_key"

def process_payment(user_id: int, amount: float, card_token: str):
    """Отправка запроса на платеж и обработка ответа"""
    payload = {
        "user_id": user_id,
        "amount": amount,
        "currency": "USD",
        "card_token": card_token
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.post(PAYMENT_API_URL, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200 and response_data.get("status") == "success":
            logging.info(f"Платеж {response_data.get('transaction_id')} успешно выполнен.")
            return response_data
        else:
            logging.error(f"Ошибка при проведении платежа: {response_data}")
            return None

    except requests.RequestException as e:
        logging.error(f"Ошибка сети при обработке платежа: {e}")
        return None

# Пример использования
if __name__ == "__main__":
    result = process_payment(user_id=123, amount=100.50, card_token="sample_card_token")
    if result:
        print("Платеж прошел успешно:", result)
    else:
        print("Платеж не выполнен.")
