from .models import Transaction
from django.db import transaction


def update_wallet(wallet, amount, transaction_type):
    """
        Updates the wallet balance and logs the transaction.

        Args:
            wallet (Wallet): The Wallet object to be updated.
            amount (Decimal): The amount for the transaction.
            transaction_type (str): Either 'deposit' or 'withdrawal'.

        Returns:
            Transaction: The created Transaction object.

        Raises:
            ValueError: If insufficient funds for a withdrawal.
    """
    with transaction.atomic():
        if transaction_type == "withdrawal":
            if wallet.balance < amount:
                raise ValueError("Insufficient funds")
            wallet.balance -= amount
        elif transaction_type == "deposit":
            wallet.balance += amount
        else:
            raise ValueError("Invalid transaction type")
        wallet.save()
        
        transaction_record = Transaction(wallet=wallet, transaction_type=transaction_type, amount=amount, status="completed")
        return transaction_record