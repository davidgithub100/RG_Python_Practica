# Diario de errores

## Error #1: ValueError con int()
- **Fecha:** 02/11/2026
- **Qué hice:** escribí "veinte" cuando el programa pedía la edad
- **Error:** ValueError: invalid literal for int() with base 10: 'veinte'
- **Por qué pasó:** int() solo convierte textos que contengan dígitos
- **Cómo se arregla:** validar la entrada antes de convertir (try/except, lo veremos pronto)
- **Lección:** nunca confiar en lo que escribe el usuario

## Error #2: fatal: not a git repository
- **Fecha:** 02/11/2026
- **Qué hice:** ejecuté git status en la carpeta equivocada
- **Error:** fatal: not a git repository (or any of the parent directories): .git
- **Por qué pasó:** Git solo funciona dentro de una carpeta con repositorio (.git)
- **Cómo se arregla:** cd a la carpeta del proyecto, o git init si no es repo
- **Lección:** verificar dónde estoy con pwd y que el prompt muestre (main)

## Error #3: borré la carpeta .git
- **Fecha:** 02/11/2026
- **Qué hice:** eliminé .git para "empezar limpio"
- **Error:** git status dio fatal: not a git repository
- **Por qué pasó:** .git ES el repositorio (historial)
- **Cómo se arregla:** git init -b main y repetir add/commit/push
- **Lección:** no tocar .git salvo que quiera reiniciar a propósito

## Error #4: push colgado + historias distintas
- **Fecha:** 02/11/2026
- **Qué hice:** creé el repo en GitHub con README y no completé el login del push
- **Por qué pasó:** el README creó un commit remoto que mi repo local no tenía
- **Cómo se arregla:** git pull origin main --allow-unrelated-histories, luego git push
- **Lección:** el pull abre un editor: guardar y cerrar. El login se completa en el navegador

## Error #5: bash: it: command not found
- **Fecha:** 03/11/2026
- **Qué hice:** escribí `it status` en vez de `git status`
- **Error:** bash: it: command not found
- **Por qué pasó:** typo; bash buscó un programa llamado "it" y no existe
- **Cómo se arregla:** revisar la ortografía del comando y volver a escribirlo
- **Lección:** `command not found` casi siempre es un error de escritura

## Error #6: abrí la carpeta equivocada con code ..
- **Fecha:** 03/11/2026
- **Qué hice:** estando en PythonPractica ejecuté `code ..` en vez de `code .`
- **Error:** VS Code abrió DESARROLLO (la carpeta de arriba), no mi proyecto
- **Por qué pasó:** `.` es la carpeta actual y `..` es la carpeta padre
- **Cómo se arregla:** cerrar esa ventana y ejecutar `code .`
- **Lección:** revisar que el explorador de VS Code diga PYTHONPRACTICA antes de empezar; si abro la carpeta equivocada, git status daría fatal

---

# Conceptos aprendidos

## Concepto: TypeError vs ValueError
- **TypeError:** tipo de dato equivocado para la operación (ej. `"5" + 3`)
- **ValueError:** tipo correcto pero valor inválido (ej. `int("hola")`)
- **Regla de 2 preguntas:** 1) ¿este tipo puede entrar a esta operación? Si no, TypeError. 2) Si puede, ¿este valor sirve? Si no, ValueError
- **Analogía:** máquina que acepta monedas. Una llave es TypeError; una moneda de otro país es ValueError

## Concepto: int() devuelve una copia, no modifica la variable
- **Lo que creía:** que int() transformaba la variable original
- **Lo correcto:** devuelve un valor nuevo; la variable original sigue igual
- **Ejemplo:** `edad = "24"` y `nueva = int(edad)`: edad sigue siendo texto, nueva es entero
- **Analogía:** una fotocopiadora; el original no cambia

## Concepto: int() con float y con texto
- `int(24.5)` da `24` (corta los decimales, no redondea)
- `int(-2.7)` da `-2` (corta hacia el cero)
- `int("24.5")` da ValueError (el texto debe verse como entero)
- Para convertir `"24.5"` a entero: `int(float("24.5"))` da `24`
- **Mi error de predicción:** dije TypeError para `int(24.5)`, pero int() sí acepta floats