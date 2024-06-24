import qrcode
from PIL import Image

def generate_qr_code(input_data, output_file):
   
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    

    qr.add_data(input_data)
    qr.make(fit=True)
    
  
    img = qr.make_image(fill='black', back_color='white')
    
    img.save(output_file)

if __name__ == "__main__":
    
    data = input("Enter text or URL to generate QR code: ")
    FILENAME= input("Enter the filename to save the QR code image" )
    
    generate_qr_code(data, FILENAME)
    
    print(f"QR code saved as {FILENAME}")
  

