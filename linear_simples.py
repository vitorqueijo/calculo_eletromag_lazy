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


class linearizacao_na_mao:
	def __init__(self, list_x, list_y):
		self.list_x = list_x
		self.list_y = list_y
		self.list_xy = [round(x*y, 4) for x,y in zip(self.list_x, self.list_y)]
		self.list_x_sqrt = [round(x*x, 4) for x in self.list_x]
		self.list_y_sqrt = [round(y*y, 4) for y in self.list_y]
		self.result_b = float()
		self.result_a = float()

	def __discover_b(self):
		n = len(self.list_xy)
		media_x = (sum(self.list_x))/n
		media_y = (sum(self.list_y))/n
		self.result_b = round((sum(self.list_xy) - n*(media_y*media_x))/(sum(self.list_x_sqrt) - n*sum(self.list_y_sqrt)), 6)

	def __discover_a(self):
		# dado que a = Ym - b*Xm
		self.result_a = round(((sum(self.list_y))/(len(self.list_y))) - self.result_b*((sum(self.list_x))/(len(self.list_x))), 6)

	def mostrar_funcao_linear(self):
		self.__discover_b()
		self.__discover_a()
		print(" Y = " + str(self.result_a) + "+ X * "+ str(self.result_b))

if __name__ == '__main__':
	lista_y = [] # x list
	lista_x = [] # y list
	if (len(lista_x)==len(lista_y)):
		linear = linearizacao_na_mao(lista_x, lista_y)
		linear.mostrar_funcao_linear()
	else:
		print("tem que ser o mesmo tamanho!")