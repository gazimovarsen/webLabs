/*
В модулях-контроллерах реализуются методы (бизнес-логика) для работы с объектами БД.
Если в вашем приложении используется несколько сущностей (таблиц) в БД, то хорошей практикой 
будет являться реализация ОТДЕЛЬНЫХ модулей с CRUD-операциями для каждой таблицы.
*/
const { dbcontext } = require('../sequelize');     // подключаем объект модели БД из модуля инициализации sequelize.js

exports.navmenu = [
    {
        name: 'HOME',
        addr: '/'
    },
    {
        name: 'ABOUT US',
        addr: '#'
    },
    {
        name: 'SERVICES',
        addr: '#'
    },
    {
        name: 'PROJECTS',
        addr: '#'
    },
    {
        name: 'MEMBERS',
        addr: '#'
    },
    {
        name: 'CONTACT',
        addr: '/contact'
    }
];


// Показать список всех запросов.
exports.get_contact_req_all = function(req, res) {
    dbcontext.query(
        'SELECT * FROM contactrequests', { type: dbcontext.QueryTypes.SELECT }
    )
    .then(data => {
      res.json(data[0]);
    })
    .catch(err => {
      res.status(500).send({
        message: err.message || "Some error occurred on the server."
      });
    });
};
  
// Показать запрос по id (primary key).
exports.get_contact_req_by_id = function(req, res) {
    dbcontext.query(
        'SELECT * FROM contactrequests WHERE id = :id',
        {
            replacements: { id: req.params.id },
            type: dbcontext.QueryTypes.SELECT
        }
    )
    .then(data => {
      res.json(data[0]);
    })
    .catch(err => {
      res.status(500).json({ message: err.message });
    });
};
  
// Показать запрос по имени автора.
exports.get_contact_req_by_firstname = function(req, res) {
    dbcontext.query(
        'SELECT * FROM contactrequests WHERE "firstname" = :firstname',
        {
            replacements: { firstname: req.params.firstname },
            type: dbcontext.QueryTypes.SELECT
        }
    )
    .then(data => {
      res.json(data[0]);
    })
    .catch(err => {
        res.status(500).json({ message: err.message });
    });
};
  
// Создать новый запрос.
exports.create_contact_req = function(req, res) {
    // Проверяем полученные данные на наличие обязательных полей (firstname и reqtext)
    if (!req.body.firstname || !req.body.reqtext) {
            res.status(400).json({ message: "Data validation error!" });    // если данные не найдены, возвращаем HTTP-код 400
        return;
    }
    // Записываем объект в БД
    var curDateTime = new Date(Date.now());
    dbcontext.query(
        'INSERT INTO contactrequests (`firstname`,`lastname`, `email`, `reqtype`,`reqtext`,`createdAt`,`updatedAt`) VALUES (:firstname, :lastname, :email, :reqtype, :reqtext, :createdAt, :updatedAt)',
        {
            replacements: { firstname: req.body.firstname, lastname: req.body.lastname, email: req.body.email, 
                reqtype: req.body.reqtype, reqtext: req.body.reqtext, createdAt: curDateTime.toISOString(), updatedAt: curDateTime.toISOString() },
            type: dbcontext.QueryTypes.INSERT
        }
    )
    .then(data => {
        res.json({ message: "ContactRequest Created!" });
      })
      .catch(err => {
          res.status(500).json({ message: err.message });
    });
};
  
// Удалить запрос по id из таблицы
exports.delete_contact_req_by_id = function(req, res) {
    dbcontext.query(
        'DELETE FROM contactrequests WHERE id = :id',
        {
            replacements: { id: req.params.id },
            type: dbcontext.QueryTypes.DELETE
        }
    )
    .then(data => {
      res.json({ message: "ContactRequest Deleted!" });
    })
    .catch(err => {
        res.status(500).json({ message: err.message });
    });
};
  
// Обновить текст запроса по id в таблице
exports.update_contact_req_by_id = function(req, res) {
    // Проверяем полученные данные на наличие обязательного поля reqtext
    if (!req.body.reqtext) {
        res.status(400).json({ message: "Data validation error!" });
    return;
    }
    var curDateTime = new Date(Date.now());
    // Обновляем запись в БД
    dbcontext.query(
        'UPDATE contactrequests SET reqtext = :reqtext, updatedAt = :updatedAt WHERE id = :id',
        {
            replacements: { id: req.params.id, reqtext: req.body.reqtext, updatedAt: curDateTime.toISOString() },
            type: dbcontext.QueryTypes.UPDATE
        }
    )
    .then(data => {
      res.json({ message: "ContactRequest Updated!" });
    })
    .catch(err => {
        res.status(500).json({ message: err.message });
    });
};