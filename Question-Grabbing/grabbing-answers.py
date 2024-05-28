from bs4 import BeautifulSoup

# Replace 'yourfile.html' with the path to your downloaded HTML file
file_path = 'q21.html'

# Open and read the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the passage text within the HTML structure
passage_text = soup.find('div', class_="passage-text")

# Extract and combine the text from each span within the passage text
background_info = " ".join([span.text for span in passage_text.find_all('span')])

print(background_info)

# Find all list items which contain the choices
choices = soup.find_all('li', class_="perseus-radio-option")

# Extract and print the text from each choice
for idx, choice in enumerate(choices):
    choice_text = choice.find('div', class_='paragraph').text.strip()
    print(f"Choice {chr(65 + idx)}: {choice_text}")