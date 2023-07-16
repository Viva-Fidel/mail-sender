// Функция для создания рассылки
function sendEmail() {

    $.ajaxSetup({
      headers: { "X-CSRFToken": csrfToken },
    });

    // AJAX-запрос для отправки данных на сервер
    $.ajax({
      url: sendEmailURL,
      type: "POST",
      data: {
        email_title: $("#email-title").val(),
        html_data: $("#preview-pane").html(),
        email_time: $("#email-time").val(),
        email_date: $("#email-date").val(),
      },
      success: function (response) {
        if (response.success) {
          // Очистка полей формы
          $("#email-title").val("");
          $("#preview-pane").html("");
          $("#email-time").val("");
          $("#email-date").val("");

          // Сброс ошибок формы
          $("#email-errors").addClass("d-none");
          $("#email-success")
            .html(
              '<div class="alert alert-success mt-3"><strong>Рассылка создана!</strong></div>'
            )
            .removeClass("d-none");
        } else {
          // Скрытие успешного сообщения
          $("#email-success").addClass("d-none");

          // Отображение сообщения об ошибке
          $("#email-errors")
            .html(
              '<div class="alert alert-danger mt-3"><strong>Ошибка создания рассылки!</strong></div>'
            )
            .removeClass("d-none");
        }
      },
    });
  }

  // Привязка обработчика события клика к кнопке "Организовать рассылку"
  $(document).on("click", "#submit-email-button", function (event) {
    event.preventDefault();
    sendEmail();
  });