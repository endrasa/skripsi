class Transaksi:
    def __init__(self, tanggal, nama_barang, jumlah, modal_satuan, harga_jual_satuan):
        self.tanggal = tanggal
        self.nama_barang = nama_barang
        self.jumlah = int(jumlah)
        self.modal_satuan = float(modal_satuan)
        self.harga_jual_satuan = float(harga_jual_satuan)

    @property
    def total_modal(self):
        return self.jumlah * self.modal_satuan

    @property
    def total_jual(self):
        return self.jumlah * self.harga_jual_satuan

    @property
    def untung_rugi(self):
        return self.total_jual - self.total_modal