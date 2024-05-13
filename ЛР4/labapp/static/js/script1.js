var sendbtn = document.getElementById("submitButton");    // выбираем DOM-елемент (кнопку)

if(sendbtn)
    {
// Привязываем к элементу обработчик события "click"
sendbtn.addEventListener("click", function (e) {
    /* Инструкция preventDefault позволяет переопределить стандартное поведение браузера,
    если ее убрать, то браузер по-умолчанию обновит страницу после отправки данных формы */
    e.preventDefault();
    // Получаем данные полей формы
    let firstname = document.getElementsByName("name")[0].value;
    let first_message = document.getElementsByName("message")[0].value;
    let second_message = document.getElementsByName("message2")[0].value;
    // Преобразуем полученные данные в JSON
    var formdata = JSON.stringify({ firstname: firstname, first_message: first_message, second_message: second_message});
    console.log(firstname);
    // Отправляем запрос через fetch (необходимо выставить соответствующий заголовок (headers)!)
    fetch("/api/contactrequest",
    {
        method: "POST",
        body: formdata,
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then( response => {
        // fetch в случае успешной отправки возвращает Promise, содержащий response объект (ответ на запрос)
        // Возвращаем json-объект из response и получаем данные из поля message
        response.json().then(function(data) {
            console.log(data)
            alert(data.message);
        });
    })
    .catch( error => {
        alert(error);
        console.error('error:', error);
    });

});

// $(document).ready(function(){
//     $('#myForm').submit(function(e){
//         e.preventDefault(); // Предотвращаем отправку формы по умолчанию
//         $.ajax({
//             type: 'POST',
//             url: '/index3/', // Маршрут Flask
//             data: $('#myForm').serialize(), // Сериализуем данные формы
//             success: function(response){
//                 $('#contentPlaceholder').html('<p>Name: ' + response.name + '</p>' +
//                                               '<p>Message: ' + response.message + '</p>' +
//                                               '<p>Another Message: ' + response.message2 + '</p>');
//             },
//             error: function(error){
//                 console.log(error);
//             }
//         });
//     });
// });

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    }
$(document).ready(function() {
    $('#TOGGLEABLE').children('img').toggle();
    $('.projects h2').click(function() {
        $(this).next('.project-grid').children('img').toggle('slow');
        $(this).toggleClass('active');
    });
});

$(document).ready(function() {
    // При наведении курсора на изображение
    $('img').hover(function() {
        // Изменяем размер изображения
        $(this).css('transform', 'scale(1.2)');
        // Изменяем рамку изображения
        $(this).css('border', '2px solid blue');
        // Изменяем прозрачность изображения
        $(this).css('opacity', '0.7');
    }, function() {
        // При выходе курсора с изображения возвращаем стили по умолчанию
        $(this).css('transform', 'scale(1)');
        $(this).css('border', 'none');
        $(this).css('opacity', '1');
    });
});

$(document).ready(function() {
    // Добавляем индексы к строкам таблицы
    $('table tr').each(function(index) {
        if (index !== 0) {
            $(this).prepend('<td>' + index + '</td>');
        } else {
            $(this).prepend('<th>Index</th>');
        }
    });

    // Добавляем обработчик события для сортировки строк при нажатии на заголовок индексной колонки
    $('tr').click(function() {
        var table = $(this).parents('table').eq(0);
        var rows = table.find('tr:gt(0)').toArray().sort(function(a, b) {
            var aValue = parseInt($(a).find('td:first').text());
            var bValue = parseInt($(b).find('td:first').text());
            return aValue - bValue;
        });
        this.asc = !this.asc;
        if (!this.asc) {
            rows = rows.reverse();
        }
        for (var i = 0; i < rows.length; i++) {
            table.append(rows[i]);
        }
    });
});
