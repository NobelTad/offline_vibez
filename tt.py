import eyed3

audiofile = eyed3.load("Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster).mp3")
if audiofile.tag and audiofile.tag.images:
    for img in audiofile.tag.images:
        with open("extracted_cover.jpg", "wb") as out:
            out.write(img.image_data)
    print("✅ Cover extracted as extracted_cover.jpg")
else:
    print("❌ No cover image found")
