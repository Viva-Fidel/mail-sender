// Получение элементов HTML-ввода и элемента предварительного просмотра
const htmlInput = document.getElementById("html-input"); // HTML-элемент ввода
const previewPane = document.getElementById("preview-pane"); // Элемент предварительного просмотра

// Обновление элемента предварительного просмотра с введенным HTML-кодом
htmlInput.addEventListener("input", function () {
  previewPane.innerHTML = htmlInput.value;
});