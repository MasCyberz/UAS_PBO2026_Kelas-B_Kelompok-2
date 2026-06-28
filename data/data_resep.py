from models.resep import Resep
from models.detail_resep import DetailResep


def data_awal_resep(bahan):

    resep = {}

    # ROTI MANIS

    resep["RM001"] = Resep(
        "RM001",
        "Resep Roti Manis",
        [
            DetailResep(bahan["tepung_protein_tinggi"], 500),
            DetailResep(bahan["gula"], 100),
            DetailResep(bahan["butter"], 80),
            DetailResep(bahan["ragi"], 10),
            DetailResep(bahan["garam"], 5),
            DetailResep(bahan["susu"], 200),
            DetailResep(bahan["telur"], 2),
        ]
    )

    # CROISSANT

    resep["CR001"] = Resep(
        "CR001",
        "Resep Croissant",
        [
            DetailResep(bahan["tepung_protein_tinggi"], 500),
            DetailResep(bahan["butter"], 250),
            DetailResep(bahan["gula"], 50),
            DetailResep(bahan["ragi"], 10),
            DetailResep(bahan["garam"], 5),
            DetailResep(bahan["susu"], 100),
            DetailResep(bahan["telur"], 2),
        ]
    )

    # BUTTER COOKIE

    resep["BC001"] = Resep(
        "BC001",
        "Resep Butter Cookie",
        [
            DetailResep(bahan["tepung_protein_sedang"], 500),
            DetailResep(bahan["butter"], 250),
            DetailResep(bahan["gula"], 150),
            DetailResep(bahan["telur"], 2),
            DetailResep(bahan["vanili"], 5),
        ]
    )

    # MUFFIN

    resep["MF001"] = Resep(
        "MF001",
        "Resep Muffin",
        [
            DetailResep(bahan["tepung_protein_sedang"], 400),
            DetailResep(bahan["butter"], 100),
            DetailResep(bahan["gula"], 120),
            DetailResep(bahan["susu"], 150),
            DetailResep(bahan["telur"], 2),
            DetailResep(bahan["baking_powder"], 8),
            DetailResep(bahan["vanili"], 5),
        ]
    )

    return resep