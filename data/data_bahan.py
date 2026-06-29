from models.bahan import Bahan


def data_awal_bahan():

    daftar_bahan = {}

    # TEPUNG

    daftar_bahan["tepung_protein_tinggi"] = Bahan(
        "BHN001",
        "Tepung Protein Tinggi",
        "gram",
        100000,
        0.02
    )

    daftar_bahan["tepung_protein_sedang"] = Bahan(
        "BHN002",
        "Tepung Protein Sedang",
        "gram",
        100000,
        0.018
    )

    # GULA

    daftar_bahan["gula"] = Bahan(
        "BHN003",
        "Gula Pasir",
        "gram",
        100000,
        0.01
    )

    # BUTTER

    daftar_bahan["butter"] = Bahan(
        "BHN004",
        "Butter",
        "gram",
        50000,
        0.08
    )

    # RAGI

    daftar_bahan["ragi"] = Bahan(
        "BHN005",
        "Ragi Instan",
        "gram",
        10000,
        0.10
    )

    # GARAM

    daftar_bahan["garam"] = Bahan(
        "BHN006",
        "Garam",
        "gram",
        10000,
        0.005
    )

    # SUSU

    daftar_bahan["susu"] = Bahan(
        "BHN007",
        "Susu Cair",
        "ml",
        50000,
        0.02
    )

    # TELUR

    daftar_bahan["telur"] = Bahan(
        "BHN008",
        "Telur",
        "butir",
        1000,
        2500
    )

    # VANILI

    daftar_bahan["vanili"] = Bahan(
        "BHN009",
        "Vanili Bubuk",
        "gram",
        5000,
        0.15
    )

    # BAKING POWDER

    daftar_bahan["baking_powder"] = Bahan(
        "BHN010",
        "Baking Powder",
        "gram",
        5000,
        0.12
    )

    return daftar_bahan