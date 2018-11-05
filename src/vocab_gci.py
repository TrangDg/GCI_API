
from cromulent.model import factory, Type, Identifier, Person, Activity, \
	Material, Actor, Group, ContactPoint, MeasurementUnit, Dimension, \
	LinguisticObject
from cromulent.vocab import instances, register_aat_class, Department, CollectionSet

factory.base_url = "http://localhost:5000/gci/"

register_aat_class("Barcode", Identifier, "300343361", "Barcode")
register_aat_class("CatalogNumber", Identifier, "300404620", "Catalog Number")
register_aat_class("SamplePreparation", Type, "300379533", "Sample Preparation")
# register_aat_class("PhoneNumber", ContactPoint, "")
register_aat_class("EMail", ContactPoint, "300149026", "Electronic Mail")
register_aat_class("Telephone", ContactPoint, "300249768", "Telephone")
# Grid Locationregister_aat_class("Mass", Dimension, "300055664", "Mass")
register_aat_class("MassVolume", Dimension, "300055649", "Mass or Volume")
register_aat_class("Notes", LinguisticObject, "300027200", "Notes")
register_aat_class("Safety", Type, "300055282", "Safety")
register_aat_class("FireSafety", Type, "300055285", "Fire Safety")
# No AAT vocab term for Formulation, use Recipe aat_id instead
register_aat_class("Formulation", LinguisticObject, "300027043", "Formulation")
register_aat_class("Formula", Identifier, "300055660", "Chemical Formula")




# NATURAL/SYNTHETIC

natural = Type("http://vocab.getty.edu/aat/300219527", label="Natural")
synthetic = Type("http://vocab.getty.edu/aat/300218678", label="Synthetic")

instances["natural"] = natural 
instances["synthetic"] = synthetic

# SAMPLE TYPE

pigment = Type("http://vocab.getty.edu/aat/300013109", label="Pigment")
stone_nat = Type("http://vocab.getty.edu/aat/300011176", label="Stone, natural") 
stone_art = Type("http://vocab.getty.edu/aat/300010788", label="Stone, artificial")
mixture = Type("http://vocab.getty.edu/aat/300246925", label="Mixture")
wood = Type("http://vocab.getty.edu/aat/300011914", label="Wood")
dye = Type("http://vocab.getty.edu/aat/300013029", label="Dye")
oil_paint = Type("http://vocab.getty.edu/aat/300015050", label="Paint, oil-based")
oil_paint_water = Type("http://vocab.getty.edu/aat/300410261", label="Paint, oil-based, water mixable")
resin_nat = Type("http://vocab.getty.edu/aat/300378966", label="Natural Resin")
photo_paper = Type("http://vocab.getty.edu/aat/300014190", label="Photographic Paper")
raw_mat = Type("http://vocab.getty.edu/aat/300015351", label="Raw Material") 
# raw material - organic or inorganic can be distinguished by Compound Type
gum = Type("http://vocab.getty.edu/aat/300012866", label="Gum")
acrylic = Type("http://vocab.getty.edu/aat/300015058", label="Paint, acrylic")
protein = Type("http://vocab.getty.edu/aat/300206575", label="Protein")
oil = Type("http://vocab.getty.edu/aat/300014254", label="Oil")
watercolor = Type("http://vocab.getty.edu/aat/300015045", label="Paint, watercolor")
film = Type("http://vocab.getty.edu/aat/300014637", label="Film")
ink = Type("http://vocab.getty.edu/aat/300015012", label="Ink")
textile = Type("http://vocab.getty.edu/aat/300231565", label="Fabric/Textile")
resin_syn = Type("http://vocab.getty.edu/aat/300378967", label="Synthetic Resin")
wax = Type("http://vocab.getty.edu/aat/300014585", label="Wax")
varnish = Type("http://vocab.getty.edu/aat/300014974", label="Varnish")
additive = Type("http://vocab.getty.edu/aat/300014701", label="Paint Additive")
medium = Type("http://vocab.getty.edu/aat/300014720", label="Medium")
filler = Type("http://vocab.getty.edu/aat/300080665", label="Filler")
glass = Type("http://vocab.getty.edu/aat/300010797", label="Glass")
metal = Type("http://vocab.getty.edu/aat/300010900", label="Metal")
paint = Type("http://vocab.getty.edu/aat/300015029", label="Paint")
tempera = Type("http://vocab.getty.edu/aat/300386230", label="Paint, tempera")
leather = Type("http://vocab.getty.edu/aat/300011845", label="Leather")
oleoresin = Type("http://vocab.getty.edu/aat/http://vocab.getty.edu/aat/300012891", label="Oleoresin / Balsam")
adhesive = Type("http://vocab.getty.edu/aat/300014801", label="Adhesive")
paper = Type("http://vocab.getty.edu/aat/300014109", label="Paper")
pastel = Type("http://vocab.getty.edu/aat/300404632", label="Pastel")
gouache = Type("http://vocab.getty.edu/aat/300070114", label="Gouache")
brush = Type("http://vocab.getty.edu/aat/300024760", label="Brush")
solvent = Type("http://vocab.getty.edu/aat/300015217", label="Solvent")
sample_book = Type("http://vocab.getty.edu/aat/300027337", label="Sample Book")
glaze = Type("http://vocab.getty.edu/aat/300015091", label="Glaze")
abrasive = Type("http://vocab.getty.edu/aat/300014693", label="Abrasive")
size = Type("http://vocab.getty.edu/aat/300015312", label="Size")
plastic = Type("http://vocab.getty.edu/aat/300014570", label="Plastic")
other = Type("http://vocab.getty.edu/aat/300400513", label="Other")

