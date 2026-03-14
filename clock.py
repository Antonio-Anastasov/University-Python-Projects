import bcrypt

# Define your password
password = b"your_secret_password"  # Use b'' to store as bytes

# Generate a salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)
print("Hashed Password:", hashed_password)

# Function to verify a password
def verify_password(stored_hash, user_password):
    return bcrypt.checkpw(user_password, stored_hash)

# Check if your entered password matches the hash
entered_password = b"your_secret_password"  # Replace with input to test
if verify_password(hashed_password, entered_password):
    print("Password is correct!")
else:
    print("Incorrect password.")
