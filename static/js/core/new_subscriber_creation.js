// Функция для создания нового подписчика
function validateSubscriber() {
   
    $.ajaxSetup({
      headers: { "X-CSRFToken": csrfToken },
    });

    $.ajax({
      url: saveSubscriberURL,
      type: "POST",
      data: {
        first_name: $("#subscriber-first-name").val(),
        last_name: $("#subscriber-last-name").val(),
        date_of_birth: $("#subscriber-date-of-birth").val(),
        email: $("#subscriber-email").val(),
      },
      success: function (response) {
        if (response.success) {
          // Очистка полей формы
          $("#subscriber-first-name").val("");
          $("#subscriber-last-name").val("");
          $("#subscriber-date-of-birth").val("");
          $("#subscriber-email").val("");

          // Отображение, что форма прошла валидацию
          $("#form-errors").addClass("d-none");
          $("#form-success")
            .html(
              '<div class="alert alert-success mt-3"><strong>Подписчик добавлен!</strong></div>'
            )
            .removeClass("d-none");
        } else {
          // Отображение ошибок формы
          let errorsHtml =
            "<strong> Ошибка! Проверьте корректность ввода данных </strong><br>";
          $("#form-success").addClass("d-none");

          const fieldLabels = {
            date_of_birth: "Дата рождения",
            first_name: "Имя",
            last_name: "Фамилия",
            email: "Почта",
          };

          for (let fieldName in response.errors) {
            let fieldLabel = fieldLabels[fieldName] || fieldName;
            errorsHtml +=
              "<strong>" +
              fieldLabel +
              ": </strong>" +
              response.errors[fieldName][0] +
              "<br>";
          }
          $("#form-errors")
            .html(
              '<div class="alert alert-danger mt-3">' +
                errorsHtml +
                "</div>"
            )
            .removeClass("d-none");
        }
      },
    });
  }

  // Привязка обработчика события клика к кнопке "Добавить нового подписчика"
  $(document).on("click", "#submit-subscriber-button", function (event) {
    event.preventDefault();
    console.log(1)
    validateSubscriber();
  });