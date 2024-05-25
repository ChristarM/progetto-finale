import os  # Importa il modulo os per interagire con il sistema operativo
import speech_recognition as sr  # Importa il modulo speech_recognition e lo rinomina come sr per riconoscere la voce
import gtts  # Importa il modulo gtts per convertire il testo in voce
import playsound  # Importa il modulo playsound per riprodurre i file audio
from translate import Translator  # Importa la classe Translator dal modulo translate per tradurre il testo
import random  # Importa il modulo random per selezionare casualmente un consiglio sull'ambiente

codici_lingua = {"italiano": "it", "inglese": "en", "francese": "fr", "spagnolo": "es"}  # Dizionario che mappa i nomi delle lingue ai loro codici

counter = 0  # Contatore globale utilizzato per creare nomi di file univoci

print("Ciao sono lyla, l'assistente vocale sulal sostenibilità :)")

print("Ecco i comandi possibili:\n-Dammi un consiglio\nCome funziona la raccolta differenziata\nQual è la percentuale di CO2 nel mondo?")

consigli_ambiente = [
    "Riduci l'uso di plastica monouso per contribuire a ridurre l'inquinamento ambientale.",
    "Risparmia energia spegnendo le luci quando non sono necessarie e utilizzando elettrodomestici a basso consumo energetico.",
    "Pratica la raccolta differenziata per ridurre i rifiuti e favorire il riciclo.",
    "Utilizza mezzi di trasporto sostenibili come la bicicletta o il trasporto pubblico per ridurre le emissioni di gas serra.",
    "Scegli prodotti ecologici e sostenibili per ridurre l'impatto ambientale dei tuoi acquisti.",
    "Rispetta gli habitat naturali e evita di danneggiare ecosistemi sensibili durante le tue attività all'aperto.",
    "Partecipa a iniziative di volontariato ambientale per contribuire alla conservazione della natura e alla pulizia del territorio.",
    "Educa gli altri sull'importanza della protezione dell'ambiente e sulle azioni che possiamo intraprendere per preservarlo."
]

def scegli_lingue():  # Funzione per scegliere le lingue di input e output
    print("Le lingue disponibili sono:")  # Stampa un messaggio
    for lingua in codici_lingua.keys():  # Itera sui nomi delle lingue nel dizionario codici_lingua
        print(lingua)  # Stampa il nome della lingua

    lingua_input = input("Inserisci la lingua di input: ")  # Chiede all'utente di inserire la lingua di input

    if lingua_input not in codici_lingua:  # Se la lingua di input non è nel dizionario codici_lingua
        print("Lingua non valida. Riprova.")  # Stampa un messaggio di errore
        return scegli_lingue()  # Richiama la funzione scegli_lingue

    lingua_output = input("Inserisci la lingua di output: ")  # Chiede all'utente di inserire la lingua di output

    if lingua_output not in codici_lingua:  # Se la lingua di output non è nel dizionario codici_lingua
        print("Lingua non valida. Riprova.")  # Stampa un messaggio di errore
        return scegli_lingue()  # Richiama la funzione scegli_lingue

    return codici_lingua[lingua_input], codici_lingua[lingua_output]  # Restituisce i codici delle lingue di input e output

