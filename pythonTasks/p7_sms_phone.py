import os


def is_device_connected():
    # Check if any device is connected via ADB
    result = os.popen('adb devices').read()
    return "device" in result


def send_sms(phone_number, message):
    if not is_device_connected():
        print("Error: No ADB device connected. Please connect your device and try again.")
        return
    
    # these commands are specific to your phone specifications, it may vary for your use case
    send_command = f'adb shell am start -a android.intent.action.SENDTO -d sms:{phone_number}'
    message_command = f'adb shell input text "{message}"'
    send_enter_command = 'adb shell input tap 980 1400'  # Coordinates for the send button (may vary)
    
    os.system(send_command)
    os.system(message_command)
    os.system(send_enter_command)


def sms_phone_data():
    phone_number = input("Enter your phone number: ")
    message = input("Enter your message: ").replace(" ", "%s")
    send_sms(phone_number, message)


# Example usage
if __name__ == "__main__":
    # send_sms("9660607213","this is a test message using phone")
    sms_phone_data()
