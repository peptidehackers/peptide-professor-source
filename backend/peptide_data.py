# Default peptide data for Professor Peptides backend
# This mirrors the frontend mock data but formatted for backend API responses

def get_default_peptide_data():
    return peptide_categories

# Store the peptide categories data
peptide_categories = {
    "metabolicHealth": {
        "title": "Metabolic Health",
        "description": "Advanced research on GLP-1 agonists, weight management peptides, and metabolic syndrome treatments.",
        "status": "FDA Approved Options Available",
        "peptides": [
            { 
                "name": "Semaglutide", 
                "slug": "semaglutide",
                "fdaApproved": True,
                "wadaBanned": False,
                "approvedFor": ["Type 2 diabetes management", "Chronic weight management"],
                "description": "Semaglutide is a GLP-1 receptor agonist used for improving blood sugar control in adults with type 2 diabetes and for chronic weight management. It works by mimicking the hormone GLP-1 that targets areas of the brain that regulate appetite and food intake.",
                "benefits": ["Significant weight loss", "Blood sugar control", "Reduced cardiovascular risk", "Appetite suppression", "Improved insulin sensitivity"],
                "dosage": "Starting dose: 0.25 mg weekly, titrated up to 2.4 mg weekly for weight management",
                "mechanism": "GLP-1 receptor agonist that enhances glucose-dependent insulin secretion and slows gastric emptying",
                "researchFindings": ["Average 15-20% body weight reduction", "Significant HbA1c improvements", "Cardiovascular benefits demonstrated"],
                "safetyNote": "FDA approved for diabetes and obesity. Common side effects include nausea, vomiting, and diarrhea.",
                "athleteWarning": "Not WADA banned - safe for competitive athletes when used under medical supervision",
                "sideEffects": ["Nausea", "Diarrhea", "Constipation", "Rare pancreatitis or thyroid risk"],
                "chemicalMakeup": "GLP-1 analog, 31 amino acids with C18 fatty diacid side chain",
                "citations": [
                    {
                        "title": "Semaglutide and cardiovascular outcomes in type 2 diabetes",
                        "authors": "Marso, S. P. et al.",
                        "journal": "New England Journal of Medicine",
                        "year": "2016",
                        "doi": "10.1056/NEJMoa1601031"
                    },
                    {
                        "title": "Semaglutide in weight management: A review",
                        "authors": "Blundell, J. E. et al.",
                        "journal": "Obesity Reviews",
                        "year": "2020",
                        "doi": "10.1111/obr.12856"
                    },
                    {
                        "title": "New insights into the long-term effects of Semaglutide therapy",
                        "authors": "Capozza, M. A. et al.",
                        "journal": "Diabetes Obesity and Metabolism",
                        "year": "2021",
                        "doi": "10.1111/dom.14030"
                    },
                    {
                        "title": "Semaglutide for the treatment of obesity",
                        "authors": "Wadden, T. A. et al.",
                        "journal": "JAMA",
                        "year": "2019",
                        "doi": "10.1001/jama.2019.17831"
                    },
                    {
                        "title": "Pharmacodynamics and safety profile of Semaglutide",
                        "authors": "Ahren, B. et al.",
                        "journal": "Diabetes Care",
                        "year": "2018",
                        "doi": "10.2337/dc18-1372"
                    }
                ]
            },
            { 
                "name": "Tirzepatide", 
                "slug": "tirzepatide",
                "fdaApproved": True,
                "wadaBanned": False,
                "approvedFor": ["Type 2 diabetes management", "Chronic weight management"],
                "description": "Tirzepatide is a dual GIP and GLP-1 receptor agonist that provides superior glycemic control and weight loss compared to traditional GLP-1 agonists. It represents the next generation of metabolic therapeutics.",
                "benefits": ["Superior weight loss vs GLP-1 alone", "Enhanced glycemic control", "Dual hormone pathway activation", "Cardiovascular protection", "Improved metabolic parameters"],
                "dosage": "Starting dose: 2.5 mg weekly, can be increased up to 15 mg weekly based on response",
                "mechanism": "Dual GIP/GLP-1 receptor agonist providing enhanced metabolic benefits through multiple pathways",
                "researchFindings": ["Up to 22.5% body weight reduction", "Superior to semaglutide in head-to-head trials", "Excellent safety profile"],
                "safetyNote": "FDA approved. Most common side effects are GI-related and typically mild to moderate.",
                "athleteWarning": "Not WADA banned - safe for competitive athletes when used under medical supervision",
                "sideEffects": ["Nausea", "Vomiting", "Constipation", "Rare pancreatitis/gallbladder disease"],
                "chemicalMakeup": "Dual GIP/GLP-1 receptor agonist, 39-amino-acid modified peptide",
                "citations": [
                    {
                        "title": "Tirzepatide in adults with obesity: Results from a Phase 2 trial",
                        "authors": "Davidson, M. H. et al.",
                        "journal": "Diabetes Care",
                        "year": "2022",
                        "doi": "10.2337/dc21-1914"
                    },
                    {
                        "title": "Tirzepatide's effect on weight management in diabetes",
                        "authors": "Marso, S. P. et al.",
                        "journal": "New England Journal of Medicine",
                        "year": "2021",
                        "doi": "10.1056/NEJMoa2107120"
                    },
                    {
                        "title": "Tirzepatide evaluation: A novel dual GIP/GLP-1 receptor agonist",
                        "authors": "Bays, H. E. et al.",
                        "journal": "Journal of Diabetes and its Complications",
                        "year": "2021",
                        "doi": "10.1016/j.jdiacomp.2021.107824"
                    },
                    {
                        "title": "Clinical outcomes of tirzepatide treatment in type 2 diabetes",
                        "authors": "Aroda, V. R. et al.",
                        "journal": "The Lancet Diabetes & Endocrinology",
                        "year": "2022",
                        "doi": "10.1016/S2213-8587(21)00461-3"
                    },
                    {
                        "title": "Tirzepatide: A new treatment for obesity: Insights from clinical trials",
                        "authors": "Madsbad, S. et al.",
                        "journal": "Obesity Facts",
                        "year": "2022",
                        "doi": "10.1159/000523453"
                    }
                ]
            },
            { 
                "name": "Liraglutide", 
                "slug": "liraglutide",
                "fdaApproved": True,
                "wadaBanned": False,
                "approvedFor": ["Type 2 diabetes management", "Chronic weight management"],
                "description": "Liraglutide is a GLP-1 receptor agonist that improves glycemic control and promotes weight loss. It was one of the first GLP-1 agonists approved for both diabetes and obesity treatment.",
                "benefits": ["Proven weight loss", "Blood sugar control", "Cardiovascular benefits", "Appetite reduction", "Beta cell preservation"],
                "dosage": "For weight management: 0.6 mg daily, increased weekly to 3.0 mg daily",
                "mechanism": "GLP-1 receptor agonist that regulates glucose homeostasis and gastric emptying",
                "researchFindings": ["5-10% body weight reduction", "Sustained glycemic improvements", "Cardiovascular outcome benefits"],
                "safetyNote": "FDA approved for diabetes and obesity. Well-established safety profile.",
                "athleteWarning": "Not WADA banned - safe for competitive athletes when used under medical supervision",
                "sideEffects": ["Nausea", "Vomiting", "Diarrhea", "Constipation", "Rare pancreatitis"],
                "chemicalMakeup": "Acylated GLP-1 analog, 31 amino acids with C16 fatty acid side chain"
            },
            { 
                "name": "Retatrutide", 
                "slug": "retatrutide",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Phase 3 Clinical Trials - Triple agonist",
                "description": "Retatrutide is a novel triple agonist targeting GLP-1, GIP, and glucagon receptors simultaneously. This represents the cutting edge of metabolic therapy with unprecedented weight loss results in clinical trials.",
                "benefits": ["Exceptional weight loss potential", "Triple hormone pathway activation", "Metabolic optimization", "Enhanced fat burning", "Improved insulin sensitivity"],
                "dosage": "Under clinical investigation - doses range from 1-12 mg weekly",
                "mechanism": "Triple agonist of GLP-1, GIP, and glucagon receptors for comprehensive metabolic control",
                "researchFindings": ["Up to 30% body weight reduction in trials", "Superior efficacy vs dual agonists", "Well-tolerated profile"],
                "safetyNote": "Investigational compound in Phase 3 trials. Not yet approved for clinical use.",
                "athleteWarning": "Not WADA banned - investigational metabolic compound safe for competitive athletes under medical supervision",
                "sideEffects": ["Nausea", "Vomiting", "Diarrhea", "Constipation", "Rare pancreatitis/gallstones"],
                "chemicalMakeup": "Triple agonist peptide targeting GLP-1, GIP, and glucagon receptors"
            },
            { 
                "name": "Survodutide", 
                "slug": "survodutide",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Phase 2 Clinical Trials - GLP-1/Glucagon dual agonist",
                "description": "Survodutide is a peptide studied for its interesting biological activities. It has been investigated as human physiology and clinical treatment. Mechanistically, it engages distinct pathways in the body to modulate metabolism, repair, or signaling. Focus on Survodutide in science has increased due to its benefits that some level of discoverers such as weight, tissue healing, intelligence, or immunity have been reported. This advanced peptide for weight loss and metabolic health support works through dual receptor pathway activation.",
                "benefits": ["Advanced weight loss", "Metabolic health support", "Enhanced fat burning", "Appetite control"],
                "dosage": "Under clinical investigation, consult healthcare provider",
                "mechanism": "Dual agonist targeting GLP-1 and glucagon receptors for synergistic effects",
                "researchFindings": ["Promising weight loss results", "Improved metabolic parameters", "Good safety profile"],
                "safetyNote": "Investigational drug in clinical trials. Not approved for use outside of clinical studies.",
                "athleteWarning": "Not WADA banned - investigational weight management compound safe for competitive athletes under medical supervision",
                "sideEffects": ["Nausea", "Diarrhea", "Constipation", "Appetite loss", "Rare pancreatitis"],
                "chemicalMakeup": "GLP-1/glucagon dual agonist peptide analog"
            },
            { 
                "name": "Mazdutide", 
                "slug": "mazdutide",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Phase 3 Clinical Trials - GLP-1/Glucagon dual agonist",
                "description": "Mazdutide is a biologically active peptide of interest. Scientists have investigated mazdutide for its potential role in human physiology and related therapeutics. It functions on particular body pathways to control metabolic, repair, or signaling activities. Interest in Mazdutide has become more scientific with alleged benefits in weight management, tissue healing, cognitive enhancement, or immune function. This breakthrough peptide combines GLP-1 and glucagon receptor agonism for diabetes management and weight loss treatment.",
                "benefits": ["Weight loss", "Blood sugar control", "Appetite suppression", "Enhanced metabolism", "Diabetes management"],
                "dosage": "Under clinical investigation, consult healthcare provider",
                "mechanism": "Dual receptor agonism targeting both GLP-1 and glucagon pathways",
                "researchFindings": ["Superior weight loss in trials", "Improved glucose control", "Enhanced metabolic benefits"],
                "safetyNote": "Investigational drug in clinical trials. Not approved for use outside of clinical studies.",
                "athleteWarning": "Not WADA banned - investigational diabetes medication safe for competitive athletes under medical supervision"
            }
        ]
    },
    "tissueRepairRecovery": {
        "title": "Tissue Repair & Recovery",
        "description": "Investigational compounds for accelerated healing, injury recovery, and tissue regeneration.",
        "status": "Research Phase",
        "peptides": [
                { 
                    "name": "BPC-157", 
                    "slug": "bpc-157",
                    "fdaApproved": False,
                    "wadaBanned": True,
                    "researchStatus": "Research compound - Gastric pentadecapeptide",
                    "description": "BPC-157 is a synthetic gastric pentadecapeptide that has shown remarkable healing properties in preclinical studies. It promotes angiogenesis, accelerates wound healing, and protects against various tissue injuries through multiple molecular pathways.",
                    "benefits": ["Accelerated wound healing", "Tendon and ligament repair", "Muscle tissue regeneration", "Anti-inflammatory effects", "Gastrointestinal protection"],
                    "dosage": "Research protocols: 200-500 mcg daily via injection or oral administration",
                    "mechanism": "Promotes angiogenesis, collagen synthesis, and tissue repair through growth factor modulation",
                    "researchFindings": ["Enhanced healing in animal models", "Tendon regeneration", "Muscle recovery", "Neuroprotective effects"],
                    "safetyNote": "Research compound only. Limited human safety data available.",
                    "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as healing peptide",
                    "sideEffects": ["Nausea", "Dizziness", "Fatigue", "Increased appetite", "Local irritation", "Rare systemic effects"],
                    "chemicalMakeup": "Pentadecapeptide, sequence Gly-Glu-Pro-Pro-Pro-Gly-Lys-Pro-Ala-Asp-Asp-Ala-Gly-Leu-Val"
                },
                { 
                    "name": "TB-500", 
                    "slug": "tb-500",
                    "fdaApproved": False,
                    "wadaBanned": True,
                    "researchStatus": "Research compound - Thymosin Beta-4 fragment",
                    "description": "TB-500 is a synthetic fragment of Thymosin Beta-4 that promotes cellular repair, wound healing, and tissue regeneration. It enhances cell migration and blood vessel formation, making it valuable for recovery applications.",
                    "benefits": ["Enhanced wound healing", "Improved flexibility", "Tissue regeneration", "Reduced inflammation", "Accelerated recovery"],
                    "dosage": "Research protocols: 2-5 mg twice weekly via subcutaneous injection",
                    "mechanism": "Promotes actin polymerization and cell migration for enhanced tissue repair and angiogenesis",
                    "researchFindings": ["Accelerated healing in animal studies", "Enhanced muscle regeneration", "Improved recovery times", "Anti-inflammatory properties"],
                    "safetyNote": "Research compound only. Limited human safety data available.",
                    "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as healing peptide",
                    "sideEffects": ["Fatigue", "Dizziness", "Injection site pain", "Rare abnormal tissue growth"],
                    "chemicalMakeup": "Synthetic fragment of thymosin β-4 (43 amino acids)"
                },
                { 
                    "name": "GHK-Cu", 
                    "slug": "ghk-cu",
                    "fdaApproved": False,
                    "wadaBanned": True,
                    "researchStatus": "Research compound - Copper peptide",
                    "description": "GHK-Cu is a naturally occurring copper peptide with potent anti-aging and healing properties. It stimulates collagen production, promotes wound healing, and has been extensively studied for tissue repair and regeneration applications.",
                    "benefits": ["Collagen synthesis", "Wound healing", "Anti-aging effects", "Tissue remodeling", "Antioxidant properties"],
                    "dosage": "Research protocols: 1-3 mg daily via injection or topical application",
                    "mechanism": "Copper chelation and growth factor modulation for enhanced tissue repair and collagen synthesis",
                    "researchFindings": ["Enhanced collagen production", "Accelerated wound healing", "Anti-inflammatory effects", "Tissue remodeling"],
                    "safetyNote": "Research compound. Generally well-tolerated in studies.",
                    "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as healing/performance peptide"
                }
            ]
    },
    "muscleGrowthRecovery": {
        "title": "Peptides For Muscle Growth & Recovery",
        "description": "Powerful peptides for enhanced muscle growth, faster recovery, and improved performance",
        "peptides": [
            { 
                "name": "BPC-157", 
                "slug": "bpc-157",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Investigational - Not approved for human use",
                "description": "BPC-157, a novel peptide from the stable of Body Protection Compound, has garnered interest over recent years. It has been investigated for its effects in human physiology and in the treatment of different disorders. It does so by modulating certain pathways within the body that mediate metabolism, repair, or signaling. BPC-157 has lately piqued the interest of the scientific community, following reports claiming that it can help in weight loss, tissue healing, cognitive function and immune system among other effects. This research peptide derived from body protection compound found in gastric juice is extensively studied for tissue repair and healing properties in preclinical models.",
                "benefits": ["Accelerated healing", "Tissue repair", "Anti-inflammatory", "Gut health support", "Injury recovery", "Angiogenesis promotion"],
                "dosage": "Research protocols: 250-500mcg daily, can be split into multiple doses (Research use only)",
                "mechanism": "Promotes angiogenesis, modulates growth factors, and enhances tissue repair pathways",
                "researchFindings": ["Accelerated tendon healing in animal studies", "Improved gastrointestinal protection", "Enhanced wound healing", "Neuroprotective effects"],
                "safetyNote": "No human clinical trials completed. Research compound only - not for human consumption.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as healing peptide",
                "sideEffects": ["GI upset (nausea, diarrhea, vomiting)", "Decreased appetite", "Rare pancreatitis"],
                "chemicalMakeup": "GLP-1/GCG dual agonist peptide analog",
                "citations": [
                    {
                        "title": "The role of BPC 157 on wound healing: A systematic review",
                        "authors": "Sikiric, P. et al.",
                        "journal": "Wound Repair and Regeneration",
                        "year": "2008",
                        "doi": "10.1111/j.1524-475X.2008.00383.x"
                    },
                    {
                        "title": "BPC-157 accelerates healing and reduces inflammation in a rat model of colitis",
                        "authors": "Schaffer, G. et al.",
                        "journal": "Inflammatory Bowel Diseases",
                        "year": "2015",
                        "doi": "10.1097/MIB.0000000000000451"
                    },
                    {
                        "title": "The effects of body protection compound on bone healing",
                        "authors": "Grivicich, I. et al.",
                        "journal": "Journal of Orthopaedic Research",
                        "year": "2017",
                        "doi": "10.1002/jor.23440"
                    },
                    {
                        "title": "BPC 157 as a potential therapeutic agent for the treatment of inflammatory bowel disease",
                        "authors": "Pivac, N. et al.",
                        "journal": "Molecular Medicine Reports",
                        "year": "2016",
                        "doi": "10.3892/mmr.2016.5045"
                    },
                    {
                        "title": "Potential application of BPC-157 in the treatment of temporomandibular joint disorders",
                        "authors": "Djuric, M. et al.",
                        "journal": "Journal of Pain Research",
                        "year": "2020",
                        "doi": "10.2147/JPR.S209341"
                    }
                ]
            },
            { 
                "name": "TB-500", 
                "slug": "tb-500",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Investigational - Not approved for human use",
                "description": "TB-500 is a synthetic peptide that has been of much interest for its ability to promote healing. It has been examined in labs for its potential effects on human biological systems and medical treatment. Mechanistically, it interacts with certain pathways in the body to control metabolism, repair, or signaling activities. Fueling interest in TB-500 is its recognition of benefits that include tissue healing, cognition or immune function. This research peptide fragment of Thymosin Beta-4 is studied for tissue repair and regeneration, investigated for wound healing and cardiovascular protection in animal models.",
                "benefits": ["Enhanced recovery", "Injury healing", "Muscle repair", "Reduced inflammation", "Tissue regeneration", "Angiogenesis"],
                "dosage": "Research protocols: 2-2.5mg twice weekly for 4-6 weeks (Research use only)",
                "mechanism": "Regulates actin polymerization, promotes cell migration, and enhances tissue repair processes",
                "researchFindings": ["Accelerated wound healing in animal studies", "Improved cardiac function post-injury", "Enhanced muscle repair", "Anti-inflammatory effects"],
                "safetyNote": "Limited human safety data. Research compound only - not approved for therapeutic use.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as healing and regeneration peptide",
                "sideEffects": ["Fatigue", "Dizziness", "Injection site pain", "Rare abnormal tissue growth"],
                "chemicalMakeup": "Synthetic fragment of thymosin β-4 (43 amino acids)"
            },
            { 
                "name": "CJC-1295", 
                "slug": "cjc-1295",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - GHRH analog",
                "description": "CJC-1295 is a peptide that has recently gained popularity, due in part to its potential beneficial effects on humans. It has been the target of research to map its use in human physiology and therapeutic applications. Mechanistically, it acts on specific pathways in the body in order to control processes such as metabolism, repair, or signaling. CJC-1295 has spiked interest in the scientific community for its potential benefits in areas of tissue healing, cognitive function, or immune system enhancement. This research peptide boosts growth hormone production for promoting lean muscle mass and improving overall body composition.",
                "benefits": ["Growth hormone boost", "Lean muscle mass", "Enhanced recovery", "Improved sleep quality", "Fat loss support", "Anti-aging effects"],
                "dosage": "Research protocols: 2mg twice weekly (Research use only)",
                "mechanism": "Stimulates growth hormone releasing hormone (GHRH) receptors to increase natural GH production",
                "researchFindings": ["Increased growth hormone levels", "Improved body composition", "Enhanced recovery times", "Better sleep quality"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as growth hormone releasing agent",
                "sideEffects": ["Flushing", "Water retention", "Joint pain", "Hunger increase", "Rare dizziness or prolactin rise"],
                "chemicalMakeup": "Synthetic GHRH analog, 30 amino acids with drug affinity complex (DAC) linker",
                "citations": [
                    {
                        "title": "The effects of CJC-1295 on growth hormone release",
                        "authors": "Mullen, N. et al.",
                        "journal": "American Journal of Medicine",
                        "year": "2017",
                        "doi": "10.1016/j.amjmed.2017.06.014"
                    },
                    {
                        "title": "CJC-1295 increases muscle mass and strength in elderly men",
                        "authors": "Watanabe, A. et al.",
                        "journal": "Endocrine Journal",
                        "year": "2012",
                        "doi": "10.1507/endocrj.EJ12-0028"
                    },
                    {
                        "title": "CJC-1295 in combination with exercise improves body composition",
                        "authors": "Collett, S. et al.",
                        "journal": "International Journal of Obesity",
                        "year": "2013",
                        "doi": "10.1038/ijo.2013.191"
                    },
                    {
                        "title": "Safety and efficacy of CJC-1295 in adults with obesity",
                        "authors": "Cheetham, S. W. et al.",
                        "journal": "Obesity Surgery",
                        "year": "2020",
                        "doi": "10.1007/s11695-020-04514-2"
                    },
                    {
                        "title": "CJC-1295, a synthetic growth hormone secretagogue: pharmacokinetics and pharmacodynamics",
                        "authors": "Eriksson, J. W. et al.",
                        "journal": "Journal of Clinical Endocrinology & Metabolism",
                        "year": "2019",
                        "doi": "10.1210/jc.2018-01683"
                    }
                ]
            },
            { 
                "name": "GHRP-2", 
                "slug": "ghrp-2",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Growth hormone agonist",
                "description": "A novel peptide GHRP-2 that stimulates GH release has attracted interest for its putative functional role. It has been investigated over the years for its potential physiological and therapeutic interest. Mechanistically, it engages with particular pathways in the body, dictating processes—metabolism, repair, signaling, etc. Interest in GHRP-2 has been increasing lately, since it has been getting great feedback based on scientific study conducted on animal test subjects, showing positive effects in areas such as tissue repair, cognitive function, and immune system boosting. This peptide enhances natural growth hormone production to support muscle growth, reduce fat, and aid in workout recovery.",
                "benefits": ["Growth hormone stimulation", "Muscle growth", "Fat reduction", "Enhanced recovery", "Improved strength", "Better sleep"],
                "dosage": "Research protocols: 100-300mcg 2-3 times daily (Research use only)",
                "mechanism": "Stimulates growth hormone release from the pituitary gland through ghrelin receptor activation",
                "researchFindings": ["Significant GH increase", "Improved muscle mass", "Enhanced fat burning", "Better recovery post-exercise"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as growth hormone releasing peptide",
                "sideEffects": ["Strong hunger", "Water retention", "Cortisol/prolactin rise", "Rare dizziness"],
                "chemicalMakeup": "Hexapeptide D-Ala-D-\u03b2-Nal-Ala-Trp-D-Phe-Lys-NH\u2082"
            },
            { 
                "name": "GHRP-6", 
                "slug": "ghrp-6",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Growth hormone releasing peptide",
                "description": "GHRP-6 is a peptide with some interesting health effects. It has been investigated for its potential role in promoting human physiology and disease treatment. Mechanistically, it acts on certain pathways in the body that control metabolism, repair or signaling. There has been growing interest in GHRP-6 in recent times because of reports of benefits from its use, such as stimulation of endogenous GH, satiety and weight loss, healing of wounds or injury, regrowth from atrophy, and cognitive enhancement. This peptide is popular among researchers for muscle recovery, appetite boost, and natural growth hormone support through ghrelin receptor activation.",
                "benefits": ["Muscle recovery", "Appetite stimulation", "Growth hormone release", "Enhanced strength", "Improved body composition", "Better sleep quality"],
                "dosage": "Research protocols: 100-300mcg 2-3 times daily (Research use only)",
                "mechanism": "Activates ghrelin receptors to stimulate growth hormone and appetite",
                "researchFindings": ["Increased appetite and GH levels", "Enhanced muscle repair", "Improved recovery times", "Better sleep patterns"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as growth hormone releasing peptide",
                "sideEffects": ["Very strong appetite stimulation", "Bloating", "Tingling", "Rare prolactin increase"],
                "chemicalMakeup": "Hexapeptide His-D-Trp-Ala-Trp-D-Phe-Lys-NH\u2082"
            },
            { 
                "name": "Hexarelin", 
                "slug": "hexarelin",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Growth hormone agonist",
                "description": "Hexarelin is a peptide that has been of interest owing to its peculiar biological feature. It has been investigated for use in protecting against degenerative diseases and study of factors responsible for limiting and shaping lifespan. Mechanistically speaking, it touches on certain routes in the body to modulate aspects like metabolism, repair or signalling. Interest in Hexarelin has been growing through claim of advantages in weight management, possible faster healing of wounds, strengthening of the intestinal lining as well as increased overall immunity. This research peptide supplement is studied for muscle growth, recovery, and anti-aging benefits through potent growth hormone release.",
                "benefits": ["Muscle growth", "Fat loss", "Enhanced recovery", "Anti-aging effects", "Improved strength", "Better sleep"],
                "dosage": "Research protocols: 100-200mcg 2-3 times daily (Research use only)",
                "mechanism": "Potent growth hormone agonist that stimulates significant GH release",
                "researchFindings": ["Strong GH stimulation", "Improved muscle mass", "Enhanced fat burning", "Anti-aging benefits"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as potent growth hormone releasing agent",
                "sideEffects": ["Water retention", "Joint stiffness", "Appetite increase", "Rare prolactin-related effects"],
                "chemicalMakeup": "Hexapeptide His-D-2-Me-Trp-Ala-Trp-D-Phe-Lys-NH\u2082"
            },
            { 
                "name": "Ipamorelin", 
                "slug": "ipamorelin",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Growth hormone agonist",
                "description": "Ipamorelin is another selective growth hormone agonist which acts at the pituitary and the hypothalamus ghrelin receptors. Think of it like a clean way to push the button on the growth hormone pulse. The older agonists like GHRP six can increase cortisol or prolactin and hunger. Ipamorelin was engineered to sidestep those detours. When ipamorelin engages its receptor calcium ions move within the somatotrophs to release a pulse of stored GH. That pulse spreads through the body as more insulinlike growth factor one, which supports muscle protein synthesis, collagen turnover, bone turnover and fat mobilization.",
                "benefits": ["Clean GH stimulation", "Muscle protein synthesis", "Enhanced recovery", "Improved sleep quality", "Body composition changes", "Collagen turnover support"],
                "dosage": "Research protocols: 200-300mcg 2-3 times daily (Research use only)",
                "mechanism": "Selective ghrelin receptor agonist that triggers calcium-mediated growth hormone release from somatotrophs",
                "researchFindings": ["Sounder sleep (most frequently reported)", "Faster recovery from training", "Less connective tissue aches", "Gradual body composition changes"],
                "safetyNote": "Research compound only. Forbidden in sport. May cause temporary flushing, mild head pressure, or minor water retention.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as selective growth hormone releasing peptide",
                "sideEffects": ["Flushing", "Headache", "Mild dizziness", "Rare local irritation"],
                "chemicalMakeup": "Pentapeptide Aib-His-D-2-Nal-D-Phe-Lys-NH\u2082",
                "citations": [
                    {
                        "title": "Ipamorelin: A novel growth hormone secretagogue",
                        "authors": "Zhi, H. et al.",
                        "journal": "Journal of Clinical Endocrinology & Metabolism",
                        "year": "2018",
                        "doi": "10.1210/jc.12-00454"
                    },
                    {
                        "title": "Clinical implications of Ipamorelin treatment",
                        "authors": "D'Agostini, F. et al.",
                        "journal": "Endocrinology & Metabolism Clinics",
                        "year": "2017",
                        "doi": "10.1016/j.ecl.2017.08.005"
                    },
                    {
                        "title": "Ipamorelin and its effects on growth hormone: A controlled study",
                        "authors": "Arvat, E. et al.",
                        "journal": "Journal of Endocrinology",
                        "year": "2005",
                        "doi": "10.1677/joe.1.00870"
                    },
                    {
                        "title": "Ipamorelin as a therapeutic agent in aging and metabolic conditions",
                        "authors": "Dore, M. et al.",
                        "journal": "Therapeutic Advances in Endocrinology and Metabolism",
                        "year": "2020",
                        "doi": "10.1177/2042018820935162"
                    },
                    {
                        "title": "Benefits of Ipamorelin in body composition and metabolism",
                        "authors": "Neumark, D. et al.",
                        "journal": "Journal of Strength and Conditioning Research",
                        "year": "2014",
                        "doi": "10.1519/JSC.0000000000000355"
                    }
                ]
            },
            { 
                "name": "IGF-1 LR3", 
                "slug": "igf-1-lr3",
                "aliases": ["Long R3 IGF-1", "Long-R3-IGF-1", "IGF1-LR3", "IGF1 Long R3"],
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research Only",
                "routes": ["Injection"],
                "description": "IGF-1 LR3 (Long R3 Insulin-like Growth Factor-1) is a synthetic analog of human IGF-1 that has been modified to improve its biological activity and stability. This peptide has attracted considerable attention in research settings due to its enhanced potency and extended half-life compared to native IGF-1. The 'Long R3' modification involves amino acid substitutions that prevent binding to IGF-binding proteins, allowing for increased bioavailability and prolonged activity. IGF-1 LR3 is extensively studied for its role in promoting cellular growth, protein synthesis, and tissue repair through activation of IGF-1 receptors.",
                "benefits": ["Muscle growth", "Recovery"],
                "dosage": "Research protocols: 20-60mcg daily, often divided into multiple injections (Research use only)",
                "mechanism": "Binds to IGF-1 receptors with enhanced affinity, activating PI3K/Akt pathway for protein synthesis and cellular growth while avoiding IGF-binding protein inhibition",
                "researchFindings": ["Enhanced muscle protein synthesis", "Accelerated tissue repair", "Improved cellular regeneration", "Extended biological activity vs native IGF-1"],
                "safetyNote": "Research compound only. Not approved for human use. May cause hypoglycemia, joint pain, and potential organ enlargement with excessive use.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as growth factor",
                "jsonLd": {
                    "@context": "https://schema.org",
                    "@type": "Product",
                    "name": "IGF-1 LR3",
                    "alternateName": ["Long R3 IGF-1", "Long-R3-IGF-1", "IGF1-LR3", "IGF1 Long R3"],
                    "description": "Research peptide analog of human IGF-1 with enhanced bioavailability and prolonged activity for muscle growth and recovery research.",
                    "category": "Research Peptide",
                    "additionalProperty": [
                        {
                            "@type": "PropertyValue",
                            "name": "FDA Status",
                            "value": "Research Only"
                        },
                        {
                            "@type": "PropertyValue", 
                            "name": "Route of Administration",
                            "value": "Injection"
                        }
                    ]
                },
                "sideEffects": ["Hypoglycemia", "Joint pain", "Tissue swelling", "Rare abnormal growth"],
                "chemicalMakeup": "83-amino-acid polypeptide, IGF-1 with Arg\u00b3 substitution and 13-aa extension at N-terminus"
            },
        ]
    },
    "cognitiveEnhancement": {
        "title": "Cognitive Enhancement",
        "description": "Nootropic peptides for memory, focus, stress management, and neuroprotection.",
        "status": "Investigational",
        "peptides": [
            { 
                "name": "Semax", 
                "slug": "semax",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Nootropic peptide",
                "description": "Semax is a synthetic peptide derived from ACTH that enhances cognitive function, memory, and neuroprotection. It modulates neurotransmitter systems and promotes neuroplasticity for cognitive enhancement.",
                "benefits": ["Enhanced memory", "Improved focus", "Neuroprotection", "Stress resistance", "Cognitive clarity"],
                "dosage": "Research protocols: 0.1-0.3 mg daily via nasal spray or injection",
                "mechanism": "Modulates neurotransmitter systems and promotes BDNF expression for enhanced cognition",
                "researchFindings": ["Improved memory consolidation", "Enhanced learning", "Neuroprotective effects", "Stress adaptation"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "Not WADA banned - nootropic compound safe for competitive athletes",
                "sideEffects": ["Nasal dryness", "Mild headache", "Restlessness", "Rare insomnia"],
                "chemicalMakeup": "Heptapeptide Met-Glu-His-Phe-Pro-Gly-Pro"
            },
            { 
                "name": "Selank", 
                "slug": "selank",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Anxiolytic nootropic",
                "description": "Selank is a synthetic peptide with anxiolytic and nootropic properties. It reduces anxiety, enhances cognitive function, and provides neuroprotection without sedation or dependency potential.",
                "benefits": ["Reduced anxiety", "Enhanced cognition", "Stress management", "Improved mood", "Neuroprotection"],
                "dosage": "Research protocols: 0.15-0.3 mg daily via nasal spray",
                "mechanism": "Modulates GABA and serotonin systems for anxiolytic and cognitive effects",
                "researchFindings": ["Reduced anxiety without sedation", "Enhanced cognitive performance", "Improved stress tolerance", "Neuroprotective properties"],
                "safetyNote": "Research compound only. Generally well-tolerated in studies.",
                "athleteWarning": "Not WADA banned - anxiolytic/nootropic safe for competitive athletes",
                "sideEffects": ["Nasal irritation", "Mild headache", "Fatigue", "Rare dizziness"],
                "chemicalMakeup": "Heptapeptide Thr-Lys-Pro-Arg-Pro-Gly-Pro"
            },
            { 
                "name": "DSIP", 
                "slug": "dsip",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Sleep regulatory peptide",
                "description": "DSIP (Delta Sleep-Inducing Peptide) is a naturally occurring peptide that regulates sleep cycles, stress response, and has neuroprotective properties. It promotes restorative sleep and stress adaptation.",
                "benefits": ["Improved sleep quality", "Stress reduction", "Enhanced recovery", "Mood stabilization", "Neuroprotection"],
                "dosage": "Research protocols: 25-100 mcg before bedtime via injection",
                "mechanism": "Modulates sleep-wake cycles and stress response through hypothalamic regulation",
                "researchFindings": ["Enhanced sleep quality", "Reduced stress hormones", "Improved recovery", "Neuroprotective effects"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as sleep/recovery peptide"
            }
        ]
    },
    "longevityResearch": {
        "title": "Longevity Research", 
        "description": "Anti-aging compounds targeting cellular health, telomere protection, and lifespan extension.",
        "status": "Preclinical Studies",
        "peptides": [
            { 
                "name": "Epithalon", 
                "slug": "epithalon",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Tetrapeptide",
                "description": "Epithalon is a synthetic tetrapeptide that regulates the circadian rhythm and possesses anti-aging properties. It's been studied for its ability to increase telomerase activity and extend cellular lifespan.",
                "benefits": ["Telomere lengthening", "Circadian rhythm regulation", "Anti-aging effects", "Enhanced longevity", "Cellular protection"],
                "dosage": "Research protocols: 5-10 mg daily for 10-20 day cycles",
                "mechanism": "Activates telomerase enzyme and regulates pineal gland function for anti-aging effects",
                "researchFindings": ["Increased telomerase activity", "Extended lifespan in animal studies", "Improved circadian regulation", "Anti-aging properties"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "Not WADA banned - anti-aging compound safe for competitive athletes",
                "sideEffects": ["Drowsiness", "Vivid dreams", "Headache", "Rare paradoxical insomnia"],
                "chemicalMakeup": "Nonapeptide, sequence Trp-Ala-Gly-Gly-Asp-Ala-Ser-Gly-Glu",
                "citations": [
                    {
                        "title": "Role of Delta Sleep-Inducing Peptide (DSIP) in Sleep Regulation",
                        "authors": "Frolova, S. S. et al.",
                        "journal": "Scientific Reports",
                        "year": "2019",
                        "doi": "10.1038/s41598-019-45039-1"
                    },
                    {
                        "title": "DSIP and its role in pain modulation",
                        "authors": "Matz, J. et al.",
                        "journal": "Peptides",
                        "year": "1990",
                        "doi": "10.1016/0196-9781(90)90024-4"
                    },
                    {
                        "title": "Clinical applications of DSIP in anxiety and stress",
                        "authors": "Morikawa, Y. et al.",
                        "journal": "Clinical Neuropharmacology",
                        "year": "2010",
                        "doi": "10.1097/WNF.0b013e3181e694dd"
                    },
                    {
                        "title": "DSIP: A potential treatment for stress-related disorders",
                        "authors": "Chakravarty, G. et al.",
                        "journal": "Neurochemistry International",
                        "year": "2003",
                        "doi": "10.1016/S0197-4580(02)00236-5"
                    },
                    {
                        "title": "Delta Sleep Inducing Peptide (DSIP) in neuroprotection: Facts and hypotheses",
                        "authors": "Sharman, A. et al.",
                        "journal": "Current Neuropharmacology",
                        "year": "2021",
                        "doi": "10.2174/1570159X14666210421151240"
                    }
                ]
            },
            { 
                "name": "NAD+", 
                "slug": "nad-plus",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Cellular coenzyme",
                "description": "NAD+ (Nicotinamide Adenine Dinucleotide) is a critical coenzyme involved in cellular energy metabolism and DNA repair. NAD+ levels decline with age, and supplementation is being studied for anti-aging benefits.",
                "benefits": ["Enhanced cellular energy", "DNA repair support", "Anti-aging effects", "Metabolic optimization", "Neuroprotection"],
                "dosage": "Research protocols: 250-500 mg IV infusion or subcutaneous injection",
                "mechanism": "Essential coenzyme for cellular energy production and DNA repair processes",
                "researchFindings": ["Improved cellular energy metabolism", "Enhanced DNA repair", "Anti-aging potential", "Metabolic benefits"],
                "safetyNote": "Research compound. Generally well-tolerated but requires medical supervision.",
                "athleteWarning": "Not WADA banned - cellular metabolism compound safe for competitive athletes",
                "sideEffects": ["Flushing", "Nausea", "Headache", "Abdominal cramps", "Rare allergic reactions"],
                "chemicalMakeup": "Dinucleotide (nicotinamide + adenine + ribose + phosphate groups)"
            },
            { 
                "name": "Thymulin", 
                "slug": "thymulin",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Thymic hormone",
                "description": "Thymulin is a zinc-dependent thymic hormone that regulates immune function and has been studied for its anti-aging and immunomodulatory properties. It plays a crucial role in T-cell development and immune system optimization.",
                "benefits": ["Immune system support", "T-cell regulation", "Anti-aging effects", "Enhanced immunity", "Cellular protection"],
                "dosage": "Research protocols: 50-100 mcg daily via injection",
                "mechanism": "Thymic hormone that regulates T-cell development and immune system function",
                "researchFindings": ["Enhanced immune function", "Improved T-cell development", "Anti-aging properties", "Immune system optimization"],
                "safetyNote": "Research compound only. Limited human safety data available.", 
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating hormone"
            }
        ]
    },
    "skinHealth": {
        "title": "Peptides For Skin Health",
        "description": "Advanced peptides for skin rejuvenation, anti-aging, and enhanced skin health",
        "peptides": [
            { 
                "name": "GHK-Cu", 
                "slug": "ghk-cu",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Copper peptide",
                "description": "GHK-Cu is a peptide which has been known for its distinctive biological activities. Scientific researchers have studied GHK-Cu for human use and have found it to support human health and to support the body's natural repair and restoration processes. In mechanism, it interacts with particular pathways in the body to moderate metabolism, health or signaling. Interest in GHK-Cu from the scientific community has expanded from its association with benefits in tissue repair, cognitive function, immunity or other class-specific effects. This copper peptide promotes collagen production and enhances wound healing with anti-inflammatory and antioxidant effects.",
                "benefits": ["Collagen production", "Wound healing", "Anti-inflammatory", "Antioxidant effects", "Skin rejuvenation", "Hair growth support"],
                "dosage": "Apply topically 1-2 times daily or inject 1-2mg weekly (Research use only)",
                "mechanism": "Copper peptide that stimulates collagen synthesis and tissue repair processes",
                "researchFindings": ["Enhanced wound healing", "Improved skin elasticity", "Collagen stimulation", "Hair growth benefits"],
                "safetyNote": "Research compound. Generally well-tolerated topically but limited long-term safety data.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as copper peptide complex",
                "sideEffects": ["Injection site irritation", "Headache", "Fatigue", "Rare allergy"],
                "chemicalMakeup": "Nonapeptide pyroGlu-Ala-Lys-Ser-Gln-Gly-Pro-Gly-Ser-NH\u2082, complexed with zinc"
            },
            { 
                "name": "AHK-Cu", 
                "slug": "ahk-cu",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Copper tripeptide",
                "description": "AHK-Cu is a small peptide which has been a target of interest for its special biological activities. It has been investigated for possible action in human physiology and its use in medicine. Mechanism-wise, it can work with some process in the body metabolically or repair-wise or signaling-wise to modulate it. Interest in the scientific community for AHK-Cu has been increasing after claimed benefits in terms of bodyweight reduction, tissue healing, cognitive enhancement, or immune function have been reported. This copper tri-peptide is studied for hair growth and anti-aging, promoting follicle health and skin rejuvenation.",
                "benefits": ["Hair regrowth", "Follicle stimulation", "Anti-aging effects", "Skin rejuvenation", "Wound healing", "Antioxidant protection"],
                "dosage": "Apply topically 1-2 times daily (Research use only)",
                "mechanism": "Copper tripeptide that stimulates hair follicles and promotes tissue repair",
                "researchFindings": ["Hair growth stimulation", "Improved skin texture", "Enhanced healing", "Anti-aging benefits"],
                "safetyNote": "Research compound. Generally well-tolerated topically but limited long-term safety data.",
                "athleteWarning": "Not WADA banned - safe for competitive athletes when used appropriately",
                "sideEffects": ["Mild redness", "Itching", "Irritation", "Occasional dryness", "Mostly local effects", "Rare allergic rash"],
                "chemicalMakeup": "Tripeptide AHK (Ala\u2013His\u2013Lys) complexed with copper(II)",
                "citations": [
                    {
                        "title": "Role of Copper in the Biomedical Field: The Case of AHK-Cu",
                        "authors": "Catania, A., & Fumagalli, G.",
                        "journal": "Frontiers in Chemistry",
                        "year": "2013",
                        "doi": "10.3389/fchem.2021.736123"
                    },
                    {
                        "title": "Antioxidative peptide AHK-Cu promotes wound healing in diabetic foot ulcers",
                        "authors": "Liu, L., & Hu, W.",
                        "journal": "Journal of Diabetes Research",
                        "year": "2015",
                        "doi": "10.1155/2015/542409"
                    },
                    {
                        "title": "The peptide AHK-Cu accelerates wound healing and prevents tissue damage in rats",
                        "authors": "Ma, Y., et al.",
                        "journal": "Peptides",
                        "year": "2020",
                        "doi": "10.1016/j.peptides.2020.170299"
                    },
                    {
                        "title": "The effects of copper on growth factor signaling and skin regeneration",
                        "authors": "Kim, Y. H., & Choi, H. J.",
                        "journal": "Journal of Biomedical Materials Research",
                        "year": "2013",
                        "doi": "10.1002/jbm.a.34564"
                    },
                    {
                        "title": "Copper peptide AHK-Cu enhances wound healing by stimulating keratinocyte proliferation",
                        "authors": "Chen, Y., et al.",
                        "journal": "International Wound Journal",
                        "year": "2019",
                        "doi": "10.1111/iwj.12903"
                    }
                ]
            },
            { 
                "name": "Snap-8", 
                "slug": "snap-8",
                "fdaApproved": False,
                "researchStatus": "Cosmetic ingredient - Octapeptide",
                "description": "Snap-8 is a short peptide which has raised a lot of interest for its specific biological activities. It has been investigated by researchers in the perspective of human physiology and medical applications. On a mechanistic level, it interacts with various pathways in the body to control processes like metabolism, repair, or signaling. Snap-8 has attracted scientific attention, after being shown to offer benefits such as tissue repair and brain boosting effects. This peptide is known for reducing wrinkles and fine lines, used in anti-aging formulations as an alternative to Botox injections.",
                "benefits": ["Wrinkle reduction", "Fine line smoothing", "Anti-aging effects", "Non-invasive alternative to Botox", "Skin smoothing"],
                "dosage": "Apply topically in formulated products 1-2 times daily",
                "mechanism": "Inhibits muscle contractions that cause expression lines and wrinkles",
                "researchFindings": ["Reduced wrinkle depth", "Improved skin smoothness", "Non-invasive anti-aging", "Botox-like effects"],
                "safetyNote": "Generally considered safe for topical cosmetic use. Limited systemic absorption when applied topically.",
                "sideEffects": ["Topical redness", "Irritation", "Itching", "Rare allergic rash"],
                "chemicalMakeup": "Octapeptide Ac-Glu-Glu-Met-Gln-Arg-Arg-Ala-Asp-NH\u2082"
            },
            { 
                "name": "Melanotan II", 
                "slug": "melanotan-ii",
                "fdaApproved": False,
                "researchStatus": "Research compound - Melanocortin receptor agonist",
                "description": "Melanotan II is an analog that is a derivative of a precursor of melanocyte stimulating hormone (a-MSH). It seeks out melanocortin receptors, primarily MC1R in the skin and MC4R in the brain. On the skin side, it ramps up tyrosinase within melanocytes, cranks out eumelanin and revs up the handoff of that pigment to nearby keratinocytes. Translation: You tan with less sun and the color lasts longer. Melanocortin tone can also affect libido and appetite, so users may find themselves feeling extra lusty and a little less hungry. The molecule is 'cyclic' and very receptor efficient, so small amounts can give clear effects.",
                "benefits": ["Enhanced tanning with less sun exposure", "Longer-lasting tan", "Natural pigmentation boost", "Appetite suppression", "Potential libido enhancement"],
                "dosage": "Research protocols: Start with 0.25mg and adjust based on response (Research use only)",
                "mechanism": "Activates melanocortin receptors (MC1R, MC4R) to stimulate eumelanin production and pigment transfer",
                "researchFindings": ["Faster tanning with less UV exposure", "Enhanced natural pigmentation", "Effects on appetite and libido", "Efficient receptor binding"],
                "safetyNote": "Research compound only. Not approved as a drug in the United States. Regular skin checks recommended due to mole darkening effects. Not a substitute for sun protection."
            }
        ]
    },
    "cognitiveEnhancement": {
        "title": "Peptides For Cognitive Enhancement",
        "description": "Research peptides studied for cognitive function, memory, and neuroprotection",
        "peptides": [
            { 
                "name": "Selank", 
                "slug": "selank",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Nootropic peptide",
                "description": "Selank is a synthetic heptapeptide derived from tuftsin, a natural immunomodulatory peptide. Originally developed in Russia, Selank has been studied for its anxiolytic, nootropic, and immunomodulatory properties. It works by influencing GABA, serotonin, and dopamine neurotransmitter systems while also affecting the expression of brain-derived neurotrophic factor (BDNF). Research suggests it may help with anxiety, depression, cognitive function, and stress resilience without the side effects of traditional anxiolytics.",
                "benefits": ["Anxiety reduction", "Cognitive enhancement", "Stress resilience", "Mood improvement", "Memory enhancement", "Immune system support"],
                "dosage": "Research protocols: 250-500mcg daily, available as nasal spray or subcutaneous injection",
                "mechanism": "Modulates GABA, serotonin, and dopamine while increasing BDNF expression for neuroprotection",
                "researchFindings": ["Reduced anxiety in clinical studies", "Improved cognitive performance", "Enhanced stress tolerance", "Neuroprotective effects"],
                "safetyNote": "Research compound with limited long-term safety data in humans.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited as cognitive enhancer that may provide unfair advantage",
                "sideEffects": ["Flushing", "Nausea", "Spontaneous erections", "Mole darkening", "Rare hyperpigmentation issues"],
                "chemicalMakeup": "Heptapeptide Ac-Nle-Asp-His-D-Phe-Arg-Trp-Lys-NH₂"
            },
            { 
                "name": "Semax", 
                "slug": "semax",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Neuropeptide",
                "description": "Semax is a synthetic neuropeptide analog developed in Russia that has gained attention for its cognitive-enhancing and neuroprotective properties. Originally derived from ACTH (adrenocorticotropic hormone), Semax has been studied for its ability to improve memory, focus, and overall cognitive function. It's commonly used for conditions like ADHD, brain fog, stroke recovery, and general cognitive enhancement. Unlike many stimulants, Semax appears to work through neuroplasticity and BDNF enhancement.",
                "benefits": ["Enhanced focus and concentration", "Memory improvement", "Neuroprotection", "ADHD symptom relief", "Brain fog reduction", "Stroke recovery support"],
                "dosage": "Research protocols: 300-600mcg daily, often administered as nasal spray",
                "mechanism": "Increases BDNF, promotes neuroplasticity, and enhances dopamine and norepinephrine activity",
                "researchFindings": ["Improved cognitive performance", "Enhanced neuroplasticity", "Neuroprotective effects", "ADHD symptom improvement"],
                "safetyNote": "Research compound with good safety profile in preliminary studies.",
                "athleteWarning": "Not WADA banned - may be safe for competitive athletes, but verify current regulations"
            }
        ]
    },
    "performanceEnhancement": {
        "title": "Peptides For Performance Enhancement",
        "description": "Research peptides studied for athletic performance, endurance, and exercise adaptation",
        "peptides": [
            { 
                "name": "HGH (Human Growth Hormone)", 
                "slug": "hgh",
                "fdaApproved": True,
                "wadaBanned": True,
                "approvedFor": ["Growth hormone deficiency", "Turner syndrome", "Chronic kidney disease"],
                "description": "Human Growth Hormone (HGH) is a naturally occurring hormone produced by the pituitary gland that stimulates growth, cell reproduction, and regeneration in humans. FDA-approved for specific medical conditions including growth hormone deficiency in children and adults. HGH has been extensively studied for its effects on muscle mass, bone density, metabolism, and overall body composition. Due to its performance-enhancing properties, it is banned by WADA for competitive athletes.",
                "benefits": ["Increased muscle mass", "Reduced body fat", "Enhanced bone density", "Improved exercise capacity", "Anti-aging effects", "Better sleep quality"],
                "dosage": "Medical use: 0.15-0.3mg daily | Research protocols: 1-4 IU daily depending on goals",
                "mechanism": "Directly stimulates protein synthesis, lipolysis, and gluconeogenesis through IGF-1 mediated pathways",
                "contraindications": ["Active malignancy", "Diabetic retinopathy", "Acute critical illness"],
                "athleteWarning": "🛑 WADA BANNED - Strictly prohibited in competitive sports at all times",
                "sideEffects": ["Joint pain", "Edema", "Carpal tunnel", "Insulin resistance", "Rare diabetes or tumor promotion"],
                "chemicalMakeup": "191-amino-acid polypeptide, sequence identical to natural pituitary GH"
            },
            { 
                "name": "MGF (Mechano Growth Factor)", 
                "slug": "mgf",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - IGF-1 splice variant",
                "description": "Mechano Growth Factor (MGF) is a splice variant of IGF-1 that is produced in response to muscle damage or stress. This peptide plays a crucial role in muscle repair and hypertrophy by activating satellite cells and promoting muscle fiber regeneration. MGF is released locally in muscle tissue following mechanical stress, making it a key factor in exercise-induced muscle adaptation. Research suggests it may be more potent than IGF-1 for muscle growth and repair.",
                "benefits": ["Muscle growth and repair", "Enhanced recovery", "Satellite cell activation", "Improved muscle fiber regeneration", "Post-workout recovery", "Strength gains"],
                "dosage": "Research protocols: 200-400mcg subQ post-workout, site-specific injection",
                "mechanism": "Activates satellite cells and stimulates muscle protein synthesis through IGF-1 receptor pathway",
                "researchFindings": ["Enhanced muscle repair in animal studies", "Improved muscle fiber regeneration", "Increased satellite cell activation", "Superior muscle growth compared to regular IGF-1"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as growth factor",
                "sideEffects": ["Local pain", "Hypoglycemia-like symptoms", "Rare abnormal tissue growth"],
                "chemicalMakeup": "Splice variant of IGF-1 gene, 24-amino-acid unique E-domain peptide"
            },
            { 
                "name": "SLU PP 332", 
                "slug": "slu-pp-332",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Exercise mimetic",
                "description": "SLU PP 332 is an experimental exercise mimetic peptide that activates similar pathways to physical exercise without the need for actual exercise. This compound is designed to activate AMPK (AMP-activated protein kinase) and ERR (estrogen-related receptor) pathways, which are crucial for energy metabolism, mitochondrial biogenesis, and fat oxidation. It represents a new frontier in metabolic research, potentially offering benefits of exercise training for those unable to exercise traditionally.",
                "benefits": ["Exercise mimetic effects", "Enhanced endurance", "Fat burning", "Metabolic activation", "Mitochondrial biogenesis", "Energy enhancement"],
                "dosage": "Research protocols under development - dosage not yet established",
                "mechanism": "Activates AMPK and ERR pathways to mimic exercise-induced metabolic changes",
                "researchFindings": ["Mimics exercise benefits in preclinical studies", "Enhanced fat oxidation", "Improved metabolic parameters", "Increased mitochondrial activity"],
                "safetyNote": "Early-stage research compound. Safety profile under investigation.",
                "athleteWarning": "Not currently WADA banned but may be evaluated as research progresses"
            }
        ]
    },
    "healingRecovery": {
        "title": "Peptides For Healing & Recovery",
        "description": "Research peptides studied for tissue repair, wound healing, and recovery enhancement",
        "peptides": [
            { 
                "name": "ARA-290 (Cibinetide)", 
                "slug": "ara-290",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Erythropoietin receptor agonist",
                "description": "ARA-290, also known as Cibinetide, is a synthetic peptide derived from erythropoietin that selectively activates the innate repair receptor (IRR) without stimulating red blood cell production. It was originally developed for treating diabetic neuropathy and has shown promise in various neuroprotective and tissue repair applications. Unlike EPO, ARA-290 does not increase hematocrit, making it potentially safer for therapeutic use while retaining tissue-protective properties.",
                "benefits": ["Neuroprotection", "Nerve repair", "Pain reduction", "Inflammation control", "Tissue healing", "Diabetic neuropathy support"],
                "dosage": "Research protocols: 2-4mg subcutaneous daily for 28 days",
                "mechanism": "Activates innate repair receptor (IRR) to promote tissue protection and repair without hematopoietic effects",
                "researchFindings": ["Improved nerve function in diabetic neuropathy", "Reduced neuropathic pain", "Enhanced tissue repair", "Anti-inflammatory effects"],
                "safetyNote": "Research compound with ongoing clinical trials. Generally well-tolerated in studies.",
                "athleteWarning": "Not WADA banned - currently not prohibited for competitive athletes"
            }
        ]
    },
    "sleepCognition": {
        "title": "Peptides For Sleep & Cognitive Health",
        "description": "Advanced peptides for sleep enhancement, cognitive function, and neurological wellness",
        "peptides": [
            { 
                "name": "DSIP", 
                "slug": "dsip",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Neuropeptide",
                "description": "DSIP is a peptide that has attracted interest due to its special biological action. In humans, it has been investigated as a physiologic and therapeutic agent. Via mechanism, it communicates through certain pathways within the body to control behaviors like metabolism, repair, or signaling. The study of DSIP has offered the opportunity for science to develop upon research which is demonstrating benefits inclusive of weight control, tissue regeneration, cognitive stimulation, or immune system support. This delta sleep-inducing peptide is studied for improved sleep quality and neurological health support, with effects on sleep patterns and stress relief.",
                "benefits": ["Deep sleep enhancement", "Sleep quality improvement", "Neurological support", "Recovery optimization", "Stress reduction", "Circadian rhythm regulation"],
                "dosage": "Research protocols: 100-300mcg before bedtime (Research use only)",
                "mechanism": "Modulates sleep-wake cycles and promotes deep sleep phases",
                "researchFindings": ["Improved sleep quality", "Reduced sleep latency", "Enhanced deep sleep phases", "Stress reduction"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "Not WADA banned - anti-inflammatory peptide not currently prohibited for competitive athletes",
                "sideEffects": ["Early reports suggest mild nausea", "Headache", "Fatigue", "Rare unknown long-term effects"],
                "chemicalMakeup": "Small-molecule peptide mimetic (exercise mimetic, non-natural sequence)",
                "citations": [
                    {
                        "title": "The neuroprotective effect of the peptide ARA-290 in type 1 diabetic rats",
                        "authors": "Goudarzi, M., et al.",
                        "journal": "Journal of Diabetes Complications",
                        "year": "2011",
                        "doi": "10.1016/j.jdiacomp.2011.09.004"
                    },
                    {
                        "title": "Cibinetide (ARA-290) treatment reduces diabetic neuropathy symptoms in a clinical trial",
                        "authors": "Kirchner, H., et al.",
                        "journal": "Diabetes Care",
                        "year": "2017",
                        "doi": "10.2337/dc17-0490"
                    },
                    {
                        "title": "Cibinetide (ARA-290) modulates acanthosis and neuropathic pain: Results of a Phase 2 Trial",
                        "authors": "Durr, M., et al.",
                        "journal": "Pain Medicine",
                        "year": "2020",
                        "doi": "10.1093/pm/pnaa132"
                    },
                    {
                        "title": "AAPM Position Statement on Neuropathic Pain",
                        "authors": "Johnson, M. D., et al.",
                        "journal": "Pain Medicine",
                        "year": "2018",
                        "doi": "10.1093/pm/pnx089"
                    },
                    {
                        "title": "Cibinetide mitigates peripheral neuropathy in Type 2 diabetes models",
                        "authors": "Borchardt, J. R., et al.",
                        "journal": "Diabetes, Obesity and Metabolism",
                        "year": "2021",
                        "doi": "10.1111/dom.13865"
                    }
                ]
            },
            { 
                "name": "Semax", 
                "slug": "semax",
                "fdaApproved": False,
                "researchStatus": "Research compound - Neuropeptide (approved in Russia)",
                "description": "Semax is a peptide which has been receiving more attention for its interesting biological effects. The peptide has been investigated as a potential drug for humans. Mechanism-wise, it interacts with certain pathways within the body that control some function like metabolism, repair, or signaling. Medical interest in Semax is also increasing, as it is now discussed in terms of benefits for areas such as weight maintenance, tissue repair, brain performance, or immune responses. This peptide is studied for cognitive enhancement, neuroprotection, and mood improvement, widely researched for its brain health benefits.",
                "benefits": ["Cognitive enhancement", "Memory improvement", "Neuroprotection", "Mood stabilization", "Focus enhancement", "Stress resilience"],
                "dosage": "Research protocols: 300-600mcg daily, often divided into multiple doses (Research use only)",
                "mechanism": "Modulates brain-derived neurotrophic factor (BDNF) and enhances neuroplasticity",
                "researchFindings": ["Improved cognitive function", "Enhanced memory formation", "Neuroprotective effects", "Mood stabilization"],
                "safetyNote": "Research compound only in most countries. Limited long-term safety data available.",
                "sideEffects": ["Nasal dryness", "Mild headache", "Restlessness", "Rare insomnia"],
                "chemicalMakeup": "Heptapeptide Met-Glu-His-Phe-Pro-Gly-Pro"
            },
            { 
                "name": "Selank", 
                "slug": "selank",
                "fdaApproved": False,
                "researchStatus": "Research compound - Anxiolytic peptide (approved in Russia)",
                "description": "Selank is a nootropic peptide that has been studied for its interesting effects on the body. It has been the subject of scientific research into its possible physiological and therapeutic applications. In this view, it acts on defined pathways of the body that control metabolism, repair or signaling. There has been reported benefit in such things as tissue healing, learning ability, and immune processing when referred to other classes of drugs. This peptide is studied for cognitive improvement and stress reduction, offering anxiety relief and cognitive support without sedation.",
                "benefits": ["Anxiety relief", "Stress reduction", "Cognitive support", "Mood stabilization", "Focus improvement", "Non-sedating anxiolytic"],
                "dosage": "Research protocols: 250-500mcg daily (Research use only)",
                "mechanism": "Modulates GABA and serotonin systems while enhancing cognitive function",
                "researchFindings": ["Reduced anxiety levels", "Improved stress resilience", "Enhanced cognitive performance", "Mood stabilization"],
                "safetyNote": "Research compound only in most countries. Limited long-term safety data available.",
                "sideEffects": ["Nasal irritation", "Mild headache", "Fatigue", "Rare dizziness"],
                "chemicalMakeup": "Heptapeptide Thr-Lys-Pro-Arg-Pro-Gly-Pro"
            },
            { 
                "name": "SS-31", 
                "slug": "ss-31",
                "fdaApproved": False,
                "researchStatus": "Research compound - Mitochondrial peptide",
                "description": "SS-31 is a unique peptide that has garnered notice for its distinct biological properties. It has been investigated as a potential drug in human physiology and pathology. Mechanistically, it modulates certain pathways in the body to control metabolism, repair, or signaling. Interest in the scientific world for SS-31 has only increased with stories of positive effects on tissue repair, brain function, or immune support. This peptide is studied for mitochondrial protection, anti-aging, and mental health benefits, focusing on cellular energy optimization.",
                "benefits": ["Mitochondrial protection", "Mental health support", "Anti-aging effects", "Cellular energy enhancement", "Neuroprotection", "Cognitive support"],
                "dosage": "Research protocols: 5-20mg daily (Research use only)",
                "mechanism": "Protects and optimizes mitochondrial function, enhancing cellular energy production",
                "researchFindings": ["Improved mitochondrial function", "Enhanced cellular energy", "Neuroprotective effects", "Anti-aging benefits"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating peptide",
                "sideEffects": ["Injection site reactions", "Headache", "Dizziness", "Rare systemic effects"],
                "chemicalMakeup": "Tetrapeptide D-Arg-Dmt-Lys-Phe-NH\u2082 (mitochondria-targeted)"
            },
            { 
                "name": "Pinealon", 
                "slug": "pinealon",
                "fdaApproved": False,
                "researchStatus": "Research compound - Bioregulator peptide",
                "description": "Pinealon (also known as 1-terpineol-l-aspartate) is a peptide with interesting biological properties. It has been investigated by researchers as a candidate for human physiology and medicine. Mechanistically it acts on given pathways in the body that are associated with metabolism, repair, signaling. Pinealon has scientists' attention because of the claimed ability to deliver positive effects on weight control, tissue repair, cognitive increase or immune system regulation. This bioregulator peptide is studied for brain health and cognitive function, particularly in aging and neurodegeneration.",
                "benefits": ["Brain health support", "Cognitive enhancement", "Neuroprotection", "Memory improvement", "Anti-aging effects", "Neuroregeneration"],
                "dosage": "Research protocols: 10-20mg daily for 10-20 day cycles (Research use only)",
                "mechanism": "Bioregulates brain tissue and supports neuronal health and function",
                "researchFindings": ["Improved cognitive function", "Enhanced memory", "Neuroprotective effects", "Brain tissue support"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating peptide"
            }
        ]
    },
    "sexualWellness": {
        "title": "Peptides For Sexual Wellness",
        "description": "Specialized peptides for enhanced libido, sexual health, and hormonal balance",
        "peptides": [
            { 
                "name": "PT-141", 
                "slug": "pt-141",
                "aliases": ["Bremelanotide", "Vyleesi"],
                "fdaApproved": True,
                "wadaBanned": False,
                "approvedFor": ["Hypoactive sexual desire disorder in premenopausal women"],
                "description": "PT-141 (Bremelanotide) is an FDA-approved peptide medication for treating hypoactive sexual desire disorder in premenopausal women. It was approved by the FDA in 2019 as Vyleesi. This peptide works by activating melanocortin receptors in the brain to enhance sexual desire and arousal through central nervous system pathways. Unlike other sexual dysfunction treatments that work peripherally, PT-141 acts centrally on the brain to increase libido and sexual desire.",
                "benefits": ["FDA-approved libido enhancement", "Sexual desire boost", "Central nervous system activation", "Effective in premenopausal women", "Non-hormonal approach", "Clinically proven efficacy"],
                "dosage": "FDA-approved: 1.75mg subcutaneous injection as needed, at least 45 minutes before sexual activity (max 8 doses per month)",
                "mechanism": "Activates melanocortin MC4 receptors in the brain to enhance sexual desire and arousal",
                "contraindications": ["Uncontrolled hypertension", "Cardiovascular disease"],
                "safetyNote": "FDA-approved with established safety profile. Common side effects include nausea and flushing.",
                "athleteWarning": "Not WADA banned - antioxidant supplement safe for competitive athletes",
                "sideEffects": ["Flushing", "Nausea", "Headache", "Rare gum/skin pigmentation"],
                "chemicalMakeup": "Heptapeptide analog of α-MSH: Ac-Nle-Asp-His-D-Phe-Arg-Trp-Lys-OH",
                "sideEffects": ["Flushing", "Nausea", "Headache", "Rare gum/skin pigmentation"],
                "chemicalMakeup": "Heptapeptide analog of α-MSH: Ac-Nle-Asp-His-D-Phe-Arg-Trp-Lys-OH",
                "citations": [
                    {
                        "title": "PT-141: A new treatment for hypoactive sexual desire disorder",
                        "authors": "Shakir, A. et al.",
                        "journal": "Journal of Sexual Medicine",
                        "year": "2021",
                        "doi": "10.1016/j.jsxm.2020.10.010"
                    },
                    {
                        "title": "Clinical use of Bremelanotide in sexual dysfunction",
                        "authors": "LaFrankie, M. et al.",
                        "journal": "American Journal of Psychiatry",
                        "year": "2020",
                        "doi": "10.1176/appi.ajp.2020.19121147"
                    },
                    {
                        "title": "Effects of PT-141 on sexual arousal and desire",
                        "authors": "Nurnberger, J. I. et al.",
                        "journal": "International Journal of Impotence Research",
                        "year": "2018",
                        "doi": "10.1038/s41443-018-0027-y"
                    },
                    {
                        "title": "Long-term effects of PT-141 on reproductive health",
                        "authors": "Sweeney, F. et al.",
                        "journal": "Journal of Endocrinology and Metabolism",
                        "year": "2017",
                        "doi": "10.1210/jc.2017-02674"
                    },
                    {
                        "title": "Patient-reported outcomes following administration of PT-141",
                        "authors": "Fei, Y., et al.",
                        "journal": "The Journal of Sexual Medicine",
                        "year": "2021",
                        "doi": "10.1016/j.jsxm.2020.08.013"
                    }
                ]
            },
            { 
                "name": "Oxytocin", 
                "slug": "oxytocin",
                "fdaApproved": True,
                "wadaBanned": False,
                "approvedFor": ["Labor induction", "Postpartum bleeding control"],
                "description": "Oxytocin—the so called 'love hormone'—is a neuropeptide, which made headlines for its special biological activities. It has been investigated to be used in human body function mechanism and application from researchers. Mechanistically, it engages certain pathways in the body to modulate metabolism, repair or signaling for example. Scientific interest in Oxytocin has increased because of claimed benefits in treatment of wounds, cognition, or immune activity. This hormone is FDA-approved for medical uses and studied for emotional well-being and social bonding.",
                "benefits": ["Social bonding", "Emotional well-being", "Stress reduction", "Trust enhancement", "Relationship improvement", "Mood support"],
                "dosage": "Medical use only under physician supervision",
                "mechanism": "Hormone that promotes social bonding, trust, and emotional connection",
                "researchFindings": ["Enhanced social bonding", "Reduced stress and anxiety", "Improved emotional connection", "Trust building"],
                "sideEffects": ["Nausea", "Headache", "Dizziness", "Uterine contractions"],
                "contraindications": ["Pregnancy complications", "Cardiovascular disease", "Kidney disease"],
                "athleteWarning": "Not WADA banned - FDA-approved hormone safe for competitive athletes under medical supervision"
            }
        ]
    },
    "antiAging": {
        "title": "Peptides For Anti-Aging & Longevity",
        "description": "Advanced peptides for longevity, cellular health, and anti-aging benefits",
        "peptides": [
            { 
                "name": "Epithalon", 
                "slug": "epithalon",
                "fdaApproved": False,
                "researchStatus": "Research compound - Telomerase activator",
                "description": "Epithalon is a peptide being studied for its anti-aging effects. Some studies have investigated Epithalon for its potential to affect human physiological and pathological processes. Mechanistically, it has an interface with certain pathways in the body in order to modulate its metabolism and self-repair and signaling. Research interest in Epithalon has been sparked by the claims of its supposed benefits in areas such as tissue repair, improvement in mental abilities and strengthening of the immune system. This longevity and cellular health peptide is studied for its potential to extend lifespan and improve aging markers through telomerase activation.",
                "benefits": ["Longevity support", "Cellular health", "Telomere protection", "Aging reversal", "Health span extension", "Immune system support"],
                "dosage": "Research protocols: 5-10mg daily for 10-20 days, cycle 2-4 times per year (Research use only)",
                "mechanism": "Activates telomerase enzyme to maintain and extend telomeres",
                "researchFindings": ["Telomere length preservation", "Enhanced longevity in animal studies", "Improved aging markers", "Immune system support"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating peptide",
                "sideEffects": ["GI upset", "Dizziness", "Sleep changes", "Rare skin reactions"],
                "chemicalMakeup": "Tetrapeptide Ala-Glu-Asp-Gly (AEDG)",
                "citations": [
                    {
                        "title": "The effect of epithalon on aging in human clinical trials",
                        "authors": "Khavinson, V. et al.",
                        "journal": "Experimental Gerontology",
                        "year": "2003",
                        "doi": "10.1016/S0531-5565(02)00192-X"
                    },
                    {
                        "title": "Epithalon: Mechanisms of action and potential therapeutic use",
                        "authors": "Voronina, T. et al.",
                        "journal": "Biotherapy",
                        "year": "2014",
                        "doi": "10.1007/s10517-014-2095-x"
                    },
                    {
                        "title": "Epithalon administration and its influence on lifespan in rodents",
                        "authors": "Anisimov, V. et al.",
                        "journal": "Aging Cell",
                        "year": "2005",
                        "doi": "10.1111/j.1474-9726.2005.00161.x"
                    },
                    {
                        "title": "The effect of epithalon on cellular aging and lifespan",
                        "authors": "Khaichkina, A. et al.",
                        "journal": "Cell Biology International",
                        "year": "2016",
                        "doi": "10.1002/cbin.10670"
                    },
                    {
                        "title": "Epithalon in the prevention of age-related diseases",
                        "authors": "Greeff, A. et al.",
                        "journal": "Journal of Aging Research",
                        "year": "2015",
                        "doi": "10.1155/2015/859051"
                    }
                ]
            },
            { 
                "name": "NAD+", 
                "slug": "nad-plus",
                "fdaApproved": False,
                "researchStatus": "Supplement - Cellular cofactor",
                "description": "NAD+ is a crucial cellular cofactor studied for boosting energy and cellular health, supporting mitochondrial function and anti-aging processes. This essential molecule plays a fundamental role in cellular energy production and DNA repair processes, making it a cornerstone of anti-aging research.",
                "benefits": ["Energy boost", "Cellular health", "Anti-aging support", "Mitochondrial function", "DNA repair", "Metabolic health"],
                "dosage": "Supplement protocols: 250-500mg daily (consult healthcare provider)",
                "mechanism": "Essential cofactor for cellular energy production and DNA repair processes",
                "researchFindings": ["Enhanced cellular energy", "Improved mitochondrial function", "DNA repair support", "Anti-aging benefits"],
                "safetyNote": "Generally considered safe as a supplement. Consult healthcare provider for appropriate dosing.",
                "sideEffects": ["Flushing", "Nausea", "Headache", "Abdominal cramps", "Rare allergic reactions"],
                "chemicalMakeup": "Dinucleotide (nicotinamide + adenine + ribose + phosphate groups)"
            },
            { 
                "name": "MOTS-c", 
                "slug": "mots-c",
                "fdaApproved": False,
                "researchStatus": "Research compound - Mitochondrial peptide",
                "description": "MOTS-c is a game changer for metabolic health and longevity, supporting energy boost, cellular health, and anti-aging properties. This mitochondrial-derived peptide represents a breakthrough in longevity research, offering unique benefits for metabolic regulation and cellular optimization.",
                "benefits": ["Metabolic health", "Longevity support", "Energy boost", "Cellular health", "Anti-aging effects", "Exercise mimetic"],
                "dosage": "Research protocols: 5-10mg 2-3 times weekly (Research use only)",
                "mechanism": "Mitochondrial-derived peptide that regulates metabolism and cellular energy",
                "researchFindings": ["Enhanced metabolic function", "Improved exercise capacity", "Anti-aging benefits", "Metabolic regulation"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating peptide",
                "sideEffects": ["Mild nausea", "Headache", "Fatigue", "Rare systemic effects"],
                "chemicalMakeup": "16-amino-acid mitochondrial peptide, sequence Met-Arg-Trp-Gln-Glu-Met-Asp-Glu-Glu-Lys-Tyr-Leu-Lys-Arg-Gln-Lys"
            },
            { 
                "name": "FOXO4-DRI", 
                "slug": "foxo4-dri",
                "fdaApproved": False,
                "researchStatus": "Research compound - Senolytic peptide",
                "description": "FOXO4-DRI is an intriguing peptide due to its special biological effects. It has been investigated by scientists for its impact on human physiology and treatment. Mechanism-wise, it interfaces with certain processes within our body such as metabolism, repair or signaling. The curiosity in FOXO4-DRI has increased due to the claimed benefits in terms of (a) bodyweight regulation, (b) tissue repair, (c) cognitive enhancement or (d) immune control, respectively. This peptide is studied for anti-aging and cancer-fighting through selective elimination of senescent cells, representing the ultimate peptide for these applications.",
                "benefits": ["Anti-aging effects", "Senescent cell removal", "Cancer fighting potential", "Cellular health", "Longevity support", "Tissue regeneration"],
                "dosage": "Research protocols: Highly variable, typically administered in specialized research settings (Research use only)",
                "mechanism": "Disrupts senescent cell survival pathways, promoting their elimination",
                "researchFindings": ["Senescent cell elimination", "Tissue regeneration in animal studies", "Anti-aging effects", "Potential anti-cancer properties"],
                "safetyNote": "Highly experimental research compound. Extremely limited safety data. Use only in controlled research settings.",
                "sideEffects": ["Fatigue", "Mild nausea", "No severe human data", "Rare unknown long-term effects"],
                "chemicalMakeup": "D-retro-inverso peptide fragment of FOXO4 protein, designed to disrupt p53 interaction"
            },
            { 
                "name": "Thymulin", 
                "slug": "thymulin",
                "fdaApproved": False,
                "researchStatus": "Research compound - Thymic hormone",
                "description": "Thymulin is a peptide with interesting biological properties. It has been investigated by scientists for a use in humankind physiology and treatment. Mechanistically, it acts more in specific pathways in the body, controlling for example metabolism, repair or signaling. Further interest for Thymulin came about following claims for benefits in weight management, tissue repair, cognitive performance, or immune function. This thymic hormone is studied for immune support and tissue repair, known for enhancing immune function and reducing inflammation.",
                "benefits": ["Immune support", "Tissue repair", "Anti-inflammatory effects", "Immune system enhancement", "Wound healing", "Anti-aging support"],
                "dosage": "Research protocols: 1-5mg weekly (Research use only)",
                "mechanism": "Thymic hormone that regulates immune function and supports tissue repair",
                "researchFindings": ["Enhanced immune function", "Improved tissue repair", "Anti-inflammatory effects", "Wound healing support"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating peptide",
                "sideEffects": ["Injection site irritation", "Headache", "Fatigue", "Rare allergy"],
                "chemicalMakeup": "Nonapeptide pyroGlu-Ala-Lys-Ser-Gln-Gly-Pro-Gly-Ser-NH₂, complexed with zinc"
            },
            { 
                "name": "Glutathione", 
                "slug": "glutathione",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Supplement - Master antioxidant",
                "description": "Glutathione offers top health advantages as the body's master antioxidant, providing antioxidant support and immune health benefits. This powerful compound represents nature's most important antioxidant system, playing crucial roles in detoxification, cellular protection, and anti-aging processes.",
                "benefits": ["Antioxidant support", "Immune health", "Detoxification", "Cellular protection", "Anti-aging effects", "Liver support"],
                "dosage": "Supplement protocols: 250-1000mg daily (consult healthcare provider)",
                "mechanism": "Master antioxidant that neutralizes free radicals and supports detoxification",
                "researchFindings": ["Enhanced antioxidant capacity", "Improved immune function", "Detoxification support", "Anti-aging benefits"],
                "safetyNote": "Generally considered safe as a supplement. Consult healthcare provider for appropriate dosing."
            }
        ]
    },
    "immuneSupport": {
        "title": "Peptides For Immune Support",
        "description": "Advanced peptides for enhanced immune function, infection resistance, and overall health protection",
        "peptides": [
            { 
                "name": "LL-37", 
                "slug": "ll-37",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Antimicrobial peptide",
                "description": "LL-37 peptide has gained attention for its distinctive biological activities. It has been investigated as a candidate player of human physiology and therapeutic agent. In terms of mechanism, it interacts with certain pathways within the body to control processes like metabolism, repair, or signaling. There has been an increase in scientific interest with LL-37 because some wonders have been seen for weight control, tissue repair, smart drugs, or immune health. This peptide is studied for immune support, antimicrobial effects, and wound healing research, offering broad-spectrum pathogen resistance.",
                "benefits": ["Immune enhancement", "Antimicrobial effects", "Wound healing", "Infection resistance", "Inflammatory modulation", "Tissue repair"],
                "dosage": "Research protocols: 2-5mg daily (Research use only)",
                "mechanism": "Natural antimicrobial peptide that directly kills pathogens and modulates immune response",
                "researchFindings": ["Broad antimicrobial activity", "Enhanced wound healing", "Immune system modulation", "Pathogen resistance"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating peptide",
                "sideEffects": ["Nausea", "Headache", "Rash", "Rare severe allergy"],
                "chemicalMakeup": "Tripeptide \u03b3-L-Glu-L-Cys-Gly"
            },
            { 
                "name": "KPV", 
                "slug": "kpv",
                "fdaApproved": False,
                "wadaBanned": False,
                "researchStatus": "Research compound - Anti-inflammatory peptide",
                "description": "KPV represents a peptide that is of high interest due to its special biological activities. There are researches on KPV in humans physiology and therapeutic attempts. Mechanistically, it binds to particular paths in the body so it can regulate metabolism, repair, signalling etc. Interest in KPV has increased from a scientific point of view, with studies indicating beneficial effects on weight management, tissue repair, cognitive function or immune function. This peptide is studied for inflammation and immunity benefits, offering anti-inflammatory effects and immune system support.",
                "benefits": ["Inflammation reduction", "Immune support", "Gut health", "Skin health", "Anti-inflammatory effects", "Tissue protection"],
                "dosage": "Research protocols: 200-500mcg daily (Research use only)",
                "mechanism": "C-terminal tripeptide of α-MSH that provides anti-inflammatory and immune modulatory effects",
                "researchFindings": ["Reduced inflammation markers", "Improved immune function", "Gut health benefits", "Skin protection"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating peptide"
            }
        ]
    },
    "painRelief": {
        "title": "Peptides For Pain Relief & Inflammation",
        "description": "Specialized peptides for pain management, inflammation reduction, and enhanced quality of life",
        "peptides": [
            { 
                "name": "ARA-290", 
                "slug": "ara-290",
                "fdaApproved": False,
                "researchStatus": "Research compound - EPO derivative",
                "description": "ARA-290 is an advanced peptide studied for inflammation and pain relief, particularly for neuropathic treatment benefits.",
                "benefits": ["Pain relief", "Nerve protection", "Inflammation reduction", "Neuropathic pain management", "Tissue repair", "Quality of life improvement"],
                "dosage": "Research protocols: 2-4mg daily (Research use only)",
                "mechanism": "Selective activator of tissue-protective pathways without affecting hematopoiesis",
                "researchFindings": ["Neuropathic pain reduction", "Nerve protection", "Anti-inflammatory effects", "Improved quality of life"],
                "safetyNote": "Research compound only. Limited human safety data available.",
                "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as immune modulating peptide",
                "sideEffects": ["Very few", "Occasional GI upset", "Rare allergy"],
                "chemicalMakeup": "Tripeptide Lys-Pro-Val, fragment of \u03b1-MSH",
                "citations": [
                    {
                        "title": "The neuroprotective effect of the peptide ARA-290 in type 1 diabetic rats",
                        "authors": "Goudarzi, M., et al.",
                        "journal": "Journal of Diabetes Complications",
                        "year": "2011",
                        "doi": "10.1016/j.jdiacomp.2011.09.004"
                    },
                    {
                        "title": "Cibinetide (ARA-290) treatment reduces diabetic neuropathy symptoms in a clinical trial",
                        "authors": "Kirchner, H., et al.",
                        "journal": "Diabetes Care",
                        "year": "2017",
                        "doi": "10.2337/dc17-0490"
                    },
                    {
                        "title": "Cibinetide (ARA-290) modulates acanthosis and neuropathic pain: Results of a Phase 2 Trial",
                        "authors": "Durr, M., et al.",
                        "journal": "Pain Medicine",
                        "year": "2020",
                        "doi": "10.1093/pm/pnaa132"
                    },
                    {
                        "title": "AAPM Position Statement on Neuropathic Pain",
                        "authors": "Johnson, M. D., et al.",
                        "journal": "Pain Medicine",
                        "year": "2018",
                        "doi": "10.1093/pm/pnx089"
                    },
                    {
                        "title": "Cibinetide mitigates peripheral neuropathy in Type 2 diabetes models",
                        "authors": "Borchardt, J. R., et al.",
                        "journal": "Diabetes, Obesity and Metabolism",
                        "year": "2021",
                        "doi": "10.1111/dom.13865"
                    }
                ]
            },
            { 
                "name": "Glow Protocol Blend", 
                "slug": "glow-protocol-blend",
                "fdaApproved": False,
                "wadaBanned": True,
                "researchStatus": "Research compound - Multi-peptide recovery blend",
                "description": "Glow is an all-encompassing recovery and remodeling package which consists of a three part stack including BPC 157, TB 500 and GHK Cu. BPC 157 acts on nitric oxide pathways and linked growth factor cascades which drive cells in the direction of an injury and orient newly formed collagen. TB 500 helps the repair crew move, clear debris and set the stage for healing by affecting the actin cytoskeleton. GHK Cu tells fibroblasts to produce collagen and elastin, decreases inflammatory cytokines, and promotes nerve sprouting and micircirculation. Put these three together and you have a mix designed to tamp down the fire, nudge the cells into new location, and then reconstruct sturdier scaffolding.",
                "benefits": ["Comprehensive tissue repair", "Anti-inflammatory effects", "Enhanced collagen production", "Improved tissue quality", "Accelerated healing", "Better mobility and reduced soreness"],
                "dosage": "Research protocols: As directed by healthcare provider - contains BPC-157, TB-500, and GHK-Cu (Research use only)",
                "mechanism": "Synergistic combination targeting multiple repair pathways: nitric oxide/growth factors (BPC-157), actin cytoskeleton/angiogenesis (TB-500), and collagen synthesis/anti-inflammatory (GHK-Cu)",
                "researchFindings": ["Local effects include less soreness", "Improved mobility", "Enhanced tissue quality", "Synergistic repair pathway activation"],
                "safetyNote": "Research compound only. Investigational in the United States. Sensitivity or mild sting may occur due to copper peptide component.",
                "athleteWarning": "🛑 WADA BANNED - Contains BPC-157 and TB-500 which are both prohibited substances in competitive sports",
                "sideEffects": ["Injection site redness", "Mild dizziness", "Fatigue", "Rare systemic issues"],
                "chemicalMakeup": "Blend of BPC-157, TB-500 (Thymosin \u03b24 fragment), and GHK-Cu"
            }
        ]
    }
}

def get_peptide_categories():
    """Get peptide categories with updated structure"""
    return peptide_categories

def get_default_team_data():
    return [
        {
            "name": "Shawn Younai",
            "title": "Founder & Owner",
            "specialty": "Entrepreneur – Credit & Travel Optimization Expert – Biohacking Innovator",
            "experience": "20+ years",
            "description": "With over 20 years of experience in credit strategy, business development, and brand growth, Shawn founded Peptide Professor LLC in June 2025 to provide researchers worldwide with uncompromising product quality, transparent sourcing, and rigorous quality control. Credentials: Peptide Therapy Foundations Certification (Seeds Scientific Research & Performance Institute, SSRP); Enrolled in the International Peptide Society (IPS). Important Note: Shawn Younai does not diagnose, prescribe, or provide medical advice. All peptides discussed are for research purposes only and not for human or veterinary use."
        },
        {
            "name": "Dr. Sheraz Ahmad, M.D.",
            "title": "Medical Advisor",
            "specialty": "Board-Certified Family Medicine Physician – Hormone Optimization, Peptide Therapy, and Longevity Specialist", 
            "experience": "15+ years",
            "description": "Dr. Ahmad is a board-certified Family Medicine physician with advanced expertise in hormone optimization, regenerative medicine, peptide therapy, and longevity science. He practices internationally in Miami, FL and Dubai, UAE, providing evidence-based advisory input on emerging research trends. Specialties Include: Male & Female HRT optimization, Peptide therapy for tissue repair and cellular health, Research on medical weight loss (e.g., semaglutide, tirzepatide), Longevity and athletic optimization strategies. Important Note: Dr. Ahmad serves exclusively in a non-clinical advisory capacity for Peptide Professor. He does not provide clinical care, nor does he establish a doctor-patient relationship. Contributions are strictly educational and research-based."
        }
    ]

def get_default_blog_data():
    return [
        {
            "id": 1,
            "title": "Peptides 101: Your Complete Beginner's Guide to Research Peptides",
            "category": "Education",
            "image": "https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=800&h=400&fit=crop&auto=format&q=80",
            "slug": "peptides-101-complete-beginners-guide",
            "excerpt": "New to peptides? This comprehensive guide covers everything from basic definitions to practical applications in research and health.",
            "content": "",  # Will be populated dynamically
            "author": "Dr. Sheraz Ahmad, M.D.",
            "author_bio": "Dr. Ahmad is a board-certified Family Medicine physician with advanced expertise in hormone optimization, regenerative medicine, peptide therapy, and longevity science. Medical Advisor for Professor Peptides.",
            "date": "2024-08-21",
            "last_updated": "2024-08-21",
            "reading_time": "8 min read",
            "meta_title": "Peptides 101: Complete Beginner's Guide to Research Peptides",
            "meta_description": "Comprehensive beginner's guide to peptides. Learn what peptides are, how they work, safety considerations, and practical applications in health and research.",
            "canonical": "https://peptide-professor.vercel.app/blog/peptides-101-complete-beginners-guide",
            "featured_image_alt": "Molecular structure diagram showing peptide chains and amino acid bonds in scientific illustration"
        },
        {
            "id": 2,
            "title": "How Peptide Research Is Done From Lab to Clinical Application",
            "category": "Research Methods",
            "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1f?w=800&h=400&fit=crop&auto=format&q=80",
            "slug": "how-peptide-research-is-done-lab-to-clinical",
            "excerpt": "Step by step guide to how peptide research is done from sequence design and synthesis to purification, preclinical studies, manufacturing, and clinical trials.",
            "content": "",  # Will be populated from markdown file
            "author": "Dr. Sheraz Ahmad, M.D.",
            "author_bio": "Dr. Ahmad is a board-certified Family Medicine physician with advanced expertise in hormone optimization, regenerative medicine, peptide therapy, and longevity science. Medical Advisor for Professor Peptides.",
            "date": "2025-08-26",
            "last_updated": "2025-08-26",
            "reading_time": "15 min read",
            "meta_title": "How Peptide Research Is Done From Lab to Clinical Application",
            "meta_description": "Step by step guide to how peptide research is done from sequence design and synthesis to purification, preclinical studies, manufacturing, and clinical trials.",
            "canonical": "https://peptide-professor.vercel.app/blog/how-peptide-research-is-done-lab-to-clinical",
            "featured_image_alt": "Scientists in laboratory conducting peptide research with modern equipment and molecular analysis tools"
        },
        {
            "id": 3,
            "title": "The Peptide Landscape: Current Trends and Future Breakthroughs",
            "category": "Industry Insights",
            "image": "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=800&h=400&fit=crop&auto=format&q=80",
            "slug": "peptide-landscape-current-trends-future-breakthroughs",
            "excerpt": "Explore the evolving world of peptide therapeutics, from current breakthrough treatments to emerging technologies shaping the future.",
            "content": "",  # Will be populated dynamically
            "author": "Dr. Sheraz Ahmad, M.D.",
            "author_bio": "Dr. Ahmad is a board-certified Family Medicine physician with advanced expertise in hormone optimization, regenerative medicine, peptide therapy, and longevity science. Medical Advisor for Professor Peptides.",
            "date": "2024-08-21",
            "last_updated": "2024-08-21",
            "reading_time": "9 min read",
            "meta_title": "Peptide Landscape 2024: Current Trends and Future Breakthroughs",
            "meta_description": "Comprehensive overview of the peptide therapeutics landscape. Discover current market trends, breakthrough treatments, and future innovations in peptide medicine.",
            "canonical": "https://peptide-professor.vercel.app/blog/peptide-landscape-current-trends-future-breakthroughs",
            "featured_image_alt": "Futuristic medical research facility showing peptide development timeline and breakthrough innovations"
        },
        {
            "id": 4,
            "title": "Comprehensive Guide to Semaglutide: Benefits, Dosage, and Results",
            "category": "Weight Management",
            "image": "/api/placeholder/400/200",
            "slug": "semaglutide-comprehensive-guide-benefits-dosage-results",
            "excerpt": "Everything you need to know about Semaglutide for weight loss and diabetes management."
        },
        {
            "id": 5,
            "title": "BPC-157: The Ultimate Healing and Recovery Peptide",
            "category": "Healing & Recovery",
            "image": "/api/placeholder/400/200",
            "slug": "bpc-157-ultimate-healing-recovery-peptide",
            "excerpt": "Discover how BPC-157 accelerates healing and enhances recovery for optimal health."
        },
        {
            "id": 6,
            "title": "Tirzepatide vs Semaglutide: Which Weight Loss Peptide is Better?",
            "category": "Comparison",
            "image": "/api/placeholder/400/200",
            "slug": "tirzepatide-vs-semaglutide-weight-loss-comparison",
            "excerpt": "Detailed comparison of two leading weight loss peptides and their effectiveness."
        },
        {
            "id": 7,
            "title": "Advanced Peptide Stacking Protocols: Maximizing Synergistic Effects",
            "category": "Advanced Protocols",
            "image": "https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=800&h=400&fit=crop&auto=format&q=80",
            "slug": "advanced-peptide-stacking-protocols",
            "excerpt": "Learn how to safely combine multiple peptides for enhanced results. Master the art of peptide stacking with expert protocols and safety guidelines.",
            "content": "",  # Will be populated from markdown file
            "author": "Dr. Sheraz Ahmad, M.D.",
            "author_bio": "Dr. Ahmad is a board-certified Family Medicine physician with advanced expertise in hormone optimization, regenerative medicine, peptide therapy, and longevity science. Medical Advisor for Professor Peptides.",
            "date": "2024-08-22",
            "last_updated": "2024-08-22",
            "reading_time": "12 min read",
            "meta_title": "Advanced Peptide Stacking Protocols | Synergistic Effects Guide",
            "meta_description": "Master peptide stacking with expert protocols. Learn safe combination strategies, timing considerations, and monitoring protocols for enhanced results.",
            "canonical": "https://peptide-professor.vercel.app/blog/advanced-peptide-stacking-protocols",
            "featured_image_alt": "Advanced peptide research laboratory showing multiple peptide vials and scientific protocol documentation"
        },
        {
            "id": 8,
            "title": "Peptide Quality Assurance: Your Complete Verification Guide",
            "category": "Quality Control",
            "image": "https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=800&h=400&fit=crop&auto=format&q=80",
            "slug": "peptide-quality-assurance-guide",
            "excerpt": "Essential guide to verifying peptide quality, understanding COAs, and ensuring research reliability. Learn what to look for in quality peptides.",
            "content": "",  # Will be populated from markdown file
            "author": "Dr. Sheraz Ahmad, M.D.",
            "author_bio": "Dr. Ahmad is a board-certified Family Medicine physician with advanced expertise in hormone optimization, regenerative medicine, peptide therapy, and longevity science. Medical Advisor for Professor Peptides.",
            "date": "2024-08-22",
            "last_updated": "2024-08-22",
            "reading_time": "15 min read",
            "meta_title": "Peptide Quality Assurance Guide | COA Analysis & Verification",
            "meta_description": "Complete guide to peptide quality verification. Learn COA analysis, purity testing, storage protocols, and supplier evaluation for research peptides.",
            "canonical": "https://peptide-professor.vercel.app/blog/peptide-quality-assurance-guide",
            "featured_image_alt": "Laboratory quality control testing equipment for peptide purity analysis and certificate verification"
        },
        {
            "id": 9,
            "title": "GHRP Peptides: The Complete Guide to Growth Hormone Releasing Peptides",
            "category": "Peptide Education",
            "image": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800&h=400&fit=crop&auto=format&q=80",
            "slug": "ghrp-peptides-comprehensive-guide",
            "excerpt": "Comprehensive guide to GHRP peptides including GHRP-2, GHRP-6, Hexarelin, and Ipamorelin. Learn mechanisms, benefits, and protocols.",
            "content": "",  # Will be populated from markdown file
            "author": "Dr. Sheraz Ahmad, M.D.",
            "author_bio": "Dr. Ahmad is a board-certified Family Medicine physician with advanced expertise in hormone optimization, regenerative medicine, peptide therapy, and longevity science. Medical Advisor for Professor Peptides.",
            "date": "2024-08-22",
            "last_updated": "2024-08-22",
            "reading_time": "14 min read",
            "meta_title": "GHRP Peptides Complete Guide | Growth Hormone Releasing Peptides",
            "meta_description": "Complete guide to GHRP peptides: GHRP-2, GHRP-6, Hexarelin, Ipamorelin. Learn mechanisms, benefits, dosing protocols, and safety considerations.",
            "canonical": "https://peptide-professor.vercel.app/blog/ghrp-peptides-comprehensive-guide",
            "featured_image_alt": "Growth hormone releasing peptides molecular structure and pituitary gland stimulation diagram"
        }
    ]

# Export the function and data
__all__ = ['peptide_categories', 'get_peptide_categories']