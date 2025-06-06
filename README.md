# Procesador de Facturas con OCR y Mistral AI

Este proyecto utiliza la API de Mistral AI para extraer texto de facturas mediante OCR y estructurar la información en formato JSON.

## 🚀 Características

- **OCR automático**: Extrae texto de imágenes de facturas
- **Estructuración inteligente**: Organiza los datos en formato JSON estructurado
- **Soporte para múltiples formatos**: Compatible con imágenes JPG, PNG, etc.
- **Procesamiento completo**: Extrae información de cliente, productos, totales y conductor

## 📋 Requisitos

### Dependencias
```bash
pip install mistralai
```

### Requisitos del sistema
- Python 3.7 o superior
- Conexión a internet para acceder a la API de Mistral

## 🔧 Configuración

### 1. Obtener API Key de Mistral
1. Regístrate en [Mistral AI](https://mistral.ai/)
2. Obtén tu API key desde el dashboard
3. Reemplaza el valor de `api_key` en el script

### 2. Configurar rutas de archivos
Modifica las siguientes variables en el script:
```python
image_path = r"ruta/a/tu/factura.jpg"
output_path = r"ruta/donde/guardar/resultado.json"
```

## 📁 Estructura del proyecto

```
proyecto/
│
├── factura_processor.py    # Script principal
├── README.md              # Este archivo
├── facturas/              # Carpeta para imágenes de facturas
│   └── factura_ejemplo.jpg
└── resultados/            # Carpeta para archivos JSON generados
    └── factura_ejemplo.json
```

## 🚀 Uso

### Ejecución básica
```bash
python factura_processor.py
```

### Ejemplo de salida JSON
```json
{
  "fecha": "2024-01-15",
  "numero_remision": "REM-001234",
  "cliente": {
    "nombre": "Empresa XYZ S.A.S",
    "nit": "900123456-7",
    "direccion": "Calle 123 #45-67, Bogotá",
    "telefono": "601-234-5678"
  },
  "productos": [
    {
      "nombre": "Producto A",
      "cantidad": "10",
      "unidad": "UN",
      "precio_unitario": "15000",
      "iva": "2850",
      "total": "152850"
    }
  ],
  "totales": {
    "subtotal": "150000",
    "iva": "28500",
    "descuentos": "0",
    "total_pagar": "178500"
  },
  "conductor": {
    "nombre": "Juan Pérez",
    "placa": "ABC-123"
  }
}
```

## 📊 Campos extraídos

El script extrae y estructura los siguientes campos:

### Información general
- **Fecha**: Fecha de la factura
- **Número de remisión**: Identificador único del documento

### Datos del cliente
- **Nombre**: Razón social o nombre del cliente
- **NIT**: Número de identificación tributaria
- **Dirección**: Dirección del cliente
- **Teléfono**: Número de contacto

### Productos
- **Nombre**: Descripción del producto
- **Cantidad**: Cantidad vendida
- **Unidad**: Unidad de medida
- **Precio unitario**: Precio por unidad
- **IVA**: Impuesto al valor agregado
- **Total**: Total por producto

### Totales
- **Subtotal**: Valor antes de impuestos
- **IVA**: Total de impuestos
- **Descuentos**: Descuentos aplicados
- **Total a pagar**: Valor final

### Información del conductor
- **Nombre**: Nombre del conductor
- **Placa**: Placa del vehículo

## ⚙️ Personalización

### Modificar el formato JSON
Para cambiar la estructura del JSON de salida, modifica la variable `prompt` en el script:

```python
prompt = f"""
Ordena los datos del siguiente texto de factura en el siguiente formato JSON:
{{
  // Tu estructura personalizada aquí
}}
"""
```

### Cambiar el modelo de Mistral
Puedes usar diferentes modelos modificando el parámetro `model`:
```python
# Para OCR
model="mistral-ocr-latest"

# Para estructuración
model="mistral-small"  # o "mistral-medium", "mistral-large"
```

## 🔒 Seguridad

- **API Key**: Nunca commits tu API key en repositorios públicos
- **Variables de entorno**: Considera usar variables de entorno para la API key:
  ```python
  import os
  api_key = os.getenv("MISTRAL_API_KEY")
  ```

## 🐛 Solución de problemas

### Error de conexión
- Verifica tu conexión a internet
- Confirma que tu API key sea válida

### Archivo no encontrado
- Verifica que las rutas de archivos sean correctas
- Asegúrate de que el archivo de imagen existe

### Calidad del OCR
- Usa imágenes de alta calidad
- Asegúrate de que el texto sea legible
- Evita imágenes borrosas o con mala iluminación

## 📝 Notas adicionales

- El script procesa un archivo a la vez
- Los archivos JSON se guardan con codificación UTF-8
- Compatible con facturas en español
- Tiempo de procesamiento depende del tamaño de la imagen

## 🤝 Contribuciones

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
