import pytest
from .Account import Account, NegativeBalanceNotAllowed, IllegalWithdrawal, IllegalTransfer

@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    # We need to reset the Account class variables between tests.
    Account.reset()

def test_first_account_gets_number_1():
    account = Account()
    assert account.number == 1

@pytest.fixture
def two_accounts():
    Account()
    Account()

def test_number_of_accounts_increases_on_creation(two_accounts):
    assert Account.numberOfAccounts == 2

# Write your tests below here.

## step 2
def test_account_amount_with_constructor():
    account = Account(93762387.0)
    assert account.amount == 93762387.0

def test_valid_nonfloat_inital_amount():
    account = Account("93762387.0")
    assert account.amount == 93762387.0
    
def test_invalid_nonfloat_inital_amount():
    with pytest.raises(ValueError):
        Account("937a23h7.0")
    
## step 3
def test_regular_withdraw():
    account = Account(100.0)
    account.withdraw(99.0)
    assert account.amount == 100.0 - 99.0

def test_valid_nonfloat_withdraw():
    account = Account("100.0")
    account.withdraw("99.0")
    assert account.amount == 100.0 - 99.0

def test_invalid_nonfloat_withdraw():
    account = Account("100.0")
    with pytest.raises(ValueError):
        account.withdraw("9asdf9.0")

## step 4
def test_regular_deposit():
    account = Account(100.0)
    account.deposit(99.0)
    assert account.amount == 100.0 + 99.0

def test_valid_nonfloat_deposit():
    account = Account("100.0")
    account.deposit("99.0")
    assert account.amount == 100.0 + 99.0

def test_invalid_nonfloat_deposit():
    account = Account("100.0")
    with pytest.raises(ValueError):
        account.deposit("9asdf9.0")

## step 5
def test_transfer_keeps_total():
    donor = Account(100)
    recipient = Account(0)
    donor.transfer(recipient, 100.0)
    assert donor.amount + recipient.amount == 100.0

def test_tranfer_reduces_donor():
    donor = Account(100)
    recipient = Account(0)
    donor.transfer(recipient, 100.0)
    assert donor.amount == 0.0

def test_tranfer_increases_recipient():
    donor = Account(100)
    recipient = Account(0)
    donor.transfer(recipient, 100.0)
    assert recipient.amount == 100.0

def test_valid_nonfloat_amount():
    donor = Account(100)
    recipient = Account(0)
    donor.transfer(recipient, "100.0")
    assert donor.amount + recipient.amount == 100.0

def test_invalid_nonfloat_amount():
    with pytest.raises(ValueError):
        donor = Account(100)
        recipient = Account(0)
        donor.transfer(recipient, "1sadfh0fjgh0dsfgjh.0")

## step 6

def test_small_account_nr_str():
    account = Account()
    assert str(account) == "000001"
    
def test_medium_account_nr_str():
    account = Account()
    account.number = 50401
    assert str(account) == "050401"

def test_large_account_nr_str():
    account = Account()
    account.number = 40163423
    assert str(account) == "40163423"

### neikvæð account number er undefined behavior, ef það gerist yfir höfuð, man ekki hvort python overflowar eða crashar bara

## step 7
def test_negative_initial_amounts():
    with pytest.raises(NegativeBalanceNotAllowed):
        Account(-7)

def test_zero_initial_amounts():
    account = Account(0)
    assert account.amount == 0.0
    
## step 8

def test_overdraft():
    account = Account(100)
    with pytest.raises(IllegalWithdrawal):
        account.withdraw(101)

def test_withdraw_entire_account():
    account = Account(100)
    account.withdraw(100)
    assert account.amount == 0.0

## step 9
def test_overtransfer():
    donor = Account(100)
    recipient = Account(100)
    with pytest.raises(IllegalTransfer):
        donor.transfer(recipient,101)

## step 10
def test_total_balance():
    accounts = [Account(1),Account(2),Account(4),Account(8),Account(16)]
    assert Account.total_balance() == 31.0

def test_invalid_account_creation_affecting_total():
    accounts = [Account(1),Account(2),Account(4),Account(8),Account(16)]
    try:
        a = Account("invalid entry")
    except:
        pass
    assert  Account.total_balance() == 31.0