from crud import tasks

def cari_tugas(keyword):

    hasil = []

    for task in tasks:

        if keyword.lower() in task["nama"].lower():
            hasil.append(task)

    return hasil



priority_order = {
    "Hard": 3,
    "Medium": 2,
    "Easy": 1
}


def bubble_sort():

    n = len(tasks)

    for i in range(n):

        for j in range(0, n - i - 1):

            if priority_order[tasks[j]["prioritas"]] < priority_order[tasks[j + 1]["prioritas"]]:

                tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
