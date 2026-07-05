import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import os

# Load trained model
model_path = "ml_models/disease_model/model.h5"

model = load_model(model_path)

# Automatically read class names from dataset folders
dataset_path = "ml_models/sample_dataset"

class_names = sorted(
    [
        name for name in os.listdir(dataset_path)
        if os.path.isdir(os.path.join(dataset_path, name))
    ]
)

print("Loaded classes:")
print(class_names)


def format_cure(what, causes, severity, steps, prevention):
    return f"""
        <div class="cure-section" style="line-height:1.6;color:#cbd5e1;margin-top:1rem;background:rgba(15,23,42,0.4);padding:1.25rem;border-radius:12px;border:1px solid rgba(52,211,153,0.1);">
            <h4 style="color:#34d399;margin-bottom:0.25rem;font-size:0.95rem;font-weight:700;">What this disease is</h4>
            <p style="margin-bottom:1rem;font-size:0.85rem;">{what}</p>
            
            <h4 style="color:#34d399;margin-bottom:0.25rem;font-size:0.95rem;font-weight:700;">Why It Happens (Real Causes)</h4>
            <div style="margin-bottom:1rem;font-size:0.85rem;">{causes}</div>
            
            <h4 style="color:#34d399;margin-bottom:0.25rem;font-size:0.95rem;font-weight:700;">How Serious It Is</h4>
            <div style="margin-bottom:1rem;font-size:0.85rem;">{severity}</div>
            
            <h4 style="color:#34d399;margin-bottom:0.25rem;font-size:0.95rem;font-weight:700;">What You Should Do Now (Practical Steps)</h4>
            <div style="margin-bottom:1rem;font-size:0.85rem;">{steps}</div>
            
            <h4 style="color:#34d399;margin-bottom:0.25rem;font-size:0.95rem;font-weight:700;">Prevention for Future Plants</h4>
            <div style="font-size:0.85rem;">{prevention}</div>
        </div>
    """

