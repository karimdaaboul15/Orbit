import os, json, textwrap
from pathlib import Path

root = Path('/workspace/Orbit')

brand = {
    'name':'Orbit Aluminum Industries',
    'domain':'https://orbitalu.com',
    'email':'info@orbitalu.com',
    'phone':'+96232031353',
    'fax':'+96232031715'
}

applications = [
("Rolling Shutters","/applications/rolling-shutters/"),
("Roofing","/applications/roofing/"),
("Signage","/applications/signage/"),
("Gutters & Downspouts","/applications/gutters-downspouts/"),
("License Plates","/applications/license-plates/"),
("Truck & Trailer Panels","/applications/truck-trailer-panels/"),
("ACP","/applications/aluminum-composite-panels-acp/"),
("Cladding","/applications/cladding/"),
]

coatings = [
("PVDF","/coatings/pvdf/"),
("PE & HDPE","/coatings/pe-hdpe/"),
("PU & PUPA","/coatings/pu-pupa/"),
("Epoxy & Acrylic","/coatings/epoxy-acrylic/"),
]
finishes=[
("Woodgrain","/finishes/woodgrain/"),
("Metallic","/finishes/metallic/"),
("Matte / Gloss / Textured","/finishes/matte-gloss-textured/"),
("Anti-Graffiti","/finishes/anti-graffiti/"),
("Anti-Bacteria","/finishes/anti-bacteria/"),
("Brushed Design","/finishes/brushed-design/"),
]

