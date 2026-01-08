def bank_details(name,acc_no,acc_type):
    result = (
        f"Account Name:{name}\n"
        f"Account No:{acc_no}\n"
        f"Account Type:{acc_type}\n"
      
    )
    return result

if __name__ == "__main__":
    name ="swapna"
    acc_no ="1001"
    acc_type ="current"
   

    print(bank_details(name,acc_no,acc_type))
