from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from translate import Translator

def home(request):
    return render(request,"new.html")

# def scrape_page(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         response = requests.get(url)
#         if response.status_code == 200:
#             content = response.content
#             soup = BeautifulSoup(content, 'html.parser')

#             # Extract text content within <p> tags
#             paragraphs = soup.find_all('p')
#             paragraph_text = [p.get_text() for p in paragraphs]

#             # Save paragraph text to a text file
#             file_path = 'paragraphs.txt'
#             #  'paragraphs.txt'
#             with open(file_path, 'w') as file:
#                 for paragraph in paragraph_text:
#                     file.write(paragraph + '\n')

#             return HttpResponse("Paragraphs scraped and saved successfully.")
#         else:
#             return HttpResponse("Error: Unable to fetch content from the provided URL.")
#     return render(request, 'page1.html')


# def scrape_page(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         response = requests.get(url)
#         if response.status_code == 200:
#             content = response.content
#             soup = BeautifulSoup(content, 'html.parser')

#             # Extract text content within <p> tags
#             paragraphs = soup.find_all('p')
#             paragraph_text = [p.get_text() for p in paragraphs]

#             # Save paragraph text to a text file
#             file_path = 'paragraphs.txt'
#             with open(file_path, 'w') as file:
#                 for paragraph in paragraph_text:
#                     file.write(paragraph + '\n')

#             return render(request, 'result.html', {'paragraph_text': paragraph_text})
#         else:
#             return HttpResponse("Error: Unable to fetch content from the provided URL.")
#     return render(request, 'page1.html')


# from django.http import HttpResponse
# from django.core.files import File
# import os

# def download_paragraphs(request):
#     file_path = 'paragraphs.txt'  # Path to the saved text file

#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as file:
#             response = HttpResponse(File(file), content_type='text/plain')
#             response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
#             return response
#     else:
#         return HttpResponse("File not found.")

def scrape_page(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        lang = request.POST.get('language')
        print(lang)
        print("url is",url)
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content
            soup = BeautifulSoup(content, 'html.parser')
            
            text_content = soup.get_text()

        
            translator = Translator(to_lang=lang) 
            translated_text = translator.translate(text_content)

            return render(request, 'result.html', { 'translated_text': translated_text})
        else:
            return HttpResponse("Error: Unable to fetch content from the provided URL.")
    return render(request, 'page1.html')
