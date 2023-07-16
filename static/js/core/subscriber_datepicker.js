// Инициализация выбора даты рождения подписчика
$( document ).ready(function() {
  $("#subscriber-date-of-birth").datepicker({
    format: "yyyy-mm-dd", // Формат даты (год-месяц-день)
    language: "ru", // Язык (русский)
  });
});  