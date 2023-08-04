#Code by bigmohammad
#---------------------
#Youtube: bigmohammad
#---------------------
#Instagram: bigmohammad.official
from PIL import Image

def main():
    # Get the file location from the user
    file_location = input("Please enter the file location of the image: ")

    try:
        # Open the image file
        img = Image.open(file_location)

        # Display initial image information
        print("Current image format:", img.format)
        print("Image size:", img.size)

        # Ask the user to choose a new format
        new_format = input("Please select the new image format (jpg, png, etc.): ")
        new_format = new_format.lower()  # Convert input to lowercase

        # Handle 'jpg' and 'JPG' inputs
        if new_format == 'jpg':
            new_format = 'jpeg'

        # Change the format and save the image with the new format
        img.save("new_image." + new_format, format=new_format)

        print("Image successfully saved with the new format.")
    except Exception as e:
        print("Error processing the image: ", e)

if __name__ == "__main__":
    main()
