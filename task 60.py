import os
import requests
from bs4 import BeautifulSoup

# Base URL for the manga images
base_url = "https://cdn.black-clover.org/file/flanbox/omniscient-reader/chapter-"
output_folder = "manga_chapters"  # Folder to store downloaded images
max_chapters = int(input("How many chapters to downlaod?"))  # Max chapters to download
images_per_chapter = 10  # Max number of pages to check per chapter


# Function to download an image
def download_image(chapter, page, folder_path):
    url = f"{base_url}{chapter}/{page}.webp"
    response = requests.get(url)

    # Check if the page exists (status code 200)
    if response.status_code == 200:
        image_path = os.path.join(folder_path, f"{page}.webp")
        with open(image_path, 'wb') as f:
            f.write(response.content)
        return True
    return False


# Function to download a chapter
# Function to download a chapter
def download_chapter(chapter):
    chapter_folder = os.path.join(output_folder, f"chapter_{chapter}")

    # Create chapter folder if it doesn't exist
    if not os.path.exists(chapter_folder):
        os.makedirs(chapter_folder)

    print(f"Downloading Chapter {chapter}...")

    page = 1
    while True:  # Loop until a missing page is encountered
        if not download_image(chapter, page, chapter_folder):
            print(f"Reached end of Chapter {chapter} at page {page}.")
            break
        page += 1


# Function to generate an HTML file to view the chapters
def generate_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>orv reader</title>
        <style>
            img {
                display: block;
                width: 100%;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
    <h1>Manga Viewer</h1>
    """

    # Loop through the downloaded chapters
    for chapter in range(1, max_chapters + 1):
        chapter_folder = os.path.join(output_folder, f"chapter_{chapter}")
        if os.path.exists(chapter_folder):
            html_content += f"<h2>Chapter {chapter}</h2>\n"
            # Add images for each page in the chapter
            for img_file in sorted(os.listdir(chapter_folder)):
                img_path = os.path.join(chapter_folder, img_file)
                html_content += f'<img src="{img_path}" alt="Chapter {chapter} - Page {img_file.split(".")[0]}">\n'

    html_content += "</body></html>"

    # Write the HTML content to a file
    with open("manga_viewer.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print("HTML file generated: manga_viewer.html")


# Main function to download chapters and generate HTML
def main():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for chapter in range(1, max_chapters + 1):
        download_chapter(chapter)

    generate_html()


if __name__ == "__main__":
    main()
