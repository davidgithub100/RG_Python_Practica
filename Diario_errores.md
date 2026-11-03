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