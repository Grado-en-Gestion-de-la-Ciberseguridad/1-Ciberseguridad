class usuario: 
    def __int__(self, dni, nombre, apellidos, correo): 
        self__dni = dni 
        self.nombre = nombre 
        self__contra = ""
        self.correo =  correo 
        self.username = self.GenerarUser ()
        self.apellidos = apellidos 
    def GenerarUser (self): 
        return self__dni [0:3]+self.nombre 