import os


def make_chunks(input_file, output_folder):
    # Создаем папку, если она не существует
    os.makedirs(output_folder, exist_ok=True)

    # Читаем содержимое исходного файла
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Разбиваем текст на строки
    lines = text.splitlines()

    chunks = []
    current_chunk = []
    current_length = 0

    # Формируем куски текста с перекрытием
    for line in lines:
        if current_length + len(line) + 1 <= 1500:
            current_chunk.append(line)
            current_length += len(line) + 1
        else:
            chunks.append("\n".join(current_chunk))
            # Перекрытие: берем вторую половину текущего куска
            overlap_start = len(current_chunk) // 2
            current_chunk = current_chunk[overlap_start:]
            current_chunk.append(line)
            current_length = sum(len(l) + 1 for l in current_chunk)

    # Добавляем последний кусок, если он не пустой
    if current_chunk:
        chunks.append("\n".join(current_chunk))

    # Сохраняем куски в отдельные файлы
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(output_folder, f"chunk_{i + 1}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(chunk)

    print(f"Текст успешно разбит на {len(chunks)} частей и сохранен в папке '{output_folder}'.")