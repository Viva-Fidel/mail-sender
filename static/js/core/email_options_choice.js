// Обработчик изменения выбранной опции в поле email-option
$(document).ready(function () {
    $("#email-option").change(function () {
      if ($(this).val() === "schedule") {
        $("#schedule-options").show(); // Показать дополнительные опции для планирования
      } else {
        $("#schedule-options").hide(); // Скрыть дополнительные опции для планирования
      }
    });
  });