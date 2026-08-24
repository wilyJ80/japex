# TODO: RUN

import base64
from openai import OpenAI

# Initialize the client pointing to your local llama.cpp server
client = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="sk-no-key-required"  # llama.cpp server doesn't require a real key
)

def encode_image(image_path):
    """Encodes a local image file into a base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Path to your local image
image_path = "./src/vision/pexels-sbam-30599204.jpg"
base64_image = encode_image(image_path)

# Send the multimodal request
response = client.chat.completions.create(
    model="Qwen3VL-2B-Instruct.Q4_K_M.gguf",  # llama.cpp ignores this parameter and uses the loaded model
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image in detail."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    max_tokens=500,
    temperature=0.2
)

# Print the model's description
print(response.choices[0].message.content)

