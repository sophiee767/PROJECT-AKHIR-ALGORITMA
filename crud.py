tasks = []

def tambah_tugas(task):
    tasks.append(task)

def baca_tugas():
    return tasks

def hapus_tugas(index):

    if 0 <= index < len(tasks):
        return tasks.pop(index)

    return None
