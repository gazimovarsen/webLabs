var express = require('express');
var router = express.Router();

var mainController = require('../controllers/mainController');  // подключение контроллера

/* Обработка перехода по адресу /contact и
рендеринг соответствующего шаблона */
router.get('/', function(req, res, next) {
  res.render('contact', { 
    title: 'Whitesquare',
    pname: 'CONTACT',
    navmenu: mainController.navmenu });
});

// Обработка POST-запроса (принимаем данные, отправленные c помощью AJAX со страницы /contact)
router.post("/ajaxrequest", function (req, res) {
  console.log(req.body);  // выводим в консоль полученные данные
  if (!req.body) return response.sendStatus(400);
  // Читаем поле firstname из полученного json
  try {
    var msg = req.body.firstname + ", ваш запрос получен !";
  } catch(err) {
    console.error(err)
  }

  res.json({ message: msg }); // отправляем ответ
});

module.exports = router;