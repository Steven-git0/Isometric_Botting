import os
import cv2
import numpy as np
from PIL import Image
import concurrent.futures

class ImagePreprocessor:
    def __init__(self, input_dir, output_dir):
        """
        Initialize image preprocessor with input and output directories
        
        Args:
            input_dir (str): Directory containing source images
            output_dir (str): Directory to save processed images
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def preprocess_image(self, filename):
        """
        Comprehensive image preprocessing method
        
        Args:
            filename (str): Name of the image file to process
        
        Returns:
            bool: True if processing successful, False otherwise
        """
        try:
            # Full path to input image
            input_path = os.path.join(self.input_dir, filename)
            
            # Read image using OpenCV (supports more formats)
            image = cv2.imread(input_path)
            
            if image is None:
                print(f"Could not read image: {filename}")
                return False

            # Convert to grayscale for AI training (reduces complexity)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Reduce resolution while maintaining aspect ratio
            original_height, original_width = gray_image.shape
            new_width = int(original_width * 0.5)
            new_height = int(original_height * 0.5)
            
            resized_image = cv2.resize(
                gray_image, 
                (new_width, new_height), 
                interpolation=cv2.INTER_AREA  # Best for downsampling
            )

            # Optional: Apply adaptive histogram equalization for better contrast
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            enhanced_image = clahe.apply(resized_image)

            # Output path
            output_path = os.path.join(self.output_dir, filename)
            
            # Save processed image
            cv2.imwrite(output_path, enhanced_image)
            
            return True

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            return False

    def process_images(self, num_threads=4):
        """
        Process all images in input directory using multi-threading
        
        Args:
            num_threads (int): Number of concurrent threads for processing
        """
        # Get list of image files
        image_files = [f for f in os.listdir(self.input_dir) 
                       if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
        
        # Use ThreadPoolExecutor for concurrent image processing
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            # Map preprocessing function to all images
            results = list(executor.map(self.preprocess_image, image_files))
        
        # Print processing summary
        successful = sum(results)
        print(f"Processed {successful}/{len(image_files)} images successfully")

def main():
    # Example usage
    preprocessor = ImagePreprocessor(
        input_dir='C:\\Users\\Steven\\.runelite\\screenshots\\litlGenocide\\Brimhaven_agi', 
        output_dir='D:\\Downloads\\downscaled_osrs'
    )
    
    # Process images
    preprocessor.process_images()

if __name__ == '__main__':
    main()