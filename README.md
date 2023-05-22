# Social Media Post Generator

This script automatically generates social media posts for a collection of images. It's especially useful for print on demand services, creating a unique post for each design for various social media platforms: Facebook, Instagram, Twitter, and Pinterest.

The script reads the filenames of the images, which are expected to contain information about the garment type, event, and design. The filenames should follow this format: `garment_event_design.png` (e.g., `Shirt_FathersDay_BestDadEver.png`).

## Setup

1.  Install the necessary Python packages, if you haven't already done so:
    
    shellCopy code
    
    `pip install pandas` 
    
2.  Save the script as `post_generator.py`.
    
3.  Prepare two text files:
    
    -   `events.txt`: a list of events, one per line.
    -   `garments.txt`: a list of garment types, one per line.
    
    Make sure all garment types and events used in your image filenames are listed in these files.
    
4.  Adjust the `folder_path` in the script to point to the directory containing your images.
    
5.  Optionally, adjust the `call_to_action` and `hashtags` in the script to suit your needs.
    

## Usage

Run the script with Python:

shellCopy code

`python post_generator.py` 

The script will generate a CSV file named `social_media_posts.csv`. This file will contain a row for each image and a column for each platform's post. The posts are automatically trimmed to meet the character limits of each platform.

## Output

The output CSV file will have the following columns:

-   `image_path`: The full path to the image file.
-   `facebook_post`: The post text for Facebook.
-   `instagram_post`: The post text for Instagram. Only the first 125 characters will be visible before the "more" button.
-   `twitter_post`: The post text for Twitter.
-   `pinterest_post`: The post text for Pinterest.

Each row corresponds to a different image.

## Notes

-   If an image's filename does not contain a garment type or event listed in `garments.txt` or `events.txt`, respectively, the script will skip that image.
-   The Instagram post is formatted to show only the first 125 characters before the "more" button. This is indicated with an ellipsis (...), which is added automatically when the post exceeds this limit.
