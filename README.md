# Larvae Segmentation with Otsu

This is a web-based application for segmenting mosquito larvae using the Otsu thresholding method. The application allows users to upload an image containing mosquito larvae, and it performs image processing to detect and count the larvae. The processed image is displayed along with the count of larvae found.

## Installation

To run the application locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/nbilasals/segmentasi_jentik_nyamuk.git
   ```
2. Navigate to the project directory:
   ```bash
   cd segmentasi_jentik_nyamuk
   ```
3. Install the require dPython packages using pip
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application
   ```bash
   python app.py
   ```

## Usage
1. Access the application in your web browser.
2. Click the "Upload an Image" button to select an image containing mosquito larvae.
3. Click the "Upload and Process" button to initiate the segmentation and counting process.
4. The processed image and the count of mosquito larvae found will be displayed.
