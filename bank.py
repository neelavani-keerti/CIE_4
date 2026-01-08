def bank_details(name, acc_no, acc_type):
    return (
        f"Account Name: {name}\n"
        f"Account No: {acc_no}\n"
        f"Account Type: {acc_type}"
    )

if __name__ == "__main__":
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")
    acc_type = input("Enter account type: ")

    print(bank_details(name, acc_no, acc_type))