pages = [
    {"url":"/","title":"Orbit Aluminum Industries | B2B Coil Manufacturing","description":"B2B supplier of aluminum rolling, coil coating, and recycling solutions for Europe and North America. Send RFQs to info@orbitalu.com.","h1":"Integrated Aluminum & Coil Solutions for Manufacturers","vp":"Orbit Aluminum Industries supplies rolled and coated coil solutions from Aqaba, Jordan for Europe and North America.","proof":["ISO 9001 / 14001 / 45001 certified operations","Aluminum rolling + aluminum/steel coil coating + recycling loop","ASTM or EN per customer specification"],"body":"<p>We support manufacturers with semi-finished products in coil and sheet formats available upon request. Our integrated loop connects recycling, slab casting, rolling, and coating for reliable supply planning.</p>","type":"home"},
    {"url":"/capabilities/aluminum-rolling/","title":"Aluminum Rolling Capabilities | Orbit Aluminum","description":"Aluminum rolling for 1xxx/3xxx/5xxx alloys, 0.20-2.00 mm thickness, up to 1650 mm width, and coil weight up to 10 tons.","h1":"Aluminum Rolling Capability","vp":"Semi-finished rolled aluminum for industrial manufacturing programs.","proof":["Alloys 1xxx / 3xxx / 5xxx (others available upon request)","Thickness 0.20-2.00 mm, max width 1650 mm","Coil ID 406/508 and coil weight up to 10 tons"],"type":"cap_rolling"},
    {"url":"/capabilities/coil-coating/","title":"Coil Coating Capability | Aluminum and Steel","description":"Coil coating for aluminum and steel substrates with PE, HDPE, PVDF, PU, PUPA, Epoxy and Acrylic systems.","h1":"Coil Coating Capability","vp":"One-side or two-side coating with primer for aluminum and steel coils.","proof":["Max coating width 1350 mm and thickness up to 1.60 mm","Color matching by RAL or custom matching","MOQ 6 MT per color per size; 3 MT option for part orders"],"type":"cap_coating"},
    {"url":"/capabilities/aluminum-recycling/","title":"Aluminum Recycling Capability | Orbit Aluminum","description":"Aluminum recycling process including shredding, separation, sorting, and slab output to support resource efficiency and circularity.","h1":"Aluminum Recycling Capability","vp":"Recycling operations support resource efficiency and circularity across the supply chain.","proof":["Wide scrap acceptance including UBC, extrusion, coil, and painted scrap","Processing includes shredding, separation, sorting, and cast house furnaces","Output format: slabs"],"type":"cap_recycling"},
    {"url":"/products/rolled-aluminum-coil-sheet/","title":"Rolled Aluminum Coil & Sheet | Orbit Aluminum","description":"Rolled aluminum coil and sheet with mill finish or stucco, alloys 1xxx/3xxx/5xxx, and processing services for manufacturing supply.","h1":"Rolled Aluminum Coil & Sheet","vp":"Semi-finished rolled products built for industrial forming and fabrication.","proof":["Mill finish and stucco options","Slitting, cut-to-length, embossing, edge trimming, leveling","Protective film or lubrication available"],"type":"product_rolling"},
    {"url":"/products/prepainted-aluminum-coil/","title":"Prepainted Aluminum Coil | Orbit Aluminum","description":"Prepainted aluminum coil for roofing, cladding, signage, and shutters with flexible coating systems and custom color matching.","h1":"Prepainted Aluminum Coil","vp":"Prepainted aluminum coils for durable visual and functional performance.","proof":["PE, HDPE, PVDF, PU, PUPA, Epoxy, Acrylic, Epoxy-PE systems","Solid, metallic, woodgrain, brushed, matte/gloss, textured finishes","One-side and two-side coating with primer"],"type":"product_coating"},
    {"url":"/products/prepainted-steel-coil/","title":"Prepainted Steel Coil | Orbit Aluminum","description":"Prepainted steel coil with one-side and two-side coating, primer systems, and finish options for industrial applications.","h1":"Prepainted Steel Coil","vp":"Coated steel coil supply for demanding industrial and building products.","proof":["Steel substrate with coating thickness controls","Primer-supported one-side or two-side coating","MOQ options aligned to color and size programs"],"type":"product_steel"},
    {"url":"/products/stucco-embossed-aluminum/","title":"Stucco Embossed Aluminum | Orbit Aluminum","description":"Stucco and embossed aluminum formats for roofing, cladding, and industrial use with consistent rolling and downstream processing.","h1":"Stucco / Embossed Aluminum","vp":"Embossed surfaces for applications requiring function and appearance.","proof":["Produced within rolling thickness range 0.20-2.00 mm","Compatible with slitting and cut-to-length","Coated variants available upon request"],"type":"product_rolling"},
    {"url":"/services/slitting-cut-to-length/","title":"Slitting and Cut-to-Length Services | Orbit","description":"Precision slitting and cut-to-length support for aluminum and coated coils with edge trimming and leveling options.","h1":"Slitting & Cut-to-Length Services","vp":"Converting services that reduce downstream handling and improve line efficiency.","proof":["Slitting, edge trimming, and leveling","Format conversion for coil and sheet","Specifications aligned to RFQ requirements"],"type":"service"},
    {"url":"/quality/","title":"Quality Overview | Orbit Aluminum Industries","description":"Quality management across rolling, coating, and recycling with ISO certification, testing, and market-specific ASTM/EN specifications.","h1":"Quality Overview","vp":"Quality systems are integrated into every production stage.","proof":["ISO 9001, ISO 14001, ISO 45001","Lab and process testing across mechanical and coating metrics","ASTM or EN by customer and market requirements"],"type":"quality"},
    {"url":"/quality/certifications/","title":"ISO Certifications | Orbit Aluminum Industries","description":"Orbit Aluminum Industries certifications include ISO 9001, ISO 14001, and ISO 45001 for quality, environment, and safety systems.","h1":"Certifications","vp":"Certified management systems support consistent delivery and governance.","proof":["ISO 9001","ISO 14001","ISO 45001"],"type":"quality"},
    {"url":"/quality/testing-inspection/","title":"Testing and Inspection | Orbit Aluminum","description":"Testing includes salt spray, UV, T-bend, impact, adhesion, gloss retention, abrasion, MEK rub, pencil hardness and color checks.","h1":"Testing & Inspection","vp":"Testing verifies product behavior before shipment and during qualification.","proof":["Coating durability and adhesion tests","Appearance and color consistency controls","Mechanical response checks for forming and service"],"type":"testing"},
    {"url":"/quality/standards/","title":"Standards and Compliance | Orbit Aluminum","description":"Products manufactured to ASTM or EN per customer specification and destination market requirements in Europe and North America.","h1":"Standards & Compliance","vp":"Specification management is aligned to customer and market requirements.","proof":["ASTM or EN depending on market and customer requirements","Documentation prepared with RFQ technical package","Quality review before production release"],"type":"quality"},
    {"url":"/quality/warranty-claim-policy/","title":"Warranty and Claim Policy | Orbit Aluminum","description":"Warranty guidance and claim policy summary with terms depending on application and environment plus official PDF policy link.","h1":"Warranty & Claim Policy","vp":"Warranty terms are conditional and tied to use conditions.","proof":["Typical range 5 to 20 years depending on application and environment","Coastal vs inland exposure affects expectations","Claim handling follows published policy"],"type":"warranty"},
    {"url":"/sustainability/","title":"Sustainability Overview | Orbit Aluminum","description":"Sustainability at Orbit Aluminum focuses on recycling integration, process efficiency, and circular material flow for manufacturers.","h1":"Sustainability Overview","vp":"Our integrated process supports practical circularity for industrial supply.","proof":["Recycling loop connected to rolling and coating","Supports resource efficiency and circularity","Recycled content varies by alloy"],"type":"sustain"},
    {"url":"/sustainability/recycling-loop/","title":"Recycling Loop | Orbit Aluminum Industries","description":"See how scrap processing, slab casting, rolling, and coating connect into a practical recycling loop supporting supply continuity.","h1":"Recycling Loop","vp":"Scrap is processed into slabs that feed downstream rolling and coating.","proof":["Scrap processing, shredding, separation, sorting","Cast house furnaces and slab output","Loop supports manufacturing continuity"],"type":"sustain"},
    {"url":"/sustainability/recycled-content-by-alloy/","title":"Recycled Content by Alloy | Orbit Aluminum","description":"Recycled content varies by cast alloy. Example: 3105 alloy with PUPA paint can contain 75% recycled material.","h1":"Recycled Content by Alloy","vp":"Recycled content is specified by alloy and end-use requirements.","proof":["Values vary by cast alloy","Example: 3105 with PUPA paint can contain 75% recycled material","Final values confirmed during quotation"],"type":"sustain"},
    {"url":"/resources/","title":"Resources Overview | Orbit Aluminum Industries","description":"Technical resources including datasheets, packaging guidance, RFQ checklist, and FAQs for faster specification and procurement cycles.","h1":"Resources","vp":"Use structured resources to accelerate RFQ clarity and order execution.","proof":["Datasheets and brochures","Packaging and coil handling guidance","RFQ checklist and FAQs"],"type":"resource"},
    {"url":"/resources/datasheets-brochures/","title":"Datasheets and Brochures | Orbit Aluminum","description":"Download and request datasheets for rolled and coated products. Additional technical documents are available upon request.","h1":"Datasheets & Brochures","vp":"Technical files support specification review and procurement approvals.","proof":["Product and process summaries","Specification request workflow","Contact route for controlled documents"],"type":"resource"},
    {"url":"/resources/packaging-coil-handling/","title":"Packaging and Coil Handling | Orbit Aluminum","description":"Packaging and handling guidance for coil delivery, protection, storage, and line preparation for safer receiving and processing.","h1":"Packaging & Coil Handling","vp":"Handling guidance helps reduce transit and storage risk.","proof":["Packaging requirements can be quoted","Protective film options available","Logistics and destination conditions considered"],"type":"resource"},
    {"url":"/resources/rfq-checklist/","title":"RFQ Checklist | Orbit Aluminum Industries","description":"Use this RFQ checklist and copy-paste template to request pricing quickly for rolled or coated aluminum and steel programs.","h1":"RFQ Checklist","vp":"A complete RFQ shortens quote cycles and reduces rework.","proof":["Copy/paste email template to info@orbitalu.com","Field list for materials, coatings, and logistics","Example RFQ included"],"type":"rfq"},
    {"url":"/resources/faqs/","title":"FAQs | Orbit Aluminum Industries","description":"Frequently asked questions about rolling, coating, recycling, standards, testing, warranty expectations, logistics and RFQ details.","h1":"Frequently Asked Questions","vp":"Quick answers for technical and procurement planning.","proof":["Capabilities and product format guidance","Quality, standards, and testing references","Logistics and RFQ support"],"type":"faq"},
    {"url":"/about/","title":"About Orbit Aluminum Industries","description":"Orbit Aluminum Industries serves Europe and North America with integrated aluminum rolling, coil coating, and recycling operations.","h1":"About Orbit Aluminum Industries","vp":"Built to supply manufacturers with consistent semi-finished material programs.","proof":["Headquarters and plant in Aqaba (ASEZA), Jordan","Canada office in Mississauga, Ontario","B2B focus with direct manufacturer collaboration"],"type":"about"},
    {"url":"/location/aqaba-jordan/","title":"Aqaba Location and Logistics | Orbit Aluminum","description":"Shipping and logistics from Aqaba, Jordan with port and land options, Europe transit 5-13 days and USA transit around 25 days.","h1":"Location & Logistics","vp":"Strategic Aqaba origin supports regional and overseas shipping programs.","proof":["Origin: Aqaba, Jordan","Europe transit average 5 to 13 days; USA around 25 days","Incoterms available upon request, including DAP"],"type":"location"},
    {"url":"/contact/","title":"Contact and RFQ | Orbit Aluminum Industries","description":"Send your RFQ to info@orbitalu.com or use the RFQ form. Includes Jordan and Canada addresses, phone and fax details.","h1":"Contact & RFQ","vp":"Email-first RFQ workflow for faster technical quoting.","proof":["Primary conversion email: info@orbitalu.com","Jordan plant and Canada office listed","Copy-ready RFQ checklist embedded"],"type":"contact"},
]

