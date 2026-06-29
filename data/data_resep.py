from models.resep import Resep
from models.detail_resep import DetailResep


def data_awal_resep(bahan):

    resep = {}

    # ROTI MANIS COKLAT
    resep["RM001"] = Resep(
        "RM001",
        "Resep Roti Manis Coklat",
        [
            DetailResep(bahan["tepung_protein_tinggi"], 500),
            DetailResep(bahan["gula"], 80),
            DetailResep(bahan["ragi"], 8),
            DetailResep(bahan["susu_bubuk"], 25),
            DetailResep(bahan["telur"], 1),
            DetailResep(bahan["margarin"], 50),
            DetailResep(bahan["air"], 250),
            DetailResep(bahan["meses"], 150),
        ]
    )

    # CROISSANT

    resep["CR001"] = Resep(
        "CR001",
        "Resep Croissant",
        [
            DetailResep(bahan["tepung_protein_tinggi"], 500),
            DetailResep(bahan["garam"], 10),
            DetailResep(bahan["butter"], 250),
            DetailResep(bahan["gula"], 60),
            DetailResep(bahan["ragi"], 10),
            DetailResep(bahan["susu"], 300),
            DetailResep(bahan["telur"], 1),
        ]
    )

    # BUTTER COOKIE

    resep["BC001"] = Resep(
        "BC001",
        "Resep Butter Cookie",
        [
            DetailResep(bahan["tepung_protein_rendah"], 250),
            DetailResep(bahan["butter"], 200),
            DetailResep(bahan["gula"], 150),
            DetailResep(bahan["tepung_maizena"], 40),
            DetailResep(bahan["susu_bubuk"], 20),
            DetailResep(bahan["telur"], 2),
            DetailResep(bahan["vanili"], 5),
            DetailResep(bahan["chocochips"], 50)
        ]
    )

    # MUFFIN

    resep["MF001"] = Resep(
        "MF001",
        "Resep Muffin",
        [
            DetailResep(bahan["tepung_protein_sedang"], 200),
            DetailResep(bahan["gula"], 120),
            DetailResep(bahan["telur"], 2),
            DetailResep(bahan["susu"], 100),
            DetailResep(bahan["margarin"], 100),
            DetailResep(bahan["baking_powder"], 5),
            DetailResep(bahan["baking_soda"], 2.5),
            DetailResep(bahan["garam"], 1),
            DetailResep(bahan["chocochips"], 100),
            DetailResep(bahan["vanili"], 2),
            DetailResep(bahan["coklat_bubuk"], 25),
        ]
    )

    return resep