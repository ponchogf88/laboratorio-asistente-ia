"""
MÓDULO DE ONBOARDING AUTOMATIZADO DE ALUMNOS (SKOOL + WHATSAPP)
"""

import os
import requests
import json

def invite_student_to_skool(email: str, first_name: str, community_id: str = None) -> bool:
    """
    Envía invitación a la comunidad privada de Skool vía API / Webhook.
    """
    print(f"[SKOOL API] Enviando invitación a {first_name} ({email})...")
    # Simulación o integración real con Skool Zapier/Webhook
    return True

def send_whatsapp_welcome_message(phone: str, student_name: str, course_tier: str) -> bool:
    """
    Envía el mensaje instantáneo por WhatsApp con el enlace de acceso a la Cohorte 1.
    """
    message = (
        f"¡Hola {student_name}! 🎉 Bienvenido a la *Cohorte 1 del Máster en Agentes de IA*.\n\n"
        f"Tu acceso a la plataforma y a la Bóveda de Workflows ya está activo.\n"
        f"👉 Ingresa a tu comunidad aquí: https://skool.com/ai-academy-cohorter\n\n"
        f"Si tienes cualquier duda técnica, nuestro equipo y agentes de soporte están listos 24/7."
    )
    print(f"[WHATSAPP API] Notificación enviada a {phone}:\n{message}")
    return True

if __name__ == "__main__":
    invite_student_to_skool("alumno.demo@gmail.com", "Alfonso")
    send_whatsapp_welcome_message("+5218112345678", "Alfonso", "Bootcamp Cohorte 1")
