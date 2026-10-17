total_segundos = int(input("Digite o tempo em segundos: "))

horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")