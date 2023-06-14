print ("Bienvenidos al juego de las capitales! Responde todas las preguntas correctamente y ganarás.")
preguntes= dict([('Cuál es la capital de Andorra?', 'Andorra la Vieja'),
('Cuál es la capital de Argentina?', 'Buenos aires'),
('Cuál es la capital de Austria?', 'Viena'),
('Cuál es la capital de Cuba?', 'La Habana'),
('Cuál es la capital de Egipto?', 'El Cairo'),
('Cuál es la capital de Indonesia?', 'Yakarta'),
('Cuál es la capital de Mozambique?', 'Maputo'),
('Cuál es la capital de Tailandia?',' Bangkok'),
('Cuál es la capital de Tonga?', 'Nukualofa'),
('Cuál es la capital de Zambia?', 'Lusaka')]);
contPregunta=0;
contVidas=3;
respuestascorrectas=0
if contVidas == 0:
 print("Has perdido")
while contPregunta < 11 :

  print(list(preguntes.keys())[contPregunta]);
  respuesta=input("Introduce:");
  if respuesta == list(preguntes.values())[contPregunta]:
    print("Respuesta correcta");
    respuestascorrectas=respuestascorrectas+1;
    contPregunta=contPregunta+1;
  else:
    print("respuesta incorrecta");
    print(contVidas);
    contPregunta=contPregunta+1;
    contVidas=contVidas-1;

