from pathlib import Path

#Práctica Path 1 RUTA BASE
ruta_base = Path.home()

#Práctica Path 2 PATH DE PARENTS: 
ruta = Path("Curso Python","Día 6","practicas_path.py")

#Práctica Path 3
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")