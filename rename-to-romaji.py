import os
import re
import fugashi ### INSTALL pip3 install fugashi
import pykakasi ### INSTALL pip3 install pykakasi

### INSTALL KANJI DICTONARY: pip3 install unidic-lite unidic
#### DOWNLOAD DICTONARY: python -m unidic download

# Criar o analisador de texto com Fugashi
tagger = fugashi.Tagger()
kakasi = pykakasi.kakasi()
kakasi.setMode("H", "a")  # Hiragana -> ASCII
kakasi.setMode("K", "a")  # Katakana -> ASCII
kakasi.setMode("J", "a")  # Kanji -> ASCII
conv = kakasi.getConverter()

# Lista de caracteres inválidos no Windows (exceto o ponto)
INVALID_CHARS = r'[<>:"/\\|?*]'

def sanitize_filename(name):
    """Remove caracteres inválidos do nome, mantendo intactos os pontos usados na extensão."""
    return re.sub(INVALID_CHARS, "_", name)

def convert_to_romaji(text):
    """Converte o texto em romaji utilizando Fugashi e pykakasi."""
    romaji_list = []
    for word in tagger.parseToNodeList(text):
        if word.surface:
            # Usa a pronúncia se disponível; caso contrário, usa a superfície original
            reading = word.feature.pron if word.feature.pron else word.surface
            romaji_word = conv.do(reading)
            romaji_list.append(romaji_word)
    return "".join(romaji_list)

# Definir a pasta de animes
anime_folder = r"C:\Your\Folder"

# Processar os arquivos na pasta
for filename in os.listdir(anime_folder):
    # Separa o nome base da extensão
    base, ext = os.path.splitext(filename)
    # Converte apenas o nome base para romaji
    new_base = convert_to_romaji(base)
    # Remove caracteres inválidos do nome base
    new_base = sanitize_filename(new_base)
    # Recria o nome completo com a extensão original
    new_name = new_base + ext
    
    # Renomeia apenas se houver mudança
    if new_name and filename != new_name:
        old_path = os.path.join(anime_folder, filename)
        new_path = os.path.join(anime_folder, new_name)
        try:
            os.rename(old_path, new_path)
            print(f"Renomeado: {filename} -> {new_name}")
        except Exception as e:
            print(f"Erro ao renomear {filename}: {e}")
