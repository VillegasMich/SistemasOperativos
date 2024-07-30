# Preguntas

## RR

1. **¿Cómo afecta el quantum de tiempo al rendimiento del planificador Round
   Robin?**

- Entre menor sea el _quantum_ de tiempo del procesasdor menor va a ser el tiempo que tiene cada proceso de permanecer en la CPU,
  eso quiere decir que los procesos se van a demorar mas tiempo total en completarse ya que se van rotando
  con el resto de procesos, mientras que un quantum mas grande generaria que los procesos mas
  grandes monopolicen a los mas pequeños.

2. **¿ Qué sucede si el tiempo de ráfaga (burst time) de un proceso es menor
   que el quantum de tiempo?**

- Cuando el _burst_ time es menor que el _quantum_ time el proceso se completa dentro de ese tiempo y como sobra tiempo del quantum
  el siguiente proceso aproveha y empieza directamente cuando se acaba el anterior.

## FCFS

1. **¿Cómo afecta la planificación FCFS al tiempo de espera promedio si un
   proceso corto llega después de un proceso largo?**

- Afecta de manera negativa, ya que el proceso corto se va a ver en la obligacion de esperar que el largo termine
  sin importar cuanto se demore generando un _convoy effect_ y un mayor tiempo de espera y tiepo total de ejecucion
  de la totalidad de los procesos.

2. **¿Cuál es la principal desventaja de la planificación FCFS?**

- La principal desventaja de este planificador es que depende de la hora de llegada de los procesos y de su tamaño
  lo que quiere decir que puede salir distinto de muchas formas, cuando llega primero el proceso largo se genera un convoy
  pero si llega uno corto primero pareceria funcionar de la mejor manera. Finalmente significa que al depender tanto puede salir bien
  o mal sin encontrar una consistencia.

## Prioridad

1. **¿Cómo se produce la inversión de prioridades en un sistema de
   programación de prioridades?**

- La inversion de prioridades se da cuando dos tareas de distintas prioridades comparten un recurso
  y la tarea de **menor prioridad** bloquea a la de **mayor prioridad**, teniendo esta ultima que esperar
  a que la menor termine. Esta situacion hace que el proceso de mayor prioridad pueda
  no cumplir sus requisitos ni tiempos propuestos puediendo generar errores graves.

2. **¿Cuál podría ser una solución al problema de inversión de prioridad?**

- Una de las soluciones puede ser la **herencia de prioridades**, donde la el proceso que esta reteniendo el recurso
  (el proceso de menor prioridad) aumenta su prioridad con respecto a todos los procesos del SO para que pueda soltar el
  recurso de manera mas rapida. Otra solucion es el **limite de prioridades**, se instaura una prioridad fija a
  cada recurso que los procesos utilizan, cuando un proceso llega al recurso su prioridad aumenta a dicho limite y cuando
  suelta el recurso su prioridad regresa a la normal establecida.

  ## Conclusiones

- Primero observamos que el algoritmo de round-robin maneja mejore _response time_ a costa de _turnaround time_ por la intermitencia de
  la ejecucion de los procesos, y algoritmos como el fcfs demuestra valores contrarios en _response time_ pero similar a RR en _turnaround time_
  y con el manejo de prioridades se ve un balance en ambos casos. Claro que estos comportamientos se ven afectados por las caracteristicas de los procesos
  un proceso muy largo y con alta prioridad va a generar un _convoy effect_ en casos como fcfs y por prioridad (siempre y cuando sea el unico con la prioridad mas alta)
  mientras que en RR esto no pasa porque trata a todos por igual con un comportamiento _justo_ para todos los procesos pero demorando a los procesos mas cortos de manera
  inecesaria.

  Podemos decir que ningun algoritmo (de los manejados en este ejercicio) es perfecto, todos tienen beneficios y comportamientos negativos de acuerdo con ciertas situaciones,
  entonces el mejor planeador de procesos es aquel que esta preparado para todas las situaciones que se le pueda presentar, minimizando los riesgos de efectos adversos que se puedan generar.
