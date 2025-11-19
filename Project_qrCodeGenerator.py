import qrcode
url=input("Enter the URL to generate QR Code: ").strip()
file_path=input("Enter the file path to save the QR Code image (e.g., C:/path/to/qr_code.png): ").strip()
qr=qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
img.save(file_path)
print(f"QR Code generated and saved to {file_path}")