from requests_html import HTMLSession
import datetime


URL = 'https://nuevachevallier.centraldepasajes.com.ar/empresa.aspx?'
JUNIN = '(JUN)+Junin+(Buenos+Aires)+(Argentina)'
ID_JUN = '189'
PERGAMINO = '(PERG)+Pergamino+(Buenos+Aires)+(Argentina)'
ID_PERG = '3222'
TIPO_VIAJE = '&TipoViaje=off'
VUELTA ='&FechaVta='
TOKEN = 'rZvGIQnx7OcreHC53Jiul9SxnvejVj%2fO'



def get_departures( origen_destino, dia=None ):

    session = HTMLSession()
    fecha_ida = datetime.date.today()
    fecha_ida = fecha_ida.__format__('%d/%m/%Y')
    print(fecha_ida)
    if (dia == 'm'):
        mañana = datetime.date.today()+ datetime.timedelta(days=1)
        fecha_ida = mañana.__format__('%d/%m/%Y')   
        print(fecha_ida)
    if (origen_destino == 'PJ'):
        r = session.get(URL+'Origen='+PERGAMINO+'&IdOrigen='+ID_PERG+
                        '&Destino='+JUNIN+'&IdDestino='+ID_JUN+
                        TIPO_VIAJE+'&FechaIda='+str(fecha_ida)+
                        VUELTA+'&Token='+TOKEN
                        )
    table = r.html.find('.table',first = True)
    #print(table.html)

    fh = open("index.html", "w")
    fh.write( str(table.html) )
    fh.close()

def main():
    get_departures('PJ', dia='m' )


if __name__ == '__main__':
    main()
