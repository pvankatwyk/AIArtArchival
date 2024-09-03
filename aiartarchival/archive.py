import os
import json
import spacy
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

artwork_directory = "./artwork/"
output_file = "captions_and_keywords.json"

# Load spaCy's English model
# if you get an error here, you will need to run the following line in terminal:
# python -m spacy download en_core_web_sm
try:
  nlp = spacy.load("en_core_web_sm")
except:
  import subprocess
  import sys
  subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
  nlp = spacy.load("en_core_web_sm")
  
# Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Directory containing images
image_dir = artwork_directory  # Update this with your image directory path

# Initialize an empty list to store results
results = []

# Function to extract nouns and verbs
def extract_keywords(caption):
    doc = nlp(caption)
    nouns = [token.text for token in doc if token.pos_ == "NOUN" or token.pos_ == "PROPN"]
    verbs = [token.text for token in doc if token.pos_ == "VERB"]
    return {"nouns": nouns, "verbs": verbs}

# Loop through all images in the directory
for image_name in os.listdir(image_dir):
    if image_name.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
        image_path = os.path.join(image_dir, image_name)
        raw_image = Image.open(image_path).convert('RGB')  # load the image

        # Preprocess the image and generate a caption
        inputs = processor(raw_image, return_tensors="pt")  # process it to be ready to model
        out = model.generate(
            **inputs,
            max_length=100,  # max length of caption
            num_beams=5,  # increase this for better captions, but longer to run
            no_repeat_ngram_size=2,  # avoid repeating n-grams
            length_penalty=1.5  # increase this for longer captions
        )
        caption = processor.decode(out[0], skip_special_tokens=True)

        # Extract nouns and verbs
        keywords = extract_keywords(caption)

        # Save the result
        results.append({
            "image": image_name,
            "caption": caption,
            "keywords": keywords
        })

        # Optional: print the caption and keywords to see progress
        print(f"Caption for {image_name}: {caption}")
        print(f"Keywords: {keywords}")

# Save all results to a JSON file
with open(output_file, 'w') as f:
    json.dump(results, f, indent=4)

print(f"Captions and keywords saved to {output_file}")
