errors:
        status = errors[0].get("extensions", {}).get("status")
        message = errors[0].get("message")
        print("Status:", status)
        print("Message:", message)
    else:
        print("No errors, like thành công.")