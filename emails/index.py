import smtplib
from email.mime.text import MIMEText
from datetime import date, timedelta

# Example client loan data
clients = [
    {"name": "Jan Kowalski", "email": "jan.kowalski@example.com", "due_date": date(2025, 9, 5)},
    {"name": "Anna Nowak", "email": "anna.nowak@example.com", "due_date": date(2025, 9, 10)},
]

def send_email(to_email, subject, message):
    sender = "noreply@credit-system.com"
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    # Example (local SMTP or test service like MailHog)
    with smtplib.SMTP("localhost", 1025) as server:
        server.sendmail(sender, [to_email], msg.as_string())
    print(f"Notification sent to {to_email}")

def notify_clients(clients, days_before=3):
    today = date.today()
    for client in clients:
        if client["due_date"] - today == timedelta(days=days_before):
            subject = "Przypomnienie o terminie spłaty pożyczki"
            message = (
                f"Dzień dobry {client['name']},\n\n"
                f"Przypominamy, że termin spłaty Twojej pożyczki przypada na {client['due_date']}."
            )
            send_email(client["email"], subject, message)

if __name__ == "__main__":
    notify_clients(clients)

