import qrcode
qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=1

	)
name = input("Your Name: ")
about = input("About You: ")
email = input("Email ID: ")
contact_no = input("Contact No: ")
website = input("Website Link: ")

data = "name"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("YourQR")