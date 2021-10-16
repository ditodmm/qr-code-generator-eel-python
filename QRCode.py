from fpdf import FPDF
from base64 import b64encode
import io
import qrcode
import eel
import webbrowser as wb

eel.init('web', allowed_extensions=['.js', '.html'])


@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

@eel.expose
def generate_qr(data):
	qr=qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=4,
    border=4,
	)
	qr.add_data(data)
	qr.make(fit=True)
	img=qr.make_image(fill="black",back_color="white")
	img.save("qr.png")
	buffers = io.BytesIO()
	img.save(buffers)
	encoded = b64encode(buffers.getvalue()).decode("ascii")
	print("QR code generation successful.")
	return "data:image/png;base64, " + encoded

@eel.expose
def print_pdf():
	pdf = FPDF('P','mm','A4')
	pdf.add_page()
	pdf.set_font("Arial", size = 15)
	#. kolom pertama
	pdf.image('qr.png', 5,5,20,20)
	pdf.image('qr.png', 5,25,20,20)
	pdf.image('qr.png', 5,45,20,20)
	pdf.image('qr.png', 5,65,20,20)
	pdf.image('qr.png', 5,85,20,20)
	pdf.image('qr.png', 5,105,20,20)
	pdf.image('qr.png', 5,125,20,20)
	pdf.image('qr.png', 5,145,20,20)
	pdf.image('qr.png', 5,165,20,20)
	pdf.image('qr.png', 5,185,20,20)
	pdf.image('qr.png', 5,205,20,20)
	pdf.image('qr.png', 5,225,20,20)
	pdf.image('qr.png', 5,245,20,20)
	pdf.image('qr.png', 5,265,20,20)

	#. kolom kedua
	pdf.image('qr.png', 25,5,20,20)
	pdf.image('qr.png', 25,25,20,20)
	pdf.image('qr.png', 25,45,20,20)
	pdf.image('qr.png', 25,65,20,20)
	pdf.image('qr.png', 25,85,20,20)
	pdf.image('qr.png', 25,105,20,20)
	pdf.image('qr.png', 25,125,20,20)
	pdf.image('qr.png', 25,145,20,20)
	pdf.image('qr.png', 25,165,20,20)
	pdf.image('qr.png', 25,185,20,20)
	pdf.image('qr.png', 25,205,20,20)
	pdf.image('qr.png', 25,225,20,20)
	pdf.image('qr.png', 25,245,20,20)
	pdf.image('qr.png', 25,265,20,20)

	#. kolom ketiga
	pdf.image('qr.png', 45,5,20,20)
	pdf.image('qr.png', 45,25,20,20)
	pdf.image('qr.png', 45,45,20,20)
	pdf.image('qr.png', 45,65,20,20)
	pdf.image('qr.png', 45,85,20,20)
	pdf.image('qr.png', 45,105,20,20)
	pdf.image('qr.png', 45,125,20,20)
	pdf.image('qr.png', 45,145,20,20)
	pdf.image('qr.png', 45,165,20,20)
	pdf.image('qr.png', 45,185,20,20)
	pdf.image('qr.png', 45,205,20,20)
	pdf.image('qr.png', 45,225,20,20)
	pdf.image('qr.png', 45,245,20,20)
	pdf.image('qr.png', 45,265,20,20)

	#. kolom keempat
	pdf.image('qr.png', 65,5,20,20)
	pdf.image('qr.png', 65,25,20,20)
	pdf.image('qr.png', 65,45,20,20)
	pdf.image('qr.png', 65,65,20,20)
	pdf.image('qr.png', 65,85,20,20)
	pdf.image('qr.png', 65,105,20,20)
	pdf.image('qr.png', 65,125,20,20)
	pdf.image('qr.png', 65,145,20,20)
	pdf.image('qr.png', 65,165,20,20)
	pdf.image('qr.png', 65,185,20,20)
	pdf.image('qr.png', 65,205,20,20)
	pdf.image('qr.png', 65,225,20,20)
	pdf.image('qr.png', 65,245,20,20)
	pdf.image('qr.png', 65,265,20,20)

	#. kolom kelima
	pdf.image('qr.png', 85,5,20,20)
	pdf.image('qr.png', 85,25,20,20)
	pdf.image('qr.png', 85,45,20,20)
	pdf.image('qr.png', 85,65,20,20)
	pdf.image('qr.png', 85,85,20,20)
	pdf.image('qr.png', 85,105,20,20)
	pdf.image('qr.png', 85,125,20,20)
	pdf.image('qr.png', 85,145,20,20)
	pdf.image('qr.png', 85,165,20,20)
	pdf.image('qr.png', 85,185,20,20)
	pdf.image('qr.png', 85,205,20,20)
	pdf.image('qr.png', 85,225,20,20)
	pdf.image('qr.png', 85,245,20,20)
	pdf.image('qr.png', 85,265,20,20)

	#. kolom keenam
	pdf.image('qr.png', 105,5,20,20)
	pdf.image('qr.png', 105,25,20,20)
	pdf.image('qr.png', 105,45,20,20)
	pdf.image('qr.png', 105,65,20,20)
	pdf.image('qr.png', 105,85,20,20)
	pdf.image('qr.png', 105,105,20,20)
	pdf.image('qr.png', 105,125,20,20)
	pdf.image('qr.png', 105,145,20,20)
	pdf.image('qr.png', 105,165,20,20)
	pdf.image('qr.png', 105,185,20,20)
	pdf.image('qr.png', 105,205,20,20)
	pdf.image('qr.png', 105,225,20,20)
	pdf.image('qr.png', 105,245,20,20)
	pdf.image('qr.png', 105,265,20,20)

	#. kolom ketujuh
	pdf.image('qr.png', 125,5,20,20)
	pdf.image('qr.png', 125,25,20,20)
	pdf.image('qr.png', 125,45,20,20)
	pdf.image('qr.png', 125,65,20,20)
	pdf.image('qr.png', 125,85,20,20)
	pdf.image('qr.png', 125,105,20,20)
	pdf.image('qr.png', 125,125,20,20)
	pdf.image('qr.png', 125,145,20,20)
	pdf.image('qr.png', 125,165,20,20)
	pdf.image('qr.png', 125,185,20,20)
	pdf.image('qr.png', 125,205,20,20)
	pdf.image('qr.png', 125,225,20,20)
	pdf.image('qr.png', 125,245,20,20)
	pdf.image('qr.png', 125,265,20,20)

	#. kolom kedelapan
	pdf.image('qr.png', 145,5,20,20)
	pdf.image('qr.png', 145,25,20,20)
	pdf.image('qr.png', 145,45,20,20)
	pdf.image('qr.png', 145,65,20,20)
	pdf.image('qr.png', 145,85,20,20)
	pdf.image('qr.png', 145,105,20,20)
	pdf.image('qr.png', 145,125,20,20)
	pdf.image('qr.png', 145,145,20,20)
	pdf.image('qr.png', 145,165,20,20)
	pdf.image('qr.png', 145,185,20,20)
	pdf.image('qr.png', 145,205,20,20)
	pdf.image('qr.png', 145,225,20,20)
	pdf.image('qr.png', 145,245,20,20)
	pdf.image('qr.png', 145,265,20,20)

	#. kolom kesembilan
	pdf.image('qr.png', 165,5,20,20)
	pdf.image('qr.png', 165,25,20,20)
	pdf.image('qr.png', 165,45,20,20)
	pdf.image('qr.png', 165,65,20,20)
	pdf.image('qr.png', 165,85,20,20)
	pdf.image('qr.png', 165,105,20,20)
	pdf.image('qr.png', 165,125,20,20)
	pdf.image('qr.png', 165,145,20,20)
	pdf.image('qr.png', 165,165,20,20)
	pdf.image('qr.png', 165,185,20,20)
	pdf.image('qr.png', 165,205,20,20)
	pdf.image('qr.png', 165,225,20,20)
	pdf.image('qr.png', 165,245,20,20)
	pdf.image('qr.png', 165,265,20,20)

	#. kolom kesepuluh
	pdf.image('qr.png', 185,5,20,20)
	pdf.image('qr.png', 185,25,20,20)
	pdf.image('qr.png', 185,45,20,20)
	pdf.image('qr.png', 185,65,20,20)
	pdf.image('qr.png', 185,85,20,20)
	pdf.image('qr.png', 185,105,20,20)
	pdf.image('qr.png', 185,125,20,20)
	pdf.image('qr.png', 185,145,20,20)
	pdf.image('qr.png', 185,165,20,20)
	pdf.image('qr.png', 185,185,20,20)
	pdf.image('qr.png', 185,205,20,20)
	pdf.image('qr.png', 185,225,20,20)
	pdf.image('qr.png', 185,245,20,20)
	pdf.image('qr.png', 185,265,20,20)

	pdf.output('qr.pdf')
	wb.open_new(r'qr.pdf')

eel.start('index.html', size=(1000, 650))
