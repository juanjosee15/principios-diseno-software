#sistema de notificaciones en Python

from abc import ABC, abstractmethod

# Interfaz para diferentes tipos de notificación
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

# Implementación concreta para enviar notificaciones por correo
class NotificadorCorreo(Notificador):
    def enviar(self, mensaje: str):
        print(f"📧 Enviando correo: {mensaje}")

# Implementación concreta para enviar notificaciones por SMS
class NotificadorSMS(Notificador):
    def enviar(self, mensaje: str):
        print(f"📱 Enviando SMS: {mensaje}")
# Clase de servicio que depende de la abstracción, no de una implementación específica
class ServicioNotificacion:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador
    
    def notificar_usuario(self, mensaje: str):
        self.notificador.enviar(mensaje)
# Probando el sistema con diferentes tipos de notificación
if __name__ == "__main__":
    # Notificación por correo
    notificador_correo = NotificadorCorreo()
    servicio_correo = ServicioNotificacion(notificador_correo)
    servicio_correo.notificar_usuario("Tu pedido ha sido enviado. 📦")

    # Notificación por SMS
    notificador_sms = NotificadorSMS()
    servicio_sms = ServicioNotificacion(notificador_sms)
    servicio_sms.notificar_usuario("Tu código de verificación es 1234. 🔢")
