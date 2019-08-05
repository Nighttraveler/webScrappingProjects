# -*- coding: utf-8 -*-
import sys, logging
import re

from mechanize import Browser, CookieJar

import helpers, settings

reload(sys)
sys.setdefaultencoding("utf-8")


def login(browser):

   browser.select_form(name='j_idt42')
   login_form = browser.form

   login_form['j_idt42:username'] = settings.EMAIL
   login_form['j_idt42:password'] = settings.PASSWORD
   login_form.controls[4].__dict__["name"] = 'j_idt42:j_idt46'
   login_form.controls[4]._value= 'j_idt42:j_idt46'

   browser.submit()

   pass


def submit_reservar(browser):

   browser.select_form(name='formRepeat')
   formRepeat = browser.form
   formRepeat.controls[1].__dict__["name"] = "formRepeat:j_idt36"
   formRepeat.controls[1]._value = "formRepeat:j_idt36"   

   browser.submit()

   pass


def submit_day(browser, carta):
   browser.select_form(name='j_idt18')

   day_form = browser.form
   day_form.controls[1].__dict__['name'] = 'j_idt18:j_idt20:4:j_idt26'
   day_form.controls[1]._value = 'j_idt18:j_idt20:4:j_idt26'

   day_form.controls[2].__dict__['name'] = 'cartas'
   day_form.controls[2]._value = carta

   browser.submit()

   pass


def submit_confirm_reserva(browser):
   browser.select_form(name='formConfirmReserva')   
   bookLunchForm = browser.form

   bookLunchForm.controls[1].__dict__["name"] = "formConfirmReserva:linkSinVoucher"
   bookLunchForm.controls[1]._value = "formConfirmReserva:linkSinVoucher"

   browser.form = bookLunchForm

   browser.submit()

   pass


def get_cartas_id(browser):

   cartas_id = list()

   for link in browser.links():
      match = re.search('value:\'(\d+)\'', str(dict(link.attrs).get('onclick')))
      if match:
         cartas_id.append(match.group(1))
   return cartas_id

   pass



if __name__ == '__main__':

   if not (settings.EMAIL or settings.HOST_URL or settings.PASSWORD ):
      print "Please Fill EMAIL,PASSWORD and HOST_URL on settings.py!"
      print "Exiting"
      exit()

   browser = Browser()

   debug_headers_flag = False
   try:
      debug_headers_flag = sys.argv[1] == '-d'
   except IndexError as e:
      None

   if debug_headers_flag:
      browser.set_debug_http(True)
   
   cookies = CookieJar()
   
   browser.set_handle_refresh(False)
   browser.set_handle_robots(False)
   browser.set_cookiejar(cookies)

   browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0')]

   browser.open(settings.HOST_URL)

   login(browser)

   for index,carta in enumerate(get_cartas_id(browser)):
      print("Booking Menu N° {}".format(carta))
      submit_day(browser, carta)
      link_text_day = browser.find_link(text_regex="\d+\/\d+\/\d+", nr=index)

      l = browser.links(text="Reservar")
      match = re.search("\('(.*)'\)", dict(l.next().attrs).get("onclick"))
      if match:
         print("{0} {1}\n".format(link_text_day.text, match.group(1)))
      else:
         print("{}".format(link_text_day.text))
      submit_reservar(browser)
      submit_confirm_reserva(browser)