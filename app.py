from flask import Flask, request, render_template
import cv2

app = Flask(__name__)


@app.route('/')
def upload_image():
    return render_template('upload.html')


@app.route('/process', methods=['POST'])
def process_image():
    if 'image' in request.files:
        image = request.files['image']
        image.save('static/uploaded_image.jpg')  # Save the uploaded image
        result = detect_mosquito_larvae('static/uploaded_image.jpg')
        return render_template('result.html', result=result)
    return 'No image file found'


def detect_mosquito_larvae(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Determine Otsu Threshold
    otsu_threshold, image_otsu = cv2.threshold(
        image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Denoising Otsu
    image_otsu_clean = cv2.fastNlMeansDenoising(image_otsu, None, 20, 7, 21)

    # Gaussian Blur
    blur = cv2.GaussianBlur(image_otsu_clean, (11, 11), 0)

    # Edge Detection - Canny
    canny = cv2.Canny(blur, 30, 150, 3)

    # Dilation
    dilated = cv2.dilate(canny, (1, 1), iterations=1)

    # Find Contours (Adapt to different OpenCV versions)
    try:
        _, contours, _ = cv2.findContours(
            dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
    except ValueError:
        contours, _ = cv2.findContours(
            dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )

    # Create a copy of the original image with contours drawn
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    # Save the image with contours for display in the result
    cv2.imwrite('static/processed_image.jpg', image_with_contours)

    # Return the count of mosquito larvae
    return len(contours)


if __name__ == '__main__':
    app.run(debug=True)