for n,u in applications:
    pages.append({"url":u,"title":f"{n} Coil Solutions | Orbit Aluminum","description":f"{n} supply solutions with mill finish rolled products and prepainted aluminum/steel coil options for industrial manufacturing.","h1":n,"vp":f"Material programs for {n.lower()} including rolled and coated options.","proof":["Mill finish / rolled products available","Prepainted aluminum and steel options available","Substrate selection available upon request"],"type":"application"})
for n,u in coatings:
    pages.append({"url":u,"title":f"{n} Coating System | Orbit Aluminum","description":f"{n} coating system information, application links, testing considerations, and RFQ guidance for coated coil procurement.","h1":f"{n} Coating System","vp":f"{n} system options for performance-driven coated coil programs.","proof":["What it is and where it is used","Performance considerations tied to testing","RFQ support for specification confirmation"],"type":"coating"})
for n,u in finishes:
    pages.append({"url":u,"title":f"{n} Finish | Orbit Aluminum","description":f"{n} finish overview with use cases, performance considerations, and links to application and testing references.","h1":f"{n} Finish","vp":f"{n} options for functional and visual requirements.","proof":["Use-case guidance by application","Testing-linked performance review","RFQ pathway for color and finish confirmation"],"type":"finish"})

nav_sections = [
('Home','/'),('Capabilities','/capabilities/aluminum-rolling/'),('Products','/products/rolled-aluminum-coil-sheet/'),('Applications','/applications/rolling-shutters/'),('Quality','/quality/'),('Sustainability','/sustainability/'),('Resources','/resources/'),('About','/about/'),('Location / Logistics','/location/aqaba-jordan/'),('Contact','/contact/')]