def ascolta_e_riconosci(lingua_input):  # Funzione per ascoltare e riconoscere la voce dell'utente
    r = sr.Recognizer()  # Crea un oggetto Recognizer
    mic = sr.Microphone()  # Crea un oggetto Microphone

    print("Sto ascoltando...")  # Stampa un messaggio
    with mic as source:  # Utilizza il microfono come sorgente audio
        r.adjust_for_ambient_noise(source)  # Regola il livello del rumore ambientale
        audio = r.listen(source)  # Ascolta l'audio dal microfono

    print("Sto elaborando...")  # Stampa un messaggio
    try:
        testo = r.recognize_google(audio, language=lingua_input)  # Riconosce l'audio utilizzando il servizio Google Speech Recognition e la lingua specificata
        print("Hai detto:", testo)  # Stampa il testo riconosciuto
        if testo.lower() == "interrompi traduzione":  # Se il testo è "interrompi traduzione"
            return None  # Restituisce None per interrompere il ciclo principale
        elif testo.lower() == "dammi un consiglio":  # Se il testo è "dammi un consiglio"
            consiglio_scelto = random.choice(consigli_ambiente)  # Sceglie casualmente un consiglio sull'ambiente
            print(consiglio_scelto)  # Stampa il consiglio scelto
            return None  # Restituisce None per interrompere il ciclo principale
        elif testo.lower() == "come funziona la raccolta differenziata":  # Se il testo è "come funziona la raccolta differenziata"
            print("La raccolta differenziata è un processo di smistamento e raccolta di rifiuti domestici in modo da permettere il riciclo o il trattamento differenziato. Puoi separare i rifiuti in diverse categorie come carta, plastica, vetro e organico per facilitare il processo di smaltimento corretto.")
            return None  # Restituisce None per interrompere il ciclo principale
        elif testo.lower() == "qual è la percentuale di ci o due nel mondo":  # Se il testo è "qual è la percentuale di CO2 nel mondo?"
            print("La percentuale di CO2 nel mondo varia nel tempo e dipende da molteplici fattori come l'attività industriale, il trasporto, l'agricoltura e altri. È una delle principali cause dell'effetto serra e del riscaldamento globale.")
            return None  # Restituisce None per interrompere il ciclo principale
        return testo  # Restituisce il testo riconosciuto
    except Exception as e:  # Se si verifica un'eccezione (ad esempio, se l'audio non viene riconosciuto)
        print("Non ho capito. Riprova.")  # Stampa un messaggio di errore
        return ascolta_e_riconosci(lingua_input)  # Richiama la funzione ascolta_e_riconosci

def traduci(testo, lingua_input, lingua_output):  # Funzione per tradurre il testo dall'input all'output della lingua
    t = Translator(from_lang=lingua_input, to_lang=lingua_output)  # Crea un oggetto Translator con le lingue specificate
    testo_tradotto = t.translate(testo)  # Traduce il testo utilizzando l'oggetto Translator
    print("Il testo tradotto è:", testo_tradotto)  # Stampa il testo tradotto
    return testo_tradotto  # Restituisce il testo tradotto

def parla(testo, lingua_output):  # Funzione per convertire il testo in voce e riprodurlo
    global counter  # Utilizza la variabile globale counter
    tts = gtts.gTTS(text=testo, lang=lingua_output)  # Crea un oggetto gTTS con il testo e la lingua specificati
    filename = f"audio{counter}.mp3"  # Crea un nome di file univoco utilizzando il contatore
    tts.save(filename)  # Salva l'audio in un file MP3
    print("Sto parlando…")  # Stampa un messaggio
    playsound.playsound(filename)  # Riproduce il file audio
    os.remove(filename)  # Rimuove il file audio
    counter += 1  # Incrementa il contatore

def main():  # Funzione principale
    lingua_input, lingua_output = scegli_lingue()  # Chiama la funzione scegli_lingue per ottenere le lingue di input e output

    while True:  # Ciclo infinito
        testo = ascolta_e_riconosci(lingua_input)  # Chiama la funzione ascolta_e_riconosci per ottenere il testo dall'utente
        if not testo:  # Se il testo è None (cioè se l'utente ha detto "interrompi traduzione")
            break  # Interrompe il ciclo

        testo_tradotto = traduci(testo, lingua_input, lingua_output)  # Chiama la funzione traduci per tradurre il testo

        if not testo_tradotto:  # Se il testo tradotto è None (questo non dovrebbe mai accadere)
            break  # Interrompe il ciclo

        parla(testo_tradotto, lingua_output)  # Chiama la funzione parla per convertire il testo tradotto in voce e riprodurlo
        print(dove_buttare_oggetto(testo_tradotto)) # Chiama la funzione dove_buttare_oggetto per determinare dove buttare l'oggetto

def dove_buttare_oggetto(oggetto):
    oggetti_riciclabili = ["carta", "plastica", "vetro"]
    oggetti_non_riciclabili = ["batterie", "pile", "vernice"]

    if oggetto.lower() in oggetti_riciclabili:
        return "Puoi buttarlo nel contenitore per il riciclo."
    elif oggetto.lower() in oggetti_non_riciclabili:
        return "Non buttarlo nella spazzatura normale, consulta le istruzioni locali per lo smaltimento corretto."
    else:
        return "Non abbiamo informazioni specifiche su dove buttarlo. Consulta le istruzioni locali per lo smaltimento corretto."

if __name__ == "__main__":  # Se questo script viene eseguito come programma principale
    main()  # Chiama la funzione main
