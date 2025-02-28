import serial
# Open serial port
ser = serial.Serial("COM10", 115200, timeout=1)

try:
    while True:
        # Get user input (without manually adding \n)
        user_input = input("Enter command (starting with $): ").strip()

        # Ensure the command starts with '$'
        if not user_input.startswith('$'):
            print("Invalid command! Command must start with '$'.")
            continue

        # Append '\n' automatically
        command = user_input + '\n'

        # Send command over serial
        ser.write(command.encode())  
        print(f"Sent: {command.strip()}") 

        # Read response
        response = ser.readline().decode().strip()
        print(f"Received: {response}")

except KeyboardInterrupt:
    print("\nExiting program...")

finally:
    ser.close()  # Close the serial port
