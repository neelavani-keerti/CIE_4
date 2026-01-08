from bank import bank_details

def test_bank_details():
    expected_output = (
        "Account Name:swapna\n"
        "Account No:1001\n"
        "Account Type:current\n"
     
    )
    assert bank_details("swapna",1001, "current") == expected_output