# 🐘 tkla_postgres_client

**Librería ligera y poderosa para trabajar con PostgreSQL usando SQL puro, sin complicaciones y sin ORM.**

Ideal para proyectos rápidos, microservicios, APIs y sistemas donde prefieres control total sobre tus consultas SQL.

---

## 🚀 Características

- 🔌 Conexión automática usando `DATABASE_URL`
- 🛠️ Creación de tablas desde un `dict` estilo schema JSON
- 🔄 Soporte completo a operaciones CRUD: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- 🧠 Métodos utilitarios: `exists()`, `count()`
- 🧾 Retorno estandarizado en todos los métodos (`dict` con `success`, `data`, `message`)
- 🧱 Seguridad por defecto: no se permiten `UPDATE` o `DELETE` sin condiciones
- 🚫 Sin dependencias de ORM (como SQLAlchemy)
- 📋 Logging centralizado, sin interrupciones por errores
- 🔁 Compatible con frameworks como **Flask**, **FastAPI**, etc.

## ✅ Tipos de datos admitidos en schem

| `data_type`          | Equivalente PostgreSQL | Observaciones                           |
| -------------------- | ---------------------- | --------------------------------------- |
| `"text"`             | `TEXT`                 | Para cadenas de longitud variable       |
| `"varchar"`          | `VARCHAR(n)`           | Usa junto con `"length": 100`           |
| `"integer"`          | `INTEGER`              | Para enteros                            |
| `"serial"`           | `SERIAL`               | Auto-incremental (clave primaria común) |
| `"boolean"`          | `BOOLEAN`              | Verdadero/Falso                         |
| `"timestamp"`        | `TIMESTAMP`            | Fechas y horas                          |
| `"date"`             | `DATE`                 | Solo fecha                              |
| `"jsonb"`            | `JSONB`                | Estructuras JSON                        |
| `"float"` / `"real"` | `REAL`                 | Números decimales                       |
| `"numeric"`          | `NUMERIC`              | Para precisión exacta (moneda, etc.)    |


## 📦 Otros parámetros opcionales en el schema

| Clave         | Descripción                                    |
| ------------- | ---------------------------------------------- |
| `primary_key` | `True` → lo marca como `PRIMARY KEY`           |
| `unique`      | `True` → añade `UNIQUE`                        |
| `nullable`    | `False` → añade `NOT NULL`                     |
| `default`     | Valor por defecto (`DEFAULT valor`)            |
| `length`      | Solo para `varchar`, define la longitud máxima |
| `comment`     | No usado aún, puedes extenderlo                |
| `foreign_key` | Dict: `{"reference": "otra_tabla(campo)"}`     |

## 📌 Ejemplo simple
```python
schema = {
    "usuarios": {
        "id": {
            "data_type": "serial",
            "primary_key": True
        },
        "email": {
            "data_type": "varchar",
            "length": 100,
            "unique": True,
            "nullable": False
        },
        "perfil": {
            "data_type": "jsonb",
            "nullable": True
        }
    }
}

```
---

## 📦 Instalación

Instalación desde PyPI:

```bash
pip install tkla_postgres_client
```

O desde el código fuente:

```bash
git clone https://github.com/LOVENXON/tkla_postgres_client.git
cd tkla_postgres_client
pip install -e .
```

---

## ⚙️ Uso Básico

### 1️⃣ Conexión

```python
from tkla_postgres_client.core import PostgresClient

db = PostgresClient("postgresql://user:pass@host:port/dbname")
```

### 2️⃣ Crear Tablas

```python
from tkla_postgres_client.builder import create_tables

schema = {
    "users": {
        "id": {"data_type": "serial", "primary_key": True},
        "name": {"data_type": "varchar", "length": 100, "nullable": False},
        "email": {"data_type": "varchar", "length": 100, "unique": True}
    }
}

create_tables(schema, db)
```

### 3️⃣ Operaciones CRUD

#### ➕ Insertar

```python
db.insert_data({
    "users": {"name": "Ana", "email": "ana@example.com"}
})
```

#### 🔍 Consultar

```python
db.select_data({
    "users": {
        "conditions": {"email": "ana@example.com"},
        "columns": ["id", "name"],
        "order_by": ["created_at DESC"],
        "limit": 1
    }
})
```

#### 📝 Actualizar

```python
db.update_data({
    "users": {
        "values": {"name": "Ana Actualizada"},
        "conditions": {"email": "ana@example.com"}
    }
})
```

#### ❌ Eliminar

```python
db.delete_data({
    "users": {"conditions": {"email": "ana@example.com"}}
})
```

---

## 🔍 Métodos Útiles

### ¿Existe un registro?

```python
db.exists({
    "users": {"conditions": {"email": "ana@example.com"}}
})  # True / False
```

### ¿Cuántos registros hay?

```python
db.count({
    "users": {"conditions": {"active": True}}
})  # int
```

---

## 🧹 Buenas Prácticas

✅ Usa una sola conexión por request (por ejemplo, con `Flask.g`)  
✅ Siempre cierra la conexión con `db.close()` al final del ciclo  
✅ Valida campos requeridos antes de realizar inserciones o actualizaciones  

---

## 📄 Licencia

**MIT** – Libre para uso personal y comercial.

---

## ✨ Autor

**Lovenson Pierre**  
📧 [lovesonpierre25@gmail.com](mailto:lovesonpierre25@gmail.com)  
🐙 GitHub: [LOVENXON](https://github.com/LOVENXON)