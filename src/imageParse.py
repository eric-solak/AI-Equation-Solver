from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import os

# Initialize the processor and model globally to avoid reloading each time
processor = TrOCRProcessor.from_pretrained('fhswf/TrOCR_Math_handwritten', use_fast=True)
model = VisionEncoderDecoderModel.from_pretrained('fhswf/TrOCR_Math_handwritten')

# Function to extract text (math equation) from an image
def extractEquation(image_path):
    # Open the image from the local path
    image = Image.open(image_path).convert("RGB")
    
    # Preprocess the image
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    
    # Generate the math equation text
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    return generated_text
