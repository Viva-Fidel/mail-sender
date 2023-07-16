// Функция для получения результатов рассылок
function getResults() {
    $.ajax({
      url: getResultURL,
      type: "GET",
      dataType: "json",
      success: function (response) {
        $(".list-group").empty(); // Очистка существующего содержимого
        $.each(response, function (index, result) {
          const listItem = $(
            '<div class="list-group-item list-group-item-action"></div>'
          );
          const header = $(
            '<div class="d-flex w-100 justify-content-between"></div>'
          );
          const title = $('<h5 class="mb-1">Дата рассылки:</h5>'); // Заголовок "Рассылка от:"
          const date = $(
            '<small class="text-body-secondary">' +
              result.date_of_mailing +
              "</small>"
          ); // Дата рассылки
          const sentEmails = $(
            '<p class="mb-1">Писем отправлено: ' +
              result.sent_emails +
              "</p>"
          ); // Количество отправленных писем
          const openedEmails = $(
            '<p class="mb-1">Из них открыто: ' +
              result.opened_emails +
              "</p>"
          ); // Количество открытых писем
          header.append(title).append(date);
          listItem.append(header).append(sentEmails).append(openedEmails);
          $(".list-group").append(listItem);
        });
      },
      error: function (xhr, status, error) {
        console.error(xhr.responseText);
      },
    });
  }

  // Привязка обработчика события клика к кнопке "Проверить эффективность"
  $(document).on("click", "#get-results", function (event) {
    event.preventDefault();
    getResults();
  });