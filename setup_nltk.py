import nltk

REQUIRED_RESOURCES = [
    ("tokenizers/punkt", "punkt"),
    ("tokenizers/punkt_tab", "punkt_tab"),
    ("corpora/stopwords", "stopwords"),
]


def main():
    print("Checking NLTK resources...")
    for resource_path, package_name in REQUIRED_RESOURCES:
        try:
            nltk.data.find(resource_path)
            print(f"  ✓ {package_name}")
        except LookupError:
            print(f"  ↓ Downloading {package_name}...")
            if not nltk.download(package_name):
                raise SystemExit(f"Failed to download NLTK resource: {package_name}")

    print("NLTK resources are ready.")


if __name__ == "__main__":
    main()