faq_items = [
("What alloys do you publish for rolling?","We publish 1xxx, 3xxx, and 5xxx alloys. Other alloys are available upon request."),
("What standards can you manufacture to?","Products are manufactured to ASTM or EN per customer specification and market requirements."),
("Do you supply both rolled and prepainted options?","Yes. Across application pages, we indicate mill finish/rolled products and prepainted coil options."),
("What warranty range should buyers expect?","Typical warranty is 5 to 20 years depending on final application and installation environment, including coastal vs inland."),
("How should we submit an RFQ?","Send details to info@orbitalu.com with product type, substrate, alloy, temper, dimensions, coating/finish, quantity, application, destination, and required standard."),
]

checklist = """<ul class='checklist'><li>Product (rolled/coated)</li><li>Substrate (aluminum/steel)</li><li>Alloy (if aluminum) and temper</li><li>Thickness and width</li><li>Finish/coating system + color (RAL/custom)</li><li>Quantity (MT) and application</li><li>Destination and incoterm</li><li>Standard required (ASTM/EN)</li><li>Packaging needs</li></ul>"""


def breadcrumb(url):
    parts=[p for p in url.split('/') if p]
    crumbs=[("Home","/")]
    acc=''
    for p in parts:
        acc += '/'+p
        crumbs.append((p.replace('-',' ').title(), acc+'/'))
    lis=''.join([f"<li><a href='{u}'>{n}</a></li>" for n,u in crumbs])
    return f"<nav class='breadcrumbs'><ol>{lis}</ol></nav>"


