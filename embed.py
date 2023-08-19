from chromadb import Documents, EmbeddingFunction, Embeddings

from PIL import Image
import torch
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from tqdm import tqdm
from transformers import CLIPProcessor, CLIPModel # CLIPTokenizer, CLIPTokenizerFast


# Install necessary packages
# !pip install torch torchvision transformers tqdm Pillow


class ImageEmbedder(EmbeddingFunction):
    def __init__(self):

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")

        # Load model and processor
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)

        # Define image transformations
        self.transform = Compose([
            Resize([224, 224]), 
            CenterCrop(224), 
            ToTensor(),
            Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ])

    def __call__(self, image_filenames: Documents) -> Embeddings:
        embeddings = []

        if len(image_filenames) > 1:
            iterator = tqdm(image_filenames)
        else:
            iterator = image_filenames

        for image_path in iterator:
            # Open and process image
            image = self.transform(Image.open(image_path)).unsqueeze(0)
            
            # Move image to device
            image = image.to(self.device)

            # Vectorize
            with torch.no_grad():
                image_features = self.model.get_image_features(pixel_values=image)
                embeddings.append(
                    image_features
                    .cpu()
                    .numpy()
                    [0]
                    .tolist()
                )
            
        return embeddings
    
class LanguageEmbedder:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")

        # Load model and processor
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        # Consider: CLIPTokenizerFast

    def __call__(self, texts):
        inputs = self.processor(texts, return_tensors="pt", padding=True) # truncation=True
        inputs = inputs.to(self.device)

        with torch.no_grad():
            outputs = self.model.get_text_features(**inputs)

        return outputs \
                .cpu() \
                .numpy() \
                [0] \
                .tolist()