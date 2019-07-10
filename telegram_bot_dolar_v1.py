# -*- coding: utf-8 -*-
# Con este comando puedo ver los chat_id
# curl https://api.telegram.org/xxxxxx/getUpdates
# El nombre de las variables estan invertidas porque en la web estan asi. Digamos compra es venta y venta es compra :)
import urllib2,json, time, telebot

req = urllib2.Request('https://www.balanz.com/api/cotizacionmoneda/2')
req.add_header('cookie', '__zlcmid=rbi885ikjzQiAd')
req.add_header('Accept', 'application/json')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
resp = urllib2.urlopen(req)
content = resp.read()
data = json.loads(content)
dolarcompra = data["Cotizacion"]['PrecioVenta']
dolarventa = data["Cotizacion"]['PrecioCompra']
print "Valor compra inicial: %s" %dolarcompra
print "Valor venta inicial: %s" %dolarventa

def ejecutaScript():
        global dolarcompra, dolarventa
        fechacompleta = time.strftime("%Y-%m-%d %H:%M")
        req = urllib2.Request('https://www.balanz.com/api/cotizacionmoneda/2')
        req.add_header('cookie', '__zlcmid=rbi885ikjzQiAd')
        req.add_header('Accept', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
        resp = urllib2.urlopen(req)
        content = resp.read()
        data = json.loads(content)
        compra = data["Cotizacion"]['PrecioVenta']
        venta = data["Cotizacion"]['PrecioCompra']
        TOKEN = 'XXXXXXX' #token del bot de telegram
        tb = telebot.TeleBot(TOKEN)
        tb.get_me()

        if dolarcompra!= compra:
                comprafull = "Compra: %s" %compra
                comenzar = "-----------------------------"
                tb.send_message(-123456,fechacompleta) #ID del mensaje iniciado con el bot
                tb.send_message(-123456,comprafull)#ID del mensaje iniciado con el bot
                tb.send_message(-123456,comenzar)#ID del mensaje iniciado con el bot
                print ""
                print "Compra diferente %s - %s" %(dolarcompra,compra)
                print ""
                dolarcompra = compra

        else:
            print ""
            print "Compra %s" %fechacompleta
            print "Compra iguales %s %s" %(dolarcompra,compra)
            print ""

        if dolarventa != venta:
                ventafull = "Venta: %s"  %venta
                comenzar = "-----------------------------"
                tb.send_message(-123456,fechacompleta)#ID del mensaje iniciado con el bot
                tb.send_message(-123456,ventafull)#ID del mensaje iniciado con el bot
                tb.send_message(-123456,comenzar)#ID del mensaje iniciado con el bot
                print ""
                print "Venta diferente %s - %s" %(dolarventa,venta)
                print ""
                #dolarventa = venta

        else:
            print ""
            print "Venta %s" %fechacompleta
            print "Venta iguales %s - %s" %(dolarventa,venta)
            print ""


        time.sleep(300)


while True:

        ejecutaScript()