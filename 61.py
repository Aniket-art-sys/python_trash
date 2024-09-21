import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Base URL for the manga images
base_url = "https://cdn.black-clover.org/file/flanbox/omniscient-reader/chapter-"
output_folder = "manga_chapters"  # Folder to store downloaded images
start_chapter = int(input("where to start from?"))  # Chapter to start downloading from
max_chapters = int(input("where to end?"))   # Max chapters to download
images_per_chapter = 50  # Max number of pages to check per chapter
start_page = 1  # Page to start downloading from
num_workers = 4  # Number of parallel download threads


# Function to download an image
def download_image(chapter, page):
    url = f"{base_url}{chapter}/{page}.webp"
    image_path = os.path.join(output_folder, f"chapter_{chapter}", f"{page}.webp")

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
            return True
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
    return False


# Function to download a chapter
def download_chapter(chapter, start_page):
    chapter_folder = os.path.join(output_folder, f"chapter_{chapter}")

    # Create chapter folder if it doesn't exist
    if not os.path.exists(chapter_folder):
        os.makedirs(chapter_folder)

    print(f"Downloading Chapter {chapter}...")

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for page in range(start_page, start_page + images_per_chapter):
            futures.append(executor.submit(download_image, chapter, page))

        for future in tqdm(as_completed(futures), total=len(futures), desc=f"Chapter {chapter}", unit="page"):
            if not future.result():
                print(f"Reached end of Chapter {chapter} or failed to download page.")
                break


# Function to generate an HTML file to view the chapters
def generate_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Manga Viewer</title>
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
    for chapter in range(start_chapter, start_chapter + max_chapters):
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

    for chapter in range(start_chapter, start_chapter + max_chapters):
        download_chapter(chapter, start_page)

    generate_html()


if __name__ == "__main__":
    main()
