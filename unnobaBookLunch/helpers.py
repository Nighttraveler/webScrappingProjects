import re


def print_HTML(browser):

   print browser.response().read()

   pass


def print_forms(browser):

	for form in browser.forms():
	   print "Form name:", form.name
	   print form

	pass


def print_form_controls(form):
   
   	print '\nPrinting {} controls:'.format(form.name)
	for control in form.controls:
	  print control

	pass


def print_links(browser):
	print "\nPrinting Links:\n"
	for link in browser.links():
		print link,'\n'

	pass