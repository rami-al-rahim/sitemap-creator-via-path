import os
# data
siteMapTemplate = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    replace_here
    <!--  Add more URLs as needed  -->
</urlset>
'''


# user inputs
path = input("Enter the path to the directory: ")
mainDomain = input("Enter the main domain (e.g rami-dev.com): ").removeprefix(' ')
isHttps = ""
while True:
    isHttps = input("Is Https: (Y/N) ")
    if isHttps.upper() in ['Y', 'N']:
        break
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

URL = "https" if isHttps == "Y" else "http" + "://" + mainDomain 

print(f"URL: {URL}")

# Function to find all HTML files in a directory and its subdirectories


def find_html_files(directory):
    """Recursively find all HTML files in the given directory and its subdirectories."""
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                full_path = os.path.join(root, file)
                html_files.append(full_path)
    return html_files

# Replace with your target directory path


if not os.path.exists(path):
    print(f"The path '{path}' does not exist.")
else:
    # Find all HTML files
    html_files = find_html_files(path)
    # Print the results
    if html_files:
        print(f"Found {len(html_files)} HTML file(s):")
        urls = ''
        for file in html_files:
            content = '''
            <url>
<loc>urls_data</loc>
<priority>1.0</priority>
</url>
'''.replace("urls_data", file.replace(path, URL))
            urls += content
            siteMap = siteMapTemplate.replace("replace_here", urls.replace('\\', "/"))
            with open('output-sitemap.xml', 'w') as file:
                file.write(siteMap)
            # see output-sitemap.xml file to see generated sitemap
    else:
        print("No HTML files found.")
