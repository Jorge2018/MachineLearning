def beCheerful(name='', repeat=2):		# establecer valores predeterminados al declarar los parámetros
	print(f"good morning {name}\n" * repeat)
beCheerful()				# output: Buenos dias (repetido en 2 lineas)
beCheerful("tim")		        # output: Buenos días tim (repetido en 2 líneas)
beCheerful(name="john")			# output: buenos días john (repetido en 2 líneas)
beCheerful(repeat=6)			# output: Buenos dias (repetido en 6 lineas)
beCheerful(name="michael", repeat=5)	# output: buenos días michael (repetido en 5 líneas)
# NOTA: ¡el orden de los argumentos no importa si somos explícitos al enviar nuestros argumentos!
beCheerful(repeat=3, name="kb")		# output: Buenos dias kb (repetido en 3 lineas)

beCheerful()