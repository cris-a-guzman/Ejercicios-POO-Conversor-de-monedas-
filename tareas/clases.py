
class ListaTareas:
    def __init__(self,nombre):
        self.lista_tareas = []
        self.nombre = nombre

    def agregar_tarea(self,tarea):
        self.lista_tareas.append(tarea)
    
    def eliminar_tarea(self, indice):
        eliminada = self.lista_tareas.pop(indice)
        return eliminada
    
    def completar_tarea(self, indice):
        self.lista_tareas[indice].estado = True
        completada = self.lista_tareas[indice]
        return completada


    def __len__(self):
        return len(self.lista_tareas)
    
    def __str__(self):
        resultado = ""
        for i, tarea in enumerate(self.lista_tareas):
            if tarea.estado == False:
                resultado += f"{i+1} - {tarea.nombre.title()} | Estado: Incompleta\n"
            else:
                resultado += f"{i+1} - {tarea.nombre} | Estado: Completa\n"
        return resultado
    

class Tarea:
    def __init__(self,nombre,descripcion,estado=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self) -> str:
        if self.estado:
            return f"{self.nombre.title()} | Descripcion: {self.descripcion.title()} | Estado: Completa"
        else:
            return f"{self.nombre.title()} | Descripcion: {self.descripcion.title()} | Estado: Incompleta"
        
