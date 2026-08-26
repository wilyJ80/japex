import os
os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"

from paddleocr import PaddleOCR

# Initialize OCR
ocr = PaddleOCR(use_textline_orientation=True, lang='pt', enable_mkldnn=False)

# Run prediction
results = ocr.predict('src/ocr/convite.png')

# Iterate through the results and extract text and confidence scores
for res in results:
    # Depending on the exact PaddleX version, the result object acts like a dict or has attributes
    texts = res.get('rec_texts', [])
    scores = res.get('rec_scores', [])
    
    for text, score in zip(texts, scores):
        print(f"Text: {text}, Confidence: {score:.2f}")
