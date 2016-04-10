from django.shortcuts import render

from forms import ContactForm

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context


# Create your views here.

def contact_me( request):
	form = ContactForm
	if request.method == 'POST':
		form = form(data = request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

			template = get_template('contact_template.txt')
			context = Context({
				'contact_name':contact_name,
				'contact_email':contact_email,
				'form_content':form_content
				})

			content = template.render (context)

			email = EmailMessage ('New contact form submission', content, headers = {'Reply-To':contact_email})
			email.send()
			return redirect ('contact')


	return render (request, 'pages/contacts.html', {'form':form})