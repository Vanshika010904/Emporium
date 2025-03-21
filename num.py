import os
def read_and_increment_number():
    # Read the current number from the file
    with open('current_number.txt', 'r') as f:
        current_number = int(f.read().strip())
    
    # Increment the number
    next_number = current_number + 1
    
    # Update the current number file
    with open('current_number.txt', 'w') as f:
        f.write(str(next_number))
    
    return current_number

# Initialize the current number file if it doesn't exist
if not os.path.exists('current_number.txt'):
    with open('current_number.txt', 'w') as f:
        f.write('1')

# Example usage
number = read_and_increment_number()
print(f"Using number:{number}")
