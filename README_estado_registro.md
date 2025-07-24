# 📌 Clasificación de Registros – Glosario de `estado_registro`

Este documento explica el significado y uso de la columna `estado_registro` generada tras el merge entre los dos datasets principales:

- `Maestro de Cirugías`: contiene la información clínica de los procedimientos.
- `Maestro de Desmontaje`: contiene los registros de consumo facturable desde el área comercial.

La columna `estado_registro` permite auditar la **completitud, consistencia y trazabilidad** entre el acto médico y su correspondiente consumo o facturación.

---

## 🧾 Glosario de Valores en `estado_registro`

### 🟢 `completo`

- **Qué indica:** El `codigo_cirugia` está presente tanto en Cirugías como en Desmontaje.
- **Significado:** El procedimiento fue cargado y su consumo también.
- **Interpretación:** Caso correcto, sin anomalías.
- **Uso:** Base para análisis operativos, clínicos y comerciales.

---

### 🟡 `solo_cirugia`

- **Qué indica:** El código existe solo en el Maestro de Cirugías.
- **Significado:** La cirugía fue registrada pero no tiene aún consumo asociado.
- **Interpretaciones posibles:**
  - La cirugía fue reciente, el consumo aún no se cargó.
  - Puede haber un error o demora en el desmontaje.
- **Acción recomendada:** Monitorear en el tiempo. No eliminar.

---

### 🟠 `solo_desmontaje`

- **Qué indica:** El código figura solo en el Maestro de Desmontaje.
- **Significado:** Hay productos facturados, pero sin cirugía registrada.
- **Interpretaciones posibles:**
  - Carga adelantada del consumo.
  - Error en la codificación del `codigo_cirugia`.
  - Cirugía aún no importada.
- **Acción recomendada:** Revisión con el área médica y/o comercial.

---

### 🔴 `sin_info`

- **Qué indica:** No hay datos ni en Cirugías ni en Desmontaje para ese código.
- **Significado:** Registro inválido o corrupto.
- **Interpretaciones posibles:**
  - Fila vacía.
  - Fallo en la unión (join) por código.
- **Acción recomendada:** Auditoría inmediata. Puede ser descartable si se confirma error.

---

## 📊 Distribución en el archivo `merged_output.xlsx`

| Valor             | Total     | Estado Operativo |
|------------------|-----------|------------------|
| `completo`        | 10.309    | ✔️ Confirmado     |
| `solo_desmontaje` | 2.972     | ⚠️ Auditar        |
| `solo_cirugia`    | 816       | ⚠️ Auditar        |
| `sin_info`        | 76        | ❌ Revisar        |

---

## 📎 Consideraciones

- No se eliminan registros "incompletos" por diseño: puede existir un **delay natural** entre cirugía y desmontaje.
- Este sistema de clasificación permite trazabilidad y auditoría.
- Ideal para alimentar tableros de control y detectar desvíos o faltantes.
