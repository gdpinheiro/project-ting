import sys


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file) as f:
                split_file = f.read().split("\n")
                return split_file
        return sys.stderr.write("Formato inválido\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