def get_cure(disease_name):
    disease_name = disease_name.lower()
    
    if 'healthy' in disease_name:
        return """
        <div class="cure-section" style="line-height:1.6;color:#cbd5e1;margin-top:1rem;background:rgba(15,23,42,0.4);padding:1.25rem;border-radius:12px;border:1px solid rgba(52,211,153,0.1);">
            <h4 style="color:#34d399;margin-bottom:0.5rem;font-size:0.95rem;font-weight:700;">Status: Healthy!</h4>
            <p style="font-size:0.85rem;">Your crop is perfectly healthy and shows no visible signs of disease or pest infestation.</p>
            <h4 style="color:#34d399;margin-top:1rem;margin-bottom:0.5rem;font-size:0.95rem;font-weight:700;">Maintenance</h4>
            <p style="font-size:0.85rem;">Continue your current watering, fertilization, and care routines as they are working beautifully.</p>
        </div>
        """
        
    elif 'blight' in disease_name:
        return format_cure(
            "Early blight is a fungal infection that commonly affects plants (like tomatoes/potatoes), usually starting on the lower leaves with brown spots/halos and gradually moving upward.",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Warm temperatures (roughly 24–30 °C)</li><li>Humidity or wet leaves for long periods</li><li>Overhead watering</li><li>Crowded plants with poor airflow</li><li>Plants under stress (low nutrients, irregular watering)</li></ul>",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li><strong>Early stage:</strong> Mostly cosmetic leaf damage</li><li><strong>Moderate stage:</strong> Leaves start dying and falling</li><li><strong>Severe stage:</strong> Plant loses many leaves reducing fruit yield</li></ul>",
            "<p>1) <strong>Remove infected leaves:</strong> Cut off the worst affected leaves and dispose of them immediately.<br>2) <strong>Change watering:</strong> Water at the base, not on leaves (dry leaves=happy leaves).<br>3) <strong>Improve airflow:</strong> Space plants and prune lower leaves touching soil.<br>4) <strong>Fungicides:</strong> Apply Mancozeb, Chlorothalonil, or Copper fungicide every 7–10 days.</p>",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Rotate crops (don't grow the same crop in the same soil).</li><li>Mulch the soil to reduce fungal splash from rain.</li><li>Keep plants well-fed and remove debris after harvest.</li></ul>"
        )
        
    elif 'scab' in disease_name:
        return format_cure(
            "Scab is a fungal disease that creates rough, dark, crusty lesions on leaves and fruit. It severely downgrades the appearance and market value of the crop.",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Prolonged wet weather and high humidity.</li><li>Fungal spores surviving winter in fallen leaves or twigs.</li><li>Overcrowded canopies preventing leaf drying.</li></ul>",
            "Moderate to Severe. While it rarely kills the plant outright, it can cause premature leaf drop and make fruits entirely unsellable or inedible.",
            "<p>1) <strong>Prune lightly:</strong> Remove heavily infected shoots and leaves.<br>2) <strong>Treat actively:</strong> Spray a fungicide containing captan or sulfur according to label instructions.<br>3) <strong>Water carefully:</strong> Avoid splashing water onto the foliage.</p>",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Rake and destroy all fallen leaves at the end of the season.</li><li>Plant scab-resistant varieties when possible.</li><li>Prune canopies to improve sunlight and air circulation.</li></ul>"
        )

    elif 'black_rot' in disease_name or 'black rot' in disease_name:
        return format_cure(
            "Black Rot is a damaging bacterial or fungal disease characterized by brown or black V-shaped lesions on leaf edges that spread rapidly.",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Warm, humid, and rainy conditions.</li><li>Bacterial/fungal spread via water splashing or contaminated tools.</li><li>Using infected seeds or transplants.</li></ul>",
            "Very Serious. It can completely destroy the crops (like cabbage or grapes) if left unchecked, spreading swiftly across the field.",
            "<p>1) <strong>Remove diseased plants:</strong> Immediately dig up and destroy infected plants.<br>2) <strong>Fungicides/Copper:</strong> Apply copper-based sprays (though effectiveness is limited once established).<br>3) <strong>Sanitize tools:</strong> Disinfect all pruners and farm tools to stop manual spread.</p>",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Use certified disease-free seeds and transplants.</li><li>Practice a 3-4 year crop rotation.</li><li>Weed regularly, as related weeds can harbor the pathogens.</li></ul>"
        )

    elif 'rust' in disease_name:
        return format_cure(
            "Rust forms distinct, powdery orange, yellow, or brown pustules on the undersides of leaves, stunting plant growth.",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>High moisture and mild temperatures.</li><li>Overhead irrigation causing leaves to stay wet.</li><li>Presence of alternate plant hosts nearby.</li></ul>",
            "Moderate. Causes severe defoliation and energy loss for the plant, drastically reducing overall yield if widespread.",
            "<p>1) <strong>Isolate:</strong> Remove severely rusted leaves immediately.<br>2) <strong>Fungicidal control:</strong> Apply neem oil, sulfur, or specific rust fungicides.<br>3) <strong>Keep dry:</strong> Eliminate overhead watering immediately.</p>",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Plant resistant varieties.</li><li>Remove any alternate weed hosts from the surrounding area.</li><li>Ensure wide spacing between plants for rapid drying.</li></ul>"
        )
        
    elif 'powdery_mildew' in disease_name or 'powdery mildew' in disease_name:
        return format_cure(
            "Powdery Mildew looks like a dusting of white or gray flour on leaves and stems, usually starting on older leaves and spreading heavily.",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>High humidity combined with dry foliage.</li><li>Poor air circulation and warm days/cool nights.</li><li>High nitrogen fertilizers triggering excessive leafy growth.</li></ul>",
            "Moderate. Distorts leaves, reduces photosynthesis, and weakens the plant, leading to lower yields and poor fruit flavor.",
            "<p>1) <strong>Prune:</strong> Remove the most heavily powdered leaves.<br>2) <strong>Sprays:</strong> Apply a baking soda mixture, neem oil, or sulfur-based fungicides.<br>3) <strong>Thin out:</strong> Thin the plants to allow proper airflow and sunlight penetration.</p>",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Avoid excessive nitrogen fertilizers.</li><li>Water plants adequately to prevent drought stress.</li><li>Choose mildew-resistant cultivars.</li></ul>"
        )
        
    elif 'mite' in disease_name:
        return format_cure(
            "Spider mites are tiny arachnids that suck plant sap, causing yellow stippling on leaves and leaving fine webbing under leaves.",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Hot, dry, and dusty conditions.</li><li>Drought stress weakening the plant's defenses.</li><li>A lack of natural predators in the environment.</li></ul>",
            "Moderate to Serious. They multiply at explosive rates in hot weather, quickly yellowing and killing entire leaves.",
            "<p>1) <strong>Wash them off:</strong> Use a strong blast of water to knock them off leaves.<br>2) <strong>Apply Oils/Soaps:</strong> Spray horticultural oils, neem oil, or insecticidal soap directly on leaf undersides.<br>3) <strong>Hydrate:</strong> Deeply water the plant to relieve drought stress.</p>",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Keep the environment slightly humid if in a greenhouse.</li><li>Introduce beneficial predators like ladybugs or predatory mites.</li><li>Keep the farm dust-free.</li></ul>"
        )
        
    else:
        # Generic detailed response for other diseases
        return format_cure(
            "The model has detected signs of a fungal, bacterial, or viral disease or pest damage. Spots, wilting, curling, or discoloration are present.",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Environmental stress (too much/little water).</li><li>Pathogen buildup in the soil from previous seasons.</li><li>Spread via insects, wind, or contaminated tools.</li></ul>",
            "Varies. It can range from minor cosmetic issues to a severe threat to your crop's survival. Immediate intervention is highly recommended.",
            "<p>1) <strong>Quarantine:</strong> Remove heavily affected leaves/plants to stop the spread.<br>2) <strong>Diagnose locally:</strong> Consider bringing a physical sample to a local agricultural extension.<br>3) <strong>Broad-spectrum action:</strong> Apply neem oil or copper fungicide as a baseline preventative step.</p>",
            "<ul style='margin-left:1.5rem;margin-top:0.25rem;'><li>Ensure adequate plant spacing and sunlight.</li><li>Disinfect tools between cuts.</li><li>Maintain healthy, well-draining soil with balanced nutrients.</li></ul>"
        )

def predict_disease(image_path):

    img = Image.open(image_path).convert("RGB")

    img = img.resize((224, 224))

    img_array = np.array(img)
    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(img_array)

    index = np.argmax(prediction)

    confidence = float(
        np.max(prediction)
    )

    disease = class_names[index]

    return {
        "disease": disease,
        "confidence": round(confidence * 100, 2),
        "cure": get_cure(disease)
    }