instances["pigment"] = pigment
instances["stone, natural"] = stone_nat
instances["stone, artificial"] = stone_art
instances["prepared mixture"] = mixture
instances["wood"] = wood 
instances["dye"] = dye
instances["paint, oil-based"] = oil_paint
instances["paint, oil-based, water mixable"] = oil_paint_water
instances["natural resin"] = resin_nat
instances["photographic paper"] = photo_paper
instances["raw Material - organic (seed, nut, etc.)"] = raw_mat
instances["Raw Material - inorganic"] = raw_mat
instances["gum"] = gum
instances["paint, acrylic"] = acrylic
instances["protein"] = protein
instances["oil"] = oil
instances["paint, watercolor"] = watercolor
instances["film"] = film
instances["ink"] = ink
instances["fabric / textile"] = textile
instances["synthetic resin"] = resin_syn
instances["wax"] = wax
instances["varnish"] = varnish
instances["paint additive"] = additive
instances["medium - commercially prepared"] = medium
instances["filler"] = filler
instances["glass"] = glass
instances["metal"] = metal
instances["paint, other"] = paint
instances["paint, tempera"] = tempera
instances["leather"] = leather
instances["oleoresin / balsam"] = oleoresin
instances["adhesive"] = adhesive
instances["paper"] = paper
instances["pastel"] = pastel
instances["gouache"] = gouache
instances["brush"] = brush
instances["solvent"] = solvent
instances["sample book"] = sample_book
instances["glaze"] = glaze
instances["abrasive"] = abrasive
instances["size"] = size
instances["plastic"] = plastic
instances["other"] = other


# TYPICAL USE

