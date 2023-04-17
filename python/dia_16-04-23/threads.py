import threading

def funcao_thread():
    for i in range(5):
        print("Thread Executando")

thread = threading.Thread(target=funcao_thread)
thread.start()

for i in range(5):
    print("Programa Principal executando :) ")
