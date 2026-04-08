from .models import Ticket, Resource


def easy_task():
    return {
        "tickets": [
            Ticket(
                id="T1",
                issue="Delayed order",
                priority="low",
                customer_tone="neutral",
                time_waiting=1,
            )
        ],
        "resources": Resource(agents_available=2),
    }


def medium_task():
    return {
        "tickets": [
            Ticket(id="T1", issue="Refund request", priority="high", customer_tone="angry", time_waiting=3),
            Ticket(id="T2", issue="Order status", priority="low", customer_tone="calm", time_waiting=1),
        ],
        "resources": Resource(agents_available=1),
    }


def hard_task():
    return {
        "tickets": [
            Ticket(id="T1", issue="Payment failed", priority="high", customer_tone="angry", time_waiting=4),
            Ticket(id="T2", issue="Delayed order", priority="medium", customer_tone="neutral", time_waiting=2),
            Ticket(id="T3", issue="Wrong item delivered", priority="high", customer_tone="angry", time_waiting=3),
        ],
        "resources": Resource(agents_available=1),
    }