construction = Type("http://vocab.getty.edu/aat/300014857", label="Construction Material")
colorant = Type("http://vocab.getty.edu/aat/300013026", label="Colorant")
# Assuming Photography as a process, but could mean a discipline
photography = Type("http://vocab.getty.edu/aat/300054225", label="Photography")
vehicle = Type("http://vocab.getty.edu/aat/300014774", label="Vehicle (binder)")
# Assuming "Component of Another Category" is Material Components
component = Type("http://vocab.getty.edu/aat/300264237", label="Component of another category")
protective_coating = Type("http://vocab.getty.edu/aat/300224445", label ="Protective Coating")
surfactant = Type("http://vocab.getty.edu/aat/300015321", label="Surfactant")
# Gilding(technique): 300053789 or gilding(material): 300379350
gilding = Type("http://vocab.getty.edu/aat/300379350", label="Gilding")
support = Type("http://vocab.getty.edu/aat/300014844", label="Support")
ground = Type("http://vocab.getty.edu/aat/300015297", label="Ground")
primer = Type("http://vocab.getty.edu/aat/300015304", label="Primer")
defoamer = Type("http://vocab.getty.edu/aat/300014717", label="Defoamer")
emulsifier = Type("http://vocab.getty.edu/aat/300014735", label="Emulsifier")
dispersant = Type("http://vocab.getty.edu/aat/300015322", label="Dispersant")
thickener = Type("http://vocab.getty.edu/aat/300014795", label="Thickener")
# drying_agent 
# polishing material
# cleaning agent
# paint removal
# artificial aging
# sealant

instances["construction material"] = construction
instances["binding medium"] = medium
instances["colorant"] = colorant
instances["photography"] = photography
instances["vehicle"] = vehicle
instances['component of another category'] = component
instances['protective coating'] = protective_coating 
instances['medium'] = medium
instances['surfactant'] = surfactant
instances['gilding'] = gilding
instances['support'] = support
instances['ground'] = ground
instances['primer'] = primer
instances['defoamer'] = defoamer
instances['emulsifier'] = emulsifier
instances['dispersant'] = dispersant
instances['thickener'] = thickener


# PHYSICAL FORM

# raw / natural form
opaque = Type("http://vocab.getty.edu/aat/300056216", label="Opaque")
liquid = Type("http://vocab.getty.edu/aat/300015378", label="Liquid")
transparent = Type("http://vocab.getty.edu/aat/300056220", label="Transparent")
transluscent = Type("http://vocab.getty.edu/aat/300056219", label="Translucent")
# slides (photographs): 300128371 OR slides(microscopy): 300380440, could mean both depending on the sample
slide = Type("http://vocab.getty.edu/aat/300380440", label="Slide")
paste = Type("http://vocab.getty.edu/aat/300014838", label="Paste")
solution = Type("http://vocab.getty.edu/aat/300210311", label="Solution")
roll = Type("http://vocab.getty.edu/aat/300127382", label="Film Roll")
flake = Type("http://vocab.getty.edu/aat/300014649", label="Flakes")
# chips -- no term "chips" in AAT, could have the same meaning as flakes
solid = Type("http://vocab.getty.edu/aat/300015377", label="Solid")
# paint_out
# plate
# sheets
# granules
# blocks
# chunks -- no AAT term 

instances["opaque"] = opaque  
instances["liquid"] = liquid 
instances["transparent"] = transparent
instances["transluscent"] = transluscent
instances["slide"] = slide
instances["paste"] = paste
instances["solution"] = solution
instances["roll"] = roll
instances["flakes"] = flake
instances["flake(s)"] = flake 
instances["solid"] = solid


# COLOR 

