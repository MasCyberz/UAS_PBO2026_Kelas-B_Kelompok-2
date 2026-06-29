from services.bahan_service import BahanServices
from services.resep_service import ResepService
from services.produk_service import ProdukService
from services.proses_produksi_service import ProductionService
from services.profit_service import ProfitService


class BakeryService:

    def __init__(self):

        # MASTER DATA

        self.bahan_service = BahanServices()

        self.resep_service = ResepService(
            self.bahan_service
        )

        self.produk_service = ProdukService(
            self.resep_service
        )

        # TRANSAKSI

        self.production_service = ProductionService(
            self.produk_service,
            self.resep_service,
            self.bahan_service
        )

        self.profit_service = ProfitService(
            self.produk_service,
            self.resep_service,
            self.production_service
        )