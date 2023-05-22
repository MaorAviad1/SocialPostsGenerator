import os
import pandas as pd

# Assuming the folder path is /path/to/images
folder_path = '/path/to/images'

# Load the events and garments from text files
with open('events.txt', 'r') as f:
    events = f.read().splitlines()
with open('garments.txt', 'r') as f:
    garments = f.read().splitlines()

# Get a list of all PNG images in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

# Define your call to action and hashtags
call_to_action = "Buy now this amazing unique {design} {garment} for {event}"
hashtags = "#Fashion #NewCollection #ShopNow"


# Function to create a post text
def create_post(image_name, platform):
    # Extract details from filename
    garment, event, design = os.path.splitext(image_name)[0].split('_')

    # Verify the garment and event exist
    if garment not in garments or event not in events:
        return

    # Format the call to action
    post_text = call_to_action.format(design=design, garment=garment, event=event)
    post_text += f" {hashtags} {image_name}"

    # Define the character limits
    char_limits = {
        "facebook": 63206,
        "instagram": 2200,
        "twitter": 280,
        "pinterest": 500
    }

    # Check the character limit for the given platform
    if len(post_text) > char_limits[platform]:
        # If the post text exceeds the limit, cut it down
        post_text = post_text[:char_limits[platform]]

    # For Instagram, we also want to limit the characters before the "more" button
    if platform == "instagram" and len(post_text) > 125:
        post_text = post_text[:125] + '...' + post_text[125:]

    return post_text


# Create a dataframe
df = pd.DataFrame()

# Fill dataframe with post information
df['image_path'] = [os.path.join(folder_path, image_file) for image_file in image_files]
df['facebook_post'] = [create_post(image_file, "facebook") for image_file in image_files]
df['instagram_post'] = [create_post(image_file, "instagram") for image_file in image_files]
df['twitter_post'] = [create_post(image_file, "twitter") for image_file in image_files]
df['pinterest_post'] = [create_post(image_file, "pinterest") for image_file in image_files]

# Write to CSV
df.to_csv('social_media_posts.csv', index=False)
