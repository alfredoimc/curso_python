Python 2.7.8 (default, Jun 18 2015, 18:54:19) 
[GCC 4.9.1] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> arquivo = open('numero.txt','w')
>>> for linha in range(1,101):
	arquivo.write('%d\n' %linha)	
>>> arquivo.close()
