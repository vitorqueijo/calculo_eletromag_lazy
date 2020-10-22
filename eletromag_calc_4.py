"""
@author: vitor.queijo

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

"""
import math


k_e = 8.99e09
#obs: se vc for um programador POO purista, morra de ansiedade vendo meu código

def calculo_direta(d, m, angulo):
	return (math.pow(d,2)*((9.8)*m))*((math.pow(math.sin(math.radians(angulo)), 3))/math.cos(math.radians(angulo)))


def calculo_da_equacao(d, m, angulo):
	partial_result = calculo_direta(d, m, angulo)
	return math.sqrt(partial_result/k_e)

def calculo_media(lista_de_variavel):
	return sum(lista_de_variavel)/len(lista_de_variavel)

def calculo_forca(lista_de_cargas, d):
	lista_de_forcas = []
	for carga in lista_de_cargas:
		lista_de_forcas.append((k_e*math.pow(carga, 2))/math.pow(d,2))
	return lista_de_forcas

def calculo_desvio_padrao(lista_de_variavel, variavel_media):
	sigma = []
	n = len(lista_de_variavel)

	for variavel in lista_de_variavel:
		sigma.append(math.pow((variavel - variavel_media), 2))
	
	return math.sqrt(sum(sigma)/(n*(n-1)))

if __name__ == '__main__':

	lista_de_cargas = []
	lista_de_angulo = [15.0, 17.0, 16.5, 17.5, 16.0, 18.0, 16.5, 17.5, 16.0, 16.5]

	for angulo in lista_de_angulo:
		lista_de_cargas.append(calculo_da_equacao(6.2e-02, 70e-06, angulo))
		print("O angulo " + str(angulo) + " a carga é igual à: " + str(calculo_da_equacao(6.2e-02, 70e-06, angulo)))

	carga_media = calculo_media(lista_de_cargas)
	lista_de_forcas = calculo_forca(lista_de_cargas, 6.2e-02)
	forca_media = calculo_media(lista_de_forcas)
	desvio_carga = calculo_desvio_padrao(lista_de_cargas, carga_media)
	desvio_forca = calculo_desvio_padrao(lista_de_forcas, forca_media)
	print("lista de forças: ", lista_de_forcas)
	print("\nlista de cargas calculadas: ", lista_de_cargas)
	print("\ncarga média: ", carga_media)
	print("\nforça média: ", forca_media)
	print("\ndesvio da força: ", desvio_forca)
	print("\ndesvio da carga: ", desvio_carga)