multi_colored = Type("http://vocab.getty.edu/aat/300252256", label="Multi-colored")
yellow = Type("http://vocab.getty.edu/aat/300127794", label="Yellow")
red = Type("http://vocab.getty.edu/aat/300126225", label="Red")
blue = Type("http://vocab.getty.edu/aat/300129361", label="Blue")
white = Type("http://vocab.getty.edu/aat/300129784", label="White")
brown = Type("http://vocab.getty.edu/aat/300127490", label="Brown")
green = Type("http://vocab.getty.edu/aat/300128438", label="Green")
black = Type("http://vocab.getty.edu/aat/300130920", label="Black")
violet = Type("http://vocab.getty.edu/aat/300130602", label="Violet")
orange = Type("http://vocab.getty.edu/aat/300126734", label="Orange")
# light_amber -- no AAT term, there's term for "light"
amber = Type("http://vocab.getty.edu/aat/300311361", label="Amber")
colorless = Type("http://vocab.getty.edu/aat/300265729", label="Colorless")
light_yellow = Type("http://vocab.getty.edu/aat/300127850", label="Light Yellow")
gray = Type("http://vocab.getty.edu/aat/300130811", label="Gray")
pink = Type("http://vocab.getty.edu/aat/300124707", label="Pink")
beige = Type("http://vocab.getty.edu/aat/300266234", label="Beige")
# light_beige
# tan
dark_brown = Type("http://vocab.getty.edu/aat/300127526", label="Dark Brown")
dark_yellow = Type("http://vocab.getty.edu/aat/300127906", label="Dark Yellow")
light_brown = Type("http://vocab.getty.edu/aat/300127503", label="Light Brown")
# dark_amber
# very_light_yellow
# brownish_yellow
# light_tan
light_orange = Type("http://vocab.getty.edu/aat/300126763", label="Light Orange")
reddish_yellow = Type("http://vocab.getty.edu/aat/300127981", label="Reddish Yellow")
# clear
yellowish_white = Type("http://vocab.getty.edu/aat/300127985", label="Yellowish_white")
# very_light_beige
light_grey = Type("http://vocab.getty.edu/aat/300130813", label="Light Grey")

instances['multi-colored'] = multi_colored
instances['yellow'] = yellow
instances["red"] = red
instances['blue'] = blue
instances['white']=white
instances['brown']= brown
instances['green'] = green
instances['black'] = black
instances['violet'] = violet
instances['orange'] = orange
instances['amber'] = amber
instances['colorless'] = colorless
instances['light yellow'] = light_yellow
instances['gray'] = gray
instances['grey'] = gray
instances['pink'] = pink
instances['beige'] = beige
instances['dark brown'] = dark_brown
instances['dark yellow'] = dark_yellow
instances['light brown'] = light_brown
instances['light orange'] = light_orange
instances['reddish yellow'] = reddish_yellow
instances['yellowish white'] = yellowish_white
instances['light grey'] = light_grey


# ACQUIRED_BY PERSON

AKaplan = Person(label="Art Kaplan")
BGinell = Person(label="Bill Ginell")
TLearner = Person(label="Tom Learner")
MSchilling = Person(label="Mike Schilling")
DStulik = Person(label="Dusan Stulik")
RRenz = Person(label="Roberta Renz")
CGreet = Person(label="Casey Greet")
JJimerez = Person(label="Jesus Jimerez")
MDerrick = Person(label="M. Derrick")
CGrzywacz = Person(label="Cecily Grzywacz")
GChiari = Person(label="Giacomo Chiari")
ZPinney = Person(label="Z. Pinney")
MKomsky = Person(label="M. Komsky")
ARothe = Person(label="A. Rothe")
AParker = Person(label="A. Parker")
CBrindle = Person(label="Carrie Brindle")
HFlorsheim = Person(label="H. Florsheim")
MBolton = Person(label="M. Bolton")
CPatterson = Person(label="Catherine Patterson")
NBarrio = Person(label="N. Barrio")
MBishop = Person(label="M. Bishop")
HKhanjian = Person(label="H. Khanjian")



GCI = Department("http://www.getty.edu/conservation/", label="Getty Conservation Institute")
JPGM = Department("http://www.getty.edu/museum/", label="J. Paul Getty Museum")
JPGM_Anti = Department("http://www.getty.edu/art/antiquities/", label='JPGM Antiquities')
JPGM_Paint = Department("http://www.getty.edu/museum/conservation/index.html", label="JPGM Painting Conservation")
JPGM_Dec = Department("http://www.getty.edu/museum/conservation/index.html", label="JPGM Decorative Arts Conservation")
JPGM_Anti_Con = Department("http://www.getty.edu/museum/conservation/index.html", label="JPGM Antiquities Conservation")



