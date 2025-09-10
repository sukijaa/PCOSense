import os
import cv2
from ultralytics import YOLO

def detect(input_path):
    try:
        # Load YOLOv8 model
        model = YOLO("bestv8.pt")

        # Run detection
        results = model(input_path)

        # Ensure output directory
        output_dir = "static/output/results"
        os.makedirs(output_dir, exist_ok=True)

        # Save detection image with boxes
        saved_image_name = os.path.basename(input_path)
        saved_image_path = os.path.join(output_dir, saved_image_name)

        # Plot results with bounding boxes and labels
        plotted_img = results[0].plot(line_width=1, font_size=8)
  # thickness & font size
        cv2.imwrite(saved_image_path, plotted_img[:, :, ::-1])    # save image with boxes

        # Get cyst count
        cyst_count = len(results[0].boxes) if results and results[0].boxes is not None else 0

        return saved_image_path, cyst_count

    except Exception as e:
        return f"ERROR: {str(e)}", 0
