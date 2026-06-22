# 🌸 GlowSkin - API de Cuidado Facial

Proyecto de software para el módulo de **Integración Continua** - Politécnico Grancolombiano.

## 📋 Descripción

GlowSkin es una API REST para gestión de productos de belleza y cuidado facial, desarrollada con **Python/Flask** y **MySQL**, desplegada mediante **Docker**.

---

## 🐳 Entrega 1 - Docker (Semana 3)

### Arquitectura de contenedores

```
┌──────────────────────────────────────┐
│          glowskin_network            │
│                                      │
│  ┌─────────────┐  ┌───────────────┐  │
│  │  glowskin_  │  │  glowskin_    │  │
│  │  backend    │◄─►  db           │  │
│  │  (Flask)    │  │  (MySQL 8.0)  │  │
│  │  :5000      │  │  :3306        │  │
│  └─────────────┘  └───────────────┘  │
└──────────────────────────────────────┘
```

### Requisitos

- Docker Desktop instalado
- Docker Compose instalado

### Pasos para ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/glowskin-ci.git
cd glowskin-ci

# 2. Construir y levantar los contenedores
docker-compose up --build

# 3. Verificar que los contenedores estén corriendo
docker ps

# 4. Probar la API
curl http://localhost:5000/
curl http://localhost:5000/productos
```

### Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Info de la API |
| GET | `/salud` | Estado del servicio |
| GET | `/productos` | Lista todos los productos |
| GET | `/productos/{id}` | Obtiene un producto |
| POST | `/productos` | Crea un nuevo producto |

### Ejemplo POST

```json
{
  "nombre": "Tónico Facial",
  "descripcion": "Equilibra el pH de la piel",
  "precio": 32000,
  "categoria": "Tónicos"
}
```

---

## ⚙️ Entrega 2 - Jenkins (Semana 5)

Ver el documento `Entrega2_Jenkins_GlowSkin.docx` en la raíz del proyecto.

---

## 🏗️ Estructura del proyecto

```
glowskin-ci/
├── docker-compose.yml
├── init.sql
├── README.md
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app/
│   │   └── app.py
│   └── tests/
│       └── test_app.py
```
