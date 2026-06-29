from models.bahan import Bahan


def data_awal_bahan():

    daftar_bahan = {}
    
    # AIR
    
    daftar_bahan["air"] = Bahan(
        "BHN023",
        "Air",
        "ml",
        100000,
        0.2
    )

    # TEPUNG

    daftar_bahan["tepung_protein_tinggi"] = Bahan(
        "BHN001",
        "Tepung Protein Tinggi",
        "gram",
        100000,
        18
    )

    daftar_bahan["tepung_protein_sedang"] = Bahan(
        "BHN002",
        "Tepung Protein Sedang",
        "gram",
        100000,
        15
    )
    
    # Tepung Protein Rendah
    daftar_bahan["tepung_protein_rendah"] = Bahan(
        "BHN024",
        "Tepung Protein Rendah",
        "gram",
        100000,
        16
    )
    
    # Tepung Maizena
    daftar_bahan["tepung_maizena"] = Bahan(
        "BHN026",
        "Tepung Maizena",
        "gram",
        10000,
        50
    )

    # GULA

    daftar_bahan["gula"] = Bahan(
        "BHN003",
        "Gula Pasir",
        "gram",
        100000,
        18
    )

    # BUTTER & MARGARIN

    daftar_bahan["butter"] = Bahan(
        "BHN004",
        "Butter",
        "gram",
        50000,
        160
    )
    
    daftar_bahan["margarin"] = Bahan(
        "BHN022",
        "Margarin",
        "gram",
        10000,
        55
    )


    # RAGI

    daftar_bahan["ragi"] = Bahan(
        "BHN005",
        "Ragi Instan",
        "gram",
        10000,
        130
    )

    # GARAM

    daftar_bahan["garam"] = Bahan(
        "BHN006",
        "Garam",
        "gram",
        10000,
        10
    )

    # SUSU

    daftar_bahan["susu"] = Bahan(
        "BHN007",
        "Susu Cair",
        "ml",
        50000,
        22
    )
    
    daftar_bahan["susu_bubuk"] = Bahan(
        "BHN027",
        "Susu Bubuk",
        "gram",
        10000,
        200
    )

    # TELUR

    daftar_bahan["telur"] = Bahan(
        "BHN008",
        "Telur Ayam",
        "butir",
        1000,
        3000
    )

    # VANILI

    daftar_bahan["vanili"] = Bahan(
        "BHN009",
        "Vanili Bubuk",
        "gram",
        5000,
        300
    )

    # BAKING POWDER

    daftar_bahan["baking_powder"] = Bahan(
        "BHN010",
        "Baking Powder",
        "gram",
        5000,
        250
    )
    
    # BAKING SODA
    daftar_bahan["baking_soda"] = Bahan(
        "BHN021",
        "Baking Soda",
        "gram",
        3000,
        180
    )

    # BAHAN TAMBAHAN
    
    daftar_bahan["chocochips"] = Bahan(
        "BHN025",
        "Chocochips",
        "gram",
        10000,
        90
    )

    daftar_bahan["coklat_bubuk"] = Bahan(
        "BHN011",
        "Coklat Bubuk",
        "gram",
        10000,
        180
    )

    daftar_bahan["keju"] = Bahan(
        "BHN012",
        "Keju Cheddar",
        "gram",
        10000,
        140
    )

    daftar_bahan["meses"] = Bahan(
        "BHN013",
        "Meses Coklat",
        "gram",
        10000,
        90
    )

    daftar_bahan["selai_stroberi"] = Bahan(
        "BHN014",
        "Selai Stroberi",
        "gram",
        10000,
        75
    )

    daftar_bahan["selai_blueberry"] = Bahan(
        "BHN015",
        "Selai Blueberry",
        "gram",
        10000,
        85
    )

    daftar_bahan["coklat_batang"] = Bahan(
        "BHN016",
        "Dark Chocolate",
        "gram",
        10000,
        170
    )

    daftar_bahan["cream_cheese"] = Bahan(
        "BHN017",
        "Cream Cheese",
        "gram",
        5000,
        180
    )

    daftar_bahan["kismis"] = Bahan(
        "BHN018",
        "Kismis",
        "gram",
        5000,
        120
    )

    daftar_bahan["almond"] = Bahan(
        "BHN019",
        "Almond Slice",
        "gram",
        5000,
        250
    )

    daftar_bahan["madu"] = Bahan(
        "BHN020",
        "Madu",
        "ml",
        5000,
        120
    )

    return daftar_bahan