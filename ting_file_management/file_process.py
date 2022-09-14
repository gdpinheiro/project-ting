import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    current_file = txt_importer(path_file)

    processed_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(current_file),
        "linhas_do_arquivo": current_file,
    }

    instance.enqueue(processed_file)

    print(processed_file, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return

    file_name = instance.dequeue()["nome_do_arquivo"]

    print(f"Arquivo {file_name} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