person = {
	'Art Kaplan': AKaplan, 'A. Kaplan': AKaplan, 'Art kaplan': AKaplan,
	'Bill Ginell': BGinell, 'B. Ginell': BGinell,
	'Tom Learner': TLearner,
	'M. Schilling': MSchilling, 'Mike Schilling': MSchilling,
	'D. Stulik': DStulik, 'Dusan Stulik': DStulik,
	'Roberta Renz': RRenz,
	'Casey Greet': CGreet,
	'Jesus Jimerez': JJimerez,
	'M. Derrick': MDerrick,
	'Cecily Grzywacz': CGrzywacz, 'C. Grzywacz': CGrzywacz,
	'Giacomo Chiari': GChiari, 'G. Chiari': GChiari,
	'Z. Pinney': ZPinney, 
	'M. Komsky': MKomsky,
	'A. Rothe': ARothe,
	'A. Parker': AParker,
	'Carrie Brindle': CBrindle,
	'H. Florsheim': HFlorsheim,
	'M. Bolton': MBolton,
	'Catherine Patterson': CPatterson,
	'N. Barrio': NBarrio,
	'M. Bishop': MBishop,
	'H. Khanjian': HKhanjian,
	'JPGM Painting Conservation': JPGM_Paint,
	'JPGM Dec Arts Conservation': JPGM_Dec,
	'JPGM Antiquities Conservation': JPGM_Anti_Con
}


dept = {
	'GCI': GCI, 
	'JPGM': JPGM, 
	'JPGM Antiquities': JPGM_Anti,
	'JPGM Painting Conservation': JPGM_Paint,
	'JPGM Dec Arts Conservation': JPGM_Dec,
	'JPGM Antiquities Conservation': JPGM_Anti_Con
	
}


# ACQUIRED FROM SELLERS

CSchoettlin = Actor(label="Charles Schoettlin")
Kremer= Group(label="Kremer Pigments Inc.")
Dick_Blick = Group(label="Dick Blick Art Materials")
World_Timbers = Group(label="World Timbers")
Forbes = Group(label="E. W. Forbes Collection")
Tate = Group(label="Tate Britain")
Pearl_Art = Group("Pearl Art and Craft Supply")
McCrone = Group(label="McCrone Accessories & Components")
Schweppe = Actor(label="H. Schweppe")
US_Customs = Group(label="U.S.Customs Lab, Long Beach")
Standard_Brands = Group(label="Standard Brands")
Daniel_Smith = Group(label="Daniel Smith Artist Materials")
Arbidar = Group(label="The Arbidar Co.")
Harvard = Group(label="Harvard Art Museums")
BH_Photo = Group(label="B&H Photo Video")
Sam_Francis = Group(label="Sam Francis Foundation")
Jan_Wouters = Actor(label="Jan Wouters")
Marthe_Keller = Actor(label="Marthe Keller")
CA_State = Group(label='"CA State Poly Univ, Pomona')
Easy_Leaf = Group(label="Easy Leaf Co.")
Italian_Art = Group(label="The Italian Art Store")


sellers = {
	'Charles Schoettlin': CSchoettlin, 
	'Kremer Pigments Inc': Kremer, 'Kremer-Pigmente': Kremer, 'Kremer Pigmente (components)': Kremer, 'Kremer Pigmente': Kremer,
	'Dick Blick Art Materials': Dick_Blick,
	'World Timbers': World_Timbers,
	'E. W. Forbes Collection': Forbes,
	'Tate Britain': Tate,
	'Pearl Art and Craft Supply': Pearl_Art,
	'H. Schweppe': Schweppe,
	'U.S.Customs Lab, Long Beach': US_Customs,
	'Standard Brands':Standard_Brands,
	'Daniel Smith Artist Materials': Daniel_Smith, 'Daniel Smith': Daniel_Smith,
	'The Arbidar Co.': Arbidar,
	'Harvard Art Museums': Harvard,
	'Sam Francis Foundation': Sam_Francis,
	'B&H Photo Video': BH_Photo,
	'Jan Wouters': Jan_Wouters,
	'Marthe Keller': Marthe_Keller,
	'CA State Poly Univ, Pomona': CA_State,
	'The Italian Art Store': Italian_Art
}

