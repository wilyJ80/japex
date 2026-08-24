from ultralytics import YOLO

model = YOLO('yolo26x-cls.pt')

results = model.predict('./src/vision/pexels-sbam-30599204.jpg')

for result in results:
    top1 = result.probs.top1
    print(top1)
