// Инициализация выбора даты для рассылки
$(document).ready(function () {
    $("#email-date").datepicker({
      format: "yyyy-mm-dd", // Формат даты (год-месяц-день)
      language: "ru", // Язык (русский)
    });
  });