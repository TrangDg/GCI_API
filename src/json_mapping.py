import os
import csv
import vocab_gci as v

from cromulent.model import factory, ManMadeObject, Material, Type, Place, \
	Identifier, Acquisition, TimeSpan, Actor, Group, Production, \
	Person, Creation, LinguisticObject 
from cromulent.vocab import PrimaryName, Name, Color, instances, Department, \
	Description, Barcode, CatalogNumber, DimensionStatement, MassVolume, Notes,\
	EMail, Telephone, Safety, FireSafety, SamplePreparation, Formulation, Formula
from dateparser import parse
from datetime import timedelta

factory.base_url = "http://localhost:5000/gci/" # Change the base url

factory.validate_profile = False


def main(ID):
	data_folder = os.path.abspath('../GCI_API/data')
	f = open(os.path.join(data_folder, "ref_col.csv"), "r")
	r = csv.reader(f)

	next(r) #Skip header
	
	headers = ["acq_by", "acq_from", "acq_date", "add_names", "avai_data", "cat", 
		"certified", "chem_comp", "CAS", "chem_form", "chem_name", "coll_name", "color",
		"CI", "name", "comp_type", "contact", "email", "experiments", "fire", "formulation",
		"fbarcode", "geo_org", "grid_loc", "health", "manufacturer", "mass_vol", "mix_pigment",
		"mix_type", "MSDS", "nat_syn", "notes", "obarcode", "org_date", "other_safe", 
		"part_coll", "phone", "phys_form", "prep", "reactivity", "samp_type", "typ_use",
		"warning", "borrower", "inv_status"]
	
	for row in r:
		rec = dict(zip(headers, row))
		# Testing first two rows
		if rec['fbarcode'] == ID: 
			s = ManMadeObject(rec['fbarcode'], label=rec['name'])

		# Sample Identification/General Information
			
			s.identified_by = Barcode(label="Full Barcode", value=rec['fbarcode']) 
			s.identified_by = Barcode(label="Old Barcode", value=rec['obarcode'])
			s.identified_by = PrimaryName(label="Common Name", value=rec['name'])
			s.identified_by = Name(label="Additional Names", value=rec['add_names'])
			
			# Sample Type
			if rec['samp_type']:
				try:
					s.classified_as = instances[rec['samp_type'].lower()]
				except:
					s.referred_to_by = Description(label="Sample Type", value=rec['samp_type'])
			
			# Typical use
			if rec['typ_use']:
				use = rec['typ_use'].split('/')
				for i in range(len(use)):
					try:
						s.as_general_use = instances[use[i].lower().strip()]
					except:
						s.referred_to_by = Description(label="Typical Use", value=use[i])
			
			# Physical Form
			if rec['phys_form']:
				pf = rec['phys_form'].split()

				if len(pf) < 4:
					l = []
					
					for i in range(len(pf)):
						try:
							s.classified_as = instances[pf[i].lower().replace(',', '').strip()]
						except:
							l.append(pf[i])
					
					l_join = " ".join(l)
							
					s.referred_to_by = Description(label="Physical Form", value=l_join)
							
						
				else:
					s.referred_to_by = Description(label="Physical Form", value=rec['phys_form'])


			# Color
			if rec['color']:
				try:
					s.classified_as = instances[rec['color'].lower()]
				except:
					s.referred_to_by = Description(label="Color", value=rec['color'])

			# Index (CI) Color
			
			# Natural/Synthetic
			if rec['nat_syn']:
				s.classified_as = instances[rec['nat_syn'].lower()]
			elif rec['nat_syn'] == "Unknown":
				s.classified_as = Type(label="Natural/Synthetic", value="Unknown") 

			# Preparation : go to Production

			# Certified Standard

			# Grid Location: lab shelf/storage?
			loc = Place()
			if rec['grid_loc']:
				loc.identified_by = Identifier(label="Grid Location", value=rec['grid_loc'])
				s.current_location = loc 
			
		# Chemical Information
			# Chemical Formula
			if rec['chem_form']:
				s.identified_by = Formula(value=rec['chem_form'])

			if rec['chem_name']:
				s.identified_by = Name(label="Chemical Name", value=rec['chem_name'])

			if rec['CAS']:
				s.identified_by = Identifier(label="Chemical (CAS) No.", value=rec['CAS'])

			if rec['comp_type']:
				comp_type = rec['comp_type'].lower()
				try:
					s.classified_as = instances[comp_type]
				except:
					s.classified_as = Type(label="Compound Type", value=rec['comp_type'])

			if rec['mix_type']:
				mix_type = rec['mix_type'].split('-')
				for i in mix_type:
					s.classified_as = instances[i.lower().strip()]

		# Acquisition Information

			acq = Acquisition()
			
			s.changed_ownership_through = acq
			acq.transferred_title_to = v.dept['GCI']
			# Acquisition Date
			if rec['acq_date']:
				adate = rec['acq_date']
				tspan = TimeSpan(label=adate)
				if len(adate) == 4:
					tspan.begin_of_the_begin = str(parse(adate + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))
					tspan.end_of_the_end = str(parse(adate + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}) + timedelta(days=365))
				elif 'ca.' in adate or 'Spring' in adate:
					y = adate.split()[1]
					tspan.begin_of_the_begin = str(parse(y + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))	
					tspan.end_of_the_end = str(parse(y + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}) + timedelta(days=365))
				elif '-' in adate:
					y = adate.split('-')
					start_year = y[0].strip()
					end_year = y[1].strip()	
					if len(start_year) == 4:
						tspan.begin_of_the_begin = str(parse(start_year + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))	
						tspan.end_of_the_end = str(parse(end_year + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}) + timedelta(days=365))
					else:
						tspan.begin_of_the_begin = str(parse(adate, settings={'PREFER_DAY_OF_MONTH': 'first'}))
						tspan.end_of_the_end = str(parse(adate, settings={'PREFER_DAY_OF_MONTH': 'last'}) + timedelta(days=1))
				else:
					tspan.begin_of_the_begin = str(parse(adate, settings={'PREFER_DAY_OF_MONTH': 'first'}))
					tspan.end_of_the_end = str(parse(adate, settings={'PREFER_DAY_OF_MONTH': 'last'}) + timedelta(days=1)) 

				acq.timespan = tspan

			# Acquired by
			if rec['acq_by']:

				p = rec['acq_by'].split('-')
				pname = p[0].split()
				
				agent = " ".join(pname)
				dpt = p[-1]

				if agent in v.person:
					emp = v.person[agent]
				else:
					emp = Person(label=agent)
				acq.carried_out_by = emp
				if dpt in v.dept:
					emp.member_of = v.dept[dpt]


			# Part of Collection
			if rec['part_coll']:
				s.referred_to_by = LinguisticObject(label='Part of Collection', value=rec['part_coll'])

			# Acquired from, debating whether it should be Actor or Group,
			# so info of person in contact can be linked
			
			global seller 

			if rec['acq_from']:
				if rec['acq_from'] in v.sellers:
					seller = v.sellers[rec['acq_from'].strip()]
				else:
					seller = Actor(label=rec['acq_from'].strip())
				acq.transferred_title_from = seller

			# Collection Name
			if rec['coll_name']:
				coll = v.collection[rec['coll_name']]
				s.aggregated_by = coll
				coll_creation = Creation()
				coll.created_by = coll_creation
				coll_creation.carried_out_by = seller


			# Contact name
			if rec['contact']:
				if rec['contact'] in v.contact:
					contact_name = v.contact[rec['contact'].strip()]
				else:
					s.related_entity = contact_name
				# Email
				if rec['email']:
					contact_name.contact_point = EMail(label="E-Mail", value=rec['email'])
			
			# Phone number: could be either the number of the contact person, 
			# or of the acquired_from
			# if rec['phone']:


			prod = Production()
			s.produced_by = prod

			# Preparation
			if rec['prep']:
				prep = SamplePreparation(value=rec['prep'])
				prod.technique = prep
				if rec['formulation']:
					prep.referred_to_by = Formulation(value=rec['formulation'])
					
			# Geographic Origin
			if rec['geo_org']:
				origin = Place(label="Geographic Origin")
				origin.identified_by = Name(value=rec['geo_org'])
				prod.took_place_at = origin

			# Manufacturer
			if rec['manufacturer']:
				if rec['manufacturer'] in v.manufacturers:
					mfr = v.manufacturers[rec['manufacturer']]
				elif rec['manufacturer'] in v.sellers:
					mfr = v.sellers[rec['manufacturer']]
				else:
					mfr = Group(label=rec['manufacturer'])
				prod.carried_out_by = mfr
				

			# Catalog No.
			if rec['cat']:
				s.identified_by = CatalogNumber(label="Catalog No.", value=rec['cat'])

		# Miscellaneous

			# Origination Date
			# if rec['org_date']:
			# 	odate = rec['org_date']
			# 	t_span = TimeSpan(label=odate)
			# 	if len(adate) == 4:
			# 		t_span.begin_of_the_begin = str(parse(odate + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))
			# 		t_span.end_of_the_end = str(parse(odate + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}) + timedelta(days=365))
			# 	elif 'ca.' in adate or 'pre' in adate:
			# 		y = odate.split()[1]
			# 		t_span.begin_of_the_begin = str(parse(y + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))	
			# 		t_span.end_of_the_end = str(parse(y + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}) + timedelta(days=365))
			# 	elif '-' in adate:
			# 		y = odate.split('-')
			# 		start_year = y[0].strip()
			# 		end_year = y[1].strip()	
			# 		if len(start_year) == 4:
			# 			t_span.begin_of_the_begin = str(parse(start_year + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))	
			# 			t_span.end_of_the_end = str(parse(end_year + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}) + timedelta(days=365))
			# 		else:
			# 			t_span.begin_of_the_begin = str(parse(odate, settings={'PREFER_DAY_OF_MONTH': 'first'}))
			# 			t_span.end_of_the_end = str(parse(odate, settings={'PREFER_DAY_OF_MONTH': 'last'}) + timedelta(days=1))
			# 	else:
			# 		t_span.begin_of_the_begin = str(parse(odate, settings={'PREFER_DAY_OF_MONTH': 'first'}))
			# 		t_span.end_of_the_end = str(parse(odate, settings={'PREFER_DAY_OF_MONTH': 'last'}) + timedelta(days=1)) 


				# acq.timespan = t_span

			# Mass or Volume
			if rec['mass_vol']:
				mv = rec['mass_vol'].replace('appx.', '').replace('approx.', '').split()				
				if len(mv) == 2:
					dim = MassVolume(value=mv[0])
					s.dimension = dim
					dim.unit = instances[mv[1].replace('.', '')]
				else:
					try:
						u = instances[(mv[1]+" "+mv[2]).replace('.', '')]
						dim = MassVolume(value=mv[0])
						s.dimension = dim
						dim.unit = u
					except:
						s.referred_to_by = DimensionStatement(label="Mass or Volume", value=rec['mass_vol'])



			# Experiments on Sample
			if rec['experiments']:
				s. referred_to_by = Description(label="Experiments on Sample", value=rec['experiments'])


			# Notes
			if rec['notes']:
				s.referred_to_by = Notes(value=rec['notes'])


		# Available Data

		# MSDS & Safety

			# Safety: classified_as or referred_to_by properties
			if rec['fire']:
				s.classified_as = FireSafety(value=rec['fire'])

			if rec['health']:
				health_safe = Safety(label="Health Safety", value=rec['health'])
				s.classified_as = health_safe
				health_safe.classified_as = instances['health']

			if rec['reactivity']:
				react_safe = Safety(label="Reactivity Safety", value=rec['reactivity'])
				s.classified_as = react_safe
				react_safe.classified_as = instances['reactivity']

			if rec['other_safe']:
				other_safe = Safety(label="Other Safety", value=rec['other_safe'])
				s.classified_as = other_safe
				other_safe.classified_as = instances['other']


			js = factory.toJSON(s)
			return js
		

		 








