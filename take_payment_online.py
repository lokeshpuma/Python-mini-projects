import qrcode

upi_id = input("Enter UPI ID: ")

# defining the payment url

phonepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
googlepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
patym_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# generating QR codes for each payment app
phonepay_qr = qrcode.make(phonepay_url) 
googlepay_qr = qrcode.make(googlepay_url)
patym_qr = qrcode.make(patym_url)

# saving the QR codes to files

phonepay_qr.save("phonepay_qr.png")
googlepay_qr.save("googlepay_qr.png")
patym_qr.save("patym_qr.png")

#display the QR codes
phonepay_qr.show()
googlepay_qr.show()
patym_qr.show()


