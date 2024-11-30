import qrcode
from PIL import Image, ImageDraw

# Define the first and last name
first_name = "Ahmad"
last_name = "ALHakim"

# Create a new contact card text for the QR code
contact_card_text = f"https://bio.link/nusuk_almashaeir"

# Generate a new QR code with the contact card text
qr_contact = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr_contact.add_data(contact_card_text)
qr_contact.make(fit=True)

# Create the QR code image with red color
qr_contact_img = qr_contact.make_image(fill_color=(7, 100, 143), back_color=(0, 0, 0))

# Load the logo
logo_path = "D:/abd/abd/abd.png"
logo = Image.open(logo_path)

# Resize the logo to fit within the QR code
logo_size = int(qr_contact_img.size[0] / 4)  # Size of the logo to be one-fourth of the QR code
logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

# Ensure the logo has an alpha channel
if logo.mode != 'RGBA':
    logo = logo.convert('RGBA')

# Create a square mask for the logo (just a filled rectangle here)
mask = Image.new('L', (logo.size[0], logo.size[1]), 255)  # Create a new mask image with a white square

# Overlay the logo in the center
qr_contact_img = qr_contact_img.convert("RGBA")
qr_contact_img_with_logo = qr_contact_img.copy()

# Calculate position for the logo to be centered
logo_position = (
    (qr_contact_img.size[0] - logo.size[0]) // 2,
    (qr_contact_img.size[1] - logo.size[1]) // 2,
)

# Paste the logo onto the QR code image using the square mask
qr_contact_img_with_logo.paste(logo, logo_position, mask)

# Save the QR code with the contact card and logo
output_contact_qr_with_logo_path = "D:/abd/abd/qr/Nusuk_social.png"
qr_contact_img_with_logo.save(output_contact_qr_with_logo_path)

print(f"QR code generated and saved as '{output_contact_qr_with_logo_path}'")
