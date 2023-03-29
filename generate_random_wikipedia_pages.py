import wikipedia

def generate_random_wikipedia_pages(num_pages):
    page_names = set()

    while len(page_names) < num_pages:
        try:
            page_name = wikipedia.random(1)
            page_names.add(page_name)
        except wikipedia.exceptions.DisambiguationError:
            continue

    return page_names

if __name__ == "__main__":
    num_pages = 50
    page_names = generate_random_wikipedia_pages(num_pages)

    with open("wikipedia_pages.txt", "w") as f:
        for page_name in page_names:
            f.write(f"{page_name}\n")

    print(f"Generated {num_pages} random Wikipedia page names.")