def jsonld(page):
    canon = brand['domain']+page['url']
    bitems=[{"@type":"ListItem","position":1,"name":"Home","item":brand['domain']+'/'}]
    parts=[p for p in page['url'].split('/') if p]
    acc=''
    pos=2
    for p in parts:
        acc += '/'+p
        bitems.append({"@type":"ListItem","position":pos,"name":p.replace('-',' ').title(),"item":brand['domain']+acc+'/'}); pos+=1
    schemas=[{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":bitems}]
    if page['url']=='/':
        schemas.append({"@context":"https://schema.org","@type":"Organization","name":brand['name'],"url":brand['domain'],"email":brand['email'],"telephone":brand['phone']})
    if page['type'] in {'product_rolling','product_coating','product_steel'}:
        schemas.append({"@context":"https://schema.org","@type":"Product","name":page['h1'],"brand":brand['name'],"category":"Semi-finished products"})
    if True:
        main=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_items]
        schemas.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":main})
    return '\n'.join([f"<script type='application/ld+json'>{json.dumps(s,ensure_ascii=False)}</script>" for s in schemas])


def spec_block(ptype):
    if ptype in {'cap_rolling','product_rolling'}:
        return """<section><h2>Rolling Specifications</h2><table class='spec'><tr><th>Alloys</th><td>1xxx / 3xxx / 5xxx (others upon request)</td></tr><tr><th>Thickness</th><td>0.20-2.00 mm</td></tr><tr><th>Max width</th><td>1650 mm</td></tr><tr><th>Max coil weight</th><td>Up to 10 tons</td></tr><tr><th>Coil ID</th><td>406 / 508</td></tr><tr><th>Finishes</th><td>Mill finish, Stucco</td></tr><tr><th>Services</th><td>Slitting, Cut-to-Length, Embossing, Edge trimming, Leveling, Protective film / lubrication</td></tr></table></section>"""
    if ptype in {'cap_coating','product_coating','product_steel','coating'}:
        return """<section><h2>Coating Specifications</h2><table class='spec'><tr><th>Substrates</th><td>Aluminum & Steel coils</td></tr><tr><th>Max coating width</th><td>1350 mm</td></tr><tr><th>Max thickness</th><td>1.60 mm</td></tr><tr><th>Max coil weight</th><td>Up to 10 tons</td></tr><tr><th>Coating mode</th><td>One-side and two-side coating with primer</td></tr><tr><th>Coatings</th><td>PE, HDPE, PVDF, PU, PUPA, Epoxy, Acrylic, Epoxy-PE</td></tr><tr><th>Finishes</th><td>Solid, metallic, woodgrain, brushed design, matte/gloss, textured, anti-graffiti, anti-bacteria</td></tr><tr><th>MOQ</th><td>6 MT per color per size; option for 3 MT as part of order</td></tr></table></section>"""
    return ''


def app_links_grid():
    return "<section><h2>Applications Served</h2><div class='grid'>"+''.join([f"<a class='card' href='{u}'>{n}</a>" for n,u in applications])+"</div></section>"

def coating_cards():
    return "<section><h2>Coating Systems</h2><div class='grid'>"+''.join([f"<a class='card' href='{u}'>{n}</a>" for n,u in coatings])+"</div></section>"

def finish_cards():
    return "<section><h2>Finishes</h2><div class='grid'>"+''.join([f"<a class='card' href='{u}'>{n}</a>" for n,u in finishes])+"</div></section>"

def faq_section():
    items=''.join([f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq_items])
    return f"<section><h2>FAQs</h2><div class='faq'>{items}</div></section>"


def page_html(page):
    canon=brand['domain']+page['url']
    content=f"<section><p>{page.get('body','Orbit Aluminum Industries focuses on B2B supply with technical clarity. Details not listed are available upon request through the RFQ workflow.')}</p></section>"
    if page['type']=='home':
        content += "<section><h2>Core Capabilities</h2><div class='grid'><a class='card' href='/capabilities/aluminum-rolling/'>Aluminum Rolling</a><a class='card' href='/capabilities/coil-coating/'>Coil Coating</a><a class='card' href='/capabilities/aluminum-recycling/'>Aluminum Recycling</a></div></section>"
        content += "<section><h2>Featured Products</h2><div class='grid'><a class='card' href='/products/rolled-aluminum-coil-sheet/'>Rolled Aluminum Coil & Sheet</a><a class='card' href='/products/prepainted-aluminum-coil/'>Prepainted Aluminum Coil</a><a class='card' href='/products/prepainted-steel-coil/'>Prepainted Steel Coil</a></div></section>"
        content += app_links_grid()+"<section><h2>Integrated Loop</h2><p>Recycling → Slabs → Rolling → Coil Coating → Applications</p></section>"
    if page['type'].startswith('cap_'):
        content += app_links_grid() + "<section><h2>Related Products</h2><div class='grid'><a class='card' href='/products/rolled-aluminum-coil-sheet/'>Rolled Coil & Sheet</a><a class='card' href='/products/prepainted-aluminum-coil/'>Prepainted Aluminum Coil</a><a class='card' href='/products/prepainted-steel-coil/'>Prepainted Steel Coil</a></div></section>"
    if page['type']=='application':
        content += "<section><h2>Supply Scope for this Application</h2><ul><li>Mill finish / rolled product programs</li><li>Prepainted coated coil solutions in aluminum and/or steel (available upon request)</li></ul></section>"
        content += "<section><h2>Related Product Routes</h2><div class='grid'><a class='card' href='/products/rolled-aluminum-coil-sheet/'>Rolled Aluminum Coil & Sheet</a><a class='card' href='/products/prepainted-aluminum-coil/'>Prepainted Aluminum Coil</a><a class='card' href='/products/prepainted-steel-coil/'>Prepainted Steel Coil</a></div></section>"
        content += coating_cards()+finish_cards()
    if page['type'] in {'quality','testing'}:
        content += "<section><h2>Testing Methods</h2><ul><li>Salt spray</li><li>UV</li><li>T-bend</li><li>Impact</li><li>Adhesion</li><li>Gloss retention</li><li>Abrasion</li><li>MEK rub test</li><li>Pencil hardness</li><li>Color difference</li><li>Paint thickness</li></ul></section>"
    if page['type']=='warranty':
        content += "<section><h2>Policy Summary</h2><p>Warranty expectation is generally 5 to 20 years depending on final application and installation environment (coastal vs inland). Claim details are governed by the formal policy.</p><p><a href='https://orbitalu.com/wp-content/uploads/Resources/Claim%20Policy.pdf'>Read Claim Policy PDF</a></p></section>"
    if page['type']=='rfq':
        content += """<section><h2>Copy/Paste RFQ Email Template</h2><pre>To: info@orbitalu.com
Subject: RFQ - [Application] - [Destination]
Product: [rolled/coated]
Substrate: [aluminum/steel]
Alloy/Temper: [e.g., 3105 Hxx]
Thickness/Width: [ ]
Finish/Coating: [PUPA / PVDF / etc.]
Color: [RAL/custom]
Quantity: [MT]
Application: [rolling shutters]
Destination: [country/port]
Incoterm: [Available upon request, including DAP]
Standard: [ASTM/EN]
Packaging: [requirements]</pre></section>
<section><h2>Example RFQ</h2><p>Example only: Rolling shutters, 3105 alloy, PUPA system, custom color, 120 MT total, destination Italy, incoterm DAP, ASTM per customer specification.</p></section>"""
    if page['type']=='contact':
        content += """<section><h2>Primary RFQ Route</h2><p>Email RFQs directly to <a href='mailto:info@orbitalu.com'>info@orbitalu.com</a> <button data-copy='info@orbitalu.com'>Copy Email</button></p>
<form class='rfq-form'><label>Company<input></label><label>Email<input></label><label>RFQ Details<textarea></textarea></label><button type='button'>Generate Copyable RFQ</button></form>
<pre>Copy your RFQ and send to info@orbitalu.com</pre></section>
<section><h2>Addresses</h2><p><strong>Jordan HQ / Plant:</strong><br>Aqaba International Industrial Estate<br>P.O Box 787 Aqaba 77110<br>Aqaba (ASEZA), Jordan</p><p><strong>Canada Office:</strong><br>2222 South Sheridan Way<br>Unit 116<br>Mississauga, ON L5J2M4<br>Canada</p><p>Tel: +96232031353<br>Fax: +96232031715</p></section>"""
    if page['type']=='location':
        content += "<section><h2>Shipping Profile</h2><ul><li>Origin: Aqaba, Jordan</li><li>Nearby markets: land transport where suitable</li><li>Overseas: via port shipping</li><li>Europe: average port-to-port 5 to 13 days</li><li>USA: average port-to-port 25 days</li><li>Incoterms available upon request, including DAP</li></ul></section>"
    if page['type'] in {'coating','finish'}:
        content += "<section><h2>Where It Is Used</h2><p>Use-case selection is linked to project function, environment, and appearance. See application pages for fit-by-market requirements.</p></section>"+app_links_grid()+"<section><h2>Performance Considerations</h2><p>Review testing and inspection methods for T-bend, impact, adhesion, UV, and other controls before finalizing specifications.</p><p><a href='/quality/testing-inspection/'>View Testing & Inspection</a></p></section>"

    html=f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>
<title>{page['title']}</title><meta name='description' content="{page['description']}">
<link rel='canonical' href='{canon}'><meta property='og:title' content="{page['title']}"><meta property='og:description' content="{page['description']}"><meta property='og:url' content='{canon}'><meta property='og:type' content='website'>
<link rel='stylesheet' href='/assets/styles.css'></head><body>
<header><div class='top'><a href='/' class='logo'>Orbit Aluminum Industries</a><nav>{''.join([f"<a href='{u}'>{n}</a>" for n,u in nav_sections])}</nav><div class='lang'><button>EN</button><span>DE | AR | FR | IT | PT (Translations coming soon)</span></div></div></header>
<main>{breadcrumb(page['url'])}<section class='hero'><h1>{page['h1']}</h1><p>{page['vp']}</p><ul>{''.join([f'<li>{p}</li>' for p in page['proof']])}</ul><a class='cta' href='mailto:info@orbitalu.com'>Email RFQ</a></section>
{spec_block(page['type'])}
{content}
<section><h2>Quality & Testing</h2><p>See certification, standards, and complete test list.</p><a href='/quality/testing-inspection/'>Testing & Inspection</a> | <a href='/quality/certifications/'>Certifications</a></section>
<section><h2>What We Need to Quote Fast</h2>{checklist}<p><a href='/resources/rfq-checklist/'>Open RFQ Checklist</a></p></section>
{faq_section()}
<section class='cta-final'><h2>Send your RFQ to info@orbitalu.com</h2><a class='cta' href='/contact/'>Open Contact & RFQ Form</a></section></main>
<footer><div class='footer-grid'><div><h3>Quick Links</h3><a href='/capabilities/aluminum-rolling/'>Capabilities</a><a href='/products/rolled-aluminum-coil-sheet/'>Products</a><a href='/applications/rolling-shutters/'>Applications</a><a href='/quality/'>Quality</a></div>
<div><h3>Jordan</h3><p>Aqaba International Industrial Estate<br>P.O Box 787 Aqaba 77110<br>Aqaba (ASEZA), Jordan</p></div><div><h3>Canada</h3><p>2222 South Sheridan Way<br>Unit 116<br>Mississauga, ON L5J2M4<br>Canada</p></div><div><h3>Contact</h3><p>Tel: +96232031353<br>Fax: +96232031715<br><a href='mailto:info@orbitalu.com'>info@orbitalu.com</a></p><a class='cta' href='/contact/'>Contact / RFQ</a><p>Language selector: EN, DE, AR, FR, IT, PT</p></div></div></footer>
<script src='/assets/main.js' defer></script>
{jsonld(page)}
</body></html>"""
    return html

(root/'assets').mkdir(exist_ok=True)
(root/'content/i18n').mkdir(parents=True, exist_ok=True)
(root/'README.md').write_text("# Orbit Aluminum Industries static build\n\nOpen `index.html` with a local server, e.g. `python3 -m http.server 4173`.\n\nContent is structured in `content/pages.json` and translation placeholders in `content/i18n/*.json`.\n")
(root/'assets/styles.css').write_text("""
:root{--primary:#293e54;--secondary:#c83635;--bg:#f6f8fb;--text:#1d2430}
*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;color:var(--text);background:var(--bg);line-height:1.5}
header{position:sticky;top:0;background:#fff;border-bottom:1px solid #d8dee7;z-index:10}.top{max-width:1200px;margin:auto;padding:10px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}.logo{font-weight:700;color:var(--primary);text-decoration:none}nav a{margin-right:8px;color:var(--primary);text-decoration:none}nav a:hover{color:var(--secondary)}
main{max-width:1200px;margin:auto;padding:16px}.hero{background:#fff;border:1px solid #d8dee7;padding:20px;border-radius:10px}.cta{display:inline-block;background:var(--secondary);color:#fff;padding:10px 14px;border-radius:6px;text-decoration:none}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px}.card{background:#fff;border:1px solid #d8dee7;padding:14px;border-radius:8px;color:var(--primary);text-decoration:none}.card:hover{border-color:var(--secondary);transform:translateY(-1px)}
.spec{width:100%;border-collapse:collapse;background:#fff}.spec th,.spec td{border:1px solid #d8dee7;padding:8px;text-align:left;vertical-align:top}
section{margin:16px 0}.breadcrumbs ol{padding:0;list-style:none;display:flex;gap:6px;flex-wrap:wrap}.breadcrumbs a{color:var(--primary)}
footer{background:var(--primary);color:#fff;padding:24px 16px}.footer-grid{max-width:1200px;margin:auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}footer a{color:#fff;display:block}
.faq details{background:#fff;border:1px solid #d8dee7;padding:10px;margin:8px 0;border-radius:8px}
.checklist li{margin:4px 0}
""")
(root/'assets/main.js').write_text("document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',()=>navigator.clipboard.writeText(b.dataset.copy)));")

for lang in ['en','de','ar','fr','it','pt']:
    (root/f'content/i18n/{lang}.json').write_text(json.dumps({"language":lang,"status":"ready" if lang=='en' else "translations coming soon"},indent=2))

for p in pages:
    out = root / p['url'].strip('/')
    if p['url']=='/':
        file = root/'index.html'
    else:
        out.mkdir(parents=True, exist_ok=True)
        file = out/'index.html'
    file.write_text(page_html(p))

# 404
(root/'404.html').write_text("<!doctype html><html><head><meta charset='utf-8'><title>Page Not Found | Orbit Aluminum</title><link rel='stylesheet' href='/assets/styles.css'></head><body><main><h1>Page not found</h1><p>The page may have moved. Use the navigation or return home.</p><a class='cta' href='/'>Go to Home</a><p>For RFQs email info@orbitalu.com.</p></main></body></html>")

# sitemap
urls='\n'.join([f"  <url><loc>{brand['domain']}{p['url']}</loc></url>" for p in pages]+[f"  <url><loc>{brand['domain']}/404.html</loc></url>"])
(root/'sitemap.xml').write_text(f"<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>{urls}\n</urlset>")
(root/'robots.txt').write_text("User-agent: *\nAllow: /\nSitemap: https://orbitalu.com/sitemap.xml\n")
(root/'content/pages.json').write_text(json.dumps(pages,indent=2))
print(f'Generated {len(pages)} pages')
