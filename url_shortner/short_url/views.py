from django.shortcuts import render, redirect
import secrets, string

from .boto3_files import update_db_item, get_db_item

# Create your views here.


def index(request):
    shortened = False
    if request.method == 'POST':
        # Handle the form submission
        original_url = request.POST['original_url']
        short_url = generate_short_url()
        shortened_url = request.build_absolute_uri(f'/dev/{short_url}')

        result = update_db_item.update_db_item(short_url, original_url)
        if result:
            shortened = True
            return render(request, 'index.html', {
                'shortened': shortened,
                'short_url': shortened_url
            })
        
            # Here you would typically save the URL and return the shortened version
            # For demonstration purposes, we assume the URL is saved successfully
        else:
            # Handle form errors
            return render(request, 'index.html', { 'error': 'Invalid URL'})
        # Here you would typically shorten the URL and return the result
        
    else:
        return render(request, 'index.html', {
            'shortened': shortened,
            
            })

def generate_short_url():
    length = 7 # Length of the shortened URL
    # Here you would implement the logic to shorten the URL
    # For demonstration purposes, let's just return a dummy shortened URL
    
    url_characters = string.ascii_letters + string.digits
    short_url = ''.join(secrets.choice(url_characters) for _ in range(length))
    return short_url


def redirect_to_original_url(request, short_url):
    url = get_db_item.get_db_item(short_url)
    print(url, " =========================")
    if url:
        return redirect(url)