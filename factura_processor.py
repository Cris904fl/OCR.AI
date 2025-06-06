import base64
import json
from mistralai import Mistral

# --- CONFIGURACIÓN ---
api_key = "d6EX4VjsmC8dmFc4nWprjASCj7eYNVj6"
image_path = r"C:\Users\ivan.cespedes\Downloads\Facturas\factura prueba.jpg"
output_path = r"C:\Users\ivan.cespedes\Downloads\Facturas\factura_prueba.json"

# --- CONEXIÓN CON MISTRAL ---
client = Mistral(api_key=api_key)

# --- CONVERTIR IMAGEN A BASE64 ---
with open(image_path, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

# --- PROCESO OCR ---
ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "image_url",
        "image_url": f"data:image/jpeg;base64,{image_base64}"
    }
)

ocr_text = ocr_response.text
print("📄 Texto extraído de la factura:\n")
print(ocr_text)

# --- PROMPT PARA ESTRUCTURAR EL TEXTO EN JSON ---
prompt = f"""
Ordena los datos del siguiente texto de factura en el siguiente formato JSON:
{{
  "fecha": "",
  "numero_remision": "",
  "cliente": {{
    "nombre": "",
    "nit": "",
    "direccion": "",
    "telefono": ""
  }},
  "productos": [
    {{
      "nombre": "",
      "cantidad": "",
      "unidad": "",
      "precio_unitario": "",
      "iva": "",
      "total": ""
    }}
  ],
  "totales": {{
    "subtotal": "",
    "iva": "",
    "descuentos": "",
    "total_pagar": ""
  }},
  "conductor": {{
    "nombre": "",
    "placa": ""
  }}
}}

Texto de la factura:
{ocr_text}
"""

# --- ESTRUCTURAR EL CONTENIDO COMO JSON ---
chat_response = client.chat(
    model="mistral-small",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

structured_json = chat_response.choices[0].message["content"]

# --- GUARDAR EN ARCHIVO .JSON ---
with open(output_path, "w", encoding="utf-8") as f:
    f.write(structured_json)

print(f"\n✅ JSON guardado en: {output_path}")