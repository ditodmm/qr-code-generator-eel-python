function generateQRCode() {
	var nama = document.getElementById("nama").value
	var harga = document.getElementById("harga").value
	var tglproduksi = document.getElementById("tglproduksi").value
	var tglkadaluarsa = document.getElementById("tglkadaluarsa").value
	var data = ("Nama: " + nama + "\n" + "Harga: " + harga + "\n" + "Produksi: " + tglproduksi + "\n" + "Kadaluarsa: " + tglkadaluarsa)
	eel.generate_qr(data)(setImage)
}

function printPDF() {
	eel.print_pdf()
}

function setImage(base64) {
	document.getElementById("qr").src = base64
}