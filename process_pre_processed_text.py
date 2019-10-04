import scispacy
import spacy

nlp = spacy.load("en_core_sci_sm")
doc = nlp("Alterations in the hypocretin receptor 2 and preprohypocretin genes produce narcolepsy in some animals.")

# nlp('Vivaglobin 160 mg / mL ( human normal immunoglobin solution for MeSH_Injections_Subcutaneous ) is licensed as replacement therapy for adults and children with primary immunodeficiency syndromes , myeloma , or chronic lymphatic leukaemia .')