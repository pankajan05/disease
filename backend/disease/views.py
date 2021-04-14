from django.http import HttpResponse
from django.shortcuts import render
import joblib
from googletrans import Translator
import difflib


knn = joblib.load('./model/KNNModel.pkl')

disease=['Fungal infection', 'Allergy', 'Gastroesophageal reflux disease (GERD)', 'Chronic cholestasis',
       'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
       'Gastroenteritis disease', 'Asthma', 'Hypertension ', 'Migraine',
       'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
       'Malaria', 'Chicken pox', 'Dengue', 'Typhoid(a bacterial infection)', 'hepatitis A',
       'Hepatitis B liver infection', 'Hepatitis C virus infection', 'Hepatitis D swelling liver', 'Hepatitis E (A liver disease)',
       'Alcoholic hepatitis (swelling of the liver)', 'Tuberculosis', 'Common Cold', 'Pneumonia',
       'Swelling of the blood vessels in the rectum', 'Heart attack', 'Varicose veins',
       'Body doesn\'t produce enough thyroid hormones', 'Hyperthyroidism', 'Hypoglycemia(low blood sugar)',
       'Osteoarthristis', 'Arthritis',
       '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
       'Urinary tract infection', 'Psoriasis', 'Impetigo']


l1=['Body back pain','constipation','abdominal pain','diarrhea','mild_fever','yellowish urine',
    'yellowish eyes','liver damage','too much fluids in the blood','swelling of stomach',
    'swelled lymph nodes','malaise','Impaired vision','phlegm','Throat infections',
    'Redness of eyes','Nasal congestion','discharge mucus from the nose','Body stiffness','chest pain','weakness in limbs',
    'fast heart rate','pain during bowel movements','pain in anal region','bleeding with stool',
    'itching around the anus','neck pain','dizziness','cramps of body','bruising','obesity','swollen legs',
    'swollen blood vessels','puffy face and eyes','That the thyroid gland is large','brittle nails',
    'swelling of arms, feet, ankles, and legs','excessive hunger','Problems with unmarried relationships','drying and tingling lips',
    'slurred speech','knee pain','hip joint pain','muscle weakness','Tightness of the neck','swelling joints',
    'Tightness in body movements','Dizziness during movements','loss of body balance','Body unsteadiness',
    'weakness of one body side','loss of sense of smell','Pain in the bladder','foul smell of urine',
    'Need to urinate frequently','releasing gas through the anus','body internal itching','typhus fever',
    'depression','irritability','muscle pain','inability to think clearly or concentrate','red spots on body','lower stomach pain',
    'abnormal menstruation','Discolored skin','Tears in the eyes','Excessive hunger','production of abnormal volumes of urine','Hereditary disorders','white mucus come from the nose',
    'Rust-colored mucus come from the nose','overactivity','change in  eyesight','Transfusion Reactions',
    'unsafe injection','coma','bleeding in stomach','swelling of the abdomen',
    'high dosage of alcohol consumption','Excess fluid resulting in body weight gain','blood with mucus','swollen and enlarged veins that occur on the legs and feet',
    'feel like heart stopped beats','pain when walking','pus-filled pimples','blackheads','scurring','damage to the upper layer of your skin',
    'the skin turns blue or blue-grey','pitting in Nail','an inflammation of the skin around the nail','blister','Red skin under and around nose',
    'Yellowish crusting pus builds up']

l2=[]


def index(request):
    return render(request, 'index.html');

def predictDisease(request):
    if request.method == 'POST':
        print(request.POST.dict())

    translator = Translator()

    psymptoms = [translator.translate(request.POST.dict()['symptom1'], dest='en').text,
                 translator.translate(request.POST.dict()['symptom2'], dest='en').text,
                 translator.translate(request.POST.dict()['symptom3'], dest='en').text]
    print(psymptoms)

    for i in range(0, len(l1)):
        l2.append(0)

    for k in range(0, len(l1)):
        for z in psymptoms:
            if difflib.SequenceMatcher(None, z, l1[k]).ratio()*100 > 70:
                print(l1[k])
                l2[k] = 1

    print(l2)

    inputtest = [l2]
    predict = knn.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        predicted = disease[a]
    else:
        print("Not Found")

    data = translator.translate(predicted, dest='si')

    return render(request, 'result.html', {'data': data.text})
