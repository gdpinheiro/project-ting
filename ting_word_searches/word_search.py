def exists_word(word, instance):
    files = []
    occurrences = []

    for i in range(len(instance.data)):
        for index, line in enumerate(instance.search(i)["linhas_do_arquivo"]):
            lower_word = word.lower()
            lower_line = line.lower()
            if lower_word in lower_line:
                occurrences.append({"linha": index + 1})

        if len(occurrences) != 0:
            files.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(i)["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
