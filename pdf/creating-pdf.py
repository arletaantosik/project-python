from fpdf import FPDF 

pdf = FPDF(orientation='P', unit='pt', format='A4') #orientation='P' -> w pionie, L-> poziomie, unit='pt' -> jednostki w punktach
pdf.add_page()

pdf.image('tiger.jpeg', w=80, h=50) # by default -> in upper left corner of the page

pdf.set_font(family='Times', style='B', size=24) # style='B' -> bold (pogrubiona) czcionka
pdf.cell(w=0, h=50, txt="Tiger", align='C', ln=1) #w=0 -> automatyczna szerokosc (do konca strony), align='C' -> center, ln=1 -> new line, border = 1 -> to visualize text border

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt='Description', ln=1)

pdf.set_font(family='Times', size=12)
txt1 = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia.[5] This population inhabits the southern and central parts of the Malay Peninsula and has been classified as critically endangered on the IUCN Red List since 2015. As of April 2014, the population was estimated at 80 to 120 mature individuals with a continuous declining trend"""
pdf.multi_cell(w=0, h=15, txt=txt1) #multicell to have a long text in a A4 paper border, not just everything in one line

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Kingdom:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Phylum:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Chordata', ln=1)


pdf.output('output.pdf') #save pdf
