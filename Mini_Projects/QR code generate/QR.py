import qrcode

# provide a link to generate a qr code
data = "https://github.com/paratemihir"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10, 
    border=4,  
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
