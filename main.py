#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait
import random

# --- Configuração Inicial ---

# Inicializa o EV3
ev3 = EV3Brick()

# Define os motores
# Caso as rodas não girem como esperado, troque COUNTERCLOCKWISE para CLOCKWISE
motor_esquerdo = Motor(Port.B, Direction.COUNTERCLOCKWISE)  # Port B (LargeMotor)
motor_direito = Motor(Port.C, Direction.COUNTERCLOCKWISE)   # Port C (LargeMotor)
motor_bracos = Motor(Port.A)                                 # Port A (MediumMotor)

# --- FUNÇÕES DE DANÇA ---

def movimento_de_danca(motor_speed, tempo_movimento_ms):
    """
    Executa um passo de dança básico: move as rodas alternadamente para frente e para trás
    para simular as pernas, e mexe os braços.
    """
    # Movimento de braços (curto e rápido)
    motor_bracos.run_angle(speed=450, rotation_angle=60, wait=True)
    motor_bracos.run_angle(speed=450, rotation_angle=-60, wait=True)

    # Movimento de pernas (rodas) alternado para simular caminhada
    motor_esquerdo.run_time(speed=motor_speed, time=200, wait=False)
    motor_direito.run_time(speed=-motor_speed, time=200, wait=False)


def dancar(bpm):
    """
    Loop principal de dança sincronizado com BPM.
    """
    cores_led = [Color.GREEN, Color.RED, Color.YELLOW, Color.WHITE]
    bpm_simulado = bpm if bpm > 0 else 120
    mili_por_batida = round((60000 / bpm_simulado) * 0.65)
    speed_motor = 400

    ev3.speaker.say("Dança, Molina, Dança!")
    ev3.light.on(Color.GREEN)

    print("BPM simulado: {}. Mili por batida: {} ms.".format(bpm_simulado, mili_por_batida))

    while True:
        cor_atual = random.choice(cores_led)
        ev3.light.on(cor_atual)

        tempo_movimento = mili_por_batida // 3

        movimento_de_danca(speed_motor, tempo_movimento)
        wait(mili_por_batida - tempo_movimento)

        ev3.light.on(Color.BLACK)

        movimento_de_danca(-speed_motor, tempo_movimento)
        wait(mili_por_batida - tempo_movimento)

try:
    ev3.speaker.beep(duration=100)
    wait(100)
    ev3.speaker.beep(frequency=587, duration=100)
    wait(100)
    ev3.speaker.beep(frequency=988, duration=250)

    wait(1000)

    wait(2000)
    dancar(100)      # Inicia a dança (BPM = 100)

except Exception as e:
    print("Erro: {}".format(e))

finally:
    ev3.speaker.beep(frequency=988, duration=100)
    wait(100)
    ev3.speaker.beep(duration=100)
    ev3.light.off()
