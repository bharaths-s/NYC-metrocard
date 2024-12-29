import qrcode
import random
import string
from datetime import datetime
import os

# Function to generate a random string
def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# Function to generate and save a QR code
def generate_qr_code(data, output_directory, index):
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each QR code box
        border=4,  # Border thickness
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = os.path.join(output_directory, f"qr_code_{index}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    img.save(filename)
    print(f"QR Code {index} saved as {filename}")

# Function to generate multiple QR codes
def generate_multiple_qr_codes(count, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)  # Create the output directory if it doesn't exist

    for i in range(1, count + 1):
        random_data = generate_random_string()
        generate_qr_code(random_data, output_directory, i)

# Main function
if __name__ == "__main__":
    # Number of QR codes to generate
    num_qr_codes = 5

    # Output directory for QR codes
    output_dir = "Generated_QR_Codes"

    generate_multiple_qr_codes(num_qr_codes, output_dir)
    print(f"\n{num_qr_codes} QR codes generated in the '{output_dir}' folder.")
    
@app.route('/')
def home():
    return render_template('sjc.html', title="Random QR Code Generator")
