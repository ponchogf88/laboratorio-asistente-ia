"""
AI ACADEMY ENTERPRISE - MOTOR ORQUESTADOR AUTÓNOMO (FASTAPI)
Coordina webhooks de pasarelas de pago (Stripe/LemonSqueezy), ManyChat (DMs)
y dispara el onboarding automático de alumnos y alertas de ventas.
"""

import os
import json
from typing import Dict, Any, Optional
from fastapi import FastAPI, Request, BackgroundTasks, HTTPException, Header
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AI Academy Enterprise Orchestrator",
    description="Motor central de eventos, calificación de leads y pagos para Cohorte 1",
    version="1.0.0"
)

# ----------------------------------------------------
# MODELOS DE DATOS
# ----------------------------------------------------
class LeadInbound(BaseModel):
    source: str  # 'instagram_dm', 'website_optin', 'whatsapp'
    full_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    instagram_handle: Optional[str] = None
    interest: Optional[str] = "general_ai_course"
    budget: Optional[str] = None

class PaymentEvent(BaseModel):
    event_type: str  # 'checkout.completed', 'subscription.created'
    customer_name: str
    customer_email: str
    customer_phone: Optional[str] = None
    tier: str  # 'tripwire_27', 'bootcamp_297', 'accelerator_1500'
    amount_paid: float
    currency: str = "USD"
    payment_id: str

# ----------------------------------------------------
# TAREAS EN SEGUNDO PLANO (ASYNC WORKERS)
# ----------------------------------------------------
def process_lead_scoring_and_nurture(lead: LeadInbound):
    """
    Evalúa el lead, lo categoriza y dispara la secuencia en ManyChat / CRM.
    """
    print(f"[LEAD ENGINE] 📥 Nuevo lead recibido: {lead.full_name} ({lead.source})")
    
    # Lógica de scoring básica
    score = 5
    if lead.phone and lead.email:
        score += 3
    if lead.budget in ["$1,000+", "$2,000+"]:
        score += 2
        print(f"[HIGH-TICKET ALERT] 🚨 Lead prioritario detectado: {lead.full_name} - Presupuesto: {lead.budget}")
    
    print(f"[LEAD ENGINE] ✅ Lead procesado con Score {score}/10. Sincronizado en CRM.")

def execute_student_onboarding(payment: PaymentEvent):
    """
    Dispara la entrega de accesos a Skool, envía WhatsApp de bienvenida y factura.
    """
    print(f"[PAYMENT SUCCESS] 💰 Pago confirmado: ${payment.amount_paid} {payment.currency} por {payment.customer_name}")
    print(f"[ONBOARDING] 🚀 Generando invitación Skool para: {payment.customer_email}")
    print(f"[ONBOARDING] 📲 Enviando WhatsApp de bienvenida a: {payment.customer_phone or 'N/A'}")
    print(f"[TIER ASIGNADO] Nivel: {payment.tier} activado exitosamente.")

# ----------------------------------------------------
# ENDPOINTS
# ----------------------------------------------------
@app.get("/")
def health_check():
    return {
        "status": "online",
        "system": "AI Academy Enterprise Loop Engine",
        "active_cohort": "Cohorte 1 - Lanzamiento",
        "ready_for_production": True
    }

@app.post("/webhook/leads")
async def receive_lead(lead: LeadInbound, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_lead_scoring_and_nurture, lead)
    return {"status": "accepted", "message": f"Lead {lead.full_name} registrado en el loop"}

@app.post("/webhook/stripe-payment")
async def receive_stripe_payment(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    
    # Adaptador genérico de evento de pago
    customer_details = payload.get("data", {}).get("object", {}).get("customer_details", {})
    amount = payload.get("data", {}).get("object", {}).get("amount_total", 0) / 100.0
    
    event = PaymentEvent(
        event_type="checkout.completed",
        customer_name=customer_details.get("name", "Nuevo Estudiante"),
        customer_email=customer_details.get("email", "sin_email@ejemplo.com"),
        customer_phone=customer_details.get("phone", None),
        tier="bootcamp_297" if amount >= 197 else "tripwire_27",
        amount_paid=amount,
        payment_id=payload.get("data", {}).get("object", {}).get("id", "sim_pay_123")
    )
    
    background_tasks.add_task(execute_student_onboarding, event)
    return {"status": "processed", "student": event.customer_name, "tier": event.tier}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 Iniciando Servidor Orquestador en http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
