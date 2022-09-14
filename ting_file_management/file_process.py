import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return

    current_file = txt_importer(path_file)

    processed_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(current_file),
        "linhas_do_arquivo": current_file,
    }

    print(processed_file, file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos")

    file_name = instance.dequeue()["nome_do_arquivo"]

    print(f"Arquivo {file_name} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