# COLLECTION NAME

Schoettlin_Coll = CollectionSet(label="Schoettlin Mineral Collection")


collection = {
	"Schoettlin Mineral Collection": Schoettlin_Coll
}


# CONTACT PERSONS

WSchoettlin = Person(label="Warren Schoettlin")
MKeller = Person(label="Marthe Keller")
RSchmidtling = Person(label="Ron Schmidtling")

contact = {
	'Warren Schoettlin': WSchoettlin,
	'Marthe Keller': MKeller,
	'Ron Schmidtling': RSchmidtling
}



# MANUFACTURERS

# Kremer-Pigmente 
# Kremer Pigmente (components)
Winsor_Newton = Group(label="Winsor & Newton")
Cargille_Lab = Group(label="R.P. Cargille Laboratories")
# Kremer Pigmente
# prepared by H. Schweppe
# Daniel Smith
Max_Grumbacher = Group(label="Max Grumbacher")
Kodak = Group(label="Eastman Kodak Co.")
Verfmolen = Group(label="Verfmolen 'De Kat'")
Holbein_Works = Group(label="Holbein Works, Ltd.")
Royal_Talens = Group(label="Royal Talens")
Zecchi = Group(label="Zecchi")
Daler_Rowney = Group(label="Daler Rowney")
Cornelissen_Son = Group(label="L.  Cornelissen & Son")


manufacturers = {
	'Winsor & Newton': Winsor_Newton,
	'R.P. Cargille Laboratories': Cargille_Lab,
	'Max Grumbacher': Max_Grumbacher, 'Max Grumbacher / Sanford': Max_Grumbacher, 'Grumbacher': Max_Grumbacher,
	'Eastman Kodak Co.': Kodak,
	"Verfmolen 'De Kat'": Verfmolen,
	"Holbein Works, Ltd.": Holbein_Works,
	"Royal Talens": Royal_Talens,
	"Zecchi": Zecchi,
	"Daler Rowney": Daler_Rowney,
	"L.  Cornelissen & Son": Cornelissen_Son
}


# COMPOUND TYPE
organic = Type("http://vocab.getty.edu/aat/300191632", label="Organic")
inorganic = Type("http://vocab.getty.edu/aat/300191633", label="Inorganic")
# mix = Type("http://vocab.getty.edu/aat/300206579", label="Combination Inorganic/Organic Material")

instances['organic'] = organic
instances['inorganic'] = inorganic
# instances['mix.'] = mix
instances['mix.'] = mixture
instances['mixture'] = mixture

instances['other (i.e. many components)'] = other




# MIXTURE PIGMENT
lead_white = Type("300013754", label="Lead White")
vine_black = Type("300013161", label="Vine Black")
yellow_ochre = Type("300013967", label="Yellow Ochre")
verdigris = Type("300013491", label="Verdigris")



# MISCELLANEOUS




# Mass or Volume unit
# mass_volume = ['g', 'oz', 'kg', 'ml']
g = MeasurementUnit("http://vocab.getty.edu/aat/300379225", label="grams")
oz = MeasurementUnit("http://vocab.getty.edu/aat/300379229", label="ounces")
kg = MeasurementUnit("http://vocab.getty.edu/aat/300379226", label="kilograms")

# sheets as measurement unit 300014671 (flat object)	
# exp

# 300404395: 'cubic centimeters' == 'milliliters'
ml = MeasurementUnit("300404395", label="milliliters")
# fl. oz.

instances['g'] = g
instances['oz'] = oz
instances['kg'] = kg
instances['ml'] = ml 



# SAFETY
reactivity = Type("http://vocab.getty.edu/aat/300191639", label="Reactivity")
health = Type("http://vocab.getty.edu/aat/300055133", label="Health")

instances['reactivity'] = reactivity
instances['health'] = health








