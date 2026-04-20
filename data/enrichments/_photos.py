"""
Plantenpedia — Foto's per plant (gegenereerd via fetch_photos.py)
Foto's zijn bevestigde Wikimedia Commons bestanden uit Wikipedia-artikelen.

Upload: python data/upload.py --fields photos
"""
from ._helpers import wiki

PHOTOS: dict = {

"Abies koreana": {"photos": [
    wiki("Abies koreana leaves.jpg", "koreana — blad", type_="blad"),
    wiki("ABIES KOREANA KOREAN FIRweb.jpg", "koreana — algemeen", type_="algemeen"),
    wiki("Abies koreana01.jpg", "koreana — algemeen", type_="algemeen"),
]},

"Acaena buchananii": {"photos": [
    wiki("Acaena novae-zelandiae1.jpg", "buchananii — algemeen", type_="algemeen"),
]},

"Acanthus mollis": {"photos": [
    wiki("Acanthaceae - Acanthus mollis-2.JPG", "mollis — habitus", type_="habitus"),
    wiki("Acanthus mollis flower.JPG", "mollis — bloeiwijze", type_="bloeiwijze"),
    wiki("Acanthus mollis flower parts text.jpg", "mollis — bloeiwijze", type_="bloeiwijze"),
]},

"Acer campestre": {"photos": [
    wiki("Acer-campestre-flowers.JPG", "campestre — bloeiwijze", type_="bloeiwijze"),
    wiki("237 Acer campestre.jpg", "campestre — algemeen", type_="algemeen"),
    wiki("Acer-campestre.JPG", "campestre — algemeen", type_="algemeen"),
]},

"Acer platanoides": {"photos": [
    wiki("2020 year. Herbarium. Acer platanoides. img-001.jpg", "platanoides — habitus", type_="habitus"),
    wiki("2020 year. Herbarium. Acer platanoides. img-002.jpg", "platanoides — habitus", type_="habitus"),
    wiki("2020 year. Herbarium. Acer platanoides. img-032.jpg", "platanoides — habitus", type_="habitus"),
]},

"Acer pseudoplatanus": {"photos": [
    wiki("Ahornallee zwischen Altweitra und Hörmanns 2017-10.jpg", "pseudoplatanus — habitus", type_="habitus"),
    wiki("The Martyrs tree - geograph.org.uk - 1277399.jpg", "pseudoplatanus — habitus", type_="habitus"),
    wiki("Acer pseudoplatanusAA.jpg", "pseudoplatanus — algemeen", type_="algemeen"),
]},

"Achillea millefolium": {"photos": [
    wiki("Achillea millefolium - Köhler–s Medizinal-Pflanzen-149.jpg", "millefolium — habitus", type_="habitus"),
    wiki("Achillea millefolium capitula 2002-11-18.jpg", "millefolium — habitus", type_="habitus"),
    wiki("Koeh-149.jpg", "millefolium — habitus", type_="habitus"),
]},

"Achillea ptarmica": {"photos": [
    wiki("(MHNT) Artemisia ludoviciana - Serres du Museum de Toulouse.jpg", "ptarmica — algemeen", type_="algemeen"),
    wiki("Achillea ptarmica (Sneeze-wort) - Theodore Green - 26 1931 7.jpg", "ptarmica — algemeen", type_="algemeen"),
    wiki("Achillea ptarmica - võsa-raudrohi.jpg", "ptarmica — algemeen", type_="algemeen"),
]},

"Aconitum carmichaelii": {"photos": [
    wiki("Miko vestal virgin robes, fan and torikabuto ( phoenix hat ).jpg", "carmichaelii — vrucht", type_="vrucht"),
    wiki("AconitumNapellusByKoehler1887.jpg", "carmichaelii — algemeen", type_="algemeen"),
    wiki("Aconitum carmichaelli 'arendsii' 27-10-2005 16.09.36.JPG", "carmichaelii — algemeen", type_="algemeen"),
]},

"Aegopodium podagraria": {"photos": [
    wiki("Aegopodium podagraria-(dkrb)-1.jpg", "podagraria — habitus", type_="habitus"),
    wiki("Aegopodium podagraria PID1588-2.jpg", "podagraria — habitus", type_="habitus"),
    wiki("Oenanthe crocata flowers.jpg", "podagraria — bloeiwijze", type_="bloeiwijze"),
]},

"Aesculus hippocastanum": {"photos": [
    wiki("10 Pest damage - horse-chestnut leaf miner (Cameraria ohridella) in Parma, Italy.jpg", "hippocastanum — vrucht", type_="vrucht"),
    wiki("Aesculus hippocastanum - geograph.org.uk - 7871740.jpg", "hippocastanum — vrucht", type_="vrucht"),
    wiki("Aesculus hippocastanum Paris 1.jpg", "hippocastanum — vrucht", type_="vrucht"),
]},

"Agapanthus hybriden": {"photos": [
    wiki("Agapanthus africanus in habitat photo Nick Helme CC by SA.jpg", "hybriden — habitus", type_="habitus"),
    wiki("Agapanthus Prebloom.jpg", "hybriden — bloeiwijze", type_="bloeiwijze"),
    wiki("Agapanthus begin bloom.JPG", "hybriden — bloeiwijze", type_="bloeiwijze"),
]},

"Ajuga reptans": {"photos": [
    wiki("Ajuga reptans young plant.JPG", "reptans — habitus", type_="habitus"),
    wiki("Fleur de bugle rampante.jpg", "reptans — bloeiwijze", type_="bloeiwijze"),
    wiki("(MHNT) Ajuga reptans - Inflorescence.jpg", "reptans — algemeen", type_="algemeen"),
]},

"Alcea rosea": {"photos": [
    wiki("Stockros (Althea rosea) - Ystad-2023.jpg", "rosea — habitus", type_="habitus"),
    wiki("'Blacknight' hollyhock IMG 9621.jpg", "rosea — algemeen", type_="algemeen"),
    wiki("2021-06-06 Althaea rosea タチアオイ（立葵、学名：Althaea rosea、シノニム：Alcea rosea）DSCF3025.jpg", "rosea — algemeen", type_="algemeen"),
]},

"Alchemilla mollis": {"photos": [
    wiki("Alchemilla mollis (Fraaie vrouwenmantel bloeiwijze)1.jpg", "mollis — algemeen", type_="algemeen"),
    wiki("Vrouwenmantel (Alchemilla mollis) d.j.b 02.jpg", "mollis — algemeen", type_="algemeen"),
]},

"Alliaria petiolata": {"photos": [
    wiki("(MHNT) Alliaria petiolata - flowers.jpg", "petiolata — bloeiwijze", type_="bloeiwijze"),
    wiki("Alliaria petiolataseeds.jpg", "petiolata — vrucht", type_="vrucht"),
    wiki("Alliaria petiolata marais-belloy-sur-somme 80 26042007 3.jpg", "petiolata — algemeen", type_="algemeen"),
]},

"Allium aflatunense": {"photos": [
    wiki("02 Allium sp. 02.jpg", "aflatunense — algemeen", type_="algemeen"),
    wiki("Allium aflatunense 5801.JPG", "aflatunense — algemeen", type_="algemeen"),
]},

"Allium giganteum": {"photos": [
    wiki("PurpleBallFlower.JPG", "giganteum — bloeiwijze", type_="bloeiwijze"),
    wiki("02 Allium sp. 02.jpg", "giganteum — algemeen", type_="algemeen"),
    wiki("Allium Giganteum (1).jpg", "giganteum — algemeen", type_="algemeen"),
]},

"Allium schoenoprasum": {"photos": [
    wiki("02 Allium sp. 02.jpg", "schoenoprasum — algemeen", type_="algemeen"),
    wiki("Allium oreophilum ÖBG 2014-05-25 (04).jpg", "schoenoprasum — algemeen", type_="algemeen"),
    wiki("Alliumspecies.jpg", "schoenoprasum — algemeen", type_="algemeen"),
]},

"Alnus glutinosa": {"photos": [
    wiki("Unterspreewald-Gross-Wasserburger-Spree-01.jpg", "glutinosa — habitus", type_="habitus"),
    wiki("20120904Alnus glutinosa01.jpg", "glutinosa — algemeen", type_="algemeen"),
    wiki("20120904Alnus glutinosa14.jpg", "glutinosa — algemeen", type_="algemeen"),
]},

"Amelanchier lamarckii": {"photos": [
    wiki("1024 Felsenbirne (Amelanchier obovalis)-2247.jpg", "lamarckii — habitus", type_="habitus"),
    wiki("Amelanchier bartramiana 15-p.bot-amel.bartra-03.jpg", "lamarckii — habitus", type_="habitus"),
    wiki("Amelanchier laevis 15-p.bot-amel.laevi-17.jpg", "lamarckii — habitus", type_="habitus"),
]},

"Anemone blanda": {"photos": [
    wiki("Ranuncolaceae - Anemone hortensis-2.JPG", "blanda — habitus", type_="habitus"),
    wiki("Anemone.png", "blanda — algemeen", type_="algemeen"),
    wiki("Anemone (PSF).png", "blanda — algemeen", type_="algemeen"),
]},

"Anemone coronaria": {"photos": [
    wiki("White-Anemone-coronaria-0011.jpg", "coronaria — habitus", type_="habitus"),
    wiki("Wiki-Calaniyot-Shokeda-ZE-001.jpg", "coronaria — habitus", type_="habitus"),
    wiki("2010. Выставка цветов в Донецке на день города 73.jpg", "coronaria — algemeen", type_="algemeen"),
]},

"Anthriscus sylvestris": {"photos": [
    wiki("Anthriscus sylvestris (Köhler's Medizinal-Pflanzen).jpg", "sylvestris — algemeen", type_="algemeen"),
    wiki("Anthriscus sylvestris TK 2021-05-16 2.jpg", "sylvestris — algemeen", type_="algemeen"),
    wiki("Anthriscus sylvestris W.jpg", "sylvestris — algemeen", type_="algemeen"),
]},

"Aquilegia vulgaris": {"photos": [
    wiki("Leaf 1 web.jpg", "vulgaris — blad", type_="blad"),
    wiki("Aquilegia nora barlow.JPG", "vulgaris — algemeen", type_="algemeen"),
    wiki("Aquilegia vulgaris, Santa Coloma de Farners 03.jpg", "vulgaris — algemeen", type_="algemeen"),
]},

"Arabis caucasica": {"photos": [
    wiki("Arabis caucasica 002.JPG", "caucasica — algemeen", type_="algemeen"),
    wiki("Barbarea vulgaris 002.JPG", "caucasica — algemeen", type_="algemeen"),
]},

"Armeria maritima": {"photos": [
    wiki("20230519 Gewöhnliche Grasnelke (Armeria maritima).jpg", "maritima — algemeen", type_="algemeen"),
    wiki("Armeria maritima Dunnet Head.jpg", "maritima — algemeen", type_="algemeen"),
    wiki("Pescadero Beach - panoramio.jpg", "maritima — algemeen", type_="algemeen"),
]},

"Aster frikartii": {"photos": [
    wiki("Bloeiwijze van Aster x frikartii 'Mönch'. Locatie, Tuinreservaat Jonkervallei 02.jpg", "frikartii — algemeen", type_="algemeen"),
    wiki("Aster x frikartii 'Mönch' 02.JPG", "frikartii — algemeen", type_="algemeen"),
    wiki("Bloeiwijze van Aster x frikartii 'Mönch'. Locatie, Tuinreservaat Jonkervallei 01.jpg", "frikartii — algemeen", type_="algemeen"),
]},

"Astrantia major": {"photos": [
    wiki("Apiaceae - Astrantia major-1.JPG", "major — habitus", type_="habitus"),
    wiki("Apiaceae - Astrantia major-2.JPG", "major — habitus", type_="habitus"),
    wiki("Closeup of Astrantia Major flower.jpg", "major — bloeiwijze", type_="bloeiwijze"),
]},

"Atriplex hortensis": {"photos": [
    wiki("Atriplex hortensis MHNT.BOT.2013.22.60.jpg", "hortensis — algemeen", type_="algemeen"),
    wiki("Atriplex hortensis cleaned Sturm.png", "hortensis — algemeen", type_="algemeen"),
    wiki("Atriplex hortensis sl20.jpg", "hortensis — algemeen", type_="algemeen"),
]},

"Aubrieta": {"photos": [
    wiki("Purple rock cress.JPG", "Aubrieta — algemeen", type_="algemeen"),
]},

"Aucuba japonica": {"photos": [
    wiki("Aucuba japonica Gold Dust NBG LR.jpg", "japonica — algemeen", type_="algemeen"),
    wiki("Aucuba japonica MHNT.BOT.2007.40.91.jpg", "japonica — algemeen", type_="algemeen"),
    wiki("Garryaceae - Aucuba japonica.JPG", "japonica — algemeen", type_="algemeen"),
]},

"Aurinia saxatilis": {"photos": [
    wiki("Aurinia saxatilis TK 2021-04-22 4.jpg", "saxatilis — algemeen", type_="algemeen"),
]},

"Begonia semperflorens": {"photos": [
    wiki("Begonia blossoms maleandfemale.jpg", "semperflorens — bloeiwijze", type_="bloeiwijze"),
    wiki("Begonia johnstonii Flower 01.jpg", "semperflorens — bloeiwijze", type_="bloeiwijze"),
    wiki("Begonia 'Parviflora' Leaf 3000px.jpg", "semperflorens — blad", type_="blad"),
]},

"Bellis perennis": {"photos": [
    wiki("Bellis perennis - flowers (18739573142).jpg", "perennis — bloeiwijze", type_="bloeiwijze"),
    wiki("Bellis perennis 'Tasso Red' Stokrotka pospolita 2022-04-09 02.jpg", "perennis — algemeen", type_="algemeen"),
    wiki("Bellis perennis (8580127027).jpg", "perennis — algemeen", type_="algemeen"),
]},

"Berberis julianae": {"photos": [
    wiki("Berberis ilicifolia (drawing in colour).jpg", "julianae — algemeen", type_="algemeen"),
    wiki("Berberis julianae B.jpg", "julianae — algemeen", type_="algemeen"),
]},

"Berberis thunbergii": {"photos": [
    wiki("Berberis thunbergii flowers in Pennwood State Park.jpg", "thunbergii — bloeiwijze", type_="bloeiwijze"),
    wiki("Japanese barberry.jpg", "thunbergii — vrucht", type_="vrucht"),
    wiki("Berberis thunb frt.jpg", "thunbergii — algemeen", type_="algemeen"),
]},

"Berberis vulgaris": {"photos": [
    wiki("Berberis-vulgaris-flowers.jpg", "vulgaris — bloeiwijze", type_="bloeiwijze"),
    wiki("Dried barberries on a plate.JPG", "vulgaris — vrucht", type_="vrucht"),
    wiki("Berberis vulgaris .jpg", "vulgaris — algemeen", type_="algemeen"),
]},

"Betula pendula": {"photos": [
    wiki("B. pendula, Koivu Birch, end of August 2.jpg", "pendula — algemeen", type_="algemeen"),
    wiki("Betula pendula - Childwall Woods & Fields 01.jpg", "pendula — algemeen", type_="algemeen"),
    wiki("Betula pendula Finland.jpg", "pendula — algemeen", type_="algemeen"),
]},

"Betula pubescens": {"photos": [
    wiki("Niitvälja soo sookask 31-12-2017.jpg", "pubescens — habitus", type_="habitus"),
    wiki("Acronicta auricoma - Betula pubescens - Niitvälja bog.jpg", "pubescens — vrucht", type_="vrucht"),
    wiki("Betula pubescens - Burgwald 002.jpg", "pubescens — vrucht", type_="vrucht"),
]},

"Brunnera macrophylla": {"photos": [
    wiki("(MHNT) Brunnera macrophylla, flowers - Les Martels, Giroussens Tarn.jpg", "macrophylla — bloeiwijze", type_="bloeiwijze"),
    wiki("Heliotropium arborescens 5.jpg", "macrophylla — algemeen", type_="algemeen"),
]},

"Buddleja davidii": {"photos": [
    wiki("Monarch Butterfly Flower.jpg", "davidii — bloeiwijze", type_="bloeiwijze"),
    wiki("Buddleja davidii seeds.jpg", "davidii — vrucht", type_="vrucht"),
    wiki("Buddleia2.jpg", "davidii — algemeen", type_="algemeen"),
]},

"Buxus sempervirens": {"photos": [
    wiki("Buisfleurs.jpg", "sempervirens — bloeiwijze", type_="bloeiwijze"),
    wiki("AldenBiesen02.jpg", "sempervirens — algemeen", type_="algemeen"),
    wiki("Boxwood Buxus sempervirens var. arborescens Bark 2597px.jpg", "sempervirens — algemeen", type_="algemeen"),
]},

"Calamagrostis x acutiflora": {"photos": [
    wiki("CBG Circle Gdn - Calamagrostis x acutiflora 'Eldorado', Canna 'Cannova Red Shades', Agastache 'Tutti-Frutti' 150627 (20326371402).jpg", "acutiflora — algemeen", type_="algemeen"),
    wiki("Calamagrostis × acutiflora Overdam 2zz.jpg", "acutiflora — algemeen", type_="algemeen"),
]},

"Calendula officinalis": {"photos": [
    wiki("Flower July 2013-2.jpg", "officinalis — bloeiwijze", type_="bloeiwijze"),
    wiki("Calendula officinalis, pot marigold.JPG", "officinalis — algemeen", type_="algemeen"),
    wiki("Calendula officinalis 003.JPG", "officinalis — algemeen", type_="algemeen"),
]},

"Calluna vulgaris": {"photos": [
    wiki("CallunaVulgaris.jpg", "vulgaris — algemeen", type_="algemeen"),
]},

"Caltha palustris": {"photos": [
    wiki("Caltha palustris plant.JPG", "palustris — habitus", type_="habitus"),
    wiki("Caltha palustris seeds USDA.jpg", "palustris — vrucht", type_="vrucht"),
    wiki("Caltha palustris (navadna kalužnica).jpg", "palustris — algemeen", type_="algemeen"),
]},

"Calystegia sepium": {"photos": [
    wiki("Calystegia April 2008-1.jpg", "sepium — habitus", type_="habitus"),
    wiki("Calystegia sepium 02.jpg", "sepium — algemeen", type_="algemeen"),
    wiki("Calystegia sepium 05.jpg", "sepium — algemeen", type_="algemeen"),
]},

"Campanula carpatica": {"photos": [
    wiki("Campanula carpatica a2.jpg", "carpatica — algemeen", type_="algemeen"),
    wiki("Campanula cespitosa.jpg", "carpatica — algemeen", type_="algemeen"),
]},

"Campanula portenschlagiana": {"photos": [
    wiki("Campanula portenschlagiana A.jpg", "portenschlagiana — algemeen", type_="algemeen"),
]},

"Capsella bursa-pastoris": {"photos": [
    wiki("A_Field_of_Shepherd’s-purse.jpg", "bursa-pastoris — bloeiwijze", type_="bloeiwijze"),
    wiki("A Field of Shepherd’s-purse.jpg", "bursa-pastoris — algemeen", type_="algemeen"),
    wiki("Capsella bursa-pastoris Sturm23.jpg", "bursa-pastoris — algemeen", type_="algemeen"),
]},

"Cardamine hirsuta": {"photos": [
    wiki("Kleine veldkers Cardamine hirsuta plant.jpg", "hirsuta — habitus", type_="habitus"),
    wiki("Pollens of Cardamine hirsuta.jpg", "hirsuta — bloeiwijze", type_="bloeiwijze"),
    wiki("碎米荠种子 Seed of Cardamine hirsuta.jpg", "hirsuta — vrucht", type_="vrucht"),
]},

"Cardamine pratensis": {"photos": [
    wiki("Wiesenschaumkraut_(Cardamine_pratensis)-20200416-RM-095356.jpg", "pratensis — bloeiwijze", type_="bloeiwijze"),
    wiki("Wiesenschaumkraut (Cardamine pratensis)-20200416-RM-095356.jpg", "pratensis — habitus", type_="habitus"),
    wiki("Cuckoo flower Wiltshire.JPG", "pratensis — bloeiwijze", type_="bloeiwijze"),
]},

"Carex buchananii": {"photos": [
    wiki("Starr-120613-9611-Carex_buchananii-stems-Home_Depot_Nursery_Kahului-Maui_(25119122576).jpg", "buchananii — bloeiwijze", type_="bloeiwijze"),
    wiki("Starr-120613-9611-Carex buchananii-stems-Home Depot Nursery Kahului-Maui (25119122576).jpg", "buchananii — algemeen", type_="algemeen"),
]},

"Carpinus betulus": {"photos": [
    wiki("Carpinus_betulus_-_Hunsrück_001.jpg", "betulus — bloeiwijze", type_="bloeiwijze"),
    wiki("Common hornbeam growing in plastic tree shelter tube inside view.jpg", "betulus — habitus", type_="habitus"),
    wiki("Carpinus fruit.jpg", "betulus — vrucht", type_="vrucht"),
]},

"Cedrus atlantica": {"photos": [
    wiki("Cedrus atlantica male cones.jpg", "atlantica — vrucht", type_="vrucht"),
    wiki("Cedrus libani ssp. atlantica 'Glauca' cone 02 by Line1.jpg", "atlantica — vrucht", type_="vrucht"),
    wiki("Blue Atlas cedar.jpg", "atlantica — algemeen", type_="algemeen"),
]},

"Centaurea cyanus": {"photos": [
    wiki("Centaurea_cyanus_flower_001.jpg", "cyanus — bloeiwijze", type_="bloeiwijze"),
    wiki("005 Cornflower petals - edible flower on ice cream.jpg", "cyanus — bloeiwijze", type_="bloeiwijze"),
    wiki("Bachelor's button, Basket flower, Boutonniere flower, Cornflower - 3.jpg", "cyanus — bloeiwijze", type_="bloeiwijze"),
]},

"Centaurea montana": {"photos": [
    wiki("Centaura de las montañas - Centaurea montana (9583677454).jpg", "montana — algemeen", type_="algemeen"),
    wiki("Centaurea montana.jpg", "montana — algemeen", type_="algemeen"),
]},

"Cerastium fontanum": {"photos": [
    wiki("Gewone_hoornbloem_R0019819.JPG", "fontanum — bloeiwijze", type_="bloeiwijze"),
    wiki("Gewone hoornbloem R0019819.JPG", "fontanum — bloeiwijze", type_="bloeiwijze"),
    wiki("Mouse-ear Chickweed (49195024206).jpg", "fontanum — algemeen", type_="algemeen"),
]},

"Cerastium tomentosum": {"photos": [
    wiki("Cerastium_tomentosum.jpg", "tomentosum — bloeiwijze", type_="bloeiwijze"),
    wiki("Cerastium tomentosum flower.jpg", "tomentosum — bloeiwijze", type_="bloeiwijze"),
    wiki("Cerastium tomentosum.jpg", "tomentosum — algemeen", type_="algemeen"),
]},

"Chamaecyparis lawsoniana": {"photos": [
    wiki("Lawson cypress male cones.jpg", "lawsoniana — vrucht", type_="vrucht"),
    wiki("Chamaecyparis lawsoniana.jpg", "lawsoniana — algemeen", type_="algemeen"),
    wiki("Chamaecyparis lawsoniana Dorena1.jpg", "lawsoniana — algemeen", type_="algemeen"),
]},

"Chelidonium majus": {"photos": [
    wiki("Chelidonium majus - Köhler–s Medizinal-Pflanzen-033.jpg", "majus — habitus", type_="habitus"),
    wiki("Koeh-033.jpg", "majus — habitus", type_="habitus"),
    wiki("Flower October 2008-1.jpg", "majus — bloeiwijze", type_="bloeiwijze"),
]},

"Cirsium arvense": {"photos": [
    wiki("Cirsium_arvense_with_Bees_Richard_Bartz.jpg", "arvense — bloeiwijze", type_="bloeiwijze"),
    wiki("Carduelis carduelis2.jpg", "arvense — algemeen", type_="algemeen"),
    wiki("Cirsium arvense - pappus (aka).jpg", "arvense — algemeen", type_="algemeen"),
]},

"Citrus trifoliata": {"photos": [
    wiki("Bergapten-from-xtal-3D-bs-17.png", "trifoliata — habitus", type_="habitus"),
    wiki("Citrus canker on fruit.jpg", "trifoliata — vrucht", type_="vrucht"),
    wiki("Ichangfruit.jpg", "trifoliata — vrucht", type_="vrucht"),
]},

"Claytonia perfoliata": {"photos": [
    wiki("Claytonia_perfoliata_6641.JPG", "perfoliata — bloeiwijze", type_="bloeiwijze"),
    wiki("Claytonia perfoliata basal leaves 2003-02-04.jpg", "perfoliata — blad", type_="blad"),
    wiki("Claytone de Cuba2.jpg", "perfoliata — algemeen", type_="algemeen"),
]},

"Clematis armandii": {"photos": [
    wiki("Clematis_armandii01-4035~2015_03_22.JPG", "armandii — bloeiwijze", type_="bloeiwijze"),
    wiki("Clematis armandii01-4035~2015 03 22.JPG", "armandii — algemeen", type_="algemeen"),
    wiki("Heart of gold.JPG", "armandii — algemeen", type_="algemeen"),
]},

"Clematis jackmanii": {"photos": [
    wiki("Large purple clematis flower with white finger stamens.jpg", "jackmanii — bloeiwijze", type_="bloeiwijze"),
    wiki("Clematis seeds.jpg", "jackmanii — vrucht", type_="vrucht"),
    wiki("Old man's beard Clematis vitalba seeds.jpg", "jackmanii — vrucht", type_="vrucht"),
]},

"Clematis vitalba": {"photos": [
    wiki("Ranuncolaceae - Clematis vitalba-1.JPG", "vitalba — habitus", type_="habitus"),
    wiki("Ranuncolaceae - Clematis vitalba-3.JPG", "vitalba — habitus", type_="habitus"),
    wiki("Clematis-vitalba-Waldrebe(Samenstand).jpg", "vitalba — algemeen", type_="algemeen"),
]},

"Cordyline australis": {"photos": [
    wiki("CabbageTreeKaihoka.jpg", "australis — bloeiwijze", type_="bloeiwijze"),
    wiki("Cabbage-tree-inflorescence-branching-order.png", "australis — habitus", type_="habitus"),
    wiki("Cabbage trees in front of Anchor Bay, Tawharanui Peninsula.jpg", "australis — habitus", type_="habitus"),
]},

"Coreopsis verticillata": {"photos": [
    wiki("Coreopsis lanceolata - flower view 01.jpg", "verticillata — bloeiwijze", type_="bloeiwijze"),
    wiki("Coreopsis lanceolata - flower view 02.jpg", "verticillata — bloeiwijze", type_="bloeiwijze"),
    wiki("Coreopsis, 2024.jpg", "verticillata — algemeen", type_="algemeen"),
]},

"Cornus alba": {"photos": [
    wiki("Cornus_alba_a2.jpg", "alba — bloeiwijze", type_="bloeiwijze"),
    wiki("Cornus9389.JPG", "alba — algemeen", type_="algemeen"),
    wiki("Cornus alba 'Ivory Halo®'.jpg", "alba — algemeen", type_="algemeen"),
]},

"Cornus sericea": {"photos": [
    wiki("Cornus sericea habit.jpg", "sericea — habitus", type_="habitus"),
    wiki("Cornus sericea flower.jpg", "sericea — bloeiwijze", type_="bloeiwijze"),
    wiki("Cornus sericea seed.png", "sericea — vrucht", type_="vrucht"),
]},

"Cortaderia selloana": {"photos": [
    wiki("Herbe_Pampa_FR_2008.jpg", "selloana — bloeiwijze", type_="bloeiwijze"),
    wiki("Plantae Cortaderia Selloana(Pampas Grass) Flora.jpg", "selloana — habitus", type_="habitus"),
    wiki("Cortadera.jpg", "selloana — algemeen", type_="algemeen"),
]},

"Corylus avellana": {"photos": [
    wiki("Corylus avellana female flower - Keila.jpg", "avellana — bloeiwijze", type_="bloeiwijze"),
    wiki("Hazelnut in blossom.jpg", "avellana — vrucht", type_="vrucht"),
    wiki("Hazelnuts (Corylus avellana) - whole with kernels.jpg", "avellana — vrucht", type_="vrucht"),
]},

"Cosmos bipinnatus": {"photos": [
    wiki("Cosmos_bipinnatus_pink,_Burdwan,_West_Bengal,_India_10_01_2013.jpg", "bipinnatus — bloeiwijze", type_="bloeiwijze"),
    wiki("Cosmos bipinnatus flower bud.jpg", "bipinnatus — bloeiwijze", type_="bloeiwijze"),
    wiki("Cosmos bipinnatus flowers in Sivas, Turkey.jpg", "bipinnatus — bloeiwijze", type_="bloeiwijze"),
]},

"Cotinus coggygria": {"photos": [
    wiki("Cotinus coggygria Скумпия кожевенная European smoketree.jpg", "coggygria — habitus", type_="habitus"),
    wiki("DaydreamSmokeTree.jpg", "coggygria — habitus", type_="habitus"),
    wiki("Cotinus coggygria autumn leaf.jpg", "coggygria — blad", type_="blad"),
]},

"Cotoneaster suecicus": {"photos": [
    wiki("Cotoneaster frigidus.jpg", "suecicus — algemeen", type_="algemeen"),
]},

"Crataegus laevigata": {"photos": [
    wiki("Crataegus_laevigata-flowers.jpg", "laevigata — bloeiwijze", type_="bloeiwijze"),
    wiki("Crataegus laevigata-flowers.jpg", "laevigata — bloeiwijze", type_="bloeiwijze"),
    wiki("Aubépine épineuse. Crataegus laevigata. Mahieddine Boumendjel.jpg", "laevigata — algemeen", type_="algemeen"),
]},

"Crataegus monogyna": {"photos": [
    wiki("Hawthorn_fruit.JPG", "monogyna — bloeiwijze", type_="bloeiwijze"),
    wiki("(MHNT) Crataegus monogyna - flowers and buds.jpg", "monogyna — bloeiwijze", type_="bloeiwijze"),
    wiki("2013-05-23 07 24 06 Crataegus monogyna 'Crimson Cloud' blossoms in Elko Nevada.jpg", "monogyna — bloeiwijze", type_="bloeiwijze"),
]},

"Crocus chrysanthus": {"photos": [
    wiki("CrocusEABowles.jpg", "chrysanthus — algemeen", type_="algemeen"),
    wiki("Crocus 'Blue Pearl'05.jpg", "chrysanthus — algemeen", type_="algemeen"),
]},

"Dahlia hybriden": {"photos": [
    wiki("Collarette Dahlia - \"Apple Blossom\" cultivar.jpg", "hybriden — bloeiwijze", type_="bloeiwijze"),
    wiki("Dahlia Almost Bloomed (2).jpg", "hybriden — bloeiwijze", type_="bloeiwijze"),
    wiki("Dahlia Blooming.jpg", "hybriden — bloeiwijze", type_="bloeiwijze"),
]},

"Deutzia gracilis": {"photos": [
    wiki("Deutzia gracilis A.jpg", "gracilis — algemeen", type_="algemeen"),
    wiki("Deutzia gracilis C.jpg", "gracilis — algemeen", type_="algemeen"),
]},

"Dianthus barbatus": {"photos": [
    wiki("Dianthus_barbatus_flowers_01.jpg", "barbatus — bloeiwijze", type_="bloeiwijze"),
    wiki("Gerard John 1545-1612.jpg", "barbatus — habitus", type_="habitus"),
    wiki("Dianthus barbatus flowers 01.jpg", "barbatus — bloeiwijze", type_="bloeiwijze"),
]},

"Dianthus deltoides": {"photos": [
    wiki("0_Dianthus_deltoides_alpinus_-_Yvoire.JPG", "deltoides — bloeiwijze", type_="bloeiwijze"),
    wiki("0 Dianthus deltoides alpinus - Yvoire.JPG", "deltoides — algemeen", type_="algemeen"),
    wiki("Red campion close 700.jpg", "deltoides — algemeen", type_="algemeen"),
]},

"Dicentra spectabilis": {"photos": [
    wiki("Dicentra canadensis - Canadian Heart Flower.jpg", "spectabilis — bloeiwijze", type_="bloeiwijze"),
    wiki("Fringed bleeding-heart flower cluster.jpg", "spectabilis — bloeiwijze", type_="bloeiwijze"),
    wiki("Dicentra 'King of Hearts' and 'Ivory Hearts'.jpg", "spectabilis — algemeen", type_="algemeen"),
]},

"Diervilla sessilifolia": {"photos": [
    wiki("Diervilla-sessilifolia-bloom.jpg", "sessilifolia — bloeiwijze", type_="bloeiwijze"),
    wiki("Diervilla-sessilifolia.JPG", "sessilifolia — algemeen", type_="algemeen"),
]},

"Digitalis purpurea": {"photos": [
    wiki("Digitalis_purpurea_LC0101.jpg", "purpurea — bloeiwijze", type_="bloeiwijze"),
    wiki("Digitalis purpurea 'Primrose Carousel' Flower Closeup 1200px.jpg", "purpurea — bloeiwijze", type_="bloeiwijze"),
    wiki("Digitalis purpurea - flower view01.jpg", "purpurea — bloeiwijze", type_="bloeiwijze"),
]},

"Doronicum orientale": {"photos": [
    wiki("Doronicum_orientale.JPG", "orientale — bloeiwijze", type_="bloeiwijze"),
    wiki("2007-03-28Doronicum orientale04.jpg", "orientale — algemeen", type_="algemeen"),
    wiki("Doronicum orientale.JPG", "orientale — algemeen", type_="algemeen"),
]},

"Echinacea purpurea": {"photos": [
    wiki("Echinacea_purpurea_Grandview_Prairie.jpg", "purpurea — bloeiwijze", type_="bloeiwijze"),
    wiki("Echinacea-purpura-flower-closeup.jpg", "purpurea — bloeiwijze", type_="bloeiwijze"),
    wiki("Dried Echinacea Spines.jpg", "purpurea — algemeen", type_="algemeen"),
]},

"Echinops bannaticus": {"photos": [
    wiki("Echinops_bannaticus01.jpg", "bannaticus — bloeiwijze", type_="bloeiwijze"),
    wiki("Blå bolltistel - (Echinops bannaticus) - Ystad-2021.jpg", "bannaticus — habitus", type_="habitus"),
    wiki("CDC artichoke.jpg", "bannaticus — algemeen", type_="algemeen"),
]},

"Elytrigia repens": {"photos": [
    wiki("Kweek blad Elytrigia repens.jpg", "repens — blad", type_="blad"),
    wiki("Kweek Elytrigia repens.jpg", "repens — algemeen", type_="algemeen"),
    wiki("Elytrigia repens blatt.jpeg", "repens — algemeen", type_="algemeen"),
]},

"Equisetum arvense": {"photos": [
    wiki("Equisetum_arvense_foliage.jpg", "arvense — bloeiwijze", type_="bloeiwijze"),
    wiki("01-Stack 201 Equisetum 10x obj leaf print.jpg", "arvense — blad", type_="blad"),
    wiki("Equisetum arvense foliage.jpg", "arvense — blad", type_="blad"),
]},

"Erica carnea": {"photos": [
    wiki("Erica carnea 003.JPG", "carnea — algemeen", type_="algemeen"),
    wiki("Erica carnea Springwood.JPG", "carnea — algemeen", type_="algemeen"),
    wiki("Erica carnea close-up.jpg", "carnea — algemeen", type_="algemeen"),
]},

"Erigeron canadensis": {"photos": [
    wiki("Erigeron_canadensis_from_Britain_by_D_Merrick_14.jpg", "canadensis — bloeiwijze", type_="bloeiwijze"),
    wiki("Canadese fijnstraal plant Conyza canadensis.jpg", "canadensis — habitus", type_="habitus"),
    wiki("Conyza-canadensis-seeds.jpg", "canadensis — vrucht", type_="vrucht"),
]},

"Erysimum": {"photos": [
    wiki("Erysimum-scoparium.jpg", "Erysimum — algemeen", type_="algemeen"),
    wiki("ErysimumCheiranthoides.jpg", "Erysimum — algemeen", type_="algemeen"),
    wiki("ErysimumChelseaJacket.jpg", "Erysimum — algemeen", type_="algemeen"),
]},

"Eucalyptus gunnii": {"photos": [
    wiki("Eucalyptus_gunni_flowers.jpg", "gunnii — bloeiwijze", type_="bloeiwijze"),
    wiki("Eucalyptus gunni flowers.jpg", "gunnii — bloeiwijze", type_="bloeiwijze"),
    wiki("E. gunnii.JPG", "gunnii — algemeen", type_="algemeen"),
]},

"Euphorbia epithymoides": {"photos": [
    wiki("Euphorbia_epithymoides_MA.jpg", "epithymoides — bloeiwijze", type_="bloeiwijze"),
    wiki("Euphorbia amygdaloides cv Purpurea5 ies.jpg", "epithymoides — algemeen", type_="algemeen"),
    wiki("Euphorbia epithymoides MA.jpg", "epithymoides — algemeen", type_="algemeen"),
]},

"Fagus sylvatica": {"photos": [
    wiki("Fagus-sylvatica-cansiglio-forest-italy.jpg", "sylvatica — bloeiwijze", type_="bloeiwijze"),
    wiki("Hyde park tree.jpg", "sylvatica — habitus", type_="habitus"),
    wiki("Møns Klint beech trees in gorge 2015-04-01-4864.jpg", "sylvatica — habitus", type_="habitus"),
]},

"Fallopia baldschuanica": {"photos": [
    wiki("Polygonumbaldschuanicum.jpg", "baldschuanica — algemeen", type_="algemeen"),
]},

"Festuca glauca": {"photos": [
    wiki("Festuca_glauca_001_Tehran_Botanical_garden_2016.jpg", "glauca — bloeiwijze", type_="bloeiwijze"),
    wiki("Festuca glauca 001 Tehran Botanical garden 2016.jpg", "glauca — algemeen", type_="algemeen"),
    wiki("Festuca glauca small.jpg", "glauca — algemeen", type_="algemeen"),
]},

"Ficaria verna": {"photos": [
    wiki("Double-flowered lesser celandine.jpg", "verna — bloeiwijze", type_="bloeiwijze"),
    wiki("Flowers (2425723494) cropped.jpg", "verna — bloeiwijze", type_="bloeiwijze"),
    wiki("White- and yellow-flowered lesser celandines.jpg", "verna — bloeiwijze", type_="bloeiwijze"),
]},

"Filipendula ulmaria": {"photos": [
    wiki("20140715Filipendula ulmaria.jpg", "ulmaria — algemeen", type_="algemeen"),
    wiki("Ectropis crepuscularia caterpillar - Keila.jpg", "ulmaria — algemeen", type_="algemeen"),
    wiki("Filipendula ulmaria Sturm12.jpg", "ulmaria — algemeen", type_="algemeen"),
]},

"Foeniculum vulgare": {"photos": [
    wiki("Foeniculum July 2011-1a.jpg", "vulgare — algemeen", type_="algemeen"),
]},

"Forsythia x intermedia": {"photos": [
    wiki("Forsythia intermedia a1.jpg", "intermedia — algemeen", type_="algemeen"),
    wiki("Forsythia x intermedia 0zz.jpg", "intermedia — algemeen", type_="algemeen"),
]},

"Fragaria vesca": {"photos": [
    wiki("Walderdbeere Frucht-20210617-RM-124006.jpg", "vesca — habitus", type_="habitus"),
    wiki("Fragaria vesca seeds USDA-ARS.jpg", "vesca — vrucht", type_="vrucht"),
    wiki("PerfectStrawberry.jpg", "vesca — vrucht", type_="vrucht"),
]},

"Fraxinus excelsior": {"photos": [
    wiki("Fused Ash Trees.JPG", "excelsior — habitus", type_="habitus"),
    wiki("Ash flower.JPG", "excelsior — bloeiwijze", type_="bloeiwijze"),
    wiki("EurAshLeaf.jpg", "excelsior — blad", type_="blad"),
]},

"Fritillaria imperialis": {"photos": [
    wiki("Red Flower 777.jpg", "imperialis — bloeiwijze", type_="bloeiwijze"),
    wiki("2008-04-23 Berlin Schlosspark Charlottenburg Fritillaria imperialis.jpg", "imperialis — algemeen", type_="algemeen"),
    wiki("Corona imperial (Fritillaria imperialis), Jardín Botánico, Múnich, Alemania 2012-04-21, DD 01.JPG", "imperialis — algemeen", type_="algemeen"),
]},

"Fritillaria meleagris": {"photos": [
    wiki("Fritillaria (3).jpg", "meleagris — algemeen", type_="algemeen"),
    wiki("Fritillaria meleagris0.jpg", "meleagris — algemeen", type_="algemeen"),
    wiki("Fritillaria meleagris 002.JPG", "meleagris — algemeen", type_="algemeen"),
]},

"Fuchsia hybriden": {"photos": [
    wiki("Fuchsia flowerフクシアの花7137619.jpg", "hybriden — bloeiwijze", type_="bloeiwijze"),
    wiki("Fuchsia hybrida - flower view 01.jpg", "hybriden — bloeiwijze", type_="bloeiwijze"),
    wiki("Fuchsia regia - blossom (aka).jpg", "hybriden — bloeiwijze", type_="bloeiwijze"),
]},

"Galanthus nivalis": {"photos": [
    wiki("Distribution of the galanthus species.png", "nivalis — algemeen", type_="algemeen"),
    wiki("Galanthus Nivalis, sneeuwklokje. 12-02-2024. (d.j.b.).jpg", "nivalis — algemeen", type_="algemeen"),
    wiki("Galanthus nivalis.jpg", "nivalis — algemeen", type_="algemeen"),
]},

"Galinsoga parviflora": {"photos": [
    wiki("Estrellitas (Galinsoga parviflora).jpg", "parviflora — algemeen", type_="algemeen"),
    wiki("Galinsoga parviflora var. semicalva - Flickr - aspidoscelis.jpg", "parviflora — algemeen", type_="algemeen"),
]},

"Galium aparine": {"photos": [
    wiki("Flowers February 2008-4.jpg", "aparine — bloeiwijze", type_="bloeiwijze"),
    wiki("Cleaver plant leaf under microscope.jpg", "aparine — blad", type_="blad"),
    wiki("Galium.aparine.jpg", "aparine — algemeen", type_="algemeen"),
]},

"Galium odoratum": {"photos": [
    wiki("Galium odoratum Flower.JPG", "odoratum — bloeiwijze", type_="bloeiwijze"),
    wiki("Am.Grossen.Plunzsee.Buchenwald.Grumsin.Waldmeister.jpg", "odoratum — algemeen", type_="algemeen"),
    wiki("Galium odoratum Przytulia wonna 2022-08-11 Staszów 01.jpg", "odoratum — algemeen", type_="algemeen"),
]},

"Geranium endressii": {"photos": [
    wiki("2013-05-09 15-28-19-fleur.JPG", "endressii — bloeiwijze", type_="bloeiwijze"),
    wiki("Geranium endressii.jpg", "endressii — algemeen", type_="algemeen"),
]},

"Geranium phaeum": {"photos": [
    wiki("2013-05-09 15-28-19-fleur.JPG", "phaeum — bloeiwijze", type_="bloeiwijze"),
    wiki("Geranium phaeum Bodziszek żałobny 03.jpg", "phaeum — algemeen", type_="algemeen"),
]},

"Geranium pratense": {"photos": [
    wiki("2013-05-09 15-28-19-fleur.JPG", "pratense — bloeiwijze", type_="bloeiwijze"),
    wiki("Geranium pratense Aberystwyth flower.jpg", "pratense — bloeiwijze", type_="bloeiwijze"),
    wiki("Geranium pratense Aberystwyth leaf.jpg", "pratense — blad", type_="blad"),
]},

"Geranium sanguineum": {"photos": [
    wiki("Geraniaceae - Geranium sanguineum-1.JPG", "sanguineum — habitus", type_="habitus"),
    wiki("Geraniaceae - Geranium sanguineum-2.JPG", "sanguineum — habitus", type_="habitus"),
    wiki("Geraniaceae - Geranium sanguineum-3.JPG", "sanguineum — habitus", type_="habitus"),
]},

"Geum rivale": {"photos": [
    wiki("(MHNT) Geum rivale - flower and bottoms.jpg", "rivale — bloeiwijze", type_="bloeiwijze"),
    wiki("Geum rivale flower - Keila.jpg", "rivale — bloeiwijze", type_="bloeiwijze"),
    wiki("Geum rivale flowers.jpg", "rivale — bloeiwijze", type_="bloeiwijze"),
]},

"Geum urbanum": {"photos": [
    wiki("(MHNT) Geum urbanum - Habit.jpg", "urbanum — habitus", type_="habitus"),
    wiki("(MHNT) Geum urbanum - Buds and flower.jpg", "urbanum — bloeiwijze", type_="bloeiwijze"),
    wiki("(MHNT) Geum urbanum - flower.jpg", "urbanum — bloeiwijze", type_="bloeiwijze"),
]},

"Ginkgo biloba": {"photos": [
    wiki("Fossil Plant Ginkgo.jpg", "biloba — habitus", type_="habitus"),
    wiki("GINKGOBAUM-2.jpg", "biloba — habitus", type_="habitus"),
    wiki("Ginkgo-reborn-2.jpg", "biloba — habitus", type_="habitus"),
]},

"Glechoma hederacea": {"photos": [
    wiki("Glechoma hederacea, Hondsdraf (1).jpg", "hederacea — algemeen", type_="algemeen"),
    wiki("Glechoma hederacea - Keila.jpg", "hederacea — algemeen", type_="algemeen"),
    wiki("Ground Ivy (Glechoma hederacea) Spectral comparison Vis UV IR.jpg", "hederacea — algemeen", type_="algemeen"),
]},

"Gypsophila paniculata": {"photos": [
    wiki("Close-up of 2 baby's breath (Gypsophila paniculata) flowers.jpg", "paniculata — bloeiwijze", type_="bloeiwijze"),
    wiki("Gypsophila paniculata sl17.jpg", "paniculata — algemeen", type_="algemeen"),
    wiki("Illustration Gypsophila paniculata0.jpg", "paniculata — algemeen", type_="algemeen"),
]},

"Hedera helix": {"photos": [
    wiki("Hedera helix 2 beentree bialowieza 2005.jpg", "helix — habitus", type_="habitus"),
    wiki("Blad van klimop (Hedera helix) 02.JPG", "helix — blad", type_="blad"),
    wiki("Starr-071024-9905-Hedera helix-variegated leaves-Enchanting Floral Gardens of Kula-Maui (24895451805).jpg", "helix — blad", type_="blad"),
]},

"Helianthemum": {"photos": [
    wiki("Helianthemum alypoides (flor).jpg", "Helianthemum — algemeen", type_="algemeen"),
    wiki("Helianthemum hirtum.jpg", "Helianthemum — algemeen", type_="algemeen"),
    wiki("Helianthemum nummularium subsp obscurum 300907.jpg", "Helianthemum — algemeen", type_="algemeen"),
]},

"Helianthus annuus": {"photos": [
    wiki("Flower bud of Sunflower - Helianthus.JPG", "annuus — bloeiwijze", type_="bloeiwijze"),
    wiki("Helianthus annuus - flower view 01.jpg", "annuus — bloeiwijze", type_="bloeiwijze"),
    wiki("I-40W-Sunflowers.jpg", "annuus — bloeiwijze", type_="bloeiwijze"),
]},

"Helleborus niger": {"photos": [
    wiki("Helleborus niger volunteer seedling 02.JPG", "niger — vrucht", type_="vrucht"),
    wiki("Black Hellebore root 001.jpg", "niger — algemeen", type_="algemeen"),
    wiki("Christmas Rose (2023-12-28).JPG", "niger — algemeen", type_="algemeen"),
]},

"Heracleum sphondylium": {"photos": [
    wiki("Apiaceae - Heracleum sphondylium-6.JPG", "sphondylium — habitus", type_="habitus"),
    wiki("Heracleum sphondylium fruit.jpg", "sphondylium — vrucht", type_="vrucht"),
    wiki("Heracleum sphondylium (Thomé Bd.3 1905, BHL-81509, Tafel 451) clean, no-description.jpg", "sphondylium — algemeen", type_="algemeen"),
]},

"Hesperis matronalis": {"photos": [
    wiki("Dame's rocket2.jpg", "matronalis — algemeen", type_="algemeen"),
    wiki("Damerocket.jpg", "matronalis — algemeen", type_="algemeen"),
    wiki("Gardenology.org-IMG 2785 rbgs11jan.jpg", "matronalis — algemeen", type_="algemeen"),
]},

"Heuchera micrantha": {"photos": [
    wiki("Heuchera micrantha 1588.JPG", "micrantha — algemeen", type_="algemeen"),
    wiki("Heuchera micrantha 4940.JPG", "micrantha — algemeen", type_="algemeen"),
    wiki("Saxifraga oppositifolia upernavik 2006-06-22 2.jpg", "micrantha — algemeen", type_="algemeen"),
]},

"Hieracium aurantiacum": {"photos": [
    wiki("Yellow Hawkweed.jpg", "aurantiacum — algemeen", type_="algemeen"),
]},

"Hosta tardiana": {"photos": [
    wiki("Hosta plantaginea Funkia babkowata 02.jpg", "tardiana — habitus", type_="habitus"),
    wiki("Hosta sieboldiana (flower).jpg", "tardiana — bloeiwijze", type_="bloeiwijze"),
    wiki("Afbeelding-053-Hosta sieboldiana.tif", "tardiana — algemeen", type_="algemeen"),
]},

"Hyacinthus orientalis": {"photos": [
    wiki("Hyacinth flower.jpg", "orientalis — bloeiwijze", type_="bloeiwijze"),
    wiki("Hyacint - (Hyacinthus orientalis) - 2025.jpg", "orientalis — algemeen", type_="algemeen"),
    wiki("Hyacinths - floriade canberra.jpg", "orientalis — algemeen", type_="algemeen"),
]},

"Hydrangea anomala petiolaris": {"photos": [
    wiki("Hydrangea-08-10-08.JPG", "petiolaris — habitus", type_="habitus"),
    wiki("Hydrangea-flower.jpg", "petiolaris — bloeiwijze", type_="bloeiwijze"),
    wiki("Hydrangea Flower Color Based on Soil pH.jpg", "petiolaris — bloeiwijze", type_="bloeiwijze"),
]},

"Hydrangea macrophylla": {"photos": [
    wiki("Hortensia-1.jpg", "macrophylla — habitus", type_="habitus"),
    wiki("Bigleaf Hydrangea Hydrangea macrophylla 'Tokyo Delight' Pink 3008px.jpg", "macrophylla — blad", type_="blad"),
    wiki("(Natural) Hydrangea macrophylla, Iwafune, Isumi, Chiba, Japan 2.jpg", "macrophylla — algemeen", type_="algemeen"),
]},

"Hypericum 'Hidcote'": {"photos": [
    wiki("(MHNT) Hypericum perforatum flower and buttons.jpg", "'Hidcote' — bloeiwijze", type_="bloeiwijze"),
    wiki("Drie bloemknoppen van een Hertshooi (Hypericum). 10-07-2025 (d.j.b.).jpg", "'Hidcote' — bloeiwijze", type_="bloeiwijze"),
    wiki("Hypericum.flower.750pix.jpg", "'Hidcote' — bloeiwijze", type_="bloeiwijze"),
]},

"Hypericum perforatum": {"photos": [
    wiki("Hypericum perforatum plantlets.jpg", "perforatum — habitus", type_="habitus"),
    wiki("(MHNT) Hypericum perforatum flower and buttons.jpg", "perforatum — bloeiwijze", type_="bloeiwijze"),
    wiki("Bombus terrestris P1140477a.jpg", "perforatum — algemeen", type_="algemeen"),
]},

"Iberis sempervirens": {"photos": [
    wiki("Iberis sempervirens - Jardin des Plantes de Paris.JPG", "sempervirens — habitus", type_="habitus"),
    wiki("(MHNT) Iberis sempervirens with Ectophasia crassipennis male.jpg", "sempervirens — algemeen", type_="algemeen"),
    wiki("Iberis sempervirens 001.JPG", "sempervirens — algemeen", type_="algemeen"),
]},

"Ilex aquifolium": {"photos": [
    wiki("Hollyflowers.jpg", "aquifolium — bloeiwijze", type_="bloeiwijze"),
    wiki("2014-08-29 13 46 38 Variegated English Holly at the Pinelands Preservation Alliance headquarters in Southampton Township, New Jersey.JPG", "aquifolium — vrucht", type_="vrucht"),
    wiki("Ilex aquifolium berries rime.jpg", "aquifolium — vrucht", type_="vrucht"),
]},

"Impatiens walleriana": {"photos": [
    wiki("Impatiens walleriana.JPG", "walleriana — algemeen", type_="algemeen"),
    wiki("Impatienswalleriana.jpg", "walleriana — algemeen", type_="algemeen"),
    wiki("Starr 070906-8884 Impatiens walleriana.jpg", "walleriana — algemeen", type_="algemeen"),
]},

"Iris pseudacorus": {"photos": [
    wiki("Iris pseudacorus flower.jpg", "pseudacorus — bloeiwijze", type_="bloeiwijze"),
    wiki("Yellow Iris Iris pseudacorus Flower 1469px.jpg", "pseudacorus — bloeiwijze", type_="bloeiwijze"),
    wiki("Iris pseudacorus fruit.JPG", "pseudacorus — vrucht", type_="vrucht"),
]},

"Kerria japonica": {"photos": [
    wiki("Kerria japonica - flower.jpg", "japonica — bloeiwijze", type_="bloeiwijze"),
    wiki("Wild Kerria japonica with semi-double flowers in Fukushima (B).jpg", "japonica — bloeiwijze", type_="bloeiwijze"),
    wiki("Afbeelding-063-Kerria japonica.tif", "japonica — algemeen", type_="algemeen"),
]},

"Knautia arvensis": {"photos": [
    wiki("(MHNT) Knautia integrifolia - flower.jpg", "arvensis — bloeiwijze", type_="bloeiwijze"),
    wiki("Knautia arvensis flower (side view) - Keila.jpg", "arvensis — bloeiwijze", type_="bloeiwijze"),
    wiki("Acker-Witwenblume Knautia arvensis.jpg", "arvensis — algemeen", type_="algemeen"),
]},

"Laburnum x watereri": {"photos": [
    wiki("French Broom2.jpg", "watereri — algemeen", type_="algemeen"),
    wiki("Laburnum arbour by Temple Newsam House - geograph.org.uk - 305763.jpg", "watereri — algemeen", type_="algemeen"),
]},

"Lamiastrum galeobdolon": {"photos": [
    wiki("Lamium galeobdolon20160530 4923.jpg", "galeobdolon — algemeen", type_="algemeen"),
    wiki("Gele dovenetel (Lamium galeobdolon). 12-05-2021 (actm.).jpg", "galeobdolon — algemeen", type_="algemeen"),
    wiki("Lamiastrum galeobdolon kz01.jpg", "galeobdolon — algemeen", type_="algemeen"),
]},

"Lamium maculatum": {"photos": [
    wiki("Lamium maculatum 'Beacon Silver' Flowers.JPG", "maculatum — bloeiwijze", type_="bloeiwijze"),
    wiki("(Auch) Lamium maculatum (leaves).jpg", "maculatum — blad", type_="blad"),
    wiki("Gefleckte Taubnessel.jpg", "maculatum — algemeen", type_="algemeen"),
]},

"Lamium orvala": {"photos": [
    wiki("Horminum pyrenaicum - Saint-Hilaire.jpg", "orvala — algemeen", type_="algemeen"),
    wiki("Lamium orvala 11.jpg", "orvala — algemeen", type_="algemeen"),
]},

"Larix decidua": {"photos": [
    wiki("Larch planted on a scree slope.JPG", "decidua — habitus", type_="habitus"),
    wiki("LarixDeciduaFemaleFlower.jpg", "decidua — bloeiwijze", type_="bloeiwijze"),
    wiki("Larix decidua developing cone.JPG", "decidua — vrucht", type_="vrucht"),
]},

"Laurus nobilis": {"photos": [
    wiki("Starr-071024-0195-Laurus nobilis-leaves-Enchanting Floral Gardens of Kula-Maui (24867859296).jpg", "nobilis — blad", type_="blad"),
    wiki("Francesco Petrarca00.jpg", "nobilis — algemeen", type_="algemeen"),
    wiki("LaurusNobilisEssOil.png", "nobilis — algemeen", type_="algemeen"),
]},

"Lavandula angustifolia": {"photos": [
    wiki("Lavandula angustifolia - Köhler–s Medizinal-Pflanzen-087.jpg", "angustifolia — habitus", type_="habitus"),
    wiki("Lavande off FR 2012.jpg", "angustifolia — algemeen", type_="algemeen"),
    wiki("Lavandula angustifolia lavender Lavendel 01.jpg", "angustifolia — algemeen", type_="algemeen"),
]},

"Leucanthemum hybriden": {"photos": [
    wiki("Leucanthemum August 2012-1.jpg", "hybriden — habitus", type_="habitus"),
    wiki("A leucanthemum flower.jpg", "hybriden — bloeiwijze", type_="bloeiwijze"),
    wiki("Leucanthemum 'Crazy Daisy' 01.jpg", "hybriden — algemeen", type_="algemeen"),
]},

"Leucanthemum vulgare": {"photos": [
    wiki("Leucanthemum vulgare 'Filigran' Flower 2200px.jpg", "vulgare — bloeiwijze", type_="bloeiwijze"),
    wiki("024 065 Ile Madeleine.jpg", "vulgare — algemeen", type_="algemeen"),
    wiki("Leucanthemum vulgare 08.jpg", "vulgare — algemeen", type_="algemeen"),
]},

"Leycesteria formosa": {"photos": [
    wiki("Leycesteria-formosa-flowers.jpg", "formosa — bloeiwijze", type_="bloeiwijze"),
    wiki("Leycesteria formosa flowers.jpg", "formosa — bloeiwijze", type_="bloeiwijze"),
    wiki("Leycesteria formosa berries close-up.jpg", "formosa — vrucht", type_="vrucht"),
]},

"Ligustrum vulgare": {"photos": [
    wiki("Ligustrum vulgare fleurs0a.jpg", "vulgare — bloeiwijze", type_="bloeiwijze"),
    wiki("- Ligustrum vulgare - Berries -.jpg", "vulgare — vrucht", type_="vrucht"),
    wiki("Schurenbachhalde 10 ies.jpg", "vulgare — algemeen", type_="algemeen"),
]},

"Linaria purpurea": {"photos": [
    wiki("Linaria purpurea (Purple Toadflax) - Flickr - gailhampshire.jpg", "purpurea — algemeen", type_="algemeen"),
    wiki("Linaria purpurea 1.jpg", "purpurea — algemeen", type_="algemeen"),
]},

"Linaria vulgaris": {"photos": [
    wiki("Linaria vulgaris flowers - Keila.jpg", "vulgaris — bloeiwijze", type_="bloeiwijze"),
    wiki("Bombus hortorum - Linaria vulgaris - Valingu.jpg", "vulgaris — algemeen", type_="algemeen"),
    wiki("Common Toadflax (Linaria vulgaris) - Oslo, Norway 2020-09-16 (01).jpg", "vulgaris — algemeen", type_="algemeen"),
]},

"Lonicera nitida": {"photos": [
    wiki("Lonicera nitida flower.jpg", "nitida — bloeiwijze", type_="bloeiwijze"),
    wiki("Lonicera nitida aurea after pruning.JPG", "nitida — algemeen", type_="algemeen"),
]},

"Lonicera periclymenum": {"photos": [
    wiki("European honeysuckle 800.jpg", "periclymenum — algemeen", type_="algemeen"),
    wiki("Woodbine on Willow - Honeysuckle.JPG", "periclymenum — algemeen", type_="algemeen"),
]},

"Lupinus hybriden": {"photos": [
    wiki("Bluebonnet-8100.jpg", "hybriden — habitus", type_="habitus"),
    wiki("Mountaintop Lupin overlooking Raspberry Strait, Alaska 2009 114.jpg", "hybriden — vrucht", type_="vrucht"),
    wiki("Lupin Leaf.jpg", "hybriden — blad", type_="blad"),
]},

"Lythrum salicaria": {"photos": [
    wiki("Bombus sylvarum - Lythrum salicaria - Keila.jpg", "salicaria — algemeen", type_="algemeen"),
    wiki("Cooper Marsh - Purple-loosestrife.jpg", "salicaria — algemeen", type_="algemeen"),
    wiki("LythrumSalicariaBig.jpg", "salicaria — algemeen", type_="algemeen"),
]},

"Magnolia stellata": {"photos": [
    wiki("Magnolia stellata tree.jpg", "stellata — habitus", type_="habitus"),
    wiki("Magnoliaceae - Magnolia stellata rosea-002.JPG", "stellata — habitus", type_="habitus"),
    wiki("Flower 00068a.jpg", "stellata — bloeiwijze", type_="bloeiwijze"),
]},

"Magnolia x soulangeana": {"photos": [
    wiki("Magnolia x soulangeana tree.jpg", "soulangeana — habitus", type_="habitus"),
    wiki("Blüte der Tulpemmagniolie.jpg", "soulangeana — bloeiwijze", type_="bloeiwijze"),
    wiki("Magnolia x soulangeana flower.jpg", "soulangeana — bloeiwijze", type_="bloeiwijze"),
]},

"Mahonia aquifolium": {"photos": [
    wiki("Fruits of Mahonia lomariifolia, Luther Burbank Home and Gardens.jpg", "aquifolium — vrucht", type_="vrucht"),
    wiki("Holly1web.jpg", "aquifolium — algemeen", type_="algemeen"),
    wiki("Mahonia Golden Abundance 038.jpg", "aquifolium — algemeen", type_="algemeen"),
]},

"Malva sylvestris": {"photos": [
    wiki("Mallow January 2008-1.jpg", "sylvestris — habitus", type_="habitus"),
    wiki("Malva sylvestris - Köhler–s Medizinal-Pflanzen-222.jpg", "sylvestris — habitus", type_="habitus"),
    wiki("Common mallow closeup.jpg", "sylvestris — algemeen", type_="algemeen"),
]},

"Mandevilla": {"photos": [
    wiki("Mandevilla cv Best Red1.jpg", "Mandevilla — vrucht", type_="vrucht"),
    wiki("Mandevilla sanderi red 1.jpg", "Mandevilla — algemeen", type_="algemeen"),
    wiki("PinkMandevilla.jpg", "Mandevilla — algemeen", type_="algemeen"),
]},

"Matricaria chamomilla": {"photos": [
    wiki("Matricaria February 2008-1.jpg", "chamomilla — habitus", type_="habitus"),
    wiki("Fiore Asteraceae 04.png", "chamomilla — algemeen", type_="algemeen"),
    wiki("GermanChamomileEssOil.png", "chamomilla — algemeen", type_="algemeen"),
]},

"Mentha x piperita": {"photos": [
    wiki("Spearmint flower.jpg", "piperita — bloeiwijze", type_="bloeiwijze"),
    wiki("Mint-leaves-2007.jpg", "piperita — blad", type_="blad"),
    wiki("CSA-Chocolate-Mint.jpg", "piperita — algemeen", type_="algemeen"),
]},

"Molinia caerulea": {"photos": [
    wiki("Molinia-caerulea-habitat.JPG", "caerulea — habitus", type_="habitus"),
    wiki("Molinia caerulea habitus.jpeg", "caerulea — habitus", type_="habitus"),
    wiki("Claviceps microcephala.jpg", "caerulea — algemeen", type_="algemeen"),
]},

"Muscari armeniacum": {"photos": [
    wiki("Muscari armeniacum 'Peppermint' fruits.jpg", "armeniacum — vrucht", type_="vrucht"),
    wiki("Grape Hyacinth - Muscari armeniacum - Traubenhyazinthe - 01.jpg", "armeniacum — algemeen", type_="algemeen"),
    wiki("Muscari armeniacum, Jardín Botánico de Múnich, Alemania, 2013-05-04, DD 01.jpg", "armeniacum — algemeen", type_="algemeen"),
]},

"Myosotis scorpioides": {"photos": [
    wiki("Myosotis scorpioides PID1155-3.jpg", "scorpioides — habitus", type_="habitus"),
    wiki("Anna Munthe-Norstedt Still life with irises and forget-me-nots.jpg", "scorpioides — algemeen", type_="algemeen"),
    wiki("Cranach the Elder Girl with forget-me-nots (detail) 01.jpg", "scorpioides — algemeen", type_="algemeen"),
]},

"Narcissus": {"photos": [
    wiki("Narcissus flowers.jpg", "Narcissus — bloeiwijze", type_="bloeiwijze"),
    wiki("Narcissus 'Ice Follies' 02.jpg", "Narcissus — algemeen", type_="algemeen"),
    wiki("Narcissus-tazetta-2014-Zachi-Evenor.jpg", "Narcissus — algemeen", type_="algemeen"),
]},

"Nepeta faassenii": {"photos": [
    wiki("(MHNT) Nepeta × faassenii - flowers.jpg", "faassenii — bloeiwijze", type_="bloeiwijze"),
    wiki("Catnip-blossom.jpg", "faassenii — bloeiwijze", type_="bloeiwijze"),
    wiki("Nepeta curviflora 1.jpg", "faassenii — algemeen", type_="algemeen"),
]},

"Nymphaea alba": {"photos": [
    wiki("20150623Nymphaea alba2.jpg", "alba — algemeen", type_="algemeen"),
    wiki("2016 Kwiat grzybieni białych 2.jpg", "alba — algemeen", type_="algemeen"),
    wiki("Eriksbergnäckrosor.jpg", "alba — algemeen", type_="algemeen"),
]},

"Olea europaea": {"photos": [
    wiki("Olive-tree-fruit-august-0.jpg", "europaea — vrucht", type_="vrucht"),
]},

"Origanum vulgare": {"photos": [
    wiki("Gardenology.org-IMG 3007 rbgs11jan.jpg", "vulgare — algemeen", type_="algemeen"),
    wiki("Origanum-vulgare.JPG", "vulgare — algemeen", type_="algemeen"),
]},

"Osteospermum cultivars": {"photos": [
    wiki("Osteospermum spinosum var. spinosum 1DS-II 1-9738.jpg", "cultivars — habitus", type_="habitus"),
    wiki("Osteospermum Flower Power Spider Purple 2134px.jpg", "cultivars — bloeiwijze", type_="bloeiwijze"),
    wiki("Osteospermum flower.jpg", "cultivars — bloeiwijze", type_="bloeiwijze"),
]},

"Pachysandra terminalis": {"photos": [
    wiki("Pachysandra terminalis0.jpg", "terminalis — algemeen", type_="algemeen"),
]},

"Paeonia": {"photos": [
    wiki("Paeonia suffruticosa white070503.jpg", "Paeonia — algemeen", type_="algemeen"),
    wiki("Paeonia Detail SK.jpg", "Paeonia — algemeen", type_="algemeen"),
    wiki("Paeonia suffruticosa Yatsuka JdP.jpg", "Paeonia — algemeen", type_="algemeen"),
]},

"Papaver rhoeas": {"photos": [
    wiki("Koeh-101.jpg", "rhoeas — habitus", type_="habitus"),
    wiki("Papaver rhoeas - Köhler–s Medizinal-Pflanzen-101.jpg", "rhoeas — habitus", type_="habitus"),
    wiki("00MoinaMichael.jpg", "rhoeas — algemeen", type_="algemeen"),
]},

"Parthenocissus tricuspidata": {"photos": [
    wiki("Klättervildvin (Parthenocissus tricuspidata) Ystad-2015.jpg", "tricuspidata — habitus", type_="habitus"),
    wiki("20230730 Parthenocissus tricuspidata Winobluszcz trójklapowy Panewniki Poland 01.jpg", "tricuspidata — algemeen", type_="algemeen"),
    wiki("Cambridge - Japanese Creeper - 1308.jpg", "tricuspidata — algemeen", type_="algemeen"),
]},

"Pelargonium zonale": {"photos": [
    wiki("Pelargonium colors.jpg", "zonale — algemeen", type_="algemeen"),
    wiki("Pelargonium zonale in wild.jpg", "zonale — algemeen", type_="algemeen"),
    wiki("Pelargonium zonale umbel.jpg", "zonale — algemeen", type_="algemeen"),
]},

"Pennisetum alopecuroides": {"photos": [
    wiki("Pennisetum alopecuroides (Lampenpoetsersgras) 02.JPG", "alopecuroides — algemeen", type_="algemeen"),
    wiki("Pennisetum alopecuroides (Lampenpoetsersgras) 01.JPG", "alopecuroides — algemeen", type_="algemeen"),
    wiki("Lampenputzergras im Schrebergarten.jpg", "alopecuroides — algemeen", type_="algemeen"),
]},

"Persicaria affinis": {"photos": [
    wiki("Persicaria minor flower and leaves.jpg", "affinis — blad", type_="blad"),
    wiki("(MHNT) Persicaria microcephala Inflorescence - Les Martels, Giroussens Tarn.jpg", "affinis — algemeen", type_="algemeen"),
    wiki("Leiden University Library - Seikei Zusetsu vol. 25, page 010 - 大毛蓼 - Persicaria orientalis (L.) Spach, 1804.jpg", "affinis — algemeen", type_="algemeen"),
]},

"Persicaria maculosa": {"photos": [
    wiki("2015.09.05 12.26.43 DSC00301 - Flickr - andrey zharkikh crop.jpg", "maculosa — algemeen", type_="algemeen"),
    wiki("Ocreae of a Persicaria maculosa 2006-aug-10 Gothenburg Sweden.jpg", "maculosa — algemeen", type_="algemeen"),
    wiki("Persicaria maculosa.jpg", "maculosa — algemeen", type_="algemeen"),
]},

"Petasites hybridus": {"photos": [
    wiki("Petasites hybridus leaf.JPG", "hybridus — blad", type_="blad"),
    wiki("Pestskråp - Butterbur - (Petasites hybridus) - Ystad - 2025.jpg", "hybridus — algemeen", type_="algemeen"),
    wiki("Petasites hybridus inflorescence - Keila.jpg", "hybridus — algemeen", type_="algemeen"),
]},

"Petroselinum crispum": {"photos": [
    wiki("Petroselinum segetum 1.jpg", "crispum — algemeen", type_="algemeen"),
    wiki("QALace2675.JPG", "crispum — algemeen", type_="algemeen"),
]},

"Petunia surfinia cultivars": {"photos": [
    wiki("Petunia Flowers (2).jpg", "cultivars — bloeiwijze", type_="bloeiwijze"),
    wiki("Petunia flower growing in Boothbay Maine 2024.jpg", "cultivars — bloeiwijze", type_="bloeiwijze"),
    wiki("Starry night petunia flower in Porto Alegre - Brazil.jpg", "cultivars — bloeiwijze", type_="bloeiwijze"),
]},

"Phlox subulata": {"photos": [
    wiki("Flower (215167183).jpeg", "subulata — bloeiwijze", type_="bloeiwijze"),
    wiki("Sakura and Moss Pink - 桜(さくら)と芝桜(しばざくら).jpg", "subulata — algemeen", type_="algemeen"),
    wiki("Shibazakura.JPG", "subulata — algemeen", type_="algemeen"),
]},

"Picea abies": {"photos": [
    wiki("Picea abies - Köhler–s Medizinal-Pflanzen-105.jpg", "abies — habitus", type_="habitus"),
    wiki("Trafalgar Square Christmas tree8.jpg", "abies — habitus", type_="habitus"),
    wiki("Picea abies cone.jpg", "abies — vrucht", type_="vrucht"),
]},

"Pinus mugo mughus": {"photos": [
    wiki("Pinus mugo cone 02.jpg", "mughus — vrucht", type_="vrucht"),
    wiki("Pinus mugo subsp. uncinata MHNT.BOT.2005.0.976.jpg", "mughus — algemeen", type_="algemeen"),
    wiki("Bergkiefer (Pinus mugo).JPG", "mughus — algemeen", type_="algemeen"),
]},

"Pinus sylvestris": {"photos": [
    wiki("Pinar Sierra de Guadarrama 2005-09-13.JPG", "sylvestris — habitus", type_="habitus"),
    wiki("Pine log cross-sections, Teutendorf, 2016-09-17.jpg", "sylvestris — habitus", type_="habitus"),
    wiki("Pinus sylvestris wood ray section 1 beentree.jpg", "sylvestris — habitus", type_="habitus"),
]},

"Plantago lanceolata": {"photos": [
    wiki("Galled head of a Plantain.JPG", "lanceolata — habitus", type_="habitus"),
    wiki("Plantago lanceolata - Kulna.jpg", "lanceolata — habitus", type_="habitus"),
    wiki("Plantago lanceolata P6200323 箆大葉子、ヘラオオバコ.jpg", "lanceolata — habitus", type_="habitus"),
]},

"Plantago major": {"photos": [
    wiki("Grote weegbree bloeiwijze Plantago major subsp. major.jpg", "major — habitus", type_="habitus"),
    wiki("Plantago major 05 ies.jpg", "major — habitus", type_="habitus"),
    wiki("Purple Plantago major.JPG", "major — habitus", type_="habitus"),
]},

"Platanus x hispanica": {"photos": [
    wiki("Plane Tree bark at Tayac, Dordogne.jpg", "hispanica — habitus", type_="habitus"),
    wiki("Plane tree fruit 20180707 092951.jpg", "hispanica — vrucht", type_="vrucht"),
    wiki("Platanus orientalis fruits, Thasos.jpg", "hispanica — vrucht", type_="vrucht"),
]},

"Poa annua": {"photos": [
    wiki("Poa.annua.2.jpg", "annua — algemeen", type_="algemeen"),
    wiki("Poa.annua.jpg", "annua — algemeen", type_="algemeen"),
    wiki("Poa annua.jpeg", "annua — algemeen", type_="algemeen"),
]},

"Polygonum aviculare": {"photos": [
    wiki("Polygonum aviculare 4.JPG", "aviculare — algemeen", type_="algemeen"),
]},

"Populus alba": {"photos": [
    wiki("Lisboa June 2014-10.jpg", "alba — habitus", type_="habitus"),
    wiki("Populus alba leaf.jpg", "alba — blad", type_="blad"),
    wiki("Poplar-lined road, Khotan.jpg", "alba — algemeen", type_="algemeen"),
]},

"Populus tremula": {"photos": [
    wiki("Asp (Populus tremula) - Ystad-2025.jpg", "tremula — habitus", type_="habitus"),
    wiki("Aspfrön - Aspen seeds - 2025.jpg", "tremula — vrucht", type_="vrucht"),
    wiki("Aspen-leaves.jpg", "tremula — blad", type_="blad"),
]},

"Prunella vulgaris": {"photos": [
    wiki("Kleine Braunelle, Blüte.jpg", "vulgaris — bloeiwijze", type_="bloeiwijze"),
    wiki("Prunella vulgaris-flowers.jpg", "vulgaris — bloeiwijze", type_="bloeiwijze"),
    wiki("Common self-heal (Prunella vulgaris) -- leaf.JPG", "vulgaris — blad", type_="blad"),
]},

"Prunus cerasifera": {"photos": [
    wiki("Wildpflaume Althof-2.jpg", "cerasifera — habitus", type_="habitus"),
    wiki("01 Prunus cerasifera.jpg", "cerasifera — algemeen", type_="algemeen"),
    wiki("Cherry plums.jpg", "cerasifera — algemeen", type_="algemeen"),
]},

"Prunus padus": {"photos": [
    wiki("Apis mellifera - Prunus padus - Keila.jpg", "padus — algemeen", type_="algemeen"),
    wiki("Bird cherry pie. Siberia.jpg", "padus — algemeen", type_="algemeen"),
    wiki("Prunus padus Rauma.jpg", "padus — algemeen", type_="algemeen"),
]},

"Prunus spinosa": {"photos": [
    wiki("Husband and wife trees - Blackthorn.JPG", "spinosa — habitus", type_="habitus"),
    wiki("Blackthorn in blossom.jpg", "spinosa — bloeiwijze", type_="bloeiwijze"),
    wiki("Closeup of blackthorn aka sloe aka prunus spinosa sweden 20050924.jpg", "spinosa — algemeen", type_="algemeen"),
]},

"Pteridium aquilinum": {"photos": [
    wiki("Adelaarsvaren planten Pteridium aquilinum.jpg", "aquilinum — habitus", type_="habitus"),
    wiki("Pteridium aquilinum (northern bracken fern) 2024-06-25.jpg", "aquilinum — habitus", type_="habitus"),
    wiki("Dried Eastern brakenfern.jpg", "aquilinum — algemeen", type_="algemeen"),
]},

"Pulmonaria officinalis": {"photos": [
    wiki("Boraginaceae - Pulmonaria officinalis-1.JPG", "officinalis — habitus", type_="habitus"),
    wiki("Boraginaceae - Pulmonaria officinalis-2.JPG", "officinalis — habitus", type_="habitus"),
    wiki("Boraginaceae - Pulmonaria officinalis.JPG", "officinalis — algemeen", type_="algemeen"),
]},

"Pulmonaria saccharata": {"photos": [
    wiki("Pulmonaria saccharata A.jpg", "saccharata — algemeen", type_="algemeen"),
]},

"Pulsatilla vulgaris": {"photos": [
    wiki("Pasque Flower (Pulsatilla vulgaris) (17022184800).jpg", "vulgaris — bloeiwijze", type_="bloeiwijze"),
    wiki("Anemone Pulsatilla L. in Wolf Lake, Indiana.jpg", "vulgaris — algemeen", type_="algemeen"),
    wiki("Anemone pulsatilla subsp. grandis ÖBG Bayreuth.jpg", "vulgaris — algemeen", type_="algemeen"),
]},

"Quercus robur": {"photos": [
    wiki("Baginton oak tree july06.JPG", "robur — habitus", type_="habitus"),
    wiki("Quercus robur flowers kz01.jpg", "robur — bloeiwijze", type_="bloeiwijze"),
    wiki("Quercus robur acorns in Tuntorp 1.jpg", "robur — vrucht", type_="vrucht"),
]},

"Ranunculus acris": {"photos": [
    wiki("Illustration Ranunculus acris0.jpg", "acris — algemeen", type_="algemeen"),
]},

"Ranunculus repens": {"photos": [
    wiki("Creeping butercup close 800.jpg", "repens — algemeen", type_="algemeen"),
]},

"Rhamnus cathartica": {"photos": [
    wiki("Buckthorn cutting board.JPG", "cathartica — algemeen", type_="algemeen"),
    wiki("Illustration of Rhamnus catharticus 63-cropped.png", "cathartica — algemeen", type_="algemeen"),
    wiki("Rhamnus cathartica (8023754928).jpg", "cathartica — algemeen", type_="algemeen"),
]},

"Rhododendron ponticum": {"photos": [
    wiki("Rhododendron-by-eiffel-public-domain-20040617.jpg", "ponticum — habitus", type_="habitus"),
    wiki("(MHNT) Rhododendron ponticum - flower bud.jpg", "ponticum — bloeiwijze", type_="bloeiwijze"),
    wiki("Rhododendron ponticum 2.jpg", "ponticum — algemeen", type_="algemeen"),
]},

"Ribes sanguineum": {"photos": [
    wiki("Pink-flowering current.JPG", "sanguineum — bloeiwijze", type_="bloeiwijze"),
    wiki("Distribution of Ribes Sanguineum.png", "sanguineum — vrucht", type_="vrucht"),
    wiki("Fruit de Ribes sanguineum.jpg", "sanguineum — vrucht", type_="vrucht"),
]},

"Robinia pseudoacacia": {"photos": [
    wiki("Robinia pseudoacacia seeds.jpg", "pseudoacacia — vrucht", type_="vrucht"),
    wiki("Black Locust Leaf Close Up.jpg", "pseudoacacia — blad", type_="blad"),
    wiki("20130528Robinia pseudoacacia Hockenheim4.jpg", "pseudoacacia — algemeen", type_="algemeen"),
]},

"Rosa arvensis": {"photos": [
    wiki("Rosa arvensis (Liege-Rose) IMG 1378.JPG", "arvensis — algemeen", type_="algemeen"),
    wiki("Rosa arvensis (Liege-Rose) IMG 30074.JPG", "arvensis — algemeen", type_="algemeen"),
]},

"Rosa canina": {"photos": [
    wiki("Aestivation.png", "canina — algemeen", type_="algemeen"),
    wiki("Divlja ruza cvijet 270508.jpg", "canina — algemeen", type_="algemeen"),
    wiki("Hildesheim Rosenstock.jpg", "canina — algemeen", type_="algemeen"),
]},

"Rosa glauca": {"photos": [
    wiki("Rosa glauca leaves img 1851.jpg", "glauca — blad", type_="blad"),
    wiki("Rosa glauca img 2050.jpg", "glauca — algemeen", type_="algemeen"),
    wiki("Rosa glauca img 2726.jpg", "glauca — algemeen", type_="algemeen"),
]},

"Rosa nitida": {"photos": [
    wiki("Rosa nitida.jpg", "nitida — algemeen", type_="algemeen"),
]},

"Rosa rugosa": {"photos": [
    wiki("Rosa rugosa plant (08).jpg", "rugosa — habitus", type_="habitus"),
    wiki("Rugosa Rose (Rosa rugosa) - Oslo, Norway 2020-08-04.jpg", "rugosa — habitus", type_="habitus"),
    wiki("Rosa Rugosa With Fruit On Shoreline.jpg", "rugosa — vrucht", type_="vrucht"),
]},

"Rumex acetosa": {"photos": [
    wiki("Rumex-obtusifolius-foliage.JPG", "acetosa — blad", type_="blad"),
    wiki("RumexCrispusValven.jpg", "acetosa — algemeen", type_="algemeen"),
    wiki("Rumex X patientia Sturm55.jpg", "acetosa — algemeen", type_="algemeen"),
]},

"Rumex obtusifolius": {"photos": [
    wiki("Rumex-obtusifolius-foliage.JPG", "obtusifolius — blad", type_="blad"),
    wiki("Rumex obtusifolius Sturm48.jpg", "obtusifolius — algemeen", type_="algemeen"),
]},

"Salix alba": {"photos": [
    wiki("Salix alba leaves.jpg", "alba — blad", type_="blad"),
    wiki("Salix alba 020.jpg", "alba — algemeen", type_="algemeen"),
    wiki("Whitewillowtincture.jpg", "alba — algemeen", type_="algemeen"),
]},

"Salix aurita": {"photos": [
    wiki("Salix-catkins.JPG", "aurita — bloeiwijze", type_="bloeiwijze"),
    wiki("Salix aurita 007.jpg", "aurita — algemeen", type_="algemeen"),
    wiki("Salix aurita Sturm26.jpg", "aurita — algemeen", type_="algemeen"),
]},

"Salix babylonica": {"photos": [
    wiki("SalixBabylonicaLeaf.jpg", "babylonica — blad", type_="blad"),
    wiki("Château de Chenonceau - jardin Russell-Page (01).jpg", "babylonica — algemeen", type_="algemeen"),
    wiki("Claude Monet, Weeping Willow.JPG", "babylonica — algemeen", type_="algemeen"),
]},

"Salix x sepulcralis": {"photos": [
    wiki("Salix x sepulcralis - leafs (aka).jpg", "sepulcralis — blad", type_="blad"),
    wiki("Salix x sepulcralis (Chrysocoma) - Treurwilg uit 1949 - Statensingel - Blijdorp - Noord - Rotterdam - bijzondere bomencollectie - 2024 - pic1 - spring.jpg", "sepulcralis — algemeen", type_="algemeen"),
    wiki("Trauerweide Salix x sepulcralis.jpg", "sepulcralis — algemeen", type_="algemeen"),
]},

"Salvia nemorosa": {"photos": [
    wiki("Nemorosin.png", "nemorosa — algemeen", type_="algemeen"),
    wiki("Salvia nemorosa-IMG 3624.jpg", "nemorosa — algemeen", type_="algemeen"),
    wiki("Ковила, Тарутинський степ, Україна.jpg", "nemorosa — algemeen", type_="algemeen"),
]},

"Sambucus nigra": {"photos": [
    wiki("\"Godfrey's Extract of Elder-Flowers\" ad - Woman's Exhibition, 1900, Earl's Court, London, S.W. - official fine art, historical and general catalogue (IA gri 33125013839424) (page 7 crop).jpg", "nigra — bloeiwijze", type_="bloeiwijze"),
    wiki("Flowers Black Elder.jpg", "nigra — bloeiwijze", type_="bloeiwijze"),
    wiki("Elderberry-jam.JPG", "nigra — vrucht", type_="vrucht"),
]},

"Sanguisorba officinalis": {"photos": [
    wiki("Addisonia - colored illustrations and popular descriptions of plants (1916-(1964)) (16585422840).jpg", "officinalis — habitus", type_="habitus"),
    wiki("Sanguisorba officinalisseeds.jpg", "officinalis — vrucht", type_="vrucht"),
    wiki("Sanguisorba officinalis.jpg", "officinalis — algemeen", type_="algemeen"),
]},

"Saponaria officinalis": {"photos": [
    wiki("Saponaria-officinalis-flower.jpg", "officinalis — bloeiwijze", type_="bloeiwijze"),
    wiki("Saponaria officinalis 018.jpg", "officinalis — algemeen", type_="algemeen"),
    wiki("Saponaria officinalis MHNT.BOT.40.40.jpg", "officinalis — algemeen", type_="algemeen"),
]},

"Scilla siberica": {"photos": [
    wiki("Scilla siberica flower - Keila.jpg", "siberica — bloeiwijze", type_="bloeiwijze"),
    wiki("20210430 SiberianSquill-SQ.jpg", "siberica — algemeen", type_="algemeen"),
    wiki("20210430 SiberianSquill-SQ1.jpg", "siberica — algemeen", type_="algemeen"),
]},

"Sedum acre": {"photos": [
    wiki("Sedum acre 009.jpg", "acre — algemeen", type_="algemeen"),
    wiki("Sedum acre single - Niitvälja.jpg", "acre — algemeen", type_="algemeen"),
]},

"Sedum spectabile": {"photos": [
    wiki("EB1911 Sedum acre diagram.jpg", "spectabile — algemeen", type_="algemeen"),
    wiki("Mauerpfeffer Sedum acre.jpg", "spectabile — algemeen", type_="algemeen"),
    wiki("Sedum acre single - Niitvälja.jpg", "spectabile — algemeen", type_="algemeen"),
]},

"Senecio vulgaris": {"photos": [
    wiki("Common Groundsel-first fruits.jpg", "vulgaris — vrucht", type_="vrucht"),
    wiki("Cinnabar moth caterpillar 01.jpg", "vulgaris — algemeen", type_="algemeen"),
    wiki("Common groundsel (30809).jpg", "vulgaris — algemeen", type_="algemeen"),
]},

"Silene flos-cuculi": {"photos": [
    wiki("Silene flos-cuculi flower - Niitvälja.jpg", "flos-cuculi — bloeiwijze", type_="bloeiwijze"),
    wiki("Käokannid.JPG", "flos-cuculi — algemeen", type_="algemeen"),
    wiki("Lychnis flos-cuculi L. in Botanica in originali.jpg", "flos-cuculi — algemeen", type_="algemeen"),
]},

"Skimmia japonica": {"photos": [
    wiki("Dads garden-0971 - Flickr - Ragnhild & Neil Crawford.jpg", "japonica — algemeen", type_="algemeen"),
    wiki("Skimmia japonica Rubella.jpg", "japonica — algemeen", type_="algemeen"),
    wiki("Skimmia reevesiana1.jpg", "japonica — algemeen", type_="algemeen"),
]},

"Solanum nigrum": {"photos": [
    wiki("Black Nightshade - Flickr - treegrow (2).jpg", "nigrum — habitus", type_="habitus"),
    wiki("Solanum nigrum habit.jpg", "nigrum — habitus", type_="habitus"),
    wiki("Solanum nigrum flower.jpg", "nigrum — bloeiwijze", type_="bloeiwijze"),
]},

"Solidago": {"photos": [
    wiki("Solidago virgaurea var. leiocarpa 02-2.jpg", "Solidago — habitus", type_="habitus"),
    wiki("Solidago simplex ssp. randii var. ontarioensis fruit.jpg", "Solidago — vrucht", type_="vrucht"),
    wiki("Bombus cryptarum - Solidago virgaurea - Keila2.jpg", "Solidago — algemeen", type_="algemeen"),
]},

"Sonchus arvensis": {"photos": [
    wiki("Illustration Sonchus arvensis0.jpg", "arvensis — algemeen", type_="algemeen"),
    wiki("Sonchus arvensis.JPG", "arvensis — algemeen", type_="algemeen"),
    wiki("Sonchus arvensis20090912 303.jpg", "arvensis — algemeen", type_="algemeen"),
]},

"Sorbus aucuparia": {"photos": [
    wiki("2020 year. Herbarium. Sorbus aucuparia. img-036.jpg", "aucuparia — habitus", type_="habitus"),
    wiki("Rowan tree 20081002b.jpg", "aucuparia — habitus", type_="habitus"),
    wiki("Young trees of Sorbus aucuparia.jpg", "aucuparia — habitus", type_="habitus"),
]},

"Spiraea nipponica": {"photos": [
    wiki("Spiraea nipponica 'Gerlve's Rainbow' 01.JPG", "nipponica — algemeen", type_="algemeen"),
    wiki("Spiraea nipponica 'Snowmound', bloeiwyses, Manie van der Schijff BT, a.jpg", "nipponica — algemeen", type_="algemeen"),
    wiki("Spiraea nipponica 'Snowmound', bloeiwyses, Manie van der Schijff BT, b.jpg", "nipponica — algemeen", type_="algemeen"),
]},

"Stachys byzantina": {"photos": [
    wiki("Lamb's-ears Betony Stachys byzantina Plant 2800px.jpg", "byzantina — habitus", type_="habitus"),
    wiki("Lamb's Ear Stachys byzantina Leaf 2448px.jpg", "byzantina — blad", type_="blad"),
    wiki("Lamb's Ear Stachys byzantina Leaves 3264px.JPG", "byzantina — blad", type_="blad"),
]},

"Stellaria holostea": {"photos": [
    wiki("Greater Stitchwort close 800.jpg", "holostea — algemeen", type_="algemeen"),
    wiki("Lesser Stitchwort close 800.jpg", "holostea — algemeen", type_="algemeen"),
]},

"Symphoricarpos chenaultii": {"photos": [
    wiki("Coral berries in prairie.JPG", "chenaultii — vrucht", type_="vrucht"),
    wiki("Coralberries.JPG", "chenaultii — vrucht", type_="vrucht"),
    wiki("Coralberry.jpg", "chenaultii — vrucht", type_="vrucht"),
]},

"Symphytum officinale": {"photos": [
    wiki("Symphytum officinale 01.jpg", "officinale — algemeen", type_="algemeen"),
    wiki("Symphytum officinale 2 RF.jpg", "officinale — algemeen", type_="algemeen"),
]},

"Tagetes": {"photos": [
    wiki("Newly grown marigold (tagetes) plants.jpg", "Tagetes — habitus", type_="habitus"),
    wiki("Marigold flowers. Eastern Siberia.png", "Tagetes — bloeiwijze", type_="bloeiwijze"),
    wiki("Tagetes-Marigold-Flower 08.jpg", "Tagetes — bloeiwijze", type_="bloeiwijze"),
]},

"Tanacetum vulgare": {"photos": [
    wiki("Tanacetum cinerariifolium - Köhler–s Medizinal-Pflanzen-269.jpg", "vulgare — habitus", type_="habitus"),
    wiki("Tanacetum coccineum - Köhler–s Medizinal-Pflanzen-037.jpg", "vulgare — habitus", type_="habitus"),
    wiki("Chrysanthemum haradjanii 1.jpg", "vulgare — algemeen", type_="algemeen"),
]},

"Taraxacum officinale": {"photos": [
    wiki("Taraxacum officinale - Köhler–s Medizinal-Pflanzen-135.jpg", "officinale — habitus", type_="habitus"),
    wiki("Taraxacum officinale PID1200-1.jpg", "officinale — habitus", type_="habitus"),
    wiki("Dandelion flower head (2008-05-04 pic02).jpg", "officinale — bloeiwijze", type_="bloeiwijze"),
]},

"Taxus baccata": {"photos": [
    wiki("Farnborough, St Giles the Abbot, yew tree and bench in the churchyard - geograph.org.uk - 3394871.jpg", "baccata — habitus", type_="habitus"),
    wiki("20150624Sorbus aucuparia1.jpg", "baccata — algemeen", type_="algemeen"),
    wiki("Alte Eibe in Balderschwang, Blick von Nord-Westen.jpg", "baccata — algemeen", type_="algemeen"),
]},

"Thuja occidentalis": {"photos": [
    wiki("Northern Whitecedar (Thuja occidentalis) - Algonquin Provincial Park, Ontario 2019-09-20.jpg", "occidentalis — habitus", type_="habitus"),
    wiki("Thuja occidentalis foliage Wisconsin.jpg", "occidentalis — blad", type_="blad"),
    wiki("Poland. Warsaw. Powsin. Botanical Garden 097.jpg", "occidentalis — algemeen", type_="algemeen"),
]},

"Thymus praecox": {"photos": [
    wiki("Plant in Lonsoraefi area, Iceland.jpg", "praecox — habitus", type_="habitus"),
    wiki("Thymus praecox - Iceland - 2007-07-05.jpg", "praecox — habitus", type_="habitus"),
    wiki("Thymus praecox.JPG", "praecox — algemeen", type_="algemeen"),
]},

"Thymus pulegioides": {"photos": [
    wiki("Breitblättrige Thymian (Thymus pulegioides)-1.jpg", "pulegioides — habitus", type_="habitus"),
]},

"Tilia x europaea": {"photos": [
    wiki("Tilia x europea-1.JPG", "europaea — habitus", type_="habitus"),
    wiki("Common limes, avenue.jpg", "europaea — algemeen", type_="algemeen"),
    wiki("Common limes in the landscape, Kings Somborne, UK.jpg", "europaea — algemeen", type_="algemeen"),
]},

"Trifolium repens": {"photos": [
    wiki("Trifolium_repens_-_white_clover_on_way_from_Govindghat_to_Gangria_at_Valley_of_Flowers_National_Park_-_during_LGFC_-_VOF_2019_(1).jpg", "repens — bloeiwijze", type_="bloeiwijze"),
    wiki("2020 year. Herbarium. Clover. img-001.jpg", "repens — habitus", type_="habitus"),
    wiki("Trifolium repens - white clover on way from Govindghat to Gangria at Valley of Flowers National Park - during LGFC - VOF 2019 (1).jpg", "repens — bloeiwijze", type_="bloeiwijze"),
]},

"Tsuga canadensis": {"photos": [
    wiki("Eastern Hemlock Branch 253271179.jpg", "canadensis — algemeen", type_="algemeen"),
    wiki("Eastern Hemlocks, Fairfax, VA.jpg", "canadensis — algemeen", type_="algemeen"),
    wiki("Hemlock's deciduous nature.jpg", "canadensis — algemeen", type_="algemeen"),
]},

"Tulipa hybriden": {"photos": [
    wiki("Tulip_-_floriade_canberra.jpg", "Tulpen in bloei", type_="bloeiwijze"),
    wiki("Tulipa_gesneriana3.jpg", "Tulp — habitus", type_="habitus"),
    wiki("Tulips_various_red_and_yellow.jpg", "Tulpen — diverse kleuren", type_="bloeiwijze"),
]},

"Tussilago farfara": {"photos": [
    wiki("Tussilago farfara 15-p.bot-tussi.farfa-19.jpg", "farfara — habitus", type_="habitus"),
    wiki("Coltsfoot.jpg", "farfara — algemeen", type_="algemeen"),
    wiki("Dandelion and Coltsfoot.jpg", "farfara — algemeen", type_="algemeen"),
]},

"Urtica dioica": {"photos": [
    wiki("Textielmuseum-cabinet-13.jpg", "dioica — habitus", type_="habitus"),
    wiki("Urtica dioica (Stinging Nettle) pollen.tif", "dioica — bloeiwijze", type_="bloeiwijze"),
    wiki("Urtica dioica pollen.jpg", "dioica — bloeiwijze", type_="bloeiwijze"),
]},

"Urtica urens": {"photos": [
    wiki("Urtica_urens_002.JPG", "urens — bloeiwijze", type_="bloeiwijze"),
    wiki("Urtica urens 002.JPG", "urens — algemeen", type_="algemeen"),
]},

"Vaccinium myrtillus": {"photos": [
    wiki("Bilberry.jpg", "myrtillus — vrucht", type_="vrucht"),
    wiki("Hands scooping up fresh bilberries picked in Tuntorp.jpg", "myrtillus — vrucht", type_="vrucht"),
    wiki("203 Vaccinum myrtillus L.jpg", "myrtillus — algemeen", type_="algemeen"),
]},

"Verbascum cultivars": {"photos": [
    wiki("Verbascum sinuatum August 2007-1.jpg", "cultivars — habitus", type_="habitus"),
    wiki("Verbascum nigrum flowers closeup.jpg", "cultivars — bloeiwijze", type_="bloeiwijze"),
    wiki("AAS87.jpg", "cultivars — algemeen", type_="algemeen"),
]},

"Verbena bonariensis": {"photos": [
    wiki("Verbena_lila_(Verbena_bonariensis),_Jardín_Botánico,_Múnich,_Alemania,_2013-09-08,_DD_01.JPG", "bonariensis — bloeiwijze", type_="bloeiwijze"),
    wiki("1M3A5421.jpg", "bonariensis — algemeen", type_="algemeen"),
    wiki("Bloeiwijze van Verbena bonariensis. 07-09-2024. (d.j.b).jpg", "bonariensis — algemeen", type_="algemeen"),
]},

"Veronica filiformis": {"photos": [
    wiki("Slender_Speedwell_(Veronica_filiformis).jpg", "filiformis — bloeiwijze", type_="bloeiwijze"),
    wiki("Faden-Ehrenpreis (Veronica filiformis)-20230419-RM-125228.jpg", "filiformis — habitus", type_="habitus"),
    wiki("Slender Speedwell (Veronica filiformis).jpg", "filiformis — algemeen", type_="algemeen"),
]},

"Veronica longifolia": {"photos": [
    wiki("Veronica_longifolia_Przetacznik_długolistny_2020-07-12_05.jpg", "longifolia — bloeiwijze", type_="bloeiwijze"),
    wiki("Antirrhinum majus-Flower 02.jpg", "longifolia — bloeiwijze", type_="bloeiwijze"),
    wiki("Veronica longifolia Przetacznik długolistny 2020-07-12 02.jpg", "longifolia — algemeen", type_="algemeen"),
]},

"Viburnum opulus": {"photos": [
    wiki("Viburnum_01.JPG", "opulus — bloeiwijze", type_="bloeiwijze"),
    wiki("Snowball flowers (13985050634).jpg", "opulus — bloeiwijze", type_="bloeiwijze"),
    wiki("Viburnum opulus fruits - Keila.jpg", "opulus — vrucht", type_="vrucht"),
]},

"Vinca major": {"photos": [
    wiki("Vinca_major_-_Flower_and_bud.jpg", "major — bloeiwijze", type_="bloeiwijze"),
    wiki("Apocynaceae - Vinca major-1.JPG", "major — habitus", type_="habitus"),
    wiki("Apocynaceae - Vinca major-2.jpg", "major — habitus", type_="habitus"),
]},

"Vinca minor": {"photos": [
    wiki("Vinca_minor_Nashville.jpg", "minor — bloeiwijze", type_="bloeiwijze"),
    wiki("Vinca major-minor margins.jpg", "minor — algemeen", type_="algemeen"),
    wiki("Vinca minor 'Argenteovariegata' Barwinek pospolity 2017-10-15 01.jpg", "minor — algemeen", type_="algemeen"),
]},

"Viola": {"photos": [
    wiki("Viola_odorata_kz01.jpg", "Viooltje in bloei", type_="bloeiwijze"),
    wiki("Viola_tricolor_kz01.jpg", "Driekleurig viooltje — habitus", type_="habitus"),
    wiki("Viola_odorata1.jpg", "Viooltje — blad", type_="blad"),
]},

"Weigela": {"photos": [
    wiki("Weigela_coraeensis6.jpg", "Weigela — bloeiwijze", type_="bloeiwijze"),
    wiki("Weigela flower.jpg", "Weigela — bloeiwijze", type_="bloeiwijze"),
    wiki("Weigela foliage in garden.jpg", "Weigela — blad", type_="blad"),
]},

"Wisteria sinensis": {"photos": [
    wiki("Chinesischer_Blauregen_Detail_Blütentraube.JPG", "sinensis — bloeiwijze", type_="bloeiwijze"),
    wiki("Chinesischer Blauregen Detail Blütentraube.JPG", "sinensis — bloeiwijze", type_="bloeiwijze"),
    wiki("Wisteria sinensis (Sims) DC seeds.jpg", "sinensis — vrucht", type_="vrucht"),
]},

"Zinnia elegans": {"photos": [
    wiki("Zinnienblüte_Zinnia_elegans_stack15_20190722-RM-7222254.jpg", "elegans — bloeiwijze", type_="bloeiwijze"),
    wiki("Zinnia July 2010-1.jpg", "elegans — habitus", type_="habitus"),
    wiki("Zinnia elegans, plantation, Alhambra, Granada, Spain.jpg", "elegans — habitus", type_="habitus"),
]},

"x Cupressocyparis leylandii": {"photos": [
    wiki("x_Cupressocyparis_leylandii_kz01.jpg", "Leyland-cipres — habitus", type_="habitus"),
    wiki("Leyland_Cypress_Hedge.jpg", "Leyland-cipres — haag", type_="habitus"),
    wiki("Leyland_cypress_foliage.jpg", "Leyland-cipres — blad", type_="blad"),
]},

}
